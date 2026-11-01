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

label f2:
play music "audio/推理2.mp3"
scene 盒子
with dissolve
narrator_adv "陈铭从档案盒里找出另外几份同一天的记录。它们分别来自不同人的询问，记录内容存在一些出入。"
scene 工作间
show 陈铭 at right
with dissolve
role1 "这里说周砚曾经要求离开。"
hide 陈铭
narrator_adv "一份询问记录中写着，周砚当时情绪十分激动，多次要求顾承骁等人让开。"
show 陈铭 at right
role1 "可他们没有让他走。"
hide 陈铭
narrator_adv "另一份记录则将那次冲突描述成普通的同学争执，甚至没有提到周砚曾经急着离开。"
show 陈铭 at right
role1 "同一件事，为什么会有完全不同的说法？"
hide 陈铭
narrator_adv "陈铭继续翻阅，在一份材料的空白处发现了一行手写内容。"
show 陈铭 at right
role1 "“周砚多次提到家里有急事，需要立即离开。”"
hide 陈铭
narrator_adv "这句话没有出现在正式的事件结论里，像是后来被刻意忽略了。"
show 陈铭 at right
role1 "家里出了什么事？"
hide 陈铭
narrator_adv "陈铭将这份记录放到一旁，继续寻找当天的其他资料。"
menu:
    "寻找其他资料":
        jump f3
