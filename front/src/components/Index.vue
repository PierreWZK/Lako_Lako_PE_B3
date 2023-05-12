<template>
  <div id="indexVue">
    <div id="logoVuePrincipale">
      <img src="../assets/logo.png" alt="logo Lako Lako" draggable="false">
    </div>
    Bienvenue sur Lako Lako, entreprise de père en fils depuis 1785 !
  </div>
</template>

<style>
#indexVue {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  align-items: center;

  width: 100vw;
  height: 100vh;

  font-size: 2rem;
  font-weight: bold;
}

#logoVuePrincipale img {
  width: 70rem;
  margin-top: -7rem;
  margin-bottom: 1rem;
}
</style>

<script>

export default {
  name: 'Index'
}

</script>
