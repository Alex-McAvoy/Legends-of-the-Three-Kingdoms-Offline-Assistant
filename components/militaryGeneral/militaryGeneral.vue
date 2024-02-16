<template>
	<view class="container">
		<!-- 武将图 -->
		<image class="image" :src="item.imgSrc" mode="widthFix" @click="preView"></image>
		<!-- 内容容器 -->
		<view class="content-container">
			<!-- 武将名 -->
			<view class="name">
				<text>{{item.name}}</text>
			</view>
			
			<!-- 介绍容器 -->
			<view class="intro-container">
				<!-- 技能分隔 -->
				<image class="skill-divide" :src="skillDivideImgSrc" mode="widthFix"></image>
				<!-- 技能容器 -->
				<view class="skills-container" v-for="skill in item.skills">
					<!-- 技能名 -->
					<view class="skill-name" :style="{backgroundImage: 'url('+skillBackground+')'}">
						{{skill.name}}
					</view>
					<!-- 技能描述 -->
					<view class="skill-description">{{skill.description}}</view>
				</view>
				<!-- 台词分隔 -->
				<image class="dialogue-divide" :src="dialogueDivideImgSrc" mode="widthFix"></image>
				<!-- 台词容器 -->
				<view class="dialogues-container" v-for="dialogue in item.dialogues">
					<!-- 技能名 -->
					<view class="dialogue-name">
						{{dialogue.name}}
					</view>
					<!-- 台词容器 -->
					<view class="dialogue-description-container">
						<view v-for="(description,index) in dialogue.descriptions" class="dialogue-description">
							<!-- 台词 -->
							<text>{{description}}</text>
							<!-- 音频 -->
							<mine-audio class="dialogue-audio" :src="dialogue.srcs[index]"
								:audio-id="'audio_' + item.index + '_' + index"></mine-audio>
						</view>
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	import mineAudio from "@/components/mineAudio/mineAudio.vue"
	export default {
		name: "militaryGeneral",
		components: {
			mineAudio
		},
		props: {
			item: {
				type: Object,
				default: {
					// id
					id: '',
					// 武将名
					name: '',
					// 武将图片
					imgSrc: '',
					// 技能
					skills: [{
						// 技能名
						name: '',
						// 技能描述
						description: ''
					}],
					// 台词
					dialogues: [{
						// 技能名
						name: "",
						// 台词
						descriptions: [],
						// 音频地址
						srcs: []
					}]
				}
			}
		},
		data() {
			return {
				// 武将技能背景图
				skillBackground: "",
				// 技能分隔图
				skillDivideImgSrc: "/static/images/common/militaryGeneral/skill_divide.png",
				// 台词分隔图
				dialogueDivideImgSrc: "/static/images/common/militaryGeneral/dialogue_divide.png"
			};
		},
		mounted() {
			// 动态加载武将技能背景图
			this.skillBackground = require('@/static/images/common/militaryGeneral/' + this.$props.item.force +
				'_skill.png')
		},
		computed: {
			imgSrc() {
				return this.$props.item.imgSrc
			}
		},
		methods: {
			// 点击查看图片
			preView() {
				uni.previewImage({
					urls: [this.imgSrc],
					longPressActions: true
				})
			}
		}
	}
</script>

<style lang="scss" scoped>
	/* 容器 */
	.container {
		display: flex;
		flex-direction: column;
		margin: 30rpx;
		
		background-color: blanchedalmond;
		background-image: url("@/static/images/common/archive/list_bg.png");
		background-position: center;
		background-repeat: no-repeat;
		background-attachment: fixed;
		background-size: cover;
		padding: 20px;
		margin: 30rpx;
		margin-top: 120rpx;
		box-shadow: 3px -3px 5px rgba(0, 0, 0, 0.5);
		border-radius: 10px;
		border-style: groove;
		border-color: #413430;

		/* 武将图 */
		.image {
			width: 70%;
			height: auto;
			align-self: center;
			box-shadow: 0 -3px 5px rgba(0, 0, 0, 0.5);
		}

		/* 内容容器 */
		.content-container {
			display: flex;
			flex-direction: column;

			margin-top: 10px;
			box-shadow: 0 -3px 5px rgba(0, 0, 0, 0.5);

			background-image: url("@/static/images/common/militaryGeneral/top.png"), url("@/static/images/common/militaryGeneral/bottom.png");
			background-position: top left, bottom right;
			background-repeat: no-repeat;
			background-color: #ffffff;
			padding: 20px;

			/* 武将名 */
			.name {
				font-family: fangZhengLanTing;
				font-size: 30px;
				color: black;
				padding: 20px 10px;
				text-align: center;
			}

			


			/* 介绍容器 */
			.intro-container {
				display: flex;
				flex-direction: column;
				gap: 20px;
				
				/* 技能分隔 */
				.skill-divide {
					justify-self: center;
					align-self: center;
					width: 100%;
					height: auto;
				}

				/* 技能容器 */
				.skills-container {
					display: flex;
					gap: 20px;
					padding-top: 10px;
					font-size: 30rpx;

					/* 技能名 */
					.skill-name {
						flex-shrink: 0;
						align-self: flex-start;
						background-repeat: round;
						width: 70px;
						padding: 5px 0px;

						color: black;
						height: 33px;
						text-align: center;
						padding-right: 4px;
						font-weight: bold;
						font-size: small;

						box-sizing: border-box;
						direction: ltr;
					}

					/* 技能描述 */
					.skill-description {
						align-self: center;
					}
				}
				
				/* 台词分隔 */
				.dialogue-divide {
					justify-self: center;
					align-self: center;
					width: 100%;
					height: auto;
				}

				/* 台词容器 */
				.dialogues-container {
					display: flex;
					gap: 20px;
					padding-top: 10px;
					font-size: 30rpx;

					/* 技能名 */
					.dialogue-name {
						flex-shrink: 0;
						align-self: flex-start;
						background-image: url("@/static/images/common/militaryGeneral/dialogue.png");
						background-repeat: round;
						width: 70px;
						padding: 5px 0px;

						color: white;
						height: 33px;
						text-align: center;
						padding-right: 4px;
						font-size: small;

						box-sizing: border-box;
						direction: ltr;
					}

					/* 台词描述容器 */
					.dialogue-description-container {
						display: flex;
						flex-direction: column;
						justify-content: center;
						align-items: flex-start;
						gap: 20px;

						/* 台词描述 */
						.dialogue-description {
							display: flex;
							flex-direction: row;
							justify-content: center;

							/* 台词音频 */
							.dialogue-audio {
								margin: 5rpx 0px 0px 0px;
							}
						}
					}
				}
			}
		}


	}
</style>