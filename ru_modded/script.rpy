# ﻿init python:
#    config.overlay_screens.append('ui_text')

define fade = Fade(0.2, 0, 0.2)

default mainname = _("MC")
define s = Character("[mainname]", color='#ffb80e')
define so = Character(_("Sophie"), color='#d6e760')
define a = Character(_("Amy"), color='#d366da')
define ass = Character(_("Some Asshole"))
define dn = Character(_("Dani"), color='#e47676')
define ds = Character(_("Daisy"), color='#0e0ac2')
define j = Character(_("Jenna"), color = '#5c0d0d')
define m = Character(_("Maria"), color='#be2121')
define ma = Character(_("Mayan"), color='#754268')
define h = Character(_("Hikari"), color='#a586bf')
define w = Character(_("Walter"), color='#634216')
define tv = Character(_("TV"))
define his = Character(_("Historic Channel"))
define who = Character("???")
define ba = Character(_("Bartender"))
define com = Character(_("Commentator"))
define man = Character(_("Man"))
define woman = Character(_("Woman"))
define woman1 = Character(_("Woman 1"))
define woman2 = Character(_("Woman 2"))

### CHAR STATS
# AMY
default Mamy = False
default Oamy = 0
default Lamy = 0
default amy_love = 0
default amy_slut = 0
default amy_event = True

default amy_sauna1 = False
default lick_amy = False
default amy_bj1 = False
default amy_titjob1 = False
default amy_yoga_topless = False
default amy_yoga_topless2 = False
default amy_sex1 = False
default amy_sad_event1 = False
default amy_cum_inside = 0
default amy_plan = False
default amy_recon = False
default amy_cuck = False

# DANI
default Odani = 0
default Ldani = 0
default dani_event = True

default dani_cable = False
default dani_singing = False
# DAISY
default Odaisy = 0
default Ldaisy = 0
default daisy_event = True

default bj_daisy = False
# HIKARI
default Mhikari = False
default Mhikari2 = False
default Mhikari3 = False
default Ohikari = 0
default Lhikari = 0
default hikari_event = True

default strip1_hikari = False
default nude_locker_hikari = False
default nude_swim_hikari = False
default hikari_strip_intro = False
default hikari_bartender_help = False
default hikari_new_look = False
default hikari_first_strip = False
# JENNA
default Mjenna = False
default jenna_event = True

default jenna_shower = False
default jenna_bench_event1 = False
default jenna_event1 = False
default jenna_shower_revenge1 = False
default jenna_mma1 = False
default jenna_postmma = False
default jenna_spank1 = False
default jenna_teabag = False
default jenna_bj = False
# MARIA
default Mmaria = False
default Omaria = 0
default Lmaria = 0
default maria_event = True

default maria_yoga1 = False
default finger_maria = False
default sex_maria = False
default hikari_maria1 = False
# MAYAN
default Mmayan = False
default mayan_event = True
# SOPHIE
default Osophie = 0
default Lsophie = 0
default sophie_event = True

default sophie_yoga = False
default sophie_snack = False
default sophie_ps4 = False

default sophie_date1 = False
default sophie_gym_story1 = False
default sophie_park1 = False
default sophie_arcade1 = False
default sophie_breakup = False
default sophie_drunk = False
default sophie_drunk_bath = False # Drunk event choice
default sophie_drunk_bed = False #Drunk event choice
default sophie_hungover = False

default days = 0
default gym_intro = True
default fired = False

init:
    transform customzoom: # Guide Portrait
        zoom 0.7

    transform thumbzoom: # Gallery Thumb
        zoom 0.20

init -1 python:
#####  TIME SYSTEM ###############
    global minn
    minn = 0

    def pass_time(mins=1):
        store.minn += mins

    def hour(minn=-1):
        if minn < 0:
            minn = store.minn
        h, m = divmod(minn, 60)
        h = h % 24
        return str(h).zfill(2)+':'+str(m).zfill(2)

    def which_day(day=0):
        global minn
        global days
        day_num = (days % 7)
        day_name = (_('Sun'), _('Mon'), _('Tue'), _('Wed'), _('Thu'), _(' Fri'), _('Sat'))
        day = day_name[day_num]
        while minn > 1439:
            days += 1
            minn -= 1440
        return day


    def label_callback(name, abnormal): # variable last_label tracks the more recent label action
        if name != "gallery_label":
            if name != "guide_label":
                store.last_label = name

    config.label_callback = label_callback

########
label start:
    scene black
    $ pass_time(60)
    $ mainname = renpy.input(_("What's your name?"), _("Simon"))
    $ mainname = mainname.strip()

jump intro

return
