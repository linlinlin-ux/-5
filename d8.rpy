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

label d8:
play music "audio/恐怖.mp3"
scene 走廊早
with dissolve
narrator_adv "陈铭让众人回忆昨晚休息前后的情况，重点确认是否有人见过陆闻川。"
show 陈铭 at right
role1 "昨晚回房之后，你们有没有再见过陆闻川？"
hide 陈铭
show 许知微 at right
role3 "我没有。我回房后就没再出来。"
hide 许知微
show 程烈 at right
role4 "我也没有。我昨晚一直待在自己房间。"
hide 程烈
show 顾承骁 at right
role5 "我之前在走廊遇到过陈铭，之后就回房了。"
hide 顾承骁
show 陈铭 at right
role1 "当时你说自己也是听见声音才出来的。"
hide 陈铭
show 顾承骁 at right
role5 "没错。"
hide 顾承骁
show 陈铭 at right
role1 "除此之外，你有没有见过陆闻川？"
hide 陈铭
show 顾承骁 at right
role5 "没有。"
hide 顾承骁
narrator_adv "陈铭又询问了众人今天早晨的行动。"
show 许知微 at right
role3 "我是听见程烈敲门，才知道陆闻川没有下来。"
hide 许知微
show 程烈 at right
role4 "我先去敲他的门，没人回应，后来才叫上你们。"
hide 程烈
show 陈铭 at right
role1 "也就是说，最先发现异常的是程烈。"
hide 陈铭
show 程烈 at right
role4 "对，但我没有进过他的房间。"
hide 程烈
show 陈铭 at right
role1 "好，我会把这些情况记录下来。"
hide 陈铭
narrator_adv "众人的说法暂时没有出现明显矛盾，但仍然无法确定陆闻川具体的死亡时间。"
menu:
    "询问众人是否见过那枚戒指":
        jump d9
