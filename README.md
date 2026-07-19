# 晓晓老师的课堂（永久网课主页）

把晓晓老师讲过的互动课，一张张存成**永久的网页**，托管在 GitHub Pages。
链接长期有效，不会像聊天记录一样消失。

## 怎么打开
访问主页即可：<https://de333334.github.io/xiaoxiao-classroom/>

主页列出全部课程，点卡片就能去上课。

## 课程清单
| 课程 | 目录 | 语音方式 |
| --- | --- | --- |
| 不慌课 · 第5课（看见别人被欺负怎么管） | `buhuang-ke/` | 🎙 真人录音（晓晓 mp3），任意设备可听 |
| 不慌课 · 第6课（看见别人被当众羞辱） | `buhuang-ke6/` | 🗣 晓晓神经网络语音 |
| 不慌课 · 全集（第5-6课＋六课总复习） | `buhuang-heji/` | 🗣 晓晓神经网络语音 |
| 情绪管理 · 晓晓老师（每天一课） | `qingxu/` | 🗣 晓晓神经网络语音（自带音频，可拖动/上下句） |
| 据理力争 · 应对冲突小课堂 | `julilizheng/` | 🗣 晓晓神经网络语音 |
| 思维框架修炼课（第7课起） | `thinking-framework/` | 🗣 晓晓神经网络语音 |
| 吃动平衡 · 健康体重 | `yingyang-1/` | 浏览器语音（Edge / Chrome 最佳） |
| 多吃蔬果 · 奶类 · 全谷 · 大豆 | `yingyang-2/` | 浏览器语音（Edge / Chrome 最佳） |
| 四川风土课堂 | `sichuan/` | 浏览器语音（Edge / Chrome 最佳） |

## 目录结构
```
index.html          主页（课程导航）
buhuang-ke/         index.html + audio/（40 段晓晓真人录音）
buhuang-ke6/        不慌课第6课（晓晓神经网络语音）
buhuang-heji/       不慌课全集（六课总复习）
qingxu/             情绪管理课（每天一课，独立网页）
julilizheng/        据理力争课
thinking-framework/ 思维框架修炼课
yingyang-1/         吃动平衡课
yingyang-2/         多吃蔬果课
sichuan/            四川风土课
```

## 怎么加新课（一张网页一张网页地加）
1. 准备好新课的 `.html` 网页（最好自带语音或录音）。
2. 在仓库里新建一个文件夹，例如 `xinke/`，把 `index.html` 放进去；
   如果有录音，再建 `xinke/audio/` 放 mp3。
3. 回到主页 `index.html`，复制一张卡片，把链接改到 `xinke/`。
4. 提交并推送，GitHub Pages 会自动更新。

> 提示：录音版最稳（任意手机/电脑/微信都能放）；浏览器语音版请用 Edge 或 Chrome 打开。
