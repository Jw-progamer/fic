var app = new Vue({
  el: '#app',
  data() {
    return {
      info: [],
      autor: {
        usuario: '',
        nome: '',
        descricao: '',
        idade: ''
      }
    }
  },
  methods: {
    addUser: function () {
      axios.post('http://localhost:8210/api/Autores/', this.autor)
        .then(
          function (response) {
            console.log(response)
          }
      )
        .catch(e => console.log(e))
    },
    deleteUser: function (id) {
      console.log(id)
      axios.delete('http://localhost:8210/api/Autores/' + id)
        .then(
          function (response) {
            console.log(response)
            app.refreshUser()
          }
      )
    },
    refreshUser: function () {
      axios
        .get('http://localhost:8210/api/Autores/')
        .then(response => (this.info = response.data)).catch(e => console.log(e))
    },
    updateUser: function (autor) {
      console.log(autor.usuario)
      console.log(autor.id)
      axios.patch('http://localhost:8210/api/Autores/' + autor.id+"/", autor)
      .then(
        function(response){
          console.log(response)
          app.refreshUser()
        }
      )
      .catch(e => console.log(e))
    }
  },
  mounted() {
    axios
      .get('http://localhost:8210/api/Autores/')
      .then(response => (this.info = response.data)).catch(e => console.log(e))
  }
})