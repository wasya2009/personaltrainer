### SOPHIE APARTMENT
label loc_sophie:
    show screen ui_icons
    show screen ui_text
    if 6 <= float(minn/60)%24 < 11: ### LIVINGROOM DUSK
        scene sophie_livingroom_dusk
        if not (((days%7) == 6) or ((days%7) == 0)) and 8 <= float(minn/60)%24 < 9: # Sophie Work
            call sophie_work from _call_sophie_work

    elif 11 <= float(minn/60)%24 < 19: ### LIVINGROOM
        scene sophie_livingroom
        if (((days%7) == 6) or ((days%7) == 0)) and 16 <= float(minn/60)%24 < 18: # Sophie PS4 Weekend
            if sophie_hungover:
                scene sophie_nude_ps41
            else:
                scene sophie_ps41
            call screen sophie_ps4_button
        elif not (((days%7) == 6) or ((days%7) == 0)) and 17 <= float(minn/60)%24 < 18 and sophie_date1 and not sophie_park1: # Sophie Park Event1
            jump sophie_park_event1
        elif not (((days%7) == 6) or ((days%7) == 0)) and 17 <= float(minn/60)%24 < 18 and sophie_park1 and not sophie_arcade1: # Sophie Arcade Event1
            jump sophie_arcade_event1
        elif not (((days%7) == 6) or ((days%7) == 0)) and 17 <= float(minn/60)%24 < 18 and amy_sex1 and not sophie_breakup: # Sophie Breakup
            jump sophie_breakup
        elif not (((days%7) == 6) or ((days%7) == 0)) and 17 <= float(minn/60)%24 < 18: # Sophie Home
                jump sophie_work_home

    elif 19 <= float(minn/60)%24 < 22: ### LIVINGROOM NIGHT LIGHTS
        scene sophie_livingroom_night_lights
        if not (((days%7) == 6) or ((days%7) == 0)) and 19 <= float(minn/60)%24 < 20: # Sophie PS4 Weekday
            if sophie_hungover:
                scene sophie_nude_ps41
            else:
                scene sophie_ps41
            call screen sophie_ps4_button
        elif ((days%7) != 5) and 21 <= float(minn/60)%24 < 22: # Sophie TV
            if sophie_hungover:
                scene sophie_nude_tv1
            else:
                scene sophie_tv1
            call screen sophie_tv_button

    elif (22 <= float(minn/60)%24) or (float(minn/60)%24 <= 5) : ### LIVINGROOM NIGHT
        if ((days%7) == 5) and (22 <= float(minn/60)%24 < 24) and lick_amy and not sophie_date1: # Friday Date
            jump sophie_date_event1
        if (0 >= float(minn/60)%24) and sophie_breakup and not sophie_drunk or (float(minn/60)%24 <= 5) and sophie_breakup and not sophie_drunk: # Sophie Drunk
            jump sophie_drunk
        else:
            scene sophie_livingroom_night

    call screen loc_sophie_nav

label loc_sophie_kitchen:
    show screen ui_icons
    show screen ui_text
    if 6 <= float(minn/60)%24 < 11: ### KITCHEN DUSK
        scene sophie_kitchen_dusk
        if 7 <= float(minn/60)%24 < 8 and sophie_arcade1 and amy_sad_event1 and not amy_sex1: # Amy & Sophie Date Event
            jump amy_sophie_date1
        if 7 <= float(minn/60)%24 < 8 and sophie_drunk and not sophie_hungover: # Sophie Hangover Breakfast Event
            jump sophie_hangover
        elif not (((days%7) == 6) or ((days%7) == 0)) and 7 <= float(minn/60)%24 < 8: # Breakfast Weekday
            if sophie_hungover:
                scene cooking_nude_breakfast1
            else:
                scene cooking_breakfast1
            call screen sophie_breakfast_button
        elif (((days%7) == 6) or ((days%7) == 0)) and 8 <= float(minn/60)%24 < 9: # Breakfast Weekend
            if sophie_hungover:
                scene cooking_nude_breakfast1
            else:
                scene cooking_breakfast1
            call screen sophie_breakfast_button

    elif 11 <= float(minn/60)%24 < 19: ### KITCHEN
        scene sophie_kitchen

    elif 19 <= float(minn/60)%24 < 22: ### KITCHEN NIGHT LIGHTS
        scene sophie_kitchen_night_lights
        if not (((days%7) == 6) or ((days%7) == 0)) and 20 <= float(minn/60)%24 < 21: # Sophie Towel Snack
            if sophie_hungover:
                scene sophie_nude_towel_snack1
            else:
                scene sophie_towel_snack1
            call screen sophie_snack_button

    elif (22 <= float(minn/60)%24) or (float(minn/60)%24 <= 5) : ### KITCHEN NIGHT
        scene sophie_kitchen_night

    call screen loc_sophie_nav

