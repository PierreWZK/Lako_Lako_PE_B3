<template>
    <div class="header">
        <div id="logo">
            <img src="../assets/logo.png" alt="logo Lako Lako" draggable="false" onclick="document.location = '/'">
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
                    <div class="compte">Se Connecter
                        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="41"
                            height="41" viewBox="0 0 41 41" fill="none">
                            <rect width="41" height="41" fill="url(#pattern0)" />
                            <defs>
                                <pattern id="pattern0" patternContentUnits="objectBoundingBox" width="1" height="1">
                                    <use xlink:href="#image0_358_15" transform="scale(0.0025)" />
                                </pattern>
                                <image id="image0_358_15" width="400" height="400"
                                    xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAZAAAAGQAQMAAAC6caSPAAAAAXNSR0IB2cksfwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAZQTFRFAAAA////pdmf3QAAAAJ0Uk5TAP9bkSK1AAAEL0lEQVR4nO3cQW6cMBQG4EFesOQIPgpHs4+G1It41226S6RoaAxJlfB+v9ffmng8EV50AfmYMTb+jWF6uZylz+IST554cqXJuEaeJJZM6zNL/LpWkMiTRJJ5XV95wlYmrHRlMkkceRNsZTIhK7ORyBPuAgh8ZSa+Mo6vzLAR7gKYG1ZmoUxFy9RWhhvN9sokygS+Mr5hyyTKtKxMZMjQsDJcnxlrh6ZEkTYt43gyVARA4ImnG2arDEkGnuTKsGTiw9zx5FJBAk8mfso09kocG2Udk6Fjkn4KubCDcs8k8LdY3ZK5X8Le+r1lX7eEXi1oRWpi7D/KY5CxH/K16dxDk9fHIMNDk8OAakeyGIPt5GtDwvEvxIZ+iBVjohns5LsbMWJMzli7JWbydUucuPearEjuloziD+SWuxD5zc1b3kk0XLfEvOXtlsirw7yzlJPvTggYgVsRPcYqCEhGKyxvRfQYqyDgjLYhVow9EjFiDK1tdUvkOPWlyNxrR9QYqyAoGNsQI8Yeihgxhlq6W2KsQqOlrTqS7k7QLVEd0WIM3njdnMAorSJajEGiJ99diRZjkOjJB8+nRdK9iLoKjfu5RRZElBhrQ1DuVRIlxjBRk+/OBGxViZp8+Ba6W4Jr+F7w6TQI6k1qvrYhuJsbBF3lTks+TNSwrCB4kFPzFS9rVhA1LIuEWH5vScKtCTw1N/8UGD6zSuAYrxM4lBok8mThSeIJahiDoIbxOkENYxDUMAZBDVNBrKe8ERil5EdtC0dyN08kmXnieTLx77KMPHHsC9Ybod+ZqCL0CxAVJPBk7vhljp9E4klIQopGpKInzzWkxbXPjzADTxxPRn6Anap+jsWGxUqT/O4PmWJ55pHggdRSQRaeRJ7gk6IV0F++gYCWtAhoyW8gsllMEnkihUVQ1zcI6voGAbW3CKi9QeAlqRMkznKWs5yFKnCt1RtPmeSwOKhjUt6bjhtdYXjdS34XXMyhfGmw/LdXfIkZHefLXjFg523lSWIAsTCoY/KABnn9Z87w59n76/GpQPYDHqo6qWRExKOPPhzwcHZmlXiUWAF99JFEgsyIrOjbHg4ISakt38nyedugk/e96fO2j2yPRfKCyO9yj8mf7w+dbFtMQhfrx9d+FataY25GrxInScrdokie8j/PB7KUH7TsOxApPjXZSRAkqmQRZL8DV0gUD0GqSemtvxGTq04urYjv8otFkqhNWSRLFUF9rPhkrq4nJ3y9FC+x0lWZ9n8K5Jm/9q9iqX1bTZm1cSzOcui7lsexTP6g0fKXOloWh/EC0Ub+iIkSSaWwgCSoRMnKUvB5tHdW43VCe71K4OxiP05pquDQ3p2Upn1wcqXPlOD/ljFojV8z68PT0aA0y15VsdcrJ2w/ZWLvpJywy1b/hI6zlAlcm9bfxnLoW0/8j8jP0rT8BbiGn0GEt6i4AAAAAElFTkSuQmCC" />
                            </defs>
                        </svg>
                    </div>
                    <div class="panier">Panier
                        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="41"
                            height="41" viewBox="0 0 41 41" fill="none">
                            <rect width="41" height="41" fill="url(#pattern0)" />
                            <defs>
                                <pattern id="pattern0" patternContentUnits="objectBoundingBox" width="1" height="1">
                                    <use xlink:href="#image0_358_15" transform="scale(0.0025)" />
                                </pattern>
                                <image id="image0_358_15" width="400" height="400"
                                    xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAZAAAAGQAQMAAAC6caSPAAAAAXNSR0IB2cksfwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAZQTFRFAAAA////pdmf3QAAAAJ0Uk5TAP9bkSK1AAAEL0lEQVR4nO3cQW6cMBQG4EFesOQIPgpHs4+G1It41226S6RoaAxJlfB+v9ffmng8EV50AfmYMTb+jWF6uZylz+IST554cqXJuEaeJJZM6zNL/LpWkMiTRJJ5XV95wlYmrHRlMkkceRNsZTIhK7ORyBPuAgh8ZSa+Mo6vzLAR7gKYG1ZmoUxFy9RWhhvN9sokygS+Mr5hyyTKtKxMZMjQsDJcnxlrh6ZEkTYt43gyVARA4ImnG2arDEkGnuTKsGTiw9zx5FJBAk8mfso09kocG2Udk6Fjkn4KubCDcs8k8LdY3ZK5X8Le+r1lX7eEXi1oRWpi7D/KY5CxH/K16dxDk9fHIMNDk8OAakeyGIPt5GtDwvEvxIZ+iBVjohns5LsbMWJMzli7JWbydUucuPearEjuloziD+SWuxD5zc1b3kk0XLfEvOXtlsirw7yzlJPvTggYgVsRPcYqCEhGKyxvRfQYqyDgjLYhVow9EjFiDK1tdUvkOPWlyNxrR9QYqyAoGNsQI8Yeihgxhlq6W2KsQqOlrTqS7k7QLVEd0WIM3njdnMAorSJajEGiJ99diRZjkOjJB8+nRdK9iLoKjfu5RRZElBhrQ1DuVRIlxjBRk+/OBGxViZp8+Ba6W4Jr+F7w6TQI6k1qvrYhuJsbBF3lTks+TNSwrCB4kFPzFS9rVhA1LIuEWH5vScKtCTw1N/8UGD6zSuAYrxM4lBok8mThSeIJahiDoIbxOkENYxDUMAZBDVNBrKe8ERil5EdtC0dyN08kmXnieTLx77KMPHHsC9Ybod+ZqCL0CxAVJPBk7vhljp9E4klIQopGpKInzzWkxbXPjzADTxxPRn6Anap+jsWGxUqT/O4PmWJ55pHggdRSQRaeRJ7gk6IV0F++gYCWtAhoyW8gsllMEnkihUVQ1zcI6voGAbW3CKi9QeAlqRMkznKWs5yFKnCt1RtPmeSwOKhjUt6bjhtdYXjdS34XXMyhfGmw/LdXfIkZHefLXjFg523lSWIAsTCoY/KABnn9Z87w59n76/GpQPYDHqo6qWRExKOPPhzwcHZmlXiUWAF99JFEgsyIrOjbHg4ISakt38nyedugk/e96fO2j2yPRfKCyO9yj8mf7w+dbFtMQhfrx9d+FataY25GrxInScrdokie8j/PB7KUH7TsOxApPjXZSRAkqmQRZL8DV0gUD0GqSemtvxGTq04urYjv8otFkqhNWSRLFUF9rPhkrq4nJ3y9FC+x0lWZ9n8K5Jm/9q9iqX1bTZm1cSzOcui7lsexTP6g0fKXOloWh/EC0Ub+iIkSSaWwgCSoRMnKUvB5tHdW43VCe71K4OxiP05pquDQ3p2Upn1wcqXPlOD/ljFojV8z68PT0aA0y15VsdcrJ2w/ZWLvpJywy1b/hI6zlAlcm9bfxnLoW0/8j8jP0rT8BbiGn0GEt6i4AAAAAElFTkSuQmCC" />
                            </defs>
                        </svg>
                    </div>
                    
                </div>
            </div>
            <div id="bottomSearchBar">
                <div id="contentBottomNavBarFirst">
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
                <div id="contentBottomNavBarSecond">
                    <div class="contact">
                        Contactez-nous
                    </div>
                    <div class="aide">
                        Aide
                    </div>
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
    background-color: white;
}

