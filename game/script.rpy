define r = Character('Rohan', color="#c8ffc8", who_bold=True)
define asura = Character('Asura', color="#ff0000", who_italic=True)
define dadi = Character('Dadi Savitri', color="#8B4513", who_bold=True)
define arjun = Character('Arjun', color="#c8c8ff")
define mira = Character('Mira', color="#ffc8c8")
define tanu = Character('Tanu', color="#ffffc8")
define isha = Character('Isha', color="#c8ffff")

default health = 100
default humanity = 50
default sanity = 100
default companions = ["Arjun", "Mira"]
default inventory = []
default day = 1
default time_of_day = "morning"
default locus_of_choice = 0
default pacing_multiplier = 1.0

# =========================
# image bg_village_day = "images/bg_village_day.png"
# image bg_village_evening = "images/bg_village_evening.png"
# image bg_village_night = "images/bg_village_night.png"
# image bg_forest_twilight = "images/bg_forest_twilight.png"
# image bg_asura_throne = "images/bg_asura_throne.png"
# image char_rohan = "images/rohan.png"
# image char_arjun_smirk = "images/arjun_smirk.png"
# image char_tanu = "images/tanu.png"
# image char_isha = "images/isha.png"

# define r = Character('Rohan', image="rohan")
# image side rohan = "images/side_rohan.png"
# image side rohan happy = "images/side_rohan_happy.png"

init python:
    import random

    def change_time(inc):
        global time_of_day, day
        order = ["morning", "noon", "evening", "night"]
        try:
            i = order.index(time_of_day)
        except Exception:
            i = 0
        i = (i + inc) % 4
        time_of_day = order[i]
        if time_of_day == "morning":
            day += 1

    def alter_stats(h=0, hu=0, s=0):
        global health, humanity, sanity
        health = max(0, min(100, health + h))
        humanity = max(0, min(100, humanity + hu))
        sanity = max(0, min(100, sanity + s))

    def add_item(item):
        if item not in inventory:
            inventory.append(item)

    def has_item(item):
        return item in inventory

    def messy_random_event():
        r = random.randint(1, 100)
        if r < 30:
            return "nothing"
        if r < 60:
            return "stray_dog"
        if r < 85:
            return "merchant"
        return "asura_watch"


screen status_bar():
    frame:
        xalign 0.02
        yalign 0.02
        has vbox
        text "Health: [health]"
        text "Sanity: [sanity]"
        text "Humanity: [humanity]"
        text "Day: [day] - [time_of_day]"


label start:
    scene black
    $ renpy.music.play("audio/music_theme.ogg", channel="music", loop=True)
    show text "THE WANE OF THE HOLY MOON" at truecenter
    with dissolve
    pause 2.0 * pacing_multiplier
    hide text
    scene bg_village_day with fade
    show char_rohan at center
    r "(you wake up to the smell of damp straw and the particular taste of regret)"
    r "...Dadi Savitri always said: don't let the world look like your dreams. Make your dreams look like the world."
    $ renpy.music.play("audio/sfx_heartbeat.wav", loop=True)
    $ alter_stats()
    call prologue


label prologue:
    show bg_village_day
    dadi "Rohan, kahaani ka time aa gaya hai."
    r "(maybe it's just morning. or the calm before something that looks like cinema.)"
    menu:
        "Get out of bed quickly and run to the courtyard":
            $ locus_of_choice += 1
            jump courtyard_fast
        "Tidy up slowly, take a breath":
            $ locus_of_choice -= 1
            jump courtyard_slow

label courtyard_fast:
    scene bg_village_day
    r "I sprinted out because suspense requires motion."
    $ change_time(1)
    show screen status_bar
    jump encounter_loop

label courtyard_slow:
    scene bg_village_day
    r "I sat and listened to the old radio, letting the world think itself together."
    $ change_time(1)
    show screen status_bar
    jump encounter_loop

