# -*- coding: utf-8 -*-
# 据理力争小课堂 · 第9课生成器
# 主题：冷处理与沉默战术（有时候"不争"才是最高级的争）—— 最适合"没经验、一遇冲突就想回怼"的新手
# 六字口诀：冷 · 观 · 沉 · 隔 · 时 · 收
# 参考《学会据理力争》《请冷静，避免冲突和解决争端的秘诀》+ 2025真实案例(西夏区法院调解员扈廷刚"冷处理"退费纠纷、西陵区调解员方业寿"冷静期"、慈利县零溪镇邻里纠纷冷却期) + 前8课复习
# 产出：lessons/lesson_09/（独立永久网页，含 index.html + content.js + audio/），永不再被覆盖
# 同时：更新 julilizheng/index.html 课程目录 hub（新增第9课卡片）
import os, json, shutil, asyncio
import edge_tts

HERE = os.path.dirname(os.path.abspath(__file__))
LESSON_DIR = os.path.join(HERE, "lessons", "lesson_09")
AUDIO_DIR = os.path.join(LESSON_DIR, "audio")
os.makedirs(AUDIO_DIR, exist_ok=True)

VOICE = "zh-CN-XiaoxiaoNeural"
RATE = "-6%"
PITCH = "+2Hz"

# ===== 晓晓老师口播文本（12 节） =====
SECTIONS = [
 ("s01", "同学你好呀，我是晓晓老师。新的一课开始前，咱们先把前八节课的口诀过一遍，热热身。第一课，跟人起冲突的总纲，冷、听、准、说、退、和。第二课，被冤枉时怎么冷静自证，停、核、证、说、稳、收。第三课，一群人起哄逼你站队时怎么守住自己，看、稳、问、立、析、退。第四课，跟长辈权威说理怎么既尊重又不憋屈，敬、听、缓、据、求、谢。第五课，当众发言和反驳，备、稳、清、据、应、收。第六课，情绪快失控时怎么急救，停、呼、数、换、说、修。第七课，把道理写下来、书面据理力争，稳、清、据、理、求、留。第八课，被拒绝以后怎么体面地再争取，听、缓、换、据、求、再。都还记得吧。今天这一课，咱们学一个特别反常识的本事——冷处理与沉默战术：有时候不争，才是最高级的争。"),

 ("s02", "先讲一个特别重要的念头：不是每一场冲突，都该马上回嘴、马上争。很多没经验的同学一遇到矛盾，就觉得他怼我、我就得怼回去，不然就输了。其实啊，有些架一接就升级，越吵越乱。老师先给你掰清楚两个词：忍气吞声，和，冷处理。忍气吞声是“我怕了，我憋着”，问题没解决，自己还委屈；冷处理是“我先不接招，等看清楚、等火气降了，再漂亮地把事解决”。一个是怂，一个是有策略的暂停。记住：冷处理不等于不争，它只是把争，挪到了更合适的时间、更合适的地点。"),

 ("s03", "老师讲个2025年的真事。宁夏西夏区有个法院调解员叫扈廷刚，遇到一起培训退费纠纷。被告机构老板陈某特别激动、态度强硬，电话里就跟调解员吵，说我也懂法，不退。换作别人，可能当场跟他对吵起来。但扈廷刚心里有数，他知道一句话：话赶话没好话，事赶事没好事。要是继续争，矛盾只会更僵。他当场做了个决定——冷处理：先把案子搁下，不逼任何一方，让彼此都静一静。过了几天，他再打电话，不急着分对错，而是跟陈老板聊家常、说道理，从经营、信誉、时间成本、打官司的风险聊起。等对方情绪平了、理智回来了，才讲法律规定。结果你猜怎么着？陈老板从抗拒变成接受，主动把钱退了，还专门送来一面锦旗。你看，不急着吵，反而把事办成了。还有位调解员方业寿说：大概一半成功的调解，都用到了冷静期，因为很多矛盾表面是利益之争，其实是情绪在对抗。这俩案例，就是今天这课最好的说明书。"),

 ("s04", "好，重点来了。老师给你编了一套六字口诀，专门对付该不该现在争、怎么冷处理，精华全在里面。六个字是：冷、观、沉、隔、时、收。跟我念，冷、观、沉、隔、时、收。连成一段顺口溜：冷住火，别接招；观清楚，谁在闹；沉住气，先不吵；隔开来，别盯梢；时机到，再开口；收好尾，情不焦。下面老师一个字一个字，拆给你听。"),

 ("s05", "第一个字，冷。遇到挑事、遇到被人怼，先别跳起来接招。你可以在心里说一句，我先冷一下。冷，不是怕，是给大脑一个缓冲——还记得第6课学的吗？人生气那一下，理智还没上线，这时候回嘴最容易说错话、把事搞大。所以遇到冲突，先冷三秒，不接第一句话、不回第一条消息。冷，是冷处理的开关。"),

 ("s06", "第二个字，观。冷下来之后，你要看清楚。看清三件事：第一，是谁在拱火、谁是带头起哄的；第二，对方到底在气什么、他的真实担心是什么；第三，现在的场合合不合适说。比如同学当众嘲讽你，你观一观，发现他只是想逗大家笑、刷存在感，那你越回嘴他越来劲——这时候不值得争。观，是帮你判断这架值不值得打、该在哪打。"),

 ("s07", "第三个字，沉。看清了之后，沉住气，先不吵。这里有个心理学小知识：人的怒气就像一阵浪，冲到最高也就持续6到10秒，然后自己会退下去。所以沉默一会儿，不是怂，是让那股火自己过去。你越急着辩解、越急着赢，对方越觉得你在狡辩。先沉住，让子弹飞一会儿，等大家都冷静了，你再说的话才有人听。沉，是给理智腾地方。"),

 ("s08", "第四个字，隔。物理上、信息上，跟冲突拉开距离。三招特别好用：第一，先离场——吵起来的地方，你找个借口先走开，眼不见心不烦；第二，别盯手机——对方发的气话、群里的起哄，别一遍遍刷，越刷越火；第三，设边界——该拉黑拉黑、该屏蔽屏蔽、该举报举报，不跟烂人烂事纠缠。隔，是保护你自己不被持续消耗。网上那些评论区对线、越对越凶的，往往就是没做到隔。"),

 ("s09", "第五个字，时。等火气降了，选个对的时间、对的地点，再开口。冷处理不是冷战、不是永远不说话，而是等合适的时机把事说清。比如跟爸妈闹别扭，别在饭桌上当众吵，等晚上俩人都平静了，再坐下来好好说；跟同学有误会，别在大家面前对质，下课私下聊。时机对了，同样的话，效果天差地别。时，是让冷变成成的关键一步。"),

 ("s10", "第六个字，收。冷处理到最后，要主动把关系收回来、破个冰。记住：冷处理不等于记仇、不等于不理人。你的目的是把事解决、把关系留住，不是把人推开。等气氛好了，主动说一句那天我也有点急，咱不纠结了，或者做件小事缓和一下。你看前面那个调解员，冷了几天后主动打电话聊家常，就是把关系收回来。收，是冷处理的句号，也是下一回好好说话的起点。"),

 ("s11", "光听不练假把式，咱们用六字，帮一个同学走一遍。小杰小组作业被队友当众冤枉你根本没做，队友还拍桌子。第一步，冷：小杰没立刻拍回去，心里先冷三秒。第二步，观：他发现队友其实自己漏了步骤、怕被老师骂，才拿他撒气。第三步，沉：下课再说，不当面争。第四步，隔：回座位先把证据，他早发过的文件记录，找出来，不刷群里起哄。第五步，时：下课后私下找队友和老师，平心静气拿出记录。第六步，收：队友发现错怪了他，道了歉，小杰也说没事，咱们把作业补齐。你看，全程没吵，问题还解决了——这就是冷处理的高明。"),

 ("s12", "今天的课到这儿，咱们把地图再过一遍：冷、观、沉、隔、时、收。再加上前八天，冷听准说退和、停核证说稳收、看稳问立析退、敬听缓据求谢、备稳清据应收、停呼数换说修、稳清据理求留、听缓换据求再，你手里已经有九套武器啦。老师送你一句话：会争的人很多，但懂得暂时不争的人，才是真厉害。下课前，晓晓老师用费曼学习法考考你。假如你在班级群被同学误会、还被好几个人起哄，你会怎么用这六个字，既不放过澄清、又不把场面搞炸？能讲给同学听明白，才是真学会了。加油，有时候不争，才是最高级的争。"),
]

