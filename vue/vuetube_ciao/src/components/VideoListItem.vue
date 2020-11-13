<template>
  <li class="video-list-item" @click="selectVideo">
    <img :src="imgSrc" alt="youtube-video-thumbnail">
    <p>{{ video.snippet.title | unescape }}</p>
  </li>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem',
  props: {
    video: {
      type: Object,
    },
  },
  computed: {
    imgSrc: function () {
      return this.video.snippet.thumbnails.default.url
    }
  },
  filters: {
    unescape: function (text) {
      return _.unescape(text)
    }
  },
  methods: {
    selectVideo: function () {
      this.$emit('select-video', this.video)
    }
  }
}
</script>

<style>
.video-list-item {
  display: flex;
  margin-bottom: 1rem;
  cursor: pointer;
}

.video-list-item > img {
  height: fit-content;  /* 텍스트 늘어나도 이미지는 원래 사이즈 유지 */
  margin-right: .7rem;
}
</style>