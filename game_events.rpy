### SOPHIE APARTMENT

label sleep:
    "I should get some sleep."
    scene sleep
    "(...zzZZzz..)"
    if 6 <= float(minn/60)%24 < 24:
        $ minn = 420
        $ days += 1
        jump loc_sophie
    else:
        $ minn = 420
        jump loc_sophie

label sophie_bath:
    $ sophie_bath = True
    scene sophie_bath1
    s "(Sophie's taking a bath and didn't close the door)"
    s "(Who the hell does that? Only in adult games and horror movies do people shower with the door unlocked.)"
    menu:
        "Keep Looking":
            s "(She's so sexy but she's also my cousin. I shouldn't be doing this... )"
            "Sophie suddenly jerked her head up, as if she heard something."
            so "Hello?... [s] is that you?"
            scene sophie_bath2
            "[s] entered the bathroom, trying his hardest to sell an act of ignorance."
            s "Did you need so-... what the hell? Why'd you call me in here when you're taking a bath."
            scene sophie_bath3
            so "Maybe I missed the good old days when we bathed as kids and had splashed each other?"
            s "... are you serious?"
            scene sophie_bath2
            so "No I'm not serious you doofus. I thought I heard something and didn't realize you were home."
            s "You should really lock the bathroom when you're in here."
            so "I sometimes forget that I'm not living alone anymore, old habits."
            scene sophie_bath4
            so "Anyways, sorry for scarring you for life with my hideous appearance."
            s "Get me a seeing eye-dog and I'll call it even."
            so "Very funny. Please close the door on your way out."
            $ pass_time(60)
            jump loc_sophie


        "Leave":
            s "(Better not risk spying on her... that'd be awkward to explain.)"
            jump loc_sophie

label sophie_yoga:
    $ sophie_yoga = True
    s "(Oh, so she does yoga now?)"
    menu:
        "Watch":
            if sophie_hungover:
                scene sophie_nude_home_yoga2
            else:
                scene sophie_home_yoga2
            s "(She really does have a plump bottom.)"
            if sophie_hungover:
                scene sophie_nude_home_yoga3
            else:
                scene sophie_home_yoga3
            s "(What is she doing, praying to the Goddess of great figures?)"
            if sophie_hungover:
                scene sophie_nude_home_yoga4
            else:
                scene sophie_home_yoga4
            so "(Why the hell is [s] watching me?)"
            if sophie_hungover:
                scene sophie_nude_home_yoga5
            else:
                scene sophie_home_yoga5
            so "Do you normally stand there quietly like a creep, spying on people in their underwear?"
            if sophie_hungover:
                scene sophie_nude_home_yoga6
            else:
                scene sophie_home_yoga6
            s "What? No!"
            s "I was hungry and was wondering why you weren't cooking breakfast."
            so "Oh, what poor little baby. Doesn't know how to cook for himself."
            s "Without you I'd simply starve."
            so "How about you let me finish what I'm doing and then I'll come out and get breakfast going?"
            s "That sounds great, thanks."
            so "*Sigh* Sometimes I feel like I'm babysitting you, [s]."
            s "Good thing I'm such a cute kid."
            $ pass_time(60)
            jump loc_sophie

        "Leave":
            s "(Probably best to not bother her while she's so... exposed.)"
            jump loc_sophie

label sophie_breakfast:
    $ sophie_breakfast = True
    if sophie_hungover:
        scene cooking_nude_breakfast1
    else:
        scene cooking_breakfast1
    s "(Looks like Sophie's making breakfast.)"
    menu:
        s "(Should I join her?)"
        "Yes":
            if sophie_hungover:
                scene cooking_nude_breakfast2
            else:
                scene cooking_breakfast2
            s "That smells delicious Sophie!"
            if sophie_hungover:
                scene cooking_nude_breakfast3
            else:
                scene cooking_breakfast3
            so "Good morning, sleepy bum. Do you want some too?"
            s "Sure."
            so "Get seated, it'll be ready in just a minute."
            if sophie_hungover:
                scene cooking_nude_breakfast4
            else:
                scene cooking_breakfast4
            s "This looks so good, thanks!"
            so "You're welcome."
            menu:
                "Chat":
                    if not sophie_gym_story1 and not gym_intro:
                        if sophie_hungover:
                            scene cooking_nude_breakfast4
                        else:
                            scene cooking_breakfast4
                        so "So are you going to lay around all day again today?"
                        s "Some of us have jobs you know."
                        so "Really? Are you messing with me?"
                        s "Nope, your little boy has become a little man."
                        so "That's so awesome [s], congratulations! So where do you work?"
                        s "I'm a personal trainer at a gym."
                        so "A trainer, huh? Going to whip some flabby butts into shape, eh? Which gym?"
                        s "Um, one not too far from here."
                        so "What is this, a gym for the secret service? Be a little more specific."
                        s "I, uh..."
                        so "Oh come on, spill it out already."
                        s "I work at the women's gym."
                        so "Very funny. Come on tell me, I promise not to embarrass you at work."
                        s "I'm serious, I work at the women's gym."
                        so "Right...except you know... you aren't a woman so I'm going to call bs on that story."
                        s "I told them I was gay, and they let me work there."
                        if sophie_hungover:
                            scene cooking_nude_breakfast5
                        else:
                            scene cooking_breakfast5
                        "Sophie erupted into laughter, gasping for air like a fish out of water."
                        so "You're kidding me. That's hilarious. Hahahahahah!"
                        if sophie_hungover:
                            scene cooking_nude_breakfast4
                        else:
                            scene cooking_breakfast4
                        so "Wait a minute...this isn't you coming out of the closet, right?"
                        s "Fuck off Sophie."
                        if sophie_hungover:
                            scene cooking_nude_breakfast5
                        else:
                            scene cooking_breakfast5
                        so "Hahahahaha. Oh that's rich. Well don't worry Mr. Fabulous, your secret is safe with me."
                        s "*grumbles*"
                        if sophie_hungover:
                            scene cooking_nude_breakfast4
                        else:
                            scene cooking_breakfast4
                        so "At least maybe now you can actually help around with groceries and stuff."
                        so "Just don't get any ideas of redecorating my apartment."
                        so "...and I better not catch you wearing any of my dresses!"
                        if sophie_hungover:
                            scene cooking_nude_breakfast5
                        else:
                            scene cooking_breakfast5
                        s "You're not going to let me live this one down are you?"
                        so "Of course I will, in like a year or two."
                        if sophie_hungover:
                            scene cooking_nude_breakfast4
                        else:
                            scene cooking_breakfast4
                        so "Anyways, I've got to get ready for work, can you please take care of the dishes?"
                        "Sophie left the table, giggling to herself as she headed towards her room."
                        $ sophie_gym_story1 = True
                    elif sophie_gym_story1:
                        if sophie_hungover:
                            scene cooking_nude_breakfast4
                        else:
                            scene cooking_breakfast4
                        so "So how's work, did you help paint any of the girls nails?"
                        s "Very funny, Sophie."
                        so "I'm sorry... I forgot how sensitive men like you can be."
                        if sophie_hungover:
                            scene cooking_nude_breakfast5
                        else:
                            scene cooking_breakfast5
                        so "Are your coworkers treating you well? Do you feel like one of the girls now?"
                        s "Yeah, they're treating me really great. One of them blew me, really sweet girl."
                        if sophie_hungover:
                            scene cooking_nude_breakfast4
                        else:
                            scene cooking_breakfast4
                        so "Eww, why you gotta make gross jokes at breakfast? I'm still eating here!"
                        s "Maybe I'm hoping for you to leave that bacon behind."
                        "[s] reached over to grab a strip of bacon but was tactfully slapped back by Sophie."
                        so "That was just a warning shot, never mess with this girl's bacon!"
                        s "I think you broke my hand."
                        "Sophie laughed as she dropped her plate into the sink and headed towards her room."
                    else:
                        so "So...any productive plans for today?"
                        s "I'd need a plan first before I could tell you whether it's productive or not."
                        if sophie_hungover:
                            scene cooking_nude_breakfast5
                        else:
                            scene cooking_breakfast5
                        so "Very funny. If I come home to you just sitting on the couch all day...I'll...I'll kick you in the head."
                        s "Did I ever tell you what a beautiful and loving creature you are?"
                        so "Ahuh... I need to get ready for work. Can you please clean up?"
                        s "No problem! (I wonder how aerodynamic these plates are.)"
                    $ pass_time(60)
                    jump loc_sophie_kitchen
                "Leave":
                    jump loc_sophie_kitchen
                    $ pass_time(60)
        "No":
            jump loc_sophie_kitchen

label sophie_work:
    $ sophie_work_leave = True
    $ sophie_work = True
    scene sophie_work1
    so "Hey [s], I'm heading out to work."
    so "Be honest, do I look too slutty like this?"
    s "(Sophie came out wearing a pretty outfit.)"
    scene sophie_work2
    s "(It's pretty mild aside from the revealing cleavage.)"
    scene sophie_work1
    s "No, it's not slutty at all."
    s "You look like you won't compromise your morals for anything less than a promotion."
    scene sophie_work3
    "Sophie laughed as she walked towards the door."
    so "Great! That's exactly the look I was going for."
    scene sophie_work4
    so "See you later!"
    $ pass_time(60)
    jump loc_sophie

label sophie_work_home:
    $ sophie_work_home = True
    scene sophie_work5
    s "(Looks like Sophie's just getting home from work.)"
    so "Hey [s]."
    s "(She does not look like a happy camper.)"
    s "Hey, how was work? Did you get that promotion?"
    scene sophie_work6
    "[s] winked at Sophie as she glared him down before letting out a giggle."
    scene sophie_work7
    so "No promotion. I guess I need to work on my oral skills."
    s "You know what they say, practice makes perfect!"
    scene sophie_work8
    so "Thanks for the inspiring pep talk. I'm going to go get changed."
    $ pass_time(60)
    jump loc_sophie

label sophie_changing:
    $ sophie_changing = True
    if days%7 == 3:
        scene sophie_changing1
        s "(Oh wow! Sophie forgot to close her door.)"
        menu:
            "Look":
                scene sophie_changing2
                s "(She's got such a great body.)"
                menu:
                    "Keep looking":
                        scene sophie_changing3
                        s "(I can't wait to see what those tits look like.)"
                        menu:
                            "Keep looking":
                                scene sophie_changing4
                                s "(Holy hell! If only I could get a better view..)"
                                menu:
                                    "Keep looking":
                                        scene sophie_changing5
                                        s "(Oh...I'm fucked.)"
                                        so "What the hell?!"
                                        scene sophie_changing6
                                        so "Why didn't you say anything!?"
                                        s "Sorry Sophie, I only just now noticed!"
                                        so "Yeah  right..."
                                        jump loc_sophie
                                    "Look away":
                                        s "(I better not get caught.)"
                                        jump loc_sophie
                            "Look away":
                                s "(I better not get caught.)"
                                jump loc_sophie
                    "Look away":
                        s "(I better not get caught.)"
                        jump loc_sophie

            "Look away":
                s "(I better not get caught.)"
                jump loc_sophie
    else:
        scene sophie_door_closed
        s "(Sophie's in there, better not bug her.)"
        jump loc_sophie

label sophie_ps4:
    $ sophie_ps4 = True
    if sophie_hungover:
        scene sophie_nude_ps41
    else:
        scene sophie_ps41
    s "(Oh man, she gets so intense when she plays these shooting games.)"
    menu:
        "Join her":
            if sophie_hungover:
                scene sophie_nude_ps42
            else:
                scene sophie_ps42
            so "Where'd he go?"
            s "How's my elite little Nazi killer doing?"
            if sophie_hungover:
                scene sophie_nude_ps43
            else:
                scene sophie_ps43
            so "Now I've got you, you little cunt."
            "Sophie wasn't quick enough as her character took two bullets to the head before dropping on to the ground."
            so "WHAT THE HELL? "
            so "FUCKING LAG!"
            so "I will find your children and rip their heads off, then I will shit down their goddamn neck!"
            s "Jesus Christ, Sophie. Tell me how you really feel?"
            if sophie_hungover:
                scene sophie_nude_ps44
            else:
                scene sophie_ps44
            so "Sorry, you're just distracting me."
            s "But I'm not doing anything."
            so "You being here is distracting to me."
            s "Ok, guess I'll go fuck off somewhere else then."
            if sophie_hungover:
                scene sophie_nude_ps45
            else:
                scene sophie_ps45
            so "Motherfuckers, why won't you die!?"
            s "Love ya."
            so "Love you too!"
            so "You think you're safe in that tank from ME!?"
            jump loc_sophie

        "Leave":
            s "(Better not bug her. If she dies she'll blame me for it.)"
            jump loc_sophie

label sophie_tv:
    $ sophie_tv = True
    if sophie_hungover:
        scene sophie_nude_tv1
    else:
        scene sophie_tv1
    hide screen loc_sophie_nav
    s "(Sophie's watching TV, should I join her?)"
    menu:
        "Yes":
            if sophie_hungover:
                scene sophie_nude_tv2
            else:
                scene sophie_tv2
            menu:
                "Smack her ass":
                    if sophie_hungover:
                        scene sophie_nude_tv3
                    else:
                        scene sophie_tv3
                    with vpunch
                    "*SMACK*"
                    s "HEY, SPORT!"
                    if sophie_hungover:
                        scene sophie_nude_tv4
                    else:
                        scene sophie_tv4
                    so "Owww!!!"
                    if sophie_hungover:
                        scene sophie_nude_tv5
                    else:
                        scene sophie_tv5
                    so "What the hell? *Laughing* You're such a sneaky terrorist."
                    s "What are we watching?"
                    so "Just the news."
                    so "I plopped down on the couch and was too lazy to even grab the remote."
                    if sophie_hungover:
                        scene sophie_nude_tv6
                    else:
                        scene sophie_tv6
                    tv "A new study by St. Mary's Analytics has been causing quite the stir lately."
                    tv "In a blind study with 500 participants, scientists have isolated cell compounds found in semen which they claim is the cause of male homosexuality."
                    tv "'When a man orally ingests semen, the body begins displaying homosexual side-effects,' says Viktor Spunklov, St. Mary's lead researcher."
                    tv "'We've now successfully identified the cellular structure that makes men have the desire to go to hell.'"
                    tv "'Now that we know what causes homosexuality, we can work on altering semen to reverse its gay properties.'"
                    tv "Participants of the study had mixed results in the way the experiment was conducted."
                    tv "'The whole thing was bit strange. I jumped at the chance to help science in the battle against homosexuality,' says Mack Johnson, 37."
                    tv "'We were brought into a room in groups of 6. We had to suck each other off in order to ensure that the samples were fresh and most potent.'"
                    tv "'I had to suck 5 dicks in a row and it was absolutely disgusting. I had to do it man, I just had to do it in the hopes of finding a cure for the sick and depraved in our community.'"
                    tv "'When faced with adversity I always ask myself, what would Jesus do? I then swallowed every last drop.'"
                    tv "'If it means saving the souls of these faggots then by God I will do all I can to help.'"
                    tv "However, not all of the participants were there solely out of civil duty."
                    tv "'I thought it was just a standard good ol fashioned gay orgy,' says Billy Federson.'"
                    tv "'It wasn't until I was handed a $50 bill that I realized that they were doing some sort of experiment'"
                    tv "'Hell boy, that was the best day of my life and I earned more than my standard rate.'"
                    tv "Although research is still ongoing, the initial takeaway seems to be that swallowing semen has a high risk of contracting homosexuality."
                    tv "This has been Weasel News, bringing you fair and balanced coverage."
                    if sophie_hungover:
                        scene sophie_nude_tv7
                    else:
                        scene sophie_tv7
                    if sophie_gym_story1:
                        so "Oh my God! Is that what happened to you? Did you unexpectedly contract homosexuality from sucking dick?"
                        s "Oh jeez, you're so funny, Sophie."
                        s "Now if you excuse me, I need to get up before I contract the 'Monkey Face Virus' from you."
                        so "Hmmm, that would explain why I love bananas so much... "
                    else:
                        so "Sometimes I feel like I should never leave this apartment and pretend the outside world doesn't exist."
                        s "I'm right there with you."
                    $ pass_time(120)
                    jump loc_sophie

                "Sit down":
                    s "What are we watching?"
                    if sophie_hungover:
                        scene sophie_nude_tv5
                    else:
                        scene sophie_tv5
                    so "Just the news."
                    so "I plopped down on the couch and was too lazy to even grab the remote."
                    if sophie_hungover:
                        scene sophie_nude_tv6
                    else:
                        scene sophie_tv6
                    tv "A local firefighter is facing sexual assault charges after what seemed like a routine night of work."
                    tv "A video recorded by the neighbor of the victim has gone viral, showing what appears to be firefighter Jason Kinley grabbing a woman by her genitals."
                    tv "911 recordings show that at approximately 1:30am last Tuesday, a woman was calling about a domestic emergency. That's when Engine 17 was dispatched to her house."
                    tv "The woman states that her cat, Lola, had been stuck in a nearby tree overnight and she feared for her safety."
                    tv "'I just wanted my little Lola safe and cuddled up against me. Instead, I was violated by the men in uniform that I was raised to trust.'"
                    tv "Jason Kinley is claiming that he did not intend to sexually harass the woman."
                    tv "'This is all a misunderstanding, really!'"
                    tv "'When we arrived at her house, she answered the door wearing a thong and a nearly transparent top.'"
                    tv "'When I asked her what the emergency was she kept telling me to climb up and bring her pussy to bed.'"
                    tv "'I know it's unprofessional of me to engage in such activities while in uniform, but frankly, I haven't bust a nut in a while.'"
                    tv "'When I obliged with her request and put my arms around her waist, she began screaming hysterically that I should get her pussy off instead of touching her.'"
                    tv "'I admit that it was confusing, but I've never turned down a pretty lady before.'"
                    tv "'I apologize for my actions but maybe going forward, she should stop calling her cat a pussy.'"
                    tv "President Drumpf made a few remarks about this incident at a press conference this morning."
                    tv "'I just don't get it folks, I don't get it. A lady, asks a man, to grab her pussy. What do you do? Of course you grab her pussy!'"
                    tv "'When you're famous, they let you do it. And some, I imagine, let you do it if you're a fireman.'"
                    tv "'A poor innocent man has now had his life destroyed because of this political hit job, believe me folks.'"
                    tv "'Maybe the Clantons and Greg Soros paid her to lie. I don't know. That's just what I know.'"
                    tv "'Ask anyone, really, ask anyone. They'll tell you that Soros and Barnie Sanders grab pussy all the time. Does the media cover that? Noooo!'"
                    tv "'This country's too politically correct, too correct. First you can't piss on under-age hookers, now you can't grab women's pussies.'"
                    tv "'What's next? I tell you what. They will come and say you can't shoot your guns either. They will then give your guns to illegal immigrants from shit hole countries.'"
                    tv "'Trust me folks, I went to the best schools, the best. I know a lot of things and I say a lot of things too!'"
                    tv "Some have criticized the President for using such profane and insensitive language to which he replied 'Buckle up, Snowflake'."
                    tv "This has been Weasel News, bringing you fair and balanced coverage."
                    s "Ummm.... what?"
                    if sophie_hungover:
                        scene sophie_nude_tv7
                    else:
                        scene sophie_tv7
                    so "What part didn't you understand?"
                    s "Better if you ask me what I {b}did{/b} understand."
                    so "Don't worry, they're just talking about pussy grabbing."
                    so "Cock grabbing seems to be ok, so you're in the clear."
                    s "You're never going to live down the gay thing, are you?"
                    so "Of course I will eventually... when I get old and my memory fails me."
                    $ pass_time(120)
                    jump loc_sophie

        "No":
            s "(Maybe another time.)"
            jump loc_sophie

label sophie_snack:
    $ sophie_snack = True
    if sophie_hungover:
        scene sophie_nude_towel_snack2
    else:
        scene sophie_towel_snack2
    s "Are you practicing for something?"
    "Sophie turned around with her mouth full after taking a huge bite out of the cucumber."
    if sophie_hungover:
        scene sophie_nude_towel_snack3
    else:
        scene sophie_towel_snack3
    so "I dohn't nhed practesh."
    s "Come on now, don't talk with your mouth full. I can't understand you."
    so "*Gulp*"
    if sophie_hungover:
        scene sophie_nude_towel_snack4
    else:
        scene sophie_towel_snack4
    so "Well, well, never thought I'd see the day where you'd be jealous of a cucumber."
    s "I'm not jealous, especially not after what you did to the poor guy at the end there."
    so "Make all the jokes you want but we'll see who's laughing once the world recognizes my talents!"
    s "I can already imagine all of the nice things you'll buy me!"
    so "Ha, your stocking's going to be full of coal this Christmas."
    jump loc_sophie_kitchen

label sophie_laptop:
    $ sophie_laptop = True
    if sophie_hungover:
        scene sophie_nude_home_laptop2
    else:
        scene sophie_home_laptop2
    s "Hey monkey, whatchya doing?"
    so "Watching Survivor Island Child Pageant."
    so "It's that great new show where they take a bunch of child beauty pageant winners and their parents and throw them on an island with limited resources."
    so "Whoever can stay there the longest without crying to go home wins."
    so "Wanna watch it together?"
    s "Uhhhh... that doesn't sound like my kind of jam."
    if sophie_hungover:
        scene sophie_nude_home_laptop3
    else:
        scene sophie_home_laptop3
    so "You mean you don't want to see Honey Boobee's 300lb mom get bitten in the ass by a snake?"
    s "Surprisingly, no."
    so "Ok, your loss."
    s "Goodnight, Sophie."
    if sophie_hungover:
        scene sophie_nude_home_laptop4
    else:
        scene sophie_home_laptop4
    "Sophie began giggling when Honey Boobee tried to suck the venom out of her mother's ass."
    jump loc_sophie_bedroom

label sophie_sleeping:
    $ sophie_sleep = True
    if days%7 == 1 or days%7 == 3:
        if sophie_hungover:
            scene sophie_nude_sleep3
        else:
            scene sophie_sleeping_blanketon
        s "(Looks like Sophie forgot to close her door.)"
        if sophie_hungover:
            menu:
                "Take a look":
                    scene sophie_nude_sleep4
                    s "(I really hope that she just has a couple dozen pairs of those same panties rather than wearing the same dirty ones all the time.)"
                    jump loc_sophie
                "Leave":
                    jump loc_sophie
        else:
            menu:
                "Leave":
                    jump loc_sophie
    if days%7 == 2 or days%7 == 4:
        if sophie_hungover:
            scene sophie_nude_sleep1
        else:
            scene sophie_sleeping_blanketoff1
        s "(Whoa, there's a nice sight!)"
        menu:
            "Take a closer look":
                if sophie_hungover:
                    scene sophie_nude_sleep2
                else:
                    scene sophie_sleeping_blanketoff2
                s "(I better get out in case she wakes up.)"
                menu:
                    "Leave":
                        jump loc_sophie
            "Leave":
                jump loc_sophie
    else:
        scene sophie_door_closed
        s "(Sophie's door's closed. Better not bother her.)"
        jump loc_sophie

label sophie_date_event1:
    $ sophie_date = True
    hide screen ui_icons
    hide screen ui_text
    scene sophie_date1
    "Sophie was surprised to see [s] as she entered the room. She was wearing an elegant red dress that contrasted the adorable childish expression on her face."
    so "Oh... uh hey [s]. I wasn't expecting you to be home."
    s "Well well well, look who we got here. Where were you out to looking so fancy?"
    so "*Sigh*... I was having dinner with a friend."
    s "A friend huh? Do you normally get so flustered when having dinner with friends?"
    so "I was on a date ok? I know a butt like you would love to tease me about it so I didn't want you to know."
    s "*Gasp* A date!? How'd you score a date with a goofy face like that?"
    scene sophie_date2
    so "Duhhh, I just gave him one of these brilliant smiles and he couldn't resist!"
    scene sophie_date3
    "Sophie walked across the room, the sounds of her heels echoing across, and took a seat next to [s] on the couch."
    so "It's just a date. I couldn't pass up a free dinner you know."
    scene sophie_date4
    so "Dinner AND drinks!"
    s "AND drinks!? Well why didn't you say so from the beginning!"
    s "You know it's in our blood to never pass up a drink, especially a free one."
    so "Red dress pairs with red wine, didn't you know?"
    s "Excellent point as always. I'm now at ease knowing that your date was engaged in stimulating conversation the entire time."
    s "Did you tell him about your booger collection too?"
    scene sophie_date5
    "Sophie burst into laughter as she playfully smacked [s] in the head."
    so "You butt, I was 6 years old! You're laughing now but just wait till the booger appraiser values my collection at a million dollars."
    so "You'll be sooo sorry you didn't believe in me!"
    scene sophie_date6
    s "You know I only tease you because I love you, Sophie."
    s "I only hope whoever he is, that he appreciates what a worthless creature he is compared to you."
    s "Any man would be absolutely lucky to have you."
    so "Awww, thanks [s], you're kind of ok in my book too."
    so "I'm going to go take a shower and change."
    s "Ok, just remember that red means hot and blue means cold. I don't want you getting hurt again."
    scene sophie_date7
    so "Huurrr durrr, you're so funny!"
    so "Good night [s]. Thanks for being the best."
    "Sophie gave [s] a kiss on the cheek before heading off towards her bedroom."
    $ sophie_date1 = True
    $ pass_time(60)
    jump loc_sophie

label sophie_park_event1:
    hide screen ui_icons
    hide screen ui_text
    scene sophie_park1
    "Sophie was home already, mumbling a greeting while reading the paper."
    s "Hey, want to go do something?"
    scene sophie_park2
    so "What'd you have in mind?"
    s "Nothing big, just wanted to get some fresh air and catch up with my lovely cousin."
    s "Want to go for a walk?"
    so "Things you'd say to a dog for 400, Alex."
    s "*Laughing* Come on girl!"
    scene sophie_park3
    " [s] and Sophie walked a few blocks around their building, stopping at a relaxing bench hidden in an alcove."
    s "That looks like a good place to take a break."
    so "You're tired already? Don't you work at a gym?"
    s "I'm just looking out for you, silly."
    scene sophie_park4
    "The two sat for a while and chatted about times long past."
    so "Hey... hey look, do you see that?"
    s "... what am I looking at?"
    so "That person over there, by that shop. See them?"
    s "The lady sitting down?"
    so "Yeah! She's wearing the same shirt as you!"
    s "Haha, you're so funny."
    scene sophie_park5
    so "I'm sorry, I didn't mean to offend you. It looks good on you too!"
    "Sophie couldn't contain her laughter. A few pig like snorts escaped her."
    so "Phew... I thought I was going to cry and pee my pants. Is my eyeliner running?"
    s "I don't think so... maybe?"
    so "Sorry, I thought you were an expert on feminine products."
    scene sophie_park6
    "Sophie burst out into laughter once again."
    "[s] pinched her on the side until she settled down."
    scene sophie_park7
    so "Owww! That was mean."
    scene sophie_park8
    s "Listen Sophie... I've been meaning to tell you this for a while..."
    s "Thank you for taking me in. From the bottom of my heart, I can't thank you enough."
    scene sophie_park9
    so "Of course, that's what family's for."
    s "Not always, no one made you do it. But you took me in when I was at my lowest and I want you to understand how much it means to me."
    scene sophie_park10
    "Sophie reached up and pinched [s]'s cheek."
    so "Aww, I'd never let anything bad happen to my little [s]!"
    s "Ah yuck, I regret saying anything!"
    "The two sat for a few moments, watching the busy life of others on the street."
    scene sophie_park11
    s "So... who's this guy you've been seeing?"
    so "Oh it's no one."
    s "No one, huh? You're blushing and have been coming home late all dolled up over a no one lately."
    so "Ok... so it's this guy I met at work, a client actually."
    so "He was looking for a new firm to do his accounting with and I got assigned."
    s "Wow, lucky him. Got the prettiest accountant in all the city."
    so "Lucky him indeed! So we went to coffee a few times to discuss financials, turns out he's a super nice guy."
    s "What's he do?"
    so "He owns his own dental office, pretty cool right?"
    s "Cool isn't the first word that comes to mind when I think of dentists, but it's not bad I guess."
    s "Most importantly though, does he treat you right?"
    so "Of course, I wouldn't put up with someone who didn't!"
    s "If that dentist ever hurts you, I'll curb stomp his pearly white teeth!"
    scene sophie_park12
    so "Pffft, I'll cut off his head myself and mail it to his parents!"
    s "Damn Sophie, strict but fair."
    scene sophie_park13
    so "*Laughing* This has been a lot of fun, we should do it more often."
    "After a few more minutes of stimulating conversation, [s] and Sophie found themselves heading back home."
    $ sophie_park1 = True
    $ pass_time(120)
    jump loc_sophie # NEED TO ADD TO GAME

label sophie_arcade_event1:
    hide screen ui_icons
    hide screen ui_text
    scene sophie_arcade1
    "[s] entered the apartment to find Sophie resting her eyes."
    s "Hey couch potato, want to go do something?"
    so "I would but these puppies are barking today."
    s "That's what happens when you wear heels 24/7."
    scene sophie_arcade2
    so "A girl's gotta look good, ok?"
    s "Oh come on, let's get out of the house. We can head down the street to the arcade."
    s "It'll be like the good ol' days."
    so "Funny that you think of them as 'good' ol' days, considering I kicked your ass every time."
    s "We'll see about that... let's go."
    scene black
    "The arcade was only a short walk from home."
    scene sophie_arcade3
    so "Ahhh, I haven't stepped foot into one of these in ages!"
    so "What should we play first?"
    jump sophie_arcade_games

label sophie_arcade_games:
    menu:
        "Air Hockey":
            scene sophie_arcade4
            s "How about I kick your butt at air hockey?"
            so "Are you asking me to let you win? Sorry kid, life's a bitch *wink*."
            scene sophie_arcade5
            so "We should check if they have an extra striker you could use, to make things fair you know."
            s "So cocky for someone who's about to get their butt ki-"
            scene sophie_arcade6
            "Sophie struck a devastating blow and scored before [s] could finish his taunt."
            so "WHAT WERE YOU SAYING? I CAN'T HEAR YOU!"
            s "*mumbling* lucky shot... "
            "The game went on for a while with both players failing to find an opening in each other's defense."
            "Finally [s] managed a lucky shot that bounced off the side and centered into the goal."
            scene sophie_arcade7
            "[s] erupted into an obnoxious commentated cheer."
            s "GOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALLLLLLLLLLLL!!!!"
            s "MAGNIFICO, EXTRAORDINAIRE!"
            scene sophie_arcade8
            so "This isn't futbol, what the hell are you even saying?"
            s "EL CLASSICO STRIKES AGAIN!"
            so "You're such a dork, I can't believe we're related."
            who "Um- excuse me miss."
            "Sophie noticed the young girl, barely old enough to wear makeup, standing next to her."
            scene sophie_arcade9
            who "I just wanted to say that you and your boyfriend look soooo cute together!"
            so "Actually he's n-"
            who "I hope I find love like that when I get older."
            so "Um, thank you sweetheart!"
            who "Don't worry, you can kiss and stuff. I won't find that gross. Have a nice day!"
            scene sophie_arcade10
            "Sophie watched with fascination as the little girl ran off back to her parents."
            s "Well... that was interesting."
            scene sophie_arcade11
            so "Awwww! Did you hear that? We make such a cute couple!"
            s "Gross. Don't you understand that it would be illegal for us to be a couple?"
            so "Hey, it's legal in some states."
            s "No it's not."
            so "Yeah it is! Some states let cousins marry one other."
            s "Cousins? I'm talking about bestiality laws."
            s "You think they'd let me marry a donkey like you?"
            "Sophie burst into laughter and began hitting [s] on the shoulder."
            so "You're such a little jerk!"
            jump sophie_arcade_games
        "Skee-Ball":
            scene sophie_arcade12
            so "Oooh, I actually want to play that ball roly game!"
            s "Skee-ball?"
            so "Yeah, yeah whatever it's called, I'm going to kick your butt at it."
            scene sophie_arcade13
            "As Sophie bent forward to grab a ball, [s]'s eyes couldn't help but wander to her ass."
            s "(She really does have a great figure.)"
            s "(All those years of playing sports in school left her a nice thick lower half.)"
            scene sophie_arcade14
            pause(1.5)
            scene sophie_arcade13
            s "(Whoa... get a grip of yourself [s].)"
            s "(Now is not the time to start fantasizing about your cousin.)"
            scene sophie_arcade15
            "[s] was too lost in his thoughts to realize Sophie's been trying to talk to him."
            so "Did you hear me?"
            s "I'm sorry, what?"
            so "I said I bet I can make it in on my first try."
            s "Well let's see it then."
            scene sophie_arcade16
            "Sophie launched the ball down the center and sunk it into the whole."
            scene sophie_arcade17
            so "Boooyah!"
            "She broke out into song and dance."
            so "Who's good? I'm good. I said who's good? I'm good."
            s "Relax, it's only the easiest one for 10 points. Bet you can't hit the 50."
            so "You're on, sista!"
            scene sophie_arcade18
            "Sophie launched one ball after the other and could not manage to sink one in."
            s "*Yawn* I'm falling asleep Sophie. Just admit defeat and let's move on."
            scene sophie_arcade19
            so "Hush, we're not leaving till I make one in. I don't care if we starve to death before I do."
            s "Meee-yeeow kitty."
            scene sophie_arcade20
            "After what felt like days, Sophie finally managed to land one in the 50 point target."
            scene sophie_arcade21
            so "Whooooo, I did it!"
            so "Who's good? I'm good. I said who's good? I'm good."
            s "Let it be known, Sophie never misses the target more than 97 times in a row."
            scene sophie_arcade22
            so "Quit being a butt, I can see the pride in your eyes!"
            s "That's just my soul you're seeing. It's leaving my body because I'm dying of old age from waiting on you."
            so "Haha, damn I look real good for my age."
            jump sophie_arcade_games
        "Go Home":
            scene black
            "After another hour playing classic arcade games like Pic-man and Face Invaders, the two decided to call it a night."
            scene sophie_arcade23
            so "I had so much fun tonight! Thanks for dragging me out."
            s "I had a lot of fun with you as always."
            so "We should hang out again more often. I miss us."
            s "I miss those days too Sophie. We'll definitely be spending more time together."
            $ pass_time(300)
            $ sophie_arcade1 = True
            jump loc_sophie

