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

label d18:
play music "audio/宁静.mp3"
scene 走廊
with dissolve
narrator_adv "陈铭找到独自站在走廊上的程烈，准备和他单独谈谈。"
show 陈铭 at right
role1 "程烈，我有些事情想问你。"
hide 陈铭
show 程烈 at right
role4 "又怎么了？"
hide 程烈
show 陈铭 at right
role1 "你刚才似乎很确定，凶手和十年前的事情有关。"
hide 陈铭
show 程烈 at right
role4 "我只是觉得这件事太巧了。"
hide 程烈
show 陈铭 at right
role1 "你是不是知道什么？"
hide 陈铭
show 程烈 at right
role4 "我知道的事情不比你多。"
hide 程烈
show 陈铭 at right
role1 "那你为什么一直强调有人想让知情者闭嘴？"
hide 陈铭
show 程烈 at right
role4 "因为我不相信这些事情都是巧合。"
hide 程烈
show 陈铭 at right
role1 "你和陆闻川以前有过矛盾吗？"
hide 陈铭
show 程烈 at right
role4 "有过一些争执，但那都是以前的事情了。"
hide 程烈
show 陈铭 at right
role1 "是什么事情？"
hide 陈铭
show 程烈 at right
role4 "没什么好说的。他那个人太看重利益，很多时候根本不顾别人的感受。"
hide 程烈
show 陈铭 at right
role1 "你们最近还有联系吗？"
hide 陈铭
show 程烈 at right
role4 "没有。至少我没有主动找过他。"
hide 程烈
show 陈铭 at right
role1 "好，我知道了。"
hide 陈铭
show 程烈 at right
role4 "陈铭，我劝你一句。别太相信这里的任何人。"
hide 程烈
show 陈铭 at right
role1 "包括你吗？"
hide 陈铭
show 程烈 at right
role4 "当然。"
hide 程烈
narrator_adv "程烈说完便离开了走廊。陈铭暂时没有从这次谈话中找到直接证据。"
menu:
    "与许知微单独谈谈":
        jump d17

    "暂停调查":
        jump d19
