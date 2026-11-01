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

label e10:
play music "audio/推理2.mp3"
scene 大厅早
show 陈铭 at right
with dissolve
role1 "上次检查时，我们只确认了床铺凌乱，桌上有钥匙和一张带有划痕的纸。还有些地方没有仔细看。"
hide 陈铭
show 许知微 at right
role3 "你觉得他会把重要的东西留在自己的房间里？"
hide 许知微
show 陈铭 at right
role1 "如果他是突然离开的，未必来得及带走所有东西。"
hide 陈铭
show 许知微 at right
role3 "那先检查书桌吧。"
scene 卧室早
hide 许知微
show 陈铭 at right
with dissolve
role1 "抽屉里只有一些日常用品和旧文件，没有明显异常。"
hide 陈铭
show 许知微 at right
role3 "这里有个空文件夹。"
hide 许知微
show 陈铭 at right
role1 "文件夹里面没有东西，但内侧有一道明显的折痕，像是曾经夹过比较厚的文件。"
hide 陈铭
show 许知微 at right
role3 "会不会是我们之前在陆闻川那里发现的那种资金文件？"
hide 许知微
show 陈铭 at right
role1 "不能确定。先把它记录下来。"
hide 陈铭
show 许知微 at right
role3 "床底下也没有东西。"
scene 角落2
hide 许知微
show 陈铭 at right
with dissolve
role1 "等等，床头柜后面有一小块纸屑。"
scene 角落
hide 陈铭
show 许知微 at right
with dissolve
role3 "和地下储藏室发现的那片碎纸有点像。"
scene 卧室早
hide 许知微
show 陈铭 at right
with dissolve
role1 "纸张颜色和厚度确实相近，但还不足以证明它们来自同一张纸。"
hide 陈铭
show 许知微 at right
role3 "程烈为什么会有这种纸？"
hide 许知微
show 陈铭 at right
role1 "也许他曾经接触过某份文件。我们需要把纸屑和地下室的碎纸放在一起比对。"
hide 陈铭
show 许知微 at right
role3 "如果能拼起来，是不是就能知道他在调查什么？"
hide 许知微
show 陈铭 at right
role1 "有这个可能。不过在确认之前，不能急着下结论。"
hide 陈铭
show 许知微 at right
role3 "那现在怎么办？"
hide 许知微
show 陈铭 at right
role1 "先把发现的纸屑收好，再去找顾承骁。让他也看看这些东西。"
menu:
    "会合":
        jump e11