label loc_sophie_bedroom:
    show screen ui_icons
    show screen ui_text
    scene sophie_bedroom
    if 0 <= float(minn/60)%24 <= 6: # Sophie Sleeping
        jump sophie_sleeping
    elif (((days%7) == 6) or ((days%7) == 0)) and 7 <= float(minn/60)%24 < 8: # Sophie Yoga
        if sophie_hungover:
            scene sophie_nude_home_yoga1
        else:
            scene sophie_home_yoga1
        call screen sophie_yoga_button
    elif 18 <= float(minn/60)%24 < 19: # Sophie Changing
        jump sophie_changing
    elif 22 <= float(minn/60)%24: # Sophie Laptop
        if sophie_hungover:
            scene sophie_nude_home_laptop1
        else:
            scene sophie_home_laptop1
        call screen sophie_laptop_button
        jump sophie_laptop

    call screen loc_sophie_nav

label loc_sophie_bathroom:
    show screen ui_icons
    show screen ui_text
    scene sophie_bathroom
    if 19 <= float(minn/60)%24 < 20:
        jump sophie_bath
    call screen loc_sophie_nav


### GYM LOCATIONS
label loc_gym:
    show screen ui_icons
    show screen ui_text
    hide screen map
    if 6 <= float(minn/60)%24 < 24:
        if gym_intro:
            jump gym_first_time
        elif not Mjenna and lick_amy: # Jenna Intro Event
            jump jenna_intro
        elif hikari_maria1 and not fired: # MC Fired Event
            jump dani_fired
        elif 6 <= float(minn/60)%24 < 24 and amy_sex1 and not amy_plan: # Amy Revenge Plan Event
            jump amy_plan
        elif 19 <= float(minn/60)%24 < 24 and jenna_shower_revenge1 and not jenna_mma1: # Jenna MMA Fight Event
            jump jenna_mma1
        elif 6 <= float(minn/60)%24 < 7: # Saggy Tits Latina Reception
            scene daisy_reception_saggylatina
            call screen loc_gym_nav
        elif 7 <= float(minn/60)%24 < 8: # Blonde Sport Reception
            scene daisy_reception_blondesport
            call screen loc_gym_nav
        elif 9 <= float(minn/60)%24 < 10: # Black Blue Eyed Reception
            scene daisy_reception_blackblue
            $ renpy.pause()
        elif 12 <= float(minn/60)%24 < 13: # Fattie Reception
            scene daisy_reception_fattie
            $ renpy.pause()
        else:
            scene gym_reception
            call screen daisy_reception_button
    else:
        jump gym_closed

label loc_gym_gym:
    show screen ui_icons
    show screen ui_text
    scene gym_gym
    if 6 <= float(minn/60)%24 < 24:
        if 8 <= float(minn/60)%24 <= 10 and nude_swim_hikari and sex_maria and not hikari_maria1: # Maria & Hikari nude pool EVENT
            jump maria_hikari1
        elif 8 <= float(minn/60)%24 < 10: # Maria Treadmill
            call screen maria_treadmill_button
        elif 11 <= float(minn/60)%24 < 13: # Amy Stretch
            call screen amy_gym_button
        elif 14 <= float(minn/60)%24 < 16 and jenna_mma1 and not jenna_postmma:
            jump jenna_postmma # Jenna Post MMA EVENT
        elif 14 <= float(minn/60)%24 < 15 and Mjenna and not jenna_bench_event1: # Jenna Bench EVENT
            jump jenna_bench_event1
        elif 14 <= float(minn/60)%24 < 16 and jenna_spank1 and not jenna_teabag: # Jenna Teabag EVENT
            jump jenna_teabag
        elif 14 <= float(minn/60)%24 < 15 : # Fattie Treadmill
            scene fattie_treadmill1
            call screen fattie_treadmill_button
        elif 14 <= float(minn/60)%24 < 16 and Mjenna: # Jenna Benching
            call screen jenna_bench_button
        call screen loc_gym_nav
    else:
        jump gym_closed

