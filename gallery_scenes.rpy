screen amy_gallery1:
    tag gallery

    if amy_bj1: #Coffee BJ
        imagebutton:
            auto "gui/gallery/amy/coffee_bj_%s.jpg"
            action Replay("g_amy_coffee_event1", locked=False)
            xalign 0.05
            yalign 0.35
            at thumbzoom
    else:
        imagebutton: #UNKNOWN
            idle "gui/gallery/locked.png"
            xalign 0.05
            yalign 0.35
            at thumbzoom

    if amy_titjob1: #Yoga Titjob
        imagebutton:
            auto "gui/gallery/amy/yoga_titjob_%s.jpg"
            action Replay("g_amy_daisy_yoga1", locked=False)
            xalign 0.35
            yalign 0.35
            at thumbzoom
    else:
        imagebutton: #UNKNOWN
            idle "gui/gallery/locked.png"
            xalign 0.35
            yalign 0.35
            at thumbzoom

    if amy_titjob1: #Car Sex
        imagebutton:
            auto "gui/gallery/amy/car_sex_%s.jpg"
            action Replay("g_amy_sophie_date1", locked=False)
            xalign 0.65
            yalign 0.35
            at thumbzoom
    else:
        imagebutton: #UNKNOWN
            idle "gui/gallery/locked.png"
            xalign 0.65
            yalign 0.35
            at thumbzoom

    if amy_plan: # Amy Plan
        imagebutton:
            auto "gui/gallery/amy/amy_plan_%s.jpg"
            action Replay("g_amy_plan", locked=False)
            xalign 0.95
            yalign 0.35
            at thumbzoom
    else:
        imagebutton:
            idle "gui/gallery/locked.png"
            xalign 0.95
            yalign 0.35
            at thumbzoom

    if amy_recon: # Amy Recon
        imagebutton:
            auto "gui/gallery/amy/amy_recon_%s.jpg"
            action Replay("g_amy_recon", locked=False)
            xalign 0.05
            yalign 0.65
            at thumbzoom
    else:
        imagebutton:
            idle "gui/gallery/locked.png"
            xalign 0.05
            yalign 0.65
            at thumbzoom

    if amy_cuck: # Amy Dinner Cuck
        imagebutton:
            auto "gui/gallery/amy/amy_dinner_%s.jpg"
            action Replay("g_amy_dinner", locked=False)
            xalign 0.35
            yalign 0.65
            at thumbzoom
    else:
        imagebutton:
            idle "gui/gallery/locked.png"
            xalign 0.35
            yalign 0.65
            at thumbzoom


    # if amy_bj1: # 3,1
    #     imagebutton:
    #         idle "gui/gallery/amy/coffee_bj.jpg"
    #         hover "gui/gallery/amy/coffee_bj.jpg"
    #         selected_idle "gui/gallery/amy/coffee_bj.jpg"
    #         action Show("daisy_hint")
    #         xalign 0.05
    #         yalign 0.95
    #         at thumbzoom
    # else:
    #     imagebutton:
    #         idle "gui/gallery/locked.png"
    #         xalign 0.05
    #         yalign 0.95
    #         at thumbzoom

screen daisy_gallery1:
    tag gallery

screen dani_gallery1:
    tag gallery

