### GYM
label black_girl_changing:
    hide screen ui_icons
    hide screen ui_text
    scene black_girl_changing2
    woman "(... huh?)"
    scene black_girl_changing3
    woman "Are you peeping on me? Get out of here!"
    s "Sorry, I'll come back another time."
    $ pass_time(60)
    jump loc_gym

label blonde_locker_masturbating:
    hide screen ui_icons
    hide screen ui_text
    scene blonde_rubbing_locker1
    "Loud moans fill the air as [s] walks in."
    scene blonde_rubbing_locker2
    s "(What a shameless animal.)"
    scene blonde_rubbing_locker3
    s "Sorry, I didn't realize you were doing... that."
    s "I'll come back some other time."
    woman "NO!"
    woman "... almost there."
    woman "*Panting* I'm.. I."
    scene blonde_rubbing_locker4
    with hpunch
    woman "Ahhhhhh!"
    scene blonde_rubbing_locker3
    woman "th-thanks!"
    s "Uh... glad I could help?"
    $ pass_time(60)
    jump loc_gym_locker

label fattie_swimming:
    hide screen ui_icons
    hide screen ui_text
    scene fattie_swimming1
    s "(Either Hikari has really let herself go lately... or we've sponsored something from the local aquarium.)"
    scene fattie_swimming2
    s "(To think that this is only the tip of the iceberg.)"
    scene fattie_swimming3
    s "(Nope, I was wrong.)"
    s "(That's the Titanic and it's going down fast.)"
    $ pass_time(60)
    jump loc_gym_pool

label fattie_treadmill:
    hide screen ui_icons
    hide screen ui_text
    scene fattie_treadmill2
    s "(Got to hand it to her, she's a bit on the big side but has the confidence to rock that tiny outfit.)"
    s "(Or maybe that was the largest size the store offered?)"
    scene fattie_treadmill3
    menu:
        "Tell her that her shoes are untied?"
        "Yes":
            scene fattie_treadmill2
            s "Excuse me miss, I just wanted to let you know th-"
            woman "NOT NOW! *PANTING*"
            woman "I'M IN THE FUCKING ZONE!"
            s "But your shoes are-"
            woman "Fuck off already!"
            s "(Well fuck you too then.)"
            s "Have a nice day."
            scene fattie_treadmill4
            "As expected, the woman trips over a shoelace and starts tumbling over."
            scene fattie_treadmill5
            "The woman did her best Peter Griffin impersonation as she laid on the floor in pain."
            woman "Ahh.... *sucking in air rapidly* ... ahhhh."
            s "(We could have all avoided that seismic 7.2 event if you had just been a little nicer.)"


        "No":
            scene fattie_treadmill4
            "As expected, the woman trips over a shoelace and starts tumbling over."
            scene fattie_treadmill5
            "The woman did her best Peter Griffin impersonation as she laid on the floor in pain."
            woman "Ahh.... *sucking in air rapidly* ... ahhhh."
            s "(Maybe I should have said something.)"
    $ pass_time(60)
    jump loc_gym_gym

label fattie_attack:
    hide screen ui_icons
    hide screen ui_text
    scene fattie_locker_attack2
    woman "Hey, I’ve seen you around here. You perform services for the girls, right?"
    s "Umm… not exactly I j-"
    scene fattie_locker_attack3
    woman "Well I’m here for my service."
    menu:
        "Distract her":
            "Whoa, who leaves a box of donuts in their locker like that?"
            scene fattie_locker_attack4
            woman "It's mine!"
            s "(Now’s my chance to get out of dodge!)"

        "Try to reason with her":
            s "I think you got it mixed up, I don’t-"
            scene fattie_locker_attack5
            with fade
            s "Oh fuck."
            woman "There we go."
            scene fattie_locker_attack6
            with fade
            s "(I wonder how much health insurance will cover for a crushed pelvis?)"
            woman "{i}Hnnngggg{/i}... ah yeah."
            woman "That’s exactly what I needed, thanks doll."
            scene fattie_locker_attack7
            with fade
            s "(Water… soap… bleach.)"
            s "(I don’t think I’ll ever feel clean again.)"
    $ pass_time(60)
    jump loc_gym_locker

label saggy_tits_latina_sauna:
    hide screen ui_icons
    hide screen ui_text
    scene saggy_tits_latina_sauna2
    s "Pardon me, I didn't realize you were in here and so... uncovered."
    woman "I wouldn't be here looking like this if I was concerned with what people may or may not see."
    s "Fair enough, do you mind if I join you?"
    woman "Come, sit. Don't let me scare you away."
    scene saggy_tits_latina_sauna3
    woman "You're either the new trainer here who has... alternative preferences or you're a random guy off the street who found a way to sneak in."
    woman "One scenario leaves me disappointed while the other has me worried."
    s "No you're right, I'm the new guy."
    s "Wait, why would you be disappointed?"
    scene saggy_tits_latina_sauna4
    woman "I'm feeling a bit exhausted, baby. I hope you don't mind me cutting our conversation short while I lay down."
    s "(Disappointed how, that I'm 'gay'?)"
    s "By all means go ahead."
    scene saggy_tits_latina_sauna5
    s "(At least she can't see me admiring her from this angle.)"
    $ pass_time(60)
    jump loc_gym_sauna

