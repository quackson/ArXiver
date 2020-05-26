<template>
    <div class="login-wrap">
        <div class="head">
            <el-button type="info" round @click="signup">Sign Up</el-button>
            <el-button type="info" round @click="signin">Sign In</el-button>
        </div>
        <div class="ms-login">
            <div class="ms-title">arXiver</div>
            <el-form :model="param" :rules="rules" ref="login" label-width="0px" class="ms-content">
                <el-form-item prop="username">
                    <el-input v-model="param.username" placeholder="请输入用户名">
                        <el-button slot="prepend" icon="el-icon-user-solid"></el-button>
                    </el-input>
                </el-form-item>
                <el-form-item prop="emali">
                    <el-input v-model="param.email" placeholder="请输入邮箱">
                        <el-button slot="prepend" icon="el-icon-message"></el-button>
                    </el-input>
                </el-form-item>
                <el-form-item prop="password">
                    <el-input
                        type="password"
                        placeholder="请输入密码"
                        v-model="param.password"
                        @keyup.enter.native="registerForm()"
                    >
                        <el-button slot="prepend" icon="el-icon-lock"></el-button>
                    </el-input>
                </el-form-item>
                <div class="login-btn">
                    <el-button type="info" @click="registerForm()">注册</el-button>
                </div>
            </el-form>
        </div>
    </div>
</template>

<script>
export default {
    data: function() {
        return {
            param: {
                username: '',
                password: '',
                email: '',
            },
            rules: {
                username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
                email: [{ required: true, message: '请输入邮箱', trigger: 'blur' }],
                password: [{ required: true, message: '请输入密码', trigger: 'blur' }],
            },
        };
    },
    methods: {
        signin() {
            this.$router.push('/login');
        },
        signup() {
            this.$router.push('/signup');
        },
        registerForm() {
            var post_request = new FormData()
            post_request.append('userName', this.param.username)
            post_request.append('password', this.param.password)
            post_request.append('email', this.param.email)
            let _this = this;
            this.$http
            .request({
              url: this.$url + '/register',
              method: 'post',
              data: post_request,
              headers: { 'Content-Type': 'multipart/form-data' },
            })
            .then(function(response) {
              console.log(response)
              if(response.data.register.retCode == 1){
                _this.$message({
                    message: response.data.register.message + "！请登录",
                    type: 'success',
                });
                _this.$router.push('/login');
              }
              else {
                _this.$message({
                    message: response.data.register.message,
                    type: 'error',
                });
              }
              
            })
            .catch(function(response) {
              console.log(response)
            });
        },
    },
};
</script>

<style scoped>
.login-wrap {
    position: fixed;
    width:100%;
    height: 100%;
    background-size: 100%;
    background-repeat:no-repeat;
    background-attachment: fixed;
    background-image: url(../../assets/img/login5.png);
}
.head {
    width: 100%;
    height: 70px;
    background-color: #324157;
}
.head button {
    float: right;
    height: 36px;
    margin-left: 10px;
    margin-top: 15px;
}
.ms-title {
    width: 100%;
    line-height: 50px;
    text-align: center;
    font-size: 40px;
    color: #fff;
    border-bottom: 1px solid #ddd;
}
.ms-login {
    position: absolute;
    left: 50%;
    top: 0%;
    width: 350px;
    margin: 190px 0 0 -175px;
    border-radius: 5px;
    background: rgba(255, 255, 255, 0.3);
    overflow: hidden;
}
.ms-content {
    padding: 30px 30px;
}
.login-btn {
    text-align: center;
}
.login-btn button {
    width: 100%;
    height: 36px;
    margin-bottom: 10px;
}
.login-tips {
    font-size: 12px;
    line-height: 30px;
    color: #fff;
}
</style>