# ===== 板书视觉 =====
VISUALS = {
 "s01": {"tag":"开场 · 复习","title":"上课啦！先热身，复习前8课👩‍🏫",
  "html":"""<p class='lead'>开讲前，先把前8课的口诀过一遍——</p>
  <div class='three'>
    <div class='card good'>第1课·冲突总纲<br><b>冷·听·准·说·退·和</b></div>
    <div class='card good'>第2课·被冤枉自证<br><b>停·核·证·说·稳·收</b></div>
    <div class='card good'>第3课·群体压力<br><b>看·稳·问·立·析·退</b></div>
    <div class='card good'>第4课·跟长辈/权威<br><b>敬·听·缓·据·求·谢</b></div>
    <div class='card good'>第5课·当众发言反驳<br><b>备·稳·清·据·应·收</b></div>
    <div class='card good'>第6课·情绪失控急救<br><b>停·呼·数·换·说·修</b></div>
    <div class='card good'>第7课·书面据理力争<br><b>稳·清·据·理·求·留</b></div>
    <div class='card good'>第8课·被拒绝再争取<br><b>听·缓·换·据·求·再</b></div>
  </div>
  <div class='banner'>今天第9课：冷处理与沉默战术——有时候「不争」才是最高级的争 🧊</div>"""},

 "s02": {"tag":"心法","title":"不是每场冲突，都该马上回嘴🤔",
  "html":"""<div class='two'>
    <div class='card bad'>忍气吞声<br><small>我怕了，我憋着<br>问题没解决<br>自己还委屈</small></div>
    <div class='card good'>冷处理 ✅<br><small>先不接招<br>等看清楚、火气降<br>再漂亮地把事解决</small></div>
  </div>
  <div class='def'>记住：<b>冷处理 ≠ 不争</b>，它只是把「争」挪到更合适的时间、更合适的地点。一个是怂，一个是有策略的暂停。</div>
  <div class='banner'>一遇冲突就回怼？很可能「一接就升级，越吵越乱」💡</div>""","quiz":"q1"},

 "s03": {"tag":"热点案例","title":"真事：法院调解员用「冷处理」把硬骨头纠纷办成了",
  "html":"""<div class='scene'>⚖️ 2025·宁夏西夏区。培训退费纠纷，被告陈老板电话里就吵：「我也懂法，不退！」调解员扈廷刚没对吵，而是——<b>冷处理</b>。</div>
  <svg class='scene-svg' viewBox='0 0 340 120' xmlns='http://www.w3.org/2000/svg' aria-label='冷处理时间线'>
    <rect x='4' y='20' width='72' height='80' rx='10' fill='rgba(255,255,255,.12)'/>
    <text x='40' y='40' font-size='11' text-anchor='middle' fill='#eafff4' font-family='serif'>①热冲突</text>
    <text x='40' y='74' font-size='30' text-anchor='middle' fill='#ff8a8a'>✗</text>
    <text x='92' y='64' font-size='16' text-anchor='middle' fill='#ffe08a'>➜</text>
    <rect x='100' y='20' width='72' height='80' rx='10' fill='rgba(255,255,255,.12)'/>
    <text x='136' y='40' font-size='11' text-anchor='middle' fill='#eafff4' font-family='serif'>②冷处理·暂停</text>
    <text x='136' y='74' font-size='26' text-anchor='middle' fill='#9bd6ff'>⏸</text>
    <text x='188' y='64' font-size='16' text-anchor='middle' fill='#ffe08a'>➜</text>
    <rect x='196' y='20' width='72' height='80' rx='10' fill='rgba(255,255,255,.12)'/>
    <text x='232' y='38' font-size='11' text-anchor='middle' fill='#eafff4' font-family='serif'>③数天后聊家常</text>
    <text x='232' y='58' font-size='10' text-anchor='middle' fill='#eafff4' font-family='serif'>讲法理</text>
    <text x='232' y='78' font-size='20' text-anchor='middle' fill='#9be8b0'>💬</text>
    <text x='284' y='64' font-size='16' text-anchor='middle' fill='#ffe08a'>➜</text>
    <rect x='292' y='20' width='46' height='80' rx='10' fill='rgba(255,255,255,.12)'/>
    <text x='315' y='40' font-size='10' text-anchor='middle' fill='#eafff4' font-family='serif'>④退款</text>
    <text x='315' y='74' font-size='26' text-anchor='middle' fill='#9be8b0'>✓</text>
  </svg>
  <div class='def'>他记着一句话：<b>话赶话没好话，事赶事没好事</b>。先搁下案子让双方静心，几天后再从经营、信誉、诉讼风险聊起，等理智回来才讲法——陈老板主动退款，还送锦旗🎖️。</div>
  <div class='tip'>调解员方业寿说：约一半成功调解都用了「冷静期」，因为很多矛盾「表面是利益之争，实则是情绪在对抗」。</div>""","student":"student2"},

 "s04": {"tag":"核心口诀","title":"六字口诀 = 该不该现在争、怎么冷处理🧊",
  "html":"""<div class='koujue'>
    <span>冷</span><span>观</span><span>沉</span><span>隔</span><span>时</span><span>收</span>
  </div>
  <div class='rhyme'>
    冷住火，别接招；<br>观清楚，谁在闹；<br>沉住气，先不吵；<br>隔开来，别盯梢；<br>
    时机到，再开口；<br><b>收好尾，情不焦。</b>
  </div>""","quiz":"q2"},

 "s05": {"tag":"口诀①","title":"冷 —— 遇挑事，先别跳起来接招",
  "html":"""<div class='big'>冷</div>
  <div class='def'>遇到被人怼，<b>先别跳起来接招</b>，心里说一句「我先冷一下」。</div>
  <ul class='steps'>
    <li>🧊 先冷三秒，<b>不接第一句话、不回第一条消息</b></li>
    <li>🧠 给大脑一个缓冲（第6课：生气那一下理智还没上线）</li>
    <li>🚫 这时候回嘴最容易说错话、把事搞大</li>
  </ul>
  <div class='tip'>冷，是冷处理的开关。不是怕，是先把理智请回来。</div>""","quiz":"q3"},

 "s06": {"tag":"口诀②","title":"观 —— 看清：谁在拱火、气什么、场合对不对",
  "html":"""<div class='big'>观</div>
  <div class='def'>冷下来后，<b>看清楚三件事</b>👇</div>
  <div class='three'>
    <div class='card'>①谁在拱火<br><small>谁是带节奏<br>谁在起哄</small></div>
    <div class='card'>②气什么<br><small>对方真实<br>担心/委屈</small></div>
    <div class='card'>③场合对不对<br><small>现在该不该<br>当面说</small></div>
  </div>
  <div class='tip'>比如同学当众嘲讽你，只是想刷存在感——你越回嘴他越来劲，<b>这时候不值得争</b>。观，是判断「这架值不值得打、该在哪打」。</div>""","student":"student1"},

 "s07": {"tag":"口诀③","title":"沉 —— 沉住气，让那股火自己过去",
  "html":"""<div class='big'>沉</div>
  <div class='def'>看清之后，<b>沉住气，先不吵</b>。</div>
  <div class='def'>心理学小知识：人的怒气像一阵浪，冲到最高也就持续 <b>6~10 秒</b>，然后自己退下去。</div>
  <ul class='steps'>
    <li>🌊 沉默一会儿不是怂，是让那股火自己过去</li>
    <li>🗣️ 你越急着辩解、越急着赢，对方越觉得你狡辩</li>
    <li>🧩 等大家都冷静了，你再说的话才有人听</li>
  </ul>
  <div class='tip'>沉，是给理智腾地方——让子弹飞一会儿。</div>""","quiz":"q4"},

 "s08": {"tag":"口诀④","title":"隔 —— 物理/信息上，跟冲突拉开距离",
  "html":"""<div class='big'>隔</div>
  <div class='def'>三招特别好用，都是「拉开距离、保护自己」👇</div>
  <div class='three'>
    <div class='card'>①先离场<br><small>吵起来的地方<br>找借口先走开</small></div>
    <div class='card'>②别盯手机<br><small>不一遍遍刷<br>对方气话/群起哄</small></div>
    <div class='card'>③设边界<br><small>该拉黑拉黑<br>该举报举报</small></div>
  </div>
  <div class='tip'>网上那些「评论区对线、越对越凶」的，往往就是没做到「隔」。隔，是不跟烂人烂事纠缠。</div>""","quiz":"q5"},

 "s09": {"tag":"口诀⑤","title":"时 —— 选对时间地点，再开口",
  "html":"""<div class='big'>时</div>
  <div class='def'>冷处理 <b>不是冷战、不是永远不说话</b>，而是等合适时机把事说清。</div>
  <ul class='steps'>
    <li>👪 跟爸妈闹别扭：别饭桌上当众吵，等晚上都平静了再坐下来说</li>
    <li>🤝 跟同学有误会：别大家面前对质，下课私下聊</li>
    <li>⏰ 时机对了，<b>同样的话，效果天差地别</b></li>
  </ul>
  <div class='tip'>时，是让「冷」变成「成」的关键一步。</div>"""},

 "s10": {"tag":"口诀⑥","title":"收 —— 主动破冰，把关系收回来",
  "html":"""<div class='big'>收</div>
  <div class='def'>冷处理到最后，<b>要主动把关系收回来、破个冰</b>。</div>
  <div class='def'>记住：<b>冷处理 ≠ 记仇、≠ 不理人</b>。目的是把事解决、把关系留住，不是把人推开。</div>
  <ol class='flow'>
    <li>💬 气氛好了，主动说「那天我也有点急，咱不纠结了」</li>
    <li>🌱 或做件小事缓和一下</li>
    <li>🤝 前面调解员冷几天后主动打电话「聊家常」，就是把关系收回来</li>
  </ol>
  <div class='banner'>收，是冷处理的句号，也是下一回好好说话的起点 🔚</div>""","student":"student3"},

 "s11": {"tag":"实战演练","title":"用六字，帮小杰把「被冤枉拍桌子」化于无形",
  "html":"""<div class='scene'>🧒 小杰小组作业被队友当众冤枉「你根本没做」，队友还拍桌子。</div>
  <ol class='flow'>
    <li><b>冷</b>：没立刻拍回去，心里先冷三秒</li>
    <li><b>观</b>：发现队友自己漏了步骤、怕被老师骂，才拿他撒气</li>
    <li><b>沉</b>：下课再说，不当面争</li>
    <li><b>隔</b>：回座位先找出证据（早发过的文件记录），不刷群里起哄</li>
    <li><b>时</b>：下课后私下找队友和老师，平心静气拿出记录</li>
    <li><b>收</b>：队友发现错怪他、道了歉；小杰也说「没事，咱把作业补齐」</li>
  </ol>
  <div class='banner'>全程没吵，问题还解决了 —— 这就是冷处理的高明 ✅</div>"""},

 "s12": {"tag":"费曼总结","title":"下课前，晓晓老师考考你！",
  "html":"""<div class='koujue'>
    <span>冷</span><span>观</span><span>沉</span><span>隔</span><span>时</span><span>收</span>
  </div>
  <div class='quote'>会争的人很多，<br><b>但懂得「暂时不争」的人，才是真厉害。</b></div>
  <p class='lead'>费曼学习法：能把它<b>讲给「同学」听明白</b>，才是真的学会了 👇</p>""",
  "quiz":"qfinal"},
}

