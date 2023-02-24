<template>
    <!-- <h1>{{ msg }}</h1> -->
    <div class="header">
        <div id="logo">
            <h1>Logo</h1>
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
            </div>
            <div id="bottomSearchBar">
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
                <div class="produitsPopulaire">
                    Nos produits populaires
                </div>
                <div class="promos">
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
        </div>
    </div>
</template>

<script>

export default {
    name: 'HeaderTemplate',
    props: {
        msg: String
    }
}

</script>

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
    display: flex;
    flex-direction: row;
    align-items: flex-end;

    height: 12vh;
    width: 100vw;

    border-bottom: 2px solid #D9D9D9;
}

#logo {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;

    width: 15vw;
    height: 100%;
}

#contentNavBar {
    display: flex;
    flex-direction: column;
    align-items: flex-end;

    width: 85vw;
    height: 100%;
}

#topSearchBar {
    display: flex;
    flex-direction: row;
    align-items: center;

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

    border-left: 7.2vh solid transparent;
    border-top: 7.2vh solid var(--color-grey-100, #D9D9D9);
    width: 0;
    height: 0;

    left: -7.2vh;
    top: 0;
}

#bottomSearchBar {
    z-index: 1;
    display: flex;
    flex-direction: row;
    align-items: center;

    width: 85vw;
    height: 40%;

    list-style-type: none;
}

#bottomSearchBar .produitsNav {
    display: flex;
    align-items: center;
    font-weight: bold;
}

#bottomSearchBar div {
    margin-right: 2vw;
    cursor: pointer;
    transition: all 0.3s ease;
}

#bottomSearchBar .produitsNav svg {
    margin-left: 1vw;
}

#bottomSearchBar .produitsNav svg,
#bottomSearchBar .promos svg {
    margin-right: 0.5vw;
}

#bottomSearchBar .promos svg,
#bottomSearchBar .promos svg line,
#bottomSearchBar .promos svg path,
#bottomSearchBar .promos svg rect,
#bottomSearchBar .promos svg circle {
    fill: #007EA7;
    stroke: #007EA7;
    transition: all 0.1s ease;
}

#bottomSearchBar .promos {
    color: #007EA7;
    font-weight: bold;
    transition: all 0.3s ease;
}

#bottomSearchBar .promos:hover,
#bottomSearchBar .promos:hover svg,
#bottomSearchBar .promos:hover svg line,
#bottomSearchBar .promos:hover svg path,
#bottomSearchBar .promos:hover svg rect,
#bottomSearchBar .promos:hover svg circle{
    color: #003249;
    fill: #003249;
    stroke: #003249;
}
</style>