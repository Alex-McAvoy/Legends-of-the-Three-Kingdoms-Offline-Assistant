<template>
	<view class="military-container">
		<!-- 武将图容器 -->
		<view class="military-image-container" @click="preView">
			<!-- 边框盒子 -->
			<view class="border-box">
				<image class="border-image" :src="militaryBorder" mode="widthFix"></image>
			</view>
			<!-- 组件盒子 -->
			<view class="component-box">
				<!-- 势力盒子 -->
				<view class="force-box">
					<image class="force-image" :src="militaryForce" mode="widthFix"></image>
				</view>
				<!-- 勾玉盒子 -->
				<view class="magatama-box">	
					<view v-if="item.magatama.actual>10" class="magatama">
						<image class="magatama-image" :src="militaryMagatama"
							mode="widthFix"></image>
						<view class="magatama-text">×{{item.magatama.actual}}</view>
					</view>
					<view v-else class="magatama">
						<image v-for="index in item.magatama.actual" class="magatama-image" :src="militaryMagatama"
							mode="widthFix"></image>
						<image v-for="index in item.magatama.blank" class="magatama-image" :src="militaryMagatamaBlank"
							mode="widthFix"></image>
					</view>
				</view>
			</view>
			<!-- 武将图盒子 -->
			<view class="military-image-box">
				<image class="military-image" :src="item.imgSrc" mode="widthFix"></image>
			</view>
		</view>
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
					<view class="skill-name" :style="{backgroundImage: 'url('+skillBackground+')', color: skillFontColor }">
						{{skill.name}}
					</view>
					<!-- 技能描述 -->
					<view class="skill-description">{{skill.descriptions}}</view>
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
				// 武将边框图
				militaryBorder: "/static/images/common/militaryGeneral/border.png",
				// 武将势力图
				militaryForce: "",
				// 武将技能背景图
				skillBackground: "",
				// 武将技能字体颜色
				skillFontColor: "",
				// 武将勾玉图
				militaryMagatama: "",
				// 武将空白勾玉图
				militaryMagatamaBlank: "/static/images/common/militaryGeneral/magatama_blank.png",
				// 技能分隔图
				skillDivideImgSrc: "/static/images/common/militaryGeneral/divide_skill.png",
				// 台词分隔图
				dialogueDivideImgSrc: "/static/images/common/militaryGeneral/divide_dialogue.png"
			};
		},
		mounted() {
			// 动态加载武将技能背景图
			this.skillBackground = require('@/static/images/common/militaryGeneral/skill_' + this.$props.item.force +
				'.png')
			// 动态加载武将技能字体颜色
			if(this.$props.item.force == "shen"){
				this.skillFontColor = "white"
			} else {
				this.skillFontColor = "black"
			}
			// 动态加载武将势力图
			this.militaryForce = require('@/static/images/common/militaryGeneral/force_' + this.$props.item.force +
				'.png')
			// 动态加载武将勾玉图
			this.militaryMagatama = require('@/static/images/common/militaryGeneral/magatama_' + this.$props.item.force +
				'.png')
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
	.military-container {
		display: flex;
		flex-direction: column;
		margin: 30rpx;
		padding: 20px;

		background-color: blanchedalmond;
		background-image: url("@/static/images/common/archive/list_bg.png");
		background-position: center;
		background-repeat: no-repeat;
		background-attachment: fixed;
		background-size: cover;

		box-shadow: 3px -3px 5px rgba(0, 0, 0, 0.5);
		border-radius: 10px;
		border-style: groove;
		border-color: #413430;

		/* 武将图容器 */
		.military-image-container {
			display: grid;
			grid-template-columns: 1fr 4fr 1fr;
			grid-template-rows: 8fr;

			/* 武将边框盒子 */
			.border-box {
				grid-area: 1/2/2/2;
				z-index: 2;

				/* 武将边框图 */
				.border-image {
					width: 100%;
					height: auto;
					align-self: center;
					box-shadow: 0 -3px 5px rgba(0, 0, 0, 0.5);
					border-radius: 5%;
				}
			}

			/* 组件盒子 */
			.component-box {
				grid-area: 1/2/2/2;
				z-index: 3;
				display: grid;
				grid-template-columns: 2fr 6fr 2fr;
				grid-template-rows: 2fr 8fr;

				/* 武将势力盒子 */
				.force-box {
					grid-area: 1/1/1/1;
					z-index: 3;

					/* 武将势力图 */
					.force-image {
						width: 100%;
						height: auto;
						align-self: center;
					}
				}

				/* 武将勾玉盒子 */
				.magatama-box {
					grid-area: 1/2/1/2;
					z-index: 3;

					.magatama {
						display: flex;
						flex-direction: row;

						/* 勾玉图 */
						.magatama-image {
							width: 10%;
							height: auto;
							margin-top: 5px;
							align-self: center;
						}
						
						/* 勾玉文本 */
						.magatama-text {
							color: white;
						}
					}
				}

			}


			/* 武将盒子 */
			.military-image-box {
				grid-area: 1/2/2/2;
				z-index: 0;

				/* 武将图 */
				.military-image {
					width: 100%;
					height: auto;
					align-self: center;
					border-radius: 5%;
				}
			}
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
				font-family: heiTi;
				color: black;
				font-size: 30px;
				font-weight: bold;
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