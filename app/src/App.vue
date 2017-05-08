<template>
  <div id="app">
    <nav>
      <div id="logo">Good vs Bad UI</div>
      <router-link :to="'/' + c" v-for="(c,i) in categories" :key="i" :class="{ active: c === active}">
        <div class="category" @click="active = c">{{ c }}</div>
      </router-link>
    </nav>
    <router-view :key="$route.fullPath"></router-view>
  </div>
</template>

<script>
import examples from './examples';

export default {
  name: 'app',
  data () {
    return {
      categories: Object.keys(examples),
      active: 'Button'
    }
  },
  mounted() {
    let category = this.$route.params['category'];
    if (category) {
      this.active = this.$route.params['category'];
    }
  }
}
</script>

<style lang="scss">
  * {
    font-family: 'Open Sans', sans-serif;
    color: #333;
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    vertical-align: top;
  }

  h1 {
    text-align: center;
    margin: 60px 0;
  }

  a {
    text-decoration: none;
  }

  html, body {
    height: 100%;
    width: 100%;
    background: #f5f5f5;
  }

  nav {
    height: 100%;
    width: 250px;
    position: fixed;
    left: 0; top: 0;
    background: #fff;
    border-right: 1px solid #ccc;
  }

  #logo {
    width: 100%;
    height: 60px;
    line-height: 60px;
    text-align: center;
    color: #F62459;
    font-weight: 600;
    font-size: 20px;
    border-bottom: 1px solid #ccc;
    margin-bottom: 20px;
  }

  .category {
    padding: 10px 20px;
    cursor: pointer;
  }

  .category:hover, a.active .category {
    background: #ececec;
    color: #F62459;
  }

  .material-icons {
    font-family: 'Material Icons', sans-serif;
    font-weight: normal;
    font-style: normal;
    font-size: 24px;  /* Preferred icon size */
    display: inline-block;
    line-height: 1;
    text-transform: none;
    letter-spacing: normal;
    word-wrap: normal;
    white-space: nowrap;
    direction: ltr;

    /* Support for all WebKit browsers. */
    -webkit-font-smoothing: antialiased;
    /* Support for Safari and Chrome. */
    text-rendering: optimizeLegibility;

    /* Support for Firefox. */
    -moz-osx-font-smoothing: grayscale;

    /* Support for IE. */
    font-feature-settings: 'liga';
  }

</style>
