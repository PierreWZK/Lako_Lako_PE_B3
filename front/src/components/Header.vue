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
    list-style-type: none;

    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;

    width: 100%;

    background-color: lightblue;
}

li {
    margin: 0 1rem 0 1rem;
}
</style>