label sophie_breakup:
    hide screen ui_icons
    hide screen ui_text
    scene sophie_breakup1
    with fade
    so "Heyyy [s], how was your day?"
    s "It was pretty good actually, I we-"
    so "It doesn't matter, you know why?"
    s "Erm... why?"
    so "Because THIS GIRL GOT PROMOTED!"
    scene sophie_breakup2
    so "That's right, ah yeah!"
    s "Wow, really? Congratu-fucking-lations!"
    so "Thanks, I'm so excited! I'm finally a Senior Accountant I."
    scene sophie_breakup3
    so "You know what that means for us?"
    s "You're going to be buying me lots of presents and playboys and stuff?"
    so "Close... it means YOU and I are going to DRINK!"
    s "Great, when?"
    so "NOW! Let's go."
    scene sophie_breakup4
    so "Ahhh, I still can't believe I finally got it. I've been gunning for this promotion for so long now."
    s "Congrats Soph, I knew they'd finally realize that you're pretty smart... for a girl."
    so "Har har, and you're pretty straight for a gay guy."
    scene sophie_breakup5
    so "Now where'd I put it?"
    so "I know I left a bottle somewhere around here..."
    scene sophie_breakup6
    so "Aha! It's go-time, bitches!"
    s "You sure you haven't already been drinking?"
    so "Stupid question, I'm an accountant. Next."
    scene sophie_breakup7
    s "Ok, so how'd you end up getting the promotion?"
    so "What do you mean, how?"
    s "Well, like you've been trying to get it for a while right? So what'd you do that they finally ended up giving it to you."
    so "... you really want to know?"
    s "Duh."
    so "You sure you're not going to see me in a different light and get all judgmental?"
    s "Uhh... I don't like where this is going..."
    scene sophie_breakup8
    so "Well first I waited for everyone to leave, it's pretty usual for me to be one of the last people left in the office."
    so "I noticed my boss's light was still on in his office."
    so "So I knocked on his door and he said 'Come in'."
    so "I walked over all seductive, like so."
    so "Puffed out my chest while looking him straight in the eyes."
    scene sophie_breakup9
    so "I said, 'Oh Mr. Schnyder, you know how long and... hard, I've been working for that promotion?'"
    so "You know I would do anything to earn it. It's my duty as an employee to make sure my superior is satisfied."
    s "What the fuck, Sophie?"
    so "Then I got down on my knees and said..."
    scene sophie_breakup10
    so "'Is there {b}nothing{/b} that I can do to help {i}relieve{/i} your load... workload.?'"
    so "Long story short, that's how I got my promotion."
    s "Are you fucking kidding me? You really sold yourself out like that!?"
    scene sophie_breakup11
    so "No you fucking idiot."
    s "So what did you do then?"
    so "I worked my ass off for years until someone finally recognized it."
    so "Do you really think that little of me?"
    s "Oh... no Soph... it's just tha-"
    scene sophie_breakup12
    so "Relax, I'm messing with you. God, you're such a doofus sometimes!"
    so "You know me, I'd never take shit from someone. I have a little bit of self respect you know... or something like that."
    s "Yeah, not going to lie you had me going for a second."
    s "You always came up with the best bullshit when we were kids."
    s "How many times did I get in trouble for your mischief?"
    so "Hahaha, a princess can do no wrong!"
    so "Can you imagine though? There {i}are{/i} girls out there who would allow themselves to be lied to and manipulated like that, for a promotion or whatever."
    s "Yeah..."
    scene sophie_breakup13
    so "What's wrong with you? Have you still not gotten over my joke or something?"
    s "No, it's not that... it's..."
    s "{i}*Sigh*{/i} I need to talk to you about something."
    so "Did something happen to you, are you ok?"
    s "I'm fine, listen, maybe we should sit down for this."
    scene sophie_breakup14
    so "You're starting to scare me, [s]."
    s "I know, I'm sorry. Please sit."
    scene sophie_breakup15
    s "So you know that guy you've been seeing?"
    s "Weston?"
    so "Walter."
    s "Right, Walter."
    s "How serious are you two?"
    so "What is this, an intervention? I'm a grown woman I don't have to get your approval."
    s "No, no, of course not. You can do whatever you want, I know that."
    s "It's just I'm afraid Weston h-"
    so "Walter."
    s "Walter hasn't been completely honest with you."
    s "Did you know that he's married?"
    so "...."
    scene sophie_breakup16
    so "Hahaha, you had me going for a second."
    so "You're such a jerk. Was that payback for how I pranked you earlier?"
    s "No, I-"
    so "You got me good, phew. Are they teaching improv classes down at that gym or something?"
    s "Sophie, I'm not messing with you. This is not a joke."
    scene sophie_breakup15
    so "Ok, you're overdoing it now."
    s "I'm not overdoing anything, I'm telling you the truth."
    so "How would you even know? You only met the guy for 2 seconds."
    so "Don't tell me you ran a background check or something?"
    s "You know my 'date' for that night, who had a bit of an emergency which is why we couldn't make it?"
    so "Yeah?"
    s "That's Walter's wife, Amy. She came into the bowling alley, saw him, and bolted out of there."
    so "Walter's wife... you're dating his WIFE?"
    s "No, it's not like that it's... complicated."
    s "But you're missing the point, Sophie. He's been LYING to you!"
    scene sophie_breakup17
    s "Are you okay, Soph?"
    s "I know it hurts to be betrayed like that, believe me. But I'm here for you."
    scene sophie_breakup18
    so "Hurts... HURTS!?"
    so "Not as bad as he's going to hurt when I'm done with him."
    so "I'm going to RIP OFF HIS GOD-DAMN HEAD AND SHIT DOWN HIS NECK!"
    s "Whoa..."
    so "That motherfucker, who does he think he is? Pasty ass bitch thinks he can play me?"
    s "Please Sophie, don't do anything rash."
    so "What the hell are you talking about? You out of all people should understand how I feel right now!"
    s "I do, believe me, I do. But you said he's a client of yours. I don't want that smug little fuck to be the cause of you losing your job."
    s "Just trust in me, ok? I will make sure he pays."
    so "... and what are you going to do about it?"
    so "I don't want you going to jail for something stupid."
    s "Trust me, I won't be going to jail. He's been cheating on his wife remember?"
    s "Amy and I will figure something out. Trust me when I say that his ass will be crying for mommy."
    so "Good, make that pig suffer."
    scene sophie_breakup19
    with fade
    s "Where are you going, I thought you agreed not to do anything?"
    so "I'm going to blow off some steam, don't wait up for me."
    so "*Mumbling* {i}...two-faced motherfucker.{/i}"
    s "(Uh, I hate seeing Sophie hurt like this.)"
    s "(I need to lay down for a bit and think things through.)"
    $ sophie_breakup = True
    $ pass_time(300)
    jump loc_sophie

label sophie_drunk:
    hide screen ui_icons
    hide screen ui_text
    scene sophie_drunk1
    with fade
    s "(What the hell is this? Why is she sleeping on the couch?)"
    s "Pssst... Sophie, you up?"
    scene sophie_drunk2
    with fade
    s "(Atta girl, looks like she polished off the whole bottle.)"
    s "(Must be taking the news about Weston harder than I thought.)"
    s "(Still, I should get her to bed.)"
    scene sophie_drunk3
    s "Sophie, wake up!"
    "[s] began shaking Sophie out of her drunken slumber."
    so "Uhhhh... wha?"
    s "Get up, you're passed out on the couch."
    so "Ugh, I don't wanna... I go to shleeppp..."
    s "No Sophie, get up. Let's get you to bed."
    so "Nnhhhh... jush let me... shleep."
    "[s] yanked her by the arms, forcing her upright."
    scene sophie_drunk4
    so "Nnhhhh, why you {i}(hic){/i} not let me sleep?"
    s "Come on, donkey. You smell about as bad as one."
    s "Let's get you to bed."
    so "Ughhh, you arrrre... so bad. Let me shleep."
    s "As much as I like your pirate impression, we need to get you up."
    s "Unless you want me to lay on you and crush you?"
    so "Noooo... you'rrre fatassshh too big."
    scene sophie_drunk5
    with fade
    so "{i}(Hic){/i} Happy?"
    menu:
        "Take her to bed":
            s "I'll be happy once you're in bed and out of my hair."
            so "{i}Hahaha{/i} You'll be happy withh {i}(hic){/i} me in bed?"
            s "Not like that, weirdo."
            s "Come on, it's just a few steps."
            scene sophie_drunk_bed1
            so "Ish sho hot here..."
            s "Looks like you had the living room window open."
            s "Feels much cooler on the couch than here."
            so "Sho hot {i}(hic){/i} ish sho hot."
            s "Okay, we'll figure that out later. Let's get you into bed."
            scene sophie_drunk_bed2
            with fade
            with vpunch
            s "What the fuck are you doing?"
            so "I told you!"
            so "Ish sho hot."
            s "But I'm STILL HERE!"
            scene sophie_drunk_bed3
            s "If you're {i}(hic){/i} uncomfortable..."
            s "...leave."
            scene sophie_drunk_bed4
            s "It's not that I'm uncomfortable, you're just not supposed to get naked in front of me."
            so "My apartment."
            so "I can {i}(hic){/i} do what I want."
            s "So what, now you're just going to be prancing naked around the place?"
            scene sophie_drunk_bed5
            so "Shtop bein a little bitcshh..."
            so "Ish jusht boobsh..."
            scene sophie_drunk_bed6
            with fade
            so "Jusht my boobsh..."
            so "{i}zzZZ{/i}"
            s "(What the fuck, Sophie.)"
            s "(If you were anyone else right now...)"
            s "(No, I couldn't take advantage of the only person who's given a damn about me my whole life.)"
            s "(She's right though... why {i}didn't{/i} I just leave?)"
            s "(I need to remember to cover her up in a little bit before she gets a cold.)"
            s "{i}(Sigh){/i}"
            s "Good night, Soph. Sweet dreams."
            $ sophie_drunk = True
            $ sophie_drunk_bed = True
            $ pass_time(180)
            jump loc_sophie


        "She needs a bath to sober up":
            s "You're drunk off your ass."
            so "I'm not drunk. {i}(hic){/i}"
            so "YOU'RE drunk!"
            s "{i}(Sigh){/i} Ok, let's get you into the bath. You clearly need to sober up."
            scene sophie_drunk_bath1
            with fade
            so "Hehe, did you bring me {i}(hic){/i} here... did you bring me here- to see me naked?"
            s "What? No, you dirty donkey. I'm trying to take care of you."
            so "Bet you wishhh you can {i}(hic){/i} take care of me?"
            s "What's gotten into you? Take a bath and sober up you lunatic."
            s "I'll be right outside this door if you need anything."
            so "{i}Hehe{/i} You wait outside... while I get naked in {i}(hic){/i} here."
            scene sophie_drunk_bath2
            s "(Man, I've never seen her like this before.)"
            s "(She's usually been a pretty mellow drunk from what I remember.)"
            s "(Never seen her so out of it like this though, and making jokes like that too.)"
            scene sophie_drunk_bath2
            with hpunch
            $ renpy.pause(1)
            s "SOPHIE!?"
            s "YOU OK IN THERE?"
            so "[s]!!!"
            scene sophie_drunk_bath3
            with fade
            $ renpy.pause(1)
            s "What the fuck? Why are you naked on the floor?"
            scene sophie_drunk_bath4
            so "I fell... {i}hahahahaha{/i}"
            s "Jesus Christ, Soph. How'd you get to this level?"
            so "I drank... a lot! {i}hehe{/i}"
            so "Help me up doofush!"
            scene sophie_drunk_bath5
            with fade
            so "Oh man, I drank sho much."
            so "And then I fell, like drrrunk old grandma {i}hahaha{/i}"
            s "Yup, old grandma."
            s "Time for old grandma to take her bath and sober up."
            so "{b}Shexy{/b} old grandma!"
            s "Ok, sexy old grandma, get the water going and I'll go wait outside."
            so "You're {i}(hic){/i} an old gaypa!"
            so "{i}Hahahaha{/b}"
            s "Don't tell me you've hit your head and gone retarded."
            so "Don't telllllll {b}me{/b} that you... that you'rrrre happy seeing sexy grandma naked."
            s "Ooookay, time for me to go."
            scene sophie_drunk_bath6
            with fade
            s "I'm keeping the door open in case you fucking fall again or drowned."
            so "Or to shpy on your naked cousin!"
            so "{b}ROLLLLL TIIIIIIIIIDEEEE!{/b}."
            s "(She has absolutely lost her mind.)"
            s "I can't wait for tomorrow morning to tell you what you were saying."
            s "Wish I could record it just to embarrass you."
            so "Wish you could record it sho {i}(hic){/i} you couldddd- jyack OOOOOHHHFFFFFFF!"
            s "Alllright then, note to self, hide all the wine bottles."
            s "(I'm going to love embarrassing her with this night.)"
            s "(Next time she cracks a gay joke at me, I'll just shout {b}ROLLLL TIIIIIIIDEEEEEEEE{/b})"
            $ renpy.pause(1)
            s "(Not going to lie though, she does look good.)"
            s "(I've always been curious to see what she has going on under there.)"
            s "(It's pretty obvious to anyone that little Soph grew up to be thicc.)"
            s "(Meat on her bone in all the right places.)"
            s "(Still kind of mentally processing that I've now seen all of her.)"
            s "(If I was any shittier of a person than this would be a dream scenario to be in.)"
            s "(But no... I couldn't do that to Sophie.)"
            s "(She's the only one in this world who actually cares about me.)"
            s "(She wouldn't backstab or abandon me like some of the trash I've had the foul fortune of having in my life.)"
            s "(Without her, I'd probably be sleeping on the streets right now, or in jail for a double homicide.)"
            s "Soph, you almost done?"
            s "..."
            s "Sophie?"
            scene sophie_drunk_bath7
            with fade
            $ renpy.pause(1)
            s "Are you fucking kidding me?"
            s "The water's not even that warm, how the hell did you manage to fall asleep?"
            so "Uhhhnnn... be quiter. I'm trying to sh.... {i}(zzzZZ){/i}."
            s "WAKE UP!"
            so "AH!"
            s "Get out and put on a towel."
            so "You jusht want to {i}(hic){/i} see me naked again!"
            s "That doesn't even make any sense. You're already naked, I can see you right now!"
            so "But I'm in water..."
            s "I don't even know how many brain cells I've lost tonight... get up, Soph!"
            scene sophie_drunk_bath8
            so "You losht brain shells because there ish blood- {i}(hic){/i}."
            so "There ish blood in your weiner."
            so "{i}Hahahaha{/i}"
            s "What?"
            so "Blood's in your weiner {i}(hic){/i} not in your head."
            so "{i}Hahahaha{/i}"
            s "Okay, off we go."
            scene sophie_drunk_bath9
            with fade
            so "You want to take me to bed?"
            so "But you cant!"
            s "That's fine, I think you can manage it from he-"
            so "BECAUSE {b}ROLLLLLLL TIIIIIIDEEEEE{/b}!"
            so "{i}Bahahahaha{/b}!"
            s "{i}(Sigh){/i} Yup, ok. Off you go now."
            s "Sweet dreams and all."
            scene black
            with fade
            "Only a few steps in, Sophie somehow managed to lose her towel as she face planted onto the bed."
            scene sophie_drunk_bath10
            with fade
            $ renpy.pause (0.4)
            scene sophie_drunk_bath11
            with hpunch
            so "Fuuuuuck!"
            s "Holy shit, are you okay?"
            so "{i}Hahahahahahaha{/i}"
            s "I leave you for literally two seconds and you've already hurt yourself."
            so "Help me up."
            scene sophie_drunk_bath12
            so "{i}Hahaha{/i} I keep falling like an old grandma!"
            s "You're falling like an old grandma that got knee-capped with a bat."
            s "Now let's get you into bed, you little drunk maniac."
            scene sophie_drunk_bath13
            with fade
            so "Shanks {i}(hic){/i} [s]."
            s "Don't worry about it, donkey."
            so "I want- I want to {i}(hic){/i} tell you shomething."
            s "Yeah?"
            s "..."
            s "Soph?"
            so "{i}zzZZ{/i}"
            s "(Guess she's finally out for the night.)"
            s "(Maybe now I can finally get some sleep myself.)"
            s "(Probably will have to lay on my back though for reasons completely unrelated to the events of this night...)"
            s "Sweet dreams, you weirdo."
            scene black
            with fade
            $ sophie_drunk = True
            $ sophie_drunk_bath = True
            $ pass_time(180)
            jump loc_sophie

label sophie_hangover:
    hide screen ui_icons
    hide screen ui_text
    scene sophie_hangover1
    with fade
    s "(Looks like Sophie’s still recovering from last night. Damn she was in a rough state.)"
    s "(Least I can do is surprise her with some breakfast, considering she’s been feeding my ass this whole time.)"
    scene sophie_hangover2
    s "(Speak of the devil…)"
    s "Rise and shine, beautiful."
    so "{i}Uhhh{/i} I feel like death, don’t patronize me with your new-found bubbly personality."
    s "Meeeooow! Someone’s grumpy this morning."
    scene sophie_hangover3
    so "My head is ringing and my stomach is re-enacting a nuclear strike."
    s "Yeah, I’ve never seen you that drunk in my life."
    s "You were a hot mess. Making me proud as always, cuz."
    so "Am I still drunk or are you actually cooking?"
    s "Possibly, and yes I am."
    so "I didn’t even think you knew how the stove works, much less actually being able to whip something up."
    s "Hey, I did a lot of cooking when I lived with… her."
    s "I only stopped when I saw someone else scrambling her eggs."
    s "Now sit down, breakfast will be ready soon."
    so "I hope I don’t regret this."
    s "It’s not like it’ll make you feel any worse than you do now."
    scene sophie_hangover4
    with fade
    so "Wow… this actually looks pretty good."
    so "Just to be clear, eggs, bacon and toast is hard to fuck up… but coming from you, I’m impressed."
    s "You gently embrace me with one hand and smack me with the other."
    s "So what happened last night? You smelled like a vineyard."
    so "I guess I got a little carried away with the wine."
    s "Understatement of the day. Looks like you took the Wesley situation pretty hard."
    so "It’s Walt-"
    $ renpy.pause(1)
    so "Fuck it, he’s Wesley now."
    so "I texted him that it’s over."
    so "He blew up my phone, leaving voicemails trying to figure out why I’m leaving him."
    s "You didn’t tell him why, right? He can’t know that Amy found out about him or else it will rui-"
    so "Relax. He doesn’t know anything. I kept my mouth shut and ignored him."
    so "Do you know how hard it is to not say anything to the very person that you’re imagining driving a fork through their face?"
    s "Yikes. He’s your client right? Maybe you can arrange for him to have a meeting in a Saudi Arabian embassy or something."
    so "That won’t work, he’s a dentist not a journalist."
    scene sophie_hangover5
    so "{i}(Sigh){/i} I just need to forget about him until you give me the satisfaction of knowing that you’ve made his life hell."
    s "I will, Sophie, I promise you that."
    s "He will suffer for breaking your heart."
    scene sophie_hangover6
    so "Breaking my heart? Oh no, no, no! My heart is {i}not{/i} broken by any stretch of the imagination."
    so "Sure, I’m disappointed that it’s yet another loser that I ended up dating."
    so "I hoped he would be different, but no matter how great a guy seems it’s always the same shithead in the end."
    s "So if you’re not hurting… why were you such a mess last night?"
    so "Because he played me for a fucking {i}idiot{/i}!"
    so "I’m so angry that I got played by a God damn sleazy dentist!"
    s "That’s not fair, Soph. How are you supposed to know that he’s married?"
    so "The signs were all there, I allowed myself to ignore them."
    s "What do you mean?"
    so "Single men try to get you back to their place as soon as possible, they don’t avoid bringing you home like the damn plague."
    so "They don’t hide you from their friends and colleagues."
    so "It was all right there in front of me, clear as day, and I let myself get fooled because I was feeling a little lonely."
    so "But never again, it’s not going to happen."
    s "Soph, you shouldn’t be so hard on yourself. It could have happened to anyone."
    scene sophie_hangover7
    so "Whatever, it doesn’t really matter anymore. Can’t let it ruin such a special occasion."
    s "What’s the occasion?"
    s "Don’t tell me it’s your birthday."
    s "Fuck, I’m so sorry, I didn’t even get you a present."
    so "No doofus, it’s not my birthday."
    so "We’re celebrating you cooking for the first time."
    so "Congratulations, you’re now official one step closer to adulthood."
    s "Gee, thanks monkey."
    so "You know, this is actually not bad. Good job, kiddo, making mamma proud!"
    s "Aw thanks! I even sucked all the grease off the bacon just to make it lean and healthy for you."
    so "You’re disgusting. {i}Hahahaha{/i}"
    so "By the way… can you tell me exactly what happened last night?"
    so "More specifically, why was I naked this morning?"
    s "Oh boy, where to start."
    s "Well, when I came home you were passed out on the couch."
    if sophie_drunk_bed:
        s "I woke you up and dragged you to your room."
        s "Which by the way was no easy task. You’re even sassier drunk than you are now."
        s "Anyways, you decided it was too hot and started taking off your clothes."
        s "When I told you to wait until I leave, you called me a little bitch and just kept rolling with it."
    else:
        s "It took a lot of effort waking you up. You were so drunk that you couldn’t even stand."
        s "So I sent you into the bathroom to take a bath and sober up a bit."
        so "You thought it was a good idea to send a person, who is too drunk to stand, into a tub full of water?"
        s "I mean, sure, you could have drowned... I guess."
        s "But I was standing outside the door just in case!"
        so "How would you even know if I was drowning?"
        s "I don’t know… you’d make drowning noises?"
        so "[s], I love you… but you’re an idiot."
        s "{i}ANYWAYS{/i}... after your bath I tried to get you into bed."
        s "Your towel fell off and you just passed out on top of the bed."
    scene sophie_hangover8
    so "Sounds like I gave you a lot of trouble."
    s "Yeah… you were getting pretty silly."
    so "So you saw me naked?"
    s "I didn’t try to, if that’s what you’re wondering."
    so "But you {i}did{/i} see me naked, right?"
    s "Yeah…"
    s "I know it must be really embarrassing for you. I couldn’t wait to make fun of you for it, but thought I’d give you at least a day to recover first."
    so "I’m not embarrassed."
    s "Yeah right, Soph. Every time you bring up the whole ‘gay’ thing I’m going to grill you about last night."
    so "Do whatever you want. I’ve got nothing to be embarrassed about."
    so "I’m in great shape and got nothing to be ashamed of."
    s "You can’t tell me that you’re {i}not{/i} embarrassed about being naked in front of your own cousin!?"
    so "Nope! As a matter of fact, it’s probably more embarrassing for you than for me."
    s "How the fuck does that make any sense?"
    scene sophie_hangover9
    so "I mean… it’s got to be embarrassing popping a boner at the sight of your own cousin’s body."
    s "What? No fucking way!"
    so "No to what, that you didn’t get a little stiffy last night, or that you’re not embarrassed by it?"
    s "I didn’t get a boner, especially not because of a donkey like you!"
    so "Sure you didn’t…   do you remember Mrs. Levin?"
    s "What, your neighbor from when we were kids?"
    s "Yeah I remember her, how could I not? That woman was a goddess."
    so "That lady was a 50 year old train wreck. She was always tanning with a cigarette in her hand."
    so "Her skin looked like wrinkly leather."
    s "But she had a great pair of tits."
    so "If by great you mean it looked like a botched boob-job from the silent film era, then sure."
    so "That lady was such a mess. Yet whenever she was out in the front yard, tanning in her bikini, little [s] would get a little boner."
    so "Then try to run away and hide before anyone noticed."
    s "That only happened once!"
    so "Oh please,	 the kids called you Woody."
    s "Whatever, I don’t see why you even brought this up."
    so "Because I doubt anything’s changed. You’re embarrassed that Woody made a special appearance last night."
    s "Nope, never happened. You had zero effect on me, sorry to disappoint you."
    scene sophie_hangover10
    so "Zero effect, is that so?"
    so "The only reason I even bother putting on a shirt is out of courtesy, I don’t want to make you feel uncomfortable."
    so "I used to always just hang out in my underwear, that’s the perk of having your own place."
    s "Sorry for disrupting your way of life."
    so "Well if I had ‘zero effect’ on you last night, maybe I’ll return to living like a queen of her own castle again."
    s "..."
    s "I’ve got to hand it to you. You had me going for a while."
    s "But you’re not going to bullshit me this time around. As long as you bust my balls about my job, I’ll bust you right back for last night."
    scene sophie_hangover11
    with fade
    so "Thanks again for breakfast, but I’ve got to run."
    so "Be a babe and pack the rest of it for my lunch."
    s "Wh-what…"
    scene sophie_hangover12
    with fade
    so "By the way…"
    so "Try not to get any nail polish onto your clothes at work today, it’s a real bitch to wash off."
    so "{i}Hahaha…{/i}"
    scene sophie_hangover13
    so "(What the fuck just happened. Is she really going to go through with this?)"
    so "(Hungover the morning after a breakup and she still somehow managed to wrestle back control?)"
    so "(Damn, what a woman…)"
    $ sophie_hungover = True
    $ pass_time(60)
    jump loc_sophie_kitchen

### COFFEE

label coffee_closed:
    scene coffee
    "The shop is open from 08:00 - 20:00"
    jump map_label

label mayan_intro:
    hide screen ui_icons
    hide screen ui_text
    scene mayan_intro1
    "[s] walked into a quaint coffee shop in a quiet part of town. Only the sound of the radio and the buzz of the fan could be heard. The size of the shop was quite optimistic for the amount of patrons present."
    "'Hipsters and coffee shops, name a more iconic duo' [s] mused to himself. The hipster's carefully crafted outfit screamed 'I'm really laid back, look at my hair! I just rolled out of bed', yet the blazer signaled his high status in the intellectual world."
    scene mayan_intro2
    ass "YOU CALL THIS A LOW-FAT CARAMEL FRENCH VANILLA LATTE WITH A HINT OF MONGOLIAN CAMEL MILK?! DISGRACE!"
    ass "THE VANILLA DOESN'T EVEN TASTE FRENCH DAMNNIT!"
    scene mayan_intro3
    who "Sir, please calm down. I already explained to you earlier that most coffee shops don't carry camel milk...."
    ass "You want to play games with me, you minimum wage ugly bitch!? You want another scar for your collection?"
    ass "Do you know who I am? I could cut you right now and no one would do anything!"
    who "Sir, there's no need t-"
    ass "I WILL CUT YOU FROM EAR TO EAR AND YOU WILL LOOK LIKE THE FUCKING JOKER!"
    ass "You'd like that wouldn't you? Probably got that on your lip from herpes."
    "No longer able to stand quietly on the sidelines, [s] decided it was time to make this clown leave."
    scene mayan_intro4
    s "Chad...? THERE YOU ARE!"
    "The douchebag turned, his body screaming 'Come at me bro' long before his lips could form the sentence."
    s "I waited at your apartment for over a damn hour! Don't even think that you're getting your deposit back."
    ass "Uhh... what? Do I know you bro?"
    s "I ran all over town getting everything you wanted, the 12inch black dildo, handcuffs, lube. The entire season of Dora the Explorer, although a strange request, I picked that up."
    s "I didn't even ask questions when you requested a life-size cardboard cutout of Donald Trump in his underwear. DO YOU EVEN KNOW WHAT I HAD TO DO TO GET IT!?"
    scene mayan_intro5
    "Senor Numbnuts was visibly uncomfortable. The hissy-fit from moments ago was replaced with confusion and perhaps slight arousal."
    ass "Bro... I don't know what you're talking about."
    s "Don't play stupid with me. This is EXACTLY why I ask for half of the money now, and half later."
    "Justin Bieber's biggest fan began noticing the stifled laughter and murmur's around the room."
    scene mayan_intro6
    ass "Guys, it's not true. I don't know this crazy guy."
    s "And you never will! You missed your chance. No amount of money is going to make me change my mind now."
    scene mayan_intro7
    "Even the barista tried her hardest to hide her laugh, which only infuriated Ryan Seacrest's scrotum."
    ass "Look motherfucker, I've had enough of you. If you don't tell these people that you're lying, I'm going to POUND...YOUR...ASS...SO HARD!"
    "The room erupted in laughter as the physical manifestation of Paul Manafort's conscience quickly realized how poorly chosen his words were."
    "'This isn't over' muttered Bentdick Arnold as he rushed out the door in embarrassment."
    scene mayan_intro8
    who "Thanks for doing that. I really wanted to kill him, but what you did was better."
    s "Doing what? You mean my performance wasn't authentic? Do you think I'm not hot enough to be a kinky sex-artist?"
    who "Ha, that was some top notch method acting, you nearly had me fooled."
    who "My name's Mayan by the way."
    s "Nice to meet you, I'm [s]."
    ma "What would you like?"
    s "I'd like a large Cappuccino to go. If it's not authentic Mongolian camel milk, I'm sending it back."
    "Mayan giggled off towards the espresso machine. Within a few minutes, the drink was ready."
    scene mayan_intro9
    ma "There you go [s]. It's on the house."
    s "Aw thanks, you didn't have to do that."
    ma "And you didn't have to do what you did, but you did it anyways. Hope to see you again soon."
    $ pass_time(60)
    $ Mmayan = True
    jump loc_coffee

label mayan_coffee:
    $ mayan_coffee = True
    scene mayan_intro8
    ma "Hey [s], what's it gonna be?"
    menu:
        "Order Coffee":
            s "Hey Mayan, hope your day's going well. I'd like a large cappuccino to go please."
            ma "Coming right up."
            "After a short moment, Mayan returned with the finished drink."
            scene mayan_intro9
            ma "There you go. See you next time."
            s "See ya."
            jump loc_coffee

        "Leave":
            s "I actually just wanted to say hello real quick. See ya later!"
            jump loc_coffee

label amy_coffee_event1:
    hide screen ui_icons
    hide screen ui_text
    scene amy_coffee1
    "Much to the pleasant surprise of [s], Amy was sitting at a table by herself."
    scene amy_coffee2
    "As he approached her he quickly realized that she was upset about something."
    s "Hey Amy...are you ok?"
    a "Oh? Hi [s]... I'm fine it's nothing. What a surprise to see you here, huh?"
    s "Yeah, I have a life out side of the gym you know. Mind if I join you?"
    "Amy motioned for [s] to sit, looking slightly more excited than moments earlier."
    scene amy_coffee3
    s "So what's going on, why are you sitting here alone all gloomy like?"
    a "I'm just thinking about stuff...everything's completely ok though."
    s "Is it something about your husband again?"
    scene amy_coffee4
    "Amy's body tensed at the mention of her husband. She couldn't look [s] in the eyes when she lied that it wasn't about him."
    s "Enough already, I know it's about your husband and you know I'm here to help. What's going on, is he not helping you out with your back pains?"
    a "*sigh* If only it was just about that. He refuses to do anything with me, let alone tell me he loves me every once in a while."
    scene amy_coffee5
    a "Am I being crazy? Is it unrealistic to expect even the tiniest shred of romance or affection from your spouse?"
    "Tears began forming on Amy's face. [s] knew that the last thing he wanted to do was console a sobbing woman in public."
    s "Let's go shopping."
    "Amy looked at [s] as if he was wearing a straitjacket."
    s "I'm serious. If your husband doesn't appreciate how sexy you are now, wait till he sees you after we dress you up."
    a "I don't know...I don't know how that would help."
    s "Come on, it'll be fun!"
    scene amy_coffee6
    a "You really want to go shopping with me?"
    s "It's time you TREAT YO-SELF!"
    scene amy_coffee7
    "The boutique was only a short walk away. [s] drooled at the thought of playing dress-up with this fiery milf."
    s "You can wait for me in the dressing room while I go pick something sexy for you."
    a "But you don't even know what style I like."
    s "Well judging by your shirt, your style is 'middle aged woman playing golf'. I think you should let me run this show."
    "Amy shuffled towards the dressing room muttering to herself."
    a "There's nothing wrong with my shirt..."
    scene amy_coffee8
    "The clothes were rather uninspiring for a boutique. After moving on to what felt like the 100th rack, [s] found what he was looking for."
    s "(There's no way she'll buy this but maybe I can convince her to try it on for me.)"
    scene amy_coffee9
    s "Ok, you're putting this on and I don't want to hear any objections."
    "Shock spread across her face as she realized how revealing the outfit was. After some back and forth, Amy gave up arguing and conceded."
    a "Fine, give it to me. I'll be out in a second."
    scene amy_coffee10
    "[s] shook his head and stepped into the dressing room, closing the door behind him."
    s "Don't be silly, just put it on while I'm here."
    a "Are you insane? You can't be in here, we're going to get in trouble!"
    s "I highly doubt anyone will care. Now hurry up and put it on."
    scene amy_coffee11
    "[s] found it oddly endearing to see Amy turn around before removing her top. It's not like he's never seen her bare breasts before."
    s "Do you ever wear a bra?"
    a "No, I don't find bra's or underwear comfortable at all."
    s "You don't wear underwear? You always go full commando!?"
    a "YES! Underwear is not comfortable, ok?"
    s "Well you're going to have to start wearing sexy bra's and panties at home at least. I'm sure your husband will appreciate it."
    a "Like that's going to matter."
    s "I'm sorry...did Santa never wrap your presents for Christmas when you were a kid?"
    s "Either way, I'm going to go look for some sexy panties for you. I'll be right back."
    "Within minutes [s] found attractive pink panties with a transparent laced design on top."
    scene amy_coffee12
    "As he re-entered the dressing room, Amy had already put her new top on, cautiously awaiting his judgement."
    s "Wow..."
    a "I told you this is stupid. A woman my age would be out of her mind to shove her saggy breasts into something like this!"
    s "Are you kidding me? You look absolutely stunning. Your tits are out of this world!"
    s "Look how well that top supports them. It's like gravity doesn't exist."
    scene amy_coffee13
    "Amy raised her hands to her breasts, enjoying the smooth fabric on her skin. A smile crept along her face as she realized that her breasts do in fact look great with the extra support."
    a "I guess you may be right. But it's still too revealing to ever wear."
    s "If you don't buy that top, I'm going to make you do 200 push-ups every time you step foot into the gym. You'd be absolutely crazy to not buy it."
    a "I'll think about it..."
    s "Great, now take off your pants."
    a "Gee, that's a reasonable request."
    s "I brought you panties to try on, doofus."
    scene amy_coffee14
    "Amy unzipped her pants and proved herself to be a woman of her word. She wasn't wearing any underwear."
    scene amy_coffee15
    s "You have such a great body Amy. I can't imagine what's wrong with your husband to not jump your bones every time he sees you."
    a "You're just saying that."
    s "I'm getting pretty tired of having to constantly convince you that you are so god-damn sexy."
    s "Do I have to fuck your husband straight before you believe me?"
    a "Hahaha, at this point he may as well be pitching for the other team. I don't even remember the last time we had sex."
    s "Well he should start changing his mind once he sees the new sexy Amy."
    scene amy_coffee16
    a "Tadaa! I'm wearing underwear. You happy?"
    s "You're not just wearing underwear, you're wearing sexy panties...and yes I'm happy."
    s "Even little [s] is happy, he's straining against my jeans."
    "Amy rolled her eyes sarcastically."
    a "Sure he is. I almost forgot that the 'new' Amy is so sexy that she turns gay men straight."
    scene amy_coffee17
    "[s] dropped his pants, exposing his soldier at attention."
    s "Like I said, I'm really tired of convincing you that you're attractive. Just look down and tell me what you see?"
    a "Oh my God [s], what the hell are you doing!?"
    s "Look down and tell me what you see."
    a "You have your fucking pants off!"
    s "Good, what else do you see?"
    "Amy felt like outrage was the proper response in a situation like this. Yet a part of her was excited to see a penis. It's been so long that she'd almost forgotten what they look like."
    a "Your penis for fucks sake!"
    s "Very good. Now tell me, is it flaccid?"
    a "No...."
    s "Damn right, it's hard as a rock. You know why? Because you're God damn sexy and you're turning me on. Do I need to keep convincing you?"
    "Amy felt a rush, was she actually as sexy as [s] said she was? She knew that she was no longer the red bombshell that made boys drool in college, but could it be that men still found her attractive after all these years?"
    a "(It's hard to assume he's lying just to be nice when there's hard evidence to prove otherwise.)"
    scene amy_coffee18
    a "(Why wouldn't a man want to be with me? A few wrinkles and extra pounds never stopped me from sleeping with older men back in my days...)"
    s "Uhhh... go ahead, make yourself at home."
    "Amy was so lost in thought that she didn't realize that she's been subconsciously holding on to [s]'s penis. Her hand shot back like it touched a hot stove."
    a "Oh my God, I'm so sorry!"
    s "That's totally ok. Obviously you haven't seen a dick in a long time. You'll be holding your husband's dick as soon as he sees you in the new outfit we picked out."
    a "I highly doubt that. Even with morning wood he won't have sex."
    s "Do you just try to hop on him or do you actually try to seduce him?"
    a "Yeah, seducing your husband after 15 years or marriage... ha."
    s "It doesn't matter how long you've been married. Sometimes men need to be teased."
    s "When's the last time you gave him a blowjob? I couldn't imagine anyone turning that down."
    "Amy looked nervously at the ground."
    a "I've....never given him a blowjob."
    s "WHAT? Not even on the honeymoon?!"
    a "No... I tried it once in college and didn't like it."
    s "Nope...nuh uh. This is unacceptable. We're going to fix that right now and save your marriage."
    s "On your knees, right now."
    a "You can't be ser-"
    s "I said on your knees. This has gone on long enough."
    scene amy_coffee19
    "Despite her protests, Amy knelt down and even grabbed a hold of [s]'s dick without command."
    s "You're going to practice giving a blowjob, and you're going to like it."
    s "When you get home today, you will give your husband a blowjob and he will like it. I don't want to hear any excuses."
    a "But what if he doesn't want one?"
    s "Then I will personally slap him myself."
    s "Now this isn't college. You did not like your experience back then, try to make the best of it now. Feel free to explore and do what you want."
    scene amy_coffee20
    "With great hesitation Amy ran her tongue around the head. 'A bit musky, but not bad' she thought."
    s "(She's not very good at this, but who am I to complain? A fucking knockout milf has my dick in her mouth.)"
    scene amy_coffee21
    "Satisfied with her expedition, Amy took the head into her mouth."
    a "(This isn't as disgusting as I remember it. There's no foul stench. Maybe it's because [s] has better hygiene than a frat boy?)"
    a "(What do I do if he cums though? What if I can't make him cum, that would be so embarrassing. Would he be mad?"
    "Amy's worries manifested itself into her act. [s] realized the need for reassurance."
    s "Stop worrying so much, this feels great. No man will ever complain about having his dick sucked no matter the experience of the performer."
    s "You have to feel sexy when you're doing it. If you act like it's a chore, it will suck all of the excitement out of it."
    "Amy muffled back a few ahuh's at her coach as she slowly began taking in more and more of his member."
    s "Look your husband in the eyes when you suck his cock. Your mouth is full, so tell him with your eyes how much you enjoy having your mouth fucked."
    scene amy_coffee22
    s "Tell me, do you enjoy getting your mouth fucked?"
    a "Mmhmm."
    a "(This talk is so disgusting and vulgar....yet why am I so wet?"
    s "When your husband comes home from work, you'll be waiting on your knees at the door like a good wife, right?"
    a "Mhmmmm!"
    s "When he pulls your sexy new panties to the side and slides two fingers in, you'll already be wet wishing it was his cock."
    a "Mmm.....mmmhhmmm."
    "Amy closed her eyes, she was lost in this exciting new fantasy. Her pace subconsciously quickened as her lipstick worked like a high-striker, marking new records along the shaft."
    scene amy_bj1_anim
    with fade
    "It wasn't long before her head was bobbing up and down with purpose. Her hand gripped the parts of [s]'s cock that her mouth wouldn't reach."
    "[s]'s breath began to shorten as he was quickly approaching orgasm."
    s "... and when he finally enters you with his cock, you'll be thinking of me. Thinking of how lucky you are to listen to my advice. How lucky you are to practice on me."
    a "Mmmm-yeshh."
    s "Once your husband is done fucking you and pushes you down onto your knees, he'll shove his cock that's covered in your juices, back down your throat."
    s "He'll hold you down by the back of your head till you're gasping for air."
    s "Then he'll say the two words that you've been hungrily waiting for this entire time."
    s "I'M COMING!"
    "[s] gripped Amy by the back of the head as hot cum filled her mouth. She lapped it up desperately, carefully trying not to spill a single drop."
    "Amy's own body shuttered as climax washed over her."
    scene amy_coffee23
    "Out of breath, with a few rogue drops of cum leaking down her face and chest, Amy looks up at [s] with fierce passion in her eyes."
    s "That was fantastic Amy. Look how well you made me cum."
    "Amy took a moment to catch her breath before responding."
    a "(Did I really cum while sucking some guy's dick? What the hell is wrong with me?)"
    a "You came so much...I can't believe I swallowed it."
    s "I can't believe it either, you handled it like a pro."
    a "I used to think that blowjobs were so disgusting...but I actually enjoyed this."
    "Amy quickly realized what she had just said and horror washed over her."
    a "I-uh- I mean I think I will actually really enjoy giving them to my husband."
    s "He's going to be a very lucky man."
    s "Now let's get you cleaned up a bit and go pay up front."
    "Amy decided to purchase both the top and panties after all, excited by the prospects they may bring. With only a short walk back to the coffee shop, they said their goodbyes and parted ways."
    $ amy_bj1 = True
    $ pass_time(120)
    jump loc_coffee

