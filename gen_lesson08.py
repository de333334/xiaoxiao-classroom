# -*- coding: utf-8 -*-
# 据理力争小课堂 · 第8课生成器
# 主题：被拒绝之后，怎么体面地再争取一次（不撒泼、不放弃）
# 六字口诀：听 · 缓 · 换 · 据 · 求 · 再
# 参考《学会据理力争》《请冷静，避免冲突和解决争端的秘诀》+ 留面子效应(门面效应/拆屋效应, Cialdini 1975) + 登门槛效应(弗里德曼&弗雷瑟 1966) + 前6课复习
# 产出：lessons/lesson_08/（独立永久网页，含 index.html + content.js + audio/），永不再被覆盖
# 同时：把当前第7课冻结为 lessons/lesson_07/（永久），并重建根 index.html 作为目录 hub
import os, json, shutil, asyncio
import edge_tts

HERE = os.path.dirname(os.path.abspath(__file__))
LESSON_DIR = os.path.join(HERE, "lessons", "lesson_08")
AUDIO_DIR = os.path.join(LESSON_DIR, "audio")
os.makedirs(AUDIO_DIR, exist_ok=True)

VOICE = "zh-CN-XiaoxiaoNeural"
RATE = "-6%"
PITCH = "+2Hz"

# ===== 晓晓老师口播文本（12 节） =====
SECTIONS = [
 ("s01", "同学你好呀，我是晓晓老师。新的一课开始前，咱们先把前七节课的口诀过一遍，热热身。第一课，跟人起冲突的总纲，冷、听、准、说、退、和。第二课，被冤枉时怎么冷静自证，停、核、证、说、稳、收。第三课，一群人起哄逼你站队时怎么守住自己，看、稳、问、立、析、退。第四课，跟长辈权威说理怎么既尊重又不憋屈，敬、听、缓、据、求、谢。第五课，当众发言和反驳，备、稳、清、据、应、收。第六课，情绪快失控时怎么急救，停、呼、数、换、说、修。第七课，把道理写下来、书面据理力争，稳、清、据、理、求、留。都还记得吧。今天这一课，咱们学一个特别实用的本事——被别人拒绝以后，怎么体面地再争取一次，不撒泼、也不放弃。"),

 ("s02", "先讲一个特别重要的念头：被拒绝，不等于你输了，更不等于你这个人不行。对方拒绝的，是“这个请求”，不是“你这个人”。很多没经验的同学一被拒，就觉得丢脸、觉得完了、觉得对方讨厌自己，结果要么当场吵起来，要么再也不敢开口。其实拒绝只是沟通里再正常不过的一步，就像你也会拒绝别人一样。记住这句话：拒绝对事，不对人。想通了这一点，你才能不玻璃心、不炸毛，冷静地想想——我还能怎么再把这件事说通。"),

 ("s03", "老师先讲个真事。有个同学要借教室搞活动，心里很虚，怕老师不答应借那么久。他灵机一动，先开口说：老师，我能不能借两天？老师一听，有点犹豫，担心和其他安排冲突。他马上改口：那借一天半行吗？老师查了查表，爽快答应了。后来心理老师点破：这叫“留面子效应”。你先提个大要求被拒，对方心里会有点过意不去，这时候你退一步提个小的，他更容易答应，等于给你“留了面子”。今天这课，就教你怎么用好这一招，把“不行”变成“行”。"),

 ("s04", "好，重点来了。老师给你编了一套六字口诀，专门用来“被拒之后，再争取回来”，精华全在里面。六个字是：听、缓、换、据、求、再。跟我念，听、缓、换、据、求、再。连成一段顺口溜：听他因，别急辩；缓一缓，不翻脸；换说法，给台阶；据事实，讲利害；求具体，好商量；再择时，争回来。下面老师一个字一个字，拆给你听。"),

 ("s05", "第一个字，听。被拒之后，先别急着反驳，先听清楚对方到底为什么拒绝你。你可以平和地问一句：您主要是担心什么呀？听清楚了，你才知道该往哪使劲。举个例子，你妈拒绝给你买手机，可能不是不爱你，而是怕影响你学习。你听懂了这个“担心”，后面才能对症下药。反过来，一被拒就打断、就吵，你永远不知道真正的障碍在哪。听，是再争取的第一步。"),

 ("s06", "第二个字，缓。被拒的那一刻，火气最容易上来，想当场争个高低。这时候请你搬出咱们第六课学过的急救招：停、呼、数、换、说、修，先把自己稳住。千万别当场撒泼、摔门、说狠话，因为那会把关系搞僵，以后更难开口。缓一缓，不翻脸，给对方、也给自己留个好印象。今天留个好印象，明天才有的聊。缓，是把门留着、不关死的那一步。"),

 ("s07", "第三个字，换。换角度、换方案，给对方一个能下的台阶。这里有两招特别好用。第一招，留面子效应：你先提个大一点的要求，被拒了，再退一步提小的，小的更容易成。第二招，登门槛效应：把大请求拆小，一步一步来。还有个说话诀窍：先认同、再转折，别说“但是”。比如不说“但是我想去”，而是说“我理解您担心安全，所以我打算……”。换，是让对方“够得着”、愿意点头的那一步。"),

 ("s08", "第四个字，据。摆事实、讲利害，说明为什么该答应你。把“我信息”用起来：说这件事对你有什么好处、你做了什么准备。比如你想周末出去玩，别只说“我想去”，而说“我作业都写完了，出去走走放松一下，回来效率更高”。你越拿事实和准备说话，对方越觉得你是认真想过的，不是胡闹。据，是让你的请求站得住脚、有分量的那一步。"),

 ("s09", "第五个字，求。提出具体、好商量的请求。别用质问的口气，比如“你凭什么不答应我”，那只会把人推远。要用商量的口气：“我能不能……如果能……我就……”。最好给个具体的条件，让对方好做决定。比如“我能不能下午出去两小时？如果能，我六点前一定回来，作业也保证写完”。你把话说到这个份上，对方拒绝你都难。求，是让请求变得“可以点头”的那一步。"),

 ("s10", "第六个字，再。换个时机，再来一次。再争取，不是死缠烂打，而是择时再试。这次被拒了，别急，过两天、等对方心情好了、你又多做了点准备，再开口。拒绝从来不是终审判决。你看，留面子效应本身就是“先被拒、再提小要求”的武器。所以记住：这回不行，咱回回头、备备课，下次再来。再，是把“不行”变成“行”的那最后一步。"),

 ("s11", "光听不练假把式，咱们用六字，帮一个同学走一遍。小浩想周末和同学出去玩，爸妈一口拒绝：不行，在家写作业。第一步，听：小浩先问，您主要是怕我耽误学习吧？第二步，缓：他不吵，说“那我再想想”。第三步，换：他先说“那我能不能玩一整天”，被拒，再退一步“就下午两小时行吗”。第四步，据：“我作业已经写完一大半了，出去放松下回来效率更高”。第五步，求：“我能不能下午两点到四点出去？四点准时回来，作业今晚保证写完”。第六步，再：爸妈还是有点犹豫，他说“那您考虑下，我明天再问您”。你看，全程没吵，道理一层层讲，这就是体面地再争取。"),

 ("s12", "今天的课到这儿，咱们把地图再过一遍：听、缓、换、据、求、再。再加上前七天，冷听准说退和、停核证说稳收、看稳问立析退、敬听缓据求谢、备稳清据应收、停呼数换说修、稳清据理求留，你手里已经有八套武器啦。老师送你一句话：被拒绝不是终点，是下一次开口的起点。下课前，晓晓老师用费曼学习法考考你。假如你晚交的作业，老师以“截止了”为由拒绝你补交，你会怎么用这六个字，体面地再争取一次？能讲给同学听明白，才是真学会了。加油，把道理讲到位，“不行”也能变成“行”。"),
]

