### SOPHIE APARTMENT
# HOTBUTTONS
screen sophie_breakfast_button:
    $ modal = False
    use loc_sophie_nav
    default tt = Tooltip("")
    imagebutton:
        xalign 0.52
        yalign 0.25
        focus_mask True
        auto "gui/icons/point_of_interest_%s.png" hovered tt.Action("Talk to Sophie")
        clicked [Hide("ui_icons"), Hide("ui_text"), Hide("loc_sophie_nav"), Jump("sophie_breakfast")]

screen sophie_yoga_button:
    $ modal = False
    use loc_sophie_nav
    default tt = Tooltip("")
    imagebutton:
        xalign 0.61
        yalign 0.18
        focus_mask True
        auto "gui/icons/point_of_interest_%s.png" hovered tt.Action("Watch")
        clicked [Hide("ui_icons"), Hide("ui_text"), Hide("loc_sophie_nav"), Jump("sophie_yoga")]

screen sophie_tv_button:
    $ modal = False
    use loc_sophie_nav
    default tt = Tooltip("")
    imagebutton:
        xalign 0.65
        yalign 0.45
        focus_mask True
        auto "gui/icons/point_of_interest_%s.png" hovered tt.Action("Talk to Sophie")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("sophie_tv")]

screen sophie_ps4_button:
    $ modal = False
    use loc_sophie_nav
    default tt = Tooltip("")
    imagebutton:
        xalign 0.655
        yalign 0.31
        focus_mask True
        auto "gui/icons/point_of_interest_%s.png" hovered tt.Action("Talk to Sophie")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("sophie_ps4")]

screen sophie_snack_button:
    $ modal = False
    use loc_sophie_nav
    default tt = Tooltip("")
    imagebutton:
        xalign 0.475
        yalign 0.2
        focus_mask True
        auto "gui/icons/point_of_interest_%s.png" hovered tt.Action("Talk to Sophie")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("sophie_snack")]

screen sophie_laptop_button:
    $ modal = False
    use loc_sophie_nav
    default tt = Tooltip("")
    imagebutton:
        xalign 0.633
        yalign 0.46
        focus_mask True
        auto "gui/icons/point_of_interest_%s.png" hovered tt.Action("Talk to Sophie")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("sophie_laptop")]

### GYM
# HOTBUTTONS
# AMY
screen amy_gym_button:
    $ modal = False
    use loc_gym_nav
    default tt = Tooltip("")
    imagebutton:
        xalign 0.525
        yalign 0.3
        focus_mask True
        auto "hotbutton/amy_gymgym_%s.png" hovered tt.Action("Amy") #action NullAction()
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("amy_gym_stretch")]

screen amy_locker_button:
    $ modal = False
    use loc_gym_nav
    default tt = Tooltip("")
    imagebutton:
        xalign 0.525
        yalign 0.3
        focus_mask True
        auto "hotbutton/amy_locker_%s.png" hovered tt.Action("Amy") #action NullAction()
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("amy_gym_locker")]

# DANI
screen dani_office_button:
    $ modal = False
    use loc_gym_nav
    default tt = Tooltip("")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        auto "hotbutton/dani_office_%s.png" hovered tt.Action("Dani")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("dani_office")]
# DAISY
screen daisy_reception_button:
    $ modal = False
    use loc_gym_nav
    default tt = Tooltip("")
    imagebutton:
        xalign 0.525
        yalign 0.3
        focus_mask True
        auto "hotbutton/daisy_reception_%s.png" hovered tt.Action("Daisy") #action NullAction()
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("daisy_reception")]
# HIKARI
screen hikari_pool_button:
    $ modal = False
    use loc_gym_nav
    default tt = Tooltip("")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        auto "hotbutton/gym_pool_hikari_%s.png" hovered tt.Action("Hikari")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("hakari_pool")]
screen hikari_nude_pool_sit_button:
    $ modal = False
    use loc_gym_nav
    default tt = Tooltip("")
    imagebutton:
        xalign 0.355
        yalign 0.39
        focus_mask True
        auto "gui/icons/point_of_interest_%s.png" hovered tt.Action("Talk to Hikari")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("hikari_nude_pool_sit")]
screen hikari_new_look_pool_sit_button:
    $ modal = False
    use loc_gym_nav
    default tt = Tooltip("")
    imagebutton:
        xalign 0.36
        yalign 0.36
        focus_mask True
        auto "gui/icons/point_of_interest_%s.png" hovered tt.Action("Talk to Hikari")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("hikari_new_look_pool_sit")]

screen hikari_swim_button:
    $ modal = False
    use loc_gym_nav
    default tt = Tooltip("")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        auto "hotbutton/gym_swim_hikari_%s.png" hovered tt.Action("Hikari")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("hikari_pool_swim")]
screen hikari_swim_nude_button:
            $ modal = False
            use loc_gym_nav
            default tt = Tooltip("")
            imagebutton:
                xpos 0
                ypos 0
                focus_mask True
                auto "hotbutton/hikari_swim_nude_%s.png" hovered tt.Action("Hikari")
                clicked [Hide("ui_icons"), Hide("ui_text"), Jump("hikari_pool_swim")]
screen hikari_locker_button:
    $ modal = False
    use loc_gym_nav
    default tt = Tooltip("")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        auto "hotbutton/hikari_locker_%s.png" hovered tt.Action("Hikari")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("hikari_locker")]
screen hikari_nudelocker_button:
    $ modal = False
    use loc_gym_nav
    default tt = Tooltip("")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        auto "hotbutton/hikari_locker_nude_%s.png" hovered tt.Action("Hikari")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("hikari_locker")]
screen hikari_strip_club_button:
    $ modal = False
    use bartender_button
    default tt = Tooltip("")
    imagebutton:
        xalign 0.595
        yalign 0.22
        focus_mask True
        auto "gui/icons/point_of_interest_%s.png" hovered tt.Action("Watch")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("hikari_strip1")]

# JENNA
screen jenna_bench_button:
    $ modal = False
    use loc_gym_nav
    default tt = Tooltip("")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        auto "hotbutton/jenna_bench_%s.png" hovered tt.Action("Jenna")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("jenna_bench")]
screen jenna_shower_button:
    $ modal = False
    use loc_gym_nav
    default tt = Tooltip("")
    imagebutton:
        xalign 0.355
        yalign 0.08
        focus_mask True
        auto "gui/icons/point_of_interest_%s.png" hovered tt.Action("Look at Jenna")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("jenna_shower")]

# MARIA
screen maria_shower_button:
    $ modal = False
    use loc_gym_nav
    default tt = Tooltip("")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        auto "hotbutton/maria_locker_shower_%s.png" hovered tt.Action("Maria") #action NullAction()
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("maria_shower")]
screen maria_treadmill_button:
    $ modal = False
    use loc_gym_nav
    default tt = Tooltip("")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        auto "hotbutton/maria_treadmill_%s.png" hovered tt.Action("Maria")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("maria_treadmill")]
screen maria_sauna_button:
    $ modal = False
    use loc_gym_nav
    default tt = Tooltip("")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        auto "hotbutton/maria_sauna_%s.png" hovered tt.Action("Maria") #action NullAction()
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("maria_sauna1")]

### STRIP CLUB
screen bartender_button:
    $ modal = False
    use loc_strip_nav
    default tt = Tooltip("")
    imagebutton:
        xalign 0.25
        yalign 0.25
        focus_mask True
        auto "gui/icons/point_of_interest_%s.png" hovered tt.Action("Talk") #action NullAction()
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("bartender")]
