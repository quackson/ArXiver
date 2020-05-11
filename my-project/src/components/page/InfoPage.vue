<template>
  <div class="full-content">
    <!-- 头像 -->
    <el-row :gutter="20" style="margin-top:5%;">
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
          <input type="file" accept="image/*" @change="handleFile" class="hiddenInput" /></div
      ></el-col>
      <!-- 基本账户信息 -->
      <el-col :span="12">
        <el-form class="main-info" :model="info" label-position="left" width="80%" label-width="100px">
          <el-form-item label="用户名：">{{ info.name }}</el-form-item>
          <el-form-item label="电子邮件：" class="form-row">
            <el-input v-model="info.email"></el-input>
          </el-form-item>
          <el-form-item label="专业：" class="form-row">
            <el-input v-model="info.profession" maxlength="15" show-word-limit></el-input>
          </el-form-item>
          <el-form-item label="电话号码：" class="form-row">
            <el-input v-model="info.phoneNumber" maxlength="11"></el-input>
          </el-form-item>
          <el-form-item label="个人主页：" class="form-row">
            <el-input v-model="info.personHomepage" maxlength="30"></el-input>
          </el-form-item>
          <el-form-item label="备注：" show-word-limit class="form-row">
            <el-input type="textarea" v-model="info.note" maxlength="80" show-word-limit></el-input>
          </el-form-item>
        </el-form>
        <el-row :gutter="20" style="margin-top:5%;">
          <el-button type="primary" class="center" style="margin-top:50px">保存信息</el-button>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      avatarImg: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png',
    }
  },
  computed: {
    info() {
      let info = {
        name: 'admin',
        email: 'admin@admin.com',
        profession: 'xxx',
        phoneNumber: '135',
        personHomepage: 'www.linxin.com',
        note: 'hi!我是linxin',
      };
      return info;
      console.log(name)
      var post_request = new FormData()
      post_request.append('userName', name)
      this.$http
        .request({
          url: this.$url + '/getUserInformation',
          method: 'post',
          data: post_request,
          headers: { 'Content-Type': 'multipart/form-data' },
        })
        .then(function(response) {
          console.log(response)
          info.email = response.data.email
          info.profession = response.data.profession
          info.phoneNumber = response.data.phoneNumber
          info.area = response.data.area
          info.personHomepage = response.data.personHomepage
          info.note = response.data.note
        })
        .catch(function(response) {
          console.log(response)
        })
    },
  },
  methods: {
    // 打开图片上传
    uploadAvatar: function() {
      this.$el.querySelector('.hiddenInput').click()
    },
    // 将头像显示
    handleFile: function(e) {
      let $target = e.target || e.srcElement
      let file = $target.files[0]
      var reader = new FileReader()
      reader.onload = (data) => {
        let res = data.target || data.srcElement
        this.avatarImg = res.result
      }
      reader.readAsDataURL(file)
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