# ===== 费曼提问（章节末固定）=====
QUIZZES = {
 "q1": {"ask":"「冷处理」和「忍气吞声」，下面哪句说对了？",
   "type":"choice",
   "options":["冷处理是有策略的暂停，之后会选对时机把事解决；忍气吞声是憋着、问题没解决","两者完全一样，都是不敢争","冷处理就是永远不说话、记仇"],
   "answer":0,
   "explain":"冷处理≠不争，是有策略的暂停，把「争」挪到更合适的时间地点；忍气吞声才是怂、问题一直挂着。一个是方法，一个是逃避。"},
 "q2": {"ask":"复述一下：冷处理「六字口诀」是哪六个字？(先自己说，再点开对照)",
   "type":"reveal",
   "answer_text":"冷 · 观 · 沉 · 隔 · 时 · 收\n冷：遇挑事先别跳，不接第一句、不回第一条消息；观：看清谁在拱火、对方气什么、场合对不对；沉：沉住气先不吵，怒气峰值只6~10秒，让火自己过去；隔：物理/信息拉开距离（离场、不刷手机、拉黑举报）；时：等火气降了选对时间地点再开口（不是冷战）；收：主动破冰，把关系收回来。冷处理≠忍气吞声，是有策略的暂停。"},
 "q3": {"ask":"遇到被人当众怼，最好的第一反应通常是？",
   "type":"choice",
   "options":["立刻回怼，不然就输了","先冷三秒，不接第一句话、不回第一条消息","当场比谁嗓门大"],
   "answer":1,
   "explain":"生气那一下理智还没上线，马上回嘴最容易说错话、把事搞大。先冷三秒，是冷处理的开关——不是怕，是先把理智请回来。"},
 "q4": {"ask":"人的怒气冲到最高，一般能持续多久就开始自己退下去？",
   "type":"choice",
   "options":["一整天都不消","大概 6~10 秒","永远停不下来"],
   "answer":1,
   "explain":"心理学小知识：怒气像一阵浪，冲到峰值也就持续6~10秒就自己退。所以「沉默一会儿」不是怂，是让那股火过去、给理智腾地方——这就是「沉」。"},
 "q5": {"ask":"想跟冲突「拉开距离」（隔），下面哪个做法对？",
   "type":"choice",
   "options":["先离场、不刷手机、该拉黑就拉黑","一遍遍刷对方的气话越看越火","当场对线一定要争赢"],
   "answer":0,
   "explain":"「隔」=物理/信息上拉开距离：离场、不盯对话框、设边界（拉黑/屏蔽/举报）。越刷越火、越对线越凶，恰恰就是没做到「隔」，会持续消耗你。"},
 "qfinal": {"ask":"费曼大挑战🎓：你在班级群被同学误会，还被好几个人起哄。你会怎么用「冷观沉隔时收」，既不放过澄清、又不把场面搞炸？(先完整讲一遍，再点开参考答案)",
   "type":"reveal",
   "answer_text":"""「班级群被误会+被起哄」为例：
冷：先在群里不秒回、不接第一句气话，心里冷三秒，不跟着情绪走。
观：看清楚——带头起哄的同学可能只是想刷存在感，真正误会你的人未必恶意，群里围观的人越多你越回越被动。
沉：不当场在群里对线争辩，沉住气，让那阵火过去（怒气峰值就6~10秒）。
隔：先别一遍遍刷群、别被起哄带节奏；需要的话把群消息设成免打扰，保护自己的情绪。
时：等火气降了，选对时机——私下找那位误会的同学（或课后找老师）平心静气澄清事实，而不是在群里公开对质。
收：澄清后主动缓和，说一句「没事，误会解开就好」，把关系收回来，不让这事变成长期疙瘩。
全程没在群里互怼，误会也澄清了、场面没炸——这就是冷处理的高明：暂时不争，是为了把事争明白。"""},
}

