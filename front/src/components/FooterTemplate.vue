<template>
    <div class="footer">
        <div id="logoFooter">
            <img src="../assets/logo.png" alt="logo Lako Lako" draggable="false" onclick="document.location = '/'">
        </div>
        <div id="contentAllfooter">
            <div id="backgroundFooter">
                <div id="contentFooter">
                    <div id="siteMap" class="listContentFooter">
                        <div class="title">
                            Plan du site
                        </div>
                        <div>
                            <span class="linkNav">Accueil</span>
                        </div>
                        <div>
                            <span class="linkNav">Produits</span>
                        </div>
                        <div>
                            <span class="linkNav">À propos</span>
                        </div>
                        <div>
                            <span class="linkNav">Mentions légales</span> & <span class="linkNav">CGV</span>
                        </div>
                        <div>
                            <span class="linkNav">Aide</span>
                        </div>
                    </div>
                    <div id="contact" class="listContentFooter">
                        <div class="title">
                            Contact
                        </div>
                        <div>
                            <span class="linkNav">contact.client@lako-lako.fr</span>
                        </div>
                        <div>
                            <span class="linkNav">09 84 65 75 35</span>
                        </div>
                        <div>
                            <span class="linkNav">Contact</span>
                        </div>
                        <div id="socialMedia">

                        </div>
                    </div>
                    <div id="horaire" class="listContentFooter">
                        <div class="title">
                            Horaires
                        </div>
                        <div>
                            <span>Lundi au Vendredi</span>
                        </div>
                        <div>
                            <span>9h30 - 18h</span>
                        </div>
                        <div id="horaireJour">
                            <span>Samedi</span>
                        </div>
                        <div>
                            <span>9h30 - 12h</span>
                        </div>
                    </div>
                    <div id="agrement" class="listContentFooter">
                        <div class="title">
                            Agrément & Habilitation
                        </div>
                        <div>
                            <span>Numéro d’agrément : 15746</span>
                        </div>
                        <div>
                            <span>Numéro d’habilitation : 657287</span>
                        </div>
                    </div>
                    <div id="copyright">
                        Copyright © 2023 Lako Lako. Tous droits réservés
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
.footer {
    position: relative;
    z-index: 99;
    bottom: 0;
    display: flex;
    flex-direction: row;
    align-items: flex-end;

    height: 10rem;
    width: 100vw;

    background-color: white;
    border-top: solid 2px #D9D9D9;
    color: black;
}

#logoFooter {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;

    width: 15vw;
    height: 100%;
}

#logoFooter img {
    max-width: 24.5rem;
    margin-bottom: 1vw;
    cursor: pointer;
    margin-bottom: 2rem;
    margin-left: 2rem;
    max-height: 10rem;
}

#contentAllfooter {
    display: flex;
    flex-direction: column;
    align-items: flex-end;

    width: 85vw;
    height: 100%;
}

#backgroundFooter {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;

    width: 76vw;
    height: 100%;

    list-style-type: none;
    background-color: #D9D9D9;
    position: relative;
}

#backgroundFooter::after {
    content: "";
    display: block;
    position: absolute;

    border-left: 10rem solid transparent;
    border-top: 10rem solid var(--color-grey-100, #D9D9D9);
    width: 0;
    height: 0;

    left: -10rem;
    top: 0;
}

#contentFooter {
    display: flex;
    flex-direction: row;
    align-items: space-between;
    justify-content: space-around;

    width: 100%;
    height: 100%;

    /* margin-right: 5rem; */
}

#contentFooter .listContentFooter {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;

    width: 25%;
    height: 100%;
}

#contentFooter .listContentFooter div {
    width: 80%;
    text-align: center;
    font-size: 0.7rem;
    font-weight: bold;
}

#contentFooter .listContentFooter .title {
    font-size: 1.2rem;
    font-weight: bold;
    margin-bottom: 0.5rem;
    margin-top: 0.5rem;
}

#contentFooter .listContentFooter #horaireJour {
    margin-top: 0.6rem;
}



#contentFooter #copyright {
    position: absolute;
    bottom: 0;
    right: 0;
    margin-right: 2rem;
    margin-bottom: 0.5rem;
    font-size: 0.7rem;
}

/* LINK */
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

/* LINK */
</style>

<script>

export default {
    name: 'FooterTemplate'
}

</script>