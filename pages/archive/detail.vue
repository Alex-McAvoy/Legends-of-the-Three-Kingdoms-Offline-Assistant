<template>
	<view class="main">
		<!-- 导航栏 -->
		<mine-navbar :title="navbarTitle"></mine-navbar>
		<!-- 武将详情 -->
		<military-general :item="military"></military-general>
		<!-- 底部导航栏 -->
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
			// 所属包id
			const packageId = option.index
			// 武将id
			const militaryId = option.id
			
			if (packageId == 0) {
				// 引入标准武将包数据
				const militariesData = require("@/static/json/online/biaoZhun.json")
				// 获取当前武将数据
				this.military = militariesData.militaries[militaryId]
				// 修改导航栏
				this.navbarTitle = this.military.name
			} else if(packageId == 1) {
				// 引入神话再临武将包数据
				const militariesData = require("@/static/json/online/shenHuaZaiLin.json")
				// 获取当前武将数据
				this.military = militariesData.militaries[militaryId]
				// 修改导航栏
				this.navbarTitle = this.military.name
			} else if(packageId == 2) {
				// 引入一将成名武将包数据
				const militariesData = require("@/static/json/online/yiJiangChengMing.json")
				// 获取当前武将数据
				this.military = militariesData.militaries[militaryId]
				// 修改导航栏
				this.navbarTitle = this.military.name
			} else if(packageId == 3) {
				// 引入界限突破武将包数据
				const militariesData = require("@/static/json/online/jieXianTuPo.json")
				// 获取当前武将数据
				this.military = militariesData.militaries[militaryId]
				// 修改导航栏
				this.navbarTitle = this.military.name
			} else if(packageId == 4) {
				// 引入界·一将成名武将包数据
				const militariesData = require("@/static/json/online/jieYiJiangChengMing.json")
				// 获取当前武将数据
				this.military = militariesData.militaries[militaryId]
				// 修改导航栏
				this.navbarTitle = this.military.name
			}  else if(packageId == 5) {
				// 引入文德武备武将包数据
				const militariesData = require("@/static/json/online/wenDeWuBei.json")
				// 获取当前武将数据
				this.military = militariesData.militaries[militaryId]
				// 修改导航栏
				this.navbarTitle = this.military.name
			}  else if(packageId == 6) {
				// 引入璀璨星河武将包数据
			}
			else if(packageId == 7) {
				// 引入谋扩展包数据
				const militariesData = require("@/static/json/online/mouKuoZhanBao.json")
				// 获取当前武将数据
				this.military = militariesData.militaries[militaryId]
				// 修改导航栏
				this.navbarTitle = this.military.name
			}
		}
	}
</script>

<style lang="scss" scoped>
</style>