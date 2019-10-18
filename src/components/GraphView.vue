<template>
  <v-container>
      <div class="graph-page">
        <div v-if="network1">
          <d3-network :net-nodes="nodes1" :net-links="links" :options="options"></d3-network>
        </div>
        <div v-if="network2">
          <d3-network :net-nodes="nodes2" :net-links="links" :options="options"></d3-network>
        </div>
        <div v-if="network3">
          <d3-network :net-nodes="nodes3" :net-links="links" :options="options"></d3-network>
        </div>
      </div>

      <button class="btn btn-main " v-on:click="network1">
          View Profile
      </button>
      <button class="btn btn-main " v-on:click="network2">
          View Profile
      </button>
      <button class="btn btn-main " v-on:click="network3">
        View Profile
      </button>
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
        { id: 4 },
        { id: 5 },
        { id: 6 },
        { id: 7 },
        { id: 8 },
        { id: 9 }
      ],
            nodes2: [
        { id: 1, name: 'John S' },
        { id: 2, name: 'Jack H' },
        { id: 3, name: 'Tim H', _color: 'orange'},
        { id: 4 },
        { id: 5 },
        { id: 6 },
        { id: 7 },
        { id: 8 },
        { id: 9 }
      ],
            nodes3: [
        { id: 1, name: 'John S' },
        { id: 2, name: 'Jack H' },
        { id: 3, name: 'Tim H', _color: 'orange'},
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
      },
      
      network1: true,
      network2: false,
      network3: false
    }
  },
  methods: {
    network1: function() {
      network1= true,
      network2= false,
      network3= false
    },
    network2: function() {
      network1= false,
      network2= true,
      network3= false
    },
    network3: function() {
      network1= false,
      network2= false,
      network3= true
    }
  },
components: {
    D3Network
  }
};
</script>
