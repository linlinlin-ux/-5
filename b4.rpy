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

label b4:
play music "audio/杀人之夜.mp3"
scene 命案现场
show 陈铭 at right
with dissolve
role1 "林伯，我需要你重新说明一下发现尸体的经过。"
hide 陈铭
show 林伯 at right
role6 "今天早晨，我像往常一样准备给主人送早餐。来到房门外敲门，却一直没有回应。"
hide 林伯
show 陈铭 at right
role1 "然后呢？"
hide 陈铭
show 林伯 at right
role6 "我担心主人出了什么事，于是打开房门进去查看，随后就发现他倒在地上。"
hide 林伯
show 陈铭 at right
role1 "你进去之前，房门是关着的吗？"
hide 陈铭
show 林伯 at right
role6 "是的。我记得房门当时是关着的。"
hide 林伯
show 陈铭 at right
role1 "你有没有发现门锁损坏，或者其他异常？"
hide 陈铭
show 林伯 at right
role6 "没有。我当时太着急了，看到主人倒在地上，就立刻出来叫各位。"
hide 林伯
show 陈铭 at right
role1 "昨晚你最后一次见到周砚是什么时候？"
hide 陈铭
show 林伯 at right
role6 "晚饭后不久。我确认主人回房休息，就没有再打扰他。"
hide 林伯
show 陈铭 at right
role1 "你确定此后没有再见过他？"
hide 陈铭
show 林伯 at right
role6 "是的。至少在今天早晨发现他之前，我没有再见过主人。"
hide 林伯
narrator_adv "林伯回答得很平静，但仅凭这段证词，陈铭还无法确认昨晚究竟发生了什么。"
show 陈铭 at right
role1 "好，我暂时没有其他问题。如果想起新的细节，请立刻告诉我。"
menu:
    "检查房间":
        jump b3

    "检查尸体":
        jump b2

    "询问陆闻川的旧事":
        jump b8
