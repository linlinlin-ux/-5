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

label d10:
play music "audio/恐怖.mp3"
scene 纸条
with dissolve
narrator_adv "陈铭重新拿出从陆闻川口袋里发现的纸条，将它小心展开。"
scene 走廊早
show 陈铭 at right
with dissolve
role1 "之前只看见了一个金额，现在可以仔细辨认一下其他内容。"
hide 陈铭
narrator_adv "纸条上有几行被折痕遮住的文字，其中一行写着一笔转账金额，旁边还有一个日期。"
show 陈铭 at right
role1 "这个日期……比我们收到邀请函的时间早了几天。"
hide 陈铭
show 许知微 at right
role3 "这能说明什么？"
hide 许知微
show 陈铭 at right
role1 "说明这笔交易可能早在我们登岛之前就已经发生了。"
hide 陈铭
show 程烈 at right
role4 "他是不是欠了别人钱？"
hide 程烈
show 陈铭 at right
role1 "也有可能。但纸条没有写明收款人的姓名。"
hide 陈铭
narrator_adv "陈铭将纸条与书桌上的资金文件进行对照，发现两者记录的金额一致。"
show 陈铭 at right
role1 "至少可以确认，这张纸条和他桌上的资金记录有关。"
hide 陈铭
show 顾承骁 at right
role5 "就算他有经济纠纷，也不能说明这就是杀人动机。"
hide 顾承骁
show 陈铭 at right
role1 "我知道。我们现在只是确认陆闻川生前处理过哪些事情。"
hide 陈铭
narrator_adv "陈铭把纸条重新收好，暂时没有找到更多有效信息。"
menu:
    "返回大厅":
        jump d11
