<template>
  <div id="app">
    <nav>
      <div id="logo">Good vs Bad UX</div>
      <router-link to="/" v-for="(c,i) in categories" key="i">
        <div class="category">{{ c }}</div>
      </router-link>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      categories: ["Button", "Dialog", "404 page", "Search", "Navigation", "Form", "Chat", "Notification", "Map", "List"]
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
    background: #ececec;
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

  .category:hover {
    background: #ececec;
    color: #F62459;
  }
</style>