# ===== 板书视觉 =====
VISUALS = {
 "s01": {"tag":"开场 · 复习","title":"上课啦！先热身，复习前7课👩‍🏫",
  "html":"""<p class='lead'>开讲前，先把前7课的口诀过一遍——</p>
  <div class='three'>
    <div class='card good'>第1课·冲突总纲<br><b>冷·听·准·说·退·和</b></div>
    <div class='card good'>第2课·被冤枉自证<br><b>停·核·证·说·稳·收</b></div>
    <div class='card good'>第3课·群体压力<br><b>看·稳·问·立·析·退</b></div>
    <div class='card good'>第4课·跟长辈/权威<br><b>敬·听·缓·据·求·谢</b></div>
    <div class='card good'>第5课·当众发言反驳<br><b>备·稳·清·据·应·收</b></div>
    <div class='card good'>第6课·情绪失控急救<br><b>停·呼·数·换·说·修</b></div>
    <div class='card good'>第7课·书面据理力争<br><b>稳·清·据·理·求·留</b></div>
  </div>
  <div class='banner'>今天第8课：被拒绝之后，怎么体面地再争取一次 🔁</div>"""},

 "s02": {"tag":"心法","title":"被拒绝 ≠ 你输了，更≠你不行🙅",
  "html":"""<div class='three'>
    <div class='card good'>拒绝的是「请求」<br><small>对方说“不”<br>是针对这件事<br>不是针对你这个人</small></div>
    <div class='card good'>不是「你不行」<br><small>一次被拒<br>不定义你<br>也不判你出局</small></div>
    <div class='card good'>拒绝是正常一步<br><small>就像你也会<br>拒绝别人一样<br>别玻璃心</small></div>
  </div>
  <div class='def'>记住这句话：<b>拒绝对事，不对人</b>。想通了，你才能不炸毛，冷静想想——我还能怎么再把事说通。</div>
  <div class='banner'>被拒就吵或再也不敢开口？都亏了。稳住，才是再争取的开始 💡</div>""","quiz":"q1"},

 "s03": {"tag":"热点案例","title":"真事：借教室，用「留面子效应」把“不行”变“行”",
  "html":"""<div class='scene'>🏫 同学要借教室搞活动，怕借太久老师不答应。他先说「借 <b>2 天</b>？」老师犹豫；他马上改口「那借 <b>1天半</b>行吗？」老师查表，<b>爽快答应</b>！</div>
  <svg class='scene-svg' viewBox='0 0 320 150' xmlns='http://www.w3.org/2000/svg' aria-label='留面子效应：先大后小'>
    <rect x='6' y='14' width='146' height='120' rx='10' fill='rgba(255,255,255,.12)'/>
    <text x='79' y='30' font-size='12' text-anchor='middle' fill='#eafff4' font-family='serif'>先提大要求</text>
    <circle cx='40' cy='66' r='14' fill='#ffd49a'/><rect x='28' y='82' width='24' height='26' rx='6' fill='#ffd49a'/>
    <text x='36' y='62' font-size='11' text-anchor='middle' fill='#5a3d1c' font-family='serif'>学</text>
    <text x='110' y='68' font-size='15' text-anchor='middle' fill='#eafff4' font-family='serif'>借2天？</text>
    <text x='110' y='102' font-size='28' text-anchor='middle' fill='#ff8a8a'>✗</text>
    <text x='160' y='80' font-size='18' text-anchor='middle' fill='#ffe08a'>➜</text>
    <rect x='168' y='14' width='146' height='120' rx='10' fill='rgba(255,255,255,.12)'/>
    <text x='241' y='30' font-size='12' text-anchor='middle' fill='#eafff4' font-family='serif'>退一步提小的</text>
    <circle cx='202' cy='66' r='14' fill='#ffd49a'/><rect x='190' y='82' width='24' height='26' rx='6' fill='#ffd49a'/>
    <text x='198' y='62' font-size='11' text-anchor='middle' fill='#5a3d1c' font-family='serif'>学</text>
    <text x='272' y='68' font-size='15' text-anchor='middle' fill='#eafff4' font-family='serif'>借1.5天？</text>
    <text x='272' y='102' font-size='28' text-anchor='middle' fill='#9be8b0'>✓</text>
  </svg>
  <div class='def'>这叫 <b>留面子效应（门面效应 / 拆屋效应）</b>：先提大要求被拒，对方心里过意不去，你再退一步提小的，他更容易点头。</div>
  <div class='tip'>今天这课，就教你怎么用好这一招，把“不行”变成“行”。</div>""","student":"student2"},

 "s04": {"tag":"核心口诀","title":"六字口诀 = 被拒之后，再争取回来🧰",
  "html":"""<div class='koujue'>
    <span>听</span><span>缓</span><span>换</span><span>据</span><span>求</span><span>再</span>
  </div>
  <div class='rhyme'>
    听他因，别急辩；<br>缓一缓，不翻脸；<br>换说法，给台阶；<br>据事实，讲利害；<br>
    求具体，好商量；<br><b>再择时，争回来。</b>
  </div>""","quiz":"q2"},

 "s05": {"tag":"口诀①","title":"听 —— 先听清「为什么被拒」",
  "html":"""<div class='big'>听</div>
  <div class='def'>被拒之后，<b>先别急着反驳，先听清楚对方到底为啥拒绝你</b>。</div>
  <ul class='steps'>
    <li>🗣️ 平和地问一句：「您主要是担心什么呀？」</li>
    <li>👂 <b>别打断、别抢话</b>，让对方把理由说完</li>
    <li>🔍 听懂真正的“障碍”在哪，后面才能对症下药</li>
  </ul>
  <div class='tip'>比如妈妈拒绝买手机，可能不是不爱你，而是怕影响学习。你听懂了这个“担心”，才知道往哪使劲。听，是再争取的第一步。</div>""","quiz":"q3"},

 "s06": {"tag":"口诀②","title":"缓 —— 别当场炸毛，把门留着",
  "html":"""<div class='big'>缓</div>
  <div class='def'>被拒那一刻火气最易上头。请搬出第6课急救招：<b>停、呼、数、换、说、修</b>，先稳住自己。</div>
  <ul class='steps'>
    <li>🚫 <b>不撒泼、不摔门、不说狠话</b>——那会把关系搞僵</li>
    <li>😮‍💨 说一句「那我再想想」，给自己和对方留台阶</li>
    <li>🌱 今天留个好印象，<b>明天才有的聊</b></li>
  </ul>
  <div class='tip'>缓，是把门留着、不关死的那一步。当场翻脸，等于自己把下次开口的路堵死了。</div>""","student":"student1"},

 "s07": {"tag":"口诀③","title":"换 —— 换角度、换方案，给对方台阶",
  "html":"""<div class='big'>换</div>
  <div class='def'>两招特别好用，都是“换说法、给台阶”👇</div>
  <div class='two'>
    <div class='card good'>①留面子效应<br><small>先提大要求被拒<br>再退一步提小的<br>小的更容易成</small></div>
    <div class='card good'>②登门槛效应<br><small>把大请求拆小<br>一步一步来<br>对方更好点头</small></div>
  </div>
  <div class='def'>说话诀窍：<b>先认同、再转折，别说“但是”</b>。不说「但是我想去」，改说「我理解您担心安全，所以我打算……」。</div>
  <div class='tip'>换，是让对方“够得着”、愿意点头的那一步。</div>""","quiz":"q4"},

 "s08": {"tag":"口诀④","title":"据 —— 摆事实、讲利害，让请求有分量",
  "html":"""<div class='big'>据</div>
  <div class='def'>说明<b>为什么该答应你</b>，把“我信息”用起来：说好处、说准备。</div>
  <div class='three'>
    <div class='card'>📌 我信息<br><small>说“我”的感受<br>和打算</small></div>
    <div class='card'>📋 摆事实<br><small>作业写完了<br>计划做好了</small></div>
    <div class='card'>⚖️ 讲利害<br><small>放松后效率更高<br>对双方都好</small></div>
  </div>
  <div class='eg'>❌ 只说「我想去」 → ✅「我作业都写完了，出去走走放松下，回来效率更高」</div>
  <div class='tip'>你越拿事实和准备说话，对方越觉得你认真想过、不是胡闹。据，是让你的请求站得住脚的那一步。</div>"""},

 "s09": {"tag":"口诀⑤","title":"求 —— 提具体、好商量的请求",
  "html":"""<div class='big'>求</div>
  <div class='def'>别用质问口气把人推远，要用商量口气👇</div>
  <div class='eg'>❌「你凭什么不答应我！」<br>✅「我能不能……如果能……我就……」</div>
  <div class='def'>最好给个<b>具体条件</b>，让对方好做决定：</div>
  <div class='eg'>「我能不能<b>下午出去两小时</b>？如果能，我<b>六点前一定回来</b>，作业也保证写完。」</div>
  <div class='tip'>你把话说到这个份上，对方拒绝你都难。求，是让请求变得“可以点头”的那一步。</div>""","quiz":"q5"},

 "s10": {"tag":"口诀⑥","title":"再 —— 换个时机，再来一次",
  "html":"""<div class='big'>再</div>
  <div class='def'>再争取，<b>不是死缠烂打，而是择时再试</b>。</div>
  <ol class='flow'>
    <li>⏳ 这次被拒别急，<b>过两天、等心情好了、多备点准备</b>再开口</li>
    <li>🚪 <b>拒绝从来不是终审判决</b></li>
    <li>🔁 留面子效应本身就是「先被拒、再提小要求」的武器</li>
  </ol>
  <div class='banner'>这回不行？咱回回头、备备课，下次再来 —— 再，是把“不行”变“行”的最后一步 🔁</div>""","student":"student3"},

 "s11": {"tag":"实战演练","title":"用六字，帮小浩把“不行”说成“行”",
  "html":"""<div class='scene'>🧒 小浩想周末和同学出去玩，爸妈一口拒绝：「不行，在家写作业。」</div>
  <ol class='flow'>
    <li><b>听</b>：先问「您主要是怕我耽误学习吧？」</li>
    <li><b>缓</b>：不吵，说「那我再想想」</li>
    <li><b>换</b>：先说「玩一整天？」被拒 → 退一步「就下午两小时行吗」</li>
    <li><b>据</b>：「我作业写完一大半了，放松下回来效率更高」</li>
    <li><b>求</b>：「我能不能下午2点到4点出去？4点准时回，作业今晚保证写完」</li>
    <li><b>再</b>：爸妈犹豫，他说「那您考虑下，我明天再问您」</li>
  </ol>
  <div class='banner'>全程没吵，道理一层层讲 —— 这就是体面地再争取 ✅</div>"""},

 "s12": {"tag":"费曼总结","title":"下课前，晓晓老师考考你！",
  "html":"""<div class='koujue'>
    <span>听</span><span>缓</span><span>换</span><span>据</span><span>求</span><span>再</span>
  </div>
  <div class='quote'>被拒绝不是终点，<br><b>是下一次开口的起点</b>。</div>
  <p class='lead'>费曼学习法：能把它<b>讲给「同学」听明白</b>，才是真的学会了 👇</p>""",
  "quiz":"qfinal"},
}

