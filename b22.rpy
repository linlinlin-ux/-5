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

label b22:
play music "audio/杀人之夜.mp3"
scene 走廊早
show 陈铭 at right
with dissolve
role1 "林伯，你在这座宅子里工作多久了？"
hide 陈铭
show 林伯 at right
role6 "已经有些年头了。"
hide 林伯
show 陈铭 at right
role1 "你以前就认识周砚吗？"
hide 陈铭
show 林伯 at right
role6 "认识。主人还没有如今的条件时，我就见过他。"
hide 林伯
show 陈铭 at right
role1 "你们以前住得很近？"
hide 陈铭
show 林伯 at right
role6 "可以这么说。他母亲还在世的时候，我们确实有过一些往来。"
hide 林伯
show 陈铭 at right
role1 "那你应该知道他十年前经历过什么。"
hide 陈铭
show 林伯 at right
role6 "知道一些，但那毕竟是主人的私事，我不方便随意议论。"
hide 林伯
show 陈铭 at right
role1 "他母亲去世之后，你还见过他吗？"
hide 陈铭
show 林伯 at right
role6 "后来就很少见了。他离开原来的地方以后，我们便没有多少联系。"
hide 林伯
show 陈铭 at right
role1 "你刚才说，你知道一些旧事。那你认为，十年前的事情对他影响大吗？"
hide 陈铭
show 林伯 at right
role6 "有些事情，旁人看起来已经过去了，当事人却未必真的放下。"
hide 林伯
show 陈铭 at right
role1 "你是在说周砚一直记着那些事？"
hide 陈铭
show 林伯 at right
role6 "我不敢替主人下判断。"
hide 林伯
show 陈铭 at right
role1 "那你觉得，他这次邀请这些人来到岛上，是为了什么？"
hide 陈铭
show 林伯 at right
role6 "主人的想法，我不敢妄加揣测。"
hide 林伯
show 陈铭 at right
role1 "你似乎很谨慎。"
hide 陈铭
show 林伯 at right
role6 "我只是一个管家，不应该替主人说话。"
hide 林伯
narrator_adv "林伯没有否认自己了解周砚的过去，却始终避开了更具体的细节。"
show 陈铭 at right
role1 "好，我暂时不问了。"
menu:
    "进入第二次集中讨论":
        jump b23
