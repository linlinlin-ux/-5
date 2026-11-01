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

label a4:
play music "audio/宁静.mp3"
scene 豪宅
narrator_adv "你沿着豪宅外墙走了一小段。"
narrator_adv "房屋背面有几扇窄窗，玻璃上积着灰。"
narrator_adv "通往地下室的侧门紧闭着，门边堆着几片枯叶。"
narrator_adv "这栋房子似乎已经很久没有人长期居住。"
show 陈铭 at right
role1 "邀请者为什么选在这里？"
hide 陈铭
narrator_adv "你没有答案，于是返回正门。"
scene 大厅
with fade
narrator_adv "大厅里，其他人正等着最后一位客人。"
show 程烈 at right
role4 "看完了？"
hide 程烈
show 陈铭 at right
role1 "嗯。"
hide 陈铭
narrator_adv "程烈没有再问。"
narrator_adv "你决定先做什么。"
menu:
    "和陆闻川聊聊":
        jump a5

    " 和许知微聊聊":
        jump a6

    "询问程烈是否知道更多情况":
        jump a7
