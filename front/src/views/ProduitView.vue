<template>
  <!-- <img alt="Vue logo" src="../assets/logo.png" /> -->
  <Produit/>
</template>

<script>
// @ is an alias to /src
import Produit from "@/components/Produit.vue";

export default {
  name: "ProduitView",
  components: {
    Produit,
  },
};
</script>