import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
// import test from '@/components/test'
// import rate from '@/components/rate'
import ElementUI from 'element-ui'

Vue.use(Router)

export default new Router({
  /*routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    }
  ]*/
  routes: [
        {
            path: '/',
            redirect: '/login'
        },
        {
            path: '/',
            component: () => import(/* webpackChunkName: "home" */ '../components/common/Home.vue'),
            meta: { title: '自述文件' },
            children: [
                {
                    path: '/dashboard',
                    component: () => import(/* webpackChunkName: "dashboard" */ '../components/page/Dashboard.vue'),
                    meta: { title: '综合页面' }
                },
                {
                    path: '/readpage/:url',
                    name: 'readpage',
                    component: () => import(/* webpackChunkName: "dashboard" */ '../components/page/ReadPage.vue'),
                    meta: { title: '论文阅读页面' }
                },
                
                {
                  path: '/account/:activeName',
                  component: () => import(/* webpackChunkName: "homepage" */ '../components/page/Homepage.vue'),
                  meta: {title: '个人信息页面'}
                },
				{
                  path: '/search',
                  component: () => import(/* webpackChunkName: "search" */ '../components/page/searchPage.vue'),
                  meta: {title: '搜索页面'}
                },
            ]
        },
        {
            path: '/login',
            component: () => import(/* webpackChunkName: "login" */ '../components/page/Login.vue'),
            meta: { title: '登录' }
        },
        {
            path: '/signup',
            component: () => import(/* webpackChunkName: "login" */ '../components/page/Signup.vue'),
            meta: { title: '注册' }
        },
        {
            path: '/hello',
            component: () => import(/* webpackChunkName: "login" */ '../components/HelloWorld.vue'),
            meta: { title: '测试' }
        }
        
    ]
})
