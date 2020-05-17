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
                            title: 'Astrophysics',
							subs:[
							{
								index:'search?m=4&&k=astro-ph.GA',
								title:' Astrophysics of Galaxies'
							},					
							{
								index:'search?m=4&&k=astro-ph.CO',
								title:'Cosmology and Nongalactic Astrophysics'
							},
							{
								index:'search?m=4&&k=astro-ph.EP',
								title:'Earth and Planetary Astrophysics'
							},
							{
								index:'search?m=4&&k=astro-ph.HE',
								title:'High Energy Astrophysical Phenomena'
							},
							{
								index:'search?m=4&&k=astro-ph.IM',
								title:'Instrumentation and Methods for Astrophysics'
							},
							{
								index:'search?m=4&&k=astro-ph.SR',
								title:'Solar and Stellar Astrophysics'
							},
							]
                        },
                        {
                            index: 'search?m=4&&k=cond-mat',
                            title: 'Condensed Matter',
                            subs:[
							{
								index:'search?m=4&&k=cond-mat.dis-nn',
								title:'Disordered Systems and Neural Network'
							},					
							{
								index:'search?m=4&&k=cond-mat.mes-hall',
								title:'Mesoscale and Nanoscale Physics'
							},
							{
								index:'search?m=4&&k=cond-mat.other',
								title:'Other Condensed Matter'
							},
							{
								index:'search?m=4&&k=cond-mat.quant-gas',
								title:' Quantum Gases'
							},
							{
								index:'search?m=4&&k=cond-mat.soft',
								title:' Soft Condensed Matter'
							},
							{
								index:'search?m=4&&k=cond-mat.stat-mech',
								title:' Statistical Mechanics'
							},
							{
								index:'search?m=4&&k=cond-mat.str-el',
								title:' Strongly Correlated Electrons'
							},
							{
								index:'search?m=4&&k=cond-mat.supr-con',
								title:' Superconductivity'
							},
							]
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
							 subs:[
							{
								index:'search?m=4&&k=nlin.AO',
								title:'Adaptation and Self-Organizing Systems'
							},					
							{
								index:'search?m=4&&k=nlin.CG',
								title:'Cellular Automata and Lattice Gases'
							},
							{
								index:'search?m=4&&k=nlin.CD',
								title:'Chaotic Dynamics'
							},
							{
								index:'search?m=4&&k=nlin.SI',
								title:'Exactly Solvable and Integrable Systems'
							},
							{
								index:'search?m=4&&k=nlin.PS',
								title:'Pattern Formation and Solitons'
							},
							]
                            
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
                            subs:[
							{
								index:'search?m=4&&k=physics.acc-ph',
								title:'Accelerator Physics'
							},					
							{
								index:'search?m=4&&k=physics.app-ph',
								title:'Applied Physics'
							},
							{
								index:'search?m=4&&k=physics.ao-ph',
								title:'Atmospheric and Oceanic Physics'
							},
							{
								index:'search?m=4&&k=physics.atom-ph',
								title:'Atomic Physics'
							},
							{
								index:'search?m=4&&k=physics.atm-clus',
								title:'Atomic and Molecular Clusters'
							},
							{
								index:'search?m=4&&k=physics.bio-ph',
								title:'Biological Physics'
							},					
							{
								index:'search?m=4&&k=physics.chem-ph',
								title:'Chemical Physics'
							},
							{
								index:'search?m=4&&k=physics.class-ph',
								title:'Classical Physics'
							},
							{
								index:'search?m=4&&k=physics.comp-ph',
								title:'Computational Physics'
							},
							{
								index:'search?m=4&&k=physics.data-an',
								title:'Data Analysis, Statistics and Probability'
							},
							{
								index:'search?m=4&&k=physics.flu-dyn',
								title:'Fluid Dynamics'
							},
							{
								index:'search?m=4&&k=physics.gen-ph',
								title:'General Physics'
							},					
							{
								index:'search?m=4&&k=physics.geo-ph',
								title:'Geophysics'
							},
							{
								index:'search?m=4&&k=physics.hist-ph',
								title:'History and Philosophy of Physics'
							},
							{
								index:'search?m=4&&k=physics.ins-det ',
								title:'Instrumentation and Detectors'
							},
							{
								index:'search?m=4&&k=physics.med-ph',
								title:'Medical Physics'
							},
							{
								index:'search?m=4&&k=physics.optics',
								title:'Optics'
							},
							{
								index:'search?m=4&&k=physics.ed-ph',
								title:'Physics Education'
							},
							{
								index:'search?m=4&&k=physics.soc-ph',
								title:'Physics and Society'
							},
							{
								index:'search?m=4&&k=physics.plasm-ph',
								title:'Plasma Physics'
							},					
							{
								index:'search?m=4&&k=physics.pop-ph',
								title:'Popular Physics'
							},
							{
								index:'search?m=4&&k=physics.space-ph',
								title:'Space Physics'
							},
							]
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
                    title: 'Mathematics',
					subs:[
					{
                            index:'search?m=4&&k=math.AG ',
                            title: 'Algebraic Geometry'
                    },
					{
                            index:'search?m=4&&k=math.AT ',
                            title: 'Algebraic Topology'
                    },
					{
                            index:'search?m=4&&k=math.AP ',
                            title: 'Analysis of PDEs'
                    },
					{
                            index:'search?m=4&&k=math.CT  ',
                            title: 'Category Theory'
                    },
					{
                            index:'search?m=4&&k=math.CA ',
                            title: 'Classical Analysis and ODEs'
                    },
					{
                            index:'search?m=4&&k=math.CO ',
                            title: 'Combinatorics'
                    },
					{
                            index:'search?m=4&&k=math.AC ',
                            title: 'Commutative Algebra'
                    },
					{
                            index:'search?m=4&&k=math.CV ',
                            title: 'Complex Variables'
                    },
					{
                            index:'search?m=4&&k=math.DG ',
                            title: 'Differential Geometry'
                    },
					{
                            index:'search?m=4&&k=math.DS ',
                            title: 'Dynamical Systems'
                    },
					{
                            index:'search?m=4&&k=math.FA ',
                            title: 'Functional Analysis'
                    },
					{
                            index:'search?m=4&&k=math.GM ',
                            title: 'General Mathematics'
                    },
					{
                            index:'search?m=4&&k=math.GN ',
                            title: 'General Topology '
                    },
					{
                            index:'search?m=4&&k=math.GT ',
                            title: 'Geometric Topology'
                    },
					{
                            index:'search?m=4&&k=math.GR ',
                            title: 'Group Theory'
                    },
					{
                            index:'search?m=4&&k=math.HO ',
                            title: 'History and Overview'
                    },
					{
                            index:'search?m=4&&k=math.IT ',
                            title: 'Information Theory'
                    },
					{
                            index:'search?m=4&&k=math.KT ',
                            title: 'K-Theory and Homology'
                    },
					{
                            index:'search?m=4&&k=math.LO ',
                            title: 'Logic'
                    },
					{
                            index:'search?m=4&&k=math.MP ',
                            title: 'Mathematical Physics'
                    },
					{
                            index:'search?m=4&&k=math.MG ',
                            title: 'Metric Geometry'
                    },
					{
                            index:'search?m=4&&k=math.NT ',
                            title: 'Number Theory'
                    },
					{
                            index:'search?m=4&&k=math.NA ',
                            title: 'Numerical Analysis'
                    },
					{
                            index:'search?m=4&&k=math.OA ',
                            title: 'Operator Algebras'
                    },
					{
                            index:'search?m=4&&k=math.OC ',
                            title: 'Optimization and Control'
                    },
					{
                            index:'search?m=4&&k=math.PR ',
                            title: ' Probability'
                    },
					{
                            index:'search?m=4&&k=math.QA ',
                            title: 'Quantum Algebra'
                    },
					{
                            index:'search?m=4&&k=math.RT ',
                            title: 'Representation Theory'
                    },
					{
                            index:'search?m=4&&k=math.RA ',
                            title: 'Rings and Algebras'
                    },
					{
                            index:'search?m=4&&k=math.SP ',
                            title: 'Spectral Theory'
                    },
					{
                            index:'search?m=4&&k=math.ST ',
                            title: 'Statistics Theory'
                    },
					{
                            index:'search?m=4&&k=math.SG ',
                            title: 'Symplectic Geometry'
                    },
					]
                },
                {
                    icon: 'el-icon-cherry',
                    index: 'search?m=4&&k=Computer Science',
                    title: 'Computer Science',
                    subs: [
                        {
                            index:'search?m=4&&k=CoRR.AI ',
                            title: 'Computing Research Repository',
							 subs:[
							 {
								index:'search?m=4&&k=cs.AI',
								title:'Artificial Intelligence'
							},
							{
								index:'search?m=4&&k=cs.CL',
								title:'Computation and Language'
							},
							{
								index:'search?m=4&&k=cs.CC',
								title:'Computational Complexity'
							},
							{
								index:'search?m=4&&k=cs.CE',
								title:'Computational Engineering, Finance, and Science'
							},
							{
								index:'search?m=4&&k=cs.CG',
								title:'Computational Geometry'
							},
							{
								index:'search?m=4&&k=cs.GT',
								title:'Computer Science and Game Theory'
							},
							{
								index:'search?m=4&&k=cs.CV',
								title:'Computer Vision and Pattern Recognition'
							},
							{
								index:'search?m=4&&k=cs.CY',
								title:'Computers and Society'
							},
							{
								index:'search?m=4&&k=cs.CR',
								title:'Cryptography and Security'
							},
							{
								index:'search?m=4&&k=cs.DS',
								title:'Data Structures and Algorithms'
							},
							{
								index:'search?m=4&&k=cs.DB',
								title:'Databases'
							},
							{
								index:'search?m=4&&k=cs.DL',
								title:'Digital Libraries'
							},
							{
								index:'search?m=4&&k=cs.DM',
								title:'Discrete Mathematics'
							},
							{
								index:'search?m=4&&k=cs.DC',
								title:'Distributed, Parallel, and Cluster Computing'
							},
							{
								index:'search?m=4&&k=cs.ET',
								title:'Emerging Technologies'
							},
							{
								index:'search?m=4&&k=cs.FL',
								title:'Formal Languages and Automata Theory'
							},
							{
								index:'search?m=4&&k=cs.GL',
								title:'General Literature'
							},
							{
								index:'search?m=4&&k=cs.GR',
								title:'Graphics'
							},
							{
								index:'search?m=4&&k=cs.AR',
								title:'Hardware Architecture'
							},
							{
								index:'search?m=4&&k=cs.HC',
								title:'Human-Computer Interaction'
							},
							{
								index:'search?m=4&&k=cs.IR',
								title:'Information Retrieval'
							},
							{
								index:'search?m=4&&k=cs.IT',
								title:'Information Theory'
							},
							{
								index:'search?m=4&&k=cs.LO',
								title:'Logic in Computer Science'
							},
							{
								index:'search?m=4&&k=cs.LG',
								title:'Machine Learning'
							},
							{
								index:'search?m=4&&k=cs.MS',
								title:'Mathematical Software'
							},
							{
								index:'search?m=4&&k=cs.MA',
								title:'Multiagent Systems'
							},
							{
								index:'search?m=4&&k=cs.MM',
								title:' Multimedia'
							},
							{
								index:'search?m=4&&k=cs.NI',
								title:' Networking and Internet Architecture'
							},
							{
								index:'search?m=4&&k=cs.NE',
								title:'Neural and Evolutionary Computing'
							},
							{
								index:'search?m=4&&k=cs.NA',
								title:'Numerical Analysis'
							},
							{
								index:'search?m=4&&k=cs.OS',
								title:'Operating Systems'
							},
							{
								index:'search?m=4&&k=cs.OH',
								title:'Other Computer Science'
							},
							{
								index:'search?m=4&&k=cs.PF',
								title:'Performance'
							},
							{
								index:'search?m=4&&k=cs.PL',
								title:'Programming Languages'
							},
							{
								index:'search?m=4&&k=cs.RO',
								title:'Robotics'
							},
							{
								index:'search?m=4&&k=cs.SI',
								title:'Social and Information Networks'
							},
							{
								index:'search?m=4&&k=cs.SE',
								title:'Software Engineering'
							},
							{
								index:'search?m=4&&k=cs.SD',
								title:' Sound'
							},
							{
								index:'search?m=4&&k=cs.SC',
								title:' Symbolic Computation'
							},
							{
								index:'search?m=4&&k=cs.SY',
								title:'Systems and Control'
							},
							]
                        },
                    ]
                },
                {
                    icon: 'el-icon-apple',
                    index: 'search?m=4&&k=q-bio',
                    title: 'Quantitative Biology',
                    subs:[
						{
                            index:'search?m=4&&k=q-bio.BM ',
                            title: 'Biomolecules'
                        },
						{
                            index:'search?m=4&&k=q-bio.CB ',
                            title: 'Cell Behavior'
                        },
						{
                            index:'search?m=4&&k=q-bio.GN ',
                            title: 'Genomics'
                        },
						{
                            index:'search?m=4&&k=q-bio.MN ',
                            title: 'Molecular Networks'
                        },
						{
                            index:'search?m=4&&k=q-bio.NC ',
                            title: 'Neurons and Cognition '
                        },
						{
                            index:'search?m=4&&k=q-bio.OT ',
                            title: ' Other Quantitative Biology'
                        },
						{
                            index:'search?m=4&&k=q-bio.PE ',
                            title: 'Populations and Evolution'
                        },
						{
                            index:'search?m=4&&k=q-bio.QM ',
                            title: 'Quantitative Methods'
                        },
						{
                            index:'search?m=4&&k=q-bio.SC ',
                            title: 'Subcellular Processes'
                        },
						{
                            index:'search?m=4&&k=q-bio.TO ',
                            title: 'Tissues and Organs'
                        },
					]
                },
                {
                    icon: 'el-icon-pear',
                    index: 'search?m=4&&k=q-fin',
                    title: 'Quantitative Finance',
					subs:[
					{
                            index: 'search?m=4&&k=q-fin.CP',
                            title: 'Computational Finance',                            
                    },
					{
                            index: 'search?m=4&&k=q-fin.EC',
                            title: 'Economics',                            
                    },
					{
                            index: 'search?m=4&&k=q-fin.GN',
                            title: 'General Finance',                            
                    },
					{
                            index: 'search?m=4&&k=q-fin.MF',
                            title: 'Mathematical Finance',                            
                    },
					{
                            index: 'search?m=4&&k=q-fin.PM',
                            title: 'Portfolio Management',                            
                    },
					{
                            index: 'search?m=4&&k=q-fin.PR',
                            title: 'Pricing of Securities',                            
                    },
					{
                            index: 'search?m=4&&k=q-fin.RM',
                            title: 'Risk Management',                            
                    },
					{
                            index: 'search?m=4&&k=q-fin.ST',
                            title: 'Statistical Finance',                            
                    },
					{
                            index: 'search?m=4&&k=q-fin.TR',
                            title: 'Trading and Market Microstructure',                            
                    },
					]
                },
                {
                    icon: 'el-icon-orange',
                    index: 'search?m=4&&k=stat',
                    title: 'Statistics',
					subs:[
					{
                            index: 'search?m=4&&k=stat.AP',
                            title: 'Applications',                            
                    },
					{
                            index: 'search?m=4&&k=stat.CO',
                            title: 'Computation',                            
                    },
					{
                            index: 'search?m=4&&k=stat.ML',
                            title: 'Machine Learning',                            
                    },
					{
                            index: 'search?m=4&&k=stat.ME',
                            title: 'Methodology',                            
                    },
					{
                            index: 'search?m=4&&k=stat.OT',
                            title: 'Other Statistics',                            
                    },
					{
                            index: 'search?m=4&&k=stat.TH',
                            title: 'Statistics Theory',                            
                    },
					]
                },
                {
                    icon: 'el-icon-lollipop',
                    index: 'search?m=4&&k=eess',
                    title: 'Electrical Engineering and Systems Science',
					subs:[
					{
                            index: 'search?m=4&&k=eess.ASP',
                            title: ' Audio and Speech Processing',                            
                    },
					{
                            index: 'search?m=4&&k=eess.IV',
                            title: 'Image and Video Processing',                            
                    },
					{
                            index: 'search?m=4&&k=eess.SP',
                            title: 'Signal Processing',                            
                    },
					{
                            index: 'search?m=4&&k=eess.SY',
                            title: 'Systems and Control',                            
                    },
					]
                },
                {
                    icon: 'el-icon-sugar',
                    index: 'search?m=4&&k=econ',
                    title: 'Economics',
					subs:[
					{
                            index: 'search?m=4&&k=econ.EM',
                            title: 'Econometrics',                            
                    },
					{
                            index: 'search?m=4&&k=econ.GN',
                            title: 'General Economics',                            
                    },
					{
                            index: 'search?m=4&&k=econ.TH',
                            title: 'Theoretical Economics',                            
                    },
					]
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
			/*
			var url=this.$url;
			var k=0;
			var L=url.length;
			while(k<L)
			{
				if (url[k]=='#')
				{
					k++;
					break;
				}
			}
			url=url.substring(0,k);
            return url;
			*/
			var pre=this.$route.path.replace('/','');
			//console.log(pre);
			return pre;
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