screen hikari_gallery1:
    tag gallery

    if nude_locker_hikari: #Locker Strip
        imagebutton:
            auto "gui/gallery/hikari/first_nude_%s.jpg"
            action Replay("g_hikari_nude_locker", locked=False)
            xalign 0.05
            yalign 0.35
            at thumbzoom
    else:
        imagebutton: #UNKNOWN
            idle "gui/gallery/locked.png"
            xalign 0.05
            yalign 0.35
            at thumbzoom

    if hikari_strip_intro: #Pool Dance
        imagebutton:
            auto "gui/gallery/hikari/first_strip_pool_%s.jpg"
            action Replay("g_hikari_stripclub1", locked=False)
            xalign 0.35
            yalign 0.35
            at thumbzoom
    else:
        imagebutton: #UNKNOWN
            idle "gui/gallery/locked.png"
            xalign 0.35
            yalign 0.35
            at thumbzoom

    if hikari_new_look: #Stripper Tease
        imagebutton:
            auto "gui/gallery/hikari/stripper_tease_%s.jpg"
            action Replay("g_hikari_new_look", locked=False)
            xalign 0.65
            yalign 0.35
            at thumbzoom
    else:
        imagebutton: #UNKNOWN
            idle "gui/gallery/locked.png"
            xalign 0.65
            yalign 0.35
            at thumbzoom

    # if hikari_first_strip: #
    #     imagebutton:
    #         auto "gui/gallery/hikari/first_strip_%s.jpg"
    #         action Replay("g_amy_coffee_event1", locked=False)
    #         xalign 0.95
    #         yalign 0.35
    #         at thumbzoom
    # else:
    #     imagebutton: #UNKNOWN
    #         idle "gui/gallery/locked.png"
    #         xalign 0.95
    #         yalign 0.35
    #         at thumbzoom

screen jenna_gallery1:
    tag gallery

    if jenna_event1: #Shower Prank
        imagebutton:
            auto "gui/gallery/jenna/jenna_shower_%s.jpg"
            action Replay("g_jenna_event1", locked=False)
            xalign 0.05
            yalign 0.35
            at thumbzoom
    else:
        imagebutton: #UNKNOWN
            idle "gui/gallery/locked.png"
            xalign 0.05
            yalign 0.35
            at thumbzoom


    if jenna_mma1: #MMA
        imagebutton:
            auto "gui/gallery/jenna/mma_%s.jpg"
            action Replay("g_jenna_mma1", locked=False)
            xalign 0.35
            yalign 0.35
            at thumbzoom
    else:
        imagebutton: #UNKNOWN
            idle "gui/gallery/locked.png"
            xalign 0.35
            yalign 0.35
            at thumbzoom

    if jenna_spank1: #Spank
        imagebutton:
            auto "gui/gallery/jenna/spank_%s.jpg"
            action Replay("g_jenna_spank1", locked=False)
            xalign 0.65
            yalign 0.35
            at thumbzoom
    else:
        imagebutton: #UNKNOWN
            idle "gui/gallery/locked.png"
            xalign 0.65
            yalign 0.35
            at thumbzoom

    if jenna_teabag: #Teabag
        imagebutton:
            auto "gui/gallery/jenna/teabag_%s.jpg"
            action Replay("g_jenna_teabag", locked=False)
            xalign 0.95
            yalign 0.35
            at thumbzoom
    else:
        imagebutton: #UNKNOWN
            idle "gui/gallery/locked.png"
            xalign 0.95
            yalign 0.35
            at thumbzoom

screen maria_gallery1:
    tag gallery

    if hikari_maria1: #Hikari Wingman
        imagebutton:
            auto "gui/gallery/maria/wingman_hikari_%s.jpg"
            action Replay("g_maria_hikari1", locked=False)
            xalign 0.05
            yalign 0.35
            at thumbzoom
    else:
        imagebutton: #UNKNOWN
            idle "gui/gallery/locked.png"
            xalign 0.05
            yalign 0.35
            at thumbzoom

screen mayan_gallery1:
    tag gallery

screen sophie_gallery1:
    tag gallery

    if sophie_drunk: # Sophie Drunk
        imagebutton:
            auto "gui/gallery/sophie/sophie_drunk_%s.jpg"
            action Replay("g_sophie_drunk", locked=False)
            xalign 0.05
            yalign 0.35
            at thumbzoom
    else:
        imagebutton: #UNKNOWN
            idle "gui/gallery/locked.png"
            xalign 0.05
            yalign 0.35
            at thumbzoom

    # if nude_locker_hikari:
    #     imagebutton:
    #         auto "gui/gallery/sophie/first_nude_%s.jpg"
    #         action Replay("g_hikari_nude_locker", locked=False)
    #         xalign 0.35
    #         yalign 0.35
    #         at thumbzoom
    # else:
    #     imagebutton: #UNKNOWN
    #         idle "gui/gallery/locked.png"
    #         xalign 0.35
    #         yalign 0.35
    #         at thumbzoom
