<template>
	<view>
		<u-navbar :title="title" height="44" :autoBack="true" :placeholder="true" :bgColor="navbarVar.bgColor"
			:titleStyle="navbarVar.titleStyle">
			<view class="u-nav-slot" slot="left">
				<u-icon name="/static/images/common/narbar/arrow.png" size="20"></u-icon>
			</view>
		</u-navbar>
	</view>
</template>

<script>
	export default {
		name: "mineNavbar",
		props: {
			// title
			title: {
				type: String,
				default: ""
			}
		},
		data() {
			return {
				// 导航栏
				navbarVar: {
					// 背景色
					bgColor: "#1e1b1b",
					// 文字样式
					titleStyle: {
						"font-family": "heiTi",
						"font-size": "20px",
						"font-weight": "bold",
						"-webkit-background-clip": "text",
						"-webkit-text-fill-color": "transparent",
						"textShadow": "0px 0px 7px rgba(52, 255, 204, 0.1)",
						"background-image": "-webkit-linear-gradient(top, #aca08d,#f3f1f4,#b9b196)",
					}
				},
			};
		}
	}
</script>

<style lang="scss" scoped>
</style>