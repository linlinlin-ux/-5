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

label c8:
play music "audio/荒谬2.mp3"
scene 地下室入口
show 陈铭 at right
with dissolve
role1 "在继续讨论之前，我想知道，你们当初为什么答应来到这里？"
hide 陈铭
show 陆闻川 at right
role2 "邀请函上说有十年前的霸凌证据，我当然想知道到底是谁拿到了这些东西。"
hide 陆闻川
show 许知微 at right
role3 "我也是。我不希望十年前的事情再被翻出来。"
hide 许知微
show 程烈 at right
role4 "我来这里是想把事情问清楚，不代表我有什么好隐瞒的。"
hide 程烈
show 顾承骁 at right
role5 "我已经说过了，只是想看看周砚究竟想做什么。"
hide 顾承骁
show 陈铭 at right
role1 "你们有没有收到过邀请函之外的消息？或者有人私下联系过你们？"
hide 陈铭
narrator_adv "几个人互相看了一眼，却没有人立刻回答。"
show 陆闻川 at right
role2 "没有。至少我没有。"
hide 陆闻川
show 许知微 at right
role3 "我也没有。"
hide 许知微
show 程烈 at right
role4 "你是在怀疑我们私下串通？"
hide 程烈
show 陈铭 at right
role1 "我只是想确认有没有遗漏的信息。"
hide 陈铭
show 顾承骁 at right
role5 "问完了吗？如果没有别的事情，我不想继续浪费时间。"
hide 顾承骁
narrator_adv "陈铭没有继续追问。他注意到众人都在刻意回避某些话题，但目前还没有足够依据判断原因。"
menu:
    "结束讨论":
        jump c9
