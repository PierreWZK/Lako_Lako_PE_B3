/* eslint-disable */
<template>
    <h1>{{ msg }}</h1>
    <div class="header">
        <ul>
            <li>
                logo
            </li>
            <li>rechercher</li>
            <li>articles</li>
            <li>
                Compte
            </li>
            <li>Panier</li>
        </ul>
    </div>
</template>

<script>

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}

</script>

<style>
.header{
    display: flex;
    background-color: lightcoral;
}
ul{
    display: flex;
    background-color: lightblue;
    width: 100%;
}
</style>