### GYM
label gym_closed:
    scene gym_reception
    "The Gym is open from 6am - 12am"
    jump map_label

# AMY
label amy_gym_locker:
    $ amy_locker_room = True
    if Mamy and lick_amy:
        scene amy_locker1
        s "Hey Amy!"
        scene amy_locker3
        "Amy relaxed upon realizing it was [s], unconsciously brushing her hair behind her ear."
        a "Oh, hey [s]. You startled me."
        s "Everything good?"
        a "Yeah, just freshening up a bit. I'll talk to you later."
        jump loc_gym_locker
    elif Mamy:
        scene amy_locker1
        s "Hey Amy!"
        a "[s]! I'm changing!"
        s "That's ok, I just wanted to talk."
        scene amy_locker2
        a "No... I'm not comfortable with this.."
        s "(Unfortunately she isn't completely relaxed around me yet.)"
        s "No worries, I'll catch you some other time."
        "Content under development"
        jump loc_gym_locker
    else:
        scene amy_locker_hotbutton
        s "(Someone's changing in here. I should probably leave before they get mad.)"
        jump loc_gym_gym

label amy_gym_stretch:
    scene amy_gym_stretch1
    $ amy_gym_stretch = True
    menu:
        "Chat":
            if Mamy & lick_amy:
                s "Hey Amy, ready for another round of training?"
                scene amy_gym_stretch3
                a "Sure. I uh... really enjoyed our last workout"
                scene amy_gym_stretch4
                s "You look real comfortable with these stretches now."
                scene amy_gym_stretch5
                a "This was the one part I was always good at, remember?"
                s "Ahuh, down on the floor we go."
                scene amy_gym_stretch6
                a "Sir, yes sir!"
                scene amy_gym_stretch7
                "A few minutes passed by and Amy started to look exhausted."
                scene amy_gym_stretch8
                s "Ok, I think you've had enough."
                a "Pffft, I hardly broke a sweat."
                s "The yoga room should be available again, let's go."
                scene amy_gym_stretch10
                "[s] and Amy found their way back to their usual spot."
                s "Your form is looking real good!"
                a "Thanks, it still feels tight but it's a lot easier now."
                scene amy_gym_stretch11
                s "Your butt seems to be tightening up a bit too."
                scene amy_gym_stretch10
                a "Really? I should have started doing this so much sooner."
                scene amy_gym_stretch12
                a "Oh no, not again!"
                s "Boob popped out?"
                scene amy_gym_stretch13
                a "Yeah, I really need to get a better fitting top."
                s "Agreed, in the meantime take it off and let's continue."
                scene amy_gym_stretch16
                a "*sigh*"
                scene amy_gym_stretch17
                s "(Wow, no resistance this time.)"
                scene amy_gym_stretch19
                a "(I wonder if this will end like last time.)"
                s "Lay down."
                scene amy_gym_stretch20
                s "(I still can't believe that this is my fucking job.)"
                "Amy closed her eyes. A lone moan escaped her lips."
                s "Ok, time for you to get on top."
                scene amy_gym_stretch21
                s "(I just want to burry my face in those tits.)"
                scene amy_gym_stretch22
                a "(Why I can't stop thinking about what he did to me last time.)"
                a "Umm...[s]. Can we take a break? My lower back is um.. hurting again."
                s "Of course. Let's take a look."
                scene amy_gym_stretch23
                "Amy bent over with anticipation."
                scene amy_gym_stretch24
                s "Your lower back muscles and upper glutes are still extremely tight."
                scene amy_gym_stretch27
                s "Do you masturbate often? This tension is not good for you."
                scene amy_gym_stretch31
                a "*Mmmm* I- don't masturbate."
                scene amy_gym_stretch28
                s "(Wow, she's dripping wet already)"
                s "Well you need to find more opportunities to orgasm throughout the week. You don't want to be a hunchback in 10 years do you?"
                scene amy_gym_stretch31
                a "..no... of course not."
                a "(...please let me feel his tongue.)"
                scene amy_gym_stretch29
                s "Well you're nice and wet already."
                scene amy_gym_stretch30
                s "You know your pussy is actually really tight, especially considering that you're a mother."
                scene amy_gym_stretch31
                a "Th-thanks...*mmm*"
                a "(THANKS?? I'm being finger banged by my gym instructor who's vulgarly describing my vagina and all I can say is 'thanks'?!)"
                a "(What sort of parent am I?)"
                scene amy_gym_stretch32
                "Not able to resist any longer, [s] gave Amy's pretty pussy another taste."
                scene amy_gym_stretch33
                s "*lick* Your husband *slurp* really needs to step up and *lick* eat your pussy."
                scene amy_gym_stretch31
                a "*Mhmm*"
                scene amy_gym_stretch33
                s "Do I *slurp* need to eat- *lick* your pussy everyday?"
                scene amy_gym_stretch34
                "Just the thought of being eaten out by her instructor daily sent Amy over the edge."
                a "I'm going to-"
                a "I..."
                a "Ahhhhhh."
                scene amy_gym_stretch35
                "Amy collapsed onto the ground, panting heavily trying to regain her composure."
                s "You doing ok?"
                scene amy_gym_stretch36
                a "Yeah.....just catching my breath."
                s "Does your back feel better?"
                a "..it does."
                scene amy_gym_stretch37
                s "If your husband doesn't step up and take care of you, I'll be here for you."
                a "Thank you [s]... I'm not really comfortable with all this but I really appreciate you looking out for me."
                scene amy_gym_stretch38
                s "(Well she seems to be comfortable enough sitting completely naked in front of me.)"
                s "That's what I'm here for. If you ever need a partner to help you stretch or need tension relief, let me know."
                $ Oamy += 1
                $ Lamy += 1
                $ pass_time(180)
                jump loc_gym_yoga
            elif amy_sauna1:
                s "Hey Amy, ready for another round of training?"
                scene amy_gym_stretch3
                a "Sure. It's not like I was planning on walking tomorrow anyways."
                s "The yoga room is available right now. I think we should move there to avoid the chance of falling and hitting some of this equipment."
                a "Ok, why not."
                scene amy_gym_stretch9
                s "Plenty of room here for us to work with. Pick whichever mat calls out to you."
                a "Ha! That one in the corner is whispering 'Amyyyyyy.' Can't you hear it?"
                s "I'm hearing it say 'baayyybyyy'. I think it's mocking you!"
                a "Pffft. I'll show him."
                scene amy_gym_stretch10
                a "Oooh... this position is totally kicking my butt."
                s "You're doing great! Just try to keep this position as long as you can."
                scene amy_gym_stretch11
                s "(So that I could examine your body some more)"
                s "So Amy, tell me a bit about yourself. Are you attending the university here?"
                scene amy_gym_stretch10
                a "Haha, you're funny kid. I can almost remember college. I'm an old lady now. Kids, husband, the whole 9 yards."
                s "Wow, that's amazing. Your husband is very lucky to have such a beautiful wife who's in great shape."
                a "Yeah...he's thrilled to have a hag like me."
                scene amy_gym_stretch11
                "Amy started to lose her balance. As she tried to stabilize, her breast popped out of her top."
                a "Oh my God...STOP!"
                a "Let me go!"
                scene amy_gym_stretch12
                s "What happened?"
                a "My breast slipped out..."
                s "So...?"
                scene amy_gym_stretch13
                a "What do you mean so!? My breast slipped out, it's embarrassing!"
                s "You have nothing to be embarrassed about. So what that a little skin was shown? You have a beautiful figure."
                a "You're just saying that because you haven't seen my saggy breasts and stretch marks."
                scene amy_gym_stretch15
                "Tears began swelling in Amy's eyes."
                a "You have no idea what a disgusting toll children take on your body."
                s "Amy, you are stunning and have a beautiful body. Do you think that I'm a liar?"
                a "I....no."
                s "So then you believe me when I say you have nothing to be embarrassed of, right?"
                a "I'm sorry, it's just hard to believe that when your own husband says otherwise."
                s "Your husband says that you're not attractive?"
                a "He says I'm not the same woman that he married. That I used to be a tight little bombshell and now I'm nothing more than a crater."
                s "I'm sorry to say this, but your husband is a fucking idiot."
                s "Now are we going to keep talking about this idiot, or should we continue with the exercises?"
                a "I guess you're right..."
                s "Now take off your top. I don't know why you're wearing such loose clothing to the gym, but it's only going to constrain your stretches and get in the way."
                s "(I really have no idea how this will end. I'm guessing with a sneaker up my ass.)"
                scene amy_gym_stretch14
                a "What!? You want me to work out topless?"
                s "Yes, for three reasons. You're beautiful and have nothing to be ashamed of."
                s "That top is loose and will just get in the way."
                s "And I'm gay... so this is no different than you in the locker room with your girls."
                " Amy sat quietly for what seemed like far too long."
                scene amy_gym_stretch16
                a "*sigh* Fine...just try not to throw up."
                scene amy_gym_stretch17
                s "(She did it, she fucking did it!)"
                s "(Why the hell did I never get into sales? I'd be making a killing!)"
                scene amy_gym_stretch18
                s "Why are you covering yourself?"
                a "I...."
                s "Amy. PUT. DOWN. YOUR. ARMS!"
                scene amy_gym_stretch19
                "Amy's eyes widened with shock, but she reluctantly let her arms fall."
                s "(She seems to respond well to authority. I wonder how that asshole husband really treats her)"
                s "(Either way, I can probably use this to my advantage.)"
                s "There we go. Now we can proceed. Lay down."
                scene amy_gym_stretch20
                s "(Her body does have some mileage but it's still so incredibly sexy.)"
                s "Do you feel that burn in your thighs?"
                "Amy was so embarrassed that she closed her eyes to avoid direct eye-contact."
                a "Mmmmmhmmm..."
                s "Great. Now I'll lay down and you get on top of me, kind of like a 69. I'll hold your legs up and you hold on to mine."
                s "This will strengthen both your arms and abs."
                scene amy_gym_stretch21
                "Amy did as she was told, reluctantly but with little objection."
                s "(I just want to burry my face in those tits.)"
                scene amy_gym_stretch22
                a "Umm...[s]. Can we take a break? My lower back is hurting."
                s "Of course, we don't want you injured. Get up and let me take a look."
                scene amy_gym_stretch23
                s "Does it hurt when you're bend over like that?"
                a "A little, but not like before."
                scene amy_gym_stretch24
                s "I think your lower back muscles and upper glutes are extremely tight. They're pulling on your spine."
                scene amy_gym_stretch27
                s "Yup. Your muscles here are extremely tight. I'm going to remove your shorts so I have better access to your glutes."
                scene amy_gym_stretch31
                a "(Am I really going to let him take off my clothes like this?)"
                scene amy_gym_stretch28
                s "(Wow, what a pretty little pussy. Hard to imagine that she's had kids.)"
                s "Amy, you are ridiculously tight down here."
                s "When is the last time you had an orgasm?"
                scene amy_gym_stretch25
                a "What the hell kind of question is that?! That's not very appropriate!"
                scene amy_gym_stretch29
                s "I ask because I think I know what's causing you back pain (Other than those huge tits of course)."
                s "(She's not running away screaming, maybe she finds this exciting?)"
                s "If your husband is not giving your body the attention it deserves, you may have a lot of pent-up stress and tension down here."
                s "This will spread to your lower back, causing the pain and discomfort you've already experienced."
                scene amy_gym_stretch30
                s "This is exactly what I'm going to help you relieve today."
                s "(She's already wet enough for me to easily slide a finger in. This is definitely exciting for her too.)"
                scene amy_gym_stretch31
                a "(Oh my God...he's fingering me. Why is he fingering me? Why am I letting him..)"
                a "(It feels so good though... maybe just for a little bit.)"
                scene amy_gym_stretch32
                "Not able to resist any longer, [s] gave Amy's pretty pussy a taste."
                scene amy_gym_stretch33
                s "*lick* Does- *slurp* your husband *lick* ever eat your pussy?"
                scene amy_gym_stretch31
                a "*Mhmm* no."
                s "What a shame. He needs to know that his lack of attention is causing health problems."
                scene amy_gym_stretch33
                "Conversation became difficult to maintain as [s] continued to eat out Amy."
                scene amy_gym_stretch34
                a "I'm going to-"
                a "I..."
                a "Ahhhhhh."
                scene amy_gym_stretch35
                "Amy collapsed onto the ground, panting heavily trying to regain her composure."
                s "You doing ok?"
                scene amy_gym_stretch36
                a "Yeah.....just catching my breath."
                s "Does your back feel better?"
                a "Actually..it does."
                scene amy_gym_stretch37
                s "When a person orgasms, every muscle in their body contracts and releases. It's a great way to relieve of tight knots and sore spots."
                a "I can't believe you just did that to me..."
                a "What if my husband finds out? He'll kill you!"
                s "He won't find out if you don't tell him. I'm just trying to relieve you of your pain and paving the way for a healthier future."
                a "Thank you [s]. I don't know what you did to me, but my back is feeling better already."
                scene amy_gym_stretch38
                s "(She's seems to be comfortable sitting completely naked in front of me. I wonder if the orgasm lowered her defenses.)"
                s "That's what I'm here for. If you ever need a partner to help you stretch or need tension relief, don't be shy and let me know."
                s "I'm a health professional, that's why they pay me the big bucks."
                s "(Barely above minimum wage, but at least the benefits are starting to look great.)"
                $ lick_amy = True
                $ pass_time(180)
                jump loc_gym_yoga

            elif Mamy and not amy_sauna1:
                s "Hey Amy, ready for another round of training?"
                scene amy_gym_stretch3
                a "You betchya!"
                scene amy_gym_stretch4
                s "Great, looks like you already remember some of the routine."
                scene amy_gym_stretch5
                a "I remember it because I'm so good at this part."
                s "Oh, confident are we? I think it's time to kick your butt with sit-ups."
                scene amy_gym_stretch6
                a "*Umfff* I knew I should have kept my mouth shut."
                scene amy_gym_stretch7
                s "(Hello again ladies! I pray that this is the only top she owns.)"
                "A few minutes passed by and Amy started to look exhausted."
                scene amy_gym_stretch8
                s "Ok, I think you've had enough."
                s "If you found this routine helpful, I can show you some more two person exercises."
                a "Oh my God...you mean you have additional ways of torturing me?"
                s "No pain no gain, sweetheart!"
                $ pass_time(180)
                jump loc_gym_gym
            else:
                scene amy_gym_stretch1
                s "(Who's this sexy redhead?)"
                "[s] watched the woman stretch for a while until she noticed him."
                scene amy_gym_stretch2
                who "You know... I joined this gym so I wouldn't have to deal with guys staring at me."
                "(Damn. I guess I was just kind of standing around staring at her..)"
                s "I'm so sorry, I didn't mean to disturb you. My name is [s] and I'm the new personal trainer here."
                s "I was just observing you stretch because I think I can show you a more effective way of doing it."
                scene amy_gym_stretch3
                who "Oh! Daisy told me about you, it must have slipped my mind."
                who "I'm sorry...my name's Amy by the way."
                s "Nice to meet you Amy. Looks like you're working on your core and legs. Mind if I help you?"
                a "Umm... sure. What do I do?"
                s "Stand up and give me your leg. We'll give your thighs a nice deep burn."
                scene amy_gym_stretch4
                s "Perfect. Now try to reach your toes if you can. Don't push yourself if it hurts."
                scene amy_gym_stretch5
                a "Ha. That's no problem."
                s "Wow, you're already pretty flexible. Awesome!"
                s "(I wonder what else she can do with her body)"
                scene amy_gym_stretch6
                s "Now lay down on the mat. I'll hold your legs down and you do sit-ups."
                scene amy_gym_stretch7
                "As Amy did her sit-ups, her top crept higher and higher up her chest. Exposing her large...tracts of land."
                s "(Thank you God for creating large breasts and small tops)"
                a "Wow! It's so much harder to do when you're being held down like this."
                scene amy_gym_stretch8
                s "Definitely. You probably feel a good burn in your abs now huh?"
                s "(I definitely feel something burning down below as well)"
                a "*Panting* Uh... Yea... this is quite the workout."
                "Amy followed directions obediently for what must have been her first real workout"
                scene amy_gym_stretch7
                s "Good work Amy, I think that's enough for today."
                a "Thank God, I don't think I could have done another sit-up."
                s "(She's smoking hot. I can't wait to work with her again.)"
                $ Mamy = True
                $ pass_time(180)
                jump loc_gym_gym

        "Leave":
            s "(I've got other things to do.)"
            jump loc_gym_gym

label amy_sauna1:
    hide screen ui_icons
    hide screen ui_text
    scene amy_sauna1
    "[s] quickly changed out of his clothes and wrapped a complimentary towel around his waist."
    "As he entered the sauna, he discovered Amy was resting against a wall. The light rising of her chest signaled she was asleep."
    s "(Jackpot. That ginger fox looks to be naked under her towel.)"
    "[s] moved to take a seat near her."
    scene amy_sauna2
    s "(Damn, I just want to run my hands up and down her body.)"
    scene amy_sauna3
    s "(Holy shit, I can see her pussy!)"
    "[s]'s clunky movements woke Amy unexpectedly."
    scene amy_sauna4
    a "Ahh!"
    s "I'm so sorry Amy, I didn't mean to wake you."
    a "Oh it's ok, I was just startled."
    scene amy_sauna5
    "Becoming aware of her compromising position, Amy shuffled her weight to try and cover herself up."
    s "I didn't mean to make you uncomfortable."
    s "Should I leave?"
    scene amy_sauna6
    a "No, it's not you specifically who's making me uncomfortable. I'm just uncomfortable with my body in general."
    a "I'm not as young as I used to be."
    scene amy_sauna7
    s "Hi 'ImnotasyoungasIusedtobe', I'm [s]."
    scene amy_sauna8
    "Amy giggled at the joke, despite it being both lame and unoriginal."
    a "Did you really just pull a dad joke?"
    s "Sorry, I panicked."
    s "Seriously though, you've got nothing to be shy about. The whole point of this gym is to work out and get in better shape."
    s "If you already had the body you are dreaming of, then why come here? You'd be done."
    s "I'd make you a graduation cap and everything."
    a "*Giggles* I guess you're sort of right. Still, I get a little self conscious with all these younger girls running around."
    s "All I know is that you look great."
    "The compliments seemed genuine and Amy began to let down her guard."
    "Fortunately for [s], this created an opportunity for the fabric to find it's freedom."
    scene amy_sauna9
    "No sooner had the towel fallen to reveal her breast had Amy snatched it back up, covering herself tightly."
    scene amy_sauna10
    a "Oh my God, that didn't just happen."
    s "Oh come on, it's just a boob."
    "Amy sat in silence. [s] was uncertain if it was the heat of the sauna or her embarrassment that was further reddened her face."
    s "Ah come on Amy, seriously it's not a big deal."
    s "In Scandinavian countries, men and women share a steam room in the nude."
    s "You're making too big of a deal of it."
    a "Sorry... I'm just embarrassed."
    s "(Hmmmm, I've got an idea. Maybe if I take off my towel she'll realize that nudity isn't a big deal?)"
    menu:
        "Take off your towel (Harvey Weinstein approves)":
            s "It's ok, I understand."
            s "Maybe this will level the playing field."
            "[s] removed his towel, exposing himself to Amy."
            a "(Hmm?)"
            scene amy_sauna11
            a "(Oh my God, he took off his towel!)"
            a "(I can see his penis.)"
            scene amy_sauna12
            s "See, it's no problem."
            a "Oh... "
            scene amy_sauna13
            a "I swear I didn't see anything!"
            s "It's ok if you did. That's the whole point."
            s "We have to be comfortable in our own skin, you know?"
            "Panic swept over Amy as this experience was too much for her to handle."
            scene amy_sauna14
            a "Thanks for chatting with me, but I've gotta run!"
            s "You don't have t-"
            a "See you later [s]!"
            s "(Damn... maybe I was a little to aggressive there.)"
            s "(I hope I didn't ruin my chances with her.)"
            $ amy_sauna1 = True
            $ pass_time(120)
            jump loc_gym_sauna

        "That's some Bill Cosby shit, better just play it cool man":
            s "That's ok, we don't have to talk about it anymore if you don't want to."
            a "Thank you."
            s "I noticed you were taking a nap earlier in here, do you not get enough sleep at night?"
            a "Not really, lately things have been pretty hectic at home."
            s "Hectic in a good way I hope?"
            a "Something like that... "
            scene black
            with fade
            "[s] and Amy continued chatting for a few more minutes."
            scene amy_sauna14
            a "It's been nice talking to you [s], but I've got to get going."
            s "No problem, see you tomorrow."
            $ amy_sauna1 = True
            $ pass_time(120)
            jump loc_gym_sauna

label amy_yoga:
    $ amy_yoga = True
    hide screen ui_icons
    hide screen ui_text
    if amy_bj1 and amy_yoga_topless:
        scene amy_yoga_eventnude1
        "Amy sat alone on a yoga mat topless, lost in concentration."
        scene amy_yoga_eventnude2
        s "Great, she listened to my advice and dropped the top."
        s "Hey, Amy. You need help again?"
        scene amy_yoga_eventnude3
        a "Hey, I'd love your help."
        scene amy_yoga_eventnude4
        a "It's the same stretch as last time."
        s "Of course, I can do that."
        scene amy_yoga_eventnude5
        a "Just hold down my legs so I don't lift my feet off the ground."
        s "(It's hard to concentrate when you're looking at those bad boys.)"
        scene amy_yoga_event7
        a "That felt pretty great. Now on to the next one."
        scene amy_yoga_event8
        a "Push down on the back of my thighs. I won't tell you to stop until I feel a burn."
        s "I know, I know."
        scene amy_yoga_event9
        a "(I really need to find a new stretch. This is pure torture having his cock so close to me.)"
        a "(He ate me out, I sucked him off. Surely a little penetration won't make a difference?)"
        a "(No, get a grip on yourself. You don't want to cross that line.)"
        a "(Shit, I'm getting wet again. I need to stop this before he notices.)"
        a "Ok, that's enough."
        scene amy_yoga_event10
        s "Did you feel the burn?"
        a "Yeah, I definitely felt it burning down there."
        a "Thanks for your help again, that's the end of the routine for me."
        $ amy_yoga_topless2 = True
        $ pass_time(120)
        jump loc_gym_yoga

    else:
        scene amy_yoga_event1
        "Amy sat alone on a yoga mat, lost in concentration."
        scene amy_yoga_event2
        s "(Looks like she's taking this stuff more seriously now.)"
        s "Hey, Amy."
        scene amy_yoga_event3
        a "Oh, hey [s]. I didn't hear you come in."
        s "Yeah, I thought I saw someone head in here earlier so I wanted to check in."
        a "I'm just practicing yoga. The stretches you taught me were great, but now I need to work on clearing my mind too."
        s "Getting rid of bad vibes and voodoo I assume?"
        a "Haha, something like that."
        scene amy_yoga_event4
        a "Hey... this is perfect timing. I could use your help."
        s "That's what I'm here for."
        a "This next stretch is so a lot easier with two people."
        scene amy_yoga_event5
        a "Just hold down my legs so I don't lift my feet off the ground."
        "Amy's top slipped, revealing her breasts... again."
        s "Hey... I'm not complaining but your tits are out again."
        scene amy_yoga_event6
        a "Ugh, why do I even bother with this top?"
        s "More like, why do you even bother being dressed in here? No one comes here but you."
        scene amy_yoga_event7
        a "I know but I can't just run around naked."
        s "No one's talking about you running around naked... just stretch naked instead."
        a "Very funny, now help me out here."
        scene amy_yoga_event8
        a "Push down on the back of my thighs. I won't tell you to stop until I feel a burn."
        s "You're the boss."
        scene amy_yoga_event9
        a "(Mmm... this position is pretty hot. His cock is only inches away from entering me.)"
        a "(Stop it Amy, you're a married woman. You can't entertain thoughts like that.)"
        a "(I wonder how it'd feel though... I don't even remember what another man feels like... or my own for that matter.)"
        a "(Gosh, I'm getting wet. I need to stop this before he notices.)"
        a "Ok, that's enough."
        scene amy_yoga_event10
        s "Did you feel the burn?"
        a "Yeah, something like that."
        a "Thanks for your help again, that's the end of the routine for me. (I wonder where I hid my pink best friend all those years ago?)"
        $ amy_yoga_topless = True
        $ pass_time(120)
        jump loc_gym_yoga

label amy_daisy_yoga1:
    hide screen ui_icons
    hide screen ui_text
    scene amy_daisy_yoga_event1
    "Amy wasn't doing her yoga routine as usual, instead she was resting on a nearby bench."
    s "Hey Amy, why are you just sitting there?"
    a "I'm just thinking about... stuff."
    s "Wasn't that the whole point of all this, to clear your head?"
    a "Yeah, I guess so."
    s "... husband?"
    a "Yup..."
    scene amy_daisy_yoga_event2
    a "It's just so frustrating!"
    a "I'm doing this all for him. Getting into shape, trying new things in the bedroom."
    a "Not once has he noticed or mentioned my progress."
    s "Maybe he's just a busy man and needs a small smack to the head before he pays attention?"
    a "Ha, busy... that's what he always says. 'I'm so busy, I don't have time for this nonsense.'"
    a "'We can't fool around tonight honey, I got a busy day tomorrow and need my sleep'."
    a "Have you ever heard of such a busy dentist? It's not like he's on call for the ER at a hospital."
    scene amy_daisy_yoga_event3
    a "Maybe he just doesn't find me attractive anymore and there doesn't seem to be anything I could do about that."
    scene amy_daisy_yoga_event4
    s "Amy, I've told you a million times already that you're drop dead gorgeous."
    s "You are one of the sexiest women I've known."
    s "Some men see art when they look at a Rolls Royce, others see just a car."
    a "Thanks [s], but I think a rusty hatchback is a better description."
    scene amy_daisy_yoga_event5
    "Daisy entered the room before the conversation got too depressing."
    ds "I heard you fools do yoga in here."
    ds "Jenna says she'll cover the reception area for only 15 minutes, let's do this."
    scene amy_daisy_yoga_event6
    a "Daisy... are you ok? You look a little..."
    scene amy_daisy_yoga_event7
    s "Stoned. You look absolutely stoned out of your mind."
    scene amy_daisy_yoga_event5
    ds "What are you talking about? I don't do that kind of thing."
    scene amy_daisy_yoga_event7
    s "You sure? Your eyes are bloodshot red."
    scene amy_daisy_yoga_event5
    ds "I think I would remember what I put into my body, ok?"
    ds "All I had today was cereal and a teeeny weeeny bit of some delicious brownies my roommate baked."
    ds "Can you believe her? She bakes brownies and tells me I can't have any. Some people..."
    scene amy_daisy_yoga_event7
    s "I can't believe it... Daisy ate pot brownies."
    scene amy_daisy_yoga_event8
    ds "Whatever... are you two assholes going to just stand around there or are we going to do some fucking yoga!?"
    scene amy_daisy_yoga_event9
    s "Holy shit are you seeing this? Stoned Daisy is an absolute lunatic!"
    scene amy_daisy_yoga_event10
    a "Ok, Daisy. You can try to do our routine with us. Just copy what I'm doing."
    ds "Like this?"
    scene amy_daisy_yoga_event11
    s "Almost. You're doing a pretty good job, just need to arch your back a little more."
    a "(Why is [s] paying so much attention to her?)"
    scene amy_daisy_yoga_event12
    a "Hey [s], can you help me out too? Is my pose right?"
    s "Yes it looks great. We've practiced this many times already."
    a "Are you sure? Do I have enough arch in my lower back?"
    s "Yeah, you look great."
    a "(Whatever... )"
    a "Ok, let's move on to the next position."
    scene amy_daisy_yoga_event13
    a "Try to keep your feet and butt on the mat at all times."
    scene amy_daisy_yoga_event14
    a "(Does he like her?)"
    a "(What am I even thinking, he's gay why would he even like either of us?)"
    a "(But still... he's paying all of his attention on her!)"
    scene amy_daisy_yoga_event15
    a "(This should help remind him as to why I'm his favorite.)"
    scene amy_daisy_yoga_event16
    ds "Ummm... why is Amy taking off her top?"
    scene amy_daisy_yoga_event17
    a "Huh? Oh my, how silly of me. I didn't realize I was doing that."
    a "I'm so used to doing this routine with my top off because the fabric restricts my movement and gets in the way."
    a "Oh my... how embarrassing."
    scene amy_daisy_yoga_event18
    ds "Ooohhh, that makes sense. [s] do you mind if I do that too?"
    s "Do whatever you're comfortable with."
    scene amy_daisy_yoga_event19
    ds "You're right Amy, it feels so much easier this way. How's my form now?"
    scene amy_daisy_yoga_event20
    a "(That shady little bitch... )"
    ds "Can you push a little harder? I'm not feeling a burn or anything yet!"
    a "(Push harder? I need to get rid of you fast.)"
    scene amy_daisy_yoga_event21
    "Amy suddenly dropped to the floor howling in pain."
    a "Owww, my back!"
    scene amy_daisy_yoga_event22
    ds "Oh my gawd, Amy! Are you okay?"
    scene amy_daisy_yoga_event23
    s "It's your lower back again right?"
    a "Mmmm... yes. Looks like my muscles spasmed... I think I'll be okay."
    scene amy_daisy_yoga_event24
    ds "Are you sure you'll be ok? I can go run and grab some ice or something."
    a "No that's ok, thank you."
    ds "Ok, looks like [s] will take care of you. I need to run back to my desk before Jenna gets mad."
    ds "Thanks for the yoga lesson."
    scene amy_daisy_yoga_event25
    a "Help me up please."
    s "Are you sure? You should probably lay down for a while. I can give you a massage."
    a "No, that's ok. You're always giving me massages, it's time I be a good friend and give you one instead."
    s "But I'm not sore."
    scene amy_daisy_yoga_event26
    a "You're not, but this guy down here must be. Poor thing's been straining against your shorts ever since Daisy took her top off."
    s "That's not true, he was doing that long before her."
    scene amy_daisy_yoga_event27
    "Amy ripped off [s]'s shorts and wrapped her hand around his member."
    a "That's ok, I understand. Men get turned on by younger women."
    scene amy_daisy_yoga_event28
    a "My breasts aren't perky like hers anymore. They're old and saggy."
    s "(What the fuck has gotten into her... is she jealous?)"
    s "I love your tits. Their the tits of a real woman."
    a "Is that true, do they turn you on?"
    s "Very much so."
    scene amy_daisy_yoga_event29
    a "Does it turn you on when I wrap them around your cock?"
    s "(Did I accidentally eat a pot brownie myself? When the hell did Amy start talking so dirty?)"
    a "Does it turn you on when I rub them up and down your shaft?"
    s "*Groan*"
    scene amy_daisy_yoga_event30
    a "I'll take that for a yes."
    a "Do you like it when an old hag like me milks your cock with her old saggy tits?"
    scene amy_daisy_yoga_event31
    a "I'm starting to think that you're just a dirty pervert."
    a "Why else would you be so hard for me, when there's plenty of tight young bodies running around here."
    scene amy_daisy_yoga_event32
    a "I'm down on my knees working your cock with my tits, like the dirty old hag I am."
    a "You must really be a pervert to get turned on by this."
    a "What sort of gay men gets this hard from such nasty tits."
    a "Are you even gay? Or do you just fuck anything that moves."
    a "You must have really low standards... "
    scene amy_daisy_yoga_event33
    s "*Groans* Amy..."
    a "You're going to cum soon aren't you?"
    a "Then cum for me. Cover me with your seed. It's not like I'll get any filthier than I already am."
    a "Is a garbage can ever clean, no matter how many times you wash it?"
    a "Cum on me, cum on your garbage can."
    "Hearing Amy talk so dirty was too much to bear, [s]'s orgasm made his knees tremble as he tried his hardest to not fall right on top of her."
    s "Amy... I'm-"
    scene amy_daisy_yoga_event34
    "Shot after shot fired onto Amy. Most of it was directed at her chest but some made its way onto her hair and face."
    a "How do I look? Like a filthy old hag covered in cum?"
    "Slowly regaining his composure, [s] knew he needed to nip this before Amy completely spiraled downwards."
    s "No, you look beautiful as you always have."
    s "Your problems with your husband are obviously taking a toll on your mental health. Please Amy, I'm here if you need to talk."
    s "You're my friend, you're beautiful, and I want to help."
    a "What's the point? I don't deserve your friendship."
    "Tears swelled up in her face as she got up and ran away."
    s "(That was one of the sexiest things I've been a part of.)"
    s "(Yet why do I feel so bad? Wasn't that always part of the plan?)"
    s "(Rape and pillage just like Long John Genghis Khan.)"
    s "(Amy really deserves better though. I need to figure out how I can help her.)"
    $ amy_titjob1 = True
    $ pass_time(120)
    jump loc_gym_yoga

