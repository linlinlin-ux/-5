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

label h2:
play music "audio/宁静.mp3"
scene 大厅早
with dissolve
narrator_adv "陈铭离开地下储物间，回到大厅。那个一直以顾承骁身份留在众人身边的人正站在窗边。"
show 顾承骁 at right
role5 "你回来了。档案看完了吗？"
hide 顾承骁
show 陈铭 at right
role1 "看完了一部分。十年前的事情，比我想象得严重。"
hide 陈铭
show 顾承骁 at right
role5 "你现在才知道？"
hide 顾承骁
show 陈铭 at right
role1 "我知道他们曾经霸凌周砚，但我不知道那一天还发生过别的事。"
hide 陈铭
show 顾承骁 at right
role5 "那你现在知道了。"
hide 顾承骁
show 陈铭 at right
role1 "你似乎很在意那件事。"
hide 陈铭
show 顾承骁 at right
role5 "如果有人毁掉了你最后一次见到母亲的机会，你会怎么想？"
hide 顾承骁
show 陈铭 at right
role1 "……"
hide 陈铭
narrator_adv "顾承骁望向窗外，语气平静得近乎冷漠。"
show 顾承骁 at right
role5 "那天，那个人一直求他们放自己走。他说家里出了急事，可他们没有一个人愿意放过他。"
hide 顾承骁
show 陈铭 at right
role1 "你是说周砚的母亲？"
hide 陈铭
show 顾承骁 at right
role5 "她当时正在医院抢救。"
hide 顾承骁
show 陈铭 at right
role1 "他最后赶到了吗？"
hide 陈铭
show 顾承骁 at right
role5 "没有赶上。至少，他一直觉得自己没能赶上。"
hide 顾承骁
narrator_adv "对方停顿了一会儿，没有继续解释。"
show 顾承骁 at right
role5 "你们可以忘记那一天，但有些人做不到。"
hide 顾承骁
show 陈铭 at right
role1 "所以你认为这些死亡都是为了报复？"
hide 陈铭
show 顾承骁 at right
role5 "你很快就会明白。"
scene 卧室早
hide 顾承骁
with dissolve
narrator_adv "陈铭离开了大厅，回到卧室内整理线索"
menu:
    "下一段故事":
        jump h3
