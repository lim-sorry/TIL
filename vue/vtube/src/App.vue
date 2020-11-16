<template>
  <div>
    <header class="d-flex align-items-center m-2">
      <div class="d-flex align-items-center">
        <img class="mx-3" src="@/assets/Logo.png" width="50rem" alt="">
        <h4>Vuetube</h4>
      </div>
      <SearchBar @search-input="searchInput"/>
    </header>
    <section class="d-flex justify-content-start">
      <VideoDetail :video="video"/>
      <VideoList :videos="videos" @select-video="selectVideo"/>  
    </section>
  </div>
</template>

<script>
import SearchBar from "@/components/SearchBar.vue"
import VideoList from "@/components/VideoList.vue"
import VideoDetail from "@/components/VideoDetail.vue"
import axios from "axios"
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

const YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search'
const YOUTUBE_COMMENT_URL = 'https://www.googleapis.com/youtube/v3/commentThreads'
const YOUTUBE_API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY

export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  data: function () {
    return {
      videos: [],
      video: '',
    }
  },
  methods: {
    searchInput (query) {
      axios.get(YOUTUBE_API_URL, {
        params: {
          key: YOUTUBE_API_KEY,
          part: 'snippet',
          type: 'video',
          q: query,
        }
      })
      .then(res => {
        this.videos = res.data.items
        this.selectVideo(this.videos[0])
      })
      .catch(err => console.log(err))
    },
    selectVideo (video) {
      this.video = video
      this.getComments(this.video.id.videoId)
    },
    getComments (videoId) {
      axios.get(YOUTUBE_COMMENT_URL, {
        params: {
          key: YOUTUBE_API_KEY,
          textFormat: 'plainText',
          part: [
            'snippet',
            'replies',
          ],
          videoId: videoId,
          maxResults: 50,
        }
      })
      .then(res => {
        console.log(res)
      })
      .catch(err => console.log(err))
    },
  }
}
</script>

<style>

</style>
