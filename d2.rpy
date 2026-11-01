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

label d2:
play music "audio/恐怖.mp3"
scene 命案现场2
with dissolve
narrator_adv "陈铭轻轻推开房门，房间内一片安静。窗帘半掩，桌上的物品摆放得有些凌乱。"
show 陈铭 at right
role1 "陆闻川？你在里面吗？"
hide 陈铭
narrator_adv "没有人回应。陈铭走进房间，目光很快停留在床边。"
show 许知微 at right
role3 "那边……是不是有人？"
hide 许知微
narrator_adv "陆闻川倒在床边的地毯上，一动不动。"
show 程烈 at right
role4 "陆闻川！"
hide 程烈
narrator_adv "程烈快步上前，蹲下身查看情况，随后脸色骤变。"
show 程烈 at right
role4 "没气了……"
hide 程烈
show 许知微 at right
role3 "怎么会这样？昨天晚上不是还好好的吗？"
hide 许知微
show 顾承骁 at right
role5 "先别碰他。"
hide 顾承骁
show 陈铭 at right
role1 "所有人退后，不要随意移动房间里的东西。"
hide 陈铭
narrator_adv "陈铭走到尸体旁，仔细观察陆闻川的状态。"
show 陈铭 at right
role1 "暂时不要判断死亡原因。我们先保护现场。"
hide 陈铭
show 许知微 at right
role3 "又死人了……我们真的要一个接一个死在这里吗？"
hide 许知微
show 程烈 at right
role4 "到底是谁干的？有本事就站出来！"
hide 程烈
show 顾承骁 at right
role5 "你现在喊也没有用。"
hide 顾承骁
narrator_adv "陈铭没有回应众人的争吵，而是开始观察房间里的情况。"
show 陈铭 at right
role1 "这次必须仔细检查，不能再遗漏任何东西。"
menu:
    "检查陆闻川尸体":
        jump d3

    "检查房间现场":
        jump d4
