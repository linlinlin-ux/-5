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

label b12:
play music "audio/杀人之夜.mp3"
scene 走廊早
show 陈铭 at right
with dissolve
role1 "我们先停一下。继续各自调查，只会让已经掌握的信息变得更加混乱。"
hide 陈铭
show 陈铭 at right
role1 "先说目前能够确认的事情。尸体是在今天早晨被发现的，房间的门没有明显的破坏痕迹。"
hide 陈铭
role1 "衣着没有明显的撕扯痕迹，房间里也没有发现足以直接判断死因的证据。"
show 陆闻川 at right
role2 "说了这么多，不还是不知道他怎么死的？"
hide 陆闻川
show 程烈 at right
role4 "那你想怎么样？难道站在这里等他自己活过来？"
hide 程烈
show 许知微 at right
role3 "你们能不能先别吵……现在最重要的不是查清楚发生了什么吗？"
hide 许知微
show 顾承骁 at right
role5 "查？这里又没有警察。你们不会真打算把自己当侦探吧？"
hide 顾承骁
show 陈铭 at right
role1 "不查，我们就只能接受别人告诉我们的答案。你们愿意相信谁，那是你们的事。"
hide 陈铭
show 陆闻川 at right
role2 "那你说，接下来查什么？"
hide 陆闻川
show 陈铭 at right
role1 "先核对昨晚的行动。每个人最后一次见到死者是什么时候，之后又去了哪里。"
hide 陈铭
show 许知微 at right
role3 "昨晚不是都说过了吗？"
hide 许知微
show 陈铭 at right
role1 "说过，不代表已经核实。人在紧张的时候，很容易遗漏细节。"
hide 陈铭
show 程烈 at right
role4 "行。你问吧。反正我没做过什么亏心事。"
hide 程烈
show 陈铭 at right
role1 "那就从昨晚晚饭结束后开始。一个一个说清楚。"
menu:
    "核对第一夜行踪":
        jump b13

    "重新整理尸体与房间的线索":
        jump b14

    "继续追问十年前的旧事":
        jump b15