label amy_sad_event1:
    $ amy_coffee = False
    hide screen ui_icons
    hide screen ui_text
    scene amy_sad_event1
    s "(There she is.)"
    scene amy_sad_event2
    s "Hey Amy, why the long face?"
    scene amy_sad_event3
    a "Hey... it's nothing. I'm just thinking about things."
    s "I wanted to talk to you about what happened earlier... how you ran out after our yoga... session."
    scene amy_sad_event4
    a "Don't worry, that was just a silly little outburst. It won't happen again."
    scene amy_sad_event5
    s "It wasn't an outburst though, was it?"
    s "It's something that's been bothering you for a while."
    a "I just... sometimes feel like my husband is repulsed by me and there's nothing I can do about it."
    scene amy_sad_event6
    a "No matter what I do, he acts like I'm disgusting."
    menu:
        "Comfort Her":
            scene amy_sad_event6
            s "Amy, your husband is an idiot. I'm sorry to say that."
            s "No heterosexual man would find you anything but attractive."
            s "In fact, maybe I should try to seduce your husband and see if he bites."
            scene amy_sad_event7h
            a "Ha, I wouldn't be surprised if he finds you sexy like I do..."
            s "You find me sexy?"
            scene amy_sad_event8h
            a "I mean... you're in great shape and look nice."
            s "The same thing can be said about you though."
            s "You've given birth to two kids and yet you still have a killer body."
            s "Plus, you look nice too."
            scene amy_sad_event9h
            a "Thank you [s]. That means a lot to me."
            s "No need to thank me. You're a great person and I enjoy spending time with you."
            scene amy_sad_event10h
            "Amy began sobbing as she embraced [s] tightly."
            s "You sure you're doing ok?"
            a "I'm sorry... I just needed to hear that."
            scene amy_sad_event11h
            a "Thanks for cheering me up. I'm glad I met you."
            s "I'm glad I met you too, beautiful."
            $ amy_love += 1
            $ amy_sad_event1 = True
            $ pass_time(60)
            jump loc_gym_pool

        "Take Advantage":
            scene amy_sad_event6
            s "So what if he's disgusted by you? His opinion doesn't matter."
            s "What kind of man looks at a dirty slut and gets repulsed?"
            scene amy_sad_event7s
            a "What are you saying?"
            s "I'm calling you a nasty slut. You tried to play the role of a good mother and wife, but you can't keep the truth hidden forever."
            s "You're just a dirty slut who loves being treated like one, don't deny it."
            scene amy_sad_event8s
            a "Look [s], I know I said some things earlier that I shouldn't have, but I don't appreciate you talking to me like that right now."
            s "Don't lie to yourself. You can pretend to be offended all you want, but that's not going to phase me."
            s "Look at yourself now, sticking your chest out at me, playing with your hair."
            s "Do you expect me to believe that you're insulted rather than turned on?"
            scene amy_sad_event9s
            a "[s] you're being so rude... I don- I don't like the way you're treating me."
            s "Yet here you are squirming in front of me."
            s "Don't tell me that it didn't turn you on the way I used your body."
            s "You were practically gushing when you wrapped your saggy tits around my cock."
            a "That's not fair... I wasn't being myself."
            s "Oh you were being yourself alright, you were finally being the real you, even if for a moment."
            s "Here you are crying about how your husband doesn't treat you right, but I know the truth of it."
            a "And what truth is that?"
            s "You're crying because your husband won't bend you over, fuck you and fill you full of cum like you want him to."
            s "You're crying because you're a nasty old cum bucket that hasn't been filled in years."
            scene amy_sad_event10s
            "Something snapped within Amy. She stopped sobbing and slowly looked up with an intense gaze."
            a "Let me guess, you want to be the one to fill my bucket?"
            a "You want to bend me over and spank me, pull my hair, and tell me what a dirty little bitch I am?"
            scene amy_sad_event11s
            a "You want to rip my shorts off and take me right here in public, because you're just a dirty little pervert."
            scene amy_sad_event12s
            a "If I bend over like this, would you be able to control yourself?"
            scene amy_sad_event13s
            a "Would you shove your cock in me and mark me as yours?"
            scene amy_sad_event14s
            a "Would it help if I pulled these down?"
            a "My loose old pussy is on display, what are you going to do about it?"
            scene amy_sad_event15s
            a "Nothing, because just like my husband you're not man enough to take what you want."
            a ".. or are you?"
            scene amy_sad_event16s
            "The doors to the pool swung open as Dani waltzed in at the most inopportune moment."
            dn "Hey Hikari, you in h-"
            scene amy_sad_event17s
            dn "What the fuck?"
            dn "I am NOT okay with this, damnnit!"
            scene amy_sad_event18s
            "Dani practically ran out of the room, trying her best to unsee things."
            scene amy_sad_event19s
            a "Well, looks like we'll never find out just how much of a dirty pervert you really are."
            s "Don't count on it. I'll see you around Amy. Glad you're feeling better."
            $ amy_slut += 1
            $ amy_sad_event1 = True
            $ pass_time(60)
            jump loc_gym_pool

label amy_sophie_date1:
    hide screen ui_icons
    hide screen ui_text
    scene amy_sophie_date1
    s "(Looks like I'm a little late, Sophie's already cleaning up her plate.)"
    scene amy_sophie_date2
    s "(Either her ass grew or that shirt got smaller.)"
    s "(I love that she's comfortable enough around me to be in her panties like that.)"
    scene amy_sophie_date3
    s "Good morning donkey."
    so "Morning sleepy bum."
    s "So did you grow overnight or did your shirt shrink?"
    scene amy_sophie_date4
    so "There is a itty bitty small chance that my shirt shrank in the wash."
    s "Maybe your butt just got bigger?"
    so "Tisk tisk, talking about your cousins ass. Have you no shame?"
    s "But you're a donkey, so technically you ARE an ass."
    scene amy_sophie_date5
    so "Well aren't you quick on your feet. You should have gone into politics."
    s "That's true... I mean I DO love fucking people."
    s "By the way, I want to meet your lover boy. We should do something."
    so "I don't know... I don't want you seducing him away from me."
    s "I'll try my best not to. How about tonight? We can go bowling or something."
    so "You really want to be the third wheel?"
    s "I mean, I can always bring someone too you know... I have friends."
    scene amy_sophie_date6
    so "It's settled then. We'll go bowling tonight so I can show you and your 'friend' who's in charge."
    s "It ain't the dentist, that's for sure."
    so "*Laughing* At least try to be nice to him tonight."
    scene black
    "Some time passed before [s] stumbled upon Amy getting ready to take a shower."
    scene amy_sophie_date7
    s "(I won't ever get tired of seeing her MILF body.)"
    s "Hey Amy!"
    scene amy_sophie_date8
    "Amy turned around with a startled look on her face."
    a "Oh it's you, [s]. Gave me a little scare for a second there."
    s "What, did you think it was some creepy pervert hanging around the locker room?"
    scene amy_sophie_date9
    "Amy smirks"
    a "Maybe I still think that."
    s "Well would a creepy pervert invite you to go bowling tonight?"
    a "Really? Just the two of us?"
    s "Well no, my cousin Sophie and the guy she's seeing will be there as well."
    s "Come with me so we can kick their ass."
    scene amy_sophie_date10
    a "Mmm, when you put it that way... sure I'll come."
    s "Great, I'll text you my address so you can pick me up."
    a "You really need to buy a car."
    s "No need when I can have pretty girls drive me around instead."
    scene black
    "Amy pulled up to [s]'s place later that evening."
    scene amy_sophie_date11
    s "A MILF in a bug? I was half expecting a mini-van."
    scene amy_sophie_date12
    a "Naw, this girl rides in style!"
    a "Now hop in before I change my mind and make you walk."
    scene black
    "The car filled with the sounds of mediocre 90's boy bands as Amy sang along."
    "Not a moment too soon did they arrive at their destination."
    scene amy_sophie_date13
    with fade
    "The two entered a bowling alley, deserted aside from Sophie and what appeared to be her date."
    "Amy took a few steps through the door before her body froze completely."
    scene amy_sophie_date14
    a "... I-"
    s "Something wrong?"
    a "I... I can't."
    s "Amy, what's wrong?"
    a "I'll be in the car."
    "Amy ran outside before [s] could stop her."
    s "(Well that was weird. I better check on her.)"
    scene amy_sophie_date15
    s "I didn't know monkeys could look so pretty in dresses."
    so "Ha, you made it."
    so "[s], this is Walter."
    so "Walter, this butthead is my cousin [s]."
    w "Pleasure to meet you, champ."
    s "(Champ? I don't like him already.)"
    s "I'm sorry for doing this, but my date just had an emergency and ran out the door."
    scene amy_sophie_date16
    so "Oh no, is she ok?"
    s "I have no idea. I'm going to go check on her."
    s "I apologize ahead of time if we don't end up coming back today."
    so "That's ok [s], go on and make sure she's ok."
    s "(Is Walter trying to hide his laughter from me? Fuck you, Walter.)"
    scene amy_sophie_date17
    with fade
    "[s] found Amy sitting in her car, sobbing against the steering wheel."
    scene amy_sophie_date18
    s "Hey Amy... you ok?"
    scene amy_sophie_date19
    a "Stupid... stupid... stupid..."
    s "Who's stupid?"
    scene amy_sophie_date20
    a "I'M stupid for thinking I could make that pig love me again."
    s "Amy, wha-"
    "A light went off in [s]'s head. Amy did mention that her husband was a dentist and Sophie mentioned the same for her date."
    s "Your husband's name is Walter, isn't it?"
    scene amy_sophie_date21
    a "Does she know?"
    s "Sophie? Are you asking if she know that he's married?"
    a "Does she?"
    s "No, she wouldn't be seeing him if she knew. She's not that kind of girl, trust me on this."
    scene amy_sophie_date19
    a "What was I thinking? Did I really believe that I could compete with those gorgeous young girls?"
    a "What kind of woman am I that I can't even keep my own husband interested in me?"
    s "Amy, you're no-"
    a "I'm just a washed up old hag, he was right all along."
    menu:
        "Comfort Her":
            scene amy_sophie_date19
            s "You're not a washed up old hag. You're a beautiful wife and a loving mother."
            s "Despite him being an ungrateful little shithead, you still went out of your way to get in shape for him."
            s "You went out of your way to pleasure him and spice up your romance."
            scene amy_sophie_date22h
            a "*Sniff* Is that really what you think of me?"
            s "Every word of it."
            s "If that asshole can't see that then he deserves to die alone."
            scene amy_sophie_date23h
            "Amy suddenly moved forward and kissed [s] on the lips."
            "The kiss began as an act of innocence and comfort, but it wasn't long before passion took over and her tongue found its way into his mouth."
            scene amy_sophie_date24
            a "There's one thing you left out when describing me..."
            "[s] raised an eyebrow in silence."
            a "You forget that I am also a dirty little slut that deserves to be treated as such."
            scene amy_sophie_date25
            a "I need my filthy old body used."
            a "No one but the nastiest of perverts would want my saggy tits."
            scene amy_sophie_date26
            a "Only a disgusting man would fuck this loose pussy."
            scene amy_sophie_date27
            a "Only someone with no shame or self respect would fuck such a repulsive cunt..."
            scene amy_sophie_date28
            a "... and I think that shameless person is you, [s]."
            s "Are you sure you want to do this? You're obviously very upset right now..."
            a "I've been wanting to fuck you for a long time. I've held back because I'm married."
            a "Now seeing that this pig has been fucking around behind my back all along..."
            a "Fuck me now, [s]."
            scene amy_sophie_date29
            "[s] wasted no time as he shed his pants and positioned behind Amy."
            scene amy_sophie_date30
            "Her pussy was already soaking wet. All it took was one thrust to enter her."
            scene amy_sophie_date31
            a "Oh my GOD!"
            "Amy moaned uncontrollably like a sex depraved nympho."
            "The little car was quickly filled with the sounds of low moaning and skin slapping against skin."
            a "Fuck me from behind and spank me. I deserve to be punished."
            jump amy_sex1_anim
            $ amy_love += 1

        "Take Advantage":
            scene amy_sophie_date19
            s "Shut up already."
            scene amy_sophie_date22s
            a "... what?"
            s "I said quit your whining."
            s "I'm tired of your self pity. So what if you're a washed up old hag?"
            s "Even old hags can be good little sluts."
            a "[s] now's not the time t-"
            s "I said shut up."
            s "You may not be as young and as sexy as some other girls, but you are still a sexy old hag."
            s "Men would kill each other for a chance to spank your fat ass and grab those saggy tits."
            scene amy_sophie_date22h
            a "Yes... yes, they would... wouldn't they?"
            s "Let me see those disgusting floppy tits."
            scene amy_sophie_date24
            a "Are these what you wanted to see?"
            s "Absolutely disgusting. Won't be long now before they touch your knees."
            s "Now let's see that loose old pussy of yours."
            scene amy_sophie_date25
            "Amy did as she was told, trying her best to hide the smirk on her face."
            scene amy_sophie_date26
            a "Are you sure you want to see my dirty loose pussy?"
            s "On your knees."
            scene amy_sophie_date27
            s "Look at you, bent over naked in the middle of a parking lot."
            s "Have you no shame? Exposing your body for everyone to see."
            scene amy_sophie_date28
            a "I have no shame at all. I'm a dirty old slut that needs to be punished."
            scene amy_sophie_date29
            "[s] wasted no time as he shed his pants and positioned behind Amy."
            scene amy_sophie_date30
            "Her pussy was already soaking wet. All it took was one thrust to enter her."
            scene amy_sophie_date31
            a "Mmmmmmmm, fuck my dirty pussy."
            a "It's been so long since anyone's fucked me."
            a "I've been so bad for so long and no one's punished me for it."
            $ amy_slut += 1
            jump amy_sex1_anim

label amy_sex1_anim:
    scene amy_sophie_date32
    menu:
        "Front View":
            scene amy_sex_face_anim
            with fade
            $renpy.pause()
            jump amy_sex1_anim

        "Rear View":
            scene amy_sex_rear_anim
            with fade
            $renpy.pause()
            jump amy_sex1_anim

        "Cum":
            scene amy_sophie_date33
            a "I'm gonna-"
            "Amy let out a long piercing scream."
            "[s] feared that someone in the parking lot would hear them."
            jump amy_sex1_cum

label amy_sex1_cum:
    menu:
        "Cum inside of her":
            scene amy_sophie_date38
            "Amy's quivering pussy was too much for [s]. He grabbed her hips firmly as he climaxed deep inside her."
            "Amy's pussy walls began contracting and releasing rapidly, milking every ounce of cum he had to offer."
            "Semen began leaking out of her pussy, making its way down her legs and onto the seat."
            scene amy_sophie_date35
            a "Well... I don't think my back's going to hurt for a while."
            s "After a performance like that, it better not."
            a "I can't believe you came in me."
            s "What good is a cum dumpster if it can't take a load?"
            "The two got dressed and sat in relative silence, absorbing the events of that night as Amy drove [s] back home."
            scene amy_sophie_date36
            s "You still look sad... did we take it too far?"
            scene amy_sophie_date37
            a "No, what we did was perfect. I'm just thinking about that asshole and what I'm going to do with him."
            s "Are you going to file for divorce?"
            scene amy_sophie_date36
            a "I don't know... as much as I hate him I don't know what the divorce would do to the kids."
            s "So you're just going to ignore the issues in your marriage and let him get away with what he's been doing?"
            a "No, I will make him pay. I just need to figure out how."
            s "We'll come up with something. That asshole doesn't deserve you."
            scene amy_sophie_date37
            a "Thank you [s], thank you for everything."
            s "We'll figure this out, don't worry."
            s "Don't let him know that you know, we have the element of surprise."
            a "I'll do whatever you say. Good night [s]."
            $ amy_sex1 = True
            $ amy_sex1_cum = True
            $ pass_time(900)
            jump loc_sophie

        "Cum on her back":
            scene amy_sophie_date34
            "[s] pulled out and emptied load after load onto Amy's ass and back."
            "The two were frozen in their current position desperately gasping for breath as semen began leaking down Amy's legs and pussy."
            scene amy_sophie_date35
            a "Well... I don't think my back's going to hurt for a while."
            s "After a performance like that, it better not."
            "The two got dressed and sat in relative silence, absorbing the events of that night as Amy drove [s] back home."
            scene amy_sophie_date36
            s "You still look sad... did we take it too far?"
            scene amy_sophie_date37
            a "No, what we did was perfect. I'm just thinking about that asshole and what I'm going to do."
            s "Are you going to file for divorce?"
            scene amy_sophie_date36
            a "I don't know... as much as I hate him I don't know what the divorce would do to the kids."
            s "So you're just going to ignore the issues in your marriage and let him get away with what he's been doing?"
            a "No, I will make him pay. I just need to figure out how."
            s "We'll come up with something. That asshole doesn't deserve you."
            scene amy_sophie_date37
            a "Thank you [s], thank you for everything."
            s "We'll figure this out, don't worry."
            s "Don't let him know that you know, we have the element of surprise."
            a "I'll do whatever you say. Good night [s]."
            $ amy_sex1 = True
            $ pass_time(900)
            jump loc_sophie

label amy_plan:
    hide screen ui_icons
    hide screen ui_text
    scene amy_plan1
    with fade
    ds "[s], there you are!"
    ds "Amy’s been looking for you. I think I saw her head off towards the sauna."
    s "Great, thanks for the heads up."
    scene amy_plan2
    with fade
    s "(Where is she?"
    scene amy_plan3
    s "(I must have missed her, maybe she’s working out?)"
    scene amy_plan4
    a "Nice of you to finally show up."
    s "Wow, you’re stunning! I hope you greet me this way more often."
    a "Did you miss your dirty old cum dumpster?"
    s "You can say that again."
    a "I don’t know if I believe you."
    a "Let’s see if you’re an honest boy and telling the truth."
    scene amy_plan5
    with fade
    a "Hmmm… doesn’t look like you miss me all that much."
    scene amy_plan6
    a "Let’s make an honest man out of you."
    scene amy_plan7
    a "You're finally starting to miss me."
    scene amy_plan_bj_anim
    with fade
    s "Finally, a lie detector test that I can get behind."
    scene amy_plan8
    with fade
    $renpy.pause(2)
    scene amy_plan9
    with fade
    a "You got that right."
    scene amy_plan10
    with fade
    a "Come here and let’s get the truth out of you."
    scene amy_plan11
    a "Fill my loose dirty pussy."
    s "Maybe I’ve changed my mind."
    s "Come to think of it, I could go for a latte right about now."
    a "Quit teasing, I need you inside me… {i}NOW{/i}!"
    scene amy_plan_sex_anim
    with fade
    a "{i}Mmmm{/i} fuck!"
    a "Tell me what a dirty, worthless whore I am."
    s "You’re {i}my{/i} dirty whore!"
    a "Th-that’s right… no one else wants this loose pussy."
    a "Only you’re depraved enough to own it."
    s "Turn around."
    a "W-what?"
    s "I want to look my slut in the eyes when I cum in her."
    scene amy_plan_sex2_anim
    with fade
    s "Your husband will soon know that you belong to me."
    a "Yes… yes! Fill me with your cum."
    a "Mark me as your property!"
    scene amy_plan12
    with fade
    a "{i}*Panting*{/i} you can use me whenever you want."
    a "Ride me into the ground until my old body gives out."
    a "Fill me with your delicious cum whenever you desire."
    scene amy_plan13
    with fade
    $ renpy.pause(1)
    s "You’re disgusting… and incredible."
    s "If I was your husband, I’d drench your pretty face in cum every night before you go to sleep."
    scene amy_plan14
    with fade
    a "Unfortunately, the only thing my husband drenches me in is sweat and farts."
    s "You deserve better, Amy."
    s "Does he have any idea that you know what he’s been up to?"
    a "I don’t think so. I haven’t said anything and nothing’s changed."
    a "He still ignores me every night and casually mocks me whenever he gets the chance."
    s "Have you thought about leaving him?"
    a "Of course I have… but how can I?"
    a "He’s the one who makes the money. Plus, I don’t want to put our kids through a messy divorce."
    s "So you’re just going to live through your misery and pretend everything’s ok?"
    scene amy_plan15
    a "No, I want to make that son of a bitch pay!"
    a "... I just don’t know how."
    s "I’m sure we can think of something."
    s "If he’s going around cheating on his wife I’m sure there’s some sort of dirt you can dig up on him?"
    a "I don’t know… he’s been pretty good at keeping me in the dark about most things."
    s "Snoop around, check his phone, emails, work bag. I’m sure you’ll find something of use."
    scene amy_plan16
    a "What if I fuck up and ruin everything?"
    a "I’m not really good at anything, [s]. I’m not like you."
    menu:
        "Kiss her":
            scene amy_plan17
            with fade
            $renpy.pause(1)
            scene amy_plan18
            a "Wow… what was that for?"
            s "Look Amy, you may be my dirty little fuckbag, but you’re also an incredible woman."
            s "Just because your husband treats you like you’re worthless doesn’t make it true."
            s "I know you’ll be able to handle this, I’m not asking you to do anything I don’t think you’re capable of."
            s "If you don’t want to do it, then that’s fine. But if you’re just too {i}scared{/i} to do it, then we have a problem."
            s "So which is it?"
            $ amy_love += 1

        "Push her to do it":
            s "Look, I don’t really care about your excuses."
            scene amy_plan19
            a "[s]...?"
            s "Your husband has been a shitbag to you {i}and{/i} he’s been a shitbag to Sophie."
            s "So either you find some dirt on him, or I’ll end up simply breaking his legs anyways."
            a "I don't know if I can handle it."
            s "You can and you will, because it's the only way to take back control of your life."
            a "..."
            $ amy_slut += 1

    scene amy_plan20
    a "I’ll do it... "
    a "I’ll find something!"
    s "I have no doubts that you’ll figure it out."
    s "Let me know when you find something."
    s "In the meantime, I think it’s best we get out of here before someone catches us."
    $ amy_plan = True
    $ amy_event = False
    $ pass_time(120)
    show screen amy_timer
    jump loc_gym_sauna

label amy_recon:
    hide screen ui_icons
    hide screen ui_text
    scene amy_recon1
    with fade
    a "[s], I’ve been looking for you!"
    s "What’s up?"
    a "I did it!"
    s "What?"
    a "I found dirt on that pig."
    a "He’s royally fucked!"
    s "I knew you could do it. Now give me the deets."
    scene amy_recon2
    s "Holy shit! Is he fucking his patients?"
    a "Worse, he molests them while they’re unconscious."
    s "How do you know?"
    a "I went through his phone while he was showering."
    a "He has a bunch of these photos."
    a "Who knows how long that bastard’s been doing this?"
    s "I’m sorry, Amy. It must have been hard looking at them."
    scene amy_recon3
    a "I don’t care about him… fuck that bastard."
    a "It’s not like it hurts knowing that your husband would rather rape a passed out meat bag rather than his own willing wife."
    s "Do you want to talk about it?"
    scene amy_recon4
    a "..."
    scene amy_recon5
    a "What’s the plan now?"
    s "Send me everything you have."
    s "You can now confront him and blackmail him into doing anything you want."
    a "So I can finally force him to sleep with his own wife?"
    s "Yeah… I guess."
    a "I’m just kidding. I belong to you now… not that dirt bag."
    s "Figure out what you want out of this marriage, or if you even want one at all."
    s "You now have leverage to shape your life however you want."
    s "With this evidence, we can send him to prison for 20 years if that’s what you want."
    s "He no longer really has a say in anything."
    a "I’ll think about it."
    scene amy_recon6
    a "Will you be with me when I tell him?"
    a "I don’t think I have the strength to do it without you…"
    s "Of course, I’ll be right there with you. You know that."
    s "Just give me a heads-up if he’s packing heat."
    a "Huh?"
    s "Guns… does he own guns?"
    scene amy_recon7
    a "Ha! What makes you think he’d own a gun?"
    s "When I saw him, he had dog tags. Thought that maybe he served?"
    a "He probably just bought those from a vending machine."
    s "So not a tough guy, huh?"
    a "Yeah, he’s a dentist by day and bouncer by night."
    s "I don’t really know what I was thinking."
    a "You’ll find out for yourself soon enough."
    a "How about dinner Friday night? Swing by the house and the three of us will figure it out."
    s "Sure, just text me when and where."
    a "..."
    s "What? Why are you looking at me like that?"
    a "Did I not do a good job getting dirt on that dimwit?"
    s "You sure did."
    scene amy_recon8
    with fade
    a "So don’t I deserve a reward?"
    s "You sure do."
    "You walk up behind Amy and throw her down onto the bench."
    scene amy_recon9
    s "My little slut wants her reward?"
    a "Yes!"
    a "Please reward your dirty little slut."
    scene amy_recon10
    with fade
    a "{i}Huh{/i}... wrong port, sailor."
    "You prep Amy’s asshole by spitting on it."
    a "WAIT!"
    a "[s], I’ve never done it there!"
    s "Does my slut not want her reward?"
    a "..."
    a "... please be gentle."
    scene amy_recon11
    a "{i}Ahhhhhhh!{/i}"
    a "It hurts!"
    s "Do you want me to stop?"
    a "{i}Ahh{/i}… no."
    scene amy_recon12
    s "Do you like getting your asshole stretched by my cock?"
    a "{i}Oww{/i}... {i}oww{/i}... {i}oww{/i}."
    "You increase your intensity causing a loud smack with each thrust."
    scene amy_recon13
    a "{i}Ahhhhhhh!{/i}"
    s "Doesn’t sound like you’re enjoying this… maybe I should stop."
    a "DON’T YOU FUCKING DARE!"
    a "My little asshole is {i}ahh{/i} yours to destroy."
    scene amy_recon14_2
    s "My whore loves her reward."
    a "... yes!"
    s "Do you want me to fill your tight little asshole with my cum?"
    a "I’m cu-u… {i}Ahhhhhhh{/i}!"
    "The sounds of Amy completely lost in ecstasy is enough to drive you over the edge."
    scene amy_recon14
    "You feel her tight asshole squeeze around your cock as her body shakes in orgasm, milking every last drop."
    scene amy_recon15
    with fade
    a "That was... {i}(panting){/i}."
    a "... that was amazing."
    s "Glad you enjoyed your reward."
    s "You should probably get cleaned up before someone sees you laying in a pool of cum."
    a "{i}Mmmm{/i}... can’t wait to see you Friday night."
    $ amy_recon = True
    $ pass_time(60)
    jump loc_gym_locker

