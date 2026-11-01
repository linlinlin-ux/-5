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

label d13:
play music "audio/推理.mp3"
scene 孔雀羽毛
with dissolve
narrator_adv "陈铭将孔雀羽毛放在桌面上，借着窗边的光仔细观察。"
scene 起点
show 陈铭 at right
with dissolve
role1 "羽毛保存得还算完整，颜色也很特别。"
hide 陈铭
narrator_adv "羽毛末端呈现出类似眼睛的圆形纹路，外圈是暗绿色与蓝色交错的色泽。"
show 陈铭 at right
role1 "这种纹路……确实很像孔雀的尾羽。"
hide 陈铭
narrator_adv "陈铭检查羽毛根部，没有发现明显的血迹或其他特殊痕迹。"
show 陈铭 at right
role1 "单凭这根羽毛，暂时无法判断它属于谁。"
hide 陈铭
narrator_adv "他将羽毛装进证物袋，与之前记录的第一案线索放在一起。"
show 陈铭 at right
role1 "第一案的现场，可能还有一些我们没有注意到的细节。"
hide 陈铭
narrator_adv "陈铭暂时没有得出结论。他决定先保留这件物品，等找到更多相关线索后再进行判断。"
menu:
    "返回大厅":
        jump d14
