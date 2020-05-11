<template>
  <div class = "wrapper">
    <el-main class = "col1">
        <div class="main">
            <pdf
            :src="src"
            :page="currentPage"
            @progress="loadedRatio = $event"
            @loaded="loadPdfHandler"
            @num-pages="pageCount=$event"
            @page-loaded="currentPage=$event"
            ref="wrapper"
            class="pdf"></pdf>
        </div>
        <ul class="footers">
            <li :class="{select:idx==0}" @touchstart="idx=0" @touchend="idx=-1" @click="scaleD">
                <p class="more-p">放大</p>
            </li>
            <li :class="{select:idx==1}" @touchstart="idx=1" @touchend="idx=-1" @click="scaleX">
                <p class="small-p">缩小</p>
            </li>
            <li :class="{select:idx==2}" @touchstart="idx=2" @touchend="idx=-1" @click="changePdfPage(0)">
                <p class="up-p">上一页</p>
            </li>
            <li :class="{select:idx==3}" @touchstart="idx=3" @touchend="idx=-1" @click="changePdfPage(1)">
                <p class="down-p">下一页</p>
            </li>
            <li>
                <p>当前第{{ currentPage }}页/共{{ pageCount }}页</p>
            </li>
            <a style = "margin-top: 15px;margin-left: 30px"  @click = "downloadPdf">download</a>
            <el-button class="mark-btn" size="medium" type="info" @click = "addcollect">收藏</el-button>
            <el-button class="mark-btn" size="medium" type="info" @click = "cancelcollect">取消收藏</el-button>
        </ul>
    </el-main>
  </div>
</template>

<script>
import pdf from 'vue-pdf';
export default {
  data() {
  	const papers = {currentPage: 1, pageCount: 0, url: 'http://storage.xuetangx.com/public_assets/xuetangx/PDF/PlayerAPI_v1.0.6.pdf'};
    return {
      currentPage: papers.currentPage, // 当前页码
      pageCount: papers.pageCount, // 总页码
      src: 'http://arxiv.org/pdf/cond-mat/0402245v1.pdf',
      url: 'http://arxiv.org/pdf/cond-mat/0402245v1',
      paperID:'',
      myName: localStorage.getItem("ms_username"),
      scale: 100,
      idx: -1,
      loadedRatio: 0,
    }
  },
  created() {
    console.log(this.$route.params.url);
    this.url = this.$route.params.url;
    this.paperID = this.$route.params.id;
    this.src = this.url+'.pdf';
    console.log(this.src);
    this.src = pdf.createLoadingTask(this.src) // 处理一下跨域
  },
  components: {
    pdf
  },
  methods: {
    addcollect() {
      var post_request = new FormData()
      post_request.append('userName', this.myName)
      post_request.append('paperID', this.paperID)
      let _this = this;
      this.$http
        .request({
          url: _this.$url + '/addCollect',
          method: 'post',
          data: post_request,
          headers: { 'Content-Type': 'multipart/form-data' },
        })
        .then(function(response) {
          _this.$message({
              message: "添加收藏成功！",
              type: 'success',
          });
          console.log(response)
        })
        .catch(function(response) {
          console.log(response)
        })
    },
    cancelcollect() {
      var post_request = new FormData()
      post_request.append('userName', this.myName)
      post_request.append('paperID', this.paperID)
      let _this = this;
      this.$http
        .request({
          url: _this.$url + '/cancelCollect',
          method: 'post',
          data: post_request,
          headers: { 'Content-Type': 'multipart/form-data' },
        })
        .then(function(response) {
          _this.$message({
              message: "取消收藏成功！",
              type: 'success',
          });
          console.log(response)
        })
        .catch(function(response) {
          console.log(response)
        })
    },
    
    // 改变PDF页码,val传过来区分上一页下一页的值,0上一页,1下一页
    changePdfPage(val) {
      if(val === 0 && this.currentPage > 1) {
        this.currentPage--;
      }
      if(val === 1 && this.currentPage < this.pageCount) {
        this.currentPage++;
      }
      console.log(this.currentPage);
      console.log(this.pageCount);
    },
    goBack() {
      this.$router.go(-1);
    },
    // pdf加载时
    loadPdfHandler(e) {
      this.currentPage = 1; // 加载的时候先加载第一页
    },
    downloadPdf() {
      let a = document.createElement('a');
      a.href = this.$url + '/getPdfFile?url='+this.url ;
      a.click();
    },
    //放大
    scaleD() {
      this.scale += 5;
      this.$refs.wrapper.$el.style.width = parseInt(this.scale) + "%";
    },
    //缩小
    scaleX() {     
      this.scale += -5;
      this.$refs.wrapper.$el.style.width = parseInt(this.scale) + "%";
    }
  }
}
</script>

<style lang="stylus" scoped>

.main 
  top 0
  margin-bottom 20px
  left 0
  width 70%
  bottom 30px
  position absolute
  z-index 1
  overflow auto

.footers 
  position absolute
  bottom 0
  left 0
  width 70%
  display flex
  z-index 100
  color #333
  line-height 10px
  height 30px

.li 
  text-align center
  flex 1
  padding 5px
  cursor pointer

.ul 
  list-style none

.more-p 
  border-right 1px solid #f0f0f0
  margin-right 40px
  cursor pointer

.small-p 
  margin-right 40px
  cursor pointer

.up-p 
  margin-right 40px
  cursor pointer

.down-p 
  border-radius 0 none
  cursor pointer
  margin-right 50px
</style>