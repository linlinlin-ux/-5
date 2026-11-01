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

label b18:
play music "audio/推理.mp3"
scene 长桌
with dissolve
narrator_adv "夜色渐深，大厅里的灯仍然亮着。其余几人陆续回房休息，四周逐渐安静下来。"
narrator_adv "大厅布置得十分整洁，墙上挂着几幅旧画，角落里摆放着一座落地钟。"
show 陈铭 at right
role1 "这座宅子维护得很好，不像是长期无人居住的地方。"
hide 陈铭
narrator_adv "陈铭注意到，落地钟的指针正在缓慢移动，但钟面上的时间似乎与自己的手表有些出入。"
show 陈铭 at right
role1 "……是钟走得不准，还是我的手表出了问题？"
hide 陈铭
narrator_adv "他没有继续纠结这个细节，只是记下了大厅的布局。"
show 陈铭 at right
role1 "如果明天真的发生什么事，至少得知道这里有哪些可以藏身或通行的地方。"
menu:
    "查看走廊":
        jump b19

    "前往第三天早晨（第三章）":
        jump b20
