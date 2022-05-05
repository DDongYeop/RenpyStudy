define ch_jemin = Character('제민', color = "#00BFB7")
define ch_bora = Character("보라", color = "#C986BE")
define ch_seol = Character("설아", color = "#FFFF4A")

define narrator = Character(None,kind = nvl)

define ch_narrator = Character(None)

image bg_001 = "bg/BackGround_001.jpg"
image bg_002 = "bg/BackGround_002.jpg"

image scg_bora:
    im.FactorScale("charactor/charator_001.png",0.5)
    yalign 0.0

image scg_seol:
    im.FactorScale("charactor/charator_002.png",0.5)
    yalign 0.0

define cetner = Position(xalign = 0.5, yalign = 0.0)
define left = Position(xalign = 0.2, yalign = 0.0)
define right = Position(xalign = 0.8, yalign = 0.0)

label start:
    scene bg_001 with fade 

    "이것은 나레이션 입니다"
    nvl clear

    ch_jemin "보라가 교실에 들어왔다"
    #주석 테스트 

    show scg_bora at right with dissolve

    ch_bora "안녕"

    show scg_seol at left with dissolve

    ch_seol "안녕 나도 왔어"

    ch_bora "너는 누가 더 좋아?"

    ch_seol "내가 더 좋지?"

    scene bg_002 with dissolve

    menu:
        "보라가 좋아":
            ch_jemin "보라가 더 좋아"
            ch_seol "나쁜 자식"
        "설아가 좋아":
            ch_jemin "설아가 좋아"
            ch_bora "나쁜 자식"
        "둘다 싫어":
            ch_jemin "둘다 싫어"
            "보라, 설아" "너는 정말 최악이야"
    
    # 위 선택지가 다 끝나면 여기로 온다
    ch_jemin "어떤식으로 결정하든 한명은 날 싫어하네"

    hide scg_bora
    hide scg_seol
    with dissolve

    ch_jemin "보라가 나갔다"

    ch_narrator "속상하다"

    ch_jemin "마음이 상한채로 집으로 왔다"
    return
