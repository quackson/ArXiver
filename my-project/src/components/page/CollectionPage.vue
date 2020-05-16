<template>
  <div class="wrapper">
    <div style="margin-bottom: 20px;float:right;">
      <el-button @click="toggleSelection()">取消选择</el-button>
      <el-button type="danger" @click="deletePapers()">删除</el-button>
    </div>
    <el-table
      ref="collections"
      :data="
        tableData.slice((currentPage - 1) * pageSize, currentPage * pageSize)
      "
      height="100%"
      style="width: 100%;"
    >
      <el-table-column type="selection" width="55"> </el-table-column>
      <el-table-column prop="paper" label="收藏论文" style="width:20%">
        <template slot-scope="scope">
          <el-button type="text" @click="openDialog(scope.row)">{{
            scope.row.title
          }}</el-button>
        </template>
      </el-table-column>
      <el-table-column prop="author" label="作者" style="width:20%">
      </el-table-column>
      <el-table-column prop="summary" label="描述" show-overflow-tooltip>
      </el-table-column>
    </el-table>

    <div class="block">
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page.sync="currentPage"
        :page-size="pageSize"
        layout="prev, pager, next, jumper"
        :total="totalNum"
      >
      </el-pagination>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tableData: null,
	  username:'',
      currentPage: 1,
      pageSize: 8,
      totalNum: 100,
      toDelete: []
    };
  },
  methods: {
    ///分页    初始页currentPage、初始每页数据数pagesize和数据testpage
    handleSizeChange(val) {
      this.pageSize = val; //动态改变
    },
    handleCurrentChange(val) {
      this.currentPage = val; //动态改变
    },
    openDialog(paper) {
			console.log(`dash: ${paper.pdfLink}`);
		  this.$router.push({
          name: 'readpage',
          params: {url:paper.pdfLink,id:paper.id}
		  });
    },
    deletePapers(rows) {
		/*
		console.log(rows);
		if (rows) {
        rows.forEach(row => {
		var post_request = new FormData()
		post_request.append('userName', this.username)
		post_request.append('paperID', row.id)
		let _this = this;
		this.$http
        .request({
          url: _this.$url + '/cancelCollect',
          method: 'post',
          data: post_request,
          headers: { 'Content-Type': 'multipart/form-data' },
        })
        .then(function(response) {
          _this.$message({
              message: "取消收藏成功！",
              type: 'success',
          });
          console.log(response),		  
		  this.loadcollect()
        })
        .catch(function(response) {
          console.log(response)
        })
        });
		}		
		*/
	},
    toggleSelection(rows) {
      if (rows) {
        rows.forEach(row => {
          this.$refs.collections.toggleRowSelection(row);
        });
      } else {
        this.$refs.collections.clearSelection();
      }
    },
	loadcollect(){
	 this.username=localStorage.getItem('ms_username')
		//加载收藏夹列表		
      var post_request = new FormData()
      post_request.append('userName', this.username)
      this.$http
        .request({
          url: this.$url + '/getUserInformation',
          method: 'post',
          data: post_request,
          headers: { 'Content-Type': 'multipart/form-data' },
        })
        .then((response) => {
          console.log(response.data.userInfo.collectList)
          this.tableData= response.data.userInfo.collectList,
		  this.totalNum=response.data.userInfo.collectList.length
        })
        .catch(function(response) {
          console.log(response)
        })
	 
	}
  },
  created() {
		this.loadcollect();
  }
};
</script>

<style scoped>
.el-row {
  top: 100px;
  bottom: 70px;
  left: 400px;
  right: 0px;
  overflow-y: scroll;
  position: absolute;
  z-index: 1;
}
.el-row ::-webkit-scrollbar {
    width: 0;
}
.el-row  > ul {
    height: 100%;
}
.block {
  bottom: 0px;
  left: 50%;
  position: fixed;
  z-index: 1;
}
</style>
