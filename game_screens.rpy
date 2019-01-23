image map = "locations/map.jpg"

# screen close_window:
#     zorder 101
#     imagebutton: # Closes windows if clicked outside window
#         xalign 1
#         yalign 0
#         focus_mask True
#         idle "gui/trans_close.png"
#         clicked [Hide("close_window"), Hide("char_stats"), Hide("relationships")]

screen ui_text:
    zorder 101
    text which_day() size 36 color "#ffffff" font "IndieFlower-Regular.ttf" xpos 31 ypos 27
    text hour() size 32 color "#ffffff" font "IndieFlower-Regular.ttf" xpos 126 ypos 32
    text '+ 1H' size 16 color "#ffffff" font "Roboto-Bold.ttf" xpos 115 ypos 9
    text '+ 6H' size 16 color "#ffffff" font "Roboto-Bold.ttf" xpos 180 ypos 9
    text 'zzZ' size 16 color "#ffffff" font "Roboto-Bold.ttf" xpos 250 ypos 9

screen ui_icons:
    zorder 100
    default tt = Tooltip("")
    vbox:
        xalign .99
        ypos 100
        frame:
            style "frame_gui1"
            text tt.value size 32 font "Roboto-Regular.ttf" color '#ffffff' outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
            background None #"#4b8ab8"

    imagebutton: # Day
        xpos 0
        ypos 5
        focus_mask True
        auto "gui/icons/day_icon_%s.png" action NullAction()

    imagebutton: # Time
        xpos 110
        ypos 26
        focus_mask True
        auto "gui/icons/display_text2_%s.png" action NullAction()

    imagebutton: #+ 1 hour
        xpos 75
        ypos -30
        focus_mask True
        auto "gui/icons/hour_icon_%s.png" hovered tt.Action("+ 1 hour") action [Function(pass_time, 60), Call(last_label)]

    imagebutton: #+ 6 hours
        xpos 140
        ypos -30
        focus_mask True
        auto "gui/icons/hour_icon_%s.png" hovered tt.Action("+ 6 hours") action [Function(pass_time, 360), Call(last_label)]

    imagebutton: # Sleep
        xpos 205
        ypos -30
        focus_mask True
        auto "gui/icons/hour_icon_%s.png" hovered tt.Action("Go to Sleep") action [Jump('sleep')]

    imagebutton: #Patreon
        xpos 1830
        ypos 1000
        focus_mask True
        auto "gui/icons/patreon_icon_%s.png" hovered tt.Action("Follow Domiek")
        clicked [OpenURL("https://www.patreon.com/domiek")]

    imagebutton: #Map
        xpos 1800
        ypos 5
        focus_mask True
        auto "gui/icons/map_%s.png" hovered tt.Action("Map")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("map_label")]

    imagebutton: #Phone
        xpos 1700
        ypos 5
        focus_mask True
        auto "gui/icons/phone_%s.png" hovered tt.Action("Memories Gallery")
        clicked [Hide("ui_icons"), Hide("ui_text")]#, Show("gallery_screen")]
        action ui.callsinnewcontext ("gallery_label")
    imagebutton: #Hints
        xpos 1600
        ypos 5
        focus_mask True
        auto "gui/icons/relations_%s.png" hovered tt.Action("Hints")
        action ui.callsinnewcontext ("guide_label")

label map_label:
    scene map
    call screen map

screen map:
    zorder 102
    default tt = Tooltip("")

    frame:
        background None
        xalign 0.5 ypos 20
        text tt.value size 32 color '#ffffff' outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]

    imagebutton: # Sophie
        xpos 1063
        ypos 351
        focus_mask True
        auto ("gui/map_icons/home_%s.png") hovered tt.Action("Sophie's Apartment")
        clicked [Show("ui_icons"), Show("ui_text"), Jump("loc_sophie")]
    if amy_recon:
        imagebutton: # Amy
            xpos 1400
            ypos 750
            focus_mask True
            auto ("gui/map_icons/amy_%s.png") hovered tt.Action("Amy's Place")
            clicked [Show("ui_icons"), Show("ui_text"), Jump("loc_amy")]
    imagebutton: # Gym
        xpos 1219
        ypos 534
        focus_mask True
        auto ("gui/map_icons/gym_%s.png") hovered tt.Action("Gym")
        clicked [Show("ui_icons"), Show("ui_text"), Jump("loc_gym")]
    imagebutton: # Coffee
        xpos 1105
        ypos 821
        focus_mask True
        auto ("gui/map_icons/coffee_%s.png") hovered tt.Action("Coffee Shop")
        clicked [Show("ui_icons"), Show("ui_text"), Jump("loc_coffee")]
    imagebutton: # Arcade
        xpos 1137
        ypos 307
        focus_mask True
        auto ("gui/map_icons/arcade_%s.png") hovered tt.Action("Arcade")
        clicked [Show("ui_icons"), Show("ui_text"), Jump("loc_arcade")]
    imagebutton: # Strip Club
        xpos 835
        ypos 643
        focus_mask True
        auto ("gui/map_icons/stripclub_%s.png") hovered tt.Action("Strip Club")
        clicked [Show("ui_icons"), Show("ui_text"), Jump("loc_stripclub")]

