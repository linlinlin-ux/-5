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

label c16:
play music "audio/推理.mp3"
scene 卧室
with dissolve
narrator_adv "陈铭回到房间，关上房门。他将白天找到的旧照片放在床头柜上，随后躺下休息。"
narrator_adv "这一夜，豪宅里再也没有传出其他动静。"
narrator_adv "海风不断拍打着窗户，时间一点点过去。"
narrator_adv "第三天，就这样结束了。"
menu:
    "进入第四天（第四章）":
        jump d1
