<!-- eslint-disable -->
<template>
  <Header/>
  <IndexVue/>
  <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  <Footer msg=""/>
</template>

<script>
import Header from './components/HeaderTemplate.vue'
import Footer from './components/FooterTemplate.vue'

import HelloWorld from './components/HelloWorld.vue'
import IndexVue from './components/Index.vue'

export default {
  name: 'App',
  components: { 
    Header,
    Footer,
    HelloWorld,
    IndexVue
  }
}
</script>

<style>
body{
  margin: 0px;
}
</style>


