<template>
  <div class="full-content">
    <!-- 头像 -->
    <el-row :gutter="20" style="margin-top:5%;">
      <el-col :span="12"
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
          <input
            type="file"
            accept="image/*"
            @change="handleFile"
            class="hiddenInput"
          /></div
      ></el-col>
      <!-- 基本账户信息 -->
      <el-col :span="12"
        ><el-form class="main-info" width="100%">
          <div class="usrname">{{ name }}</div>
          <div class="email">{{ email }}</div>
        </el-form></el-col
      >
    </el-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      avatarImg:
        "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
      name: "admin",
      email: "admin@admin.com"
    };
  },
  methods: {
    // 打开图片上传
    uploadAvatar: function() {
      this.$el.querySelector(".hiddenInput").click();
    },
    // 将头像显示
    handleFile: function(e) {
      let $target = e.target || e.srcElement;
      let file = $target.files[0];
      var reader = new FileReader();
      reader.onload = data => {
        let res = data.target || data.srcElement;
        this.avatarImg = res.result;
      };
      reader.readAsDataURL(file);
    }
  }
};
</script>

<style>
.full-content {
  width: 100%;
}
.icon .center {
  float: none;
  margin-left: auto;
  margin-right: auto;
  display: -webkit-box;
  -webkit-box-align: center;
  -webkit-box-pack: center;
}
.usrname,
.email {
  font-size: 16px;
  color: #898989;
  width: 100%;
  margin-top: 50px;
}
.usrname::before {
  content: "用户名：";
}
.email::before {
  content: "邮箱：";
}
.usrname::before,
.email::before {
  float: left;
  width: 25%;
  color: black;
}
.hiddenInput {
  display: none;
}
</style>
