<template>
	<view>
		<u-tabbar :value="current" v-model="current" :list="list" 
		:mid-button="true" @change="change" :border="false"
		            active-color="white"
		            inactiveColor="#e4d9b5"
					>
			<u-tabbar-item class="tabbar"
				v-for="(tabbar, index) in list" 
				:text="tabbar.text" 
				:icon="tabbar.iconPath"
				:key="index">
			</u-tabbar-item>
		</u-tabbar>
	</view>
</template>
<script>
	export default {
		name: "mineTabbar",
		props: {
			current: {
				type: Number,
				default: 0
			}
		},
		data() {
			return {
				// tabbar 列表
				list: [{
						pagePath: "pages/index/index",
						text: "主页",
						iconPath: "home",
						selectedIconPath: "home-fill",
						customIcon: false,
					},
					{
						pagePath: "pages/utils/index",
						text: "工具",
						iconPath: "photo",
						selectedIconPath: "photo-fill",
						midButton: true,
						customIcon: false,
					},
					{
						pagePath: "pages/archive/index",
						text: "武将图鉴",
						iconPath: "photo",
						selectedIconPath: "photo-fill",
						midButton: true,
						customIcon: false,
					},
					{
						pagePath: "pages/card/index",
						text: "卡牌图鉴",
						iconPath: "photo",
						selectedIconPath: "photo-fill",
						midButton: true,
						customIcon: false,
					},
					{
						pagePath: "pages/mine/index",
						text: "我的",
						iconPath: "account",
						selectedIconPath: "account-fill",
						customIcon: false,
					}
				],
				
			};
		},
		methods: {
			change(index) {
				uni.switchTab({
					url: '/' + this.list[index].pagePath
				})
			}
		}
	}
</script>

<style lang="scss" scoped>
	.tabbar {
		background-color: #1e1b1b;
		border-top: #413430 groove 5px;
		font-size: 23px;
	}
</style>