<template>
	<view class="main">
		<!-- 导航栏 -->
		<mine-navbar :title="navbarTitle"></mine-navbar>


		<!-- 标签栏 -->
		<u-tabs :list="lamps" :is-scroll="true" class="tabs" lineColor="#60544a" lineWidth="50"
			:activeStyle="tabsActive" :inactiveStyle="tabsInactive" @click="getLampList">
		</u-tabs>


		<!-- 图鉴 -->
		<view class="container">
			<!-- 背景 -->
			<view class="bg">
				<!-- 大将灯容器 -->
				<view class="lamp-container">
					<!-- 大将灯 -->
					<view :class="lamp.class" class="lamp-icon"></view>
					<!-- 大将灯名 -->
					<view class="lamp-name">{{lamp.name}}</view>
				</view>
				<!-- 横戟分隔 -->
				<image class="divide" :src="divideImgSrc" mode="widthFix"></image>
				<!-- 图鉴容器 -->
				<view class="archive-container">
					<!-- 扩展包容器 -->
					<view v-for="item in lamp.nodes" class="package-container">
						<!-- 扩展包名与小将灯容器 -->
						<view class="package-title-container">
							<!-- 扩展包名 -->
							<view :class="item.titleClass"></view>
							<!-- 小将灯 -->
							<view :class="item.lampClass" class="package-lamp"></view>
						</view>
						<!-- 扩展包武将容器 -->
						<view class="militaries-container">
							<!-- 武将 -->
							<view v-for="military in item.militaries" class="military">
								<view :class="military.avatarClass" @click="getMilitary(military)"></view>
							</view>
						</view>
					</view>
				</view>
			</view>
		</view>
		<!-- 底部导航栏 -->
		<mine-tabbar :current="-1"></mine-tabbar>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				topHeight: 0,
				// 导航栏title
				navbarTitle: '',
				// 所有将灯数据
				lamps: [],
				// 当前将灯数据
				lamp: {},
				// 标签栏选中样式
				tabsActive: {
					padding: '0 10rpx',
					color: '#efe5bf',
					fontWeight: 'bold',
					fontWeight: '600',
					transform: 'scale(1.5)',
				},
				// 标签栏未选中样式
				tabsInactive: {
					padding: '10rpx',
					color: '#efe5bf',
					fontSize: '30rpx',
					fontWeight: '600',
				},
				// 横戟分隔图
				divideImgSrc: "/static/images/common/archive/divide.png",
			};
		},
		onLoad(option) {
			// 三国杀Online
			if (option.index == 0) {
				// 修改导航栏
				this.navbarTitle = "三国杀 Online"

				// 获取将灯数据
				this.lamps = require("@/static/json/online/lamps.json")

				// 获取标准将灯
				this.getLampList(this.lamps[0])
			}
			// 三国杀十周年
			if (option.index == 1) {
				// 修改导航栏
				this.navbarTitle = "三国杀十周年"
			}
			// 三国杀移动版
			if (option.index == 2) {
				// 修改导航栏
				this.navbarTitle = "三国杀移动版"
			}
		},
		methods: {
			// 获取当前将灯列表
			getLampList(item) {
				this.lamp = item
				if (this.lamp.index != 0 && this.lamp.index != 1) {
					uni.showToast({
						title: '模块建设中~',
						icon: "none",
						duration: 2000
					})
				}
			},
			// 点击武将头像跳转武将详情页
			getMilitary(item) {
				uni.navigateTo({
					url: '/pages/archive/detail?index=' + this.lamp.index + '&id=' + item.id
				})
			}
		}
	}
</script>

<style>
	/* 将灯 */
	@import url(@/static/css/online/lamps/biaoZhun.css);
	@import url(@/static/css/online/lamps/shenHuaZaiLin.css);
	
	@import url(@/static/css/online/lamps/cuiCanXingHe.css);
	@import url(@/static/css/online/lamps/guoZhan.css);
	@import url(@/static/css/online/lamps/jieXianTuPo.css);
	@import url(@/static/css/online/lamps/jieYiJiangChengMing.css);
	@import url(@/static/css/online/lamps/menFaShiZu.css);
	@import url(@/static/css/online/lamps/mouKuoZhanBao.css);
	@import url(@/static/css/online/lamps/qiFu.css);
	@import url(@/static/css/online/lamps/SP.css);
	@import url(@/static/css/online/lamps/wenDeWuBei.css);
	@import url(@/static/css/online/lamps/xianDing.css);
	@import url(@/static/css/online/lamps/yiJiangChengMing.css);

	/* 头像 */
	@import url(@/static/css/online/militaryGeneral/biaoZhun.css);
	@import url(@/static/css/online/militaryGeneral/shenHuaZaiLin.css);
</style>
<style lang="scss" scoped>
	/* 标签栏 */
	.tabs {
		height: 80rpx;
		padding: 5px 10px 0px 10px;
		font-family: huaWenXingKai;
		background-color: #2e2b2c;
		border-bottom: #413430 groove 5px;
	}

	/* 图鉴 */
	.container {
		display: flex;
		flex-direction: column;


		/* 背景 */
		.bg {
			background-color: blanchedalmond;
			background-image: url("@/static/images/common/archive/list_bg.png");
			background-position: center;
			background-repeat: no-repeat;
			background-attachment: fixed;
			background-size: cover;
			padding: 20px;
			margin: 30rpx;
			box-shadow: 3px -3px 5px rgba(0, 0, 0, 0.5);
			border-radius: 10px;
			border-style: groove;
			border-color: #413430;

			/* 大将灯容器 */
			.lamp-container {
				display: flex;
				flex-direction: row;
				justify-content: center;
				align-items: center;

				/* 大将灯 */
				.lamp-icon {
					margin-left: -20px;
				}

				/* 大将灯名 */
				.lamp-name {
					font-family: huaWenXingKai;
					color: black;
					font-size: 32px;
					font-weight: bold;
					text-align: center;
				}
			}

			/* 横戟分隔 */
			.divide {
				width: 100%;
				height: auto;
				align-self: center;
			}

			/* 图鉴容器 */
			.archive-container {
				display: flex;
				flex-direction: column;
				justify-content: center;
				align-items: center;

				/* 扩展包容器 */
				.package-container {
					display: flex;
					flex-direction: column;
					justify-content: center;
					align-items: center;

					/* 扩展包名与小将灯容器 */
					.package-title-container {
						display: flex;
						flex-direction: row;
						justify-content: center;
						align-items: center;

						/* 小将灯 */
						.package-lamp {
							margin-left: -40px;
							margin-top: 8px;
						}
					}

					/* 扩展包武将容器 */
					.militaries-container {
						display: flex;
						flex-direction: row;
						flex-wrap: wrap;
						// gap: 20px;
						justify-content: center;
						align-items: center;

						/* 武将 */
						.military {
							margin: 5px;
							box-shadow: 3px -3px 5px rgba(0, 0, 0, 0.5);
						}
					}
				}
			}
		}
	}
</style>