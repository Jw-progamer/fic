<template>
    <div>
      <span v-if="carregando">
        <p>carregando</p>
      </span>
      <span v-else>
        <b-jumbotron :header="historia.titulo" :lead="historia.autor.usuario">
        <h1>Capitulos de {{historia.titulo}}</h1>
        <ul>
          <li v-for="genero in historia.generos">
            {{genero.nome}}
          </li>
        </ul>
        <h1>Classificao etaria {{historia.restricao_etaria}}</h1>
    </b-jumbotron>
        <b-table striped hover :items="capitulos" :fields="colunas"></b-table>
      </span>
    </div>
</template>

<script>
import axios from "axios";

export default {
  props: {
    historia: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      capitulos: [],
      colunas: ["indice", "titulo"],
      carregando : true
    };
  },
  watch: {
    historia: function(newVal, oldVal) {
      console.log("Prop mudou: ", newVal, " | era: ", oldVal);
      this.fecthCapitulos();
      this.carregou();
    }
  },
  methods: {
    fecthCapitulos() {
      if (typeof this.historia.id === "undefined") {
        console.log("E nulo caramba");
      } else {
        axios
          .get(
            "http://localhost:8211/api/Capitulos/getcapitulos/" +
              this.historia.id
          )
          .then(response => {
            this.capitulos = response.data.capitulos;
          })
          .catch(response => console.log(this.historia));
      }
    },
    carregou(){
      this.carregando = false
    }
  },
};
</script>