#logo {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;

    width: 15vw;
    height: 100%;
}

#logo img {
    width: 11vw;
    margin-bottom: 1vw;
    cursor: pointer;
    
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

    border-left: 7.2vh solid transparent;
    border-top: 7.2vh solid var(--color-grey-100, #D9D9D9);
    width: 0;
    height: 0;

    left: -7.2vh;
    top: 0;
}

#topSearchBar #buttonMenuNavBar {
    display: flex;
    align-items: center;
    justify-content: center;

    height: 100%;

    border-radius: 1vw;
}

#topSearchBar #buttonMenuNavBar div {
    cursor: pointer;
    min-width: 10rem;
    padding: 0.5rem;
    margin-right: 1rem;
    color: white;
}

.panier {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 10vw;
    height: 80%;

    border-radius: 1vw;
    padding-left: 1rem;
    padding-right: 1rem;

    background-color: blue;
}

.panier svg {
    max-height: 70%;
}

.compte {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 10vw;
    height: 80%;

    border-radius: 1vw;
    padding-left: 1rem;
    padding-right: 1rem;

    background-color: red;
}

.compte svg {
    max-height: 70%;
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
}

#bottomSearchBar #contentBottomNavBarFirst .promos:hover,
#bottomSearchBar #contentBottomNavBarFirst .promos:hover svg,
#bottomSearchBar #contentBottomNavBarFirst .promos:hover svg line,
#bottomSearchBar #contentBottomNavBarFirst .promos:hover svg path,
#bottomSearchBar #contentBottomNavBarFirst .promos:hover svg rect,
#bottomSearchBar #contentBottomNavBarFirst .promos:hover svg circle {
    color: #003249;
    fill: #003249;
    stroke: #003249;
}

#bottomSearchBar #contentBottomNavBarSecond div {
    cursor: pointer;
    font-weight: 600;
    margin-right: 1vw;
}
</style>