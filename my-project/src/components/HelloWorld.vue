<template>
  <div class = "test">
    <h1>This is the comments data</h1>
    <button @click = "getdata">点击获取数据</button>
    {comment}
  </div>
</template>

<script>
  export default {
    data:function() {
      return {
        comment:null
      }
    },
    methods: {
      getdata:function() {
        let _this = this
        this.$http.request({
          url:_this.$url + '/display_page/1/?paperID=1&sortedBy=time',
          method:'get',
        }).then(function(response) {
          _this.comment = response.data.comments,
          console.log(response)
        }).catch(function(response) {
          console.log(response)
        })

      }
    }
  }
</script>

<style scoped>
</style>