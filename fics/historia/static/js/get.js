var app = new Vue({
    el: '#view',
    data () {
        return {
            info: ""
        }
    },
    mounted () {
       axios
       .get("http://localhost:8210/api/Autores/")
       .then(response => (this.info = response.data))
    }
})