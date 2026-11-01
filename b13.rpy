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

label b13:
play music "audio/杀人之夜.mp3"
scene 走廊早
show 陈铭 at right
with dissolve
role1 "昨晚晚饭结束后，大家分别去了哪里？先从陆闻川开始。"
hide 陈铭
show 陆闻川 at right
role2 "我回了自己的房间。发生这种事之前，我根本没打算在这里多待。"
hide 陆闻川
show 陈铭 at right
role1 "有人能证明吗？"
hide 陈铭
show 陆闻川 at right
role2 "没有。我一个人待着，还需要找人证明？"
hide 陆闻川
show 陈铭 at right
role1 "我只是确认情况。许知微，你呢？"
hide 陈铭
show 许知微 at right
role3 "我回房间休息了。中途好像听见过走廊有声音，但我没有出去看。"
hide 许知微
show 陈铭 at right
role1 "你记得大概是什么时候吗？"
hide 陈铭
show 许知微 at right
role3 "不太记得。可能是晚饭后，也可能更晚……我当时没在意。"
hide 许知微
show 程烈 at right
role4 "我也回了房间。你们不会觉得，只要听见一点动静，就能把人当成凶手吧？"
hide 程烈
show 陈铭 at right
role1 "目前没有任何人被认定为凶手。继续说，顾承骁。"
hide 陈铭
show 顾承骁 at right
role5 "我当然也回房间了。还有什么好问的？"
hide 顾承骁
show 陈铭 at right
role1 "你昨晚不是一直在说想离开这里吗？后来有没有找林伯？"
hide 陈铭
show 顾承骁 at right
role5 "没有。我又不是不知道船明天才来。找他有什么用？"
hide 顾承骁
show 陈铭 at right
role1 "好。那我最后问一个问题。昨晚有人见过周砚吗？"
hide 陈铭
show 陆闻川 at right
role2 "林伯不是说，主人身体不舒服吗？谁会特意去打扰他？"
hide 陆闻川
show 许知微 at right
role3 "我没见过。"
hide 许知微
show 程烈 at right
role4 "我也没有。"
hide 程烈
show 顾承骁 at right
role5 "没见过。现在可以结束了吗？"
hide 顾承骁
show 陈铭 at right
role1 "暂时没有更多问题。不过，大家的说法目前都缺少独立证实。"
hide 陈铭
show 陈铭 at right
role1 "仅凭这一点，还不能确定昨晚究竟发生了什么。"
menu:
    "返回第一次集中讨论":
        jump b12

    "追问林伯昨晚的行动":
        jump b16

    "等待第三天船只到来":
        jump b17