label amy_dinner:
    hide screen ui_icons
    hide screen ui_text
    scene amy_dinner1
    with fade
    a "[s], you came!"
    s "Were you starting to doubt me?"
    a "No… I don’t know."
    a "I’m just really nervous about the whole thing."
    s "Don’t worry, I’ll be right here with you."
    a "I know… everything will be ok."
    s "Are your kids here?"
    a "No, they’re having a sleepover at a friends house."
    s "Perfect. Look here, everything is going to work out."
    a "{i}(Deep breath){/i}"
    a "Let’s do this!"
    a "HONEY, [s]’s here!"
    scene amy_dinner2
    with fade
    w "The hell are you wearing?"
    w "Are you trying to make our guest lose his appetite?"
    a "No… I’m just-"
    s "Hi Walter, it’s nice to finally meet you."
    w "Likewise, I apologize for that, [s]."
    w "Sometimes my wife forgets to dress her age."
    s "That’s alright, I think she looks fine in that."
    w "Take a look at this guy here with the heart of gold!"
    s "You guys have a lovely home."
    w "It’s not too shabby, eh?"
    w "Come on, I’ll give you a tour after we eat."
    scene amy_dinner3
    with fade
    w "Bring us whiskey, baby. Something off the top shelf."
    a "Did you have something particular in mind?"
    w "Didn’t you hear me? I said just bring something off the top shelf."
    w "If it’s whiskey and it’s on the highest shelf... bring it."
    w "I hope that wasn’t too confusing for you."
    a "... yes, dear."
    scene amy_dinner4
    w "I’m going to introduce you to the finer things in life, [s]."
    w "Tonight we drink like kings!"
    s "Beautiful home, beautiful wife, I haven’t met your kids yet but I’m sure they’re amazing as well."
    w "Well you got two out of three right."
    w "You know how women are. They dress all sexy, tits that defy gravity and asses so tight that you could bounce quarters off of em."
    w "Then the moment you get married and have kids, it all goes down the drain."
    w "‘But you don’t know what childbirth does to your body’, bah, excuses."
    s "That seems like a pretty rude thing to say about your wife in front of guests."
    w "Eh, she knows I’m just kidding."
    w "Right, hun?"
    a "... yes, love."
    w "See it’s fine."
    w "But good thing you’re here, maybe you’ll be able to whip her ass into shape soon enough."
    scene amy_dinner5
    a "Here you go, [s]."
    s "Thank you, Amy."
    w "Wait till you get a sip of this, I want to see your face when that God’s nectar touches your lips."
    scene amy_dinner6
    s "{i}Sips{/i}"
    w "Well? Isn’t that the greatest thing you’ve ever tasted?"
    s "Hmmm, this stuff is amazing."
    s "Glenmorangie, right?"
    s "It’s not my absolute favorite but it’s definitely up there."
    w "W-wha... Glenmorangie? Argh Amy, you grabbed the wrong bottle!"
    w "I’m sorry [s], she must have not reached high enough."
    a "I got your favorite bottle…"
    w "Pffft, like you know."
    w "Women like to pretend they know everything, right [s]?"
    scene amy_dinner7
    with fade
    s "S-sure."
    w "Haha, I like you. A man of class like me."
    w "I’m surprised Amy invited you here for dinner. She should be worried that you’ll try to steal me from her."
    w "Hahaha."
    a "Oh no! [s] please respect this house and don’t try to seduce my husband."
    s "I’ll do my best."
    w "If only you understood the basics, dear."
    w "Take all these empty glasses away. We’re starting to look like alcoholics."
    scene amy_dinner8
    with fade
    a "Oops!"
    w "Haha, what a clutz!"
    w "How do you even manage to train her? I’m surprised she hasn’t dropped a dumbbell on your foot yet."
    scene amy_dinner9
    with fade
    s "She’s actually pretty damn {i}ahh{/i}!"
    w "What’s wrong with you?"
    s "Sorry, had a sharp pain in my side. It’s gone now."
    s "So uh, she’s pretty damn motivated and… {i}uh{/i} focused at the gym."
    w "Well that’s a first."
    s "Ye-yeah she’s following my instructions with no hesitation."
    scene amy_dinner10
    with fade
    s "I know I can sometimes be a mouthful, but she swallows everything I throw at her."
    w "Maybe something will come of her yet."
    w "Speaking of which, did you fall asleep down there?"
    scene amy_dinner11
    with fade
    a "Found it, it rolled away."
    w "Where’s the food, woman?"
    a "It’s still cooking!"
    w "{i}(Sigh){/i} This is what I deal with everyday."
    w "I work all day and then come home to my second job as a supervisor."
    s "Sounds rough. Hey, you’re a military guy though, it’s nothing you cant handle."
    w "Military?"
    w "Oh right, yeah they took us in as boys and spit us out as men."
    w "They worked our asses off, a lesson that Amy needs to learn."
    w "Maybe then she'd get in shape."
    s "Hey Amy, come here for a second."
    scene amy_dinner12
    with fade
    s "Have you seen her stomach lately?"
    s "Look how much she’s slimmed down."
    w "Ha, you call that slim? You should have seen her 15 years ago!"
    w "She had washboard abs. That little pudge is no comparison."
    a "I gave birth to your children! What did you expect?"
    w "Here we go again with the excuses."
    s "Come on Walt, you can’t expect her to look like she’s 20 again."
    s "It’s not like you look like the same as the day you got married."
    w "Hey, I work all day! It’s understandable if I gain a couple of pounds."
    w "She sits at home all day on her fat ass, it’s inexcusable!"
    s "I’m not sure what fat ass he’s talking about."
    s "I must be remembering things differently."
    scene amy_dinner13
    s "Let’s get these pants off you."
    w "What the fuck?!"
    w "What do you think you’re doing?"
    s "Relax, I’m just giving you my professional opinion."
    w "Amy, don’t you dare!"
    scene amy_dinner14
    with fade
    s "How can you say anything bad about this ass?"
    s "Look how firm yet plump it is?"
    w "Why the fuck aren’t you wearing underwear!?"
    s "We quickly found out that her panties got in the way of our exercises, so she’s been going commando ever since."
    s "Ain’t that right, Amy?"
    a "Yup! Our time spent together was much better without silly panties getting in the way."
    scene amy_dinner15
    w "You’re fucking dead!"
    w "How dare you put your fucking hands on my wife!?"
    s "You sound upset."
    s "I think you should sit down."
    w "Don’t tell me what to do, I’m going to beat that smug grin off your face."
    s "No you won’t, Walt."
    s "I will fuck you in the ass till you love me, faggot."
    s "Now…"
    s "There’s no reason we can’t be civilized. Sit down."
    w "I’m going to call the cops."
    s "That’s unfortunate. It will be difficult for you to explain why you’ve been raping women at your clinic."
    scene amy_dinner16
    w "What!?"
    w "What the fuck did you say?"
    s "We know everything."
    s "Every slimy little disgusting thing that you’ve done, we know."
    w "I don’t know what you’re talking about."
    s "Really? Should I show you the photos now or wait for the police to show up?"
    w "..."
    w "What the fuck do you want?"
    s "First I’d like for you to sit down."
    scene amy_dinner17
    s "Very good."
    s "Now I wasn’t done explaining your wife’s progress to you."
    s "We’ve been focusing on her core strength and legs, allowing her to slim down her figure."
    s "However, there’s nothing I can do about her tits."
    scene amy_dinner18
    s "Because frankly, they’re absolutely perfect the way they are."
    s "Do you even remember how they feel?"
    s "Probably not, you’ve really been letting her down lately."
    w "{i}(muttering){/i} You son of a bitch…"
    s "Now that’s not a very nice thing to say."
    s "I’m just trying to be helpful here."
    s "When’s the last time you fucked your wife?"
    s "..."
    s "I asked you a question."
    w "I don’t know… it’s been a while."
    s "Sounds like you don’t know how to handle a real woman in bed."
    s "Are you worried that you won’t be able to please a woman with experience?"
    w "What? No, you little shit."
    s "I think you are. Maybe that’s why you keep going after younger women."
    s "Or women who are unconscious."
    s "Hard to disappoint someone who isn’t even awake."
    s "But I get the feeling that you still end up disappointing them somehow."
    scene amy_dinner19
    with fade
    s "Don’t worry though, I’ll show you how it’s done."
    w "Fuck you, you stu-"
    s "SILENCE!"
    s "It’s rude to talk during a lecture."
    s "If you want your woman to have pleasure, you need to stimulate both her body and mind."
    s "Foreplay is very important… I hope you’re taking notes."
    s "Amy, my dear. You’re naked and on display over a table, how does that make you feel?"
    a "Like a dirty little slut!"
    s "Atta girl! Now can you tell your husband who you belong to?"
    a "I belong to [s]!"
    s "And what do you want me to do with your dirty little pussy?"
    a "I want you to fuck me with that cock of yours."
    a "I want you to fill be with your hot cum."
    s "You see, Walt? A little foreplay and she’s begging to be fucked into next Thursday."
    s "No need to gas her and put her to sleep."
    w "Fuck this, I’m out of here."
    s "YOU SIT THE FUCK DOWN!"
    s "You will watch me fuck your wife, making her cum like you were never able to."
    s "It’s too late for second chances, but maybe you’ll learn a thing or two."
    w "{i}Argh{/i} You son of a bitch!"
    w "Who do you think you are?"
    w "I have friends in the military who owe me favors, you’re dead!"
    a "Shut the fuck up, Walt. No one’s scared of your friends from the cart at the mall where you bought those cheap dog tags."
    w "Why you little bit-"
    s "One more word and I will report you to the cops and fuck your wife anyway."
    scene amy_dinner20
    a "{i}Ohhhh{/i}"
    s "I barely even stuck my cock in her and she’s already moaning like a common whore."
    s "You see how much a little foreplay does?"
    scene amy_dinner_sex_anim
    with fade
    a "{i}Mmm{/i} Fuck your dirty little cum dumpster."
    a "Your cock is so much bigger than my husbands."
    w "Hey!"
    s "Shut the fuck up Walt! Don’t ruin the mood with your nasally voice."
    a "I’m almost there…"
    a "Tell Walt to shut up again."
    s "Looks like you’re going to get involved in this after all."
    s "Just not the way you wanted."
    s "You slimy ugly motherfucker."
    w "How d-"
    s "SHUT THE FUCK UP WALT!"
    s "Real dog tags aren’t covered in chrome paint, you douchebag."
    a "I’m gon- I’m cu… {i}Ahhhhh{/i}!"
    s "Look at your wife, Walt. No shame at all, this one."
    s "Just came on the dinner table while getting fucked by another man."
    s "The same table you eat off of."
    a "Cum in me, [s]."
    a "I need to feel your hot cum in me right now!"
    s "No."
    a "What!?"
    scene amy_dinner22
    a "I won’t cum unless Walt tells me to."
    w "Are you out of your fucking mind!?"
    a "Walt, you son of a bitch. Tell [s] you want him to cum in my pussy."
    w "I’m not fucking saying that!"
    a "Say it, or I tell the police everything."
    w "You wouldn’t dare throw your own husband in prison."
    w "Leave our kids without a father."
    a "Only reason you’re not in prison now IS because of our kids."
    a "But if you don’t listen to me from now on, I swear to God I will make sure you rot in a cell for the rest of your life."
    a "Tell [s] to cum in me… NOW!"
    w "..."
    w "You can cum."
    s "What’s that, did you say something?"
    w "I said you can cum in my wife…"
    s "I can’t hear you."
    w "CUM IN MY FUCKING WIFE!"
    w "Are you fucking happy now?"
    scene amy_dinner23
    with fade
    w "What the hell are you thinking, Amy?"
    w "What if you get pregnant?"
    s "You seem to be doing pretty well for yourself. I think you can handle a third child."
    w "You’re fucking sick!"
    s "Says the guy who drugs and rapes women."
    scene amy_dinner24
    s "Speaking of which, here’s the deal."
    s "We won’t report your slimy evil ass to the cops."
    w "Thank y-"
    s "But…"
    s "You have to install cameras in every one of your rooms at the clinic."
    s "Amy will have access to the stream. If you get frisky with another client again, deal's off."
    s "If the feed, for whatever reason, fails to display even for 5 minutes, deal’s off."
    s "Amy is now your captain. She says jump-"
    w "{i}(Sigh){/i} I say how high?"
    s "No, you jump you fucking idiot."
    s "You’re not allowed to lay one finger on her."
    s "She’s mine now, you’ve lost your chance."
    s "And if you even think of doing something stupid like trying to get us killed…"
    s "... I’ve already written into my will to have your photos released."
    s "Don’t be an asshole and don’t go drugging women and you’ll be fine… think you will manage?"
    w "{i}(Sigh){/i} Yes…"
    s "Good, then we have a deal."
    s "Oh, before I forget. I’m also taking a spare key to the house."
    w "No fucking way, my kids live here!"
    s "Don’t worry, I’m not a sick fuck like you."
    s "I’ll only use the key to come fuck your wife when your kids are asleep."
    s "Yeah?"
    w "{i}(Grumbling){/i}"
    s "Good."
    s "Abide by the rules and you can live your life however you want."
    s "Go meet women, go wear tacky dog tags, whatever you want, champ."
    scene amy_dinner25
    a "I’m sorry, Walt. That was really harsh what we just put you through."
    w "You think?"
    a "I think you deserve your wife’s touch one last time, for old times’ sake."
    a "Let me help you out of those."
    scene amy_dinner26
    with fade
    a "Would you look at that? He’s rock hard."
    s "Ha, do you enjoy watching your wife get fucked by another man?"
    s "I didn’t know you were into that."
    w "No… I didn’t enjoy that…"
    scene amy_dinner27
    with hpunch
    a "Good, because you’re never going to enjoy me again."
    w "{i}OWWWWW{/i}"
    a "This is for all the pain and emotional abuse you’ve caused me over the years."
    s "That’s enough, Amy. We crushed his spirit, let his balls go."
    s  "Walt, get out of here."
    w "Where am I supposed to go?"
    s "Your room, outside, I don’t care. I just don’t want to look at your face while I’m eating."
    w "..."
    s "Wait... one more thing."
    s "If you ever talk or so much as look at Sophie again."
    s "I will personally come and crush your little grapes myself."
    w "Sophie?"
    w "How do you know about Sophie?"
    s "You don’t remember me, do you?"
    w ".... no?"
    s "Well that’s ok, you’ll remember me now."
    scene amy_dinner28
    with fade
    a "I can’t believe that just happened!"
    s "How do you feel?"
    a "Exhilarated!"
    a "I feel like a huge stone has been lifted off my chest."
    a "..."
    a "Guilty..."
    a "Don’t get me wrong, he’s an asshole, but he’s still the father of my kids."
    s "It’s okay to feel sorry for him. We did what we had to do to make sure that he knows you’re not bluffing."
    s "You’re free to live your life now."
    scene amy_dinner29
    s "What’s wrong?!"
    a "{i}(Sob){/i} I...I-"
    s "Don’t be sad, Amy. We did what needed doing."
    a "What kind of mother does what I did to her children's father?"
    s "You stood up for yourself."
    a "I laid down to get fucked on the dining room table."
    a "The same table where my boys eat every morning."
    a "How can I look them in the eyes tomorrow knowing that I’m just a disgusting whore?"
    s "Amy, don’t confuse two entirely different things."
    s "First, you’re not wandering the streets looking for dick from strangers."
    s "You’re my woman now, and it’s your right to be fucked however way you want to be fucked."
    s "And second, you’re an amazing mother."
    s "You’ve stayed in a sexless, loveless and downright abusive marriage for how many years now?"
    s "All for the sake of your kids."
    s "Even now, you’re still sharing a bed with that asshole just to create the illusion of stability and family."
    s "You’re a good mother and a strong woman."
    scene amy_dinner30
    a "Thank you , [s]."
    a "Thank you… thank you."
    s  "Of course, beautiful, you know I’m here for you."
    scene amy_dinner31
    a "So… does all this mean that you’re not gay after all?"
    s "..."
    s "Let’s just say I like anal and leave it at that."
    a "{i}Hahaha{/i}"
    scene amy_dinner32
    with fade
    s "Thanks for dinner, it was delicious."
    a "Next time you’re going to be the one taking me out for dinner."
    a "I’ve got an appearance to upkeep. Can’t let people think I’m giving it up for free."
    s "We wouldn’t want people to think that you’re getting railed for anything less than soup and complimentary breadsticks."
    a "{i}Hahaha{/i}"
    a "Thank you [s]."
    a "Thank you for everything."
    s "Good night, Amy. See you soon."
    $ amy_cuck = True
    $ pass_time(300)
    jump loc_sophie

# DANI
label dani_office:
    if fired:
        scene dani_office_chat1
        s "(Doesn't seem like Dani noticed me entering her office)"
        menu:
            "Chat":
                s "Hey Dani."
                scene dani_office_chat5
                "Dani swung around, glaring at [s]."
                dn "I have nothing to say to you, leave my office."
                s "(Ok, she's still pissed.)"
                jump loc_gym_office

            "Leave":
                s "(I'll talk to her later)"
                jump loc_gym_office
    else:
        scene dani_office_chat1
        s "(Doesn't seem like Dani noticed me entering her office)"
        menu:
            "Chat":
                s "Hey Dani."
                scene dani_office_chat2
                dn "Hi [s], I didn't hear you come in. What's up?"
                s "Not much, just thought I'd see how you're doing."
                scene dani_office_chat3
                dn "I'm ok, just trying to get these financial reports done."
                scene dani_office_chat4
                dn "I'm sorry but can we catch up sometime later? I'm pretty swamped right now."
                s "Yeah of course, no problem. I'll see you later."
                jump loc_gym_office

            "Leave":
                s "(I'll talk to her later)"
                jump loc_gym_office

label dani_fired:
    hide screen ui_icons
    hide screen ui_text
    scene dani_fired1
    dn "YOU! Into my office... NOW!"
    s "Uh...is something wr-"
    dn "I SAID NOW!"
    scene dani_fired2
    "Daisy looked down silently, avoiding eye contact and too afraid to say anything."
    scene dani_fired3
    dn "I was this close...THIS CLOSE to believing you."
    dn "Your bullshit story about the gym being a 'safe space' for you. Your bullshit story about respecting the women here."
    dn "You're not even gay. How dare you stoop so low to lie about that!?"
    s "Dani...I'm not sure what you're talking about, but I assure you that I'm gay."
    scene dani_fired4
    dn "Hmmm, let's see. A gay man getting oral sex from women."
    dn "Yeah, that definitely makes sense."
    "[s] was caught off guard. 'Damn, how did she find out,' he thought to himself."
    dn "That's right, I know everything. I overheard Daisy telling her friend about it over the phone."
    s "It's not what you think, I was j-"
    scene dani_fired5
    dn "ENOUGH with your lies!"
    dn "You know damn right what you were doing."
    s "I don't understand, I was just trying t-"
    scene dani_fired6
    dn "Stop. You're done. I'll mail your last paycheck and I don't want to see you around here ever again."
    s "Dan-"
    dn "Out. Get out."
    scene black
    "Later that night."
    scene dani_fired7
    s "(Looks like it's just you and me again, old friend.)"
    "[s] swirled the glass around before lifting it to his lips."
    s "(I had a good run. Pretending to be gay just to fuck everyone at the gym, that idea was insane to begin with.)"
    s "(I should feel lucky to have even gotten so far.)"
    scene dani_fired8
    s "(Now I just need to figure out what I'm going to do moving forward.)"
    s "(Most importantly, how am I going to explain to Sophie that I can't even keep a job?)"
    s "(I don't even want to imagine the disappointed look she'll give me... and rightfully so.)"
    "Lost in thought, sleep overtook him."
    scene black
    "*Bzzzzzzzzt*"
    "..."
    "*Bzzzzzzzzt*"
    scene dani_fired10
    s "(Uh....it's morning. How long was I out?)"
    s "(Looks like I got some texts.)"
    scene dani_fired11
    s "(What the hell does she want from me now?)"
    s "(Did she find out about the others? Could I be in legal trouble?)"
    s "(Shit... shit... shit...)"
    s "(I better go and find out what she wants.)"
    scene black
    "[s] approached Dani's door. As he raised his fist to knock, a cold voice rang out, 'Come in'."
    scene dani_fired12
    "Dani was already sitting at the table. She didn't look happy to see him but her temper seemed under control."
    dn "Please sit down."
    s "Good morning Dani. Why am I here?"
    "Dani looked down and let out long sigh."
    dn "I don't even know where to start to be honest. I don't want you here, I don't even want to look at you."
    dn "I know that Daisy wasn't the only one you abused here."
    s "I didn't abuse anyone."
    dn "When the girls found out that I fired you, some of them stormed my office looking for answers."
    dn "Did you really have sex with Maria?...she's old enough to be your mother for christ's sake!"
    s "I only provided what she both wanted and needed."
    dn "...and did you really eat-... *clears throat*, perform... oral sex on Amy?"
    s "She had severe tension and back pains. Orgasms tighten and then relax every muscle in a human body. I provided relief that she wasn't able to acquire elsewhere."
    scene dani_fired13
    "Dani leaned forward with a piercing gaze."
    dn "Look, don't try to bullshit me again as if you were doing some noble good deed for these girls."
    dn "You are using them for your own sexual perversion and nothing more."
    s "I would have to disagree with you there, Dani."
    s "More importantly, why does any of this matter? You fired me, why am I here?"
    "Frustration swept over Dani's face before her entire body slumped forward in defeat."
    scene dani_fired14
    dn "I don't agree with what you're doing. I think-... no, I know that you're nothing more than a pervert and a womanizer. However..."
    dn "... it seems that none of that matters when it comes to profit."
    dn "We're busier than we've ever been, and some of the girls even threatened to terminate their membership if you weren't brought back."
    dn "I'd love nothing more than to see your sorry ass thrown out into the alley, but the owner has expressed her disapproval with that idea."
    s "(Wait... WHAT!? Am I getting my job back?)"
    scene dani_fired15
    dn "[s], I'm asking you to come back and work here."
    s "I.. um..."
    s "(There's no way I can let this opportunity pass. She just threw everything out on the table and I now have leverage.)"
    s "(I need to use this moment to gain more leniency in the future.)"
    s "Look Dani... I really enjoy working here."
    dn "Well of course you fucking do, you per-"
    "Dani caught herself losing her temper and decided it would be best to hold her tongue."
    s "I also love the girls here. They are wonderful and sweet people. (Except you Jenna, eat a bag of dicks!)"
    s "However, I don't know how I will be able to continue my work if you're going to be constantly hounding and restraining me."
    s "If one of the girls needs something, I will do everything in my power to make it happen."
    scene dani_fired16
    dn "Even now you're still feeding me your bullshit."
    dn "Do you really want me to tell you 'Go ahead, have sex with everyone, I approve!'?"
    s "No. What I want you to say is that you won't interfere with the services I provide the girls."
    s "Just like you said, this place has never been so busy and most importantly. MOST importantly, the girls actually want to come to the gym now."
    scene dani_fired17
    dn "How did I get here, to this low point in my life?"
    dn "Rather than managing a gym, I feel like I'm managing a brothel."
    dn "Rather than providing a safe place for women to work on improving themselves and their bodies, I've allowed a pervert to exploit and use them."
    "After what seemed like an eternity, Dani broke the silence."
    dn "Fine, [s]. Do what you need to do. I will try to not stand in your way."
    dn "But if you dare hurt one of these girls, I will claw your fucking eyes out... do you understand?"
    s "Certainly."
    dn "So you'll come back?"
    s "Starting now."
    "[s] got up and headed towards the door while Dani remained seated, barely supporting the weight of her head in her hands."
    scene black
    with fade
    "Daisy waited outside the office, curious of the outcome of the meeting."
    scene dani_fired18
    ds "She's not letting you come back, right?"
    s "Daisy, actually I-"
    ds "It's all my fault. I'm sorry! Me and my big stupid mouth. If only-"
    s "DAISY! I'm back. Don't worry."
    scene dani_fired19
    ds "Really? Are you messing with me?"
    s "No, I promise. Dani said I can work here again."
    ds "Oh my god, I'm so happy! Sorry for getting you in trouble [s]"
    s "Hey... don't worry about it. It's not your fault."
    a "... [s]?"
    scene dani_fired20
    "Amy and Maria strolled around the corner wearing concerned looks."
    a "What'd Dani say? Is she still mad at you?"
    s "Oh she's mad alright."
    a "So does that mean we won't see you again?"
    s "Only if you don't want to."
    a "Of course I want t-... wait, does that mean you're not fired?"
    s "Not anymore, and it's thanks to you ladies."
    scene dani_fired21
    "The mood instantly lifted as the girls let out a sigh of relief."
    m "Welcome back suga."
    a "YES! I knew she wouldn't be able to keep you away for long!"
    a "You should have heard the beating Maria gave her yesterday."
    m "It was nothing, just a light warning."
    m "Ain't nobody feel the wrath of Mamma Maria and live to talk about it."
    m "Dani should feel herself lucky."
    s "Whatever you girls did, I'm in your debt. Thank you for that."
    a "We're all just glad to have you back."
    m "Well, most of us. Jenna was jumping with joy yesterday, I don't know how she'll be feeling today."
    s "Don't worry about Jenna. I think she likes me, she just doesn't know it yet."
    s "Now that I'm a trainer again, what are you girls doing standing around?"
    s "Let's go, I want to see you sweat!"
    a "*Giggle*"
    a "Yes sir!"
    $ fired = True
    jump loc_gym

label dani_cable:
    hide screen ui_icons
    hide screen ui_text
    scene dani_cable1
    with fade
    s "(What is she doing?)"
    scene dani_cable2
    s "(Not that I mind the view.)"
    s "Ahem, Dani?"
    scene dani_cable3
    with vpunch
    dn "Argh, fuck!"
    scene dani_cable4
    with fade
    s "Jesus Christ... are you ok?"
    scene dani_cable5
    dn "What do you want?"
    s "I just swung by to say hi... what were you doing?"
    scene dani_cable6
    dn "*Sigh* My stupid monitor wont turn on. I'm guessing the cleaners may have accidentally bumped a cable or something."
    dn "But there's too many damn cables so I just started plugging and unplugging all of them."
    dn "I have so much work to get through and don't have time for this nonsense."
    s "You know I could take a look?"
    dn "I mean... fine do whatever you want."
    scene black
    with fade
    "In just under a minute [s] managed to identify the proper cables and plug them back in."
    scene dani_cable7
    s "There you go, that should take care of it."
    dn "So what, I'm supposed to thank you now?"
    s "That's usually what decent people do but I'm not twisting your arm here."
    scene dani_cable8
    dn "*Grumbling* Decent people my ass... "
    s "What was that?"
    dn "Thanks, ok?"
    dn "Now get out of here so I can get some work done."
    $ dani_cable = True
    $ pass_time(60)
    jump loc_gym

label dani_singing:
    hide screen ui_icons
    hide screen ui_text
    scene dani_sing1
    with fade
    dn "{i}Ya no estás más a mi lado, corazón, en el alma sólo tengo soledad.{/i}"
    s "(What... she's singing? I didn't think she was even capable of any sort of happy emotions.)"
    scene dani_sing2
    dn "{i}Y si ya no puedo verte, por qué Dios me hizo quererte, para hacerme sufrir mas.{/i}"
    scene dani_sing3
    dn "{i}Siempre fuiste la razón de mi existir, adorarte para mi fue religión{/i}"
    scene dani_sing4
    dn "{i}en tus besos yo encontraba, el calor que me brindaba, el amor y la pasión.{/i}"
    s "(She's actually really good... surprisingly good)"
    scene dani_sing5
    dn "{i}Es la historia de un amor, como no hay otro igual{/i}"
    s "*Ahem* Holahhh mih Ahmego!"
    scene dani_sing6
    with hpunch
    dn "[s]... No!"
    dn "How much did you hear?"
    s "Enough to see that you're quite the talented singer."
    scene dani_sing7
    dn "Don't mock me, asshole!"
    s "Mock you? I'm being dead serious, you have a beautiful voice."
    scene dani_sing8
    dn "You're not just saying that so I don't fire you again?"
    s "I'm not kidding, you should think about doing karaoke nights or something."
    s "That song was really beautiful."
    dn "Thanks, it's one of my favo-"
    scene dani_sing9
    dn "What am I even talking about? Get out of here!"
    dn "And don't spy on me like that again!"
    s "Okay, okay... sheesh."
    $ dani_singing = True
    $ pass_time(60)
    jump loc_gym

# DAISY
label daisy_reception:
    scene daisy_reception_chat1
    ds "Hey [s]!"
    menu:
        "Chat":
            if bj_daisy:
                s "Hey Daisy, staying busy?"
                ds "No, it's soooo slow and boring!"
                ds "How about you entertain me!?"
                s "I know just the thing."
                scene daisy_reception3
                ds "Jesus Christ [s]! Talk about going 0-60!"
                s "If you don't want to practice that's fine, I'll jus-"
                scene daisy_reception6
                "Daisy grabbed [s]'s cock before he could finish."
                ds "Nooo, you can stay. I still need more practice."
                scene daisy_reception9
                ds "*slurp*... *lick*"
                s "You're really starting to get better at this, you know?"
                scene daisy_reception10
                ds "Mmhmmm.."
                scene daisy_reception11
                s "Keep practicing going deep like that and you'll be the most popular girl at school."
                s "Here let me help."
                scene daisy_reception14
                "[s] grabbed Daisy by the back of the head and firmly guided her face farther down his cock."
                scene daisy_reception_bj_anim
                with fade
                ds "*gagging sounds*"
                s "Just keep breathing through your nose and relax your throat."
                s "You're doing great, just keep doing exactly what you're doing now."
                s "I'm gonna cum soon...get ready."
                menu:
                    "Cum on her face":
                        scene daisy_reception_cumshot1
                        "[s] pulled his cock out of Daisy's mouth and primed the shaft while aiming steady at her face."
                        "Daisy's right eye instantly took a direct hit as more reinforcements found their way on to her face."
                        ds ".....seriously?"
                        s "Sorry I didn't mean to get it in yo-"
                        ds "SERIOUSLY!? ON MY FUCKING FACE...AT WORK!?"
                        "Daisy stormed off to the bathroom before anyone could see her."
                        s "(Maybe I could have handled that a little better..)"
                        $ pass_time(60)
                        jump loc_gym
                    "Cum in her mouth":
                        s "Here...I..CUM!"
                        scene daisy_reception_cumshot2
                        "With a grunt, [s] kept his hands firmly on the back of Daisy's head as he pumped a stream of cum down her throat."
                        "Daisy struggled to keep it all in as some trickled its way down her mouth."
                        "A look of determination washed over Daisy's face as she took an audible gulp and swallowed everything."
                        ds "Did you see that!? I swallowed EVERYTHING!"
                        s "Wow, I'm impressed. These lessons aren't going to waste after all. You're going to be a pro just yet!"
                        $ pass_time(60)
                        jump loc_gym

            else:
                s "Hey Daisy, holding down the fort?"
                ds "What...what fort?"
                s "It means you're- actually never mind."
                s "Everything good up here?"
                ds "Yeah...but it's sooooo boooorrrrring!"
                ds "No one's been in for almost an hour. There's nothing to do!"
                s "Don't you still have work to do even if even if there are no clients?"
                ds "Sure, but that's like cleaning and stuff."
                scene daisy_reception_reception1
                ds "Can I ask you for a favor please?"
                ds "Remember when you said I can look at your...thing, if I just ask?"
                s "(Holy shit, is she really going to ask to see my dick?)"
                s "What are you talking about, what thing did you want to see?"
                scene daisy_reception_reception2
                "Daisy pouted a bit, reluctant to say it directly"
                ds "Your thing...when I fell and pulled down your shorts... remember?"
                s "OHHHH! You want to see my cock?"
                ds "Yeah...can I please see it?"
                s "Call it what it is and then I'll show you."
                ds "Your p-penis. Can I please see your penis?"
                s "It's called a cock dear, we're not in anatomy class. Call it a cock."
                ds "Uh...do I have to?"
                ds "Fine....cock. Can I see your cock?"
                s "(Hearing her talk about my dick woke him from his slumber. I proudly brought him out.)"
                scene daisy_reception_reception3
                "Daisy looked mesmerized"
                ds "Whoa it's already so hard!"
                scene daisy_reception_reception4
                ds "It's longer than my hand! How do girls fit this inside themselves?"
                s "So not only are you a virgin, but you've never even seen a dick in person before?"
                ds "Shut up, I was just like super busy all the time!"
                ds "Why are you so hard anyways? Aren't you gay?"
                s "Yup. He does tend to wake up when someone won't stop talking and looking at him though."
                ds "Can I touch it?"
                s "Go ahead."
                scene daisy_reception_reception5
                "Daisy ran a finger along the top of the shaft before grasping it ever so gently."
                ds "So it feels good when you go up and down right?"
                s "Yup, that's pretty much what jerking-off is."
                ds "I'm not trying to sound like a perv or anything, but do you think I can practice on you?"
                ds "I don't really have experience with boys, and I'm too afraid of screwing it up."
                s "Go ahead. I don't mind teaching you some things."
                s "Just grab firmly and start stroking it up and down."
                scene daisy_reception_reception6
                "Daisy began jerking off [s] clumsily but enthusiastically"
                ds "My arm's getting sore, thanks for the lesson!"
                if Ldaisy >= 1:
                    s "No way, you're not torturing me again."
                    ds "What do you mean?"
                    s "If you're going to get me worked up just to give up halfway through, then we're not doing any more lessons."
                    ds "But I just told you my arm's tired!"
                    s "Then don't use your arm."
                    ds "Huh, how then?"
                    s "How's this for an idea, do you want to learn about blowjobs?"
                    ds "You want me to put it in my mouth?"
                    s "Yes, put my cock in your mouth. If you don't like it you can stop."
                    ds "I don't know about this..."
                    s "You'll never learn otherwise."
                    scene daisy_reception_reception7
                    "Daisy brought her face up to [s]'s dick, unsure of herself."
                    "[s] felt her hot breath on the tip."
                    s "Before you start sucking on it, it's best practice to give it a little lick first. If you tease a guy first, it will drive him crazy."
                    s "The anticipation and build-up of pleasure will make the orgasm much better."
                    scene daisy_reception_reception8
                    "Without a word, Daisy explored the tip of the iceberg with her tongue."
                    s "Good job. Just like that, don't ignore the rest of the shaft."
                    scene daisy_reception_reception9
                    ds "Your skin is so soft. Does this feel good?"
                    s "You're doing a great job. I think you're ready to put it in your mouth now."
                    scene daisy_reception_reception10
                    "Daisy slid the cock in her mouth. She didn't get far before struggling."
                    scene daisy_reception_reception11
                    "Straining herself, Daisy managed to get about halfway down."
                    scene daisy_reception_reception12
                    ds "*Gasping for air*"
                    ds "How the hell am I supposed to fit this whole thing in my mouth?"
                    s "You'll get better with time. You're way too tense. The more you relax the easier it will be."
                    s "Relax your throat and lets try again."
                    ds "I don't know if I c-"
                    scene daisy_reception_reception13
                    "Before she could finish her objection, [s] grabbed Daisy by the back of the head and forced himself in."
                    ds "*Gagging sounds*"
                    "Daisy attempted to push herself off, but [s] overpowered her and kept guiding her head back onto his cock."
                    s "Just like this, we need to get you used to it."
                    s "Don't forget to breathe through your nose."
                    scene daisy_reception_reception14
                    "Daisy stopped struggling and started to make her actions resemble a blowjob."
                    scene daisy_reception_bj_anim
                    with fade
                    "Only the sounds of gagging and saliva could be heard."
                    scene daisy_reception_reception14
                    s "I'm almost there Daisy...get ready."
                    "[s] kept her head in place as his seed began pumping into  her mouth."
                    "Daisy began protesting and pulling away but was firmly held in place."
                    scene daisy_reception_reception15
                    "Finally the flow ended and Daisy lifted her head, mouth full of cum."
                    ds "MMMMMMHHHMHH!!! MHHMHHM!!!??"
                    s "Just swallow it."
                    scene daisy_reception_reception16
                    "Daisy shook her head through muffled objections."
                    s "Look you either swallow it or run to the bathroom and spit it out."
                    "Daisy leapt to her feet and ran off towards the bathroom."
                    s "(I hope she doesn't run into Dani along the way)"
                    s "(Well... that was interesting. Either we'll continue with these lessons or she'll be so pissed off at me that I lose my job)"
                    s "(It was probably worth it)"
                    $ Odaisy += 1
                    $ Ldaisy += 1
                    $ bj_daisy = True
                    $ pass_time(60)
                    jump loc_gym

                else:
                    s "Wait what? You're just going to stop now?"
                    ds "Well yeah.. I just told you, my arm's tired. Duh."
                    s "Do you want me to get blue balls!?"
                    ds "Haha, you're funny [s]. Your balls are not blue! My shirt is blue."
                    ds "You are so silly. I'm going to go back to work."
                    s "(Damn it. Next time she's going to see a job through, whether she likes it or not.)"
                    s "(I should get out of here before someone gets suspicious)"
                    $ Odaisy += 1
                    $ Ldaisy += 1
                    $ pass_time(60)
                    jump loc_gym_gym

        "Leave":
            s "(I'll talk to her later)"
            jump loc_gym

# JENNA
label jenna_shower:
    $ jenna_shower = True
    if jenna_bj:
        menu:
            "Order her to suck your dick":
                s "Hey Jenna, come on out."
                scene jenna_bj2
                j "What do you want?"
                s "I want you to get down on your knees in front of me."
                scene jenna_bj3
                j "Now just wait one s-"
                scene jenna_bj5
                "Jenna caught herself in her act of disobedience."
                j "... *groan*"
                scene jenna_bj10
                with fade
                "Jenna got down on her knees and put [s]'s cock into her mouth."
                s "Did I tell you to do that?"
                scene jenna_bj9
                j "Isn't it what you wanted?"
                s "That's for me to decide."
                $ renpy.pause(1)
                s "{b}Now{/b} put it in your mouth."
                scene jenna_bj11
                s "Very good... get to sucking."
                scene jenna_bj15
                s "Yes... just like that."
                jump jenna_bj1_anim

            "Leave":
                s "(I'll get to her some other time.)"
                jump loc_gym_locker
    else:
        s "(I don't think I can do anything here just yet, other than look at her.)"
        jump loc_gym_locker

label jenna_teabag:
    hide screen ui_icons
    hide screen ui_text
    scene jenna_teabag1
    s "(This is a good opportunity, plenty of people around to see her.)"
    s "(Let's see how she reacts when I embarrass her in public.)"
    scene jenna_teabag2
    s "Nice ass, bitch."
    scene jenna_teabag3
    with hpunch
    "Jenna swung around silently, almost out of instinct, connecting her fist to [s]'s face."
    scene jenna_teabag4
    j "Oh my God! [s]!?"
    s "Ughhh... are you kidding me? You wanted my help yet you punch me?!"
    j "I'm sorry, I didn't know! I didn't know it was you!"
    s "I'm the only guy here, who the hell else could it be?"
    j "I'm so sorry [s], I didn't mean to, I-"
    s "Enough!"
    s "Our deal is over, I'm out of here."
    scene jenna_teabag5
    "[s] began walking away. Before he could take more than a few steps Jenna had turned him around, begging for forgiveness."
    scene jenna_teabag6
    j "Please [s], it was an accident. I swear never to do it again!"
    s "I don't care."
    j "Please, I'll do anything you want. I'll listen to your directions completely."
    s "You punched me in the face Jenna."
    j "I know... you can punch mine if you want. We'll call it even!"
    s "No, I'm not going to punch you. I'm not going to do anything with you, I'm done."
    j "No, wait! I beg for your forgiveness, don't leave. I'll do as you say!"
    s "Do you promise to follow my orders, no matter how embarrassing they may be?"
    j "I swear!"
    s "*Sigh*... fine, you get one more chance."
    j "Thank you so much! You won't regret this."
    s "First, you have to be punished for what you did."
    j "*Gulp* Of course... "
    s "Get down on your knees."
    scene jenna_teabag7
    j "And beg for forgiveness? Of course!"
    j "I'm so sorry, I won't do that again."
    "[s] pulled down his shorts, placing his cock at eye level with Jenna."
    scene jenna_teabag8
    s "It's not going to be that easy for you."
    j "What the fuck do you th-"
    s "Shut up!"
    s "Rub your forehead on my balls."
    j "... but there's people watching."
    s "Exactly."
    "Reluctantly, Jenna raised her head until she could feel the weight of [s]'s scrotum."
    scene jenna_teabag9
    j "This is so demeaning... "
    s "That's the point."
    scene jenna_teabag10
    "Murmurs and some gasps of shock were echoed throughout the room."
    s "You've officially been tea-bagged, how do you feel?"
    j "Disgusting... I feel so disgusting and embarrassed."
    "Jenna's words were barely whispers."
    s "Alright, I think that's enough."
    scene jenna_teabag11
    j "That was so humiliating *sob*, can I go now?"
    s "Yes Jenna, you can go do whatever you want now."
    s "While you shed those tears, just remember, you asked for this."
    scene jenna_teabag12
    j "*whispers* I know... "
    $ jenna_teabag = True
    $ pass_time(180)
    jump loc_gym_gym