# ===== 不定时抽考 =====
SURPRISE = {
 "sp1": {"ask":"🎯 突击小测：冷处理的第一步，最好先做什么？",
   "type":"choice",
   "options":["立刻回怼争赢","先冷三秒，不接第一句话、不回第一条消息（冷）","装没看见永远不理"],
   "answer":1,
   "explain":"冷，是冷处理的开关：遇挑事先别跳，给理智一个缓冲。不是怕，是把「争」挪到更合适的时机。"},
 "sp2": {"ask":"🎯 突击小测：人的怒气冲到最高，一般持续多久就自己退了？",
   "type":"choice",
   "options":["一整天","6~10 秒","一辈子"],
   "answer":1,
   "explain":"怒气像浪，峰值只持续6~10秒就退。所以「沉」住气、沉默一会儿不是怂，是让火自己过去、给理智腾地方。"},
 "sp3": {"ask":"🎯 突击小测：冷处理和「冷战/记仇」一样吗？",
   "type":"choice",
   "options":["一样，都是不理人","不一样：冷处理是暂不打、之后选时机把事解决并把关系收回来","冷处理就是认输"],
   "answer":1,
   "explain":"冷处理≠冷战≠认输。它是有策略的暂停，目的是把事解决、把关系留住；最后还要「收」——主动破冰。忍气吞声/记仇才是真怂。"},
 "sp4": {"ask":"🎯 突击小测：网上被喷、被起哄，最聪明的做法是？",
   "type":"choice",
   "options":["在评论区跟他对线争赢","不回线、该拉黑拉黑该举报举报，让风波自己散（隔）","挨个私信骂回去"],
   "answer":1,
   "explain":"「隔」=信息上拉开距离：不跟烂人烂事纠缠，不刷不回、拉黑举报，风波往往自己散。越对线越凶，恰恰是没做到隔。"},
}