# ===== 费曼提问（章节末固定）=====
QUIZZES = {
 "q1": {"ask":"被拒绝的时候，最重要的是先想明白哪件事？",
   "type":"choice",
   "options":["对方讨厌我这个人","对方拒绝的是“这个请求”，不是“我这个人”","我彻底没希望了"],
   "answer":1,
   "explain":"拒绝对事不对人——拒绝一个请求，不等于否定你这个人。想通了，你才不会玻璃心、才能冷静下来再争取。一次被拒，不算数。"},
 "q2": {"ask":"复述一下：被拒之后「再争取」的六字口诀是哪六个字？(先自己说，再点开对照)",
   "type":"reveal",
   "answer_text":"听 · 缓 · 换 · 据 · 求 · 再\n听：先听清对方为什么拒绝，别急着反驳；缓：别当场炸毛撒泼，把门留着；换：换角度/换方案，给对方台阶（留面子效应先大后小、登门槛效应拆小请求）；据：摆事实讲利害，用“我信息”说准备和好处；求：提具体、好商量的请求（我能不能…如果能…我就…）；再：择时再试，拒绝不是终审。"},
 "q3": {"ask":"想搞清「对方为什么拒绝你」，下面哪种做法更好？",
   "type":"choice",
   "options":["打断对方，马上反驳","先别打断，平和地问“您主要是担心什么”听清楚","假装听懂，直接再吵"],
   "answer":1,
   "explain":"先听清楚障碍在哪，后面才能对症下药。一被拒就打断、就吵，你永远不知道真正的理由，也最容易把关系搞僵——这就是「听」。"},
 "q4": {"ask":"「留面子效应（门面效应）」说的是什么？",
   "type":"choice",
   "options":["先提一个大要求被拒，再提个小的，小的更容易被答应","一直只提小要求","当场吵赢对方"],
   "answer":0,
   "explain":"心理学家查尔迪尼(Cialdini)1975年实验：人拒绝大要求后心里过意不去，再提小要求时更愿让步“留面子”。这就是「换」——先大后小，给对方台阶。借教室那个真事就是这么成的。"},
 "q5": {"ask":"提请求时，下面哪种说法更可能成功？",
   "type":"choice",
   "options":["“你凭什么不答应我！”","“我作业写完了，能不能下午出去两小时？如果能，我六点前回来”","一句话不说直接摔门"],
   "answer":1,
   "explain":"具体 + 给条件 + 好商量 = 「据 + 求」。用“我能不能…如果能…我就…”的口气，把请求说成对方“可以点头”的样子，拒绝你都难。"},
 "qfinal": {"ask":"费曼大挑战🎓：你晚交的作业，老师以「截止了」为由拒绝你补交。你会怎么用「听缓换据求再」体面地再争取一次？(先完整讲一遍，再点开参考答案)",
   "type":"reveal",
   "answer_text":"以“老师以截止为由拒绝补交作业”为例：\n听：先问“老师主要是担心什么呢？是怕破坏规矩，还是影响别的同学？”不急着争。\n缓：不当场吵，说“老师我再想想”，稳住自己（第6课 停呼数换说修），把门留着。\n换：先认同“我理解作业要守截止时间”，再换说法“那我能不能用午休把补上的部分先交给课代表？”把“整份重交”这个大请求，拆成“先交一部分/走特殊通道”的小请求。\n据：摆事实“我昨晚发烧去医院了，有病历；这份作业我真写完了，只是没来得及交”，讲利害“补交不影响别人，也能让我跟上进度”。\n求：具体商量“我能不能在今天放学前补交？如果能，我保证今后按时，还愿意把笔记共享给小组”。\n再：老师还是犹豫，就说“那您考虑下，我明天再来问”，择时再试。拒绝不是终审。\n全程不撒泼、不质问，道理一层层讲——这就是体面地再争取，把“不行”变成“行”。"},
}

