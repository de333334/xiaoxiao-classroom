# 据理力争小课堂 · 永久网页版

晓晓老师主讲的「如何应对冲突 / 据理力争」系列课程。面向没见过大风大浪、缺乏经验的人，
参考《学会据理力争》《请冷静，避免冲突和解决争端的秘诀》两本书，结合热点与日常案例，
每天一课、初中生也能听懂，配有图示、口诀、晓晓老师神经网络语音讲解、字幕、上一句/下一句、
不定时抽考、费曼复述与同学小剧场。

## 课程结构（每课一个永久网页，永不更新）
- 本目录 `julilizheng/index.html` = 课程目录（hub），点击进入各课。
- `julilizheng/lessons/lesson_XX/index.html` = 第 XX 课独立永久页（自带 `content.js` 与 `audio/`）。
- 每天先复习前一天的口诀，再学新课，符合费曼记忆法。
- 整个课堂放在 `xiaoxiao-classroom` 仓库的 `julilizheng/` 子目录下，不与仓库里其它课程（不慌课/营养/四川）冲突。

## 已上线的课
| 课次 | 主题 | 六字口诀 |
|------|------|----------|
| 第7课 | 书面据理力争：把道理写下来，理性维权/申诉 | 稳·清·据·理·求·留 |
| 第8课 | 被拒绝之后，怎么体面地再争取一次 | 听·缓·换·据·求·再 |

> 说明：第1–6课为早期「单页演进」版本（每天覆盖更新），尚未制成独立永久网页。
> 如需补制，请告知。

## 本地预览
```bash
cd 据理力争课堂
python3 -m http.server 8000
# 浏览器打开 http://localhost:8000/
```

## 部署（GitHub Pages）
本仓库（de333334/xiaoxiao-classroom）已启用 GitHub Pages，本课程站点地址：
`https://de333334.github.io/xiaoxiao-classroom/julilizheng/`
（仓库根目录主页 `https://de333334.github.io/xiaoxiao-classroom/` 也新增了「据理力争」卡片，点击即进入本课程。）

发布新的一课时，把 `julilizheng/lessons/lesson_XX/` 生成好，并在 `julilizheng/index.html`
加一张卡片；同时可在仓库根 `index.html` 也加一张。然后
`git add -A && git commit && git push` 即可。每课网页生成后不再改动（永久）。

## 生成与同步脚本（维护用）
- `gen_lesson08.py` —— 生成第8课音频/字幕/网页（每课一个生成脚本，作模板复用）。
- `push_ima.py` —— 把每课「费曼参考答案」写入 ima 知识库（imao）。
