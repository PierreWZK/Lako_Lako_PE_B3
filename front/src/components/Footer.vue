<template>
    <div class="footer">
        <h4 class="text">Copyright Nous en 2023</h4>
        <h4 class="text">Mentions légales <a>Contacts</a></h4>
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
.footer{
    background-color: #9B9B9B;
    position: fixed;
    bottom: 0;
    width: 100%;
}
.text{
    text-align: center;
    padding: 0;
    margin: 0.5em;
}
</style>