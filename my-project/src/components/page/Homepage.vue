<template>
  <div class="homepage">
    <div class="full-content">
      <el-tabs v-model="onRoutes" tab-position="left" style="height: 100%;">
        <el-tab-pane label="关注列表" name="follow" :key="'follow'">
            <follow-content></follow-content>
        </el-tab-pane>
        <el-tab-pane label="个人信息" name="info" :key="'info'">
          <info-content></info-content>
        </el-tab-pane>
        <el-tab-pane label="收藏夹" name="collection" :key="'collection'">
          <collection></collection>
        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>

<script>
import followList from "./FollowListPage.vue";
import infoPage from "./InfoPage.vue";
import collection from "./CollectionPage.vue";
export default {
  data() {
    return {
    };
  },
  components: {
    followContent: followList,
    collection: collection,
    infoContent: infoPage
  },
  computed:{
    onRoutes:{
      get(){
        return this.$route.params.activeName;
      },
      set(v){
      }
    },
  }
};
</script>

<style>
.homepage{
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