style frame_gui1:
    padding gui.frame_borders.padding

screen amy_timer():
    if (0 <= float(minn/60)%24 <= 7):
        timer 0.1 action [SetVariable("amy_event", True), Hide("amy_timer")]

screen dani_timer():
    if (0 <= float(minn/60)%24 <= 7):
        timer 0.1 action [SetVariable("dani_event", True), Hide("dani_timer")]

screen daisy_timer():
    if (0 <= float(minn/60)%24 <= 7):
        timer 0.1 action [SetVariable("daisy_event", True), Hide("daisy_timer")]

screen hikari_timer():
    if (0 <= float(minn/60)%24 <= 7):
        timer 0.1 action [SetVariable("hikari_event", True), Hide("hikari_timer")]

screen jenna_timer():
    if (0 <= float(minn/60)%24 <= 7):
        timer 0.1 action [SetVariable("jenna_event", True), Hide("jenna_timer")]

screen maria_timer():
    if (0 <= float(minn/60)%24 <= 7):
        timer 0.1 action [SetVariable("maria_event", True), Hide("maria_timer")]

screen mayan_timer():
    if (0 <= float(minn/60)%24 <= 7):
        timer 0.1 action [SetVariable("mayan_event", True), Hide("mayan_timer")]

screen sophie_timer():
    if (0 <= float(minn/60)%24 <= 7):
        timer 0.1 action [SetVariable("sophie_event", True), Hide("sophie_timer")]


### STORE SCREEN
screen store_items:
    default tt = Tooltip("")

    frame:
        background None
        # set this frame to the position of the mouse
        pos renpy.get_mouse_pos()

        # display text with value set in tt.Action() above.
        text tt.value size 16 color '#ffffff' outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]

    imagebutton auto "locations/store/gym_clothes_%s.jpg" xpos 365 ypos 136 focus_mask True hovered tt.Action("Gym Clothes") action Return ("gym_clothes")

### NAVIGATION
screen loc_sophie_nav:
    zorder 101
    tag navigation
    $ modal = False
    default tt = Tooltip("")

    frame:
        background None
        xalign 0.5 ypos 20
        text tt.value size 32 color '#ffffff' outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]

    imagebutton: #Living room
        xpos 0
        ypos 980
        focus_mask True
        auto "locations/sophie_apartment/livingroom_%s.png" hovered tt.Action("Living Room")
        clicked [Jump("loc_sophie")]

    imagebutton: #Kitchen
        xpos 100
        ypos 980
        focus_mask True
        auto "locations/sophie_apartment/kitchen_%s.png" hovered tt.Action("Kitchen")
        clicked [Jump("loc_sophie_kitchen")]

    imagebutton: #Bedroom
        xpos 200
        ypos 980
        focus_mask True
        auto "locations/sophie_apartment/bedroom_%s.png" hovered tt.Action("Bedroom")
        clicked [Jump("loc_sophie_bedroom")]

    imagebutton: #Bathroom
        xpos 300
        ypos 980
        focus_mask True
        auto "locations/sophie_apartment/bathroom_%s.png" hovered tt.Action("Bathroom")
        clicked [Jump("loc_sophie_bathroom")]

screen loc_gym_nav:
    tag navigation
    $ modal = False
    default tt = Tooltip("")

    frame:
        background None
        xalign 0.5 ypos 20
        text tt.value size 32 color '#ffffff' outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]


    imagemap:
        ground "locations/gym/loc_gym_idle.png"
        ypos -10
        hover "locations/gym/loc_gym_hover.png"

        hotspot (14, 1004, 103, 59) clicked Jump("loc_gym") hovered tt.Action("Lobby")
        hotspot (120, 1004, 103, 59) clicked Jump("loc_gym_gym") hovered tt.Action("Main Floor")
        hotspot (226, 1004, 103, 59) clicked Jump("loc_gym_yoga") hovered tt.Action("Yoga")
        hotspot (331, 1004, 103, 59) clicked Jump("loc_gym_sauna") hovered tt.Action("Sauna")
        hotspot (434, 1004, 103, 59) clicked Jump("loc_gym_pool") hovered tt.Action("Pool")
        hotspot (539, 1004, 103, 59) clicked Jump("loc_gym_locker") hovered tt.Action("Locker Room")
        hotspot (644, 1004, 103, 59) clicked Jump("loc_gym_office") hovered tt.Action("Office")

screen loc_arcade_nav:
    tag navigation
    $ modal = False
    default tt = Tooltip("")

    frame:
        background None
        xalign 0.5 ypos 20
        text tt.value size 32 color '#ffffff' outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]

screen loc_coffee_nav:
    tag navigation
    $ modal = False
    default tt = Tooltip("")

    frame:
        background None
        xalign 0.5 ypos 20
        text tt.value size 32 color '#ffffff' outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]

screen loc_strip_nav:
    tag navigation
    $ modal = False
    default tt = Tooltip("")

    frame:
        background None
        xalign 0.5 ypos 20
        text tt.value size 32 color '#ffffff' outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
