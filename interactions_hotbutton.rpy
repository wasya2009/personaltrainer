### GYM
# Main Floor
screen fattie_treadmill_button:
    $ modal = False
    use loc_gym_nav
    default tt = Tooltip("")
    imagebutton:
        xalign 0.83
        yalign 0.42
        focus_mask True
        auto "gui/icons/point_of_interest_%s.png" hovered tt.Action("Look")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("fattie_treadmill")]

# Locker Room
screen black_girl_changing_button:
    $ modal = False
    use loc_gym_nav
    default tt = Tooltip("")
    imagebutton:
        xalign 0.85
        yalign 0.2
        focus_mask True
        auto "gui/icons/point_of_interest_%s.png" hovered tt.Action("Look")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("black_girl_changing")]

screen fattie_attack_button:
    $ modal = False
    use loc_gym_nav
    default tt = Tooltip("")
    imagebutton:
        xalign 0.535
        yalign 0.13
        focus_mask True
        auto "gui/icons/point_of_interest_%s.png" hovered tt.Action("Look")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("fattie_attack")]


screen blonde_locker_masturbating_button:
    $ modal = False
    use loc_gym_nav
    default tt = Tooltip("")
    imagebutton:
        xalign 0.62
        yalign 0.28
        focus_mask True
        auto "gui/icons/point_of_interest_%s.png" hovered tt.Action("Look")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("blonde_locker_masturbating")]

screen monica_rubbing_button:
    $ modal = False
    use loc_gym_nav
    default tt = Tooltip("")
    imagebutton:
        xalign 0.41
        yalign 0.34
        focus_mask True
        auto "gui/icons/point_of_interest_%s.png" hovered tt.Action("Look")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("monica_rubbing")]

# Pool
screen fattie_swimming_button:
    $ modal = False
    use loc_gym_nav
    default tt = Tooltip("")
    imagebutton:
        xalign 0.82
        yalign 0.55
        focus_mask True
        auto "gui/icons/point_of_interest_%s.png" hovered tt.Action("Look")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("fattie_swimming")]

# Sauna
screen saggy_tits_latina_sauna_button:
    $ modal = False
    use loc_gym_nav
    default tt = Tooltip("")
    imagebutton:
        xalign 0.35
        yalign 0.23
        focus_mask True
        auto "gui/icons/point_of_interest_%s.png" hovered tt.Action("Talk to her")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("saggy_tits_latina_sauna")]

# Yoga
screen yoga_2girls_button:
    $ modal = False
    use loc_gym_nav
    default tt = Tooltip("")
    imagebutton:
        xalign 0.47
        yalign 0.6
        focus_mask True
        auto "gui/icons/point_of_interest_%s.png" hovered tt.Action("Look")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("yoga_2girls")]

### ARCADE
screen bored_gf_button:
    $ modal = False
    use loc_arcade_nav
    default tt = Tooltip("")
    imagebutton:
        xalign 0.64
        yalign 0.5
        focus_mask True
        auto "gui/icons/point_of_interest_%s.png" hovered tt.Action("Eavesdrop")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("bored_gf")]

screen high_school_sluts_button:
    $ modal = False
    use loc_arcade_nav
    default tt = Tooltip("")
    imagebutton:
        xalign 0.36
        yalign 0.55
        focus_mask True
        auto "gui/icons/point_of_interest_%s.png" hovered tt.Action("Look")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("high_school_sluts")]

### Coffee
screen mayan_ruclark1_button:
    $ modal = False
    use loc_coffee_nav
    default tt = Tooltip("")
    imagebutton:
        xalign 0.48
        yalign 0.38
        focus_mask True
        auto "gui/icons/point_of_interest_%s.png" hovered tt.Action("Approach")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("mayan_ruclark1")]

### Strip Club
screen stripper_ginger_button:
    $ modal = False
    use loc_strip_nav
    default tt = Tooltip("")
    imagebutton:
        xalign 0.64
        yalign 0.28
        focus_mask True
        auto "gui/icons/point_of_interest_%s.png" hovered tt.Action("Watch")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("stripper_ginger")]

screen stripper_brunette_button:
    $ modal = False
    use loc_strip_nav
    default tt = Tooltip("")
    imagebutton:
        xalign 0.61
        yalign 0.28
        focus_mask True
        auto "gui/icons/point_of_interest_%s.png" hovered tt.Action("Watch")
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("stripper_brunette")]