label jenna_bj:
    hide screen ui_icons
    hide screen ui_text
    scene jenna_bj1
    "Jenna noticed [s] the moment he walked in."
    j "[s], don't go anywhere. I'll be right out."
    scene jenna_bj2
    j "You're exactly who I needed to see."
    s "Umm, you sound happy to see me but you sure as hell don't look happy."
    j "Happy? Who gives a fuck about happy. I'm here to prove that no matter what you do to me, I'll rise back up stronger than before."
    s "Challenge accepted."
    scene jenna_bj3
    j "Now drop your shorts!"
    s "Normally I'm the one giving the orders, don't forget that."
    j "Sorry..."
    s "But since I like where this is going, I'm going to let it slide."
    "[s] took off his shorts a little more eagerly than he anticipated."
    scene jenna_bj4
    j "What the fuck!?"
    j "You weren't hard when you teabagged me last time!"
    s "That's probably because you punched me in the fucking face, Jenna."
    s "Also you're standing naked in front of me, what the hell else do you expect?"
    scene jenna_bj5
    j "I... I just wanted to prove to myself that I could let you teabag me without breaking down again."
    s "And now you're too chicken shit scared of the big bad boner?"
    scene jenna_bj6
    j "No, it's just that it's not the same quality of teabagging if you're erect."
    j "The skin is now stretched and so the quality of th-"
    s "Jenna, shut the fuck up and get down on your knees already, Jesus."
    scene jenna_bj7
    s "It's so much better when you're not talking."
    j "Well that's just plain rude."
    scene jenna_bj8
    s "Oh, and having my nuts in your face isn't?"
    j "Yeah... I guess you have a point."
    s "Didn't we agree last time that you'd follow my orders and not give me so much shit?"
    s "Do you remember that? Or did you repress all of the memories of yourself groveling on the floor in public?"
    j "I remember..."
    s "Yet you've been awfully snappy with me today, I think you're forgetting your place."
    "[s] pulled his cock up before releasing it like a spring, smacking Jenna in the nose."
    scene jenna_bj9
    with vpunch
    j "Owww, what the fuck?"
    "Taking advantage of Jenna's open mouth, [s] slid the tip of his dick inside."
    scene jenna_bj10
    s "There we go, so much better with your mouth doing something other than talking."
    j "*Muffled* Wait a minute I-"
    scene jenna_bj11
    with hpunch
    "Not allowing her the chance to finish her sentence, [s] slid his cock further into her mouth."
    scene jenna_bj12
    s "Here's the deal. You asked for help and I've helped you."
    s "You went from being frozen like a deer in headlights at just a little nipple showing, to now getting sassy with me while sitting naked with my cock on your face."
    s "This tells me that our training is working, wouldn't you agree?"
    scene jenna_bj13
    j "Mmmhmmm"
    s "I'm glad we're in agreement."
    s "This also tells me, however, that you're getting too used to what we're doing and it's time to step up the intensity."
    "[s] rammed his cock even further into Jenna's mouth until he could feel it hitting the back of her throat."
    scene jenna_bj14
    "Jenna gagged and spit out his cock while gasping for air."
    s "Oh no, weak little Jenna can't handle it. Even Daisy can handle a dick better than you."
    j "*Cough* Daisy gave yo-"
    scene jenna_bj15
    with hpunch
    "Once again, [s] rammed his cock into Jenna's mouth before she could complete her sentence."
    s "Nothing matters to you right now other than getting this dick sucked. I don't want to have to remind you again."
    s "Look me in the eyes as you suck on my cock like some common whore."
    "Jenna managed to let out a grunt in agreement as she doubled her efforts."
    "The sooner she makes him cum, the sooner she can put an end to this humiliation."
    jump jenna_bj1_anim

label jenna_bj1_anim:
    menu:
        "Side View":
            scene jenna_locker_bj_side
            with fade
            $renpy.pause()
            jump jenna_bj1_anim

        "Top View":
            scene jenna_locker_bj_top
            with fade
            $renpy.pause()
            jump jenna_bj1_anim

        "Cum":
            if jenna_bj:
                "[s] groaned loudly as he approached his orgasm."
                "Without warning he pushed Jenna's head off his cock and directed the cum at her face."
                scene jenna_bj17
                with vpunch
                $renpy.pause(1)
                s "You're getting used to having your face covered in cum."
                s "I'm starting to think that maybe you like it."
                j "Ugh... *grumbles*"
                s "Go clean yourself off, you're disgusting."
                $ pass_time(60)
                jump loc_gym_locker

            else:
                "[s] groaned loudly as he approached his orgasm."
                "Without warning he pushed Jenna's head off his cock and directed the cum at her face."
                scene jenna_bj17
                with vpunch
                $renpy.pause(1)
                s "Now you're covered in cum like a proper slut."
                s "How does that make you feel?"
                $renpy.pause(1)
                s "...well?"
                "Jenna did not say a word. [s] thought he saw something in her eyes and it wasn't the cum."
                "Her expression filled with pain and the emptiness of defeat."
                "She slowly lifted herself up off the floor and walked towards the shower."
                $ jenna_bj = True
                $ pass_time(120)
                jump loc_gym_locker

label jenna_bench_event1:
    scene jenna_bench1
    "Jenna was dead focused on her workout. Audible grunts and the suction of air surrounded her."
    scene jenna_bench2
    "[s] walked behind her, hoping to casually get a brief glance at her fake breasts."
    j "What do you want, sissy?"
    s "Nothing, just walking by."
    j "Well keep walking."
    scene jenna_bench3
    "Jenna continued with her workout, as if certain that [s] would follow her command."
    scene jenna_bench4
    "Suddenly her arms began to shake and the barbell could no longer be supported."
    "A look of panic swept across her face as she gasped 'help' to [s]."
    s "Hmmm, I could help lift this weight off your chest."
    s "But then again, you're a competing bodybuilder. You should be able to handle this no problem."
    s "However, I am still a personal trainer and it's my duty to assist you."
    s "But you did tell me to keep walking...hmmm...such a difficult decision...what shall I do?"
    "While [s] was busy entertaining himself with petty vengeance, Jenna's eyes began to flutter as the darkness closed in around her."
    "Her arms fell limb to the side as she blacked out."
    s "Holy shit, you weren't kidding!? Jenna...JENNA!"
    "[s] rushed over and barely managed to pull the weight off her chest."
    scene jenna_bench5
    "Jenna regained consciousness, weakly raising her head to look at [s]."
    s "Oh my God Jenna, I'm so sorry! I thought you were playing a prank on me."
    j "Help me up please."
    scene jenna_bench6
    s "I thought you could easily handle that weight, I thought you were joking. I'm so sorry!"
    scene jenna_bench7
    "As [s] approached Jenna and offered his extended arm, she jumped to her feet and put all of her weight into shoving him."
    scene jenna_bench8
    "Caught in an off-balanced position, Jenna managed to drop [s] on to his back."
    scene jenna_bench9
    j "*Muffled sounds*"
    s "(What the hell...uh...what's going on?)"
    scene jenna_bench10
    "A light went out in the background, adding to the dramatic sense of dark power Jenna possessed, standing over [s] with a foot on his chest."
    j "-and if you ever, and I mean EVER think to try and exert power on me like that again. If you ever think you can clown me like that or disrespect me."
    j "I will break you in half, DO YOU UNDERSTAND ME!?"
    s "Uhhhh..."
    j "I'll take that as a yes."
    "Jenna removed her foot from [s]'s chest and triumphantly walked towards the lockers."
    $ jenna_bench_event1 = True
    $ pass_time(120)
    jump loc_gym_gym

label jenna_bench:
    scene jenna_bench3
    $ jenna_bench = True
    if jenna_spank1:
        menu:
            "Pull her top down":
                scene jenna_benchtits
                j "What the hell? .... [s]!"
                s "Just shut up and continue your workout."
                j "Grrr..."
                jump loc_gym_gym

            "Leave":
                s "(Let's not risk it with her today.)"
                jump loc_gym_gym
    else:
        s "(I'm not about to get my ass kicked again. I think I'll just keep on walking.)"
        jump loc_gym_gym

label jenna_event1:
    hide screen ui_icons
    hide screen ui_text
    scene jenna_shower_event1
    s "(Jenna's taking a shower. Why does someone so shitty have to be so damn hot?)"
    s "(I could just run up behind her, grab her by her ponytail and fuck her against the wall.)"
    s "(Yeah right... she'd probably throw me down and crush my chest again.)"
    scene jenna_shower_event2
    s "(There's her clothes though. I can still fuck with her and get a little payback)"
    "[s] quietly snuck across the room, snatching Jenna's clothes before sprinting towards the exit"
    scene jenna_shower_event1
    s "(Hehe, this isn't exactly a master-mind evil plan but it'll do for now.)"
    scene jenna_shower_event3
    "[s] tossed Jenna's garments into a nearby trashcan before heading out into the lobby, trying to play it cool."
    s "What's up, Daisy... bored?"
    ds "You can say that again. This job is no fun. Noooooothing ever happens."
    ds "I should find somewhere fun to work. Like the FBI, oooh, or maybe as a vetri-vetrinari... a vet!"
    s "Um, you do realize you need to go to school for both of those things, right?"
    ds "Really? Aww man, that's so stupid."
    s "Hey, you could always try Wellmart. I hear it's really exciting, especially if you like animals."
    ds "What do you mean? I don't remember any animals at Wellmart, except for like...fishies and stuff."
    s "You mean you've never seen the native Wellmart Wilder Beast?"
    s "Experts say that they can grow up to 600lbs in the wild."
    s "When denied the use of an expired coupon for Daritos chips, the hairs on their backs can stand up to 6 inches tall as adrenaline and rage fills their tiny little hearts."
    ds "Whaaa? Are you serious? I've never seen or heard of a Wellmart Wilder Beast. They sell them?"
    s "Unfortunately no, it's illegal to own or sell one of those. Scientists are still trying to figure out their reproduction cycle."
    s "All we know is that the alley behind Wellmart is often used as a mating ground."
    s "Those who've attempted to document this act of nature were never to be seen again, presumed dead."
    ds "That's so interesting. [s], you know so much stuff!"
    scene jenna_shower_event4
    j "You dirty little sack of shit!"
    "[s] looked around, acting aloof."
    j "Yes, you! You son of a bitch."
    s "What the hell is it this time, Jenna?"
    j "You stole my clothes. Where'd you put em?"
    scene jenna_shower_event5
    ds "[s] was with me this whole time. We were talking about the Wellmart Wilder Beasts."
    ds "Did you know that the hair on their back can stand up to 6 feet tall when they feel threatened!?"
    s "6 inches Daisy, 6 inches."
    scene jenna_shower_event6
    j "Shut the hell up both of you. I'm going to kick your ass you little twerp!"
    ds "But he didn't do anything! He was just cheering me up because I was sooo bored."
    j "Then you'll find this beating exciting!"
    scene jenna_shower_event7
    "As Jenna stepped forward her towel slipped, exposing her breasts."
    s "Hey, you're right. I DO find this exciting."
    "Jenna quickly covered herself once more, face dark red with anger."
    s "Hey Jenna, we have plenty of racks at the gym. You don't need to bring your own."
    scene jenna_shower_event8
    "Embarrassed, Jenna turned back around towards the locker room, yelling obscenities over her shoulder."
    ds "Oh my gaaaaawd that was hilarious!"
    ds "Did you see how embarrassed she was!?"
    s "Well you did want some more excitement around here."
    scene jenna_shower_event9
    ds "Totes! That was fun. You need to hang around here more often."
    s "I'll do my best. You know entertaining you is always a top priority of mine."
    s "Anyways, I need to get back to work before Jenna decides to flash us again."
    $ jenna_event1 = True
    $ pass_time(60)
    jump loc_gym

label jenna_shower_revenge1:
    hide screen ui_icons
    hide screen ui_text
    scene jenna_shower_revenge1
    j "(Now where did that bastard go?)"
    scene jenna_shower_revenge2
    j "(Aha... got you now.)"
    scene jenna_shower_revenge3
    j "(Let's see how you like a taste of your own medicine.)"
    scene jenna_shower_revenge4
    j "(Careful now, wouldn't want him to turn around and catch me in the act.)"
    scene jenna_shower_revenge5
    j "(He doesn't look half bad, naked with his mouth closed.)"
    scene black
    with fade
    "Jenna grabbed [s]'s clothes and quickly made her escape."
    scene jenna_shower_revenge6
    j "Hey Daisy, want to see something funny?"
    ds "Ooh, are you going to make faces?"
    j "What? No."
    j "I'm going to play a prank on [s]. He's in the shower and I hid his clothes."
    ds "Well that's not very nice of you."
    j "He did the same thing to me last time, so fair is fair."
    scene jenna_shower_revenge7
    ds "Oooh, gotchya!"
    scene jenna_shower_revenge8
    s "So... I'm guessing you took my clothes?"
    scene jenna_shower_revenge9
    ds "Well, well, well... How the turn tables."
    scene jenna_shower_revenge10
    $ renpy.pause()
    scene jenna_shower_revenge11
    j "It must be so embarrassing, standing out here with nothing but a towel on."
    s "I don't really mind to be honest."
    j "You must be feeling so vulnerable right now."
    s "Really, it's not a big deal. Just wondering where you put my-"
    scene jenna_shower_revenge12
    j "Would be a shame if something were to... SNATCH YO TOWEL!"
    scene jenna_shower_revenge13
    s "Seriously?"
    j "Haha! Look at this pathetic little penis."
    scene jenna_shower_revenge14
    ds "I don't know Jenna, looks pretty big to me."
    scene jenna_shower_revenge15
    j "*Grumbling* What do you even know about dicks?"
    scene jenna_shower_revenge16
    s "Are we done here? I've got things to do."
    j "Ha, look at him. Running away with embarrassment."
    s "Not everyone is as insecure about their body as you are."
    j "THAT'S NOT TRUE. I HAVE A KILLER BODY. I'M MUCH MORE FIT THAN YOU!"
    scene jenna_shower_revenge17
    s "Whatever helps you sleep at night."
    j "Hey, don't you dare walk away from me."
    s "Bye Felicia."
    scene jenna_shower_revenge18
    j "I HAVE A GREAT BODY AND YOU HAVE A TINY DICK!"
    j "DO YOU HEAR ME!?"
    $ jenna_shower_revenge1 = True
    $ pass_time(120)
    jump loc_gym

label jenna_mma1:
    hide screen ui_icons
    hide screen ui_text
    scene jenna_mma17
    s "Hey Daisy, is that Jenna on TV?"
    ds "Yeah! She's having her first match ever."
    ds "Goooooooooooo Jenna, woooooo!"
    "[s] decides to stay and watch."
    scene jenna_mma1
    com "What a devastating kick to the head!"
    scene jenna_mma2
    j "(Hmmm, this bitch is done.)"
    scene jenna_mma3
    com "Spectacular deflection by our new challenger."
    scene jenna_mma4
    com "Counter attack lands on target."
    com "If this keeps up, the ref will surely have to step in and stop the fight."
    scene jenna_mma5
    j "Is this what you all came for?"
    "The crowd erupts in cheers."
    j "Are you not entertained?"
    scene jenna_mma6
    "Jenna's ego got the best of her as she did not notice her opponent recover and charge her from the side."
    scene jenna_mma7
    "Jenna collapsed to the ground, the impact of the fall knocking all of the air out of her lungs."
    com "What an arrogant display by the new comer."
    com "Michele Tyson has found her opening and has taken Jenna to the ground."
    scene jenna_mma8
    "Jenna tried to roll over and get back on her feet as her opponent reached out to grapple her."
    "Michele managed to grab a hold of Jenna's shorts causing her to lose her balance and fall over."
    scene jenna_mma9
    com "What a turn of events. You folks have paid for a great show, feast your eyes on this!"
    com "Our newest challenger must have lost her mind to celebrate prematurely."
    com "Now she has lost her shorts."
    scene jenna_mma10
    "The crowd erupted in laughter and cat-calls as Jenna managed to get on to her feet."
    j "(What the fuck are these assholes laughing at?)"
    j "(Huh?)"
    scene jenna_mma11
    j "OH MY GOD!"
    scene jenna_mma12
    j "STOP THE FIGHT! STOP THE FIGHT!"
    j "I'M NAKED, STOP THE FIGHT!"
    scene jenna_mma13
    "Jenna's protest fell on deaf ears as Michele delivered a powerful kick to the face."
    scene jenna_mma14
    com "MICHELE TYSON HAS DONE IT, SHE HAS KNOCKED OUT JENNA!"
    com "Well there you have it folks, humility goes a long way."
    scene jenna_mma15
    "The crowd erupted in both cheers and laughter."
    com "Now is the time to celebrate, take notes Jenna... whenever you wake up."
    scene jenna_mma14
    com "This has definitely been a first for us, we have never witnessed a fighter become disrobed."
    com "Looks like one man in the crowd has taken advantage of the situation and began pleasuring himself."
    com "Security has escorted him out although it appears he is repeatedly yelling 'Worth it'."
    com "To those at home, thank you for watching our premium match of the week."
    com "Good night and God bless."
    scene jenna_mma18
    ds "Oh nooo... poor Jenna."
    s "Pfft, serves her right."
    ds "Don't be a jerk, this will crush her."
    s "Whatever."
    $ jenna_mma1 = True
    $ pass_time(180)
    jump loc_gym

label jenna_postmma:
    hide screen ui_icons
    hide screen ui_text
    scene jenna_post_mma1
    "Jenna's body tensed as she noticed [s] nearby."
    j "Did you come here to talk shit again?"
    s "No, I'm not going to tease you anymore."
    scene jenna_post_mma2
    j "Finally learned your lesson, eh."
    s "How long are you going to keep this 'tough girl' facade?"
    j "What are you saying? I could break you into pieces right now if I wanted to."
    s "Probably, but it won't change what an insecure little girl you are on the inside."
    scene jenna_post_mma3
    j "Oh what, you're a psychologist now?"
    j "You don't know what you're talking about."
    s "Jenna, you were beating that other girls ass in your fight."
    s "I mean, it wasn't even close. You were practically playing with your food."
    j "Exactly! She just got lucky, that's all."
    s "Yeah, she got lucky that your shorts came off and you ended up being a little bitch about it."
    scene jenna_post_mma4
    j "Call me a little bitch again and see what happens."
    s "I have no doubts you'll probably punch me or knock me down."
    s "Still doesn't change the fact that you're so damn insecure about your body."
    scene jenna_post_mma5
    j "I'm NOT insecure about my body!"
    j "You know how many men AND women want to have sex with me?"
    s "Cut the bullshit."
    s "You ran away scared when your towel fell off in the lobby."
    s "You froze up like a deer in headlights when your shorts came off during your fight."
    s "You're probably too ashamed to even get back into the cage."
    scene jenna_post_mma6
    j "You don't know what you're talking about..."
    s "Even Hikari is more comfortable about being naked than you are, and she's a timid little mouse."
    j "You're wrong, I'm proud of myself... I'm proud of my body..."
    j "... I've worked hard so many years to get this body..."
    s "Whatever you say, Jenna. I see right through your little act."
    scene jenna_post_mma7
    j "I'm strong... I'm sexy..."
    j "... no one can compare..."
    j "... I'm the best."
    "[s] walked away as Jenna continued mumbling to herself."
    $ jenna_postmma = True
    $ pass_time(60)
    jump loc_gym_gym

label jenna_spank1:
    hide screen ui_icons
    hide screen ui_text
    scene jenna_spank_event1
    s "(I'm allowed into the women's locker room and yet there's no one here...)"
    s "(What a shame.)"
    scene jenna_spank_event2
    j "YOU!"
    j "I've been looking for you!"
    s "Well you found me, want a cookie or something?"
    j "No... I just wanted to say that..."
    s "Come on, spill it already. You look like you're about to cry."
    j "Can you not be an asshole while I'm trying to apologize!?"
    s "You... apologizing?"
    s "Is it April fools day already?"
    scene jenna_spank_event3
    j "Trust me, I'm in more disbelief than you are."
    j "You were right, I'm sorry."
    s "I like where this is going, continue."
    j "You were right... I am ashamed of my body."
    j "Maybe it's because I was always teased growing up, called an Amazon woman since I eclipsed the boys."
    j "Or worse yet... people called me a boy."
    s "So you got yourself a pair of fake tits to prove them wrong?"
    scene jenna_spank_event4
    j "Something like that... "
    s "Ok, apology accepted. Why are you even telling me this?"
    j "Because you're so comfortable with yourself. I'm in much better shape than you yet somehow that doesn't even seem to bother you."
    j "How do you do it?"
    j "How can I become confident like you?"
    s "Are you saying you want to be more like me?"
    scene jenna_spank_event3
    j "... I just don't want to be uncomfortable in my own body."
    j "I don't want to get laughed at anymore."
    s "First off, you will never get people to stop laughing at you. All you can do is not let it phase you."
    j "How do I do that? Were you always so confident?"
    s "No, but when you walk in on your gir-... boyfriend fucking another man, it gets easier."
    s "There's nothing more embarrassing than realizing that all your friends and coworkers were really just laughing at you behind your back."
    s "They knew what was going on and no one told me. I was the butt of their jokes for... God knows for how long, without even knowing it."
    scene jenna_spank_event2
    j "So what, I need to go get into a relationship and get cheated on? That's stupid."
    s "No dumbass, you need to be torn down to nothing. Once you know what true humiliation is, everything else will feel trivial."
    s "Are you prepared for me to brutally tear you apart?"
    j "You think I can't take it? Try your worst."
    s "Okay then, but you have to do exactly as I tell you."
    j "*Sigh* Fine, I'll listen..."
    s "Okay then, let's start off with something easy."
    s "Take off your clothes."
    scene jenna_spank_event5
    j "WHAT? You perverted piece of shit. I knew you'd try to take advantage of me."
    s "You're ashamed of your body, seemed like a good place to start."
    j "No, fuck you. Do something else. Insult me or something."
    s "You've been talking shit and had shit talked back to you all your life."
    s "Nothing I say will make a difference."
    s "Undress or leave, I don't have time for these games."
    scene jenna_spank_event6
    j "You're serious aren't you?"
    j "*Gulp* ...fine. But if you try to touch me I will break your goddamn hand!"
    scene jenna_spank_event7
    "Jenna shed her clothes, unable to look [s] in the eyes."
    j "Happy?"
    s "No, you're covering yourself up. Lower your hands."
    j "Grrr...."
    scene jenna_spank_event8
    s "That's better. Look at you, standing naked in front of the person you hate."
    s "Showing yourself off like you have no shame."
    j "You motherfucker! You said you were going to help me."
    s "I said I was going to help you by humiliating you to the point of nothing else mattering."
    s "Once you know what rock bottom feels like, everything else will seem trivial."
    s "Now let me take a good look at those tits."
    scene jenna_spank_event9
    s "Was the surgeon old?"
    j "No... why?"
    scene jenna_spank_event10
    s "Because your tit job looks like it was done by a half blind man with shaky hands."
    j "*Under her breath* You son of a bitch..."
    s "Now turn around and let me see that disgusting pussy."
    scene jenna_spank_event11
    j "No! Too soon. I can't... "
    s "Why?"
    j "I just... I can't show you that."
    s "Look Jenna, half the world saw your pussy on TV. What are you so ashamed of now?"
    j "... it's just... I have an oversized... "
    s "Ego? Yes you do. Don't worry, I'm here to fix that."
    j "I have an oversized clit!"
    s "Ah, there we go. Now we're getting to the root of it."
    s "Well then, go on and show me."
    scene jenna_spank_event12
    "Jenna turned around begrudgingly."
    s "Well I've got some good news and bad news for you."
    scene jenna_spank_event13
    s "Bad news, you really do have an oversized clit."
    scene jenna_spank_event12
    j "... and the good news?"
    s "I'd still fuck it."
    j "... perverted little bastard."
    scene jenna_spank_event14
    j "There, I showed you everything. I'm going to go now."
    s "Not so fast."
    s "You're embarrassed, but I haven't humiliated you yet."
    j "What could be worse than this?"
    s "Come here and lay down on my lap."
    j "... why did I ever agree to this bullshit."
    s "Because you know it's your best chance at not being a whiny little bitch forever."
    scene jenna_spank_event15
    s "You know... you've got a pretty good looking ass."
    s "Too bad it's attached to a colossal bitch."
    j "Fuck you asshole."
    scene jenna_spank_event16
    with fade
    "*SMACK*"
    s "Now now, that's no way to talk to your friend."
    scene jenna_spank_event17
    j "OWWW! What the fuck [s]? I didn't give you permission to spank me."
    scene jenna_spank_event18
    s "I don't need permission to spank little brats."
    scene jenna_spank_event19
    "*SMACK*"
    j "FUCK!"
    s "What kind of fighter can't even take a little smack on the bum."
    scene jenna_spank_event18
    s "What a disgrace."
    j "Listen here you litt-"
    scene jenna_spank_event19
    "*SMACK*"
    j "JESUS FUCKING CHRIST!"
    s "Look, I can do this all day until you learn you lesson."
    j "Ok... ok."
    j "Can I PLEASE get up now?"
    s "Manners? Now that's much better."
    scene jenna_spank_event20
    s "Well that was a fun little introduction to the world of humiliation and shamelessness."
    j "Introduction? How much worse could it get?"
    s "Careful , you may not want answers to that question just yet."
    j "Whatever... where's my clothes? I'm getting out of here."
    s "You forgot something."
    j "What?"
    s "You forgot to thank me."
    j "For what, for spanking and humiliating me?"
    s "For giving a damn about you and your fragile little ego."
    s "You will thank me if you want our training to continue."
    "Jenna glared daggers at [s] before releasing a huge sigh."
    j "Thank you [s]."
    s "You're welcome Jenna, till next time."
    $ jenna_spank1 = True
    $ pass_time(120)
    jump loc_gym_locker

label jenna_intro:
    hide screen ui_icons
    hide screen ui_text
    scene jenna_intro1
    "A gorgeous athletic girl stood guard, watching over the empty desk that Daisy normally occupied."
    "Her muscles were huge and would put most men to shame, yet she still managed to look incredibly feminine and sexy."
    scene jenna_intro2
    s "Hey, where's Daisy?"
    who "Not here. Just like you shouldn't be here."
    s "I'm actually a personal trainer here."
    who "Oh... you must be Calvin, the sissy Daisy told me about."
    s "The name's [s]."
    j "Yeah, whatever."
    s "Why are you being so needlessly rude? Did I do something to you?"
    scene jenna_intro3
    "The girl ignored [s]'s question and as if he wasn't standing there next to her, began stretching her thighs."
    s "What's your name?"
    who "Jenna."
    s "Well Jenna, I'm a trainer here so if you ever need any help or have any questions, let me know."
    "Jenna began ignoring [s] once more, not shy in displaying her contempt for him."
    s "You have great arms. I can spot you at the bench if you'd like."
    scene jenna_intro4
    j "You'd spot me? Hmmmm let me think about it."
    scene jenna_intro5
    j "So on one hand, you're a personal trainer."
    scene jenna_intro4
    j "Then again... I'm a competing bodybuilder."
    scene jenna_intro5
    j "Hmmm...this is a difficult choice."
    scene jenna_intro4
    j "Bodybuilder being helped by a sissy trainer...hmmm, this is a tough one...hmmm."
    s "Alright, alright, you don't need to be such a jerk about it."
    scene jenna_intro6
    j "YEAH! You got it buddy!"
    scene jenna_intro7
    j "Now run along."
    s "(What a bitch...)"
    $ Mjenna = True
    $ pass_time(60)
    jump loc_gym

# HIKARI
label hakari_pool:
    $ hikari_pool = True
    if Mhikari:
        scene gym_pool_hikari1
        menu:
            "Chat":
                s "Hey Hikari, just hanging out by the pool again?"
                scene gym_pool_hikari2
                h "Yes, just thinking."
                s "Can I help in any way?"
                scene gym_pool_hikari3
                h "No, thank you. I think alone."
                s "Ok, I'm here if you need me."
                $ Ohikari += 1
                $ pass_time(60)
                jump loc_gym_pool
            "Leave":
                s "(Probably best to leave her alone.)"
                jump loc_gym_pool
    else:
        scene gym_pool_hikari1
        "A petite girl with short black hair sat idly at the edge of the pool."
        s "I haven't seen you around yet, do you need some hel-"
        scene gym_pool_hikari2
        who "WHAT? You! You here why?"
        s "I'm the new trainer here. Thought I'd introduce myself."
        who "You gay man miss Daisy say about? If you gay, I Queen of Japan. You go now."
        scene gym_pool_hikari1
        s "..."
        who "Still here?"
        s "Yes..."
        scene gym_pool_hikari2
        who "Said you go now."
        s "I know."
        who "Why you no go?"
        scene gym_pool_hikari1
        s "I'm waiting for a name."
        who "Why you so interest?"
        s "It's my job to be interested, but you also look like you could use a friend."
        scene black
        with fade
        "*SPLASH*"
        scene gym_pool_hikari4
        with fade
        s "(Wow, she must be half mermaid.)"
        scene gym_pool_hikari5
        s "You're fast, girl. Why won't you give me your name?"
        scene gym_pool_hikari6
        who "You no give up easy?"
        s "You seem sad and I won't leave till I know why."
        scene gym_pool_hikari7
        who "I look sad?"
        s "A little bit..."
        "A small moment of silence passes."
        scene gym_pool_hikari8
        who "Not sad, just..."
        s "Yes?"
        who "Just think about things."
        s "Maybe I can help?"
        scene gym_pool_hikari9
        who "How? Make me exercise?"
        scene gym_pool_hikari8
        who "Well? How help me?"
        s "I do more than just fitness you know?"
        who "What you do?"
        s "I'm a good listener. Every girl needs a gay best friend *wink*."
        scene gym_pool_hikari9
        who "Hahahaha, Queen of America."
        s "Just princess for now."
        scene gym_pool_hikari8
        who "Hikari."
        s "Hikari? What's that mean? Did you call me an asshole in your language?"
        scene gym_pool_hikari9
        who "Funny boy. Hikari my name. You are asshole too. Funny asshole."
        s "I'm [s], nice to meet you. I want to know more about you."
        scene gym_pool_hikari8
        h "No, I want just swim. I good at swim."
        h "Only good at swim..."
        scene gym_pool_hikari4b
        s "(Guess I'll have to be more patient with her.)"
        $ Ohikari += 1
        $ pass_time(60)
        $ Mhikari = True
        jump loc_gym_pool

label hikari_pool_swim:
    $ hikari_pool = True
    if nude_swim_hikari:
        scene nude_swim_hikari3
        s "(Hikari looks at peace, I won't disturb her...except maybe to stare a little.)"
        jump loc_gym_pool
    elif Mhikari and strip1_hikari and nude_locker_hikari:
        scene gym_pool_hikari4
        menu:
            "Watch":
                scene gym_pool_hikari5
                s "Hikari, what are you doing!?"
                scene gym_pool_hikari6
                h "Hi [s], I swim."
                s "Yes I can see that, but why are you not swimming naked?"
                h "But someone can see me!"
                s "No one uses this pool but you."
                scene gym_pool_hikari8
                h "What if Dani walk and see? She kick me from gym!"
                s "She won't kick you nor will she see you. Enough excuses, take it off."
                scene gym_pool_hikari7
                h "*sigh*... ok"
                "Hikari took her swimsuit off underwater and kicked off the side of the pool before [s] could get a good look."
                scene nude_swim_hikari1
                s "That wasn't so bad now was it?"
                s "You better be naked every time you swim or I'm going to be upset with you."
                scene nude_swim_hikari2
                "Hikari flipped onto her back, grinning as her breasts teased the surface of the water."
                $ nude_swim_hikari = True
                $ pass_time(60)
                jump loc_gym_pool
            "Leave":
                jump loc_gym_pool

    elif Mhikari:
        scene gym_pool_hikari4
        menu:
            "Watch":
                if Mhikari2:
                    jump hikari_pool_secrets
                else:
                    scene gym_pool_hikari4
                    s "(Damn that girl's fast.)"
                    scene gym_pool_hikari4c
                    s "(I know I've seen her before. Think [s], think. TV? No, not TV.)"
                    s "(Porn? No, that's not it. I would have definitely remembered a tight body like that.)"
                    scene gym_pool_hikari5
                    h "Funny gay boy come talk with Japanese Queen again?"
                    s "M'lady, this humble peasant is not worthy of your grace, or speed for that matter. Are you part dolphin or something?"
                    scene gym_pool_hikari6
                    h "I like you gay boy. You funny. I not dolphin. I come to America for education, swim for school."
                    s "That's where I know you from! You swim for Candyland University Ninja Titans. You beat out everyone with meters to spare."
                    s "I just saw that on the local news last week."
                    scene gym_pool_hikari9
                    h "I beat many teams. Very fast dolphin."
                    scene gym_pool_hikari8
                    s "What's wrong, Hikari? You look sad again."
                    h "Can I tell you a little secret?"
                    s "Please."
                    h "I don't like to swim."
                    h "My parents make me because I good. I swim good and get good school."
                    s "So you hate swimming now? You could have fooled me."
                    scene gym_pool_hikari9
                    h "You fool. Easy to fool."
                    s "Accurate."
                    scene gym_pool_hikari8
                    h "I swim for parents. I do nothing for Hikari."
                    s "So what is it that you want to do? What's your dream?"
                    s "Maybe I can help?"
                    h "No, you no help."
                    "Hikari pushes off the side of the pool and swims away."
                    h "Bye gay boy."
                    $ Mhikari2 = True
                    $ pass_time(120)
                    jump loc_gym_pool
            "Leave":
                s "(She'll probably give me the cold shoulder again anyways)"
                jump loc_gym_pool
    else:
        s "(Someone is swimming in the pool. I wonder if she's sexy? I need to get a better look.)"
        scene gym_pool_hikari5
        s "(Pretty face, so far so good.)"
        s "You're a great swimmer!"
        scene gym_pool_hikari7
        "The girl looked away without responding"
        s "(What a bitch...or maybe she's shy? Oooh, I hope she's shy! That'll be fun!)"
        s "Well, enjoy the rest of your swim."
        $ pass_time(60)
        jump loc_gym_pool

