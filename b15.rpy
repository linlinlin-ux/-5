define role1 = Character('陈铭', color="#c8c8ff", image="role1")
define role2 = Character('陆闻川', color="#c8c8ff", image="role2")
define role3 = Character('许知微', color="#c8c8ff", image="role3")
define role4 = Character('程烈', color="#c8c8ff", image="role4")
define role5 = Character('顾承骁', color="#c8c8ff", image="role5")
define role6 = Character('林伯', color="#c8c8ff", image="role6")
define role7 = Character('周砚', color="#c8c8ff", image="role7")
define narrator_nvl = Character(None, kind=nvl)
define narrator_adv = Character(None, kind=adv)
define config.voice_filename_format = "audio/{filename}"

label b15:
play music "audio/杀人之夜.mp3"
scene 走廊早
show 陈铭 at right
with dissolve
role1 "在继续调查之前，我想先问清楚一件事。"
hide 陈铭
show 陈铭 at right
role1 "你们都认识周砚，而且认识了很多年。十年前，你们之间究竟发生过什么？"
hide 陈铭
show 陆闻川 at right
role2 "不是已经说过了吗？就是一次举报。学校取消了周末补课，事情闹得有些难看。"
hide 陆闻川
show 陈铭 at right
role1 "只是一次举报，为什么你们现在提起他时，还是这么紧张？"
hide 陈铭
show 陆闻川 at right
role2 "因为那件事害得所有人都不痛快！你想听的就是这个答案吗？"
hide 陆闻川
show 许知微 at right
role3 "陆闻川，你别激动……"
hide 许知微
show 陈铭 at right
role1 "许知微，你之前提到过班级群里的事情。那时候究竟发生了什么？"
hide 陈铭
show 许知微 at right
role3 "有人会在群里点名问周砚今天又举报了谁。后来，他的座位被挪到了最后一排，值日也总是轮到他打扫厕所。"
hide 许知微
show 许知微 at right
role3 "还有人撕过他的试卷。班主任知道以后，没有真正阻止这些事。"
hide 许知微
show 陈铭 at right
role1 "你当时知道这些事情吗？"
hide 陈铭
show 许知微 at right
role3 "知道……至少有一部分，我是知道的。"
hide 许知微
show 顾承骁 at right
role5 "说到底，不就是一次举报引起的事情？至于把它说得这么严重吗？"
hide 顾承骁
show 陆闻川 at right
role2 "你倒是说得轻松。"
hide 陆闻川
show 顾承骁 at right
role5 "我只是觉得，事情已经过去十年了，现在追究这些有什么用？"
hide 顾承骁
show 陈铭 at right
role1 "过去十年，并不代表当时发生的事情就不存在。"
hide 陈铭
show 顾承骁 at right
role5 "那你们想怎么样？让我现在向他道歉？"
hide 顾承骁
show 陈铭 at right
role1 "许知微，那你做了什么？"
hide 陈铭
show 许知微 at right
role3 "我没有参与撕试卷，也没有带头欺负他。我只是没有站出来。"
hide 许知微
show 程烈 at right
role4 "够了！你们打算把十年前的事翻出来说多少遍？"
hide 程烈
show 陈铭 at right
role1 "程烈，现在没人要求你承认没有做过的事。我们只是想知道当时发生了什么。"
hide 陈铭
show 程烈 at right
role4 "我跟他确实发生过冲突，但我不记得你说的那些细节。"
hide 程烈
show 陈铭 at right
role1 "你是不记得，还是不想说？"
hide 陈铭
show 程烈 at right
role4 "你少用这种语气审问我！"
hide 程烈
show 陈铭 at right
role1 "……好，我暂时不追问。"
hide 陈铭
show 陆闻川 at right
role2 "你自己不也在那个班里吗？现在装得像个局外人一样，有意思吗？"
hide 陆闻川
show 陈铭 at right
role1 "我没有说自己是局外人。"
hide 陈铭
narrator_adv "陈铭说完，短暂地沉默了一下。他很快移开目光，没有继续解释。"
show 陆闻川 at right
role2 "说起来，周砚以前的长相，和顾承骁确实有几分相似。"
hide 陆闻川
show 许知微 at right
role3 "你现在才说？他们两个站在一起的时候，有时候确实容易让人看错。"
hide 许知微
show 顾承骁 at right
role5 "长得像又怎么样？难道长得像的人就一定有什么关系？"
hide 顾承骁
show 陈铭 at right
role1 "你们以前经常把他们认错吗？"
hide 陈铭
show 陆闻川 at right
role2 "也没有经常。只是有些角度看过去，轮廓确实很像。"
hide 陆闻川
show 陈铭 at right
role1 "……我知道了。继续说正事吧。"
menu:
    "核对第一夜行踪":
        jump b13
