<template>
  <div class="dashboard">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to HRM"/>
  </div>
</template>

<script>
import HelloWorld from './HelloWorld.vue';

export default {
  name: 'dashboard',
  components: {
    HelloWorld
  }
}
</script>

<style>
.dashboard {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
