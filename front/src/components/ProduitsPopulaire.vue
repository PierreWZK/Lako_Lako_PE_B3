<template>
    <div id="produitsPopulaire">
        <div id="titleProduitPopulaire">
            <div>
                Produits populaire
            </div>
            <div id="filtresProduitsPopulaire">
                <!-- Filtres : Gamme de prix, couleurs, Trier par -->
                <div class="filter-section">
                    <h2>Gamme de prix</h2>
                    <div class="price-range-container">
                        <span>Prix minimum : <span id="min-price">0</span></span>
                        <input type="range" id="price-range" min="0" max="100" step="1">
                        <span>Prix maximum : <span id="max-price">100</span></span>
                    </div>
                </div>

                <div class="filter-section">
                    <h2>Couleurs</h2>
                    <div class="color-filter">
                        <input type="checkbox" id="blue-color" class="color-checkbox">
                        <label for="blue-color" class="color-option blue"></label>
                    </div>
                    <div class="color-filter">
                        <input type="checkbox" id="black-color" class="color-checkbox">
                        <label for="black-color" class="color-option black"></label>
                    </div>
                    <div class="color-filter">
                        <input type="checkbox" id="white-color" class="color-checkbox">
                        <label for="white-color" class="color-option white"></label>
                    </div>
                    <div class="color-filter">
                        <input type="checkbox" id="beige-color" class="color-checkbox">
                        <label for="beige-color" class="color-option beige"></label>
                    </div>
                    <div class="color-filter">
                        <input type="checkbox" id="brown-color" class="color-checkbox">
                        <label for="brown-color" class="color-option brown"></label>
                    </div>
                </div>

                <div class="filter-section">
                    <h2>Filtrer par</h2>
                    <select id="sort-by">
                        <option value="price-asc">Prix croissant</option>
                        <option value="price-desc">Prix décroissant</option>
                        <option value="name-asc">Nom A-Z</option>
                        <option value="name-desc">Nom Z-A</option>
                    </select>
                </div>

            </div>
        </div>
        <div id="lineProduitPopulaire"></div>

        <div id="contentProduitsPopulaire">
            <div class="produitPopulaire">
                <div class="contentTitleProduit">
                    <span>Ensemble de table et chaise en bois design, ...</span>
                </div>
                <div class="contentImgProduit">
                    <img src="../assets/produit2.png" alt="produit1" draggable="false">
                </div>
                <div class="descriptionProduitPopulaire">
                    <span>
                        Lorem ipsum dolor sit amet. Hic labore sequi ut molestiae natus et voluptas illum ea voluptas
                        voluptatem nam numquam quasi eum deleniti tenetur. Sed porro quis in delectus fuga aut iure suscipit
                        est numquam vitae? Et praesentium magni et galisum obcaecati est enim nesciunt a pariatur recusandae
                        id voluptas voluptatum...
                        <br> <span>En savoir plus ...</span>
                    </span>
                </div>
                <div class="prixProduitPopulaire">
                    <span>900€</span>
                </div>
                <div class="starsProduitPopulaire">
                    <span class="etoiles">
                        <span class="etoileAvis etoileRempli">★</span>
                        <span class="etoileAvis etoileRempli">★</span>
                        <span class="etoileAvis etoileRempli">★</span>
                        <span class="etoileAvis etoileRempli">★</span>
                        <span class="etoileAvis etoileNonRempli">★</span>
                    </span>
                    <span class="noteProduitPopulaire">
                        <span class="avisNoteProduitPopulaire">4.8 <span class="avisSlashCinqProduitPopulaire">/5</span> </span>
                    </span>
                </div>
            </div>
            <div class="produitPopulaire">
                <div class="contentTitleProduit">
                    <span>Canapé en velours, Bleu foncé, 3 places, ....</span>
                </div>
                <div class="contentImgProduit">
                    <img src="../assets/produit1.png" alt="produit1" draggable="false">
                </div>
                <div class="descriptionProduitPopulaire">
                    <span>
                        Lorem ipsum dolor sit amet. Hic labore sequi ut molestiae natus et voluptas illum ea voluptas
                        voluptatem nam numquam quasi eum deleniti tenetur. Sed porro quis in delectus fuga aut iure suscipit
                        est numquam vitae? Et praesentium magni et galisum obcaecati est enim nesciunt a pariatur recusandae
                        id voluptas voluptatum...
                        <br> <span>En savoir plus ...</span>
                    </span>
                </div>
                <div class="prixProduitPopulaire">
                    <span>1200€</span>
                </div>
                <div class="starsProduitPopulaire">
                    <span class="etoiles">
                        <span class="etoileAvis etoileRempli">★</span>
                        <span class="etoileAvis etoileRempli">★</span>
                        <span class="etoileAvis etoileRempli">★</span>
                        <span class="etoileAvis etoileRempli">★</span>
                        <span class="etoileAvis etoileNonRempli">★</span>
                    </span>
                    <span class="noteProduitPopulaire">
                        <span class="avisNoteProduitPopulaire">4.7 <span class="avisSlashCinqProduitPopulaire">/5</span> </span>
                    </span>
                </div>
            </div>
            <div class="produitPopulaire">
                <div class="contentTitleProduit">
                    <span>Canapé en velours, Bleu foncé, 3 places, ....</span>
                </div>
                <div class="contentImgProduit">
                    <img src="../assets/produit1.png" alt="produit1" draggable="false">
                </div>
                <div class="descriptionProduitPopulaire">
                    <span>
                        Lorem ipsum dolor sit amet. Hic labore sequi ut molestiae natus et voluptas illum ea voluptas
                        voluptatem nam numquam quasi eum deleniti tenetur. Sed porro quis in delectus fuga aut iure suscipit
                        est numquam vitae? Et praesentium magni et galisum obcaecati est enim nesciunt a pariatur recusandae
                        id voluptas voluptatum...
                        <br> <span>En savoir plus ...</span>
                    </span>
                </div>
                <div class="prixProduitPopulaire">
                    <span>1200€</span>
                </div>
                <div class="starsProduitPopulaire">
                    <span class="etoiles">
                        <span class="etoileAvis etoileRempli">★</span>
                        <span class="etoileAvis etoileRempli">★</span>
                        <span class="etoileAvis etoileRempli">★</span>
                        <span class="etoileAvis etoileRempli">★</span>
                        <span class="etoileAvis etoileNonRempli">★</span>
                    </span>
                    <span class="noteProduitPopulaire">
                        <span class="avisNoteProduitPopulaire">4.7 <span class="avisSlashCinqProduitPopulaire">/5</span> </span>
                    </span>
                </div>
            </div>
            <div class="produitPopulaire">
                <div class="contentTitleProduit">
                    <span>Ensemble de table et chaise en bois design, ...</span>
                </div>
                <div class="contentImgProduit">
                    <img src="../assets/produit2.png" alt="produit1" draggable="false">
                </div>
                <div class="descriptionProduitPopulaire">
                    <span>
                        Lorem ipsum dolor sit amet. Hic labore sequi ut molestiae natus et voluptas illum ea voluptas
                        voluptatem nam numquam quasi eum deleniti tenetur. Sed porro quis in delectus fuga aut iure suscipit
                        est numquam vitae? Et praesentium magni et galisum obcaecati est enim nesciunt a pariatur recusandae
                        id voluptas voluptatum...
                        <br> <span>En savoir plus ...</span>
                    </span>
                </div>
                <div class="prixProduitPopulaire">
                    <span>900€</span>
                </div>
                <div class="starsProduitPopulaire">
                    <span class="etoiles">
                        <span class="etoileAvis etoileRempli">★</span>
                        <span class="etoileAvis etoileRempli">★</span>
                        <span class="etoileAvis etoileRempli">★</span>
                        <span class="etoileAvis etoileRempli">★</span>
                        <span class="etoileAvis etoileNonRempli">★</span>
                    </span>
                    <span class="noteProduitPopulaire">
                        <span class="avisNoteProduitPopulaire">4.8 <span class="avisSlashCinqProduitPopulaire">/5</span> </span>
                    </span>
                </div>
            </div>
            <div class="produitPopulaire">
                <div class="contentTitleProduit">
                    <span>Ensemble de table et chaise en bois design, ...</span>
                </div>
                <div class="contentImgProduit">
                    <img src="../assets/produit2.png" alt="produit1" draggable="false">
                </div>
                <div class="descriptionProduitPopulaire">
                    <span>
                        Lorem ipsum dolor sit amet. Hic labore sequi ut molestiae natus et voluptas illum ea voluptas
                        voluptatem nam numquam quasi eum deleniti tenetur. Sed porro quis in delectus fuga aut iure suscipit
                        est numquam vitae? Et praesentium magni et galisum obcaecati est enim nesciunt a pariatur recusandae
                        id voluptas voluptatum...
                        <br> <span>En savoir plus ...</span>
                    </span>
                </div>
                <div class="prixProduitPopulaire">
                    <span>900€</span>
                </div>
                <div class="starsProduitPopulaire">
                    <span class="etoiles">
                        <span class="etoileAvis etoileRempli">★</span>
                        <span class="etoileAvis etoileRempli">★</span>
                        <span class="etoileAvis etoileRempli">★</span>
                        <span class="etoileAvis etoileRempli">★</span>
                        <span class="etoileAvis etoileNonRempli">★</span>
                    </span>
                    <span class="noteProduitPopulaire">
                        <span class="avisNoteProduitPopulaire">4.8 <span class="avisSlashCinqProduitPopulaire">/5</span> </span>
                    </span>
                </div>
            </div>
            <div class="produitPopulaire">
                <div class="contentTitleProduit">
                    <span>Canapé en velours, Bleu foncé, 3 places, ....</span>
                </div>
                <div class="contentImgProduit">
                    <img src="../assets/produit1.png" alt="produit1" draggable="false">
                </div>
                <div class="descriptionProduitPopulaire">
                    <span>
                        Lorem ipsum dolor sit amet. Hic labore sequi ut molestiae natus et voluptas illum ea voluptas
                        voluptatem nam numquam quasi eum deleniti tenetur. Sed porro quis in delectus fuga aut iure suscipit
                        est numquam vitae? Et praesentium magni et galisum obcaecati est enim nesciunt a pariatur recusandae
                        id voluptas voluptatum...
                        <br> <span>En savoir plus ...</span>
                    </span>
                </div>
                <div class="prixProduitPopulaire">
                    <span>1200€</span>
                </div>
                <div class="starsProduitPopulaire">
                    <span class="etoiles">
                        <span class="etoileAvis etoileRempli">★</span>
                        <span class="etoileAvis etoileRempli">★</span>
                        <span class="etoileAvis etoileRempli">★</span>
                        <span class="etoileAvis etoileRempli">★</span>
                        <span class="etoileAvis etoileNonRempli">★</span>
                    </span>
                    <span class="noteProduitPopulaire">
                        <span class="avisNoteProduitPopulaire">4.7 <span class="avisSlashCinqProduitPopulaire">/5</span> </span>
                    </span>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