# ===== 同学小剧场 =====
STUDENTS = {
 "student1": {
   "asker":"同学小宇","avatar":"🧑‍🎓",
   "question":"老师，我每次被怼就忍不住回嘴，然后越吵越大，怎么办呀？",
   "answer":"这是最典型的「没做到冷和沉」。给你两招立刻能用：\n\n第一招，被怼的那一秒，先在心里说「我先冷三秒」，同时配合第6课学的——深呼吸、数到十。怒气峰值就6~10秒，数完那股火就退了，你也就不会脱口而出伤人的话。\n第二招，物理上先离场。比如对方越说越凶，你就说「我先去个洗手间」走开，眼不见心不烦，等回来大家都冷静了再谈。\n记住：不接第一句话、不回第一条消息，就是「冷」；等火过去再开口，就是「沉」。你越能忍住那三秒，吵架就越少、越容易收场。"},
 "student2": {
   "asker":"同学小美","avatar":"👧",
   "question":"晓晓老师，冷处理是不是就是怂、就是不敢争啊？我怕别人觉得我好欺负。",
   "answer":"这恰恰是最容易搞反的一点：冷处理不是怂，是更聪明地争。\n\n你看前面讲的真事——法院调解员扈廷刚，面对态度强硬的老板，他没对吵，而是冷处理、几天后再聊家常讲法理，最后对方主动退款还送锦旗。他要是一上来就吵，这案子八成僵死。他不是不敢争，是把「争」挪到了对方理智在线的时候，一下子就把事办成了。\n真怂是「忍气吞声」：憋着、问题永远挂着、自己还委屈。冷处理是「先不接招、看清了、等火气降了，再漂亮地把事解决」。一个是逃避，一个是有策略的暂停。所以别怕显得好欺负——真正厉害的人，是懂得「暂时不争」的那个人。"},
 "student3": {
   "asker":"同学小浩","avatar":"🧒",
   "question":"老师，我在班级群被同学误会，好几个人跟着起哄，我要不要马上在群里怼回去？",
   "answer":"千万别在群里对线，那是把火浇油。用上「观、沉、隔、时」四步：\n\n观：你看清楚，带头起哄的同学多半只是想刷存在感，群里围观的人越多，你越回越被动——这时候不值得在公开场合争。\n沉：不当场在群里争辩，沉住气，让那阵火过去。\n隔：先别一遍遍刷群、别被起哄带节奏；把群消息设成免打扰，保护自己的情绪。\n时：等火气降了，私下找那位误会的同学（或课后找老师）平心静气澄清事实，而不是在群里公开对质。澄清完再说一句「没事，误会解开就好」，把关系收回来。\n你看，全程没在群里互怼，误会也澄清了、场面没炸——这就是冷处理的高明：暂时不争，是为了把事争明白。"},
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
    # 用已冻结的第8课原始页作为模板（含可替换 token），生成第9课独立页
    tpl_src = os.path.join(HERE, "lessons", "lesson_08", "index.html")
    if not os.path.exists(tpl_src):
        tpl_src = os.path.join(HERE, "index.html")
    tpl = open(tpl_src, encoding="utf-8").read()
    repl = [
      ("第8课 被拒绝后如何再争取 · 晓晓老师", "第9课 冷处理与沉默战术：有时不争才是最高级的争 · 晓晓老师"),
      (" · 第8课</h1>", " · 第9课</h1>"),
      ("被拒绝后，怎么体面地再争取一次：不撒泼、不放弃 · 六字口诀「听缓换据求再」· 初中生也能懂",
       "冷处理与沉默战术：有时“不争”才是最高级的争 · 六字口诀「冷观沉隔时收」· 初中生也能懂"),
      ("你已经掌握了「听缓换据求再」六步法", "你已经掌握了「冷观沉隔时收」六字法"),
      ("今天学的「听·缓·换·据·求·再」", "今天学的「冷·观·沉·隔·时·收」"),
    ]
    for a, b in repl:
        if a not in tpl:
            raise SystemExit("TOKEN NOT FOUND: " + a)
        tpl = tpl.replace(a, b)
    with open(os.path.join(LESSON_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(tpl)
    print("lessons/lesson_09/index.html written")

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
 <a class="card" href="lessons/lesson_09/index.html"><div class="n">第9课</div><div class="t">冷处理与沉默战术：有时“不争”才是最高级的争</div><div class="k">六字口诀「冷·观·沉·隔·时·收」</div></a>
 <a class="card" href="lessons/lesson_08/index.html"><div class="n">第8课</div><div class="t">被拒绝之后，怎么体面地再争取一次</div><div class="k">六字口诀「听·缓·换·据·求·再」</div></a>
 <a class="card" href="lessons/lesson_07/index.html"><div class="n">第7课</div><div class="t">书面据理力争：把道理写下来，理性维权/申诉</div><div class="k">六字口诀「稳·清·据·理·求·留」</div></a>
 <div class="note">说明：第1–6课为早期「单页演进」版本（每天覆盖更新），如需把它们也制成各自独立的永久网页，告诉我一声即可补制。第7、8、9课起已改为「每课一个永久网页、永不再覆盖」的新模式。</div>
</div></body></html>"""
    with open(os.path.join(HERE, "index.html"), "w", encoding="utf-8") as f:
        f.write(hub)
    print("root hub index.html rewritten (julilizheng/ course directory)")

if __name__ == "__main__":
    manifest = asyncio.run(gen_audio())
    build_content(manifest)
    build_lesson_html()
    build_hub()
    print("ALL DONE -> lessons/lesson_09/")