label encounter_loop:
    $ ev = messy_random_event()
    if ev == "nothing":
        r "It was a quiet stretch, the sort that fills a heart with small fossils."
        $ alter_stats(h=0, hu=1, s=-1)
        $ change_time(1)
        jump hub_choices
    elif ev == "stray_dog":
        show bg_forest_twilight
        r "A stray dog followed me in, eyes too old for its face."
        menu:
            "Feed the dog (give bread)":
                $ add_item('dog_friend')
                $ alter_stats(hu=2)
                r "He stays. He will be called 'Tara' later."
            "Shoo it away":
                $ alter_stats(hu=-3)
                r "It ran. Guilt smells like last night's tea."
        $ change_time(1)
        jump hub_choices
    elif ev == "merchant":
        show bg_village_day
        r "A merchant with a crooked smile had trinkets that hummed."
        menu:
            "Buy the humming amulet (cost: sanity 5)":
                if sanity >= 5:
                    $ add_item('amulet_hum')
                    $ alter_stats(s=-5)
                    r "Something in the amulet looks back when you blink."
                else:
                    r "Couldn't afford the price in steadiness."
            "Ignore and walk away":
                r "Merchants sell what you don't need."
        $ change_time(1)
        jump hub_choices
    else:
        show bg_asura_throne
        $ renpy.music.play("audio/music_suspense.ogg", loop=True)
        asura "I have been watching your steps, Rohan."
        menu:
            "Confront Asura":
                $ locus_of_choice += 5
                jump confront_asura
            "Hide and observe":
                $ locus_of_choice -= 2
                jump observe_asura

label hub_choices:
    menu:
        "Follow the main rumor (ask about the Moon relic)":
            jump main_quest_start
        "Visit Arjun (companion) and trigger companion scene":
            jump arjun_scene
        "Explore the marketplace (chance for side content)":
            jump marketplace
        "Rest at Dadi's home (restore stats, triggers dreams)":
            jump rest_dadi
        "Force a random event again":
            jump encounter_loop
        "Save and quit":
            return

label main_quest_start:
    scene bg_forest_twilight
    r "Rumor: the Moon relic can tilt the balance of sanity."
    $ add_item('moon_rumor_note')
    $ change_time(1)
    menu:
        "Head to the old temple immediately":
            jump temple_path
        "Gather allies first":
            jump recruit_path

label recruit_path:
    scene bg_village_day
    r "Allies help. Try to recruit Tanu or Isha before the temple."
    menu:
        "Find Tanu and help with a practice":
            jump recruit_tanu
        "Visit Isha and listen":
            jump recruit_isha
        "Skip recruiting and head to the temple":
            jump temple_path

label recruit_tanu:
    scene bg_village_day
    show char_tanu at left
    tanu "Training! I need props but my wallet cries. Help?"
    menu:
        "Buy her props (adds chance to recruit)":
            $ add_item('tanu_prop')
            $ alter_stats(hu=2)
            tanu "Legend. Maybe I'll join you."
            $ change_time(1)
            jump recruit_outcome
        "Train with her (build bond)":
            $ change_time(1)
            $ alter_stats(hu=3)
            tanu "Weird training but fun. Maybe I'll join later."
            jump recruit_outcome

label recruit_isha:
    scene bg_village_day
    show char_isha at left
    isha "I heard about the Moon relic. Someone has to keep stories honest."
    menu:
        "Convince Isha to join (humanity check)":
            if humanity >= 40:
                $ add_item('isha_bond')
                $ alter_stats(hu=4)
                isha "Alright. I'll walk with you a while."
                $ change_time(1)
                jump recruit_outcome
            else:
                isha "Not yet. I need to see more."
                $ change_time(1)
                jump recruit_outcome

label recruit_outcome:
    if "tanu_prop" in inventory and "isha_bond" in inventory:
        if "Tanu" not in companions:
            $ companions.append("Tanu")
        if "Isha" not in companions:
            $ companions.append("Isha")
        r "With promises made, Tanu and Isha join."
    elif "tanu_prop" in inventory or "isha_bond" in inventory:
        if "tanu_prop" in inventory and "Tanu" not in companions:
            $ companions.append("Tanu")
            r "Tanu joins you, sparkly and loud."
        elif "Isha" not in companions:
            $ companions.append("Isha")
            r "Isha joins you, steady and sharp."
    else:
        r "Recruitment failed this time."
    jump temple_path

label arjun_scene:
    scene bg_village_day
    show char_arjun_smirk at left
    arjun "You look like a storm was born in you. Starting one?"
    menu:
        "Share your fears (bond increases)":
            $ alter_stats(hu=3)
            $ add_item('arjun_bond')
            arjun "Good. Now I know where to find you when trouble comes."
        "Tease him and move on":
            $ alter_stats(hu=1)
            arjun "One day you'll laugh about this."
    $ change_time(1)
    jump hub_choices

