<template>
  <div>
    <div class="container">
      <img :src="movieImgSrc" alt="영화이미지" />
      <div id="rank" class="d-flex align-items-end">
        <h4 class="m-2">{{ movie[0].title }}⭐ : {{ movie[0].vote_average / 2 }}</h4>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieDetail",
  computed: {
    movie: function () {
      return this.$store.state.searchedMovie;
    },
    movieImgSrc: function () {
      return this.movie[0].poster_path;
    },
  },
};
</script>

<style>
.container {
  position: relative;
  display: block;
  width: 100%;
  height: 20rem;
  overflow: hidden;
  border-top-left-radius: .3rem;
  border-top-right-radius: .3rem;
}
.container img {
  position: absolute;
  width: 100%;
  height: auto;
  top: 0;
  left: 0;
  margin-top: -10%;
  filter: opacity(80%);
}
#rank {
  position: absolute;
  height: 3em;
  width: 100%;
  bottom: 0;
  left: 0;
  background-color: black;
  filter: opacity(80%);
  color: white;
  font-size: 1em;
}
</style>