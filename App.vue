<script>
	export default {
		onLaunch: function() {
		},
		onShow: function() {
		},
		onHide: function() {
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
	
	
	/* 黑体 */
	@font-face {
		font-family: heiTi;
		src: url("@/static/font/heiTi.ttf");
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