label marketplace:
    scene bg_village_day
    r "The market is a corridor of potential."
    menu:
        "Play a gambling game (small chance to win item)":
            $ outcome = renpy.random.randint(1, 6)
            if outcome == 6:
                $ add_item('golden_coin')
                r "Luck nods at you."
            else:
                r "The trickster takes your coin and leaves."
        "Listen to the traveling bard (story extension)":
            call bard_tale
        "Buy food and heal a bit":
            $ alter_stats(h=10, s=2)
            r "A simple stew holds its own kind of magic."
    $ change_time(1)
    jump hub_choices

label rest_dadi:
    scene bg_village_night
    show dadi at center
    dadi "Sleep. But stories bleed into dreams."
    $ alter_stats(h=10, s=10, hu=2)
    call dream_sequence
    $ change_time(1)
    jump hub_choices

label bard_tale:
    show bg_village_day
    $ renpy.music.play("audio/music_theme.ogg", loop=True)
    "The bard spins a tale of a boy who stole night."
    menu:
        "Ask about the boy's motive":
            "The boy wanted to see his mother's face at midday."
            $ alter_stats(s=-2)
        "Stay silent and just listen":
            "You let the cadence wash over you. You feel fuller."
            $ alter_stats(hu=2)
    $ renpy.music.play("", loop=False)
    return

label dream_sequence:
    scene black
    with fade
    show text "Dream: The moon drips like ink." at truecenter
    pause 2.0
    hide text
    menu:
        "Embrace the dream (investigate deeply)":
            $ alter_stats(s=-10)
            r "You swim without lungs; the ink tastes like memory."
        "Wake up quickly (safety)":
            $ alter_stats(s=5)
            r "Cold air slaps awake the rest of you."
    return

label temple_path:
    scene bg_forest_twilight
    r "The old temple smells of salt and old promises."
    if has_item('amulet_hum'):
        r "The amulet hums and points you toward a hidden side-entrance."
        menu:
            "Use the amulet to access the secret":
                jump temple_secret
            "Avoid the amulet and go through the main gate":
                jump temple_main
    else:
        jump temple_main

label temple_main:
    show bg_asura_throne
    asura "So you arrive — like a film's last act."
    menu:
        "Demand the relic":
            $ alter_stats(h=-10, s=-20)
            asura "Bold and loud, but bold makes holes in the loud."
            jump boss_encounter
        "Negotiate (humanity check)":
            if humanity >= 60:
                $ alter_stats(hu=5)
                asura "A bargain. Here's a piece of the moon."
                $ add_item('moon_fragment')
                jump after_temple
            else:
                $ alter_stats(h=-5)
                asura "You smell of desperation."
                jump boss_encounter

label temple_secret:
    r "Inside the secret passage, murals tell of a person who traded their name for a star."
    $ add_item('star_name_note')
    $ alter_stats(s=-5)
    jump after_temple

label boss_encounter:
    asura "Fight, or let me narrate your defeat."
    menu:
        "Attack (physical)":
            if health > 40:
                $ alter_stats(h=-30, s=-10)
                r "You strike and the scene cracks like glass."
                jump after_boss
            else:
                r "Too weak. The world narrows."
                jump death_scene
        "Use cunning (if you have golden_coin or arjun_bond)":
            if has_item('golden_coin') or has_item('arjun_bond'):
                $ alter_stats(h=-5, hu=10)
                r "A trick, a friend, a coin — Asura retreats for now."
                jump after_boss
            else:
                $ alter_stats(h=-20)
                r "Cunning without the tools is theatre without an audience."
                jump death_scene

label after_boss:
    $ renpy.music.play("", loop=False)
    asura "This is not the end. It's a bookmarked end."
    $ add_item('asura_mark')
    jump after_temple

label after_temple:
    scene bg_village_night
    r "With a shard of moon or an asura mark, the world rearranges its furniture."
    menu:
        "Pursue the Moon Relic's deeper mystery":
            jump moon_relic_arc
        "Settle into village life and conclude with small scenes":
            jump village_epilogue

label moon_relic_arc:
    $ add_item('moon_path_started')
    r "You spend days, weeks. Do chores, gather clues, speak to elders."
    call gather_clues
    call elder_trials
    call final_reckoning
    return

label gather_clues:
    $ clues_found = 0
    while clues_found < 3:
        $ choice = messy_random_event()
        if choice == "nothing":
            r "A dead-end alley, a face that ignores you. Write it down anyway."
            $ clues_found += 1
            $ change_time(1)
        elif choice == "merchant":
            r "A merchant tells of a shrine and charges tea. You take the tea."
            $ clues_found += 1
            $ change_time(1)
        elif choice == "stray_dog":
            r "The dog leads you to a scratched obelisk with a symbol from a dream."
            $ add_item('obelisk_rub')
            $ clues_found += 1
            $ change_time(1)
        else:
            r "Asura's shadow, shortcutting through your notes."
            $ change_time(1)
    return

