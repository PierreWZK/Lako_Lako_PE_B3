<!-- eslint-disable -->
<template>
  <Header msg="bienvenu a tous"/>
  <Template/>
  <Footer/>
</template>

<script>
import Template from './components/Template.vue'
import Footer from './components/Footer.vue'
import Header from './components/HeaderTemplate.vue'

export default {
  name: 'App',
  components: { 
    Header,
    Template,
    Footer
  }
}
</script>

<style>
body{
  margin: 0px;
}
</style>


