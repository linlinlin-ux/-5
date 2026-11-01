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

label d11:
play music "audio/推理.mp3"
scene 大厅早
with dissolve
narrator_adv "陈铭将戒指、纸条和资金文件摆在一起，重新梳理目前掌握的信息。"
show 陈铭 at right
role1 "现在可以确认，陆闻川生前存在一笔金额较大的资金往来。"
hide 陈铭
show 陈铭 at right
role1 "这枚戒指的来历仍然不明，纸条上的交易记录也没有出现明确的姓名。"
hide 陈铭
show 许知微 at right
role3 "所以我们还是不知道是谁杀了他。"
hide 许知微
show 陈铭 at right
role1 "是。目前也无法确定这些东西是否与他的死亡直接相关。"
hide 陈铭
show 程烈 at right
role4 "那接下来怎么办？"
hide 程烈
show 陈铭 at right
role1 "我想再检查一次第一案的现场。"
hide 陈铭
show 顾承骁 at right
role5 "又回那个房间？"
hide 顾承骁
show 陈铭 at right
role1 "第一案和第二案之间可能存在我们尚未注意到的联系。重新检查一次，也许能找到遗漏的东西。"
hide 陈铭
narrator_adv "陈铭收起记录，决定独自前往最初发现尸体的房间。"
menu:
    "前往第一案现场":
        jump d12
