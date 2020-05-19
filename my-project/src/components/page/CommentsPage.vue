<template>
  <div class="wrapper">
    <el-main class="col2">
      <div class="comment">
        <el-select v-model="value" placeholder="时间" size="mini" style="padding-top: 10px;float:right;">
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          >
          </el-option>
        </el-select>
        <div v-clickoutside="hideReplyBtn" @click="inputFocus" class="my-reply">
          <el-avatar class="header-img" :size="40" :src="myImage"></el-avatar>
          <div class="reply-info">
            <div
              tabindex="0"
              contenteditable="true"
              id="replyInput"
              spellcheck="false"
              placeholder="输入评论..."
              class="reply-input"
              @focus="showReplyBtn"
              @input="onDivInput($event)"
            ></div>
          </div>
          <div class="reply-btn-box" v-show="btnShow">
            <el-button class="reply-btn" size="medium" @click="sendComment" type="primary">发表评论</el-button>
          </div>
        </div>
        <div v-for="(item, i) in comments" :key="i" class="author-title reply-father">
          <el-avatar class="header-img" :size="40" :src="item.avatar"></el-avatar>
          <div class="author-info">
            <span class="author-name">{{ item.userName }}</span>
            <span class="author-time">{{ item.pubTime }}</span>
          </div>
          <div class="icon-btn">
            <span @click="showReplyInput(i, item.userName, item.id)"
              ><i class="iconfont el-icon-s-comment"></i>{{ item.replyNum }}</span
            >
            <span class="like" @click="likeClick(i, item)">
              <i v-if = "item.currentUserLike == '0'" class="iconfont el-icon-star-on"></i>
              <i v-else class="iconfont el-icon-star-off"></i>
              {{ item.likeNum }}
            </span>
            <span class="dislike" @click="dislikeClick(i, item)">
              <i v-if = "item.currentUserLike == '1'" class="iconfont el-icon-error"></i>
              <i v-else class="iconfont el-icon-close"></i>
              {{ item.dislikeNum }}
            </span>
          </div>
          <div class="talk-box">
            <p>
              <span class="reply">{{ item.contentView }}</span>
            </p>
          </div>
          <div class="reply-box">
            <div v-for="(reply, j) in item.replyList" :key="j" class="author-title">
              <el-avatar class="header-img" :size="40" :src="reply.avatar"></el-avatar>
              <div class="author-info">
                <span class="author-name">{{ reply.userName }}</span>
                <span class="author-time">{{ reply.pubTime }}</span>
              </div>
              <div class="icon-btn">
                <span class="like" @click="likeClickreply(i, j, reply)">
                  <i v-if = "reply.currentUserLike == '0'" class="iconfont el-icon-star-on"></i>
                  <i v-else class="iconfont el-icon-star-off"></i>
                  {{ reply.likeNum }}
                </span>
                <span class="dislike" @click="dislikeClickreply(i, j, reply)">
                  <i v-if = "reply.currentUserLike == '1'" class="iconfont el-icon-error"></i>
                  <i v-else class="iconfont el-icon-close"></i>
                  {{ reply.dislikeNum }}
                </span>
              </div>
              <div class="talk-box">
                <p>
                  <span>回复 {{ reply.replyCommentUserName }}:</span>
                  <span class="reply">{{ reply.contentView }}</span>
                </p>
              </div>
              <div class="reply-box"></div>
            </div>
          </div>
          <div v-show="_inputShow(i)" class="my-reply my-comment-reply">
            <el-avatar class="header-img" :size="40" :src="myImage"></el-avatar>
            <div class="reply-info">
              <div
                tabindex="0"
                contenteditable="true"
                spellcheck="false"
                placeholder="输入评论..."
                @input="onDivInput($event)"
                class="reply-input reply-comment-input"
              ></div>
            </div>
            <div class=" reply-btn-box">
              <el-button class="reply-btn" size="medium" @click="sendCommentReply(i, j)" type="primary"
                >发表评论</el-button
              >
            </div>
          </div>
        </div>
      </div>
    </el-main>
  </div>
</template>

