




label start:




    $ anticheat = persistent.anticheat


    $ chapter = 0



    $ _dismiss_pause = config.developer




    $ s_name = "Сайорі"
    $ m_name = "Моніка"
    $ n_name = "Нацукі"
    $ y_name = "Юрі"


    $ quick_menu = True



    $ style.say_dialogue = style.normal


    $ in_sayori_kill = None


    $ allow_skipping = True
    $ config.allow_skipping = True



    if persistent.playthrough == 0:



        $ chapter = 0
        call script_48h from _call_script_48h
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
