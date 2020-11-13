<template>
  <div class="search-bar" :style="{ margin: videosLength ? '0' : '40vh 0' }">
    <input @keypress.enter="onEnter" type="text">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  props: {
    videosLength: {
      type: Number,
    },
  },
  methods: {
    onEnter: function (event) {
      this.$emit('search-input', event.target.value)
    },
  },
}
</script>

<style>
.search-bar {
  transition: margin .5s;
}

.search-bar > input {
  width: 100%;
  padding: .5rem;
  font-size: 1.2rem;
}
</style>