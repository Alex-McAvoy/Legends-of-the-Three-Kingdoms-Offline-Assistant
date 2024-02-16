<template>
	<view class="main">
		<u-sticky>
			<page-search></page-search>
		</u-sticky>
		<view class="container">
			<h1>模块建设中</h1>
		</view>
		<mine-tabbar :current="0"></mine-tabbar>
	</view>
</template>

<script>
	export default {
		data() {
			return {}
		},
		onLoad() {
			// 隐藏原生tabbar
			uni.hideTabBar({})
		},
		methods: {}
	}
</script>

<style lang="scss" scoped>
	.container {
		margin-top: 80px;
	}
</style>