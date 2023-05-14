<template>
    <div id="global">
        <div id="loginBox">
            <div id="login">
                <h1>Merci de nous faire confiance</h1>
                <form id="form">
                    <label>
                        <h3>Identifiant</h3>
                    </label>
                    <input id="formInputIdentifiant" type="text" v-model="username">
                    <label>
                        <h3>Email</h3>
                    </label>
                    <input id="formInputEmail" type="email" v-model="email">
                    <label>
                        <h3>Mot de passe</h3>
                    </label>
                    <input id="formInputPassword" type="password" v-model="password">
                    <div style="align-self: center; padding: 1em;">
                        <button type="submit" id="bouton">
                            <h2>S'inscrire</h2>
                        </button>
                    </div>
                </form>
                <div style="width: 80%">
                    <div
                        style="width:100%; text-align:center; border-bottom: 3px solid lightgray; line-height:0.1em; margin:10px 0 20px;">
                        <span style="background:#A9A9A9; padding:0 10px; color: white;" value="1">
                            ou s'inscrire avec
                        </span>
                    </div>
                </div>
                <div id="otherAccounts">
                    <img class="logoConnection" src="../assets/google.jpg" alt="google" width="50px"
                        style="border-radius: 100%;">
                    <img class="logoConnection" src="../assets/facebook.png" alt="facebook" width="50px">
                    <img class="logoConnection" src="../assets/twitter.png" alt="twitter" width="50px">
                </div>
                <span style="padding: 1em;" class="login"><router-link to="/login">Vous avez déjà un compte ? Se
                        connecter</router-link></span>
            </div>
            <div id="contentImgMeuble">
                <img src="../assets/meuble1.png" alt="produit1" draggable="false">
            </div>
        </div>
    </div>
</template>
  
<style>
#global {
    display: flex;
    width: 100%;
    justify-content: center;
}

#loginBox {
    margin: 1em;
    background: #a9a9a9;
    display: flex;
    flex-direction: row;
    align-items: center;
    width: 70%;
    border-radius: 30px;
    height: 50em;
    box-shadow: 10px 10px 5px grey;
}

#login {
    color: white;
    width: 50%;
    display: flex;
    flex-direction: column;
    align-items: center;
}

#form {
    display: flex;
    width: 80%;
    flex-direction: column;
}

#formInputIdentifiant,
#formInputEmail,
#formInputPassword {
    border-bottom: 1px solid lightgrey;
}

#bouton {
    background: #007ea7;
    border: none;
    border-radius: 5px;
    color: white;
    padding-right: 1em;
    padding-left: 1em;
}

#bouton:hover {
    cursor: pointer;
}

#contentImgMeuble {
    width: 50%;
    height: 100%;
}

#contentImgMeuble img {
    object-fit: cover;
    width: 100%;
    height: 100%;
    border-radius: 0 30px 30px 0;
}

#otherAccounts {
    width: 80%;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    margin: 1em;
}

.login a {
    color: #FFF;
    text-decoration: none;
}

.login a:hover {
    color: #007ea7;
    text-decoration: underline;
}

.logoConnection {
    cursor: pointer;
}
</style>
  
<script>
export default {
    name: 'Login'
}

window.onload = function () {
    // Récupère le 'formInputIdentifiant' et créer un cookie avec la valeur de l'input (si l'input existe)
    if (document.getElementById('formInputIdentifiant') != null) {
        document.getElementById('formInputIdentifiant').addEventListener('input', function (e) {
            document.cookie = "username=" + e.target.value;
        });
    }

}

</script>