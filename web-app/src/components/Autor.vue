<template>
    <b-table striped :items="atr">
        <template slot="usuario" slot-scope='user'>
            <b-link :to="'/'+user.value+'/historias/'">{{user.value}}</b-link>
        </template>
    </b-table>
</template>
<script>
export default {
    name:"Autor",
    props:{
        atr: Array
    },
    data(){
        return{
            campos:['Usuario','Nome','Idade','Data de Inscricao','Descricao']
        }
    }
}
</script>
