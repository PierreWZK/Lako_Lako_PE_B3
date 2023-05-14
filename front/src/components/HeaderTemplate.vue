<!-- eslint-disable -->
<template>
    <div class="header">
        <div id="logoHeader" style="z-index: 99;">
            <router-link to="/">
                <img src="../assets/logo.png" alt="logo Lako Lako" draggable="false">
            </router-link>
        </div>
        <div id="contentNavBar">
            <div id="topSearchBar">
                <div class="searchBar">
                    <input type="text" placeholder="Recherchez un produit, une catégorie, une marque, ...">
                    <svg aria-hidden="true" width="1.5em" height="1.5em" fill="#454545" xmlns="http://www.w3.org/2000/svg"
                        viewBox="0 0 24 24">
                        <path
                            d="M18 6.05a7 7 0 00-10.51 9.14l-3.08 3.08a1 1 0 001.41 1.42l3.09-3.09A7 7 0 0018 6.05zm-1.41 8.49a5 5 0 110-7.08 5 5 0 01.04 7.08z">
                        </path>
                    </svg>
                </div>
                <div id="buttonMenuNavBar">
                    <div class="compte">
                        <router-link to="/login">
                            <span>Bonjour, <span id="username">Identifiez-vous</span></span>
                            <span id="seConnecter">Se connecter</span>
                        </router-link>
                    </div>
                    <div class="panier">
                        <div>
                            Mon
                            <span>Panier</span>
                        </div>
                        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="204"
                            height="200" viewBox="0 0 204 200" fill="none">
                            <rect width="204" height="200" fill="url(#pattern0)" />
                            <defs>
                                <pattern id="pattern0" patternContentUnits="objectBoundingBox" width="1" height="1">
                                    <use xlink:href="#image0_549_168"
                                        transform="matrix(0.00295299 0 0 0.00301205 -0.00643751 0)" />
                                </pattern>
                                <image id="image0_549_168" width="343" height="332"
                                    xlink:href="data:image/png;base64,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" />
                            </defs>
                        </svg>
                    </div>

                </div>

            </div>
            <div id="bottomSearchBar">
                <div id="contentBottomNavBarFirst">
                    <router-link to="/produitsPopulaire">
                        <div class="produitsNav">
                            <svg xmlns="http://www.w3.org/2000/svg" width="21" height="13" viewBox="0 0 21 13" fill="none">
                                <rect x="6" width="15" height="3" fill="black" />
                                <rect x="6" y="5" width="15" height="3" fill="black" />
                                <rect x="6" y="10" width="15" height="3" fill="black" />
                                <circle cx="1.5" cy="11.5" r="1.5" fill="black" />
                                <circle cx="1.5" cy="6.5" r="1.5" fill="black" />
                                <circle cx="1.5" cy="1.5" r="1.5" fill="black" />
                            </svg>
                            Produits
                        </div>
                    </router-link>
                    <router-link to="/produitsPopulaire">
                        <div class="produitsPopulaire linkNav">
                            Nos produits populaires
                        </div>
                    </router-link>
                    <div class="promos linkNav">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="23" viewBox="0 0 24 23">
                            <line x1="1.69935" y1="13.4393" x2="13.0838" y2="2.05492" stroke="#007EA7" stroke-width="3" />
                            <line x1="21.5099" y1="11" x2="21.5099" y2="3" stroke="#007EA7" stroke-width="3" />
                            <line x1="12.0099" y1="2.5" x2="20.0099" y2="2.5" stroke="#007EA7" stroke-width="3" />
                            <line x1="21.0099" y1="3.5" x2="23.0099" y2="3.5" stroke="#007EA7" stroke-width="3" />
                            <line x1="20.0099" y1="2.5" x2="22.0099" y2="2.5" stroke="#007EA7" stroke-width="3" />
                            <line x1="2.06066" y1="11.6776" x2="12.2819" y2="21.8988" stroke="#007EA7" stroke-width="3" />
                            <path d="M11.0583 21.0032L21.9429 9.95202" stroke="#007EA7" stroke-width="3" />
                            <rect x="17.0099" y="5" width="2" height="2" rx="1" fill="#007EA7" />
                            <circle cx="21.499" cy="2.5" r="1" fill="#007EA7" />
                        </svg>
                        En promo !
                    </div>
                </div>
                <div id="contentBottomNavBarSecond">
                    <div class="contact linkNav">
                        Contactez-nous
                    </div>
                    <div class="aide linkNav">
                        Aide
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
input {
    background-color: inherit;
    border: none;
    padding: 0;
    margin: 0;
    font-size: inherit;
    font-family: inherit;
    color: inherit;
    outline: none;
}

.header {
    position: relative;
    z-index: 99;
    display: flex;
    flex-direction: row;
    align-items: flex-end;

    height: 6rem;
    width: 100vw;

    border-bottom: 2px solid #D9D9D9;
    background-color: white;
}

#logoHeader {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;

    width: 15vw;
    height: 100%;
}

#logoHeader img {
    max-width: 10vw;
    margin-bottom: 1vw;
    cursor: pointer;
    max-height: 6rem;
}

#contentNavBar {
    display: flex;
    flex-direction: column;
    align-items: flex-end;

    width: 100vw;
    height: 100%;
}

#topSearchBar {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;

    width: 85vw;
    height: 60%;

    list-style-type: none;
    background-color: #D9D9D9;
    position: relative;
}

#topSearchBar .searchBar {
    display: flex;
    align-items: center;

    overflow: hidden;
    width: 50vw;
    height: 65%;
    margin-left: 1vw;

    border: 1px solid white;
    border-radius: 5px;
    background-color: #FFFCFC;
}

