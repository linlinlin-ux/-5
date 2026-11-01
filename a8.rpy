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

label a8:
play music "audio/宁静.mp3"
scene 大厅
narrator_adv "夜色渐深，陆闻川、许知微和程烈已经等候多时。陈铭站在大厅一侧，观察着这栋陌生的豪宅。"
show 陆闻川 at right
role2 "顾承骁怎么还没到？就剩他一个人了。"
hide 陆闻川
show 许知微 at right
role3 "邀请函上也没说具体几点。再等等吧。"
hide 许知微
show 程烈 at right
role4 "我可没耐心一直等下去。"
hide 程烈
narrator_adv "大门终于传来动静。一名男子走进大厅，脱下外套，目光扫过在场的几个人。"
show 顾承骁 at right
role5 "抱歉，路上耽搁了一会儿。"
hide 顾承骁
show 陆闻川 at right
role2 "你总算来了。我们都到了，就等你一个。"
hide 陆闻川
show 顾承骁 at right
role5 "看来大家都很准时。"
hide 顾承骁
show 许知微 at right
role3 "你知道周砚为什么把我们叫来吗？"
hide 许知微
show 顾承骁 at right
role5 "邀请函只提到十年前的事情。我也想知道他到底想做什么。"
hide 顾承骁
show 陈铭 at right
role1 "既然人都到齐了，应该很快就能知道答案。"
hide 陈铭
narrator_adv "众人简单交谈了几句，却始终没有见到这栋豪宅真正的主人周砚。"
show 陆闻川 at right
role2 "说起来，周砚人呢？他把我们叫来，总不能一直不露面吧。"
hide 陆闻川
narrator_adv "就在这时，林伯从走廊深处走了出来。"
show 林伯 at right
role6 "各位，实在抱歉。主人今天身体抱恙，不方便接待客人。"
hide 林伯
show 陆闻川 at right
role2 "周砚身体不舒服？那他什么时候能见我们？"
hide 陆闻川
show 林伯 at right
role6 "主人希望各位今晚先在这里住下。明天身体好些，再与各位见面。"
hide 林伯
show 许知微 at right
role3 "还要在这里住一晚？"
hide 许知微
show 林伯 at right
role6 "客房已经准备好了。请各位放心。"
hide 林伯
show 程烈 at right
role4 "真够麻烦的。人都到了，偏偏主人不见客。"
hide 程烈
show 顾承骁 at right
role5 "既然周砚身体不适，那就明天再说吧。"
hide 顾承骁
show 陈铭 at right
role1 "现在确实没有其他办法。先休息，明天再问清楚。"
menu:
    "询问林伯周砚的身体情况":
        jump a9

    "与其他人商量留宿安排":
        jump a11

    "前往客房休息":
        jump a12
