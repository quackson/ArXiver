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
                    index: 'search?m=4&&k=Physics',
                    title: 'Physics',
                    subs: [
                        {
                            index: 'search?m=4&&k=astro-ph',
                            title: 'Astrophysics'
                        },
                        {
                            index: 'search?m=4&&k=cond-mat',
                            title: 'Condensed Matter',
                            
                        },
                        {
                            index: 'search?m=4&&k=gr-qc',
                            title: 'General Relativity and Quantum Cosmology'
                        },
                        {
                            index: 'search?m=4&&k=hep-ex',
                            title: 'High Energy Physics - Experiment',
                            
                        },
                        {
                            index: 'search?m=4&&k=hep-lat',
                            title: 'High Energy Physics - Lattice',
                            
                        },
                        {
                            index: 'search?m=4&&k=hep-ph',
                            title: 'High Energy Physics - Phenomenology',
                            
                        },
                        {
                            index: 'search?m=4&&k=hep-th',
                            title: 'High Energy Physics - Theory',
                            
                        },
                        {
                            index: 'search?m=4&&k=math-ph',
                            title: 'Mathematical Physics',
                            
                        },
                        {
                            index: 'search?m=4&&k=nlin',
                            title: 'Nonlinear Sciences',
                            
                        },
                        {
                            index: 'search?m=4&&k=nucl-ex',
                            title: 'Nuclear Experiment',
                            
                        },
                        {
                            index: 'search?m=4&&k=nucl-th',
                            title: 'Nuclear Theory',
                            
                        },
                        {
                            index: 'search?m=4&&k=physics',
                            title: 'Physics',
                            
                        },
                        {
                            index: 'search?m=4&&k=quant-ph',
                            title: 'Quantum Physics',
                            
                        },
                    ]
                },
                {
                    icon: 'el-icon-watermelon',
                    index: 'search?m=4&&k=math',
                    title: 'Mathematics'
                },
                {
                    icon: 'el-icon-cherry',
                    index: 'search?m=4&&k=Computer Science',
                    title: 'Computer Science',
                    subs: [
                        {
                            index:'search?m=4&&k=CoRR ',
                            title: 'Computing Research Repository'
                        }
                    ]
                },
                {
                    icon: 'el-icon-apple',
                    index: 'search?m=4&&k=q-bio',
                    title: 'Quantitative Biology'
                    
                },
                {
                    icon: 'el-icon-pear',
                    index: 'search?m=4&&k=q-fin',
                    title: 'Quantitative Finance'
                },
                {
                    icon: 'el-icon-orange',
                    index: 'search?m=4&&k=stat',
                    title: 'Statistics'
                },
                {
                    icon: 'el-icon-lollipop',
                    index: 'search?m=4&&k=eess',
                    title: 'Electrical Engineering and Systems Science'
                },
                {
                    icon: 'el-icon-sugar',
                    index: 'search?m=4&&k=econ',
                    title: 'Economics'
                }
                
            ]
        };
    },
	methods: {
		/*
		search_cat(e){
			//console.log(e.target);
			//console.log(e.currentTarget.getElementById("string"));
			console(e);
			var category=e;
				
		},		
		*/
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
