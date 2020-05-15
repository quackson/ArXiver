<template>
  <div class="homepage">
    <div class="full-content">
      <el-tabs v-model="onRoutes" tab-position="left" style="height: 100%;overflow-y:scroll;" @tab-click="handleTabClick">
        <el-tab-pane label="关注列表" name="follow" :key="'follow'">
          <follow-content v-if="tabRefresh.follow"></follow-content>
        </el-tab-pane>
        <el-tab-pane label="个人信息" name="info" :key="'info'">
          <info-content v-if="tabRefresh.info"></info-content>
        </el-tab-pane>
        <el-tab-pane label="收藏夹" name="collection" :key="'collection'">
          <collection v-if="tabRefresh.collection"></collection>
        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>

<script>
import followList from './FollowListPage.vue'
import infoPage from './InfoPage.vue'
import collection from './CollectionPage.vue'
export default {
  data() {
    return {
      tabRefresh: {
        follow: false,
        info: false,
        collection: false,
      },
    }
  },
  components: {
    followContent: followList,
    collection: collection,
    infoContent: infoPage,
  },
  computed: {
    onRoutes: {
      get() {
        this.switchTab(this.$route.params.activeName)
        return this.$route.params.activeName
      },
      set(v) {},
    },
  },
  methods: {
    handleTabClick: function(tab, event) {
      this.$router.push({ path: '/account/' + tab.name })
      switch (tab.name) {
        case 'follow':
          this.switchTab('follow')
          break
        case 'info':
          this.switchTab('info')
          break
        case 'collection':
          this.switchTab('collection')
          break
        default:
          console.log('wrong choice')
      }
    },
    switchTab: function(tab) {
      for (let [key, value] of Object.entries(this.tabRefresh)) {
        if (key == tab) {
          this.tabRefresh[key] = true
        } else {
          this.tabRefresh[key] = false
        }
      }
    },
  },
}
</script>

<style>
.homepage {
  height: 100%;
}
.full-content {
  margin-top: 20px;
  margin-left: 10px;
  margin-right: 20px;
  height: 100%;
}
.el-tabs__item {
  font-size: 17px !important;
  margin-right: 10px;
  margin-left: 10px;
}
</style>
