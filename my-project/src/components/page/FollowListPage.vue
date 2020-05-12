<template>
  <div class="wrapper">
    <div>
      <el-tree
        class="follow-list"
        :props="props"
        :data="data"
        ref="area"
        default-expand-all
        node-key="id"
        show-checkbox
      >
      </el-tree>
    </div>
    <el-button type="primary" class="center" @click="handleCheckChange()" style="margin-top:50px">保存关注</el-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      checked: [],
      props: {
        label: 'name',
        children: 'children',
      },
      data: [
        {
          name: 'Physics',
          id: 21,
          children: [
            {
              id: 1,
              name: 'Astrophysics',
            },
            {
              id: 2,
              name: 'Condensed Matter',
            },
            {
              id: 3,
              name: 'General Relativity and Quantum Cosmology',
            },
            {
              id: 4,
              name: 'High Energy Physics - Experiment',
            },
            {
              id: 5,
              name: 'High Energy Physics - Lattice',
            },
            {
              id: 6,
              name: 'High Energy Physics - Phenomenology',
            },
            {
              id: 7,
              name: 'High Energy Physics - Theory',
            },
            {
              id: 8,
              name: 'Mathematical Physics',
            },
            {
              id: 9,
              name: 'Nonlinear Sciences',
            },
            {
              id: 10,
              name: 'Nuclear Experiment',
            },
            {
              id: 11,
              name: 'Nuclear Theory',
            },
            {
              id: 12,
              name: 'Physics',
            },
            {
              id: 13,
              name: 'Quantum Physics',
            },
          ],
        },
        { name: 'Mathematics', id: 14 },
        { name: 'Computer Science', id: 22, children: [{ name: 'Computing Research Repository', id: 15 }] },
        { name: 'Quantitative Biology', id: 16 },
        { name: 'Quantitative Finance', id: 17 },
        { name: 'Statistics', id: 18 },
        { name: 'Electrical Engineering and Systems Science', id: 19 },
        { name: 'Economics', id: 20 },
      ],
    }
  },
  created: function() {
    this.loadFollowing()
  },
  methods: {
    loadFollowing() {
      let userName = localStorage.getItem('ms_username')
      var post_request = new FormData()
      post_request.append('userName', userName)
      this.$http
        .request({
          url: this.$url + '/getUserInformation',
          method: 'post',
          data: post_request,
          headers: { 'Content-Type': 'multipart/form-data' },
        })
        .then((response) => {
          console.log(response)
          let list = response.data.userInfo.focusList
          list.forEach((element) => {
            var temp = parseInt(element)
            if (temp <= 20 && temp >= 1) {
              this.checked.push(temp)
            }
          })
          this.setCheckedKeys()
        })
        .catch((response) => {
          console.log(response)
          this.$notify.error({
            title: '错误',
            message: '关注列表加载失败',
          })
        })
    },
    handleCheckChange(data, checked, indeterminate) {
      this.getCheckedKeys()
      let userName = localStorage.getItem('ms_username')
      var post_request = new FormData()
      post_request.append('userName', userName)
      post_request.append('focusList', this.checked)
      this.$http
        .request({
          url: this.$url + '/addFocus',
          method: 'post',
          data: post_request,
          headers: { 'Content-Type': 'multipart/form-data' },
        })
        .then((response) => {
          console.log(response)
          this.$notify({
            title: '成功',
            message: '已修改关注列表',
            type: 'success',
          })
        })
        .catch((response) => {
          console.log(response)
          this.$notify.error({
            title: '错误',
            message: '关注失败',
          })
        })
    },
    getCheckedKeys() {
      this.checked = this.$refs.area.getCheckedKeys()
    },
    setCheckedKeys() {
      this.$refs.area.setCheckedKeys(this.checked)
    },
  },
}
</script>

<style>
.el-tree {
  display: inline-block;
  min-width: 100%;
}
.el-tree > .el-tree-node {
  padding: 5px;
}
.el-tree-node__label {
  font-size: 17px !important;
  font-family: Georgia;
}
.center {
  float: none;
  margin-left: auto;
  margin-right: auto;
  display: -webkit-box;
  -webkit-box-align: center;
  -webkit-box-pack: center;
}
</style>
