<!-- eslint-disable -->
<template>
  <routeur-view>
    <Header/>
    <div v-if = "$route.path === '/'">
      <IndexVue/>
      <ProduitsPopulaire/>
    </div>
    <div v-if = "$route.path === '/login'"><LoginView/></div>
    <div v-if = "$route.path === '/signin'"><Signin/></div>
    <div v-if = "$route.path === '/produitsPopulaire'"><ProduitsPopulaire/></div>
    <Footer/>
  </routeur-view>
</template>

<script>
import Header from './components/HeaderTemplate.vue'
import Footer from './components/FooterTemplate.vue'
import LoginView from './views/LoginView.vue'
import IndexVue from './components/Index.vue'

// Templates des pages, etc...
import ProduitsPopulaire from './components/ProduitsPopulaire.vue'
import Signin from './components/Signin.vue'

export default {
  name: 'App',
  components: {
    Header,
    Footer,
    IndexVue,
    ProduitsPopulaire,
    LoginView,
    Signin
}
}
</script>

<style>
body{
  margin: 0px;
}
</style>


