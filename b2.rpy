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

label b2:
play music "audio/杀人之夜.mp3"
scene 命案现场
show 陈铭 at right
with dissolve
role1 "我先检查尸体。所有人暂时不要靠近。"
hide 陈铭
narrator_adv "陈铭蹲下身，仔细观察尸体的姿势与周围情况。"
show 陈铭 at right
role1 "尸体的面容完整，没有明显的严重外伤。"
hide 陈铭
show 陆闻川 at right
role2 "那能看出他是怎么死的吗？"
hide 陆闻川
show 陈铭 at right
role1 "现在还不能确定。仅凭外观，无法准确判断死因。"
hide 陈铭
show 许知微 at right
role3 "他看起来不像是经历过激烈挣扎。"
hide 许知微
show 陈铭 at right
role1 "不能只凭这一点下结论。是否存在挣扎痕迹，还需要结合房间里的情况判断。"
hide 陈铭
narrator_adv "陈铭继续观察尸体的双手，注意到其中一只手的手指微微蜷曲。"
show 陈铭 at right
role1 "暂时没有发现足以直接确定死因的线索。"
hide 陈铭
show 顾承骁 at right
role5 "也就是说，我们现在连他什么时候死的都不知道？"
hide 顾承骁
show 陈铭 at right
role1 "是。具体死亡时间需要进一步检查，不能凭猜测确定。"
hide 陈铭
narrator_adv "陈铭站起身，让众人继续保持距离，以免破坏现场。"
menu:
    "检查房间":
        jump b3

    "询问林伯":
        jump b4

    "检查尸体衣着":
        jump b5
