<template>
  <ul class="video-list">
    <VideoListItem
      v-for="video in videos"
      :key="video.etag"
      :video="video"
      @select-video="onSelectVideo"
    />
  </ul>
</template>

<script>
import VideoListItem from './VideoListItem.vue'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videos: {
      type: Array,
    },
  },
  methods: {
    onSelectVideo: function (video) {
      this.$emit('select-video', video)
    }
  }
}
</script>

<style>
.video-list {
  width: 30%;

  /* ul 태그의 기본 스타일링 없애기 */
  list-style: none;
  padding: 0;
  margin: 0;
}
</style>