#produitsPopulaire {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
}

#titleProduitPopulaire {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 88%;
    font-size: 2rem;
    font-weight: 400;
    margin-top: 2rem;
}

#lineProduitPopulaire {
    width: 88%;
    height: 0.2rem;
    background-color: black;
    margin-top: 0.5rem;
}

#contentProduitsPopulaire {
    width: 88%;
    height: 100%;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-between;
}

.produitPopulaire {
    width: 40%;
    margin-top: 2rem;
    margin-bottom: 2rem;
}

.produitPopulaire div img,
.produitPopulaire div span {
    cursor: pointer;
}

.contentTitleProduit {
    width: 100%;
    font-size: 1.2rem;
    font-weight: 400;
    margin-bottom: 0.5rem;
}

.contentImgProduit img {
    max-width: 100%;
    max-height: 17rem;
    object-fit: contain;
}

.descriptionProduitPopulaire {
    width: 100%;
    font-size: 1rem;
    font-weight: 400;
    margin-top: 0.5rem;
    margin-bottom: 0.5rem;
}

.descriptionProduitPopulaire span {
    font-size: 0.8rem;
    font-weight: 300;
    color: #666;
}

.descriptionProduitPopulaire span span {
    font-size: 0.8rem;
    font-weight: 300;
    color: #666;
    text-decoration: underline;
    cursor: pointer;
}