# ===== 不定时抽考 =====
SURPRISE = {
 "sp1": {"ask":"🎯 突击小测：被拒绝之后，第一步最好先做什么？",
   "type":"choice",
   "options":["马上发火","先听清对方为什么拒绝（听）","假装没听见"],
   "answer":1,
   "explain":"先听清楚“为什么拒”，才知道往哪使劲。一被拒就发火，既听不到真相，又把路堵死——这就是「听」。"},
 "sp2": {"ask":"🎯 突击小测：「留面子效应」指的是？",
   "type":"choice",
   "options":["先提大要求被拒，再提小的，小的更容易成","先提小要求","越吵越凶越好"],
   "answer":0,
   "explain":"先大后小：对方拒了大要求心里过意不去，再提小的就更容易答应，等于给你“留面子”。这是「换」的核心一招。"},
 "sp3": {"ask":"🎯 突击小测：被拒那一刻想发火，可以用第6课哪招先稳住？",
   "type":"choice",
   "options":["停·呼·数·换·说·修","转身就走不理人","当场哭出来"],
   "answer":0,
   "explain":"第6课情绪急救：停住嘴、深呼吸、数到十、换个角度、说感受、修关系。先稳住，才有后面的「缓」和「再争取」。"},
 "sp4": {"ask":"🎯 突击小测：这次被拒了，下次还能再试吗？",
   "type":"choice",
   "options":["不能，拒绝是终审","可以择时再争取（再），拒绝不是终审","只能认命"],
   "answer":1,
   "explain":"拒绝从来不是终审判决。过两天、备好准备、等心情好了再开口，就是「再」。留面子效应本身就是“先被拒、再提小要求”的武器。"},
}

