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

label b3:
play music "audio/杀人之夜.mp3"
scene 命案现场
with dissolve
narrator_adv "陈铭转而检查房间。屋内摆设整齐，床铺和桌椅没有明显被大幅移动的迹象。"
show 陈铭 at right
role1 "房间看起来没有发生过大规模的打斗。"
hide 陈铭
show 程烈 at right
role4 "那是不是说明凶手没有跟他打起来？"
hide 程烈
show 陈铭 at right
role1 "不能这么判断。现场整齐，不代表没有发生过冲突。"
hide 陈铭
narrator_adv "陈铭走到房门附近，检查门锁和门把手。"
show 陈铭 at right
role1 "目前没有看到明显的破坏痕迹。至于门是否曾经被人从外面打开，还需要更多信息。"
hide 陈铭
show 许知微 at right
role3 "如果凶手认识周砚，他可能根本不需要强行闯入。"
hide 许知微
show 陈铭 at right
role1 "这是一个可能性，但目前还不能确定凶手与死者的关系。"
hide 陈铭
narrator_adv "陈铭随后查看窗户。窗户没有明显破损，窗边也没有足以直接证明有人进出的痕迹。"
show 陆闻川 at right
role2 "所以你查了半天，什么都没找到？"
hide 陆闻川
show 陈铭 at right
role1 "调查不是每次都能立刻找到答案。排除错误的判断，同样重要。"
hide 陈铭
narrator_adv "陈铭记下房间的情况，决定再从其他人的证词中寻找突破口。"
menu:
    "检查窗户与窗边痕迹":
        jump b6

    "检查房间遗留物":
        jump b7

    "询问林伯":
        jump b4
