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

label g4:
play music "audio/荒谬.mp3"
scene 大厅早
with dissolve
narrator_adv "陈铭回到大厅。周砚仍然站在窗边，仿佛早已料到他会回来。"
show 顾承骁 at right
role7 "你查到了？"
hide 顾承骁
show 陈铭 at right
role1 "第一具尸体是顾承骁。"
hide 陈铭
show 顾承骁 at right
role7 "看来你终于认真查了一次。"
hide 顾承骁
show 陈铭 at right
role1 "你一直以顾承骁的身份待在我们中间。"
hide 陈铭
show 顾承骁 at right
role7 "你们从来没有真正分辨过我和他。"
hide 顾承骁
show 陈铭 at right
role1 "你利用了我们的误认，让所有人以为你已经死了。"
hide 陈铭
show 顾承骁 at right
role7 "。"
hide 顾承骁
show 陈铭 at right
role1 "你把我们带到这里，是为了复仇。"
hide 陈铭
show 顾承骁 at right
role7 "你知道我为什么恨他们吗？"
hide 顾承骁
show 陈铭 at right
role1 "因为十年前的霸凌。"
hide 陈铭
show 顾承骁 at right
role7 "不只是霸凌。"
hide 顾承骁
narrator_adv "周砚的表情终于出现变化。他看向窗外，像是在看一段已经过去很久、却从未真正结束的记忆。"
show 顾承骁 at right
role7 "那天我接到消息，我妈妈病情恶化，正在医院抢救。我只想赶回去见她一面。"
hide 顾承骁
show 顾承骁 at right
role7 "可他们把我堵在学校里。我求过他们，让他们放我走。我告诉他们家里出了急事。"
hide 顾承骁
show 陈铭 at right
role1 "……"
hide 陈铭
show 顾承骁 at right
role7 "他们没有停下来。对他们来说，那只是一次寻常的欺负。"
hide 顾承骁
show 顾承骁 at right
role7 "等我赶到的时候，已经晚了。"
hide 顾承骁
show 顾承骁 at right
role7 "你知道最折磨人的是什么吗？我永远不知道，如果我早到一点，妈妈是不是还有机会。"
hide 顾承骁
show 陈铭 at right
role1 "所以你把这份恨留到了现在。"
hide 陈铭
show 顾承骁 at right
role7 "我忘不了。顾承骁的傲慢、陆闻川的贪婪、许知微的嫉妒、程烈的暴怒……他们每个人都参与了那一天。"
hide 顾承骁
show 陈铭 at right
role1 "林伯呢？他为什么也死了？"
hide 陈铭
show 顾承骁 at right
role7 "林伯知道我的计划。他后来想阻止我，也想让你们离开这里。我不能让他毁掉一切。"
hide 顾承骁
show 陈铭 at right
role1 "你杀了他们。"
hide 陈铭
show 顾承骁 at right
role7 "是。顾承骁、陆闻川、程烈，还有林伯。"
hide 顾承骁
show 陈铭 at right
role1 "你觉得这样就能让十年前的一切得到补偿吗？"
hide 陈铭
show 顾承骁 at right
role7 "我从来没说过能补偿。"
hide 顾承骁
narrator_adv "周砚转过身，终于直视陈铭。"
show 顾承骁 at right
role7 "还有你。陈铭，你当年明明拍下了录像。"
hide 顾承骁
show 陈铭 at right
role1 "我知道。"
hide 陈铭
show 顾承骁 at right
role7 "你听见我求他们放我走，也知道我家里出了事。可你只是站在那里。"
hide 顾承骁
show 顾承骁 at right
role7 "你没有帮我，也没有把录像交出去。"
hide 顾承骁
show 陈铭 at right
role1 "……"
hide 陈铭
show 顾承骁 at right
role7 "我想知道，十年过去了，你是不是还会像那天一样，转身离开？"
menu:
    "承认一切":
        jump g11

    "忘却一切":
        jump g12
