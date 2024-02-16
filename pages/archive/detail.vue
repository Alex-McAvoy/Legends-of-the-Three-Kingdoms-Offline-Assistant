<template>
	<view class="main">
		<!-- 吸顶 -->
		<u-sticky>
			<!-- 导航栏 -->
			<mine-navbar :title="navbarTitle"></mine-navbar>
			<!-- 搜索栏 -->
			<page-search class="page-search"></page-search>
		</u-sticky>
		
		<military-general :item="military"></military-general>
		
		<mine-tabbar :current="-1"></mine-tabbar>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				// 导航栏title
				navbarTitle: '',
				// 武将
				military: {
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
			};
		},
		onLoad(option) {
			// 所有武将数据
			const militariesData = require("@/static/json/online/militaryGeneral.json")
			// 所属包id
			const packageId = option.index
			// 武将id
			const militaryId = option.id
			// 获取当前武将数据
			this.military = militariesData[packageId].militaries[militaryId]

			// 修改导航栏
			this.navbarTitle = this.military.name
		},
		methods: {

		}
	}
</script>

<style lang="scss" scoped>
	
</style>