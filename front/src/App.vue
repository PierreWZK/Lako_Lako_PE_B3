<!-- eslint-disable -->
<template>
  <Header/>
  <IndexVue/>
  <ProduitsPopulaire/>
  <Footer/>
</template>

<script>
import Header from './components/HeaderTemplate.vue'
import Footer from './components/FooterTemplate.vue'

import HelloWorld from './components/HelloWorld.vue'
import IndexVue from './components/Index.vue'

// Templates des pages, etc...
import ProduitsPopulaire from './components/ProduitsPopulaire.vue'

export default {
  name: 'App',
  components: { 
    Header,
    Footer,
    HelloWorld,
    IndexVue,
    ProduitsPopulaire
  }
}
</script>

<style>
body{
  margin: 0px;
}
</style>


