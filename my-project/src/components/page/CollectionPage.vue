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
          <el-button type="text" @click="openDialog">{{
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
    const test = {
      resCode: 200,
      len: 10,
      papers: [
        {
          author: "M. J. Graf/S. -K. Yip/J. A. Sauls/D. Rainer/",
          id: "http://arxiv.org/abs/cond-mat/9509046v1",
          updatedTime: "1995-09-08T22:35:56Z",
          title:
            "Electronic thermal conductivity and the Wiedemann-Franz law for\n  unconventional superconductors",
          summary:
            "  We use the quasiclassical theory of superconductivity to calculate the\nelectronic contribution to the thermal conductivity. The theory is formulated\nfor low temperatures when heat transport is limited by electron scattering from\nrandom defects and for superconductors with nodes in the order parameter. We\nshow that certain eigenvalues of the thermal conductivity tensor are universal\nat low temperature, $k_B T\\ll \\gamma$, where $\\gamma$ is the bandwidth of\nimpurity bound states in the superconducting phase. The components of the\nelectrical and thermal conductivity also obey a Wiedemann-Franz law with the\nLorenz ratio, $L(T)=\\kappa/\\sigma T$, given by the Sommerfeld value of\n$L_{\\!S}=({\\pi^2}/{3})(k_B/e)^2$ for $k_BT\\ll\\gamma$. For intermediate\ntemperatures the Lorenz ratio deviates significantly from $L_{\\!S}$, and is\nstrongly dependent on the scattering cross section, and qualitatively different\nfor resonant vs.\\ nonresonant scattering. We include comparisons with other\ntheoretical calculations and the thermal conductivity data for the high $T_c$\ncuprate and heavy fermion superconductors.\n",
          category: "cond-mat/supr-con/",
          doiLink: "http://dx.doi.org/10.1103/PhysRevB.53.15147",
          paperLink: "http://arxiv.org/abs/cond-mat/9509046v1",
          pdfLink: "http://arxiv.org/pdf/cond-mat/9509046v1"
        },
        {
          author: "Yu. A. Fadeyev/H. Le Coroller/D. Gillet/",
          id: "http://arxiv.org/abs/astro-ph/0206240v1",
          updatedTime: "2002-06-14T11:58:26Z",
          title:
            "The Structure of Radiative Shock Waves. IV. Effects of Electron Thermal\n  Conduction",
          summary:
            "  We considered the structure of steady-state radiative shock waves propagating\nin the partially ionized hydrogen gas with density rho1 = 1e-10 gm/cm^3 and\ntemperature 3000K <= T1 <= 8000K. The radiative shock wave models with electron\nthermal conduction in the vicinity of the viscous jump are compared with pure\nradiative models. The threshold shock wave velocity above of which effects of\nelectron thermal conduction become perceptible is of U1=70 km/s and corresponds\nto the upstream Mach numbers from M1= 6 at T1=8000K to M1=11 at T1=3000K. In\nshocks with efficient electron heat conduction more than a half of hydrogen\natoms are ionized in the radiative precursor, whereas behind the viscous jump\nthe hydrogen gas undergoes the full ionization. The existence of the electron\nconductive precursor leads to the enhancement of the Lyman continuum flux\ntrapped in the surroundings of the discontinuous jump. For upstream velocities\nranged within 70 km/s <= U1 <= 85 km/s the partially ionized hydrogen gas of\nthe radiative precursor undergoes the additional ionization (<= 5%), whereas\nthe total radiave flux emerging from the shock wave increases by 10% <=\ndelta(FRad) <= 25% .\n",
          category: "astro-ph/",
          doiLink: "http://dx.doi.org/10.1051/0004-6361:20020995",
          paperLink: "http://arxiv.org/abs/astro-ph/0206240v1",
          pdfLink: "http://arxiv.org/pdf/astro-ph/0206240v1"
        },
        {
          author: "Hiroaki Kusunose/T. M. Rice/Manfred Sigrist/",
          id: "http://arxiv.org/abs/cond-mat/0208113v2",
          updatedTime: "2002-08-06T13:43:12Z",
          title:
            "Electronic Thermal Conductivity of Multi-Gap Superconductors with\n  Application to MgB_2",
          summary:
            "  The remarkable field dependence of the electronic thermal conductivity\nobserved in MgB_2 can be explained as a consequence of multi-gap\nsuperconductivity. A key point is that for moderately clean samples, the mean\nfree path becomes comparable to coherence length of the smaller gap over its\nentire Fermi surface. In this case, quasiparticle excitations bound in vortex\ncores can easily be delocalized causing a rapid rise in the thermal\nconductivity at low magnetic fields. This feature is in marked contrast to that\nfor anisotropic or nodal gaps, where delocalization occurs only on part of the\nFermi surface.\n",
          category: "cond-mat.supr-con/",
          doiLink: "http://dx.doi.org/10.1103/PhysRevB.66.214503",
          paperLink: "http://arxiv.org/abs/cond-mat/0208113v2",
          pdfLink: "http://arxiv.org/pdf/cond-mat/0208113v2"
        },
        {
          author: "Roberto Raimondi/Giorgio Savona/Peter Schwab/Thomas Lueck/",
          id: "http://arxiv.org/abs/cond-mat/0402245v1",
          updatedTime: "2004-02-09T14:20:31Z",
          title: "Electronic thermal conductivity of disordered metals",
          summary:
            "  We calculate the thermal conductivity of interacting electrons in disordered\nmetals. In our analysis we point out that the interaction affects thermal\ntransport through two distinct mechanims, associated with quantum interference\ncorrections and energy exchange of the quasi particles with the electromagnetic\nenvironment, respectively. The latter is seen to lead to a violation of the\nWiedemann-Franz law. Our theory predicts a strong enhancement of the Lorenz\nratio $\\kappa /\\sigma T$ over the value which is predicted by the\nWiedemann-Franz law, when the electrons encounter a large environmental\nimpedance.\n",
          category: "cond-mat.mes-hall/",
          doiLink: "http://dx.doi.org/10.1103/PhysRevB.70.155109",
          paperLink: "http://arxiv.org/abs/cond-mat/0402245v1",
          pdfLink: "http://arxiv.org/pdf/cond-mat/0402245v1"
        },
        {
          author: "K. Vafayi/M. Calandra/O. Gunnarsson/",
          id: "http://arxiv.org/abs/cond-mat/0607634v1",
          updatedTime: "2006-07-25T15:27:59Z",
          title:
            "Electronic thermal conductivity at high temperatures: Violation of the\n  Wiedemann-Franz law in narrow band metals",
          summary:
            "  We study the electronic part of the thermal conductivity kappa of metals. We\npresent two methods for calculating kappa, a quantum Monte-Carlo (QMC) method\nand a method where the phonons but not the electrons are treated\nsemiclassically (SC). We compare the two methods for a model of alkali-doped\nC60, A3C60, and show that they agree well. We then mainly use the SC method,\nwhich is simpler and easier to interpret. We perform SC calculations for Nb for\nlarge temperatures T and find that kappa increases with T as kappa(T)=a+bT,\nwhere a and b are constants, consistent with a saturation of the mean free\npath, l, and in good agreement with experiment. In contrast, we find that for\nA3C60, kappa(T) decreases with T for very large T. We discuss the reason for\nthis qualitatively in the limit of large T. We give a quantum-mechanical\nexplanation of the saturation of l for Nb and derive the Wiedemann-Franz law in\nthe limit of T much smaller than W, where W is the band width. In contrast, due\nto the small W of A3C60, the assumption T much smaller than W can be violated.\nWe show that this leads to kappa(T) \\sim T^{-3/2} for very large T and a strong\nviolation of the Wiedemann-Franz law.\n",
          category: "cond-mat.mtrl-sci/",
          doiLink: "http://dx.doi.org/10.1103/PhysRevB.74.235116",
          paperLink: "http://arxiv.org/abs/cond-mat/0607634v1",
          pdfLink: "http://arxiv.org/pdf/cond-mat/0607634v1"
        },
        {
          author: "P. S. Shternin/D. G. Yakovlev/",
          id: "http://arxiv.org/abs/astro-ph/0608371v1",
          updatedTime: "2006-08-17T14:05:46Z",
          title:
            "Electron thermal conductivity owing to collisions between degenerate\n  electrons",
          summary:
            "  We calculate the thermal conductivity of electrons produced by\nelectron-electron Coulomb scattering in a strongly degenerate electron gas\ntaking into account the Landau damping of transverse plasmons. The Landau\ndamping strongly reduces this conductivity in the domain of ultrarelativistic\nelectrons at temperatures below the electron plasma temperature. In the inner\ncrust of a neutron star at temperatures T < 1e7 K this thermal conductivity\ncompletely dominates over the electron conductivity due to electron-ion\n(electron-phonon) scattering and becomes competitive with the the electron\nconductivity due to scattering of electrons by impurity ions.\n",
          category: "astro-ph/",
          doiLink: "http://dx.doi.org/10.1103/PhysRevD.74.043004",
          paperLink: "http://arxiv.org/abs/astro-ph/0608371v1",
          pdfLink: "http://arxiv.org/pdf/astro-ph/0608371v1"
        },
        {
          author:
            "S. Yi\u011fen/V. Tayari/J. O. Island/J. M. Porter/A. R. Champagne/",
          id: "http://arxiv.org/abs/1303.2390v2",
          updatedTime: "2013-03-10T23:02:56Z",
          title:
            "Electronic Thermal Conductivity Measurements in Intrinsic Graphene",
          summary:
            "  The electronic thermal conductivity of graphene and 2D Dirac materials is of\nfundamental interest and can play an important role in the performance of\nnano-scale devices. We report the electronic thermal conductivity, $K_{e}$, in\nsuspended graphene in the nearly intrinsic regime over a temperature range of\n20 to 300 K. We present a method to extract $K_{e}$ using two-point DC electron\ntransport at low bias voltages, where the electron and lattice temperatures are\ndecoupled. We find $K_e$ ranging from 0.5 to 11 W/m.K over the studied\ntemperature range. The data are consistent with a model in which heat is\ncarried by quasiparticles with the same mean free-path and velocity as\ngraphene's charge carriers.\n",
          category: "cond-mat.mes-hall/cond-mat.mtrl-sci/",
          doiLink: "http://dx.doi.org/10.1103/PhysRevB.87.241411",
          paperLink: "http://arxiv.org/abs/1303.2390v2",
          pdfLink: "http://arxiv.org/pdf/1303.2390v2"
        },
        {
          author:
            "K. C. Fong/Emma Wollman/Harish Ravi/Wei Chen/Aash Clerk/M. D. Shaw/H. G. LeDuc/K. C. Schwab/",
          id: "http://arxiv.org/abs/1308.2265v1",
          updatedTime: "2013-08-10T02:04:59Z",
          title:
            "Measurement of the electronic thermal conductance channels and heat\n  capacity of graphene at low temperature",
          summary:
            "  The ability to transport energy is a fundamental property of the\ntwo-dimensional Dirac fermions in graphene. Electronic thermal transport in\nthis system is relatively unexplored and is expected to show unique fundamental\nproperties and to play an important role in future applications of graphene,\nincluding opto-electronics, plasmonics, and ultra-sensitive bolometry. Here we\npresent measurements of bipolar, electron-diffusion and electron-phonon thermal\nconductances, and infer the electronic specific heat, with a minimum value of\n10 $k_{\\rm{B}}$ ($10^{-22}$ JK$^{-1}$) per square micron. We test the validity\nof the Wiedemann-Franz law and find the Lorenz number equals\n$1.32\\times(\\pi^2/3)(k_{\\rm{B}}/e)^2$. The electron-phonon thermal conductance\nhas a temperature power law $T^2$ at high doping levels, and the coupling\nparameter is consistent with recent theory, indicating its enhancement by\nimpurity scattering. We demonstrate control of the thermal conductance by\nelectrical gating and by suppressing the diffusion channel using\nsuperconducting electrodes, which sets the stage for future graphene-based\nsingle microwave photon detection.\n",
          category: "cond-mat.mes-hall/",
          doiLink: null,
          paperLink: "http://arxiv.org/abs/1308.2265v1",
          pdfLink: "http://arxiv.org/pdf/1308.2265v1"
        },
        {
          author: "M. X. Chen/R. Podloucky/",
          id: "http://arxiv.org/abs/1212.0803v2",
          updatedTime: "2012-12-04T17:33:11Z",
          title:
            "Electronic thermal conductivity as derived by density functional theory",
          summary:
            "  Reliable evaluation of the lattice thermal conductivity is of importance for\noptimizing the figure-of-merit of thermoelectric materials. Traditionally, when\nderiving the phonon mediated thermal conductivity $\\kappa_{ph} = \\kappa -\n\\kappa_{el}$ from the measured total thermal conductivity $\\kappa$ the constant\nLorenz number $L_0$ of the Wiedemann-Franz law \\mbox{$\\mathbf{\\kappa_{el}}=T\nL_0 \\sigma$} is chosen. The present study demonstrates that this procedure is\nnot reliable when the Seebeck coefficient $|S|$ becomes large which is exactly\nthe case for a thermoelectric material of interest. Another approximation using\n$L_0-S^2$, which seem to work better for medium values of $S^2$ also fails when\n$S^2$ becomes large, as is the case when the system becomes\nsemiconducting/insulating. For a reliable estimation of $\\kappa_{el}$ it is\nproposed, that a full first-principles calculations by combining density\nfunctional theory with Boltzmann's transport theory has to be made. For the\npresent study such an approach was chosen for investigating the clathrate\ntype-I compound Ba$_8$Au$_{6-x}$Ge$_{40+x}$ for a series of dopings or\ncompositions $x$. For a doping of $0.8$ electrons corresponding to $x=0.27$ the\ncalculated temperature dependent Seebeck coefficient agrees well with recent\nexperiments corroborating the validity of the density functional theory\napproach.\n",
          category: "cond-mat.mtrl-sci/",
          doiLink: "http://dx.doi.org/10.1103/PhysRevB.88.045134",
          paperLink: "http://arxiv.org/abs/1212.0803v2",
          pdfLink: "http://arxiv.org/pdf/1212.0803v2"
        },
        {
          author: "V. V. Izmodenov/D. B. Alexashov/M. S. Ruderman/",
          id: "http://arxiv.org/abs/1409.8128v1",
          updatedTime: "2014-09-29T14:07:43Z",
          title:
            "Electron thermal conduction as a possible mechanism to make the inner\n  heliosheath thnner",
          summary:
            "  We show that the electron thermal conductivity may strongly affect the\nheliosheath plasma flow and the global pattern of the solar wind (SW)\ninteraction with the local interstellar medium (LISM). In particular, it leads\nto strong reduction of the inner heliosheath thickness that makes possible to\nexplain (qualitatively) why Voyager 1 (V1) has crossed the heliopause at\nunexpectedly small heliocentric distance of 122 AU. To estimate the effect of\nthermal conductivity we consider a limiting case when thermal conduction is\nvery effective. To do that we assume the plasma flow in the entire heliosphere\nis nearly isothermal.\n  Due to this effect, the heliospheric distance of the termination shock has\nincreased by about 15 AU in V1 direction compared to the adiabatic case with\ngamma = 5/3. The heliospheric distance of the heliopause has decreased by about\n27 AU. As a result, the thickness of the inner heliosheath in the model has\ndecreased by about 42 AU and become equal to 32 AU.\n",
          category: "astro-ph.SR/physics.space-ph/",
          doiLink: "http://dx.doi.org/10.1088/2041-8205/795/1/L7",
          paperLink: "http://arxiv.org/abs/1409.8128v1",
          pdfLink: "http://arxiv.org/pdf/1409.8128v1"
        }
      ]
    };
    return {
      tableData: test.papers,
      jsondata: test,
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
    openDialog() {
      this.$router.push({ path: "/readpage" });
    },
    deletePapers() {},
    toggleSelection(rows) {
      if (rows) {
        rows.forEach(row => {
          this.$refs.collections.toggleRowSelection(row);
        });
      } else {
        this.$refs.collections.clearSelection();
      }
    }
  },
  created() {
    for (var i = 0; i < this.tableData.length; i++) {
      if (this.tableData[i].summary.length > 1000) {
        this.tableData[i].summary = this.tableData[i].summary.slice(0, 100);
      }
    }
    this.totalNum = this.tableData.length;
  }
};
</script>

<style scoped>
.el-row {
  top: 100px;
  bottom: 70px;
  left: 400px;
  right: 0px;
  position: absolute;
  z-index: 1;
}
.block {
  bottom: 0px;
  left: 50%;
  position: fixed;
  z-index: 1;
}
</style>
