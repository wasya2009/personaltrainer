screen gallery_screen:
    tag menu
    add "gui/gallery/gallery_bg.png"
    $ modal = True

# LEFT SIDE
    imagebutton: #SOPHIE
        idle "gui/portrait/sophie_idle.png"
        hover "gui/portrait/sophie_hover.png"
        selected_idle "gui/portrait/sophie_hover.png"
        action Show("sophie_gallery1")
        xalign 0.01
        yalign 0.01
        at customzoom

    if not gym_intro: #DAISY
        imagebutton:
            idle "gui/portrait/daisy_idle.png"
            hover "gui/portrait/daisy_hover.png"
            selected_idle "gui/portrait/daisy_hover.png"
            action Show("daisy_gallery1")
            xalign 0.08
            yalign 0.01
            at customzoom
    else:
        imagebutton: #UNKNOWN
            idle "gui/portrait/unknown_portrait.png"
            hover "gui/portrait/unknown_portrait.png"
            xalign 0.08
            yalign 0.01
            at customzoom

    if not gym_intro: #DANI
        imagebutton:
            idle "gui/portrait/dani_idle.png"
            hover "gui/portrait/dani_hover.png"
            selected_idle "gui/portrait/dani_hover.png"
            action Show("dani_gallery1")
            xalign 0.15
            yalign 0.01
            at customzoom
    else:
        imagebutton: #UNKNOWN
            idle "gui/portrait/unknown_portrait.png"
            hover "gui/portrait/unknown_portrait.png"
            xalign 0.15
            yalign 0.01
            at customzoom

    if Mamy: #AMY
        imagebutton:
            idle "gui/portrait/amy_idle.png"
            hover "gui/portrait/amy_hover.png"
            selected_idle "gui/portrait/amy_hover.png"
            action Show("amy_gallery1")
            xalign 0.22
            yalign 0.01
            at customzoom
    else:
        imagebutton: #UNKNOWN
            idle "gui/portrait/unknown_portrait.png"
            hover "gui/portrait/unknown_portrait.png"
            xalign 0.22
            yalign 0.01
            at customzoom

    if Mmaria: #MARIA
        imagebutton:
            idle "gui/portrait/maria_idle.png"
            hover "gui/portrait/maria_hover.png"
            selected_idle "gui/portrait/maria_hover.png"
            action Show("maria_gallery1")
            xalign 0.29
            yalign 0.01
            at customzoom
    else:
        imagebutton: #UNKNOWN
            idle "gui/portrait/unknown_portrait.png"
            hover "gui/portrait/unknown_portrait.png"
            xalign 0.29
            yalign 0.01
            at customzoom

    if Mhikari: #HIKARI
        if hikari_new_look:
            imagebutton:
                idle "gui/portrait/new_hikari_idle.png"
                hover "gui/portrait/new_hikari_hover.png"
                selected_idle "gui/portrait/new_hikari_hover.png"
                action Show("hikari_gallery1")
                xalign 0.01
                yalign 0.15
                at customzoom
        else:
            imagebutton:
                idle "gui/portrait/hikari_idle.png"
                hover "gui/portrait/hikari_hover.png"
                selected_idle "gui/portrait/hikari_hover.png"
                action Show("hikari_gallery1")
                xalign 0.01
                yalign 0.15
                at customzoom
    else:
        imagebutton: #UNKNOWN
            idle "gui/portrait/unknown_portrait.png"
            hover "gui/portrait/unknown_portrait.png"
            xalign 0.01
            yalign 0.15
            at customzoom

    if Mmayan: #MAYAN
        imagebutton:
            idle "gui/portrait/mayan_idle.png"
            hover "gui/portrait/mayan_hover.png"
            selected_idle "gui/portrait/mayan_hover.png"
            action Show("mayan_gallery1")
            xalign 0.08
            yalign 0.15
            at customzoom
    else:
        imagebutton: #UNKNOWN
            idle "gui/portrait/unknown_portrait.png"
            hover "gui/portrait/unknown_portrait.png"
            xalign 0.08
            yalign 0.15
            at customzoom
    if Mjenna: #JENNA
        imagebutton:
            idle "gui/portrait/jenna_idle.png"
            hover "gui/portrait/jenna_hover.png"
            selected_idle "gui/portrait/jenna_hover.png"
            action Show("jenna_gallery1")
            xalign 0.15
            yalign 0.15
            at customzoom
    else:
        imagebutton: #UNKNOWN
            idle "gui/portrait/unknown_portrait.png"
            hover "gui/portrait/unknown_portrait.png"
            xalign 0.15
            yalign 0.15
            at customzoom

    # PLACEHOLDER PORTRAITS
    imagebutton: #UNKNOWN
        idle "gui/portrait/unknown_portrait.png"
        hover "gui/portrait/unknown_portrait.png"
        xalign 0.22
        yalign 0.15
        at customzoom

    imagebutton: #UNKNOWN
        idle "gui/portrait/unknown_portrait.png"
        hover "gui/portrait/unknown_portrait.png"
        xalign 0.29
        yalign 0.15
        at customzoom
# RIGHT SIDE
    imagebutton: #UNKNOWN
        idle "gui/portrait/unknown_portrait.png"
        hover "gui/portrait/unknown_portrait.png"
        xalign 0.71
        yalign 0.01
        at customzoom

    imagebutton: #UNKNOWN
        idle "gui/portrait/unknown_portrait.png"
        hover "gui/portrait/unknown_portrait.png"
        xalign 0.78
        yalign 0.01
        at customzoom

    imagebutton: #UNKNOWN
        idle "gui/portrait/unknown_portrait.png"
        hover "gui/portrait/unknown_portrait.png"
        xalign 0.85
        yalign 0.01
        at customzoom

    imagebutton: #UNKNOWN
        idle "gui/portrait/unknown_portrait.png"
        hover "gui/portrait/unknown_portrait.png"
        xalign 0.92
        yalign 0.01
        at customzoom

    imagebutton: #UNKNOWN
        idle "gui/portrait/unknown_portrait.png"
        hover "gui/portrait/unknown_portrait.png"
        xalign 0.99
        yalign 0.01
        at customzoom

    imagebutton: #UNKNOWN
        idle "gui/portrait/unknown_portrait.png"
        hover "gui/portrait/unknown_portrait.png"
        xalign 0.71
        yalign 0.15
        at customzoom

    imagebutton: #UNKNOWN
        idle "gui/portrait/unknown_portrait.png"
        hover "gui/portrait/unknown_portrait.png"
        xalign 0.78
        yalign 0.15
        at customzoom

    imagebutton: #UNKNOWN
        idle "gui/portrait/unknown_portrait.png"
        hover "gui/portrait/unknown_portrait.png"
        xalign 0.85
        yalign 0.15
        at customzoom

    imagebutton: #UNKNOWN
        idle "gui/portrait/unknown_portrait.png"
        hover "gui/portrait/unknown_portrait.png"
        xalign 0.92
        yalign 0.15
        at customzoom

    imagebutton: #UNKNOWN
        idle "gui/portrait/unknown_portrait.png"
        hover "gui/portrait/unknown_portrait.png"
        xalign 0.99
        yalign 0.15
        at customzoom







    frame: #Close Button
        background None
        xalign 0.5
        yalign 0.2
        textbutton "Close":
            action Return()
            text_size 30


label gallery_label:
    call screen gallery_screen
    return
