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

label h11:
play music "audio/宁静.mp3"
scene 大厅早
with dissolve
narrator_adv "顾承骁等待着陈铭的回答。"
show 陈铭 at right
role1 "我不会再否认自己当年做过的事。"
hide 陈铭
show 顾承骁 at right
role5 "你终于愿意承认了？"
hide 顾承骁
show 陈铭 at right
role1 "我拍下了录像，却没有提交。我知道周砚当时想离开，也知道他有急事。"
hide 陈铭
show 陈铭 at right
role1 "我害怕自己受到牵连，所以没有帮他。"
hide 陈铭
show 顾承骁 at right
role5 "现在承认，还有什么意义？"
hide 顾承骁
show 陈铭 at right
role1 "我不知道能不能弥补，但我不想再逃避。"
hide 陈铭
show 陈铭 at right
role1 "不过，我仍然不知道你究竟参与了多少事情。"
hide 陈铭
narrator_adv "顾承骁看着陈铭，没有纠正他的判断。"
scene 结局三
with dissolve
narrator_adv "结局三"
