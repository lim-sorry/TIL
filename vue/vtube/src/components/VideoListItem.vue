<template>
  <ui class="d-flex m-3" @click="selectVideo">
    <img class="list-thumbnail" :src="imgSrc" alt="">
    <div class="ml-2">
      <span class="d-block">{{ video.snippet.title | unescape }}</span>
      <span class="d-block">{{ video.snippet.channelTitle }}</span>
    </div>
  </ui>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem',
  props: {
    video: Object,
  },
  methods: {
    selectVideo () {
      this.$emit('select-video', this.video)
    }
  },
  computed: {
    imgSrc () {
      return this.video.snippet.thumbnails.default.url
    },
  },
  filters: {
    unescape (text) {
      return _.unescape(text)
    }
  }
}
</script>

<style>
.list-thumbnail {
  width: fit-content;
  height:fit-content;
}
</style>