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

label c5:
play music "audio/荒谬2.mp3"
scene 地下室入口
with dissolve
narrator_adv "地下室入口处，陈铭将刚才记录的调查结果重新整理了一遍。"
show 陈铭 at right
role1 "目前有三点值得注意。"
hide 陈铭
show 陈铭 at right
role1 "第一，楼梯中段有一道新鲜擦痕，但还不能确定是什么造成的。"
hide 陈铭
show 陈铭 at right
role1 "第二，林伯后脑有撞击伤，手掌也有擦伤，无法仅凭这些判断他是意外坠落。"
hide 陈铭
show 陈铭 at right
role1 "第三，昨晚晚饭后，没人能准确说出林伯最后去了哪里。"
hide 陈铭
show 陆闻川 at right
role2 "说了半天，还是不知道他到底怎么死的。"
hide 陆闻川
show 陈铭 at right
role1 "是。但至少可以确定，我们还不能把这件事简单当成意外。"
hide 陈铭
show 许知微 at right
role3 "第一案也是这样……周砚死在房间里，现在林伯又死在地下室。"
hide 许知微
show 程烈 at right
role4 "你想说什么？"
hide 程烈
show 许知微 at right
role3 "我只是觉得，这两件事发生得太巧了。"
hide 许知微
show 顾承骁 at right
role5 "你怀疑有人杀了他们？"
hide 顾承骁
show 许知微 at right
role3 "难道你不觉得奇怪吗？"
hide 许知微
show 陆闻川 at right
role2 "等等。如果这不是意外，那是不是说明凶手一直就在我们中间？"
hide 陆闻川
narrator_adv "众人一时没有说话，彼此之间的目光开始变得警惕。"
show 程烈 at right
role4 "你看着我干什么？难道你怀疑是我？"
hide 程烈
show 陆闻川 at right
role2 "我又没指名道姓。"
hide 陆闻川
show 程烈 at right
role4 "那你刚才那句话是什么意思？"
hide 程烈
show 陈铭 at right
role1 "都冷静一点。现在没有证据能证明在场任何一个人是凶手。"
hide 陈铭
show 许知微 at right
role3 "可是我们为什么会被邀请到这里？周砚究竟想让我们看什么？"
hide 许知微
show 陆闻川 at right
role2 "你们有没有想过另一种可能？"
hide 陆闻川
show 顾承骁 at right
role5 "什么可能？"
hide 顾承骁
show 陆闻川 at right
role2 "有人根本不是为了调查周砚才来到这里的。"
hide 陆闻川
show 陆闻川 at right
role2 "如果有人担心十年前的事情曝光，影响自己的工作和现在的生活呢？"
hide 陆闻川
show 许知微 at right
role3 "你的意思是，有人想趁这次机会销毁证据？"
hide 许知微
show 陆闻川 at right
role2 "不只是销毁证据。万一有人知道得太多，甚至可能被灭口。"
hide 陆闻川
narrator_adv "这句话让原本紧张的气氛彻底失控。"
show 程烈 at right
role4 "你少在这里胡说八道！"
hide 程烈
show 许知微 at right
role3 "可是林伯已经死了！你怎么知道他说的就不可能是真的？"
hide 许知微
show 顾承骁 at right
role5 "现在互相指责有什么用？我们连凶手是谁都不知道。"
hide 顾承骁
show 陆闻川 at right
role2 "那你倒是说说，为什么每次出事，你都这么冷静？"
hide 陆闻川
show 顾承骁 at right
role5 "你想说什么？"
hide 顾承骁
narrator_adv "两人的争执逐渐升级，其他人也开始加入争论。"
show 陈铭 at right
role1 "够了！继续这样争吵，只会让真正的问题变得更复杂。"
hide 陈铭
show 陈铭 at right
role1 "我们必须弄清楚，究竟是谁在隐瞒事情，以及他为什么要这么做。"
menu:
    "继续讨论":
        jump c6
