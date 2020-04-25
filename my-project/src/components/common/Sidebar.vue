<template>
<div class="sidebar">
        <el-menu
            class="sidebar-el-menu"
            :default-active="onRoutes"
            :collapse="collapse"
            background-color="#324157"
            text-color="#bfcbd9"
            active-text-color="#20a0ff"
            unique-opened
            router
        >
            <template v-for="item in items">
                <template v-if="item.subs">
                    <el-submenu :index="item.index" :key="item.index">
                        <template slot="title">
                            <i :class="item.icon"></i>
                            <span slot="title">{{ item.title }}</span>
                        </template>
                        <template v-for="subItem in item.subs">
                            <el-submenu
                                v-if="subItem.subs"
                                :index="subItem.index"
                                :key="subItem.index"
                            >
                                <template slot="title">{{ subItem.title }}</template>
                                <el-menu-item
                                    v-for="(threeItem,i) in subItem.subs"
                                    :key="i"
                                    :index="threeItem.index"
                                >{{ threeItem.title }}</el-menu-item>
                            </el-submenu>
                            <el-menu-item
                                v-else
                                :index="subItem.index"
                                :key="subItem.index"
                            >{{ subItem.title }}</el-menu-item>
                        </template>
                    </el-submenu>
                </template>
                <template v-else>
                    <el-menu-item :index="item.index" :key="item.index">
                        <i :class="item.icon"></i>
                        <span slot="title">{{ item.title }}</span>
                    </el-menu-item>
                </template>
            </template>
        </el-menu>
    </div>
</template>

<script>
import bus from '../common/bus';
export default {
    data() {
        return {
            collapse: false,
            items: [
                {
                    icon: 'el-icon-grape',
                    index: '1',
                    title: 'Physics',
                    subs: [
                        {
                            index: '1-1',
                            title: 'Astrophysics'
                        },
                        {
                            index: '1-2',
                            title: 'Condensed Matter',
                            
                        },
                        {
                            index: '1-3',
                            title: 'General Relativity and Quantum Cosmology'
                        },
                        {
                            index: '1-4',
                            title: 'High Energy Physics - Experiment',
                            
                        },
                        {
                            index: '1-5',
                            title: 'High Energy Physics - Lattice',
                            
                        },
                        {
                            index: '1-6',
                            title: 'High Energy Physics - Phenomenology',
                            
                        },
                        {
                            index: '1-7',
                            title: 'High Energy Physics - Theory',
                            
                        },
                        {
                            index: '1-8',
                            title: 'Mathematical Physics',
                            
                        },
                        {
                            index: '1-9',
                            title: 'Nonlinear Sciences',
                            
                        },
                        {
                            index: '1-10',
                            title: 'Nuclear Experiment',
                            
                        },
                        {
                            index: '1-11',
                            title: 'Nuclear Theory',
                            
                        },
                        {
                            index: '1-12',
                            title: 'Physics',
                            
                        },
                        {
                            index: '1-13',
                            title: 'Quantum Physics',
                            
                        },
                    ]
                },
                {
                    icon: 'el-icon-watermelon',
                    index: '2',
                    title: 'Mathematics'
                },
                {
                    icon: 'el-icon-cherry',
                    index: '3',
                    title: 'Computer Science',
                    subs: [
                        {
                            index: '3-1',
                            title: 'Computing Research Repository'
                        }
                    ]
                },
                {
                    icon: 'el-icon-apple',
                    index: '4',
                    title: 'Quantitative Biology'
                    
                },
                {
                    icon: 'el-icon-pear',
                    index: '5',
                    title: 'Quantitative Finance'
                },
                {
                    icon: 'el-icon-orange',
                    index: '6',
                    title: 'Statistics'
                },
                {
                    icon: 'el-icon-lollipop',
                    index: '7',
                    title: 'Electrical Engineering and Systems Science'
                },
                {
                    icon: 'el-icon-sugar',
                    index: '8',
                    title: 'Economics'
                }
                
            ]
        };
    },
    computed: {
        onRoutes() {
            return this.$route.path.replace('/', '');
        }
    },
    created() {
        // 通过 Event Bus 进行组件间通信，来折叠侧边栏
        bus.$on('collapse', msg => {
            this.collapse = msg;
            bus.$emit('collapse-content', msg);
        });
    }
};
</script>

<style scoped>
.sidebar {
    display: block;
    position: absolute;
    left: 0;
    top: 70px;
    bottom: 0;
    overflow-y: scroll;
    z-index:50;
    float: left;
}
.sidebar::-webkit-scrollbar {
    width: 0;
}
.sidebar-el-menu:not(.el-menu--collapse) {
    width: 350px;
}
.sidebar > ul {
    height: 100%;
}
</style>
