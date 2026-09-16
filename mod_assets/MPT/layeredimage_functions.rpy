init python:

    def mref(target="master"):
        if not "monika" in renpy.get_showing_tags(layer=target, sort=True):
            
            return
        pose = str(renpy.get_attributes("monika",layer=target)[0])
        if pose == "":
            
            return
        renpy.show("monika " + pose + " refreshattribute",layer=target)
        renpy.show("monika",layer=target)

    def sref(target="master"):
        if not "sayori" in renpy.get_showing_tags(layer=target, sort=True):
            
            return
        pose = str(renpy.get_attributes("sayori",layer=target)[0])
        if pose == "":
            
            return
        renpy.show("sayori " + pose + " refreshattribute",layer=target)
        renpy.show("sayori",layer=target)

    def nref(target="master"):
        if not "natsuki" in renpy.get_showing_tags(layer=target, sort=True):
            
            return
        pose = str(renpy.get_attributes("natsuki",layer=target)[0])
        if pose == "":
            
            return
        renpy.show("natsuki " + pose + " refreshattribute",layer=target)
        renpy.show("natsuki",layer=target)

    def yref(target="master"):
        if not "yuri" in renpy.get_showing_tags(layer=target, sort=True):
            
            return
        pose = str(renpy.get_attributes("yuri",layer=target)[0])
        if pose == "":
            
            return
        renpy.show("yuri " + pose + " refreshattribute",layer=target)
        renpy.show("yuri",layer=target)

screen layeredimagetool_stats():
    vbox:
        text "Current character is " + character + ", current position is " + position_displayable size 20
        text "Last input was " + posename size 20
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
