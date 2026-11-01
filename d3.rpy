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

label d3:
play music "audio/恐怖.mp3"
scene 命案现场2
with dissolve
narrator_adv "陈铭蹲在陆闻川身旁，先观察他的姿势和衣着。"
show 陈铭 at right
role1 "身体已经没有反应，暂时无法仅凭姿势判断具体死因。"
hide 陈铭
narrator_adv "陆闻川的衣领有些凌乱，右手紧握着，手指之间似乎夹着什么东西。"
show 陈铭 at right
role1 "他的手里好像有东西。"
hide 陈铭
narrator_adv "陈铭小心地观察，发现那是一枚陌生的戒指。"
show 许知微 at right
role3 "这不是他平时戴的那枚吧？"
hide 许知微
show 陈铭 at right
role1 "现在还不能确定它属于谁。"
hide 陈铭
narrator_adv "陈铭继续检查，发现陆闻川的口袋里有一张折叠过的纸条。"
show 程烈 at right
role4 "又是什么？"
hide 程烈
show 陈铭 at right
role1 "先记录下来，等检查完现场再看。"
hide 陈铭
narrator_adv "陈铭将戒指和纸条分别收好，继续观察尸体。"
show 陈铭 at right
role1 "目前能确认的线索有限，还需要结合房间情况判断。"
menu:
    "返回房间现场":
        jump d4