label loc_gym_yoga:
    show screen ui_icons
    show screen ui_text
    if 11 <= float(minn/60)%24 < 12: # 2 Girls Yoga
        scene yoga_2girls1
        call screen yoga_2girls_button
    if 13 <= float(minn/60)%24 < 15 and Mmaria and not maria_yoga1:
        jump maria_yoga1
    elif 15 <= float(minn/60)%24 < 17 and amy_yoga_topless and amy_yoga_topless2 and not amy_titjob1:
        jump amy_daisy_yoga1
    elif 15 <= float(minn/60)%24 < 17 and amy_bj1:
        jump amy_yoga
    elif 6 <= float(minn/60)%24 < 24:
        scene gym_yoga
        call screen loc_gym_nav
    else:
        jump gym_closed

label loc_gym_sauna:
    show screen ui_icons
    show screen ui_text
    if 6 <= float(minn/60)%24 < 24:
        scene gym_sauna
        if 9 <= float(minn/60)%24 < 10: # Saggy Tits Latina
            scene saggy_tits_latina_sauna1
            call screen saggy_tits_latina_sauna_button
        elif 11 <= float(minn/60)%24 < 13:
            call screen maria_sauna_button
        elif 15 <= float(minn/60)%24 < 17 and Mamy and not amy_sauna1:
            jump amy_sauna1
        call screen loc_gym_nav
    else:
        jump gym_closed

label loc_gym_pool:
    show screen ui_icons
    show screen ui_text
    if 6 <= float(minn/60)%24 < 24:
        if 13 <= float(minn/60)%24 < 14 and amy_titjob1 and not amy_sad_event1: # Amy Sad Event
            jump amy_sad_event1
        elif 15 <= float(minn/60)%24 < 16: # Fattie Swimming
            scene fattie_swimming1
            call screen fattie_swimming_button
        elif 17 <= float(minn/60)%24 < 18 and hikari_new_look: # Hikari New Look Nude Pool Sit
            scene hikari_new_pool_sit1
            call screen hikari_new_look_pool_sit_button
        elif 17 <= float(minn/60)%24 < 18 and nude_swim_hikari and not hikari_new_look: # Hikari Nude Pool Sit
            scene hikari_pool_nude_sit
            call screen hikari_nude_pool_sit_button
        elif 17 <= float(minn/60)%24 < 18: # Hikari Pool Sit
            scene gym_pool
            call screen hikari_pool_button
        elif 18 <= float(minn/60)%24 < 20: # Hikari Nude Swim
            if nude_swim_hikari and hikari_maria1 and not hikari_strip_intro:
                jump hikari_stripclub1 # Strip Club Intro
            elif nude_swim_hikari:
                scene gym_pool
                call screen hikari_swim_nude_button
            else:
                scene gym_pool
                call screen hikari_swim_button
        else:
            scene gym_pool
        call screen loc_gym_nav
    else:
        jump gym_closed

label loc_gym_locker:
    show screen ui_icons
    show screen ui_text
    if 6 <= float(minn/60)%24 < 24:
        if 7 <= float(minn/60)%24 < 8: # Monica Rubbing
                    scene monica_locker_rub1
                    call screen monica_rubbing_button
        elif 8 <= float(minn/60)%24 < 9: # Fattie Attack
            scene fattie_locker_attack1
            call screen fattie_attack_button
        elif 10 <= float(minn/60)%24 < 11: # Black Blue Eyed  Changing
                scene black_girl_changing1
                call screen black_girl_changing_button
        elif 11 <= float(minn/60)%24 < 15 and jenna_postmma and not jenna_spank1: # Jenna Spank EVENT
                jump jenna_spank1
        elif 12 <= float(minn/60)%24 < 13 and jenna_event1 and not jenna_shower_revenge1: # Jenna Shower Revenge EVENT
            jump jenna_shower_revenge1
        elif 12 <= float(minn/60)%24 < 13 and jenna_shower_revenge1: # Blonde Masturbating
            scene blonde_rubbing_locker1
            call screen blonde_locker_masturbating_button
        elif 14 <= float(minn/60)%24 < 15 and amy_event and amy_plan and not amy_recon: # Amy Recon Event
            jump amy_recon
        elif 14 <= float(minn/60)%24 < 15: # Amy Changing
            scene gym_locker2
            call screen amy_locker_button
        elif 15 <= float(minn/60)%24 < 16: # Maria Shower
            scene gym_locker
            call screen maria_shower_button
        elif 16 <= float(minn/60)%24 < 17 and jenna_teabag and not jenna_bj: # Jenna BJ
            jump jenna_bj
        elif 16 <= float(minn/60)%24 < 17 and jenna_bench_event1 and not jenna_event1: # Jenna Shower Prank EVENT
            jump jenna_event1
        elif 16 <= float(minn/60)%24 < 17: # Jenna Shower
            scene jenna_shower
            call screen jenna_shower_button
        elif 20 <= float(minn/60)%24 < 21 and hikari_bartender_help and not hikari_new_look: # Hikari New Stripper Look
            jump hikari_new_look
        elif 20 <= float(minn/60)%24 < 21 and hikari_new_look: # Hikari New Look
            scene hikari_new_nude_locker1
        elif 20 <= float(minn/60)%24 < 21: # Hikari Changing
            scene gym_locker2
            if Mhikari and nude_locker_hikari:
                call screen hikari_nudelocker_button
            else:
                call screen hikari_locker_button
        else:
            scene gym_locker
        call screen loc_gym_nav
    else:
        jump gym_closed