.prixProduitPopulaire {
    width: 100%;
    font-size: 1.8rem;
    font-weight: 400;
}

.starsProduitPopulaire {
    display: flex;
    flex-direction: row;
    align-items: center;
    width: 100%;
    font-size: 2.2rem;
    font-weight: 400;
}

.starsProduitPopulaire span.etoileNonRempli {
    color: #D9D9D9;
}

.starsProduitPopulaire span.etoileRempli {
    color: #007EA7;
}

.starsProduitPopulaire span.etoiles span.etoileAvis.active {
    color: #005a84;
}

.avisNoteProduitPopulaire {
    font-size: 1.2rem;
    font-weight: 400;
    color: #666;
    cursor: default !important;
}

.noteProduitPopulaire {
    margin-left: 1rem;
    cursor: default !important;
    padding-bottom: 0.25rem;
}

.avisSlashCinqProduitPopulaire {
    font-size: 1rem;
    font-weight: 400;
    color: #666;
    cursor: default !important;
}

/* Filtres */
#filtresProduitsPopulaire {
    /* A FAIRE un rendu */
    display: none;
}

.filter-section {
    margin-bottom: 20px;
}

h2 {
    font-size: 16px;
    margin-bottom: 10px;
}

.price-range-container {
    display: flex;
    align-items: center;
}

