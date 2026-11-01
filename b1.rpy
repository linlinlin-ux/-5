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

label b1:
play music "audio/杀人之夜.mp3"
scene 卧室早
narrator_adv "第二天早晨，一阵急促的敲门声将陈铭从睡梦中惊醒。"
show 林伯 at right
role6 "陈先生！请您立刻出来！出事了！"
hide 林伯
show 陈铭 at right
role1 "出什么事了？"
hide 陈铭
show 林伯 at right
role6 "您先跟我来！其他几位也请尽快过来！"
scene 走廊早
hide 林伯
with dissolve
narrator_adv "陈铭跟着林伯来到走廊深处的一间房间。陆闻川、许知微、程烈和顾承骁也陆续赶到。"
show 陆闻川 at right
role2 "一大早把所有人叫来，到底发生什么事了？"
hide 陆闻川
show 林伯 at right
role6 "是主人的房间……我刚才进去的时候，发现他已经倒在地上了。"
scene 命案现场
hide 林伯
with dissolve
narrator_adv "房门敞开着。房间内陈设整齐，一具尸体倒在床边，已经没有了呼吸。"
show 许知微 at right
role3 "……那是周砚？"
hide 许知微
narrator_adv "尸体的面容清晰可辨，没有明显毁损。陈铭只看了一眼，便认出了邀请函上的那个人。"
show 陈铭 at right
role1 "是周砚。"
hide 陈铭
show 程烈 at right
role4 "怎么可能？昨天晚上他还让我们留在这里，今天人就死了？"
hide 程烈
show 陆闻川 at right
role2 "林伯，你昨天不是说他身体不舒服吗？你就没有再来看看？"
hide 陆闻川
show 林伯 at right
role6 "主人说想独自休息，我不敢擅自打扰。今天早上我来送早餐，才发现……"
hide 林伯
show 许知微 at right
role3 "你是说，整整一夜都没人知道他出了什么事？"
hide 许知微
show 林伯 at right
role6 "是。"
hide 林伯
show 顾承骁 at right
role5 "先别急着互相指责。人已经死了，现在最重要的是弄清楚发生了什么。"
hide 顾承骁
show 陈铭 at right
role1 "顾承骁说得对。所有人先不要碰房间里的东西，尤其是尸体周围的物品。"
hide 陈铭
show 陈铭 at right
role1 "林伯，你先留在这里。其他人也暂时不要离开这层楼。我要先检查现场。"
menu:
    "检查尸体":
        jump b2

    "检查房间":
        jump b3

    "询问林伯":
        jump b4
