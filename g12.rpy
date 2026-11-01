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

label g12:
play music "audio/宁静.mp3"
scene 大厅早
with dissolve
narrator_adv "周砚等待着陈铭的回答。陈铭却迟迟没有开口。"
show 陈铭 at right
role1 "十年前的事情已经过去了。"
hide 陈铭
show 顾承骁 at right
role7 "你还是不愿意承认。"
hide 顾承骁
show 陈铭 at right
role1 "当时动手的人不是我。我也没有办法改变已经发生的事。"
hide 陈铭
show 顾承骁 at right
role7 "可你看见了。"
hide 顾承骁
show 陈铭 at right
role1 "我不想再谈了。"
hide 陈铭
narrator_adv "陈铭避开周砚的目光。他明明已经知道第一案的真实身份，也知道周砚为何走到今天，却仍然不愿面对自己的责任。"
show 顾承骁 at right
role7 "原来十年过去，你还是没有变。"
hide 顾承骁
narrator_adv "陈铭没有回答。"
scene 结局二
with dissolve
narrator_adv "结局二"
