<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <Autor :atr="autores"></Autor>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import Autor from '@/components/Autor.vue'
import axios from 'axios'

export default {
  name: 'home',
  components: {
    HelloWorld,
    Autor,
  },
  data() {
    return{
      autores: []
    }
  },
  mounted() {
    axios.get("http://localhost:8211/api/Autores/")
    .then(response => (this.autores = response.data))
    .catch(response => (console.log(response)))
  },
}
</script>
