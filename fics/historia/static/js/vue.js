function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var app = new Vue({
    el: '#app',
    data () {
        return {
            info: null,
            autor: {
                usuario:"",
                nome:"",
                descricao:"",
                csrfmiddlewaretoken:""
            }
        }
    },
    methods:{
        addUser: function () {
            var crfsToken = getCookie('csrftoken')
            this.autor.csrfmiddlewaretoken = crfsToken
            axios.post("http://localhost:8210/api/Autores/",this.autor)
            .then(
                function(){
                    console.log(response)
                }
            )
            .catch(e => console.log(e))
        }
    },
    mounted () {
       axios
       .get("http://localhost:8210/api/Autores/")
       .then(
           function(response){
               this.info = response.data
           }
       )
    }
})

