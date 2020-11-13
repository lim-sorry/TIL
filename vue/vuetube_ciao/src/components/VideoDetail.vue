<template>
  <div class="video-detail" v-if="video">

    <div class="video-container">
      <iframe :src="videoUrl" frameborder="0"></iframe>
    </div>

    <h1>{{ video.snippet.title }}</h1>
    <p>{{ video.snippet.description }}</p>
  </div>
</template>

<script>
export default {
  name: 'VideoDetail',
  props: {
    video: {
      type: Object,
    },
  },
  computed: {
    videoUrl: function () {
      return `https://www.youtube.com/embed/${this.video.id.videoId}`
    },
  },
}
</script>

<style>
.video-detail {
  width: 70%;
  margin-right: 1rem;
}

.video-container {
  position: relative;   /* 기준 위치 잡기 */
  padding-top: 56.25%;  /* 비디오 비율 맞추기 */
}

.video-container > iframe {
  position: absolute;  /* container 기준으로 위치 잡기 */
  top: 0;              /* 비율에 맞게 높이 설정 */

  width: 100%;
  height: 100%;
}
</style>