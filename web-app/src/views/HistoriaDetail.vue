<template>
    <div>
        <router-view :historia="historia"></router-view>
    </div>
</template>
<script>
import axios from "axios";

export default {
  props: {
    historia_id: String
  },
  data() {
    return {
      historia: {
          type:Object
      }
    };
  },
  created() {
    axios
      .get("http://localhost:8211/api/Historias/" + this.historia_id)
      .then(response => (this.historia = response.data))
      .catch(response => console.log(response));
  }
};
</script>

