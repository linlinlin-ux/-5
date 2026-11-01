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

label g11:
play music "audio/宁静.mp3"
scene 大厅早
with dissolve
narrator_adv "周砚等待着陈铭的回答。大厅里安静得只能听见窗外的风声。"
show 陈铭 at right
role1 "我不会再逃避十年前的事情。"
hide 陈铭
show 顾承骁 at right
role7 "你终于肯承认了？"
hide 顾承骁
show 陈铭 at right
role1 "我拍下了录像，却没有提交。我看见你被他们围堵，也知道你急着赶去医院。"
hide 陈铭
show 陈铭 at right
role1 "我当时害怕惹祸，所以选择了离开。我没有资格说自己完全无辜。"
hide 陈铭
show 顾承骁 at right
role7 "现在承认这些，还有什么用？"
hide 顾承骁
show 陈铭 at right
role1 "我不能让过去重新发生，也不能让你母亲回来。但我至少可以承认自己做过的事。"
hide 陈铭
show 陈铭 at right
role1 "可我不会因为自己的过错，就认同你杀死其他人。"
hide 陈铭
narrator_adv "周砚看着陈铭，许久没有说话。"
scene 结局一
with dissolve
narrator_adv "结局一"
