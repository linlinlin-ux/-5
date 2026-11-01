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

label e29:
scene 储物间4
with dissolve
narrator_adv "陈铭将档案盒里的文件逐一取出，按照日期和资料类型重新整理。大部分文件已经泛黄，其中几页明显被人抽走。"
show 陈铭 at right
role1 "这些资料并不是同一时间整理的。最早的一份，距今已经十年。"
hide 陈铭
show 许知微 at right
role3 "这里有当年的学生名单。"
hide 许知微
narrator_adv "陈铭接过名单，发现上面有几个人的名字被圈了起来。名单上的部分字迹与旧照片背面的笔迹相似。"
show 顾承骁 at right
role5 "这几个人就是当年事件的相关人员？"
hide 顾承骁
show 陈铭 at right
role1 "现在还不能确定。名单只能证明他们曾经出现在同一份资料里。"
hide 陈铭
show 许知微 at right
role3 "那这张纸呢？"
hide 许知微
narrator_adv "许知微拿起一份事件记录的复印件。纸张中间缺了一块，剩余内容只能辨认出几个词语：学生冲突、证人、处理结果。"
show 陈铭 at right
role1 "这应该是当年某件校园事件的记录。"
hide 陈铭
show 顾承骁 at right
role5 "为什么连处理结果都被撕掉了？"
hide 顾承骁
show 陈铭 at right
role1 "有人不想让这份记录完整地留下来。至于是谁，还不能确定。"
hide 陈铭
narrator_adv "陈铭继续翻找，在档案盒最底部发现一张折叠起来的纸。纸上没有完整内容，只留下了一行手写文字。"
show 陈铭 at right
role1 "……当时还有一名在场者。"
hide 陈铭
show 许知微 at right
role3 "在场者？"
hide 许知微
show 陈铭 at right
role1 "这份资料没有写出他的名字。"
hide 陈铭
narrator_adv "陈铭盯着那行字，神情逐渐沉了下来。他没有继续说下去，而是将纸重新折好。"
show 顾承骁 at right
role5 "你是不是想到了什么？"
hide 顾承骁
show 陈铭 at right
role1 "还没有。先检查其他文件。"
menu:
    "检查其他文件":
        jump e30
