<template>
	<view v-if="src" class="audio-container">
		<view class="audio-box" @click="start(audioId)">
			<image src="/static/images/common/militaryGeneral/play.png" class="icon" v-show="!status"></image>
			<image src="/static/images/common/militaryGeneral/pause.png" class="icon" v-show="status"></image>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				duration: 0,
				status: false
			}
		},
		props: {
			// 音频地址
			src: String,
			// 必填，且id不可为数字0，建议格式：audio+数字
			audioId: [String, Number]
		},
		created() {
			//初始化音频
			this.context = uni.createInnerAudioContext();
			// 设置音频地址
			this.context.src = this.src;
			// 进入可播放状态
			this.onCanplay();
			// 设置播放结束
			this.onEnded();
			uni.$on("stop", (id) => {
				if (id && id != this.audioId) {
					this.context.stop();
					this.status = false;
				} else if (!id) {
					this.context.stop();
					this.status = false;
				}
			})
		},
		methods: {
			// 点击播放
			start(id) {
				this.context.play()
				let audioId = id;
				if (this.status) {
					this.context.pause();
					this.status = !this.status;
				} else {
					uni.$emit("stop", id)

					this.status = !this.status;
				}
			},
			onCanplay() { //进入可播放状态
				this.context.onCanplay(() => {
					this.context.duration;
					setTimeout(() => {
						this.duration = this.context.duration;
					}, 1000)
				})
			},
			// 播放结束
			onEnded() {
				this.context.onEnded(() => {
					this.status = false;
				})
			}
		}
	}
</script>

<style lang="scss" scoped>
	.audio-container {
		
		display: flex;
		flex-direction: row;
		justify-content: center;
		align-items: center;
	
		width: 38rpx;
		height: 38rpx;
		
		.audio-box {
			.icon {
				width: 38rpx;
				height: 38rpx;
				
				background-color: #f8f9fa;
				cursor: pointer;
				border-radius: 50%;
				border: 1px solid #dddddd;
				box-sizing: border-box;
			}
		}
	}
</style>