# ===== 同学小剧场 =====
STUDENTS = {
 "student1": {
   "asker":"同学小宇","avatar":"🧑‍🎓",
   "question":"老师，我上次被拒，当场就吵起来了，现在不好意思再去找他，怎么办呀？",
   "answer":"先别慌，关系还能补回来，关键是“缓”加“再”。\n\n第一步，先去缓和关系。找个轻松的时机，大方说一句“老师/爸妈，上次我有点急，说话冲了，不好意思”，先道歉、把气氛松开。这一步叫「缓」——不翻旧账、不辩解，先把好印象找回来。\n第二步，过一两天、你又多做点准备，再开口，这叫「再」。这次别一上来就硬要，先用「听」问清对方担心什么，再用「换」给个更小的、更好答应的请求。\n你看，当场吵不是世界末日，只要你愿意先低头缓和、再择时准备，门就还开着。"},
 "student2": {
   "asker":"同学小美","avatar":"👧",
   "question":"晓晓老师，我每次被拒就觉得是自己做错了、很丢脸，不敢再试了……",
   "answer":"这是最需要掰过来的一个念头：被拒绝，不等于你这个人不行。\n\n记住「听」背后的那句话——拒绝对事，不对人。对方说“不”，是针对“这个请求”，不是针对“你”。就像你也会拒绝别人一样，这太正常了。一次被拒，不算数，更不定义你。\n所以别把“被拒”翻译成“我很差”。把它翻译成“哦，这次没说通，那我听听为啥、换个说法再来”。想通了这一点，你才敢开口、也才不会因为怕丢脸而把门自己关上。"},
 "student3": {
   "asker":"同学小浩","avatar":"🧒",
   "question":"老师，我想要一台新手机/平板，爸妈一口拒绝了，我该怎么再争取啊？",
   "answer":"用上「换、据、求」三步，比硬磨管用多了。\n\n先「换」——别一上来就要最贵的，可以用留面子效应：先说“那买顶配的”，被拒，再退一步“那基础款行吗”；或者把大请求拆小（登门槛）：先要“周末能用一小时查资料”，容易答应。\n再「据」——摆事实讲准备：“我这次月考进步了”“我做了使用计划，每天只用一个小时”。用“我信息”说好处，不是只说“同学都有”。\n最后「求」——具体商量：“我能不能先用压岁钱出一半、您出一半？如果能，我保证每天只用一小时，成绩掉就停用。”你把条件摆到这份上，爸妈拒绝你都难。这回不行，就「再」——过阵子带新准备再来。"},
}

