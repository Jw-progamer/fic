<template>
    
</template>
<script>
import axios from 'axios';

export default {
    data(){
        return{
            historias: []
        }
    },
    mounted() {
        axios.get("http://localhost:8211/api/Historias/")
        .then(response => (this.historias = response.data))
        .catch(response => (console.log(response)))
    }
}
</script>
