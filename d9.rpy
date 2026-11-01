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

label d9:
play music "audio/恐怖.mp3"
scene 戒指
with dissolve
narrator_adv "陈铭拿出从陆闻川手中发现的戒指，放在桌面上。"
scene 走廊早
show 陈铭 at right
with dissolve
role1 "你们有人见过这枚戒指吗？"
hide 陈铭
show 许知微 at right
role3 "没见过。陆闻川平时戴的不是这款吧？"
hide 许知微
show 程烈 at right
role4 "我没注意过他戴什么首饰。"
hide 程烈
show 顾承骁 at right
role5 "看起来不像普通的装饰戒指。"
hide 顾承骁
show 陈铭 at right
role1 "你认识它？"
hide 陈铭
show 顾承骁 at right
role5 "不认识，只是看起来价格不低。"
hide 顾承骁
show 陆闻川 at right
role2 "旁白"
hide 陆闻川
narrator_adv "陈铭注意到戒指内侧刻着一个很小的字母和数字组合，但暂时无法辨认具体含义。"
show 陈铭 at right
role1 "戒指内侧有刻字，或许能用来确认它的来源。"
hide 陈铭
show 许知微 at right
role3 "会不会是别人送给他的？"
hide 许知微
show 程烈 at right
role4 "也可能是他自己买的。陆闻川不是一直很看重这些东西吗？"
hide 程烈
show 陈铭 at right
role1 "现在还不能确定。我们需要找到它的主人，或者弄清楚它为什么会出现在陆闻川手里。"
hide 陈铭
narrator_adv "陈铭将戒指收好，准备之后再寻找刻字对应的信息。"
menu:
    "结束询问":
        jump d10