async def gen_audio():
    manifest = []
    for sid, text in SECTIONS:
        mp3 = os.path.join(AUDIO_DIR, f"{sid}.mp3")
        comm = edge_tts.Communicate(text, VOICE, rate=RATE, pitch=PITCH)
        cues = []
        with open(mp3, "wb") as f:
            async for chunk in comm.stream():
                if chunk["type"] == "audio":
                    f.write(chunk["data"])
                elif chunk["type"] == "SentenceBoundary":
                    start = chunk["offset"] / 1e7
                    end = (chunk["offset"] + chunk["duration"]) / 1e7
                    cues.append({"start": round(start,3), "end": round(end,3), "text": chunk["text"]})
        manifest.append({"id": sid, "mp3": f"audio/{sid}.mp3", "cues": cues})
        print("done", sid, os.path.getsize(mp3), "bytes cues:", len(cues))
    return manifest

def build_content(manifest):
    m = {x["id"]: x for x in manifest}
    lesson = []
    for sid in ["s01","s02","s03","s04","s05","s06","s07","s08","s09","s10","s11","s12"]:
        v = VISUALS[sid]; mm = m[sid]
        lesson.append({"id":sid,"tag":v["tag"],"title":v["title"],"html":v["html"],
                       "mp3":mm["mp3"],"cues":mm["cues"],
                       "quiz":v.get("quiz"),"student":v.get("student")})
    out = "// 自动生成，请勿手改\nwindow.LESSON = " + json.dumps(lesson, ensure_ascii=False) + ";\n"
    out += "window.QUIZZES = " + json.dumps(QUIZZES, ensure_ascii=False) + ";\n"
    out += "window.STUDENTS = " + json.dumps(STUDENTS, ensure_ascii=False) + ";\n"
    out += "window.SURPRISE = " + json.dumps(SURPRISE, ensure_ascii=False) + ";\n"
    with open(os.path.join(LESSON_DIR, "content.js"), "w", encoding="utf-8") as f:
        f.write(out)
    print("content.js written, sections:", len(lesson), "quizzes:", len(QUIZZES),
          "students:", len(STUDENTS), "surprise:", len(SURPRISE))
    return lesson

