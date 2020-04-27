<template>
  <div class="wrapper">
    <el-main class="col2">
      <div class="comment">
        <el-select v-model="value" placeholder="排序方式" size="mini" style="padding-top: 10px;float:right;">
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
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
            <span @click="showReplyInput(i, item.name, item.id)"
              ><i class="iconfont el-icon-s-comment"></i>{{ item.replyNum }}</span
            >
            <span class="like" :class="{active: item.isLike}" @click="likeClick(i, item)">
              <i class="iconfont el-icon-star-off"></i>
              {{ item.likeNum }}
            </span>
            <span class="dislike" :class="{active: item.isDislike}" @click="dislikeClick(i, item)">
              <i class="iconfont el-icon-close"></i>
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
                <span @click="showReplyInput(i, reply.userNmae, reply.id)"></span>
                <span class="like" :class="{active: reply.isLike}" @click="likeClick(j, reply)">
                  <i class="iconfont el-icon-star-off"></i>
                  {{ reply.likeNum }}
                </span>
                <span class="dislike" :class="{active: reply.isDislike}" @click="dislikeClick(j, reply)">
                  <i class="iconfont el-icon-close"></i>
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
            <!--<el-avatar class="header-img" :size="40" :src="myImage"></el-avatar>-->
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
          value: '1',
          label: '时间',
        },
        {
          value: '2',
          label: '热度',
        },
      ],
      btnShow: false,
      index: '0',
      replyComment: '',
      myName: '攻城狮',
      myImage: 'https://ae01.alicdn.com/kf/Hd60a3f7c06fd47ae85624badd32ce54dv.jpg',
      myID: 19870621,
      to: '',
      comments: null,
    }
  },
  directives: { clickoutside },
  mounted() {
    let _this = this
    this.$http
      .request({
        url: _this.$url + '/getPaperComment?paperID=1&sortedBy=time',
        method: 'get',
      })
      .then(function(response) {
        _this.comments = response.data.comments
        console.log(response)
      })
      .catch(function(response) {
        console.log(response)
      })
  },
  methods: {
    inputFocus() {
      var replyInput = document.getElementById('replyInput')
      replyInput.style.padding = '8px 8px'
      replyInput.style.border = '2px solid blue'
      replyInput.focus()
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
      if (item.isLike === null) {
        Vue.$set(item, "isLike", true);
        item.likeNum++
        var post_request = new FormData()
        post_request.append('paperID', '1')
        post_request.append('commentID', this.comments[i].id)
        post_request.append('isLike', '1')
        post_request.append('sortedBy', 'time')
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
      } else {
        if (item.isLike) {
          item.likeNum--
          var post_request = new FormData()
          post_request.append('paperID', '1')
          post_request.append('commentID', this.comments[i].id)
          post_request.append('isLike', '1')
          post_request.append('sortedBy', 'time')
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
        } else {
          item.likeNum++
          var post_request = new FormData()
          post_request.append('paperID', '1')
          post_request.append('commentID', this.comments[i].id)
          post_request.append('isLike', '1')
          post_request.append('sortedBy', 'time')
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
        }
        item.isLike = !item.isLike;
      }
    },
    dislikeClick(i, item) {
      if (item.isDislike === null) {
        Vue.$set(item, "isDislike", true);
        item.dislikeNum++
        var post_request = new FormData()
        post_request.append('paperID', '1')
        post_request.append('commentID', this.comments[i].id)
        post_request.append('isLike', '0')
        post_request.append('sortedBy', 'time')
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
      } else {
        if (item.isDislike) {
          item.dislikeNum--
          var post_request = new FormData()
          post_request.append('paperID', '1')
          post_request.append('commentID', this.comments[i].id)
          post_request.append('isLike', '0')
          post_request.append('sortedBy', 'time')
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
        } else {
          item.dislikeNum++
          var post_request = new FormData()
          post_request.append('paperID', '1')
          post_request.append('commentID', this.comments[i].id)
          post_request.append('isLike', '0')
          post_request.append('sortedBy', 'time')
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
        }
        item.isDislike = !item.isDislike;
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
        let a = {}
        let input = document.getElementById('replyInput')
        let timeNow = new Date().getTime()
        let time = this.dateStr(timeNow)
        a.userName = this.myName
        a.contentView = this.replyComment
        a.avatar = this.myImage
        a.pubTime = time
        a.replyNum = 0
        a.likeNum = 0
        a.dislikeNum = 0
        this.comments.push(a)

        var post_request = new FormData()
        post_request.append('paperID', '1')
        post_request.append('userID', this.myID)
        post_request.append('userName', this.myName)
        post_request.append('contentView', this.replyComment)
        post_request.append('sortedBy', 'time')
        post_request.append('avatar', 'avatar')
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
        let a = {}
        let timeNow = new Date().getTime()
        let time = this.dateStr(timeNow)
        a.userName = this.myName
        a.replyCommentUserName = this.comments[i].userName
        a.avatar = this.myImage
        a.contentView = this.replyComment
        a.pubTime = time
        a.replyNum = 0
        a.likeNum = 0
        a.dislikeNum = 0
        this.comments[i].replyList.push(a)

        var post_request = new FormData()
        post_request.append('paperID', '1')
        post_request.append('userID', this.myID)
        post_request.append('userName', this.myName)
        post_request.append('sortedBy', 'time')
        post_request.append('commentID', this.comments[i].id)
        post_request.append('contentView', this.replyComment)
        post_request.append('repliedName', this.myName)

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
    dateStr(date) {
      //获取js 时间戳
      var time = new Date().getTime()
      //去掉 js 时间戳后三位，与php 时间戳保持一致
      time = parseInt((time - date) / 1000)
      //存储转换值
      var s
      if (time < 60 * 10) {
        //十分钟内
        return '刚刚'
      } else if (time < 60 * 60 && time >= 60 * 10) {
        //超过十分钟少于1小时
        s = Math.floor(time / 60)
        return s + '分钟前'
      } else if (time < 60 * 60 * 24 && time >= 60 * 60) {
        //超过1小时少于24小时
        s = Math.floor(time / 60 / 60)
        return s + '小时前'
      } else if (time < 60 * 60 * 24 * 30 && time >= 60 * 60 * 24) {
        //超过1天少于30天内
        s = Math.floor(time / 60 / 60 / 24)
        return s + '天前'
      } else {
        //超过30天ddd
        var date = new Date(parseInt(date))
        return date.getFullYear() + '/' + (date.getMonth() + 1) + '/' + date.getDate()
      }
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
        width 90%
        @media screen and (max-width:1200px) {
            width 80%
        }
        .reply-input
            min-height 20px
            line-height 22px
            padding 10px 10px
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
        >p
           margin 0
        .reply
            font-size 16px
            color #000
    .reply-box
        margin 10px 0 0 50px
        background-color #efefef
</style>
