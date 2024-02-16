<script>
	export default {
		onLaunch: function() {
			console.log('App Launch')
			uni.hideTabBar({})
		},
		onShow: function() {
			console.log('App Show')
			uni.hideTabBar({})
		},
		onHide: function() {
			console.log('App Hide')
		}
	}
</script>

<style lang="scss">
	/*每个页面公共css */
	@import "@/node_modules/uview-ui/index.scss";

	/* flex布局容器 */
	.main {
		display: flex;
		flex-direction: column;
	}

	/* 华文行楷字体 */
	@font-face {
		font-family: huaWenXingKai;
		src: url("@/static/font/huaWenXingKai.ttf");
	}
	
	/* 方正兰亭粗黑 */
	@font-face {
		font-family: fangZhengLanTing;
		src: url("@/static/font/fangZhengLanTing.ttf");
	}
	
	/* 页面内搜索框 */
	.page-search {
		border-top: #413430 groove 5px;
	}
	
	/* 背景 */
	page{
		background-image: url("@/static/images/common/bg.png");
		background-position: center;
		background-repeat: no-repeat;
		background-attachment: fixed;
		background-size: cover;
	}
</style>