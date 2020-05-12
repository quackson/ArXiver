<template>
  <div class="full-content">
    <!-- 头像 -->
    <el-row :gutter="20" style="margin-top:5%;" v-if="info.userName&&avatarImg">
      <el-col :span="10"
        ><div class="icon">
          <div class="center">
            <el-avatar
              shape="square"
              :size="200"
              :src="avatarImg"
              style="margin:20px;box-shadow: 0 0 10px rgba(0,0,0,0.5);"
            ></el-avatar>
          </div>
          <div class="center">
            <el-button @click.stop="uploadAvatar">更改头像</el-button>
          </div>
          <input type="file" accept="image/jpeg" @change="handleFile" class="hiddenInput" /></div
      ></el-col>
      <!-- 基本账户信息 -->
      <el-col :span="12">
        <el-form class="main-info" :model="info" label-position="left" width="80%" label-width="100px">
          <el-form-item label="用户名：">{{ info.userName }}</el-form-item>
          <el-form-item label="电子邮件：" placeholder="请输入您的电子邮箱" class="form-row">
            <el-input v-model="info.email"></el-input>
          </el-form-item>
          <el-form-item label="专业：" placeholder="请输入您的专业" class="form-row">
            <el-input v-model="info.profession" maxlength="15" show-word-limit></el-input>
          </el-form-item>
          <el-form-item label="电话号码：" placeholder="请输入您的电话号码" class="form-row">
            <el-input v-model="info.phoneNumber" maxlength="11"></el-input>
          </el-form-item>
          <el-form-item label="个人主页：" class="form-row">
            <el-input v-model="info.personHomepage" placeholder="请输入您的个人主页" maxlength="30"></el-input>
          </el-form-item>
          <el-form-item label="备注：" show-word-limit class="form-row">
            <el-input
              type="textarea"
              v-model="info.note"
              placeholder="请输入您的个人备注"
              maxlength="80"
              show-word-limit
            ></el-input>
          </el-form-item>
        </el-form>
        <el-row :gutter="20" style="margin-top:5%;">
          <el-button type="primary" class="center" @click="saveInfo()" style="margin-top:50px">保存信息</el-button>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  inject:['reload'],
  data() {
    return {
      avatarImg: undefined,
      info: {
      },
    }
  },
  created() {
    this.load_data()
    this.loadAvatar()
  },
  methods: {
    load_data: function() {
      this.info.userName = localStorage.getItem('ms_username')
      var post_request = new FormData()
      post_request.append('userName', this.info.userName)
      this.$http
        .request({
          url: this.$url + '/getUserInformation',
          method: 'post',
          data: post_request,
          headers: { 'Content-Type': 'multipart/form-data' },
        })
        .then((response) => {
          console.log(response)
          this.info.email = response.data.userInfo.email !== 'undefined' ? response.data.userInfo.email : ''
          this.info.profession =
            response.data.userInfo.profession !== 'undefined' ? response.data.userInfo.profession : ''
          this.info.phoneNumber =
            response.data.userInfo.phoneNumber !== 'undefined' ? response.data.userInfo.phoneNumber : ''
          this.info.personHomepage =
            response.data.userInfo.personHomepage !== 'undefined' ? response.data.userInfo.personHomepage : ''
          this.info.note = response.data.userInfo.note !== 'undefined' ? response.data.userInfo.note : ''
        })
        .catch(function(response) {
          console.log(response)
        })
    },
    saveInfo: function() {
      var post_request = new FormData()
      post_request.append('userName', this.info.userName)
      post_request.append('email', this.info.email)
      post_request.append('profession', this.info.profession)
      post_request.append('phoneNumber', this.info.phoneNumber)
      post_request.append('personHomepage', this.info.personHomepage)
      post_request.append('note', this.info.note)
      this.$http
        .request({
          url: this.$url + '/modifyUserInformation',
          method: 'post',
          data: post_request,
          headers: { 'Content-Type': 'multipart/form-data' },
        })
        .then((response) => {
          console.log(response)
          this.$notify({
            title: '成功',
            message: '信息修改成功',
            type: 'success',
          })
        })
        .catch(function(response) {
          console.log(response)
          this.$notify.error({
            title: '错误',
            message: '信息修改失败',
          })
        })
    },
    loadAvatar: function() {
      this.$http
        .request({
          url: this.$url + '/getHeadImg?userName=' + this.info.userName,
          method: 'get',
        })
        .then((response) => {
          console.log(response)
          this.avatarImg = response.data.avatar_url
        })
        .catch(function(response) {
          console.log(response)
        })
    },
    // 打开图片上传
    uploadAvatar: function() {
      this.$el.querySelector('.hiddenInput').click()
    },
    // 将头像显示、上传至后端
    handleFile: function(e) {
      let $target = e.target || e.srcElement
      let file = $target.files[0]
      if (file.type != 'image/jpeg') {
        this.$notify.error({
          title: '文件类型无效',
          message: '只能上传jpg文件作为头像',
        })
        return
      }
      if (file.size / 1024 / 1024 > 4) {
        this.$notify.error({
          title: '图片体积过大',
          message: '只能上传不超过4M的图片作为头像',
        })
        return
      }

      var post_request = new FormData()
      post_request.append('userName', this.info.userName)
      post_request.append('headImg', file)
      this.$http
        .request({
          url: this.$url + '/uploadHeadImg',
          method: 'post',
          data: post_request,
          headers: { 'Content-Type': 'multipart/form-data' },
        })
        .then((response) => {
          console.log(response)
          var reader = new FileReader()
          reader.onload = (data) => {
            let res = data.target || data.srcElement
            this.avatarImg = res.result
          }
          reader.readAsDataURL(file)
          this.reload()
          this.$notify({
            title: '成功',
            message: '头像修改成功',
            type: 'success',
          })
        })
        .catch((response) => {
          console.log(response)
          this.$notify.error({
            title: '错误',
            message: '头像修改失败',
          })
        })

      // var reader = new FileReader()
      // reader.onload = (data) => {
      //   let res = data.target || data.srcElement
      //   this.avatarImg = res.result
      // }
      // reader.readAsDataURL(file)
    },
  },
}
</script>

<style>
.full-content {
  width: 98%;
}

.form-row {
  margin-top: 50px;
}
.icon .center {
  float: none;
  margin-left: auto;
  margin-right: auto;
  display: -webkit-box;
  -webkit-box-align: center;
  -webkit-box-pack: center;
}

.hiddenInput {
  display: none;
}
</style>
