<!-- eslint-disable -->
<template>
  <Header msg=""/>
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <Footer msg=""/>
</template>

<script>
import Header from './components/HeaderTemplate.vue'
import Footer from './components/FooterTemplate.vue'

import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: { 
    Header,
    HelloWorld,
    Footer
  }
}
</script>


