<template>
    <div>
        <b-jumbotron :header="historia.titulo" lead="Use este formulario para inserir um novo capitulo">
<p>Todas as informaoes sao obrigatorias</p>
    </b-jumbotron>
    <b-form @submit="inseriCapitulo">
        <label for="">Insira um indice para o capitulo</label>
        <b-form-input type="number" v-model="capitulo.indice"></b-form-input>
        <label for="">insira um titulo para o capitulo</label>
        <b-form-input v-model="capitulo.titulo" required placeholder="Coloque o titulo do capitulo"></b-form-input>
        <label for="">Insira o texto</label>
        <b-form-textarea v-model="capitulo.texto"></b-form-textarea>
        <b-button type="submit" variant="primary">Inseri Capitulo</b-button>
    </b-form>
    </div>
</template>
<script>
import axios from "axios";
import router from "vue-router";

export default {
  props: {
    historia: Object
  },
  data() {
    return {
      capitulo: {
        indice: 0,
        titulo: "",
        texto: "",
        historia: ""
      }
    };
  },
  methods: {
    goToHome: function() {
      this.$router.push("/");
    },
    inseriCapitulo: function(env) {
      this.capitulo.historia = this.historia.id;
      axios
        .post("http://localhost:8211/api/Capitulos/", this.capitulo)
        .then(response => {
          this.goToHome();
        })
        .catch(function(response) {
          console.log(response);
        });
    }
  }
};
</script>
