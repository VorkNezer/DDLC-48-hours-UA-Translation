init python:
    menu_trans_time = 1

    splash_message_default = "Це неофіційна фанатська робота, незв'язана з Team Salvato."

    splash_messages = [
        "Будь ласка, підтримайте Doki Doki Літературний клуб.",
        "Моніка слідкує за твоїм кодом."
    ]

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)





image menu_1:
    subpixel True
    "gui/menu/menu_bg_1.png"
    xalign 1.0
    linear 40 xalign 0.0
    repeat

image menu_2:
    subpixel True
    "gui/menu/menu_bg_2.png"
    xalign 1.0
    linear 28 xalign 0.0
    repeat

image menu_3:
    subpixel True
    "gui/menu/menu_bg_3.png"
    xalign 1.0
    linear 19 xalign 0.0
    repeat




image menu_logo:
    "/mod_assets/DDLCModTemplateLogo.png"
    subpixel True
    xcenter 640
    ycenter 220
    zoom 0.60

image menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move

image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_loop

image menu_fade:
    "black"
    menu_fadeout

image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 450
    ycenter 640
    zoom 1

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 750
    ycenter 640
    zoom 0.95

image menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 300
    ycenter 640
    zoom 1

image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1080
    ycenter 640
    zoom 1.00


image menu_art_y_ghost:
    subpixel True
    "gui/menu_art_y_ghost.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_ghost:
    subpixel True
    "gui/menu_art_n_ghost.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s_ghost:
    subpixel True
    "gui/menu_art_s_ghost.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m_ghost:
    subpixel True
    "gui/menu_art_m_ghost.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)


image menu_art_s_glitch:
    subpixel True
    "gui/menu_art_s_break.png"
    xcenter 470
    ycenter 600
    zoom 0.68
    menu_art_move(.8, 470, .8)

image menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move



image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=40, particleTime=2.0, particleXSpeed=3, particleYSpeed=3).sm
    particle_fadeout

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 3.5

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0



image intro:
    truecenter
    "black"
    0.5
    "mod_assets/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "black" with Dissolve(0.5, alpha=True)
    0.5



image warning:
    truecenter
    "black"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "black" with Dissolve(0.5, alpha=True)
    0.5



init python:
    if not persistent.do_not_delete:
        
        import os
        try:
            if not os.access(config.basedir + "/characters/", os.F_OK):
                os.mkdir(config.basedir + "/characters")
            
            if persistent.playthrough <= 2:
                try: renpy.file("../characters/monika.chr")
                except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
            if persistent.playthrough <= 1 or persistent.playthrough == 4:
                try: renpy.file("../characters/natsuki.chr")
                except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
                try: renpy.file("../characters/yuri.chr")
                except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
            if persistent.playthrough == 0 or persistent.playthrough == 4:
                try: renpy.file("../characters/sayori.chr")
                except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())
        
        except:
            pass


image tos = "bg/warning.png"
image tos2 = "bg/warning2.png"



label splashscreen:

    python:
        process_list = []
        currentuser = ""
        if renpy.windows:
            try:
                process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            except:
                pass
            try:
                for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    user = os.environ.get(name)
                    if user:
                        currentuser = user
            except:
                pass


    python:
        firstrun = ""

    if not firstrun:
        if persistent.first_run and (config.version == persistent.oldversion or persistent.autoload == "postcredits_loop"):
            $ quick_menu = False
            scene black
            menu:
                "Знайдено збереження. Хочете видалити їх і почати спочатку?"
                "Так, видалити збереження.":
                    "Збереження видаляються...{nw}"
                    python:
                        delete_all_saves()
                        renpy.loadsave.location.unlink_persistent()
                        renpy.persistent.should_save_persistent = False
                        renpy.utter_restart()
                "Ні, продовжити звітти, де я зупинився.":
                    $ restore_relevant_characters()










    default persistent.first_run = False



    if not persistent.first_run:
        python:
            restore_all_characters()
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0


        "[config.name] - це фанацький мод по грі Doki Doki Literature Club, ніяк не зв'язанай з командою Сальвато."
        "Він призначений для проходження тільки після того, як офіційна гра була пройдена вами, і містить спойлери із оригінальної гри."
        "Файли гри Doki Doki Literature Club необхідні для гри в данний мод можна завантажити безкоштовно зі Steam або на сайті: http://ddlc.moe."
        menu:
            "Граючи в [config.name], ви погоджуєтесь з тим, що прийшли Doki Doki Literature Club і готові до любих спойлерів, наявними в моді."
            "Згоден.":
                pass
        $ persistent.first_run = True
        scene tos2
        with Dissolve(1.5)
        pause 1.0
        scene white

        $ persistent.first_run = True























    if not persistent.special_poems:
        python hide:
            persistent.special_poems = [0,0,0]
            a = range(1,12)
            for i in range(3):
                b = renpy.random.choice(a)
                persistent.special_poems[i] = b
                a.remove(b)

    $ basedir = config.basedir.replace('\\', '/')


    if persistent.autoload:
        jump autoload



    $ config.allow_skipping = False


    if persistent.playthrough == 2 and not persistent.seen_ghost_menu and renpy.random.randint(0, 63) == 0:
        show black
        $ config.main_menu_music = audio.ghostmenu
        $ persistent.seen_ghost_menu = True
        $ persistent.ghost_menu = True
        $ renpy.music.play(config.main_menu_music)
        $ pause(1.0)
        show end with dissolve_cg
        $ pause(3.0)
        $ config.allow_skipping = True
        return























































    show black
    $ persistent.ghost_menu = False
    $ splash_message = splash_message_default
    $ config.main_menu_music = audio.coronaradiata
    $ renpy.music.play(config.main_menu_music)
    $ starttime = datetime.datetime.now()
    show intro with Dissolve(0.5, alpha=True)
    $ pause(3.0 - (datetime.datetime.now() - starttime).total_seconds())
    hide intro with Dissolve(max(0, 3.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    if persistent.playthrough == 2 and renpy.random.randint(0, 3) == 0:
        $ splash_message = renpy.random.choice(splash_messages)
    show splash_warning "[splash_message]" with Dissolve(max(0, 4.0 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    $ pause(6.0 - (datetime.datetime.now() - starttime).total_seconds())
    hide splash_warning with Dissolve(max(0, 6.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    $ pause(6.5 - (datetime.datetime.now() - starttime).total_seconds())
    $ config.allow_skipping = True
    return


label warningscreen:
    hide intro
    show warning
    pause 3.0






























label after_load:
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False
    $ style.say_dialogue = style.normal

    if anticheat != persistent.anticheat:
        stop music
        scene black
        "Збереження не може бути завантаженим."
        "Ти намагаєшся чітерити?"

        $ renpy.utter_restart()
    return


label autoload:
    python:
        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()

        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

    $ renpy.pop_call()
    jump expression persistent.autoload


label before_main_menu:
    $ config.main_menu_music = audio.coronaradiata
    return


label quit:
    if persistent.ghost_menu:
        hide screen main_menu
        scene white
        show expression "gui/menu_art_m_ghost.png":
            xpos -100 ypos -100 zoom 3.5
        pause 0.01
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
