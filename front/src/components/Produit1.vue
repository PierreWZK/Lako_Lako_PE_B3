<template>
  <div id="produit">
    <div id="lineProduit"></div>

    <div id="contentProduit">
      <div id="imagesProduit">
        <div id="carousselProduit">
          <img src="../assets/produit2.png" alt="Images du Produit">
          <!-- point du caroussel en dessous de l'image -->
          <div id="pointsCarousselProduit">
            <div id="pointCarousselProduit1"></div>
            <div id="pointCarousselProduit2"></div>
            <div id="pointCarousselProduit3"></div>
            <div id="pointCarousselProduit4"></div>
          </div>
        </div>
      </div>
      <div id="sousContentProduit">
        <div id="nomProduit">Ensemble de table et chaise en bois design, table 6 places, 4 chaises, 80x160</div>
      </div>
    </div>
  </div>
</template>

<style>
#produit {
  display: flex;
  flex-direction: column;
  align-items: space-between;
}

#contentProduit {
  width: 100%;
  display: flex;
  justify-content: space-around;
  height: 20rem;
  margin-top: 2rem;
  margin-right: 20vw;
  margin-left: 5vw;  
}

#lineProduit {
  align-self: center;
  width: 90%;
  height: 0.2rem;
  background-color: black;
  margin-top: 3rem;
}

#imagesProduit {
  /* width: 90%; */
  height: 19rem;
  display: flex;
}

#carousselProduit {
  width: 40%;
  position: relative;
}

#carousselProduit img {
  width: 100%;
  height: 17rem;
  object-fit: cover;
}

#pointsCarousselProduit {
  position: absolute;
  bottom: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  margin-top: 2rem;
}

#pointCarousselProduit1,
#pointCarousselProduit2,
#pointCarousselProduit3,
#pointCarousselProduit4 {
  width: 0.8rem;
  height: 0.8rem;
  border-radius: 50%;
  background-color: #D9D9D9;
  margin: 0.5rem;
}

#pointCarousselProduit1 {
  background-color: #000;
}

#pointCarousselProduit1:hover,
#pointCarousselProduit2:hover,
#pointCarousselProduit3:hover,
#pointCarousselProduit4:hover {
  cursor: pointer;
  background-color: #000;
}
</style>

<script>

export default {
  name: 'Produit1'
}

</script>