#topSearchBar .searchBar input {
    margin-left: 1vw;
    width: 95%;
}

#topSearchBar .searchBar input::placeholder {
    color: black;
}

#topSearchBar .searchBar svg {
    cursor: pointer;
}

#topSearchBar::after {
    content: "";
    display: block;
    position: absolute;

    border-left: 3.66rem solid transparent;
    border-top: 3.66rem solid var(--color-grey-100, #D9D9D9);
    width: 0;
    height: 0;

    left: -3.6rem;
    top: 0;
}

#topSearchBar #buttonMenuNavBar {
    display: flex;
    align-items: center;
    justify-content: center;

    height: 100%;

    border-radius: 1vw;
    width: 23rem;
    margin-right: -3rem;
}

#topSearchBar #buttonMenuNavBar div {
    cursor: pointer;
    min-width: 10rem;
    white-space: nowrap;
}

.panier {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    width: 10vw;
    height: 80%;

    border-radius: 1vw;
    padding-left: 1rem;
    padding-right: 1rem;
}

.panier div {
    display: flex;
    flex-direction: column;
    min-width: 3rem !important;
    width: 3vw;
    font-size: 0.8rem;
}

.panier div span {
    font-size: 1rem;
    margin-top: -5px;
    font-weight: bold;
}

.panier svg {
    max-height: 120%;
    max-width: 20%;
}

.compte a {
    display: flex;
    flex-direction: column;
    /* align-items: center; */
    justify-content: center;
    width: 13.81vw;
    height: 80%;

    border-radius: 1vw;
    padding-left: 1rem;
    padding-right: 1rem;

    font-size: 0.8rem;
    text-align: start;
}

.compte a span#seConnecter {
    font-weight: bold;
    font-size: 0.9rem;
}

#bottomSearchBar {
    z-index: 1;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;

    width: 85vw;
    height: 40%;

    list-style-type: none;
}

#bottomSearchBar #contentBottomNavBarFirst,
#bottomSearchBar #contentBottomNavBarSecond {
    display: flex;
    flex-direction: row;
    align-items: center;
}

#bottomSearchBar #contentBottomNavBarFirst .produitsNav {
    display: flex;
    align-items: center;
    font-weight: bold;
}

#bottomSearchBar #contentBottomNavBarFirst div {
    margin-right: 2vw;
    cursor: pointer;
    transition: all 0.3s ease;
}

#bottomSearchBar #contentBottomNavBarFirst .produitsNav svg {
    margin-left: 1vw;
}

#bottomSearchBar #contentBottomNavBarFirst .produitsNav svg,
#bottomSearchBar #contentBottomNavBarFirst .promos svg {
    margin-right: 0.5vw;
}

#bottomSearchBar #contentBottomNavBarFirst #produitsPopulaire {
    padding-top: 0.5vw;
    padding-bottom: 0.5vw;
}

#bottomSearchBar #contentBottomNavBarFirst .promos svg {
    padding-top: 0.3vw;
    padding-bottom: 0.3vw;
}

#bottomSearchBar #contentBottomNavBarFirst .promos svg,
#bottomSearchBar #contentBottomNavBarFirst .promos svg line,
#bottomSearchBar #contentBottomNavBarFirst .promos svg path,
#bottomSearchBar #contentBottomNavBarFirst .promos svg rect,
#bottomSearchBar #contentBottomNavBarFirst .promos svg circle {
    fill: #007EA7;
    stroke: #007EA7;
    transition: all 0.1s ease;
}

#bottomSearchBar #contentBottomNavBarFirst .promos {
    color: #007EA7;
    font-weight: bold;
    transition: all 0.3s ease;

    display: flex;
    align-items: center;
}

#bottomSearchBar #contentBottomNavBarFirst .promos:hover,
#bottomSearchBar #contentBottomNavBarFirst .promos:hover svg,
#bottomSearchBar #contentBottomNavBarFirst .promos:hover svg line,
#bottomSearchBar #contentBottomNavBarFirst .promos:hover svg path,
#bottomSearchBar #contentBottomNavBarFirst .promos:hover svg rect,
#bottomSearchBar #contentBottomNavBarFirst .promos:hover svg circle {
    color: #FFF;
    fill: #FFF;
    stroke: #FFF;
}

#bottomSearchBar #contentBottomNavBarSecond div {
    cursor: pointer;
    font-weight: 600;
    margin-right: 2rem;
}

.linkNav {
    cursor: pointer;
    box-shadow: inset 0 0 0 0 #007EA7;
    /* color: #54b3d6; */
    padding: 0 .25rem;
    margin: 0 -.25rem;
    transition: color .2s ease-in-out, box-shadow .3s ease-in-out;
}

.linkNav:hover {
    color: #fff;
    box-shadow: inset 200px 0 0 0 #007EA7;
}

/* Presentational styles */
.linkNav {
    line-height: 1.5;
    text-decoration: none;
}
</style>

<script>

export default {
    name: 'HeaderTemplate'
}

window.onload = function () {
    // récupération des données de l'utilisateur (via les cookie)
    var username = getCookie("username");

    // si l'utilisateur est connecté on affiche son nom et prénom dans le header (la class .username)
    if (username != "") {
        document.getElementById("username").innerHTML = username;

        // On mets a jour le #seConnecter, et on mets le texte de #seConnecter a "Se déconnecter"
        document.getElementById("seConnecter").innerHTML = "Se déconnecter";
    }
}

</script>