label hikari_pool_secrets:
    hide screen ui_icons
    hide screen ui_text
    scene gym_pool_hikari4c
    s "Hey, Hikari."
    scene gym_pool_hikari5
    h "Gay boy, hi."
    scene gym_pool_hikari6
    h "You want talk again?"
    s "That'd be great."
    s "We can even play a game to make it more fun."
    scene gym_pool_hikari7
    h "Not hide sausage... I hate that game."
    s "What?!?"
    s "Oh no, no no no no. When did yo-"
    s "Never mind, doesn't matter. I was going to suggest 'Secret Poker'."
    scene gym_pool_hikari8
    h "You tell me I sexy, them you poke me with secret in pants. No, ok?"
    s "Yeah... I don't know any games like that."
    s "I tell you a little secret about me, it has to be true. You can choose to match my secret with one of yours."
    s "Or you can 'raise' by telling me an even bigger secret, then I will have to match it with my own."
    scene gym_pool_hikari9
    h "That silly game, sound like fun."
    h "Ok, I'll start it off easy."
    s "When I was little, I used to tuck my penis between my legs."
    s "I just wanted to see what it would look like."
    h "Haha, you were princess when little too!"
    h "Ok, when I small I read book in bed with small light on."
    s "... and?"
    h "My parents say go bed, it bedtime. But I read book. I never tell anyone!"
    s "Wow, sounds like you were quite the troublemaker."
    h "Big trouble maker."
    s "Ok, I'll raise you a bigger secret."
    s "Sometimes I don't think I'm really gay. I used to have sex with girls in college too."
    s "I really liked it, but my heart was always stolen by the boys."
    h "Haha gross, gay boy tell me gay boy secrets hahaha."
    h "Ok, I use calculator on math homework {b}one{/b} time."
    h "I know how to do it, but feel lazy."
    s "That's your big secret? Hikari, that's so lame."
    scene gym_pool_hikari8
    h "Why you mean boy now?"
    s "I'm not trying to be mean. I just told you a secret that only one other person knows."
    s "And you told me something so innocent, it's adorable really. It's not a big deal though."
    h "It big deal!"
    s "Nope. I bet you don't have any real secrets. You're too sweet of a girl to have those."
    h "I have big secret."
    s "Let me guess, you once had to scoops of rice in the cafeteria when you're only allowed to have one?"
    scene gym_pool_hikari7
    s "I'm going to get back to work Hikari. It's been fun talking to you."
    scene black
    with fade
    "[s] began heading towards the door as he heard Hikari blurt out."
    h "I WANT TO BE STRIPPER!"
    scene gym_pool_hikari7
    with fade
    s "WHAT!?"
    h "I want to be stripper."
    s "Are you messing with me?"
    h "I stupid, I know."
    s "So you seriously want to be a stripper!?"
    h "Yes... I disgusting, I know."
    s "No, that's actually pretty fantastic and very brave of you to tell me."
    scene gym_pool_hikari8
    s "Why though? What makes you want that?"
    h "It's very beautiful. Girls dance, make like art, they have beautiful body."
    h "Have much power, control men."
    s "Well you already have a beautiful body, I can't see why you couldn't achieve this dream."
    scene gym_pool_hikari9
    h "Really? You think I look nice?"
    s "You look {b}very{/b} nice."
    s "Well you're in luck, I know how to help you."
    h "Really!?"
    s "We have poles for dancers in the gym if you hadn't noticed yet. I can help you with a routine."
    scene gym_pool_hikari8
    h "But people watch and laugh!"
    s "(She's starting to get cold feet. I really need to make the close here.)"
    s "I promise you, no one will be laughing. Let's see what you have and I can give you feedback from a man's perspective."
    h "I don't know..."
    s "Come on. Go and dry yourself off and I'll meet you in the lobby."
    scene gym_pool_hikari9
    h "Ok! I come very soon."
    s "(Let's hope she doesn't have second thoughts and actually goes through with this.)"
    scene gym_pool_hikari10
    with fade
    "Hikari came out visibly less excited than when she first left the pool."
    h "This pole no good. Is big, very big."
    s "Yes, it's a bit wider than standard but it's fine for practice."
    h "Why is so big? Big stripper dance here?"
    s "Maybe it's just a load-bearing stripper pole?"
    h "What mean?"
    s "You know, load-bearing. As in it holds the building up."
    scene gym_pool_hikari11
    "Hikari jerked back in shock."
    h "No no no. I no dance on...load-b-b-boring pole. I no take risk."
    s "Don't worry Hikari, I was just making a joke."
    s "Come on, I have other members to help out too. Let's get started."
    scene gym_pool_hikari12
    s "(How adorable, she's warming up like she's about to do the 100m dash.)"
    h "Ok I start. No laugh!"
    scene gym_pool_hikari13
    "Hikari began what can only be described as the sort of dancing one does in their room while hoping no one finds out."
    scene gym_pool_hikari14
    s "(Did she mean ballet instead of stripping?)"
    s "Stop for a second."
    scene gym_pool_hikari15
    h "What, no good?"
    s "That was really good Hikari. It was very beautiful dancing. However you're forgetting one thing."
    s "Stripping is about sexuality and seduction. It's a fusion of beautiful dance with the passion of love and lust."
    s "You have to seduce me with your dance."
    "Hikari thought about this for a moment before starting her routine again"
    scene gym_pool_hikari16
    s "(Okay, still silly but a bit better.)"
    s "Excellent, show off those sexy legs."
    scene gym_pool_hikari17
    s "Try to make eye contact. Try to seduce me with your gaze."
    scene gym_pool_hikari18
    h "Like this? You feel the sexy?"
    s "Yes *chuckle*, I feel the sexy."
    s "You have the beauty of the dance and the sexual seduction. You are still missing one part though."
    scene gym_pool_hikari19
    h "What I miss?"
    s "Strippers STRIP."
    "Hikari seemed taken aback by the thought of stripping in public."
    h "I can't strip. I get in trouble! I die from embarrass."
    s "I promise you that you won't get in trouble. You're wearing a bra underneath that top. It's the same thing as wearing a swimsuit or bikini."
    "Hikari bit her lip while considering it."
    s "(Baby steps. A small yes ladder and we'll have her acting more bold in no time.)"
    h "Ok...but only shirt!"
    scene gym_pool_hikari20
    h "Stripper big breast. I small."
    s "That's not true Hikari. Strippers come in all sorts of shapes and sizes. The most important thing is to be sexy and seductive."
    scene gym_pool_hikari21
    h "Why I think I can strip? I stupid girl. I should swim not dance."
    s "Stop with that kind of talk. You are good and you're only going to get better. Now try to incorporate the pole into your routine."
    scene gym_pool_hikari22
    "Hikari began dancing once again. Wrapping her hand around the oversized pole, she executed some half-assed spins."
    s "(She needs more confidence. I may have to lie to her to keep her encouraged.)"
    s "Wow Hikari, that is incredibly sexy. Even as a gay man I'm getting all hot and bothered by you!"
    scene gym_pool_hikari23
    h "*Hehe* You hot bother?"
    s "You're doing an amazing job. Now to finish your routine with a bang. Take off your sweats!"
    h "I say only shirt, no take off pants!"
    s "Strippers don't wear sweats on stage. You will have to get used to this one way or another."
    s "Now take off those pants and shake that butt around!"
    scene gym_pool_hikari24
    s "(All it took was a little more confidence and now she's ditching those ugly sweats.)"
    s "Let's see that booty girl!"
    scene gym_pool_hikari25
    s "Woweee! I'd pay top dollar to watch this show!"
    h "Hehehe"
    scene gym_pool_hikari26
    h "You like my butt? I spread legs show you my butt!"
    s "Wow, incredibly sexy! What else you got?"
    scene gym_pool_hikari27
    h "I see woman on tv do this."
    s "Hikari, you're a natural at this. I think you have some real talent."
    h "Hehe, thank you [s]. I go home and practice very hard!"
    s "(I'll be going home hard as well...unfortunately)"
    s "(At least now we're getting somewhere)"
    $ strip1_hikari = True
    $ pass_time(120)
    jump loc_gym_gym

label hikari_locker:
    $ hikari_locker = True
    if nude_locker_hikari:
        scene locker_hikari_nude1
        s "(Hikari is comfortably naked just like I told her to be.)"
        "Content under development."
        jump loc_gym_locker

    else:
        scene locker_hikari1
        s "(Ooh, Hikari is changing. Maybe I can stay and watch)"
        menu:
            "Watch":
                if nude_locker_hikari:
                    scene locker_hikari_nude1
                    s "(Hikari is comfortably naked just like I told her to be.)"
                    "Content under development."
                    jump loc_gym_locker
                elif Mhikari and strip1_hikari:
                    scene locker_hikari4
                    s "Hey Hikari."
                    h "Oh...hi."
                    s "What's up? You seem nervous."
                    h "I change clothes."
                    s "That's fine, you can change while we talk."
                    scene locker_hikari5
                    h "But you see me naked then!"
                    s "So? A lot of people will see you naked when you get on stage."
                    scene locker_hikari6
                    "Hikari realized the truth of [s]'s statement but still clung tightly to her towel."
                    s "From now on you should not bother with a towel when you're changing. This is a locker room so it's perfectly normal to be naked, and you'll get more comfortable with being nude around people."
                    h "You no laugh at small boobs, ok?"
                    s "Not all men like big breasts, some even prefer smaller ones."
                    scene locker_hikari7
                    "Hikari lowered her towel yet still shielded her breasts from view."
                    s "Just drop the towel, you'll feel better afterwards."
                    scene locker_hikari8
                    h "What you think, I look ok?"
                    s "Wow! You're in such great shape. All that swimming really paid off."
                    h "I-...thank you."
                    s "Come on now, lower your hands."
                    h "I can't, very scary.."
                    s "You have nothing to be scared of. From what I can see, your body looks absolutely perfect."
                    scene locker_hikari9
                    h "You say true?"
                    s "Wow... absolutely perfect. I'm almost speechless."
                    scene locker_hikari10
                    "Gaining confidence from [s]'s praise, Hikari spun around."
                    h "My butt...is also good?"
                    s "Your ass looks absolutely delicious. You're in such great shape."
                    "Further fueled by compliments, Hikari flipped forward displaying her adorable virgin butthole."
                    scene locker_hikari11
                    h "I do dance like this. But tease because no show flower!"
                    s "Where'd you learn that move? That looks great!"
                    scene locker_hikari12
                    h "(I feel like real stripper...heart so beat hard!"
                    scene locker_hikari9
                    s "How do you feel?"
                    h "Very fun, very excite!!!"
                    s "That's great to hear. If you keep this up you'll be able to perform on stage some day soon."
                    h "Thank you [s]!"
                    s "(Hehe...no, thank you my dear!)"
                    $pass_time(60)
                    $ nude_locker_hikari = True
                    jump loc_gym_locker

                elif Mhikari:
                    s "(Come on, show me that sexy tight body of yours!)"
                    scene locker_hikari2
                    h "When you leave?"
                    s "Oh...hi Hikari."
                    scene locker_hikari3
                    h "You leave now."
                    s "(Shit...maybe another time)"
                    jump loc_gym_gym
                else:
                    s "(Someone's changing in here. I should probably leave before they get mad.)"
                    jump loc_gym_gym


            "Leave":
                s "(Better I not risk upsetting her)"
                jump loc_gym_locker

label hikari_nude_pool_sit:
    scene hikari_pool_nude_sit2
    s "Hey Hikari, what's up?"
    h "Hi [s], I just sit and take break."
    h "Very tired from swim."
    s "Ah ok no problem, I'll see you around."
    jump loc_gym_pool

label hikari_new_look_pool_sit:
    scene hikari_new_pool_sit2
    with fade
    menu:
        "Talk":
            s "Whatchya doing?"
            scene hikari_new_pool_sit3
            h "I practice new pose. Very concentrate and focus, no distract please."
            scene hikari_new_pool_sit2
            with fade
            menu:
                "Distract Her":
                    scene hikari_new_pool_sit4
                    with hpunch
                    "*SMACK*"
                    scene hikari_new_pool_sit5
                    h "*Laughing* Eeeeek! Why you do that?"
                    s "Because your ass is too nice to not smack."
                    h "I almost fall in water."
                    s "Good thing you're a swimmer."
                    h "Hehe, this true. Ok tho, I focus. Bye"
                    jump loc_gym_pool

                "Leave":
                    jump loc_gym_pool

        "Leave":
            jump loc_gym_pool

label hikari_stripclub1:
    hide screen ui_icons
    hide screen ui_text
    scene hikari_stripclub_intro1
    with fade
    $ renpy.pause (2)
    scene hikari_stripclub_intro2
    "[s]'s footsteps alerted Hikari of his presence."
    h "[s], I happy I see you!"
    scene hikari_stripclub_intro3
    h "Wait I show you."
    scene hikari_stripclub_intro4
    s "You seem really excited to see me Hikari, what's up?"
    scene hikari_stripclub_intro5
    "Hikari hugs [s] tightly, pressing her breasts against his chest."
    h "Very excite, I practice new dance! I want show, sexy good moves."
    scene hikari_stripclub_intro6
    h "Ok, I make dance. Not a lot practice, not too little. No laugh at me ok?"
    scene hikari_stripclub_intro7
    h "I stick butt back, it make look big."
    scene hikari_stripclub_intro8
    h "Then I show my flower but only a little, not show big yet."
    scene hikari_stripclub_intro9
    h "Then I show flower, make many very excite!"
    scene hikari_stripclub_intro10
    h "Oh my God. I really show you my flower. I suppose to only say that part not do that part."
    h "I so embarrass!"
    s "The whole point of stripping is to show what you have, and you did a great job. That was very brave of you."
    scene hikari_stripclub_intro11
    h "I can't believe I show flower! I shy but show me brave to you!"
    s "I'm really proud of you Hikari. You're on your way to fulfilling your dreams."
    s "We need to celebrate! Can you get ready in 5 minutes and meet me in the lobby?"
    h "Celebrate? So nice, I want to celebrate! Where we go?"
    s "It's a surprise, I'll see you soon."
    scene hikari_stripclub_intro12
    with fade
    h "Oooh, it so nice here."
    h "I feel under dress..."
    s "I think you'll find yourself overdressed in just a moment."
    s "I'll go grab us some drinks, what would you like?"
    h "Bring sake please, thank you."
    s "I don't think they have sake."
    h "Oh... red wine, ok?"
    scene hikari_stripclub_intro13
    with fade
    $ renpy.pause ()
    scene hikari_stripclub_intro14
    with fade
    $ renpy.pause ()
    scene hikari_stripclub_intro15
    with fade
    $ renpy.pause ()
    scene hikari_stripclub_intro16
    with fade
    $ renpy.pause()
    scene hikari_stripclub_intro17
    with fade
    s "Wow, she's good."
    h "She amazing."
    s "As she dances, pay attention to her face. Her eyes are basically inviting those men to get on stage to have sex with her."
    s "Stripping isn't just about getting naked and dancing. It's about making the men watching you forget about everything else. Only you exist in their eyes."
    h "She so strong... she control men."
    scene hikari_stripclub_intro18
    with fade
    $ renpy.pause ()
    scene hikari_stripclub_intro19
    with fade
    $ renpy.pause()
    scene hikari_stripclub_intro20
    with fade
    h "Such power, they do what she want."
    s "One day you too can wield this power."
    scene hikari_stripclub_intro21
    s "This girl's entire image oozes sex. From her hair down to her outfit... {w}if you can even call it an outfit.{w=1.0}"
    s "We're going to have to work on spicing up your looks first."
    h "What wrong how I look? You say I ugly?"
    s "No Hikari, you're not ugly. You're actually as cute as a button. That's the problem though."
    s "Men don't want to think about puppies and kitties (well maybe kitties) when they see a stripper, they want to think about bending them over."
    s "Don't worry though, we'll get you dolled up in no time."
    scene black
    h "Hikari carefully studied the girls as they came on stage. Scribbling notes on napkins like she was preparing for an exam."
    scene hikari_stripclub_intro22
    with fade
    s "Did you have fun?"
    h "So much fun! I learn a lot, maybe one day I be a good dancer too. Make famous and have many fan."
    s "I have no doubts of that. For now let's get some sleep."
    $ hikari_strip_intro = True
    $ pass_time(240)
    jump loc_sophie

label hikari_bartender_help:
    hide screen ui_icons
    hide screen ui_text
    scene hikari_bartender_help1
    with fade
    "[s] entered the strip club, unsure of who he should speak to about Hikari."
    "The club was filled with drunk men and scantily clad women."
    s "(I've never 'pimped out' a woman to a strip club before, where do I even start?)"
    scene hikari_bartender_help2
    ba "Hey you, whatchya drinking?"
    scene hikari_bartender_help3
    "[s] moved closer so that he could be heard over the loud music."
    s "I'm actually not here for a drink, I'm looking for something else."
    ba "Well you've come to the right place for 'something else'."
    ba "As you can see, there's plenty of lovely women here willing to give you some love and affection if you make it worth their time."
    s "No, not that. I'm wondering if you could help me. What do you know about stripping?"
    scene hikari_bartender_help4
    ba "Are you some sort of freak? These girls aren't enough for you so you're trying to get some sort of private action with the staff as well."
    s "No, no, no! That's not what I'm asking at all."
    s "Listen, I have a friend who dreams of being a stripper. I have no idea where to start or how to help her. I'm wondering if you have any advice?"
    scene hikari_bartender_help5
    "The bartender looked at [s] strangely as if he had a dildo stuck to his forehead."
    ba "HAHAHAHA, oh God that's rich."
    ba "I've never met a man at my bar who's actually trying to sell me one of his girls."
    s "I'm not selling you anything. Hikari is a friend of mine who wants to get into stripping."
    s "Are you able to help me out or not?"
    scene hikari_bartender_help6
    ba "You sound too naive to be running a pimp gig on the side."
    ba "Tell you what, bring this 'friend' of yours around sometime and I'll see if she's got what it takes."
    s "Thank you so much, Miss!"
    s "I'll try to get her in here as soon as possible."
    ba "Yeah, yeah... if that's everything then I've got paying customers who are missing my attention."
    s "Of course, thank you. Have a good night."
    scene black
    with fade
    s "(Ok, there's a start. I just now need to get Hikari in here and see where this goes.)"
    $ hikari_bartender_help = True
    $ pass_time(120)
    jump loc_stripclub

label hikari_new_look:
    hide screen ui_icons
    hide screen ui_text
    scene hikari_new_look1
    with fade
    s "(There's our future little stripper.)"
    scene hikari_new_look2
    s "(There's no way the bartender can say no to her when she's got such wonderful assets.)"
    s "Hey, Hikari."
    scene hikari_new_look3
    h "[s], come to say hi?"
    s "More than that, I've got a surprise for you."
    h "I like surprise, what you have?"
    s "Get dressed and come with me."
    scene hikari_new_look4
    with fade
    h "If you tell me we come here, I wear nice clothes not gym stuff."
    s "That's okay, Hikari. You look great regardless."
    s "There's someone I want you to meet."
    scene hikari_new_look5
    ba "Ah, so you must be Hikari."
    ba "Come closer so I can get a good look at you."
    scene hikari_new_look6
    h "Hi... I know you?"
    s "Hikari, she works here. She says she can help you become a dancer here if you'd like."
    h "REALLY? No joke?"
    ba "Well, not exactly. I said I'd take a look at you first."
    ba "Hmmm, to be honest you look a little bit boring."
    h "So mean... "
    ba "Turn around, let's see what else you've got."
    scene hikari_new_look7
    with hpunch
    ba "Damn girl, you've got some top class ass!"
    s "Hikari's quite the little bombshell, she just needs someone to help highlight her features."
    scene hikari_new_look8
    h "So you help or I not pretty for dance?"
    ba "Hmmmm.... "
    h "It ok, I no pretty enough. I understand. Thank you"
    h "Let's go [s], I want go home."
    ba "Whoa now, slow down a bit. I never said that."
    ba "I'm just trying to picture you in a new light, see how we can spruce you up a bit."
    h "So you help?"
    ba "Yes, I help."
    scene hikari_new_look9
    h "YES! REALLY? I can't believe!"
    ba "*Laughing* She's so adorable and innocent, I think we might go to hell for taking her along for this dirty ride."
    s "If I have to go to hell to see her dreams fulfilled then it's worth it."
    h "Aww, you nice boy, [s]."
    ba "Ok, follow me to the back. I'm sure we'll find you something nice to wear."
    ba "Normally the girls do their own makeup before coming here but we'll take care of you tonight."
    scene hikari_new_look10
    s "So I should just wait around here?"
    ba "There are worse places to be stuck waiting."
    ba "Maybe you just need to make a new friend?"
    scene black
    with fade
    "Not long after Hikari left [s] heard someone call out his name."
    scene hikari_new_look11
    with fade
    $ renpy.pause(1)
    woman "[s]?"
    s "Yes, do I know you?"
    woman "No, but you will."
    woman "Why don't you sit down so we can talk?"
    scene hikari_new_look12
    woman "Introductions, well you're [s] and I'm your hearts desire."
    s "I uh, hi... 'Hearts Desire'?"
    woman "What brings you here?"
    s "I'm waiting on my friend, Hikari. She's getting a makeover in the back."
    woman "Oh you poor thing, they left you out here waiting all by yourself?"
    woman "I hope you brought a book or something to kill time."
    scene hikari_new_look13
    "The woman began scanning the room."
    woman "I wish there was somewhere to sit down though so we could continue to get to know each other."
    s "Um, there's plenty of chairs around. I can pull one up for you?"
    woman "No, those chairs aren't very comfortable."
    scene hikari_new_look15
    woman "Feel how soft my bum is? I can't sit on those hard wooden chairs with sensitive skin like this."
    scene hikari_new_look16
    woman "Looks like I'll have to sit on your lap for now."
    woman "You don't mind, do you?"
    s "*Gulp* U-uh, go right ahead."
    scene hikari_new_look17
    woman "I knew you'd be such a wonderful gentleman."
    s "What can I say? Mamma raised me right."
    woman "She sure did. You deserve a reward for that, don't you think?"
    s "Definitely."
    scene hikari_new_look19
    woman "Do you like my ass, [s]?"
    s "I most definitely do."
    woman "Do you think my ass is better than my tits?"
    s "Um, well-"
    woman "What am I saying? You haven't felt them so there's no way you can answer that question."
    "The dancer grabbed [s]'s hands and lifted it to her breasts."
    scene hikari_new_look20
    woman "There, what do you think?"
    s "Don't these places have a no touch policy? I don't want to get kicked out."
    woman "Answer my question, [s]."
    s "I love your tits, they fit perfectly in my hands."
    scene hikari_new_look21
    woman "They do, don't they?"
    woman "I'm proud of these girls, aren't they the most perfect pair of tits you've ever seen?"
    s "Well, that really dep- I mean... yes, they're absolutely perfect!"
    woman "Hmmm, you hesitated there. Maybe you just didn't get a close enough look."
    scene hikari_new_look22
    woman "How about now, aren't they the most perfect pair?"
    s "*Muffled* Yes!"
    scene hikari_new_look23
    woman "When I first saw you, I thought you'd be a big car guy."
    woman "Turns out, you're really into motorboats."
    scene hikari_new_look24
    s "Lame puns as you suffocate me with your tits, are you trying to make me fall in love?"
    woman "*Smirking* No, you're too nice to fall for a girl like me."
    scene hikari_new_look25
    woman "It was nice to meet you, [s]. I hope this wont be our last conversation."
    scene black
    with fade
    "[s] checked his pockets to make sure nothing was missing."
    s "(That's weird, usually my wallet gets lighter because of performances like that.)"
    s "(Did the bartender send her out to entertain me while I wait?)"
    "[s] noticed how much slower time went by when there wasn't a perfect pair of tits in his face."
    "A few beers later, he noticed the girls coming out from the back."
    scene hikari_new_look26
    with fade
    s "(Whoa!)"
    scene hikari_new_look27
    ba "Sorry for making you wait so long... what do you think?"
    s "Wow... Hikari, you look drop dead gorgeous!"
    h "Really? You no think I look silly."
    s "Fuck no! I love your hair and makeup."
    s "Can you do a quick spin for me?"
    scene hikari_new_look28
    s "Careful when you walk around like that, men might accidentally step in front of traffic while staring at your ass."
    scene hikari_new_look29
    h "You just make joke and be nice."
    s "Hikari, you're a bombshell. So when do you get to dance?"
    scene hikari_new_look30
    ba "Hikari and I made a deal earlier. The makeover and clothes are hers to keep, for free. In exchange, she'll perform here next Wednesday."
    ba "She won't be getting paid, it'll just be a trial run to see how she does."
    scene hikari_new_look29
    h "I so excite! Can't wait for Wednesday."
    scene hikari_new_look30
    s "Thank you for setting this whole thing up again, we owe you big time."
    ba "Don't thank me just yet. We'll see how she does on her first night. There's no guarantees, she'll have to earn her spot."
    s "Of course, we understand."
    scene hikari_new_look31
    with fade
    h "I so happy, thank so much [s]!"
    scene hikari_new_look32
    $ renpy.pause(2)
    scene hikari_new_look33
    h "Without you, I only swim and study. Now I feel so excite for life!"
    s "I'm excited for you. I can't wait to see you dance."
    s "Now let's go home, I think we've both had too much excitement for one night."
    $ hikari_new_look = True
    $ pass_time(240)
    jump loc_sophie

label hikari_first_strip:
    hide screen ui_icons
    hide screen ui_text
    scene hikari_stripclub1
    h "I don't know if I ready. What if I no good?"
    s "You'll do amazing, remember all those times you've practiced?"
    h "What if people laugh and go boo?"
    s "No one's going to laugh beca-"
    scene hikari_stripclub2
    ba "Are you guys done with your little pep-talk? It's time."
    scene hikari_stripclub1
    h "But I no ready yet."
    scene hikari_stripclub2
    ba "Look darling, either you get your ass on that stage right now, or you take off your clothes anyways and give them back to me."
    h "... *sigh*"
    scene hikari_stripclub3
    with fade
    "Hikari slowly approached the stage, timid as a mouse."
    s "GO HIKARI! WOOOOOO!!!"
    scene hikari_stripclub4
    h "*Deep breath*"
    scene hikari_stripclub5
    "She began her performance, quickly timing her movements with the rhythm of the music."
    scene hikari_stripclub6
    man "Who's this new hottie?"
    scene hikari_stripclub7
    man "I don't know but I'd love to get my hands on her."
    scene hikari_stripclub8
    $ renpy.pause()
    scene hikari_stripclub9
    man "Look at those perky little tits!"
    scene hikari_stripclub10
    man "Yeaaaaaaah girl, take it off!"
    scene hikari_stripclub11
    man "Holy fuck, I could open a beer with that ass!"
    scene hikari_stripclub12
    woman "Damn, you're making me jealous, girl!"
    scene hikari_stripclub13
    $ renpy.pause()
    scene hikari_stripclub14
    $ renpy.pause()
    scene hikari_stripclub15
    man "She did it! SHOW US WHAT YOU GOT!"
    scene hikari_stripclub16
    "Bills were flying and littering the floor as Hikari's show came to an end."
    scene hikari_stripclub17
    man "I LOVE YOU, COME BACK!"
    s "Wow Hikari, you did amazing!"
    scene hikari_stripclub18
    h "Eeeeeeeeeeeee!!!!!"
    "Hikari squealed like an excited piggy as she ran towards [s]."
    scene hikari_stripclub19
    h "You see they cheer? They like so much. They think my dance sexy!"
    s "Your dance was beyond doubt sexy. My pants feel so much tighter now."
    scene hikari_stripclub20
    ba "You did good kid. I think we can make room for you every Wednesday here if you'd like, paid."
    scene hikari_stripclub19
    h "Wow! I real stripper?... "
    $ renpy.pause(2)
    h "I REAL STRIPPER!"
    s "You're a real stripper!"
    scene hikari_stripclub21
    with fade
    h "I like you so much. You best guy, so nice for me!"
    s "I like you too. Now let's get dressed and head home. We'll have plenty of time to celebrate in the future."
    $ hikari_first_strip = True
    $ pass_time(180)
    jump loc_sophie

label hikari_strip1:
    hide screen ui_icons
    hide screen ui_text
    scene hikari_stripclub5
    with fade
    $ renpy.pause()
    scene hikari_stripclub6
    man "What a hottie!"
    scene hikari_stripclub7
    man "I'd love to get my hands on her."
    scene hikari_stripclub8
    $ renpy.pause()
    scene hikari_stripclub9
    man "Look at those perky little tits!"
    scene hikari_stripclub10
    man "Yeaaaaaaah girl, take it off!"
    scene hikari_stripclub11
    man "Holy fuck, I could open a beer with that ass!"
    scene hikari_stripclub12
    woman "Damn, you're making me jealous, girl!"
    scene hikari_stripclub13
    $ renpy.pause()
    scene hikari_stripclub14
    $ renpy.pause()
    scene hikari_stripclub15
    man "She did it! SHOW US WHAT YOU GOT!"
    scene hikari_stripclub16
    "Bills were flying and littering the floor as Hikari's show came to an end."
    $ pass_time(60)
    jump loc_stripclub

# MARIA
label maria_treadmill_intro:
    $ maria_treadmill = True
    scene maria_tread1
    s "(Not sure how I can help someone on a treadmill, but lets see if we can find out more about her)"
    s "Hello."
    who "(hmmm?)"
    scene maria_tread2
    who "Oh, hi sugar."
    who "(Oh lord have mercy, this boy's delicious)"
    s "I didn't mean to interrupt your cardio. I just wanted to introduce myself."
    s "My name's [s] and I'm the new personal trainer here."
    scene maria_tread4
    who "Oh yeah, Daisy told me that we have a new toy in the gym."
    s "I'm sorry.. a new toy?"
    s "(Did she just check me out?)"
    scene maria_tread5
    who "BOY! We have a new boy in the gym!"
    s "I hope the girls will be comfortable with a guy around here."
    s "I intend to bring a new experience without jeopardizing everyone's comfort around here."
    scene maria_tread3
    who "Don't worry hun, if anyone gives you any problems. You just come to me and Mamma Maria will take care of everything!"
    s "Thanks! I want you to use me as a resource. If you have any questions or need any help, feel free to holler at me."
    scene maria_tread4
    m "*muttering* Oh I'll definitely use you boy..."
    s "Hmm, what was that?"
    scene maria_tread5
    m "I said I'll definitely use you as a resource! It's nice to meet you hun!"
    s "Same here, have a good workout Maria!"
    s "(What an...interesting lady)"
    $ Mmaria = True
    $ pass_time(60)
    $ Omaria += 1
    jump loc_gym_gym

label maria_treadmill:
    $ maria_treadmill = True
    if finger_maria:
        scene maria_tread1
        s "(Maria's doing her daily run.)"
        menu:
            "Chat":
                s "Come on Maria, my grandma runs on a faster setting than that."
                scene maria_tread2
                m "I'm just sore that's all....maybe I need a massage to get these old legs working again. *wink*"
                s "Ha, there's a time and place for everything."
                scene maria_tread4
                m "Mmm...guess I'll have to be at the right place and time then."
                s "Never change, Mamma Maria... never change."
                jump loc_gym_gym

            "Leave":
                s "(No need to bother her now)"
                jump loc_gym_gym

    elif Mmaria:
        scene maria_tread1
        s "(Maria's doing her daily run.)"
        menu:
            "Chat":
                s "Come on Maria, my grandma runs on a faster setting than that."
                scene maria_tread2
                m "Huh? Oh you little shit."
                m "In spite of that comment, I'm going to take a break."
                scene maria_tread3
                m "So, did you come here to tease an old woman?"
                s "Old woman my ass. If I wasn't gay I'd probably stand in this very spot and watch you run all day."
                scene maria_tread4
                m "*muttering* mmm... if only you weren't gay.."
                s "What'd you say?"
                scene maria_tread5
                m "I said 'If only I could run all day!'"
                m "Speaking off, break time's over. Thanks for chatting with me [s]!"
                s "(This woman has a hunger in her eyes that almost scares me.)"
                $ Omaria += 1
                $ pass_time(120)
                jump loc_gym_gym

            "Leave":
                s "(No need to bother her now)"
                jump loc_gym_gym

    else:
        jump maria_treadmill_intro

label maria_shower_sex_views:
    menu:
        "View 1":
            scene maria_shower_sex1_anim
            with fade
            $renpy.pause()
            jump maria_shower_sex_views
        "View 2":
            scene maria_shower_sex2_anim
            with fade
            $renpy.pause()
            jump maria_shower_sex_views
        "Cum on her back":
            scene maria_shower8
            s "I'm gonna cum....are you ready?"
            s "I'm gonna cum a load on your back!"
            m "Mmmmm, cum for Mamma Maria. Make me cum!"
            scene maria_shower10
            s "At least clean up should be easy this time around."
            scene maria_shower11
            m "How considerate. Go on and get out of here, boy. Mamma needs to catch her breath."
            s "Till next time Maria. *wink*"
            $ sex_maria = True
            $ pass_time(60)
            jump loc_gym_locker
        "Cum in her":
            scene maria_shower8
            s "I'm gonna cum..."
            m "Mmmm, I want you to cum in me. Fill up Mamma Maria! Let me feel your hot young cum inside me."
            "Hearing Maria talk like that sent [s] over the edge as he fired round after round into Maria until his juices started leaking out of her."
            scene maria_shower9
            s "At least clean up should be easy this time around."
            scene maria_shower11
            m "How considerate. Go on and get out of here, boy. Mamma needs to catch her breath."
            s "Till next time Maria. *wink*"
            $ sex_maria = True
            $ pass_time(60)
            jump loc_gym_locker

label maria_shower:
    $ maria_shower = True
    scene maria_shower1
    if finger_maria:
        s "(Maria's eyes are closed, maybe I can do something here...)"
        menu:
            "Jump in":
                scene maria_shower3
                "[s] took off his clothes and got behind Maria as quietly as possible. It wasn't until his hands were on her hips did she notice him."
                scene maria_shower4
                m "Hmmm...who could that be?"
                s "You know exactly who it is."
                m "...and what does that boy want?"
                scene maria_shower5
                "[s] placed his erect penis between Maria's cheeks and suggestively rubbed it up and down."
                s "You know exactly what I want."
                scene maria_shower6
                "Kisses rained down her neck as [s] carefully moved Maria into a more accessible position."
                scene maria_shower7
                m "Mmmmmm....don't tell me you're here for another massage, boy."
                s "Oh no, Mamma Maria...not this time."
                scene maria_shower8
                "[s] bent Maria over the splash guard and entered her with little effort."
                s "Well look at that...soaking wet already."
                m "*mmphh* Boy... I was wet the moment I heard you enter."
                scene maria_shower_sex1_anim
                with fade
                "Slow and steady thrusts put a halt to any further conversation."
                s "(I can't believe this is happening. I'm fucking the sexiest GILF on the planet.)"
                s "(I've never felt an ass like this before. If I was fired today, it'd still be worth it.)"
                jump maria_shower_sex_views

            "Leave":
                jump loc_gym_locker

    elif Mmaria:
        s "(I still can't believe she has such a remarkable body for a woman of her age.)"
        s "(Fuck that, for a woman of ANY age.)"
        s "(That gigantic perfect bubbly ass... those beautiful big tits that I'd love to wrap around my dick.)"
        scene maria_shower2
        m "Next time you come to stare, at least be polite and say hello."
        s "(..huh? Oh shit!)"
        s "I-uh...I wasn't... I mean."
        m "Why don't you go back out to the lobby and see if you can find your tongue."
        s "...sorry Mamma Maria."
        jump loc_gym_gym

    else:
        s "(Holy hell this woman's body is absolutely insane!)"
        s "(That perfectly plump ass! She'd shatter my hips to dust if she rode me and I'd have no regrets."
        s "(I wish I could see those tits though. Probably best that she doesn't turn around.)"
        scene maria_shower2
        who "I don't know where you come from boy, but I was raised to not spy on people when they shower."
        s "(..huh? Oh shit!)"
        s "I-uh...I wasn't... I mean."
        who "Why don't you go back out to the lobby and see if you can find your tongue, hun."
        s "...*gulp*"
        jump loc_gym_gym

