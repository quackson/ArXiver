<template>
    <div class="wrapper">
        <v-head></v-head>
        <v-sidebar style="width=20%"></v-sidebar>
        <div class="content-box" :class="{'content-collapse':collapse}">
                <transition name="move" mode="out-in">
                        <router-view></router-view>
                </transition>
        </div>
    </div>
</template>

<script>
import vHead from './Header.vue';
import vSidebar from './Sidebar.vue';
import bus from './bus';
export default {
    data() {
        return {
            collapse: false
        };
    },
    components: {
        vHead,
        vSidebar
    },
    created() {
        bus.$on('collapse-content', msg => {
            this.collapse = msg;
        });
    }
};
</script>

<style scoped>
.content-box{
    right: 30px;
    top: 70px;
    bottom: 0;
    padding-bottom: 30px;
    position: absolute;
    left: 350px;
    transition: left .3s ease-in-out;
}
.content-collapse{
    left: 60px;
}
</style>