label elder_trials:
    scene bg_village_day
    r "Three elders. Each asks for something: a memory, a favour, a riddle."
    menu:
        "Give a memory (lose sanity, gain wisdom)":
            $ alter_stats(s=-10, hu=5)
            r "You tell the story that made you, and for a moment you are not alone."
        "Refuse and bargain instead":
            $ alter_stats(hu=-5)
            r "Elders dislike bargaining. The world notices."
    return

label final_reckoning:
    show bg_asura_throne
    $ renpy.music.play("audio/music_suspense.ogg", loop=True)
    asura "So many days. The Moon looks different on you. Shall we finish?"
    menu:
        "Accept the Moon's offer (big sanity change)":
            $ alter_stats(s=-40, hu=20)
            r "You let the moon rewrite the edges of your face."
            jump ending_moon_taken
        "Refuse and keep your name":
            $ alter_stats(hu=10)
            r "You keep your name like a coin in the mouth."
            jump ending_keep_name

label ending_moon_taken:
    scene black
    show text "You become something that sleeps in light and wakes in history." at truecenter
    pause 3.0
    return

label ending_keep_name:
    scene bg_village_day
    r "You return, perhaps less luminous, but oddly human. The credits roll on the market."
    return

label village_epilogue:
    scene bg_village_day
    r "Days fold into one another. You open a stall, tell stories, Dadi bakes."
    $ change_time(1)
    call companion_arcs
    return

label companion_arcs:
    menu:
        "Play Arjun's story":
            call arjun_arc
        "Play Mira's story":
            call mira_arc
        "Play Tanu's street performances":
            call tanu_arc
        "Back to village life":
            return

label arjun_arc:
    scene bg_village_evening
    arjun "There is a knot in me, Rohan. Will you untie it?"
    menu:
        "Help him reconcile with his past":
            $ alter_stats(hu=5)
            arjun "I didn't know I needed that."
        "Encourage him to leave and find his own path":
            $ alter_stats(hu=0)
            arjun "Maybe I will. Maybe I won't. That's the point."
    return

label mira_arc:
    scene bg_village_day
    mira "I want to craft a song that makes people stop moving."
    menu:
        "Help compose the chorus":
            $ alter_stats(hu=3)
            r "You whistle a line and it's enough."
        "Tell her to stop chasing perfection":
            $ alter_stats(hu=1)
            mira "Is that wisdom or laziness?"
    return

label tanu_arc:
    scene bg_village_day
    tanu "My street act will bankrupt me if I fail. Help?"
    menu:
        "Train with her":
            $ change_time(1)
            $ alter_stats(hu=5)
            tanu "We made a mess and the crowd laughed."
        "Buy materials and support her show":
            $ add_item('tanu_prop')
            $ alter_stats(hu=2)
    return

label confront_asura:
    show bg_asura_throne
    asura "Ah — directness. Rare, and messy, like a good scene."
    menu:
        "Use diplomacy":
            if humanity > 50:
                asura "You speak like the wind that consoles broken statues. I respect that."
                $ add_item('asura_respect')
                $ alter_stats(hu=5)
                jump after_boss
            else:
                asura "Words without weight."
                $ alter_stats(s=-10)
                jump boss_encounter
        "Use stealth and trickery":
            if has_item('star_name_note'):
                r "You whisper the secret name carved into a star and trap Asura for a breath."
                $ add_item('trapped_asura')
                $ alter_stats(s=-20, hu=10)
                jump after_boss
            else:
                r "No star name, no trap."
                $ alter_stats(h=-10)
                jump boss_encounter

label observe_asura:
    show bg_asura_throne
    r "You watch Asura perform small cruelties like a person knitting."
    $ alter_stats(s=-5)
    $ change_time(1)
    jump hub_choices

label death_scene:
    scene black
    $ renpy.music.play("", loop=False)
    show text "You fall. The film shutters." at truecenter
    pause 2.0
    show text "GAME OVER" at truecenter
    return

label credits:
    scene black
    show text "CREATED BY: (your name here)" at truecenter
    pause 2
    show text "ASSETS: replace placeholders with your files" at truecenter
    pause 2
    return
