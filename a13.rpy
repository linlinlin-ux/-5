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

label a13:
play music "audio/推理.mp3"
scene 大厅
narrator_adv "大厅里已经没有其他人。壁灯散发着昏黄的光，映在空荡荡的长桌上。"
show 陈铭 at right
role1 "这座宅邸布置得很讲究，不过总觉得有些地方不太对劲。"
scene 长桌
hide 陈铭
narrator_adv "长桌上摆着几套餐具，数量显然是为今晚留宿的客人准备的。"
show 陈铭 at right
role1 "连餐具都提前准备好了……看来林伯早就知道我们今晚会留下。"
hide 陈铭
narrator_adv "大厅一侧的壁炉已经熄灭，旁边整齐地摆放着几把椅子，没有发现明显的打斗痕迹。"
show 陈铭 at right
role1 "暂时看不出什么。比起在这里胡乱猜测，明天见到周砚之后再问清楚更实际。"
scene 大厅
hide 陈铭
narrator_adv "陈铭最后看了一眼大厅，转身朝客房走去。"
menu:
    "回客房休息":
        jump a12

    "前往走廊查看":
        jump a14