.price-range-container span {
    margin-right: 10px;
}

.price-range-container input[type="range"] {
    flex-grow: 1;
}

.color-filter {
    display: inline-block;
    margin-right: 10px;
}

.color-option {
    display: inline-block;
    width: 20px;
    height: 20px;
    border: 1px solid #ccc;
    cursor: pointer;
}

.color-checkbox {
    display: none;
}

.color-option.selected {
    border-color: #007EA7;
}

#blue-color+.color-option {
    background-color: blue;
}

#black-color+.color-option {
    background-color: black;
}

#white-color+.color-option {
    background-color: white;
}

#beige-color+.color-option {
    background-color: beige;
}

#brown-color+.color-option {
    background-color: brown;
}

/* Fin Filtres */
</style>

<script>

export default {
    name: 'ProduitPopulaire'
}

window.onload = function () {
    // Si l'url contient produitsPopulaire, on display flex l'id "filtresProduitsPopulaire"
    if (window.location.href.includes("produitsPopulaire")) {
        document.getElementById("filtresProduitsPopulaire").style.display = "flex";
    } else {
        document.getElementById("filtresProduitsPopulaire").style.display = "none";
    }

    //GAMME DE PRIX
    const minPriceSpan = document.getElementById("min-price");
    const maxPriceSpan = document.getElementById("max-price");
    const priceRangeInput = document.getElementById("price-range");

    priceRangeInput.addEventListener("input", updatePrice);

    function updatePrice() {
        const minPrice = priceRangeInput.value;
        const maxPrice = priceRangeInput.max - minPrice;

        minPriceSpan.textContent = minPrice;
        maxPriceSpan.textContent = maxPrice;
    }
    //GAMME DE PRIX

    //COULEURS
    const colorOptions = document.querySelectorAll('.color-option');

    colorOptions.forEach(colorOption => {
        colorOption.addEventListener('click', () => {
            colorOption.classList.toggle('selected');
        });
    });
    //COULEURS

    //STARS
    var ensemblesEtoiles = document.getElementsByClassName('starsProduitPopulaire');

    for (var j = 0; j < ensemblesEtoiles.length; j++) {
        var etoiles = ensemblesEtoiles[j].getElementsByClassName('etoileAvis');

        for (var i = 0; i < etoiles.length; i++) {
            etoiles[i].addEventListener('mouseover', createMouseoverHandler(i, etoiles));
            etoiles[i].addEventListener('mouseout', decolorerEtoiles.bind(null, etoiles));
        }
    }

    function createMouseoverHandler(index, etoiles) {
        return function () {
            colorerEtoiles(index, etoiles);
        };
    }

    function colorerEtoiles(n, etoiles) {
        for (var i = 0; i <= n; i++) {
            etoiles[i].classList.add('active');
        }
    }

    function decolorerEtoiles(etoiles) {
        for (var i = 0; i < etoiles.length; i++) {
            etoiles[i].classList.remove('active');
        }
    }
    //STARS
}

</script>