<script>
const clickoutside = {
  // 初始化指令
  bind(el, binding, vnode) {
    function documentHandler(e) {
      // 这里判断点击的元素是否是本身，是本身，则返回
      if (el.contains(e.target)) {
        return false
      }
      // 判断指令中是否绑定了函数
      if (binding.expression) {
        // 如果绑定了函数 则调用那个函数，此处binding.value就是handleClose方法
        binding.value(e)
      }
    }
    // 给当前元素绑定个私有变量，方便在unbind中可以解除事件监听
    el.vueClickOutside = documentHandler
    document.addEventListener('click', documentHandler)
  },
  update() {},
  unbind(el, binding) {
    // 解除事件监听
    document.removeEventListener('click', el.vueClickOutside)
    delete el.vueClickOutside
  },
}
export default {
  data() {
    return {
      options: [
        {
          value: 'time',
          label: '时间',
        },
        {
          value: 'hot',
          label: '热度',
        },
      ],
      value: 'time',
      paperID: '',
      btnShow: false,
      index: '0',
      replyComment: '',
      myName: localStorage.getItem("ms_username"),
      myImage: 'https://ae01.alicdn.com/kf/Hd60a3f7c06fd47ae85624badd32ce54dv.jpg',
      myID: 19870621,
      to: '',
      comments: null,
    }
  },
  directives: { clickoutside },
  created() {
    this.paperID = this.$route.params.id;
    console.log(this.$route.params.id);
    this.initpage();
  },
  watch : {
    value(value, oldvalue) {
      this.value = value;
      this.initpage();
    }
  },
  methods: {
    initpage() {
      let _this = this
      this.$http
      .request({
        url: _this.$url + '/getPaperComment?paperID=' + this.paperID + '&userID='+this.myID+'&sortedBy=' + this.value,
        method: 'get',
      })
      .then(function(response) {
        _this.comments = response.data.comments
        for(var i=0;i<_this.comments.length;i++) {
          _this.$set(_this.comments[i], 'inputShow', false)
        }
        console.log(_this.comments)
      })
      .catch(function(response) {
        console.log(response)
      })
      this.$http
      .request({
        url: _this.$url + '/getHeadImg?userName=' + this.myName,
        method: 'get',
      })
      .then(function(response) {
        _this.myImage = response.data.avatar_url;
        console.log(response)
      })
      .catch(function(response) {
        console.log(response)
      })
    },
    inputFocus() {
      var replyInput = document.getElementById('replyInput')
      replyInput.style.padding = '8px 8px'
      replyInput.style.border = '2px solid blue'
      replyInput.focus()
      for(var i=0;i<this.comments.length;i++) {
        this.comments[i].inputShow = false
      }
    },
    showReplyBtn() {
      this.btnShow = true
    },
    hideReplyBtn() {
      this.btnShow = false
      replyInput.style.padding = '10px'
      replyInput.style.border = 'none'
    },
    showReplyInput(i, name, id) {
      this.comments[this.index].inputShow = false
      this.index = i
      this.comments[i].inputShow = true
      this.replyCommentUserName = name
      this.replyCommentID = id
    },
    _inputShow(i) {
      return this.comments[i].inputShow
    },
    likeClick(i, item) {
      if (item.currentUserLike === '2') {
        item.currentUserLike = '0'
        item.likeNum++
        var post_request = new FormData()
        post_request.append('paperID', this.paperID)
        post_request.append('userID', this.myID)
        post_request.append('commentID', this.comments[i].id)
        post_request.append('isLike', '1')
        post_request.append('sortedBy', this.value)
        this.$http
          .request({
            url: this.$url + '/postLike',
            method: 'post',
            data: post_request,
            headers: { 'Content-Type': 'multipart/form-data' },
          })
          .then(function(response) {
            console.log(response)
          })
          .catch(function(response) {
            console.log(response)
          })
      } else if(item.currentUserLike === '0'){
          item.currentUserLike = '2'
          item.likeNum--
          var post_request = new FormData()
          post_request.append('paperID', this.paperID)
          post_request.append('userID', this.myID)
          post_request.append('commentID', this.comments[i].id)
          post_request.append('isLike', '1')
          post_request.append('sortedBy', this.value)
          this.$http
            .request({
             url: this.$url + '/cancelLike',
              method: 'post',
              data: post_request,
              headers: { 'Content-Type': 'multipart/form-data' },
            })
            .then(function(response) {
              console.log(response)
            })
            .catch(function(response) {
              console.log(response)
            })
        } 
        item.isLike = !item.isLike;
    },
    dislikeClick(i, item) {
      if (item.currentUserLike === '2') {
        item.currentUserLike = '1'
        item.dislikeNum++
        var post_request = new FormData()
        post_request.append('paperID', this.paperID)
        post_request.append('userID', this.myID)
        post_request.append('commentID', this.comments[i].id)
        post_request.append('isLike', '0')
        post_request.append('sortedBy', this.value)
        this.$http
          .request({
            url: this.$url + '/postLike',
            method: 'post',
            data: post_request,
            headers: { 'Content-Type': 'multipart/form-data' },
          })
          .then(function(response) {
            console.log(response)
          })
          .catch(function(response) {
            console.log(response)
          })
      } else if(item.currentUserLike === '1'){
          item.currentUserLike = '2'
          item.dislikeNum--
          var post_request = new FormData()
          post_request.append('paperID', this.paperID)
          post_request.append('userID', this.myID)
          post_request.append('commentID', this.comments[i].id)
          post_request.append('isLike', '0')
          post_request.append('sortedBy', this.value)
          this.$http
            .request({
             url: this.$url + '/cancelLike',
              method: 'post',
              data: post_request,
              headers: { 'Content-Type': 'multipart/form-data' },
            })
            .then(function(response) {
              console.log(response)
            })
            .catch(function(response) {
              console.log(response)
            })
        } 
    },
    likeClickreply(i, j, item) {
      if (item.currentUserLike === '2') {
        item.currentUserLike = '0'
        item.likeNum++
        var post_request = new FormData()
        post_request.append('paperID', this.paperID)
        post_request.append('userID', this.myID)
        post_request.append('commentID', this.comments[i].replyList[j].id)
        post_request.append('isLike', '1')
        post_request.append('sortedBy', this.value)
        this.$http
          .request({
            url: this.$url + '/postLike',
            method: 'post',
            data: post_request,
            headers: { 'Content-Type': 'multipart/form-data' },
          })
          .then(function(response) {
            console.log(response)
          })
          .catch(function(response) {
            console.log(response)
          })
      } else if(item.currentUserLike === '0'){
          item.currentUserLike = '2'
          item.likeNum--
          var post_request = new FormData()
          post_request.append('paperID', this.paperID)
          post_request.append('userID', this.myID)
          post_request.append('commentID', this.comments[i].replyList[j].id)
          post_request.append('isLike', '1')
          post_request.append('sortedBy', this.value)
          this.$http
            .request({
             url: this.$url + '/cancelLike',
              method: 'post',
              data: post_request,
              headers: { 'Content-Type': 'multipart/form-data' },
            })
            .then(function(response) {
              console.log(response)
            })
            .catch(function(response) {
              console.log(response)
            })
        } 
        item.isLike = !item.isLike;
    },
    dislikeClickreply(i, j, item) {
      if (item.currentUserLike === '2') {
        item.currentUserLike = '1'
        item.dislikeNum++
        var post_request = new FormData()
        post_request.append('paperID', this.paperID)
        post_request.append('userID', this.myID)
        post_request.append('commentID', this.comments[i].replyList[j].id)
        post_request.append('isLike', '0')
        post_request.append('sortedBy', this.value)
        this.$http
          .request({
            url: this.$url + '/postLike',
            method: 'post',
            data: post_request,
            headers: { 'Content-Type': 'multipart/form-data' },
          })
          .then(function(response) {
            console.log(response)
          })
          .catch(function(response) {
            console.log(response)
          })
      } else if(item.currentUserLike === '1'){
          item.currentUserLike = '2'
          item.dislikeNum--
          var post_request = new FormData()
          post_request.append('paperID', this.paperID)
          post_request.append('userID', this.myID)
          post_request.append('commentID', this.comments[i].replyList[j].id)
          post_request.append('isLike', '0')
          post_request.append('sortedBy', this.value)
          this.$http
            .request({
             url: this.$url + '/cancelLike',
              method: 'post',
              data: post_request,
              headers: { 'Content-Type': 'multipart/form-data' },
            })
            .then(function(response) {
              console.log(response)
            })
            .catch(function(response) {
              console.log(response)
            })
        } 
    },
    sendComment() {
      if (!this.replyComment) {
        this.$message({
          showClose: true,
          type: 'warning',
          message: '评论不能为空',
        })
      } else {
        let _this = this
        let input = document.getElementById('replyInput')

        var post_request = new FormData()
        post_request.append('paperID', this.paperID)
        post_request.append('userID', this.myID)
        post_request.append('userName', this.myName)
        post_request.append('contentView', this.replyComment)
        post_request.append('sortedBy', this.value)
        post_request.append('avatar', this.myImage)
        this.replyComment = ''
        input.innerHTML = ''
        this.$http
          .request({
            url: this.$url + '/postComment',
            method: 'post',
            data: post_request,
            headers: { 'Content-Type': 'multipart/form-data' },
          })
          .then(function(response) {
            _this.comments = response.data.comments
            for(var i=0;i<_this.comments.length;i++) {
              _this.$set(_this.comments[i], 'inputShow', false)
            }
            console.log(response)
          })
          .catch(function(response) {
            console.log(response)
          })
      }
    },
    sendCommentReply(i, j) {
      if (!this.replyComment) {
        this.$message({
          showClose: true,
          type: 'warning',
          message: '评论不能为空',
        })
      } else {
        let _this = this
        var post_request = new FormData()
        post_request.append('paperID', this.paperID)
        post_request.append('userID', this.myID)
        post_request.append('userName', this.myName)
        post_request.append('sortedBy', this.value)
        post_request.append('commentID', this.comments[i].id)
        post_request.append('contentView', this.replyComment)
        post_request.append('repliedName', this.myName)
        
        post_request.append('avatar', this.myImage)

        this.replyComment = ''
        document.getElementsByClassName('reply-comment-input')[i].innerHTML = ''

        this.$http
          .request({
            url: this.$url + '/postReply',
            method: 'post',
            data: post_request,
            headers: { 'Content-Type': 'multipart/form-data' },
          })
          .then(function(response) {
            _this.comments = response.data.comments
            for(var i=0;i<_this.comments.length;i++) {
              _this.$set(_this.comments[i], 'inputShow', false)
            }
            console.log(response)
          })
          .catch(function(response) {
            console.log(response)
          })
      }
    },
    onDivInput: function(e) {
      this.replyComment = e.target.innerHTML
    },
  },
}
</script>

