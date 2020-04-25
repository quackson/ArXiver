<template>
  <div class="wrapper">
    <div>
      <el-tree class="follow-list"
        :props="props"
        :load="loadNode"
        lazy
        show-checkbox
        @check-change="handleCheckChange"
      >
      </el-tree>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      props: {
        label: "name",
        children: "zones",
        isLeaf: "leaf"
      },
      count: 1
    };
  },
  methods: {
    handleCheckChange(data, checked, indeterminate) {
      
    },
    loadNode(node, resolve) {
      if (node.level === 0) {
        return resolve([
          { name: "Physics" },
          { name: "Mathematics", leaf: true },
          { name: "Computer Science" },
          { name: "Quantitative Biology", leaf: true },
          { name: "Quantitative Finance", leaf: true },
          { name: "Statistics", leaf: true },
          { name: "Electrical Engineering and Systems Science", leaf: true },
          { name: "Economics", leaf: true }
        ]);
      }

      setTimeout(() => {
        var data;
        if (node.data.name === "Physics") {
          data = [
            {
              name: "Astrophysics",
              leaf: true
            },
            {
              name: "Condensed Matter",
              leaf: true
            },
            {
              name: "General Relativity and Quantum Cosmology",
              leaf: true
            },
            {
              name: "High Energy Physics - Experiment",
              leaf: true
            },
            {
              name: "High Energy Physics - Lattice",
              leaf: true
            },
            {
              name: "High Energy Physics - Phenomenology",
              leaf: true
            },
            {
              name: "High Energy Physics - Theory",
              leaf: true
            },
            {
              name: "Mathematical Physics",
              leaf: true
            },
            {
              name: "Nonlinear Sciences",
              leaf: true
            },
            {
              name: "Nuclear Experiment",
              leaf: true
            },
            {
              name: "Nuclear Theory",
              leaf: true
            },
            {
              name: "Physics",
              leaf: true
            },
            {
              name: "Quantum Physics",
              leaf: true
            }
          ];
        } else if (node.data.name === "Computer Science") {
          data = [{ name: "Computing Research Repository", leaf: true }];
        } else {
          data = [];
        }
        resolve(data);
      }, 500);
    }
  }
};
</script>

<style>
.el-tree{
  display: inline-block;
  min-width: 100%;
}
.el-tree>.el-tree-node{
  padding: 5px;
}
.el-tree-node__label{
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
