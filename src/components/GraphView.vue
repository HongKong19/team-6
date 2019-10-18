<template>
  <v-container>
      <div class="graph-page">
        <div v-if="network1">
          <d3-network :net-nodes="nodes1" :net-links="links" :options="options"></d3-network>
        </div>
      </div>
  </v-container>
</template>

<script>
import D3Network from 'vue-d3-network'
export default {
  data () {
    return {
      nodes1: [
        { id: 1, name: 'John S' },
        { id: 2, name: 'Jack H' },
        { id: 3, name: 'Tim H', _color: 'orange'},
        { id: 4, name: 'Michelle O'},
        { id: 5, name: 'Sam W'},
        { id: 6, name: 'Sam T'},
        { id: 7, name: 'Kyle T'},
        { id: 8, name: 'Tanmay K'},
        { id: 9, name: 'Harry T'}
      ],
      links: [
        { sid: 1, tid: 2, _color:'red' },
        { sid: 2, tid: 8, _color:'yellow' },
        { sid: 3, tid: 4, _color:'green' },
        { sid: 4, tid: 5, _color:'red'},
        { sid: 5, tid: 6, _color:'yellow'},
        { sid: 7, tid: 8, _color:'red'},
        { sid: 5, tid: 8, _color:'green'},
        { sid: 3, tid: 8, _color:'red'},
        { sid: 7, tid: 9 },
        { sid: 9, tid: 5 },
        { sid: 6, tid: 4 },
      ],
      options:
      {
        force: 2000,
        nodeSize: 25,
        nodeLabels: true,
        linkWidth: 4
      },

      network1: true,
      network2: true,
      network3: true
    }
  },

components: {
    D3Network
  }
};
</script>
