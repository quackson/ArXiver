# Arxiver 

2020春季软件工程课一组项目

- ### 概述

  - web app, 前端vue+后端django
  - 已部署在阿里云服务器，地址：<http://121.199.25.59/>
  - 实现arxiv网站客户端，基于官方接口，设计提供个人收藏，阅读，个性化推荐，搜索，评论的网络应用

- ### 面向人群

  - 具有arxiv网站使用需求的各领域学生，教师，科研人员
  - 方便arxiv网站论文的检索与收藏

- ### 功能简介

  - #### 注册

    - 通过邮箱注册
    - 用户名唯一

  - #### 登录

    - 使用用户名和密码登录

  - #### 搜索

    - 顶栏搜索
      - 通过作者搜索
      - 通过论文名搜索
      - 通过关键字搜索
    - 左边栏搜索
      - 通过学科搜索
      - 学科列表包含三级目录，对应arxiv网站最细粒度划分

  - #### 个性化推荐

    - 基于用户关注领域及收藏列表

  - #### 论文阅读

    - 采用vue-pdf插件实现
    - 提供在线阅读，收藏，下载，放大，翻页

  - #### 论文评论

    - 每篇论文拥有自己的评论区
    - 评论可回复
    - 评论可点赞/踩

  - #### 个人信息

    - 收藏夹展示，可选中一篇或多篇删除
    - 个人信息展示，包括头像，邮箱等用户信息，可上传图片或键入新内容修改
    - 个人关注领域，可修改

- ### 实现框架

  - #### 前端

    - vue框架
    - 使用element UI 设计
    - 论文阅读采用vue-pdf插件

  - #### 后端

    - django框架

  - #### 服务器部署

    - WSGI
  
- ### 注

  - 有关vue-pdf插件问题，需修改有源码

    ```c++
    npm install -D worker-plugin
    #修改vue.config.js
    const WorkerPlugin = require('worker-plugin')
    module.exports = {
      lintOnSave: false,
      configureWebpack: {
        plugins: [
          new WorkerPlugin()
        ]
      }
    }
    #修改node_modules/vue-pdf/src/vuePdfNoSss.vue,删减第13&14行改为
    PDFJS.GlobalWorkerOptions.workerPort = new Worker('pdfjs-dist/build/pdf.worker.js', { type: 'module' });
    ```

    - 第三步修改需在每次npm install后进行一次

- ### 本地运行方式

  - 前端环境及框架

    - 为避免版本不兼容问题，采用vue-cli4，安装方式见官网
      - 要求安装node.js

  - 后端环境及框架

    - django

  - 命令

    ```cmd
    cd my-project
    npm install
    npm run build
    cd ..
    py manage.py runserver
    ```

    