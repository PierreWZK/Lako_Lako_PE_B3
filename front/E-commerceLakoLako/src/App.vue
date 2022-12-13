<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Header from './components/Header.vue'
</script>

<template>
  <header>

    <div class="wrapper">
      <Header/>
<!-- 
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/header">Header</RouterLink>
      </nav> -->
    </div>
  </header>
</template>

<style scoped>
header{
  background-color: black;
}
</style>
