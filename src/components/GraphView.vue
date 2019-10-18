<template>
  <v-container>
      <div class="graph-page">
        <d3-network :net-nodes="nodes" :net-links="links" :options="options"></d3-network>
      </div>
      <div class="filter-box">
      </div>
  </v-container>
</template>

<script>
import D3Network from 'vue-d3-network'
export default {
  data () {
    return {
      nodes: [
        { id: 1, name: 'Name1' },
        { id: 2, name: 'Name2' },
        { id: 3, _color: 'orange'},
        { id: 4 },
        { id: 5 },
        { id: 6 },
        { id: 7 },
        { id: 8 },
        { id: 9 }
      ],
      links: [
        { sid: 1, tid: 2, _color:'red' },
        { sid: 2, tid: 8, _color:'f0f' },
        { sid: 3, tid: 4, _color:'rebeccapurple' },
        { sid: 4, tid: 5 },
        { sid: 5, tid: 6 },
        { sid: 7, tid: 8 },
        { sid: 5, tid: 8 },
        { sid: 3, tid: 8 },
        { sid: 7, tid: 9 },
        { sid: 9, tid: 5 },
        { sid: 6, tid: 4 },

        

      ],
      options:
      {
        force: 3000,
        nodeSize: 20,
        nodeLabels: true,
        linkWidth:5
      }
    }
  },
components: {
    D3Network
  }
};
</script>
