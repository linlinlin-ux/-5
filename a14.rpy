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

label a14:
play music "audio/推理.mp3"
scene 走廊
narrator_adv "走廊里安静得出奇，墙壁上的灯将几个人的影子投在地毯上。"
show 陈铭 at right
role1 "这么大的宅邸，晚上却几乎听不到其他动静。"
hide 陈铭
narrator_adv "陈铭沿着走廊缓步前行，经过几扇紧闭的房门。"
show 陈铭 at right
role1 "这些应该都是客房。"
hide 陈铭
narrator_adv "走廊尽头有一扇与其他房门略有不同的门，门牌上没有标注房间用途。"
show 陈铭 at right
role1 "这间房间没有标记……不过现在贸然进去，恐怕不太合适。"
hide 陈铭
narrator_adv "陈铭没有碰那扇门，只是记下了它的位置。"
play music "audio/卧室.mp3"
narrator_adv "他转身回到自己的客房。今晚没有发现足以解释周砚为何避而不见的线索。"
menu:
    "回客房休息":
        jump a12
