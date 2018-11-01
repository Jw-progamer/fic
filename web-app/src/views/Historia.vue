<template>
    <div>
        <div v-for="historia in historias">
        <b-card :title="historia.titulo"
        class="mb-2">
                <p class="card-text">
                    {{historia.descricao}}
                </p>
                <ul>
                    <li v-for="genero in historia.generos">
                        {{genero.nome}}
                    </li>
                </ul>
                <b-link router-tag="b-button" :to="historia">Novo capitulo</b-link>
                <b-link router-tag="b-button" to="/capitulo">Visualizar Historia</b-link>
        </b-card>
    </div>
    </div>
</template>
<script>
import axios from "axios";

export default {
  props: {
    autor: String
  },
  data() {
    return {
      historias: []
    };
  },
  mounted() {
    axios
      .get("http://localhost:8211/api/Historias/getautor/" + this.autor)
      .then(response => (this.historias = response.data.historias))
      .catch(response => console.log(response));
  }
};
</script>
