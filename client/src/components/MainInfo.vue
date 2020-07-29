<template>
  <div class="container">
  	<button type="button" class="btn btn-primary">{{msg}}</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'MainInfo',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://127.0.0.1:5000/';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-выключение следующей строки
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>