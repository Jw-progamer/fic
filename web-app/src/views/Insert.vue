<template>
  <b-form>
    <label>Digite seu Usuario:</label>
    <b-form-input id="usuario" placeholder="Digite seu usuario" v-model="autor.usuario"/>
    <label for="nome">Digite seu nome:</label>
    <b-form-input id="nome" placeholder="Digite seu nome" v-model="autor.nome"/>
    <label for="idade">Digite a sua idade:</label>
    <b-form-input type="number" placeholder="Digite sua idade" id="idade" v-model="autor.idade"/>
    <label for="descricao">Fale uma descricao:</label>
    <b-form-textarea id="descricao" placeholder="Digite uma descricao" cols="30" rows="10" v-model="autor.descricao"></b-form-textarea>
    <b-button variant="success" v-on:click="addUser">Adicionar autor</b-button>
  </b-form>
</template>
<script>
import axios from "axios";

export default {
  name: "Insert",
  data() {
    return {
      autor: {
        usuario: "",
        nome: "",
        idade: "",
        descricao: ""
      }
    };
  },
  methods: {
    addUser: function() {
      axios
        .post("http://localhost:8211/api/Autores/",this.autor)
        .then(function(response) {
          console.log(response);
        })
        .catch(function(response) {
          console.log(response);
        });
    }
  }
};
</script>

