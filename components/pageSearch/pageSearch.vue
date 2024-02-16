<template>
	<!-- 顶部 搜索栏 -->
	<view class="search-bar">
		<uni-row>
			<uni-col>
				<u-search v-model="query" placeholder="请输入搜索内容" 
				:clearabled="true" @clear="clear"
				:show-action="true" action-text="搜索" 
				:action-style="searchButton" 
				@search="search" @custom="search" 
				></u-search>
			</uni-col>
		</uni-row>
	</view>
</template>

<script>
	export default {
		name: "pageSearch",
		data() {
			return {
				// 搜索内容
				query: "",
				// 搜索按钮class
				searchButton: {
					color: "white"
				}
			};
		},
		methods: {
			search(query) {
				uni.showToast({
					title: "模块建设中",
					icon: 'none'
				})
				this.query = ''
			},
			clear() {
				this.query = ''
				uni.showToast({
					title:  "模块建设中",
					icon: 'none'
				})
			}
		},
		onBackPress() {
			// #ifdef APP-PLUS
			plus.key.hideSoftKeybord();
			// #endif
		}
	}
</script>

<style lang="scss" scoped>
	.search-bar {
		display: flex;
		flex-direction: column;
		padding: 10px 30px 10px 30px;
		
		background-image: url("@/static/images/common/search/bg.png");
		background-position: center center;
		background-size: cover;
		margin-left: -20px;
		margin-right: -20px;
	
		border-bottom: #413430 groove 5px;
	}
</style>