<template>
  <ul>
		<VideoListItem
			v-for="(video, idx) in videos"
			:video="video"
			:key="idx"
			@select-video="selectVideo"
		/>
  </ul>
</template>

<script>
import VideoListItem from "@/components/VideoListItem"

export default {
	name: 'VideoList',
	components: {
		VideoListItem,
	},
	props: {
		videos: Array,
	},
	methods: {
		selectVideo (video) {
			this.$emit('select-video', video)
		}
	}
}
</script>

<style>

</style>