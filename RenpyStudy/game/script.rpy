define ch_jemin = Character('제민', color = "#00BFB7")
define ch_bora = Character("보라", color = "#C986BE")

define narrator = Character(None,kind = nvl)

image bg_001 = "bg/BackGround_001.jpg"
image scg_bora:
    im.FactorScale("charactor/charator_001.png",0.5)
    yalign 0.0

define cetner = Position(xalign = 0.5, yalign = 0.0)
define left = Position(xalign = 0.2, yalign = 0.0)
define right = Position(xalign = 0.8, yalign = 0.0)

label start:
    scene bg_001

    "당신은 현제 교실에 있습니다"

    ch_jemin "보라가 교실에 들어왔다"
    #주석 테스트 

    show scg_bora at left
    ch_bora "안녕"


    return
