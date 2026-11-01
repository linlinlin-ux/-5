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

label h12:
play music "audio/宁静.mp3"
scene 大厅早
with dissolve
narrator_adv "顾承骁等待着陈铭的回答。"
show 陈铭 at right
role1 "十年前的事情已经过去了。"
hide 陈铭
show 顾承骁 at right
role5 "你还是想把自己摘干净。"
hide 顾承骁
show 陈铭 at right
role1 "我没有参与霸凌，也无法为当时发生的事情负责。"
hide 陈铭
show 顾承骁 at right
role5 "你明明看见了。"
hide 顾承骁
show 陈铭 at right
role1 "我不想再谈这件事。"
hide 陈铭
narrator_adv "陈铭再次选择回避。他没有承认自己的责任，也没有继续追问眼前这个人的真实身份。"
show 顾承骁 at right
role5 "你果然还是没有改变。"
hide 顾承骁
narrator_adv "陈铭转过身，离开了大厅。身后的那个人没有挽留他。"
scene 结局四
with dissolve
narrator_adv "结局四"
