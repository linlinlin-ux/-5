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

label b11:
play music "audio/杀人之夜.mp3"
scene 走廊早
show 陈铭 at right
with dissolve
role1 "程烈，我也想问你十年前的事。"
hide 陈铭
show 程烈 at right
role4 "又是周砚？人都死了，你还要翻多少旧账？"
hide 程烈
show 陈铭 at right
role1 "他邀请我们来到这里，就是为了谈十年前的事情。现在他死了，这件事反而更值得查清楚。"
hide 陈铭
show 程烈 at right
role4 "高中那点破事，谁没跟同学闹过矛盾？"
hide 程烈
show 陈铭 at right
role1 "你认为周砚遭遇的只是普通矛盾？"
hide 陈铭
show 程烈 at right
role4 "我可没说他没受过委屈。"
hide 程烈
show 陈铭 at right
role1 "那你承认他当年在学校里受到过排斥？"
hide 陈铭
show 程烈 at right
role4 "我承认。举报事件之后，很多人都不待见他。"
hide 程烈
show 陈铭 at right
role1 "你有没有参与过针对他的事情？"
hide 陈铭
show 程烈 at right
role4 "我跟他发生过冲突，但我没必要把所有事情都告诉你。"
hide 程烈
show 陈铭 at right
role1 "你说的冲突，具体是什么？"
hide 陈铭
show 程烈 at right
role4 "记不清了。十年过去了，你以为我会把每次吵架都记在本子上？"
hide 程烈
show 陈铭 at right
role1 "你记不清细节，却记得自己和他发生过冲突。"
hide 陈铭
show 程烈 at right
role4 "你这是在套我的话？"
hide 程烈
show 陈铭 at right
role1 "我是在记录每个人的说法。你可以不回答，但我会把你的态度也记下来。"
hide 陈铭
narrator_adv "程烈皱起眉头，显然不愿意继续谈下去。他承认自己与周砚发生过冲突，却没有提供具体时间和经过。"
show 陈铭 at right
role1 "好。之后如果想起细节，请再告诉我。"
menu:
    "询问陆闻川的旧事":
        jump b8

    "询问许知微的旧事":
        jump b9

    "询问顾承骁的旧事":
        jump b24

    "返回第一次集中讨论":
        jump b12
