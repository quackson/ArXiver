<template>
  <div class = "wrapper">
  <el-main class= "col2">
        <div class="comment">
        <el-select v-model="value" placeholder="排序方式" size = "mini" style = "padding-top: 10px;float:right;">
        <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled">
        </el-option>
        </el-select>
        <div v-clickoutside="hideReplyBtn" @click="inputFocus" class="my-reply">
            <el-avatar class="header-img" :size="40" :src="myImage"></el-avatar>
            <div class="reply-info" >
                <div 
                tabindex="0" 
                contenteditable="true" 
                id="replyInput" 
                spellcheck="false" 
                placeholder="输入评论..." 
                class="reply-input" 
                @focus="showReplyBtn"  
                @input="onDivInput($event)"
                >
                </div>
            </div>
            <div class="reply-btn-box" v-show="btnShow">
                <el-button class="reply-btn" size="medium" @click="sendComment" type="primary">发表评论</el-button>
            </div>
        </div>
        <div v-for="(item,i) in comments" :key="i" class="author-title reply-father">
            <el-avatar class="header-img" :size="40" :src="item.userImage"></el-avatar>
            <div class="author-info">
                <span class="author-name">{{item.userName}}</span>
                <span class="author-time">{{item.time}}</span>
            </div>
            <div class="icon-btn">
                <span @click="showReplyInput(i,item.name,item.id)"><i class="iconfont el-icon-s-comment"></i>{{item.commentNum}}</span>
                <span class="like" :class="{active: item.isLike}" @click="likeClick(item)">
                <i v-if = "item.isLike" class="iconfont el-icon-star-on"></i>
                <i v-else class="iconfont el-icon-star-off"></i>
                {{item.like}}
                </span>
                <span class="dislike" :class="{active: item.isdisLike}" @click="dislikeClick(item)">
                <i v-if = "item.isdisLike" class="iconfont el-icon-error"></i>
                <i v-else class="iconfont el-icon-close"></i>
                {{item.dislike}}
                </span>
            </div>
            <div class="talk-box">
                <p>
                    <span class="reply">{{item.comment}}</span>
                </p>
            </div>
            <div class="reply-box">
                <div v-for="(reply,j) in item.reply" :key="j" class="author-title">
                    <el-avatar class="header-img" :size="40" :src="reply.fromImage"></el-avatar>
                    <div class="author-info">
                        <span class="author-name">{{reply.from}}</span>
                        <span class="author-time">{{reply.time}}</span>
                    </div>
                    <div class="icon-btn">
                        <span @click="showReplyInput(i,reply.from,reply.id)"></span>
                        <span class="like" :class="{active: reply.isLike}" @click="likeClick(reply)">
                        <i v-if = "reply.isLike" class="iconfont el-icon-star-on"></i>
                        <i v-else class="iconfont el-icon-star-off"></i>
                        {{reply.like}}
                        </span>
                        <span class="dislike" :class="{active: reply.isdisLike}" @click="dislikeClick(reply)">
                        <i v-if = "reply.isdisLike" class="iconfont el-icon-error"></i>
                        <i v-else class="iconfont el-icon-close"></i>
                        {{reply.dislike}}
                        </span>
                    </div>
                    <div class="talk-box">
                        <p>
                            <span>回复 {{reply.to}}:</span>
                            <span class="reply">{{reply.comment}}</span>
                        </p>
                    </div>
                    <div class="reply-box">

                    </div>
                </div>
            </div>
            <div  v-show="_inputShow(i)" class="my-reply my-comment-reply">
                <el-avatar class="header-img" :size="40" :src="myImage"></el-avatar>
                <div class="reply-info" >
                    <div tabindex="0" contenteditable="true" spellcheck="false" placeholder="输入评论..."   @input="onDivInput($event)"  class="reply-input reply-comment-input"></div>
                </div>
                <div class=" reply-btn-box">
                    <el-button class="reply-btn" size="medium" @click="sendCommentReply(i,j)" type="primary">发表评论</el-button>
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
            return false;
        }
    // 判断指令中是否绑定了函数
        if (binding.expression) {
            // 如果绑定了函数 则调用那个函数，此处binding.value就是handleClose方法
            binding.value(e);
        }
    }
    // 给当前元素绑定个私有变量，方便在unbind中可以解除事件监听
    el.vueClickOutside = documentHandler;
    document.addEventListener('click', documentHandler);
    },
    update() {},
    unbind(el, binding) {
    // 解除事件监听
    document.removeEventListener('click', el.vueClickOutside);
    delete el.vueClickOutside;
  },
};
export default {
    data() {
        return {
            options: [{
                value: '1',
                label: '时间'
            },
            {
                value: '2',
                label: '热度' 
            }],
            btnShow: false,
            index:'0',
            replyComment:'',
            myName:'攻城狮',
            myImage:'https://ae01.alicdn.com/kf/Hd60a3f7c06fd47ae85624badd32ce54dv.jpg',
            myID:19870621,
            to:'',
            paperID:-1,
            comments:[
                {
                    userName:'攻城狮',
                    userID:19870621,
                    userImage:'https://ae01.alicdn.com/kf/Hd60a3f7c06fd47ae85624badd32ce54dv.jpg',
                    comment:'这篇论文对我启发很大',
                    time:'2020年4月16日 18:43',
                    commentNum:2,
                    like:15,
                    dislike:2,
                    isLike:false,
                    isdisLike:false,
                    inputShow:false,
                    reply:[
                        {
                            from:'程序猿',
                            fromID:19891221,
                            fromImage:'https://ae01.alicdn.com/kf/H94c78935ffa64e7e977544d19ecebf06L.jpg',
                            to:'攻城狮',
                            toID:19870621,
                            comment:'我也是！！',
                            time:'2020年4月16日 18:50',
                            like:15,
                            dislike:2,
                            isLike:false,
                            isdisLike:false,
                        },
                        {
                            from:'二进雉',
                            fromID:1123,
                            fromImage:'https://ae01.alicdn.com/kf/Hf6c0b4a7428b4edf866a9fbab75568e6U.jpg',
                            to:'攻城狮',
                            toID:19870621,
                            comment:'确实很不错啊！',
                            time:'2020年4月16日 18:59',
                            like:5,
                            dislike:2,
                            isLike:false,
                            isdisLike:false

                        }
                    ]
                },
                {
                    userName:'程序猿',
                    userID:19891221,
                    userImage:'https://ae01.alicdn.com/kf/H94c78935ffa64e7e977544d19ecebf06L.jpg',
                    comment:'这只是一个简单的测试~~~~~~',
                    time:'2020年4月16日 20:40',
                    commentNum:1,
                    like:5,
                    dislike:2,
                    isLike:false,
                    isdisLike:false,
                    inputShow:false,
                    reply:[
                        {
                            from:'我也不知道要叫什么名字了',
                            fromID:19870621,
                            fromImage:'https://ae01.alicdn.com/kf/Hd60a3f7c06fd47ae85624badd32ce54dv.jpg',
                            to:'Taylor Swift',
                            toID:19891221,
                            comment:'我也来试一下。',
                            time:'2020年4月16日 20:55',
                            like:5,
                            dislike:2,
                            isLike:false,
                            isdisLike:false

                        }
                    ]
                },
                {
                    userName:'真是太难了',
                    userID:20190830,
                    userImage:'https://ae01.alicdn.com/kf/Hdd856ae4c81545d2b51fa0c209f7aa28Z.jpg',
                    comment:'完全不知道还要说些什么。。。。。。',
                    time:'2020年4月16日 21:23',
                    commentNum:0,
                    like:5,
                    dislike:2,
                    isLike:false,
                    isdisLike:false,
                    inputShow:false,
                    reply:[]
                },
            ]
           
    }
  },
  directives: {clickoutside},
  methods: {
    inputFocus(){
            var replyInput = document.getElementById('replyInput');
            replyInput.style.padding= "8px 8px"
            replyInput.style.border ="2px solid blue"
            replyInput.focus()
        },  
        showReplyBtn(){
            this.btnShow = true
        },
        hideReplyBtn(){
            this.btnShow = false
            replyInput.style.padding= "10px"
            replyInput.style.border ="none"
        },
        showReplyInput(i,name,id){
            this.comments[this.index].inputShow = false
            this.index =i
            this.comments[i].inputShow = true
            this.to = name
            this.toID = id
        },
        _inputShow(i){
            return this.comments[i].inputShow 
        },
        likeClick(item) {
        
          if (item.isLike) {
            item.like--
          } else {
            item.like++
          }
          item.isLike = !item.isLike;
        
        },
        dislikeClick(item) {
        
          if (item.isdisLike) {
            item.dislike--
          } else {
            item.dislike++
          }
          item.isdisLike = !item.isdisLike;
        
        },

        sendComment(){
            if(!this.replyComment){
                 this.$message({
                    showClose: true,
                    type:'warning',
                    message:'评论不能为空'
                })
            }else{
                let a ={}
                let input =  document.getElementById('replyInput')
                let timeNow = new Date().getTime();
                let time= this.dateStr(timeNow);
                a.userName= this.myName
                a.comment =this.replyComment
                a.userImage = this.myImage
                a.time = time
                a.commentNum = 0
                a.like = 0
                this.comments.push(a)
                this.replyComment = ''
                input.innerHTML = '';

            }
        },
        sendCommentReply(i,j){
            if(!this.replyComment){
                 this.$message({
                    showClose: true,
                    type:'warning',
                    message:'评论不能为空'
                })
            }else{
                let a ={}
                let timeNow = new Date().getTime();
                let time= this.dateStr(timeNow);
                a.from= this.myName
                a.to = this.to
                a.fromImage = this.myImage
                a.comment =this.replyComment
                a.time = time
                a.commentNum = 0
                a.like = 0
                this.comments[i].reply.push(a)
                this.replyComment = ''
                document.getElementsByClassName("reply-comment-input")[i].innerHTML = ""
            }
        },
        onDivInput: function(e) {
            this.replyComment = e.target.innerHTML;
        },
        dateStr(date){
            //获取js 时间戳
            var time=new Date().getTime();
            //去掉 js 时间戳后三位，与php 时间戳保持一致
            time=parseInt((time-date)/1000);
            //存储转换值 
            var s;
            if(time<60*10){//十分钟内
                return '刚刚';
            }else if((time<60*60)&&(time>=60*10)){
                //超过十分钟少于1小时
                s = Math.floor(time/60);
                return  s+"分钟前";
            }else if((time<60*60*24)&&(time>=60*60)){ 
                //超过1小时少于24小时
                s = Math.floor(time/60/60);
                return  s+"小时前";
            }else if((time<60*60*24*30)&&(time>=60*60*24)){ 
                //超过1天少于30天内
                s = Math.floor(time/60/60/24);
                return s+"天前";
            }else{ 
                //超过30天ddd
                var date= new Date(parseInt(date));
                return date.getFullYear()+"/"+(date.getMonth()+1)+"/"+date.getDate();
            }
        }
  }
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
