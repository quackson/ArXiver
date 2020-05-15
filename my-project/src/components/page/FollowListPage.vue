<template>
  <div class="wrapper">
    <div>
      <el-tree
        class="follow-list"
        :props="props"
        :data="data"
        ref="area"
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
      leaf_id: 0,
      not_leaf_id: 200,
      checked: [],
      props: {
        label: 'name',
        children: 'children',
      },
      data: [
        {
          name: 'Physics',
          id: 154,
          children: [
            {
              id: 155,
              name: 'Astrophysics',
              children: [
                {
                  id: 1,
                  name: 'Astrophysics of Galaxies',
                },
                {
                  id: 2,
                  name: 'Cosmology and Nongalactic Astrophysics',
                },
                {
                  id: 3,
                  name: 'Earth and Planetary Astrophysics',
                },
                {
                  id: 4,
                  name: 'High Energy Astrophysical Phenomena',
                },
                {
                  id: 5,
                  name: 'Instrumentation and Methods for Astrophysics',
                },
                {
                  id: 6,
                  name: 'Solar and Stellar Astrophysics',
                },
              ],
            },
            {
              id: 156,
              name: 'Condensed Matter',
              children: [
                {
                  id: 7,
                  name: 'Disordered Systems and Neural Network',
                },
                {
                  id: 8,
                  name: 'Mesoscale and Nanoscale Physics',
                },
                {
                  id: 9,
                  name: 'Other Condensed Matter',
                },
                {
                  id: 10,
                  name: 'Quantum Gases',
                },
                {
                  id: 11,
                  name: 'Soft Condensed Matter',
                },
                {
                  id: 12,
                  name: 'Statistical Mechanics',
                },
                {
                  id: 13,
                  name: 'Strongly Correlated Electrons',
                },
                {
                  id: 14,
                  name: 'Superconductivity',
                },
              ],
            },
            {
              id: 15,
              name: 'General Relativity and Quantum Cosmology',
            },
            {
              id: 16,
              name: 'High Energy Physics - Experiment',
            },
            {
              id: 17,
              name: 'High Energy Physics - Lattice',
            },
            {
              id: 18,
              name: 'High Energy Physics - Phenomenology',
            },
            {
              id: 19,
              name: 'High Energy Physics - Theory',
            },
            {
              id: 20,
              name: 'Mathematical Physics',
            },
            {
              id: 157,
              name: 'Nonlinear Sciences',
              children: [
                { id: 21, name: 'Adaptation and Self-Organizing Systems' },
                { id: 22, name: 'Cellular Automata and Lattice Gases' },
                { id: 23, name: 'Chaotic Dynamics' },
                { id: 24, name: 'Exactly Solvable and Integrable Systems' },
                { id: 25, name: 'Pattern Formation and Solitons' },
              ],
            },
            {
              id: 26,
              name: 'Nuclear Experiment',
            },
            {
              id: 27,
              name: 'Nuclear Theory',
            },
            {
              id: 158,
              name: 'Physics',
              children: [
                { id: 28, name: 'Accelerator Physics' },
                { id: 29, name: 'Applied Physics' },
                { id: 30, name: 'Atomic Physics' },
                { id: 31, name: 'Atomic and Molecular Clusters' },
                { id: 32, name: 'Biological Physics' },
                { id: 33, name: 'Chemical Physics' },
                { id: 34, name: 'Classical Physics' },
                { id: 35, name: 'Computational Physics' },
                { id: 36, name: 'Data Analysis, Statistics and Probability' },
                { id: 37, name: 'Fluid Dynamics' },
                { id: 38, name: 'General Physics' },
                { id: 39, name: 'Geophysics' },
                { id: 40, name: 'History and Philosophy of Physics' },
                { id: 41, name: 'Instrumentation and Detectors' },
                { id: 42, name: 'Medical Physics' },
                { id: 43, name: 'Optics' },
                { id: 44, name: 'Physics Education' },
                { id: 45, name: 'Physics and Society' },
                { id: 46, name: 'Plasma Physics' },
                { id: 47, name: 'Popular Physics' },
                { id: 48, name: 'Space Physics' },
              ],
            },
            {
              id: 49,
              name: 'Quantum Physics',
            },
          ],
        },
        {
          name: 'Mathematics',
          id: 159,
          children: [
            { id: 50, name: 'Algebraic Geometry' },
            { id: 51, name: 'Algebraic Topology' },
            { id: 52, name: 'Analysis of PDEs' },
            { id: 53, name: 'Category Theory' },
            { id: 54, name: 'Classical Analysis and ODEs' },
            { id: 55, name: 'Combinatorics' },
            { id: 56, name: 'Commutative Algebra' },
            { id: 57, name: 'Complex Variables' },
            { id: 58, name: 'Differential Geometry' },
            { id: 59, name: 'Dynamical Systems' },
            { id: 60, name: 'Functional Analysis' },
            { id: 61, name: 'General Mathematics' },
            { id: 62, name: 'General Topology ' },
            { id: 63, name: 'Geometric Topology' },
            { id: 64, name: 'Group Theory' },
            { id: 65, name: 'History and Overview' },
            { id: 66, name: 'Information Theory' },
            { id: 67, name: 'K-Theory and Homology' },
            { id: 68, name: 'Logic' },
            { id: 69, name: 'Mathematical Physics' },
            { id: 70, name: 'Metric Geometry' },
            { id: 71, name: 'Number Theory' },
            { id: 72, name: 'Numerical Analysis' },
            { id: 73, name: 'Operator Algebras' },
            { id: 74, name: 'Optimization and Control' },
            { id: 75, name: 'Probability' },
            { id: 76, name: 'Quantum Algebra' },
            { id: 77, name: 'Representation Theory' },
            { id: 78, name: 'Rings and Algebras' },
            { id: 79, name: 'Spectral Theory' },
            { id: 80, name: 'Statistics Theory' },
            { id: 81, name: 'Symplectic Geometry' },
          ],
        },
        {
          name: 'Computer Science',
          id: 160,
          children: [
            {
              name: 'Computing Research Repository',
              id: 161,
              children: [
                { id: 82, name: 'Artificial Intelligence' },
                { id: 83, name: 'Computation and Language' },
                { id: 84, name: 'Computational Complexity' },
                { id: 85, name: 'Computational Engineering, Finance, and Science' },
                { id: 86, name: 'Computational Geometry' },
                { id: 87, name: 'Computer Science and Game Theory' },
                { id: 88, name: 'Computer Vision and Pattern Recognition' },
                { id: 89, name: 'Computers and Society' },
                { id: 90, name: 'Cryptography and Security' },
                { id: 91, name: 'Data Structures and Algorithms' },
                { id: 92, name: 'Databases' },
                { id: 93, name: 'Digital Libraries' },
                { id: 94, name: 'Discrete Mathematics' },
                { id: 95, name: 'Distributed, Parallel, and Cluster Computing' },
                { id: 96, name: 'Emerging Technologies' },
                { id: 97, name: 'Formal Languages and Automata Theory' },
                { id: 98, name: 'General Literature' },
                { id: 99, name: 'Graphics' },
                { id: 100, name: 'Hardware Architecture' },
                { id: 101, name: 'Human-Computer Interaction' },
                { id: 102, name: 'Information Retrieval' },
                { id: 103, name: 'Information Theory' },
                { id: 104, name: 'Logic in Computer Science' },
                { id: 105, name: 'Machine Learning' },
                { id: 106, name: 'Mathematical Software' },
                { id: 107, name: 'Multiagent Systems' },
                { id: 108, name: 'Multimedia' },
                { id: 109, name: 'Networking and Internet Architecture' },
                { id: 110, name: 'Neural and Evolutionary Computing' },
                { id: 111, name: 'Numerical Analysis' },
                { id: 112, name: 'Operating Systems' },
                { id: 113, name: 'Other Computer Science' },
                { id: 114, name: 'Performance' },
                { id: 115, name: 'Programming Languages' },
                { id: 116, name: 'Robotics' },
                { id: 117, name: 'Social and Information Networks' },
                { id: 118, name: 'Software Engineering' },
                { id: 119, name: 'Sound' },
                { id: 120, name: 'Symbolic Computation' },
                { id: 121, name: 'Systems and Control' },
              ],
            },
          ],
        },
        {
          name: 'Quantitative Biology',
          id: 162,
          children: [
            { id: 122, name: 'Biomolecules' },
            { id: 123, name: 'Cell Behavior' },
            { id: 124, name: 'Genomics' },
            { id: 125, name: 'Molecular Networks' },
            { id: 126, name: 'Neurons and Cognition' },
            { id: 127, name: 'Other Quantitative Biology' },
            { id: 128, name: 'Populations and Evolution' },
            { id: 129, name: 'Quantitative Methods' },
            { id: 130, name: 'Subcellular Processes' },
            { id: 131, name: 'Tissues and Organs' },
          ],
        },
        {
          name: 'Quantitative Finance',
          id: 163,
          children: [
            { id: 132, name: 'Computational Finance' },
            { id: 133, name: 'Economics' },
            { id: 134, name: 'General Finance' },
            { id: 135, name: 'Mathematical Finance' },
            { id: 136, name: 'Portfolio Management' },
            { id: 137, name: 'Pricing of Securities' },
            { id: 138, name: 'Risk Management' },
            { id: 139, name: 'Statistical Finance' },
            { id: 140, name: 'Trading and Market Microstructure' },
          ],
        },
        {
          name: 'Statistics',
          id: 164,
          children: [
            { id: 141, name: 'Applications' },
            { id: 142, name: 'Computation' },
            { id: 143, name: 'Machine Learning' },
            { id: 144, name: 'Methodology' },
            { id: 145, name: 'Other Statistics' },
            { id: 146, name: 'Statistics Theory' },
          ],
        },
        {
          name: 'Electrical Engineering and Systems Science',
          id: 165,
          children: [
            { id: 147, name: 'Audio and Speech Processing' },
            { id: 148, name: 'Image and Video Processing' },
            { id: 149, name: 'Signal Processing' },
            { id: 150, name: 'Systems and Control' },
          ],
        },
        {
          name: 'Economics',
          id: 166,
          children: [
            { id: 151, name: 'Econometrics' },
            { id: 152, name: 'General Economics' },
            { id: 153, name: 'Theoretical Economics' },
          ],
        },
      ],
    }
  },
  created: function() {
    this.loadFollowing()
  },
  methods: {
    id_plus(isleaf) {
      if(isleaf===true){
        this.leaf_id++;
        return this.leaf_id;
      }
      else{
        this.not_leaf_id++;
        return this.not_leaf_id;
      }
    },
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
            if (temp <= 153 && temp >= 1) {
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
