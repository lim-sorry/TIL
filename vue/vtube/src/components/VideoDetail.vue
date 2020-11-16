<template>
  <div class="iframe50 m-3" v-if="video">
    <iframe class="iframe50" :src="videoSrc" frameborder="0"></iframe>
    <h4 class="my-3">{{ video.snippet.title | unescape }}</h4>
    <p>{{ video.snippet.description }}</p>
    <hr>
  </div>
</template>

<script>
import _ from "lodash"

export default {
  name: 'VideoDetail',
  props: {
    video: [Object, String],
  },
  computed: {
    videoSrc () {
      return `http://www.youtube.com/embed/${this.video.id.videoId}`
    }
  },
  filters: {
    unescape (text) {
      return _.unescape(text)
    }
  }
}
</script>

<style>
.iframe50 {   
  display: block;   
  border: none;   
  height: 60vh;   
  width: 60vw; 
}
</style>