label yoga_2girls:
    scene yoga_2girls1
    menu:
        "Look at the black girl":
            scene yoga_2girls2
            $ renpy.pause ()
            jump loc_gym_yoga

        "Look at the white girl":
            scene yoga_2girls3
            $ renpy.pause ()
            jump loc_gym_yoga

label monica_rubbing:
    hide screen ui_icons
    hide screen ui_text
    scene monica_locker_rub1
    s "(What's going on in here?)"
    scene monica_locker_rub2
    with fade
    s "(Whoa... she's huge!)"
    scene monica_locker_rub3
    woman "{i}*Panting*{/i}.... mmm... it's been too long..."
    scene monica_locker_rub4
    woman "Ayy dios mio..."
    woman "Me vengo!"
    scene monica_locker_rub5
    $ renpy.pause(1)
    s "(Hoooollllyyy shit! We've got a squirter!)"
    scene monica_locker_rub6
    s "(This place is definitely not passing any sanitation inspections.)"
    s "(But I won't stick around to tell {i}her{/i} that.)"
    $ pass_time(60)
    jump loc_gym_locker

### ARCADE
label bored_gf:
    hide screen ui_icons
    hide screen ui_text
    scene arcade_guy_bored_girl2
    woman "Why does this happen every single time you take me 'shopping'?"
    man "Ahuh, that's great news dear."
    woman "You're NOT listening to me again!"
    scene arcade_guy_bored_girl3
    man "Baby... once sec. I almost got it... high score here I come."
    scene arcade_guy_bored_girl4
    woman "I can't believe you're choosing that stupid game over me."
    man "Haha, that sounds really cool."
    woman "Seriously, you're ignoring me again?"
    scene arcade_guy_bored_girl5
    "The woman notices you watching her."
    woman "Hey baby, I'm not wearing any panties..."
    man "Yeah... I totally agree."
    scene arcade_guy_bored_girl6
    woman "With this short dress I'm wearing... aren't you worried that someone might see my pussy?"
    scene arcade_guy_bored_girl7
    man "Wow, that's a crazy sto- DAMNIT!"
    man "HOW'D THAT FUCKING HIT ME?"
    woman "Oh no... you lost! That's so sad. *wink*"
    man "*Grumbling* Let's go."
    $ pass_time(60)
    jump loc_arcade

label high_school_sluts:
    s "(I suddenly have the urge to study.)"
    menu:
        "Look at the redhead":
            scene arcade_schoolgirl_hockey_3
            $ renpy.pause ()
            jump loc_arcade

        "Look at the blonde":
            scene arcade_schoolgirl_hockey_2
            $ renpy.pause ()
            jump loc_arcade

### COFFEE
label mayan_ruclark1:
    hide screen ui_icons
    hide screen ui_text
    scene mayan_ruclark1
    s "(What is this, cowboy downstairs but hairdresser up top?)"
    scene mayan_ruclark2
    s "(Are those tubes of lipstick?)"
    s "(Must be Batman's fabulous utility belt I've heard so much about.)"
    man "So you have a green ball in your left hand..."
    man "... and a green ball in your right hand,"
    man "So what do you have?"
    ma "*shrugs* What?"
    man "The Hulk's dick in your mouth!"
    man "HAHAHAHAHA!"
    scene mayan_ruclark3
    ma "Uh, sorry sir but I need to attend to the next customer."
    scene mayan_ruclark4
    man "Honey, You can go right on ahead. And Damn if you ain't the cutest thing I’ve seen all week."
    man "Girrrl, you best be up in that... or I will. *wink*"
    scene mayan_intro8
    s "Huh, nice guy I like him. Not that way but how can you not love a man with that much sass?"
    ma "Reminds me of you when I first met you."
    $ pass_time(60)
    jump loc_coffee

### STRIP CLUB
label stripper_brunette:
    scene hikari_stripclub_intro14
    with fade
    $ renpy.pause ()
    scene hikari_stripclub_intro15
    $ renpy.pause ()
    scene hikari_stripclub_intro18
    $ renpy.pause ()
    scene hikari_stripclub_intro19
    $ renpy.pause()
    scene hikari_stripclub_intro20
    $ renpy.pause()
    $ pass_time(60)
    jump loc_stripclub

label stripper_ginger:
    scene stripper_ginger2
    with fade
    $ renpy.pause()
    scene stripper_ginger3
    $ renpy.pause()
    scene stripper_ginger4
    $ renpy.pause()
    scene stripper_ginger5
    $ renpy.pause()
    scene stripper_ginger6
    $ renpy.pause()
    $ pass_time(60)
    jump loc_stripclub