label maria_yoga1:
    hide screen ui_icons
    hide screen ui_text
    scene maria_yoga1
    "Maria's stretching on the ground."
    s "Hey again Maria, how's everything?"
    scene maria_yoga2
    m "Oh hey [s], just trying to stretch out my leg."
    m "My thigh has been cramping up lately, can you help?"
    s "Sure, what do you need me to do?"
    m "Just come down here and help push me back a bit."
    scene maria_yoga3
    s "Is this too much?"
    m "Not at all hun, if anything, can you go down lower?"
    scene maria_yoga4
    s "Like this?"
    m "Yeah baby, that's good. But I'm gonna need you to push down lower."
    scene maria_yoga5
    s "Alright Maria, I can't possibly go any lower. Are you getting a good stretch now?"
    m "Lower."
    s "What?"
    s "Are you sure Maria? I'm already at the bottom of your thigh."
    m "Yes and I need you to go lower."
    s "Umm..."
    "[s] hesitated to go any further lower. As much as he'd like to explore her body, surely she doesn't want him to grab her by the pussy."
    m "(It's so cute watching him squirm.)"
    scene maria_yoga6
    "Maria reached out and stroked [s]'s crotch."
    "[s] jumped back out of surprise."
    s "Whoa!"
    m "See? It's not a big deal. Now can you do what I ask?"
    s "(Alright, she can't be any clearer than that.)"
    scene maria_yoga7
    s "Like this, Maria?"
    m "Exactly. I'm starting to feel the cramp loosen up, thanks."
    scene maria_yoga8
    m "That's exactly what I needed. I can do the rest of these exercises by myself."
    s "Uh, sure. Glad to be of help."
    s "(Damn that was weird. Somehow I feel... victimized?)"
    $ pass_time(120)
    $ maria_yoga1 = True
    jump loc_gym_yoga

label maria_sauna1:
    $ maria_sauna = True
    if finger_maria:
        scene maria_sauna1
        "Maria occupied the top step of the sauna, leaning against a wall unaware of [s]'s entrance."
        "Her eyes sprang open as he approached."
        s "Hey Maria, mind if I join you?"
        m "Please do, I enjoyed your company last time..."
        m "In fact...mind giving me another massage while you're in here?"
        menu:
            "Yes":
                s "Of course not, please lay down."
                scene maria_sauna6
                s "I think we can go ahead and skip the towel formalities."
                "[s] removed the towel and began re-exploring Maria's body."
                scene maria_sauna18
                m "Mmmmhmm."
                scene maria_sauna19
                "After some time, [s] asked Maria to flip over."
                scene maria_sauna21
                s "I don't think I'll ever get tired of this amazing body."
                m "You make an old woman very happy saying such sweet things, boy."
                scene maria_sauna22
                s "These tits are so hefty yet firm. Do you drink virgin blood to maintain your youth?"
                scene maria_sauna23
                m "Not quite dear. Although I did hear that cum is great for the skin."
                scene maria_sauna30
                "With that, Maria grabbed a hold of [s]'s towel and lowered it."
                scene maria_sauna31
                m "Looks like we're on the same page."
                scene maria_sauna33
                m "You making me so wet."
                scene maria_sauna_hj2_anim
                with fade
                "Sounds of Maria's wet pussy and moaning filled the room."
                m "Mmm...we should... make this a regular thing... don't you think?"
                scene maria_sauna_hj_anim
                with fade
                s "I have a feeling you wouldn't let me say no even if I wanted to."
                scene maria_sauna35
                m "That's right boy..*moan*... you're my toy now."
                "Ecstasy flushed over Maria as she reached her climax."
                s "I- I'm gonna come!"
                scene maria_sauna36
                "Upon hearing that, Maria picked up her pace till her arms were burning sore."
                m "Yesss... give Mamma Maria everything you got."
                scene maria_sauna37
                "Cum hit Maria's ribs and breast as [s] leaned against her for support."
                m "Oooh baby! Going to the gym got so much better since you've started working here boy!"
                s "I can honestly say that this is the first time in my life that I'm enjoying work."
                "Maria began cleaning up and heading towards the door."
                m "Until next time, suga."
                $ pass_time(180)
                jump loc_gym_sauna


            "No":
                s "Sorry Mamma, I have some things I need to take care of."
                m "Bummer, we could have taken care of things together."
                jump loc_gym_sauna
    elif Mmaria:
        scene maria_sauna1
        "Maria occupied the top step of the sauna, leaning against a wall unaware of [s]'s entrance."
        "Her eyes sprang open as he approached."
        s "Hey Maria, mind if I join you?"
        m "Of course you can, sit down hun."
        m "Are you enjoying working here?"
        s "I absolutely love it! Great staff, great patrons."
        m "..but Mamma Maria is your favorite right?"
        s "Of course! No one comes close to Mamma Maria!"
        scene maria_sauna4
        m "Ha! I know you're just teasing me boy, but this old crow still appreciates it!"
        s "I'm not joking. You're so warm and authentic and make me feel appreciated."
        scene maria_sauna2
        m "Of course hun! You're putting in a lot of work, motivating the girls to push harder."
        m "That's why I'm in this sauna. My poor muscles need some relief."
        s "You know, I could give you a massage while we're here."
        s "(Maybe I'll finally get to see what's under that towel)"
        "Maria entertained the offer for her body was sore and welcomed the relief. Yet a tinge of shame and guilt seemed to hover."
        "Could she truly let a boy half her age run his hands across her body with nothing but a towel for cover?"
        scene maria_sauna5
        m "I appreciate the offer hun, but are you sure you want to do that?"
        s "Why? I'm an asset at this gym and you're a patron."
        s "Part of my skillset is offering killer massages."
        m "(I was just messing with him earlier, could he actually be serious?)"
        "An awkward moment passed before Maria broke the silence."
        scene maria_sauna2
        m "You're right hun. My old bones and muscles are aching and could use a good rub."
        m "You are an asset of this gym and it would be silly for me to not use you, right?"
        s "Absolutely."
        scene maria_sauna6
        "Maria adjusted her towel, careful to not reveal herself as she laid face down on the bench."
        "Despite her caution, [s] noticed her breast spilling out from under the weight of her body."
        s "I'll start off up top. If you feel any discomfort let me know."
        scene maria_sauna7
        m "(Mmm, I can't remember the last time I've had a massage)"
        s "You have a lot of tension in your neck Maria."
        m "That's what happens when you're chasing tots around the house all day."
        scene maria_sauna8
        "Maria hardly noticed the towel finding its way further down her back as she fell deeper into relaxation."
        s "So then why's your back tense?"
        m "You try being down on all fours while someone's riding you on top."
        "Maria lightly blushed as the sexual innuendo dawned upon her."
        s "I'm more of a pitcher, not a catcher."
        scene maria_sauna9
        m "Hahaha. I was referring to the little ones running rampage."
        s "How old are your kids?"
        m "18 and 22."
        s "Don't you think they're a little bit too old to be riding mamma's back?"
        m "[s], you're lucky you're handsome 'cause you sure as hell ain't bright."
        m "I've got two grandkids."
        s "Bullshit. You're not a grandma."
        m "You better believe it, Mamma Maria is a nanna."
        s "You're fucking with me. You don't look like a grandmother."
        m "Black don't crack, hun."
        m "..and watch your mouth."
        m "I had my daughter real young. She took after her mamma and had her kids young too."
        scene maria_sauna10
        "[s]'s hands worked their way down Maria's back, carefully avoiding her butt along the way to her legs."
        s "You're absolutely the sexiest grandma I've ever laid eyes on."
        s "...and I still don't believe your story."
        m "Believe what you want baby."
        scene maria_sauna11
        s " How's this feel, not too much pressure?"
        m "Mmmm, absolutely perfect...relaxing"
        scene maria_sauna12
        s "(Her legs are in such great shape. So meaty but firm.)"
        "Feeling confident, [s] slowly worked his way up Maria's legs and inner thighs."
        scene maria_sauna13
        m "Mmmmm"
        "Maria began breathing heavily as the relaxing massage awoke other parts of her body."
        s "(Is she getting turned on?)"
        scene maria_sauna14
        s "(Let's see if I can spread her legs a bit...)"
        scene maria_sauna15
        "[s] gently grabbed Maria's legs and began to pry them apart."
        "Nearly effortlessly, her legs parted as his hands began inching towards their destination."
        menu:
            "Should I push my luck?"
            "Yes, worth a shot":
                if maria_yoga1:
                    scene maria_sauna16
                    "[s] placed a hand on her firm butt and began questioning his boldness."
                    "Will she allow him to continue, or is this where it all ends?"
                    s "Mamma Maria, is this ok?"
                    scene maria_sauna17
                    m "Mmm, definitely inappropriate."
                    m "Keep massaging."
                    scene maria_sauna16
                    "They both knew that a line was being crossed yet no objections were made."
                    "The towel remained the only barrier between innocence and lust."
                    s "Should I go ahead and remove your towel? It will make it much easier for me to continue."
                    scene maria_sauna17
                    m "Go ahead. You're doing the lords work here honey."
                    m "(What the hell's wrong with me? Why am I letting this boy run his hands freely all over my body?)"
                    scene maria_sauna18
                    "The towel dropped to the floor no sooner than [s] dropped his jaw."
                    "He was looking at the body of a woman in her prime. How could she be a grandmother?"
                    scene maria_sauna19
                    s "Mamma Maria, how in the world are you in such great shape?"
                    m "I go to the gym from time to time..."
                    scene maria_sauna18
                    s "Ahuh...do you do squats in your sleep too?"
                    scene maria_sauna20
                    "Maria was now laying absolutely naked before [s], yet both parties played to the guise of innocence."
                    "His fingers would occasionally graze her lips and a soft moan would escape her."
                    s "I think we're all done here. Do you want to flip over so I can do your front?"
                    scene maria_sauna21
                    "Without a word Maria turned over, exposing her breasts and a stifled smile."
                    m "Now don't get too excited by the sight of the girls, boy."
                    scene maria_sauna22
                    "The facade was up, [s] filled his hand with her right breast."
                    s "I'm gay remember?"
                    s "Not getting excited, simply doing my job."
                    scene maria_sauna23
                    m "Ahuh... and how far does this job go?"
                    "Sprawled out naked while her body's being fondled, Maria somehow managed to still stay in control."
                    scene maria_sauna24
                    s "It goes as far as it needs to. My job is to make sure you're absolutely relaxed with no tension in your body."
                    scene maria_sauna25
                    m "Mmmm, then why are you fondling my breasts?"
                    s "I'm just finding it hard to believe that a grandma has the tits of a 25 year old."
                    scene maria_sauna26
                    m "My tits?...is that a professional term we're using now?"
                    "Her body was on fire. Not able to resist any longer, Maria reached out and grabbed [s] by the waist."
                    m "Since this is just a professional massage, could you give my pussy some attention too?"
                    m "I have a lot of tension there, it's putting stress on my back."
                    scene maria_sauna27
                    "And with that she spread her legs further, giving full access to her glistening pussy."
                    scene maria_sauna28
                    "Not one to refuse a sexy woman's advances, [s] did as he was told."
                    "Two fingers made their way to her entrance while his thumb found her clit."
                    s "Is pussy a professional term now?"
                    m "Mmmmm, yes. You're performing a much needed service on me hun."
                    scene maria_sauna29
                    "Maria's soaking wet pussy allowed [s] to slide two fingers in with ease."
                    m "Ohhh God yes!"
                    s "Mamma Maria, I didn't know you enjoy the touch of a gay man so much!"
                    m "Enough with the bullshit...mmf-... You're not gay."
                    "Caught off guard, [s] wondered if she knew?"
                    "His body stopped all movement as panic took over."
                    s "I-uh... I AM gay. What do you mean?"
                    m "Yeah right. You may be fooling the other girls here, but Mamma Maria has been around long enough to know a thing or two about men."
                    s "Maria, I promise you.. I'm gay!"
                    m "It's MAMMA Maria to you..."
                    scene maria_sauna30
                    "She grabbed the front of the towel and ripped it down"
                    m "..and your friend here is telling me that you're lying. Don't lie to me again."
                    s "No, it's just that...you're so sexy and-"
                    scene maria_sauna31
                    "As [s] stammered out an excuse Maria wrapped her hand around his cock"
                    m "Shush boy, just shut up and enjoy this. I don't mind."
                    "She stroked his cock while he stood paralyzed with fear"
                    s "(Fuck! I'm an idiot. Am I going to get fired before even accomplishing anything around here?)"
                    m "Do I need to insert quarters into you to get you working again? Come on boy, get to it!"
                    scene maria_sauna32
                    "Snapping out of his paralysis, [s] started pumping fingers into her as he pulled on her nipples"
                    m "Mmmm, much better Mr. 'Gay' man."
                    scene maria_sauna33
                    s "(If she keeps this up, I'll end up glazing this place.)"
                    "Maria started panting heavily and thrusted her hips up and down"
                    scene maria_sauna_hj2_anim
                    with fade
                    "The room filled with the sounds of Maria moaning and the wet noises of [s]'s fingers blasting her pussy."
                    scene maria_sauna_hj_anim
                    with fade
                    s "(Fuck. She's so good at giving handjobs. If I wasn't knuckle deep in her pussy already, I would have suspected that she has a dick of her own to practice with.)"
                    scene maria_sauna35
                    m "Ahhhhhhh"
                    "Maria's screams of ecstasy drove [s] over the edge"
                    s "I'm cumming Mamma Maria.. I'm cumming!"
                    scene maria_sauna36
                    "[s] started shooting a load onto Maria's chest as she made no effort to direct him elsewhere"
                    scene maria_sauna37
                    "The first shot hit her directly in the rib while the second blessed the side of her breast."
                    "Cum ran down the side of her body as both fought to catch their breath."
                    m "Now that's what I call a massage. Too bad you're a child who makes a mess."
                    s "You're the one who caused the mess. I'm innocent."
                    m "Ahuh, you're the poster child of innocence. Now I got to go clean myself up like I'm your damn mamma."
                    s "Sorry MAMMA Maria."
                    m "Oh you're funny boy."
                    "Trying her best to contain the cum from dripping onto the floor, Maria waddled out of the sauna wearing a satisfied grin."
                    $ pass_time(180)
                    $ finger_maria = True
                    jump loc_gym

                else:
                    scene maria_sauna16
                    "[s] moved his hands under the towel and firmly grabbed Maria's butt."
                    "Maria suddenly jolted up and grabbed her towel. She didn't appear to be angry but there was a look of disapproval on her face."
                    m "Thanks hun, that's exactly what I needed. I think that's enough for today."
                    s "(Well, things could have gone worse.)"
                    $ pass_time(180)
                    jump loc_gym

            "No, it's too risky":
                "[s] continued massaging Maria's legs without delving into any risky business."
                scene maria_sauna17
                m "Mmm, thanks for the great massage. Mamma needed that."
                $ pass_time(180)
                $ Omaria += 1
                $ Lmaria += 1
                jump loc_gym

    else:
        show maria_sauna_idle
        s "(I haven't met her yet. Now while she's relaxing naked under a towel may not be the best time to introduce myself.)"
        jump loc_gym_sauna

label maria_hikari1:
    hide screen ui_icons
    hide screen ui_text
    scene maria_hikari_event1
    with fade
    s "Hey Mamma Maria, got a moment?"
    m "Anything for you suga, what's up?"
    s "I need your help with something...naughty."
    scene maria_hikari_event2
    m "Mmmm, I thought you might. Does it have anything to do with me showering? *wink*"
    s "No, no... I need your help with Hikari."
    scene maria_hikari_event1
    m "Hikari? Now hold it right there hun. I like the things we do together, but don't drag innocent little Hikari into this."
    s "No Mamma, it's not like that. She wants to be a stripper but doesn't have the courage to do it."
    s "We've been working on it for some time now, but I think you'll be able to help her further along."
    "Maria's face lit up with laughter as if [s] was the world's funniest man."
    m "Hikari a stripper? Good lord, why you playing games with me?"
    s "I'm serious! She said that she thinks stripping is some form of art, like a ballerina."
    s "She also looks up to the power they have over men."
    m "No shit? Are you fucking with me, boy?"
    s "You know I'd never pass the opportunity to do just that, but this is not one of those moments."
    m "Ok, I'll bite. What'd you have me do?"
    scene black
    "[s] carefully laid out his plan for what would take place later that day."
    scene maria_hikari_event3
    "The pool was quiet aside from the soft splashes of Hikari floating on her back."
    "Her comfort with her own nudity was an achievement in itself. Something that would seem nearly impossible to [s] not too long ago."
    scene maria_hikari_event4
    s "Hey Hikari, that looks comfortable. How long have you been in here?"
    h "Hi, [s]. I don't know. I love to float on back and think. Very much relax."
    s "Well you look great doing it. Doesn't being nude feel so nice... so free?"
    h "*Giggle* Yes, I feel free. So much thanks to you!"
    scene maria_hikari_event5
    "It wasn't until Maria was almost within reach of [s] that Hikari realized her presence."
    "She swam to the pool's edge frantically, trying in vain to gain cover behind the tiles."
    scene maria_hikari_event7
    m "Hey [s]... hey Hikari. You guys going swimming?"
    scene maria_hikari_event6
    h "H-hi Maria. Why you here?"
    scene maria_hikari_event7
    m "I was just in the sauna and it got heated in there, girl. Thought I'd come here an-... are you naked?"
    scene maria_hikari_event6
    h "NO! I'm.. it's jus-"
    scene maria_hikari_event7
    m "Oh, relax girl. There's nothing wrong with being naked. Feeling the cool water touch your body."
    m "As a matter of fact, that's not a bad idea."
    scene maria_hikari_event8
    "Maria threw off her towel, revealing her age defying body."
    m "Much better."
    m "Now why don't you come out of there so I can get a good look at you?"
    scene maria_hikari_event6
    h "No... I can't."
    s "She doesn't feel comfortable doing that, Mamma."
    scene maria_hikari_event9
    m "Don't talk about comfort when you're sitting there with your shirt on like a buffoon. It's a pool, let's get this off."
    m "Now why would she be scared to come out? Looks like she got a nice tight body from where I'm standing."
    s "She does have a great body, but she's too self conscious about it."
    s "Which is funny, considering that she dreams of becoming an exotic dancer."
    scene maria_hikari_event10
    h "NO! [s], why you say... how you tell her?"
    m "What? She wants to dance naked, but she's afraid of being naked? Now that don't make a lick of sense."
    m "It's ok if we see your body Hikari. It's completely natural."
    m "Would it help if we were all naked?"
    "Maria smirked at [s] as she reached for his waistband."
    s "Wait, Mamma Ma- "
    m "Hush, boy."
    scene maria_hikari_event11
    s "I really felt like I had a say in this, but I'm not one to argue with Mamma Maria."
    m "See? Nothing embarrassing about this."
    "Hikari's eyes widened as she saw [s]'s erect penis."
    "Maria must have realized the possibility that Hikari has never seen a penis up close."
    m "Sweet child, you look like you've just seen a ghost. Have you never seen a dick in person?"
    "Hikari began stammering before Maria cut her off."
    scene maria_hikari_event12
    m "Lucky for you, we have one right here to examine."
    m "Now, not all dicks are as good looking as this one."
    s "That was the kindest thing anyone has ever said about me."
    m "Maybe that's because there's not much else to say about you?"
    s "Ouch. If we weren't in a pool I'd be looking for the nearest burn center."
    m "Come closer, Hikari."
    scene maria_hikari_event13
    "Hikari froze in fear. A relaxing swim in the pool had turned into an exhibition and she somehow found herself to be the front row guest."
    m "Oh, quit being so childish and swim on over already."
    scene maria_hikari_event14
    "Hesitantly, Hikari swam over, unsure of what's to come."
    "Soon she found herself eye to 'eye' with [s]'s member."
    m "It's nice to look at, right?"
    h "Y-yes..."
    m "Good, good. If you want to become a stripper, you will need to get used to seeing these."
    m "It may be overwhelming at first, but this is how you control a man."
    m "If his dick is hard, you've got his heart. Remember that."
    m "Feel free to touch it, get used to how it feels."
    scene maria_hikari_event15
    "Hikari reached out, mesmerized by what was in front of her."
    h "It feel hard, but soft. How you walk like this?"
    s "*Laughing* Well it's not always hard like this Hikari. Do they not teach sexual education in Japan?"
    h "My parents think it bad stuff. Take me from class."
    h "Why it not always hard? Why hard now?"
    s "Because I'm sitting next to two beautiful and naked women."
    h "It hard because we sexy?"
    scene maria_hikari_event16
    m "*Whispering* I can't tell if this is the cutest or the sexiest thing I've ever seen in all my years."
    s "*Whispering* I can't tell if I should love you or be terrified of you, but damn you're good."
    m "*Whispering* You can always thank me later in the shower."
    h "You say something?"
    m "Yeah, I was just saying how I think it's time for you to come on out and show us what you got."
    scene maria_hikari_event17
    "Hikari hesitated, but ultimately climbed out of the pool with an adorable 'Tada!' as she jumped to pose."
    scene maria_hikari_event18
    "Her eyes locked with [s]'s penis once more, as she studied it from another angle."
    m "Damn sista, you looking real nice!"
    h "Thank you Maria. You look very nice too!"
    h "I like your breast, very big and nice!"
    scene maria_hikari_event19
    m "What do you think, [s]? If you had to choose, would you go with Hikari's sexy tight body, or this old ladies saggy ass?"
    s "That's like asking me if I'd rather live without food or water, the decision is impossible."
    m "You got quite a silver tongue there, boy."
    m "Anyways, I think it's time for me to leave. Been real nice hanging with you both."
    h "Bye, Mamma Maria!"
    scene maria_hikari_event20
    s "So... what do you think? Was that a good experience for you?"
    scene maria_hikari_event21
    h "Very good. Maria so nice and strong. I want be strong like her!"
    scene maria_hikari_event20
    s "Don't worry, you'll get there. It takes time to become that confident."
    s "I'm really proud of you, Hikari. You've come so far in such a short time."
    scene maria_hikari_event21
    h "Because of you. You make me stronger. Thank you [s]."
    scene black
    "The two of them discussed Hikari's growth for a while longer before heading their separate ways."
    $ hikari_maria1 = True
    $ pass_time(540)
    jump loc_gym_pool

### STRIP CLUB
label bartender:
    hide screen ui_icons
    hide screen ui_text
    scene stripper_bartender
    who "Hey hun, this club is still under construction so there's not much for you to do... unless you've progressed the story of a certain girl and know what night she works."
    jump loc_stripclub
# GYM INTRO
label gym_first_time:
    hide screen ui_icons
    hide screen ui_text
    scene gym_first1
    "The gym wasn't particularly impressive from the outside. Looked less like a gym and more like a warehouse."
    "It was clear that discretion was the goal for the location. The lobby however, was a luxurious contrast to the exterior."
    "A marvelous black marble floor led up to the reception desk sitting against a backdrop of pink and black."
    "At the seat was a young girl who looked to be no more than 18."
    s "(A young tight body. So far so good.)"
    "([s] realized that he had not prepared for infiltrating this feminine lair.)"
    s "(Hello there! I’d like to work in this ALL WOMEN’S gym, maybe even impregnate a client or two.)"
    "As he questioned himself and his ability to pull this off, the young girl looked up at him quizzically, unsure of his presence."
    scene gym_first2
    who "Hello…how many I help you?"
    s "I’m looking to apply for a job. Is the manager available?"
    "The girl's expression further delved into confusion. As if the pink walls were not enough to convey the intended demographic."
    scene gym_first3
    who "You do know that this is an all women’s gym right?"
    who "Like...just for ladies."
    s "Did you just assume my gender?"
    who "I... uh- no?"
    s "It's 2018 and I can't believe that people still assume a person's gender!"
    scene gym_first4
    "The girl held back her laughter, unsure if this was some silly prank someone's boyfriend was trying to pull."
    who "Uh, ok. What’s your name?"
    s "I’m [s]."
    who "But [s]'s a boys name!"
    "[s] feigned anger and glared at the girl."
    who "Ok-ok! I’m Daisy. Uh...give me just a second."
    scene gym_first5
    s "(Did that really work? Is she that stupid or am I a damn natural actor?)"
    s "(I never thought identity politics would come to the rescue.)"
    scene gym_first6
    "Daisy returned just as quickly as she left. She was intrigued as to what was happening."
    ds "The manager will see you now, this way."
    s "Great, thanks Daisy."
    scene gym_first7
    dn "Hi, you must be [s]. My name’s Dani."
    "A gorgeous woman awaited at the table. A beautiful olive complexion, her unbuttoned shirt revealed that she wasn't wearing a bra."
    "She appeared more competent than Daisy."
    dn "So Daisy tells me that you're looking for a job. She also tells me that...you're a woman?"
    s "Yeah...about that."
    s "I told her that just so she'd let me see you."
    dn "Ok...so you lied. Not the best first impression."
    dn "So why are you trying to work here?"
    s "I understand that women get harassed at gyms all the time."
    s "Sometimes a girl just wants to workout without worrying about being harassed or sexualized."
    s "This gym is a safe haven for those who want to focus on their health without distractions."
    scene gym_first8
    "The answers resonated with Dani. She subtly nodded her head with every talking point."
    s "I’m gay which means I will not be objectifying these women. I also want a place where I can focus on my own health without worry."
    s "Woman get hit on by men at gyms, gay men get mocked and physically assaulted."
    s "I not only understand the women here and the safety that this sanctuary provides, but I dream of a haven like this for myself as well."
    scene gym_first9
    "Dani sat upright at full attention, caught off guard by what was said."
    dn "Wow, I had no idea. You might fit our work culture, but what are your qualifications? You didn't bring a resume."
    s "To be honest, my work experience is in the office setting. However, as you can see, I’m in great shape."
    s "I take my health and fitness very seriously and have a lot of knowledge regarding nutrition, cardio and core training."
    dn "We already have certified trainers. What's something new that you can bring to the table?"
    s "I can build a strong personal connection with your clients."
    s "Not only can I provide enrichment to their physical health, but to their mental health as well."
    s "Every girl needs a good gay friend to bring a guy’s perspective. We’re great listeners!"
    scene gym_first10
    "Dani let out a laugh. She seemed to be disarmed by the very person she was entertaining to toss out moments earlier."
    dn "You have a point. I like you [s], but I still have concerns. I don't know how the girls here will react to you."
    dn "You’re also not certified."
    s "Ok, how about this? Let’s do a trial period. Give me a little time to prove myself. If you’re not happy with my performance or your clients are complaining, we’ll call it off."
    s "There’s no risk or commitment on your end."
    scene gym_first8
    dn "Hmmm, we are short on staff. I guess we can give it a shot."
    dn "You’ll be training in cardio and core strength. We’ll see where it goes from there."
    scene gym_first11
    s "Thank you Dani, you won’t be disappointed."
    dn "Happy to have you on board, you can start immediately."
    dn "Daisy will bring you up to speed."
    s "Sounds great, thanks again!"
    s "(That worked...it actually worked!)"
    s "(I need to figure out how the hell I'm going to fuck these girls while parading as a gay man.)"
    s "(Most importantly, step one is complete. Now to go let Daisy know the good news.)"
    scene gym_first12
    s "(What the fuck is she doing?)"
    s "(Is she doing a handstand? She must be super bored.)"
    scene gym_first13
    "Daisy's shirt was untucked and falling down, exposing parts of her body."
    s "(I wonder how long she'll keep this up?)"
    s "(What a cute little bra, thank you gravity!)"
    "Daisy suddenly lost her balance and dropped like a rock."
    scene gym_first14
    s "(Holy hell! Did she just knock herself out?)"
    scene gym_first15
    s "Daisy....DAISY!"
    ds "Uhhnnhh...."
    scene gym_first16
    ds "[s]..is that you?"
    s "Why the hell are you doing hands stands in the lobby?"
    ds "...my head hurts."
    s "Let's get you up."
    scene gym_first17
    "[s] extended a helping hand."
    scene gym_first18
    "As Daisy was getting up, she lost her balance and fell again."
    scene gym_first19
    "Grasping out frantically for anything to catch on to, she grabbed on to [s]'s waistband."
    scene gym_first20
    "Landing onto her knees, Daisy found herself at eye level with [s]'s dick."
    scene gym_first21
    ds "*GASP*"
    ds "WHY IS YOUR PENIS OUT!?"
    s "If you didn't want to see it, then why did you pull my shorts down?"
    ds "I didn't.. I didn't mean to!"
    s "I think this time you should help yourself up while I put our mutual friend away."
    scene gym_first22
    "Daisy got up to her feet while avoiding all eye contact."
    s "How's your head, are you hurt?"
    ds "My head hurts a little bit, but I'm ok."
    s "So I've just been hired. Dani said that you'd show me around but that can probably wait."
    ds "Yeah..."
    s "Daisy, look at me."
    s "I said look at me."
    scene gym_first23
    "Daisy meekly raised her head."
    s "I'm not mad. What happened was an accident. It's not your fault."
    s "Plus, it's not like you've never seen a dick before."
    ds "I-um...yeah I've seen tons of dicks already."
    ds "Wait, no! I mean, I've seen a couple dicks before."
    s "Okay, be honest. Was this the first dick you've ever seen?"
    ds "...yeah."
    s "Well talk about an ice breaker. I'm happy I was your first."
    s "So what'd you think?"
    ds "What?"
    s "What did you think of my dick?"
    scene gym_first22
    "Daisy lowered her head again in embarrassment."
    ds "It was ok I guess..."
    s "Just ok? He was standing at full attention for you!"
    s "Don't you think that's flattering?"
    ds "I guess..."
    scene gym_first23
    ds "So does that mean you're a boy after all?"
    s "(How many times has she fallen over and hit her head to be this slow?)"
    s "Yes Daisy.. I was just having fun with you."
    ds "That wasn't very nice!"
    s "But it was funny, for me at least."
    ds "I'm going to sit down until my brain stops bouncing around my head."
    ds "I'll let the girls know that you're working here."
    s "Thanks Daisy. And next time if you want to see my cock, just ask instead of forcefully stripping me... ok?"
    scene gym_first22
    "Daisy muttered something before running away in embarrassment."

    $ gym_intro = False
    jump loc_gym

label intro:
    scene intro 1
    s "Single malt scotch, how I’ve become familiar with you over the last few weeks. My closest friend in my time of need. It’s not easy to keep the walls from crumbling in around you, as you walk in on the woman you love fucking somebody else. "
    s "Not just a random somebody, but a bottom of the barrel scumbag. There I was putting in extra hours at work to provide a good life for my woman. Spoiling her with anything and everything she ever desired, and she fucks an unemployed asshole."
    s "What’s the point of living a good honest life when being a jackass gets you ahead? Now I’m the unemployed asshole."
    s "When I have a bottle in my desk drawer, I have a 'drinking problem' and am not a 'good fit' for the work environment. When management has a bottle on their desk, it’s called 'tasteful decoration'."

    scene intro 2
    so "Another late night of whiskey and self-pity, [s]?"
    s "No Sophie, tonight’s different. I’m drinking scotch."
    s "(My cousin Sophie, one of the few truly good people left in this world. We were inseparable as kids. She hit just as hard as the boys and outran every single one of them.)"
    s "(She was always the ambitious one so it was no surprise that she moved away to live the city life after high school.)"

    scene intro 3
    so "Oh right, we’re making progress."
    so "Listen [s], take all the time you need to deal with what happened to you. Just please promise me that this won’t break you, that you’ll bounce back… unless you want to see me go to jail for choking that little skank to death!"

    scene intro 2
    s  "Oh, how I’d love to see that. You’re right Sophie, I’ll try for you. Also, thanks again for offering to let me crash here on such short notice.  I don’t know what I’d do without you."
    so "Stop. You don’t even need to say it. That’s what family’s for. I’m sorry this apartment’s only one bedroom and you have to sleep on the couch."
    s "Yeah, how dare you rent a place without predicting your deadbeat, unemployed cousin will need a place to stay!? This is more than perfect. I’m comfortable, I promise."

    scene intro 4
    so "You’re not a deadbeat but fair enough, point taken. I’m going to go to bed. Good night cousin, try to get some sleep."
    s "Night Sophie"

    scene intro 1
    s "(She’s right, I do need to bounce back from this. But what’s the point? How am I going to open up and trust someone again?)"
    s "(How can I find motivation to throw myself back into the corporate grinder? Maybe I can pull my act together long enough to get out of Sophie’s hair, and then have a little sky diving 'accident' somewhere far away.)"
    s "(At least that way she would be sheltered from any guilt of being unable to save me.)"

    scene khan
    his '"The great Genghis Khan took what he desired. No city or state could resist his ambitions. The great Khan succeeded through force or deceit where his predecessors failed.  His treasury filled with gold and jewels and his harem filled with women."'
    his '"It is estimated that 0.5\% of the male population, or 16 million men, can directly trace their heritage back to Genghis Khan."'

    s "(Now that guy sounds like a real asshole. Uses force and deceit to get anything he wants?)"
    s "(The guy was swimming in gold and pussy, and hundreds of years later we’re still praising him for being a colossal dick.)"
    s "(Maybe I’ll be a deceitful little shit and historians around the world will sing tales of my exploits.)"
    s "(They’ll say '20 million men can trace their ancestry back to [s] the Terrible'! Now that’s what I call motivation.)"

    scene gym ad
    s "(What’s this? A gym ad that only caters to women? Now that sounds like an excellent place for a guy down on his luck. If only I could find a way to get in. I wonder what Genghis Khan would do?)"
    s "(He’d probably show up with his army and say 'I will impregnate every single woman in this building, or I will burn it down. You decide.')"

    scene sleep
    s "(Unfortunately, I don’t have an army. Maybe some deceit is in order. I’ll have to sleep on it for now.)"
    scene sophie_livingroom_dusk
    with fade
    $ pass_time(360)
    s "(Not the most comfortable sleep I've ever had, but definitely not the worst.)"
    s "(I should go see what Sophie's up to and then check out that gym.)"
    menu:
        "Do you want to skip the tutorial?"

        "Yes":
            "(Pffft... what a 'know-it-all'!)"

        "No":
            scene tut9
            "(TUTORIAL: We're going to take a quick look at the UI.)"
            scene tut10
            "(Here we see the day of the week and the current time.)"
            "(You can increase the time in 1 and 6 hour increments.)"
            "(You may also choose to go to sleep. This will move you forward to 7am the next day.)"
            scene tut11
            "(Some locations have multiple rooms to explore.)"
            "(You are able to move between rooms by clicking on the corresponding frame.)"
            scene tut1
            "(An in-game guide is available if you're stuck on how to advance with a character.)"
            scene tut2
            with fade
            "(When you meet a main character, they become revealed here.)"
            "(Clicking on their portrait will display a hint on how to progress with their story if a hint is available.)"
            scene tut3
            "(Currently there are no hints available with Sophie.)"
            "(This usually means that their progression is tied to another main character.)"
            "(In this situation, progressing with another character will eventually unlock Sophie's story.)"
            scene tut4
            "(When there are no more events left for a character in the current version, you will see this message.)"
            "(This guide only tracks STORY EVENTS. There may still be NON-STORY EVENT content available that is accessible only on certain days, time, and location.)"
            scene tut5
            "(As you interact with characters, their activity is logged into a schedule tracker.)"
            "(By selecting the day, you will see what activities you've witnessed them doing.)"
            "(We can see that Sophie plays video games at home at 19:00.)"
            scene tut6
            "(As we discover more of Sophie's schedule, it will start looking like this.)"
            scene tut7
            with fade
            "(This icon brings you to the replay gallery.)"
            "(Here you will be able to replay sexy events that you've already completed.)"
            "(Certain story events have choices that may impact your relationship with that character.)"
            "(During a replay, choosing choices will have no impact on your game so feel free to see what you may have missed otherwise.)"
            "(Only story related events are stored here because there would otherwise be no way to see that content again in a current playthrough.)"
            "(For that reason, repeatable non-story content is not included in the replay gallery.)"
            scene tut8
            "(The map screen allows you to instantly travel to any location.)"
            "(More locations become available as you progress in the game.)"
            scene tut9
            "(That should be everything, enjoy!)"
    jump loc_sophie