def build_lesson_html():
    tpl = open(os.path.join(HERE, "index.html"), encoding="utf-8").read()
    repl = [
      ("第7课 书面据理力争 · 晓晓老师", "第8课 被拒绝后如何再争取 · 晓晓老师"),
      (" · 第7课</h1>", " · 第8课</h1>"),
      ("书面据理力争：把道理写下来，理性维权/申诉 · 六字口诀「稳清据理求留」· 初中生也能懂",
       "被拒绝后，怎么体面地再争取一次：不撒泼、不放弃 · 六字口诀「听缓换据求再」· 初中生也能懂"),
      ("你已经掌握了「稳清据理求留」六步法", "你已经掌握了「听缓换据求再」六步法"),
      ("今天学的「稳·清·据·理·求·留」", "今天学的「听·缓·换·据·求·再」"),
    ]
    for a, b in repl:
        if a not in tpl:
            raise SystemExit("TOKEN NOT FOUND: " + a)
        tpl = tpl.replace(a, b)
    with open(os.path.join(LESSON_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(tpl)
    print("lessons/lesson_08/index.html written")

def freeze_lesson07():
    d7 = os.path.join(HERE, "lessons", "lesson_07")
    os.makedirs(os.path.join(d7, "audio"), exist_ok=True)
    shutil.copy(os.path.join(HERE, "index.html"), os.path.join(d7, "index.html"))
    shutil.copy(os.path.join(HERE, "content.js"), os.path.join(d7, "content.js"))
    for fn in os.listdir(os.path.join(HERE, "audio")):
        shutil.copy(os.path.join(HERE, "audio", fn), os.path.join(d7, "audio", fn))
    print("frozen lesson_07 ->", d7)

def build_hub():
    hub = """<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<meta name="format-detection" content="telephone=no">
<title>据理力争小课堂 · 课程目录</title>
<style>
 body{font-family:"Songti SC","SimSun","宋体",serif;background:#fef6ec;color:#3a2f28;margin:0;padding:24px 16px}
 .wrap{max-width:760px;margin:0 auto}
 h1{font-size:24px;text-align:center;margin:6px 0 2px}
 .sub{text-align:center;color:#a58b6f;font-size:13px;margin-bottom:18px}
 .card{display:block;text-decoration:none;background:#fffaf3;border:1px solid #e7d8c4;border-radius:16px;
   padding:16px 18px;margin:12px 0;box-shadow:0 8px 22px rgba(120,80,40,.12);transition:.2s;color:#3a2f28}
 .card:hover{transform:translateY(-3px);border-color:#ffb703}
 .card .n{font-size:20px;font-weight:800;color:#c8792f}
 .card .t{font-size:17px;margin:4px 0}
 .card .k{font-size:13px;color:#a06a2c;background:#ffe6cf;display:inline-block;padding:3px 10px;border-radius:12px;margin-top:4px}
 .note{background:#fff6e8;border:1px dashed #ffb703;border-radius:12px;padding:12px 14px;font-size:13px;color:#8a6b4a;margin-top:16px;line-height:1.8}
</style></head>
<body><div class="wrap">
 <h1>🏫 据理力争小课堂 · 课程目录</h1>
 <div class="sub">晓晓老师主讲 · 每课一个永久网页，永不更新 · 下一天先复习再学新</div>
 <a class="card" href="lessons/lesson_08/index.html"><div class="n">第8课</div><div class="t">被拒绝之后，怎么体面地再争取一次</div><div class="k">六字口诀「听·缓·换·据·求·再」</div></a>
 <a class="card" href="lessons/lesson_07/index.html"><div class="n">第7课</div><div class="t">书面据理力争：把道理写下来，理性维权/申诉</div><div class="k">六字口诀「稳·清·据·理·求·留」</div></a>
 <div class="note">说明：第1–6课为早期「单页演进」版本（每天覆盖更新），如需把它们也制成各自独立的永久网页，告诉我一声即可补制。第7、8课起已改为「每课一个永久网页、永不再覆盖」的新模式。</div>
</div></body></html>"""
    with open(os.path.join(HERE, "index.html"), "w", encoding="utf-8") as f:
        f.write(hub)
    print("root hub index.html rewritten (now a directory)")

if __name__ == "__main__":
    manifest = asyncio.run(gen_audio())
    build_content(manifest)
    build_lesson_html()
    freeze_lesson07()
    build_hub()
    print("ALL DONE -> lessons/lesson_08/")
