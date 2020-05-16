
<template>
<div>
<el-row :gutter="20">
<el-col :span="24">
	<el-table :data="tableData.slice((currentPage-1)*pageSize,currentPage*pageSize)"	
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
		username:'',
      }
    },	
   methods: {
        ///分页    初始页currentPage、初始每页数据数pagesize和数据testpage
	handleSizeChange(val) {
                   console.log(`每页 ${val} 条`);
                   this.pageSize = val;    //动态改变
	},
     handleCurrentChange(val) {
                   console.log(`当前页: ${val}`);				   	  
				 this.currentPage = val;
    },
	openDialog (paper) {
		console.log(`dash: ${paper.pdfLink}`);
		  this.$router.push({
          name: 'readpage',
          params: {url:paper.pdfLink,id:paper.id}
		  });
		 },
		 getData(qstr){
				this.username='YourFather';
				let _this=this
				this.$http.request({
				  url:_this.$url + '/getRecommendation?user='+_this.username,
				  method:'get',
				}).then(function(response) {
				  _this.tableData = response.data.papers,
				  _this.totalNum= response.data.num,
				  console.log(_this.tableData)
				}).catch(function(error) {
				  console.log(error)
				});
		 },
   },
   watch: {
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
  bottom:0px;
  left: 50%;
  position:fixed;
  z-index:1;
}
</style>