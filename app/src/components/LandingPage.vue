<template>
    <div class="content bg">
        <img src="https://thenextweb.com/wp-content/blogs.dir/1/files/2015/06/uxdesign.jpg">
        <div class="overlay"></div>
        <div class="page-title">
            Good vs Bad UI
            <div class="page-subtitle">Can you tell the difference?</div>
            <button class="special" @click="tryNow">Try now</button>
        </div>
    </div>
</template>

<script>
  export default {
    name: 'landingPage',
    data () {
      return {

      }
    },
    methods: {
      tryNow() {
        this.$router.push('/Button');
      }
    }
  }
</script>

<style lang="scss">
    .bg {
        width: calc(100% - 250px);
        margin-left: 250px;
        height: 100%;
        position: relative;
    }

    .bg img {
        height: 100%;
    }

    .overlay {
        position: absolute;
        top: 0;
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,0.7);
    }

    .page-title {
        height: 210px;
        width: 600px;
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        margin: auto;
        color: #fff;
        text-align:center;
        font-size: 70px;
    }

    .page-subtitle {
        color: #fff;
        font-size: 40px;
    }

    button.special {
        margin-top: 20px;
        background: #F62459;
        color: #fff;
    }

    button.special:hover {
        background: #e52357;
    }
</style>
