
<template>
<div>
<el-row :gutter="20">
<el-col :span="24">
	<el-table :data="tableData.slice(0,pageSize)"	
					height="tableHeight"
                    style="width: 100%"
					>
        <el-table-column prop="title" label="推荐论文" width="400":show-overflow-tooltip="true">
			<template slot-scope="scope">
            <el-button type="text" 
			@click="openDialog(scope.row)"
			>
			{{ scope.row.title}}
			</el-button>
          </template>
        </el-table-column>
        <el-table-column prop="author" label="作者" width="200" :show-overflow-tooltip="true">
        </el-table-column>
        <el-table-column prop="summary" label="描述" show-overflow-tooltip>
        </el-table-column>
	</el-table>
	
    </el-col>
	
    </el-row>
	<div class="block">
		<el-pagination
		@size-change="handleSizeChange"
		@current-change="handleCurrentChange"
		:current-page.sync="currentPage"
		:page-size="pageSize"
		layout="prev, pager, next, jumper"
		:total="totalNum">
		</el-pagination>
	</div>
</div>
</template>


<script>
export default {
 data() {		
	    return {
        tableData:null,
		tableHeight: window.innerHeight  - 100,
        currentPage:1,
        pageSize:10,
		totalNum:100, 
		 k:'0',
		 m:'0',
		 way:'origin',
      }
    },	
   methods: {
        ///分页    初始页currentPage、初始每页数据数pagesize和数据testpage
	handleSizeChange(val) {
                   console.log(`每页 ${val} 条`);
                   this.pageSize = val;    //动态改变
	},
	changetable(page){
		var begin=(page-1)*this.pageSize;
				  //加载val页信息
		let _this=this
		this.$http.request({
				  url:_this.$url + '/searchPaper?method='+_this.way+'&query='+_this.k +'&maxNum='+_this.pageSize+'&start='+begin,
				  method:'get',
				}).then(function(response) {
				  _this.tableData = response.data.papers,
				  //console.log(begin),
				  //console.log(response.data.papers),
				  console.log(_this.tableData)
				}).catch(function(error) {
				  console.log(error)
				});
				
				//获取论文列表个数
				this.$http.request({
				  url:_this.$url + '/getPaperNum?method='+ _this.way+'&query='+_this.k ,
				  method:'get',
				}).then(function(response) {
					//console.log(response),
				   _this.totalNum=response.data.num,
				   console.log('获取论文列表个数'),
				   console.log(_this.totalNum)
				}).catch(function(error) {
				  console.log(error)
				});
	},
     handleCurrentChange(val) {
                   console.log(`当前页: ${val}`);				   	  
				 this.currentPage = val;
				//console.log(this.tabelData);
    },
	openDialog (paper) {
				//console.log("get!");
				//this.$router.push({path: '/readpage' });
		console.log(`dash: ${paper.pdfLink}`);
		  this.$router.push({
          name: 'readpage',
          params: {url:paper.pdfLink,id:paper.id}
		  });
		 },
		 getData(qstr){
				this.k='github';
				this.way='ti';
				//加载列表首页信息
				this.changetable(1);
		 },
   },
   watch: {
	currentPage(newv, oldv) {
		console.log("in watch");
		console.log(newv);
        this.changetable(newv);
		},
		
	},
	created(){
		this.tabelData=new Array(this.pageSize);
		this.getData(this.$route.query);
    },   
}
</script>
<style>
    .el-tooltip__popper{max-width:40%}
</style>
<style scoped>
.el-row {
	/*
  top:30px;
  bottom: 70px;
  right:0px;
  width:100%;
  position: absolute;
  z-index:1;
  */
  top:4%;
  bottom: 4%;
  right:0px;
  width:100%;
  position: absolute;  
  overflow-y: scroll;
  z-index:1;
}
.el-row ::-webkit-scrollbar {
    width: 0;
}
.el-row  > ul {
    height: 100%;
}
.block{
	/*
  bottom:0px;
  left: 800px;
  position:fixed;
  z-index:1;
  */
  bottom:0px;
  left: 50%;
  position:fixed;
  z-index:1;
}
</style>