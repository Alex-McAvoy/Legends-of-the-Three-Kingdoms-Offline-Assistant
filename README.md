# Legends-of-the-Three-Kingdoms-Offline-Assistant
<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Downloads][Download-shield]][download-url]

<!-- PROJECT LOGO -->
<br />

<p align="center">
  <h2 align="center"><strike>三国杀面杀助手</strike> 杀批宝典</h2>
</p>
<p align="center">
  <img src="static/logo.png" alt="Logo" width="80" height="80">
  <p align="center">
    <a href="https://github.com/Alex-McAvoy/Legends-of-the-Three-Kingdoms-Offline-Assistant"><strong>探索本项目的文档 »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Alex-McAvoy/Legends-of-the-Three-Kingdoms-Offline-Assistant/issues">报告Bug</a>
    ·
    <a href="https://github.com/Alex-McAvoy/Legends-of-the-Three-Kingdoms-Offline-Assistant/issues">提出新特性</a>
    ·
    <a href="https://github.com/Alex-McAvoy/Legends-of-the-Three-Kingdoms-Offline-Assistant/releases">发行说明</a>
  </p>
</p>







## 目录

- [说明](#说明)
- [起源](#起源)
- [开源协议](#开源协议)
- [开发指南](#开发指南)
- [文件目录说明](#文件目录说明)
- [工具](#工具)
- [部署](#部署)
- [待开发特性](#待开发特性)
- [待处理Bug](#待处理Bug)
- [贡献者](#贡献者)
- [如何参与](#如何参与)
- [使用框架](#使用框架)
- [鸣谢](#鸣谢)

## 说明

本项目旨在为面杀提供便利，长期开发，长期维护

项目资源均来自于**三国杀官方**

由于作者俗务繁忙，因此预计该项目将长期处于 alpha 版，如有需要，请移步 [Releases](https://github.com/Alex-McAvoy/Legends-of-the-Three-Kingdoms-Offline-Assistant/releases) 下载

另考虑服务器成本，本项目目前为**静态项目**

## 起源

最早接触三国杀是 11 年，但关于那时的记忆已经消散地差不多了。上高中后，有幸认识一帮好友，每天中午去学校附近的麦当劳吃饭，然后打三国杀，假期聚会时，也大多是在桌游吧打一天的三国杀

时至今日，有时还会恍惚地想起那些年的盛夏，跟朋友们待在桌游吧里，慵懒地靠在桌子上，任由阳光照耀。不知道为什么，这一幕总是很深刻，哪怕到了现在，我依旧能回忆起房间中陈旧的味道

不知不觉已经快十年了，朋友们如今分散四方，每年只能聚几次，每次大抵也都是以三国杀开始，以三国杀结束

前段时间聚会，一个朋友说，现在三国杀三个服务器，武将越出越多技能越来越长，有时候同一个武将在不同服务器上技能还不一样，每次打面杀看武将技能都像在读小作文，武将起源故事、台词也不知道是什么，没有之前有意思了

我想了想，于是，就有了这个项目

## 开源协议

本项目开源协议为 [No License](https://www.google.com.hk/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwigkv-KtMT0AhXFdXAKHdI4BCcQFnoECAQQAw&url=https%3A%2F%2Fchoosealicense.com%2Fno-permission%2F&usg=AOvVaw3M2Q4IbdhnpJ2K71TF7SPB)，这意味着可以随意的 fork 和使用，但是**不能私下修改后再包装分发**，如果有这方面的需求，请联系作者，望理解

## 开发指南

1. 克隆项目

```sh
git clone https://github.com/Alex-McAvoy/Legends-of-the-Three-Kingdoms-Offline-Assistant.git
```

2. 进入项目文件夹并安装依赖

```sh
cd ./Legends-of-the-Three-Kingdoms-Offline-Assistant
npm i
```

## 文件目录说明

```
filetree 
├── /components/
├── /pages/
│  ├── /archive/
│  │  ├── detail.vue
│  │  ├── index.vue
│  │  └── list.vue
│  ├── /index/
│  │  └── index.vue
│  └── /mine/
│     └── index.vue
├── /static/
├── /uni_modules/
├── /utils/
│     └── online-video-spider.py
├── .gitignore
├── App.vue
├── README.md
├── index.html
├── main.js
├── manifest.json
├── package.json
├── pages.json
├── uni.promisify.adaptor.js
└── uni.scss

```

## 工具

`online-video-spider.py` 三国杀 Online 语音爬取脚本

调用说明：

```bash
python online-video-spider.py 游戏武将编号 实际编号 技能数 [--save_path 保存路径(可选)]
```

实例：

```bash
python online-video-spider.py 7003simayi wenWu-li-01 4 --save_path C:/Users/Alex/Desktop/mp3
```

## 部署

暂无

## 待开发特性

- [ ] 技能描述中，锁定技、主公技、限定技、转换技、隐匿解释
- [ ] 技能描述排版
- [ ] Online 国战图鉴
- [ ] 十周年武将图鉴
- [ ] 移动版武将图鉴
- [ ] 卡牌图鉴
- [ ] 工具
- [ ] 首页
- [ ] 我的

## 待处理Bug

- [ ] Online 族吴乔无配音
- [ ] Online 谋姜维无困奋、诈降语音
- [ ] Online 兀突骨血量显示异常、燃殇与死亡语音声音小
- [ ] Online 郭槐死亡语音重复两遍

## 贡献者

Nancy-月皎：提供部分可行的建议

## 如何参与

项目组全体成员十分欢迎您为本项目贡献页面

大致流程如下：

1. 将主仓库 Fork 到自己的仓库中
2. 将 Fork 后的分支仓库 Clone 到本地
3. 在本地进行修改后 Commit 更改
4. 将这些更改 Push 到克隆的分支仓库
5. 提交 Pull Request 至主仓库

对于 Commit 摘要，按照如下格式书写：

```bash
[修改类型] 修改内容
```

修改类型分为以下几类：

- `Add`：添加新模块
- `Fix`：修正现有模块的错误
- `Update`：更新现有模块
- `Refactor`：对一个页面/模块进行重构（较大规模的更改）
- `Revert`：回退之前的更改

## 使用框架

- [uniapp](https://uniapp.dcloud.net.cn/)
- [uView 2.0.36](https://uviewui.com/components/intro.html)

## 鸣谢

- [三国杀](https://www.sanguosha.com/)
- [三国杀WIKI](https://wiki.biligame.com/sgs/)
- [uniapp](https://uniapp.dcloud.net.cn/)
- [uView](https://uviewui.com/components/intro.html)


<!-- links -->
[contributors-shield]: https://img.shields.io/github/contributors/Alex-McAvoy/Legends-of-the-Three-Kingdoms-Offline-Assistant.svg?style=flat-square
[contributors-url]: https://github.com/Alex-McAvoy/Legends-of-the-Three-Kingdoms-Offline-Assistant/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Alex-McAvoy/Legends-of-the-Three-Kingdoms-Offline-Assistant.svg?style=flat-square
[forks-url]: https://github.com/Alex-McAvoy/Legends-of-the-Three-Kingdoms-Offline-Assistant/network/members
[stars-shield]: https://img.shields.io/github/stars/Alex-McAvoy/Legends-of-the-Three-Kingdoms-Offline-Assistant.svg?style=flat-square
[stars-url]: https://github.com/Alex-McAvoy/Legends-of-the-Three-Kingdoms-Offline-Assistant/stargazers
[issues-shield]: https://img.shields.io/github/issues/Alex-McAvoy/Legends-of-the-Three-Kingdoms-Offline-Assistant.svg?style=flat-square
[issues-url]: https://img.shields.io/github/issues/Alex-McAvoy/Legends-of-the-Three-Kingdoms-Offline-Assistant.svg
[download-shield]: https://img.shields.io/github/downloads/Alex-McAvoy/Legends-of-the-Three-Kingdoms-Offline-Assistant/total.svg
[download-url]: https://tooomm.github.io/github-release-stats/?username=Alex-McAvoy&repository=Legends-of-the-Three-Kingdoms-Offline-Assistant