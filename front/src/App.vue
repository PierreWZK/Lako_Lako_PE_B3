<!-- eslint-disable -->
<template>
  <routeur-view>
    <Header/>
    <div v-if = "$route.path === '/'">
      <IndexVue/>
      <ProduitsPopulaires/>
    </div>
    <div v-if = "$route.path === '/login'"><LoginView/></div>
    <div v-if = "$route.path === '/signin'"><Signin/></div>
    <div v-if = "$route.path === '/produitsPopulaires'"><ProduitsPopulaires/></div>
    <div v-if = "$route.path === '/produits'"><Produits/></div>
    <Footer/>
  </routeur-view>
</template>

<script>
import Header from './components/HeaderTemplate.vue'
import Footer from './components/FooterTemplate.vue'
import LoginView from './views/LoginView.vue'
import IndexVue from './components/Index.vue'

// Templates des pages, etc...
import ProduitsPopulaires from './components/ProduitsPopulaires.vue'
import Produits from './components/Produits.vue'
import Signin from './components/Signin.vue'

//Produits

export default {
  name: 'App',
  components: {
    Header,
    Footer,
    IndexVue,
    ProduitsPopulaires,
    LoginView,
    Produits,
    Signin
}
}
</script>

<style>
body{
  margin: 0px;
}
</style>


