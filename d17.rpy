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

label d17:
play music "audio/宁静.mp3"
scene 大厅
with dissolve
narrator_adv "陈铭趁着其他人不在，来到许知微身边。"
show 陈铭 at right
role1 "方便单独聊几句吗？"
hide 陈铭
show 许知微 at right
role3 "是有什么发现吗？"
hide 许知微
show 陈铭 at right
role1 "不是。我只是想知道，你对最近发生的事情怎么看。"
hide 陈铭
show 许知微 at right
role3 "我不知道……这几天发生的事情太多了。"
hide 许知微
show 陈铭 at right
role1 "你刚才提到了十年前的事情。你是不是知道些什么？"
hide 陈铭
show 许知微 at right
role3 "我只是觉得，周砚把我们叫到这里，肯定不是没有原因的。"
hide 许知微
show 陈铭 at right
role1 "你认为他想让我们面对过去？"
hide 陈铭
show 许知微 at right
role3 "也许吧。但我不明白，为什么要用这种方式。"
hide 许知微
show 陈铭 at right
role1 "你和陆闻川以前关系怎么样？"
hide 陈铭
show 许知微 at right
role3 "不算特别好。他有些事情从来不愿意告诉别人。"
hide 许知微
show 陈铭 at right
role1 "比如？"
hide 陈铭
show 许知微 at right
role3 "他很在意自己的利益，也经常因为一些事情和别人发生争执。"
hide 许知微
show 陈铭 at right
role1 "你知道他最近有没有和谁发生矛盾吗？"
hide 陈铭
show 许知微 at right
role3 "不清楚。我不想随便怀疑任何人。"
hide 许知微
show 陈铭 at right
role1 "好，我知道了。"
hide 陈铭
show 许知微 at right
role3 "陈铭……你真的能找到凶手吗？"
hide 许知微
show 陈铭 at right
role1 "我会尽力。"
hide 陈铭
narrator_adv "许知微没有再说话。陈铭结束了谈话，暂时没有从她口中得到更多有用的信息。"
menu:
    "与程烈单独谈谈":
        jump d18

    "暂停调查":
        jump d19