label loc_gym_office:
    show screen ui_icons
    show screen ui_text
    if 6 <= float(minn/60)%24 < 24:
        scene gym_office
        if fired and not dani_cable:
            jump dani_cable
        elif dani_cable and not dani_singing:
            jump dani_singing
        else:
            call screen dani_office_button
    else:
        jump gym_closed
    call screen loc_gym_nav
# label
### COFFEE SHOP
label loc_coffee:
        show screen ui_icons
        show screen ui_text
        hide screen map
        scene coffee
        if 8 <= float(minn/60)%24 < 20:
            if not Mmayan:
                jump mayan_intro
            elif 8 <= float(minn/60)%24 < 9:
                scene mayan_ruclark1
                call screen mayan_ruclark1_button
            elif (17 <= float(minn/60)%24 < 19) and lick_amy and not amy_bj1:
                jump amy_coffee_event1
            else:
                call screen mayan_coffee_button
        else:
            jump coffee_closed

# HOTBUTTONS
screen mayan_coffee_button:
    $ modal = False
    use loc_coffee_nav
    default tt = Tooltip("")
    imagebutton:
        xpos 0
        ypos 0
        focus_mask True
        auto "hotbutton/mayan_coffee_%s.png" hovered tt.Action(_("Mayan"))
        clicked [Hide("ui_icons"), Hide("ui_text"), Jump("mayan_coffee")]

### ARCADE
label loc_arcade:
    show screen ui_icons
    show screen ui_text
    hide screen map
    scene arcade
    if 8 <= float(minn/60)%24 < 24:
        if 8 <= float(minn/60)%24 < 9:
            scene arcade_guy_bored_girl1
            call screen bored_gf_button
        elif 16 <= float(minn/60)%24 < 17:
            scene arcade_schoolgirl_hockey_1
            call screen high_school_sluts_button
        else:
            scene arcade
            $ renpy.pause ()
    else:
        jump arcade_closed

label arcade_closed:
    scene arcade
    "The arcade is open from 08:00 - 24:00"
    jump map_label

### STRIP CLUB
label loc_stripclub:
    show screen ui_icons
    show screen ui_text
    hide screen map
    scene strip_club
    if (0 <= float(minn/60)%24 <= 3) or (21 <= float(minn/60)%24):
        if hikari_strip_intro and not hikari_bartender_help:
            jump hikari_bartender_help
        elif ((days%7) == 3) and hikari_new_look and not hikari_first_strip: # Hikari First Strip Event
            jump hikari_first_strip
        elif (days%7) == 3 and 21 <= float(minn/60)%24 and hikari_first_strip: # Hikari Stripping
            scene strip_club_hikari
            call screen hikari_strip_club_button
        elif (days%7) == 4 and 0 < float(minn/60)%24 <= 3 and hikari_first_strip: # Hikari Stripping
            scene strip_club_hikari
            call screen hikari_strip_club_button
        elif (21 <= float(minn/60)%24):
            scene stripper_ginger1
            call screen stripper_ginger_button
        elif (0 <= float(minn/60)%24 <= 3):
            scene stripper_brunette
            call screen stripper_brunette_button
        else:
            scene strip_club
            call screen bartender_button
    else:
        jump strip_club_closed
# stripper_ginger
label strip_club_closed:
    scene black
    "The strip club is open from 21:00 - 03:00"
    jump map_label

### AMY'S PLACE
label loc_amy:
    if (19 <= float(minn/60)%24) and ((days%7) == 5) and amy_recon and not amy_cuck: # Amy Dinner Cuck Event
        jump amy_dinner
    # elif (0 <= float(minn/60)%24 <= 3) or (21 <= float(minn/60)%24):
    #     # placeholder
    #     jump loc_sophie
    else:
        scene amy_house_closed
        "(Content under development)"
        jump loc_sophie
