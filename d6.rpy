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

label d6:
play music "audio/杀人之夜.mp3"
scene 命案现场2
with dissolve
narrator_adv "陈铭仔细检查公文包的夹层，发现内侧有一个空着的文件袋。"
show 陈铭 at right
role1 "这里原本应该放过什么东西。"
hide 陈铭
show 许知微 at right
role3 "会不会是刚才那些交易文件？"
hide 许知微
show 陈铭 at right
role1 "不像。文件袋的尺寸更大，而且里面还有纸张留下的压痕。"
hide 陈铭
narrator_adv "陈铭检查文件袋边缘，发现封口处有一道细小的撕裂痕迹。"
show 程烈 at right
role4 "有人把里面的东西拿走了？"
hide 程烈
show 陈铭 at right
role1 "不能排除这种可能。"
hide 陈铭
narrator_adv "陈铭将公文包放回原处，注意到桌面上还有一处被擦拭过的痕迹。"
show 陈铭 at right
role1 "这里也需要记录。"
menu:
    "查看桌上的资金文件":
        jump d5

    "整理线索":
        jump d7
