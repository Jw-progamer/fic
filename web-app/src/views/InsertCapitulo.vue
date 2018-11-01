<template>
    <div>
        <b-jumbotron header="historia.titulo" lead="Use este formulario para inserir um novo capitulo">
<p>Todas as informaoes sao obrigatorias</p>
    </b-jumbotron>
    <b-form>
        <b-form-input type="number" v-model="capitulo.index"></b-form-input>
        <b-form-input v-model="capitulo.titulo" required placeholder="Coloque o titulo do capitulo"></b-form-input>
        <b-form-textarea v-model="capitulo.texto"></b-form-textarea>
    </b-form>
    </div>
</template>
<script>
import axios from "axios";
export default {
  props: {
    historia_index: Number
  },
  data() {
    return {
      capitulo: {
        index: 0,
        titulo: "",
        texto: ""
      },
      historia: ""
    };
  },
  mounted() {
    axios
      .get("http://localhost:8211/api/Historias/" + this.historia_index)
      .then(response => (this.historia = response.data))
      .catch(response => console.log(response));
  }
};
</script>