<style lang="stylus" scoped>

.col2
    top 0
    left 70%
    bottom 0
    position absolute
    overflow auto
    float left
.my-reply
    padding 10px
    background-color #fafbfc
    .header-img
        display inline-block
        vertical-align top
    .reply-info
        display inline-block
        margin-left 5px
        width 200px
        @media screen and (max-width:1200px) {
            width 200px
        }
        .reply-input
            min-height 20px
            line-height 22px
            padding 10px 10px
            width 200px
            color #ccc
            background-color #fff
            border-radius 5px
            &:empty:before
                content attr(placeholder)
            &:focus:before
                content none
            &:focus
                padding 8px 8px
                border 2px solid blue
                box-shadow none
                outline none
    .reply-btn-box
        height 25px
        margin 10px 0
        .reply-btn
            position relative
            float right
            margin-right 15px
.my-comment-reply
    margin-left 50px
    .reply-input
        width flex
.author-title:not(:last-child)
    border-bottom: 1px solid rgba(178,186,194,.3)
.author-title
    padding 10px
    .header-img
        display inline-block
        vertical-align top
    .author-info
        display inline-block
        margin-left 5px
        width 60%
        height 40px
        line-height 20px
        >span
            display block
            cursor pointer
            overflow hidden
            white-space nowrap
            text-overflow ellipsis
        .author-name
            color #000
            font-size 18px
            font-weight bold
        .author-time
            font-size 14px
    .icon-btn
        width 30%
        padding 0 !important
        float right
        @media screen and (max-width : 1200px){
            width 20%
            padding 7px
        }
        >span
            cursor pointer
        .iconfont
            margin 0 5px
    .talk-box
        margin 0 50px
        width 150px
        >p
           margin 0
           width 150px
           word-wrap:break-word; 
           word-break:break-all;
        .reply
            font-size 16px
            color #000
    .reply-box
        margin 10px 0 0 50px
        background-color #efefef
</style>
