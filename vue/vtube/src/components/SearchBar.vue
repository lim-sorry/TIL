<template>
  <div class="input-group mx-5 w-75">
    <input @keypress.enter="searchInput" v-model="query" type="text" class="form-control" placeholder="검색">
    <div class="input-group-append">
      <button @click="searchInput" class="btn btn-outline-secondary" type="button">Search</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  data: function () {
    return {
      query: '',
    }
  },
  methods: {
    searchInput () {
      this.$emit("search-input", this.query)
    }
  }
}
</script>

<style>

</style>