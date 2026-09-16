


layeredimage sayori turned: 

    always "mod_assets/MPT/sayori/sayori_turned_facebase.png" 

    group outfit: 
        attribute uniform default null
        attribute casual null



    group mood: 



        attribute neut default null 
        attribute angr null 
        attribute anno null 
        attribute cry null  
        attribute curi null 
        attribute dist null 
        attribute doub null 
        attribute flus null 
        attribute happ null 
        attribute laug null 
        attribute lsur null 
        attribute nerv null 
        attribute pani null 
        attribute pout null 
        attribute sad null  
        attribute sedu null 
        attribute shoc null 
        attribute vang null 
        attribute vsur null 
        attribute worr null 
        attribute yand null 




    group blush: 
        attribute nobl null 
        attribute awkw null 
        attribute blus null 
        attribute blaw null 




    group left if_any(["uniform"]):
        attribute ldown default:
            "mod_assets/MPT/sayori/sayori_turned_uniform_left_down.png"
        attribute lup:
            "mod_assets/MPT/sayori/sayori_turned_uniform_left_up.png"

    group left if_any(["casual"]):
        attribute ldown default:
            "mod_assets/MPT/sayori/sayori_turned_casual_left_down.png"
        attribute lup:
            "mod_assets/MPT/sayori/sayori_turned_casual_left_up.png"




    group right if_any(["uniform"]):
        attribute rdown default:
            "mod_assets/MPT/sayori/sayori_turned_uniform_right_down.png"
        attribute rup:
            "mod_assets/MPT/sayori/sayori_turned_uniform_right_up.png"

    group right if_any(["casual"]):
        attribute rdown default:
            "mod_assets/MPT/sayori/sayori_turned_casual_right_down.png"
        attribute rup:
            "mod_assets/MPT/sayori/sayori_turned_casual_right_up.png"



    group nose:


        attribute nose default if_any(["nobl"]):
            "mod_assets/MPT/sayori/sayori_turned_nose_n1.png"
        attribute nose default if_any(["awkw"]):
            "mod_assets/MPT/sayori/sayori_turned_nose_n2.png"
        attribute nose default if_any(["blus"]):
            "mod_assets/MPT/sayori/sayori_turned_nose_n3.png"
        attribute nose default if_any(["blaw"]):
            "mod_assets/MPT/sayori/sayori_turned_nose_n4.png"



        attribute n1:
            "mod_assets/MPT/sayori/sayori_turned_nose_n1.png"
        attribute n2:
            "mod_assets/MPT/sayori/sayori_turned_nose_n2.png"
        attribute n3:
            "mod_assets/MPT/sayori/sayori_turned_nose_n3.png"
        attribute n4:
            "mod_assets/MPT/sayori/sayori_turned_nose_n4.png"
        attribute nl:
            "mod_assets/MPT/sayori/sayori_turned_nose_nl.png"



    group mouth:


        attribute cm default if_any(["happ","sedu","nerv"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_ma.png"
        attribute cm default if_any(["neut","anno","worr","curi"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_md.png"
        attribute cm default if_any(["dist","flus"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_me.png"
        attribute cm default if_any(["lsur","shoc"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mf.png"
        attribute cm default if_any(["sad","angr","pout","doub"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mj.png"
        attribute cm default if_any(["cry","pani","vsur"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mk.png"
        attribute cm default if_any(["vang"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mm.png"
        attribute cm default if_any(["laug"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mn.png"
        attribute cm default if_any(["yand"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mo.png"


        attribute om if_any(["happ","laug"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mb.png"
        attribute om if_any(["yand","nerv"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mc.png"
        attribute om if_any(["pout","sedu"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mf.png"
        attribute om if_any(["sad","lsur","dist"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mg.png"
        attribute om if_any(["neut","anno","shoc","worr"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mh.png"
        attribute om if_any(["curi","doub"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mi.png"
        attribute om if_any(["flus"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mk.png"
        attribute om if_any(["cry","vsur"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_ml.png"
        attribute om if_any(["angr","pani","vang"]):
            "mod_assets/MPT/sayori/sayori_turned_mouth_mq.png"



        attribute ma:
            "mod_assets/MPT/sayori/sayori_turned_mouth_ma.png"
        attribute mb:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mb.png"
        attribute mc:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mc.png"
        attribute md:
            "mod_assets/MPT/sayori/sayori_turned_mouth_md.png"
        attribute me:
            "mod_assets/MPT/sayori/sayori_turned_mouth_me.png"
        attribute mf:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mf.png"
        attribute mg:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mg.png"
        attribute mh:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mh.png"
        attribute mi:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mi.png"
        attribute mj:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mj.png"
        attribute mk:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mk.png"
        attribute ml:
            "mod_assets/MPT/sayori/sayori_turned_mouth_ml.png"
        attribute mm:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mm.png"
        attribute mn:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mn.png"
        attribute mo:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mo.png"
        attribute mp:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mp.png"
        attribute mq:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mq.png"
        attribute mr:
            "mod_assets/MPT/sayori/sayori_turned_mouth_mr.png"



    group eyes:


        attribute oe default if_any(["neut","angr","happ","laug","sad"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1a.png"
        attribute oe default if_any(["dist","worr","pout"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1b.png"
        attribute oe default if_any(["anno","sedu","doub"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1d.png"
        attribute oe default if_any(["cry"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1g.png"
        attribute oe default if_any(["lsur","flus","vsur","curi"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e2a.png"
        attribute oe default if_any(["nerv"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e2b.png"
        attribute oe default if_any(["pani","vang","shoc"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e2d.png"
        attribute oe default if_any(["yand"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e3a.png"


        attribute ce if_any(["sad","anno","angr","dist","shoc","worr","nerv","curi","doub"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4a.png"
        attribute ce if_any(["neut","happ","lsur","laug","vsur","yand","pout","sedu"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4b.png"
        attribute ce if_any(["vang","flus","pani"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4c.png"
        attribute ce if_any(["cry"]):
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4d.png"



        attribute e1a:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1a.png"
        attribute e1b:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1b.png"
        attribute e1c:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1c.png"
        attribute e1d:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1d.png"
        attribute e1e:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1e.png"
        attribute e1f:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1f.png"
        attribute e1g:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1g.png"
        attribute e1h:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e1h.png"
        attribute e2a:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e2a.png"
        attribute e2b:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e2b.png"
        attribute e2c:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e2c.png"
        attribute e2d:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e2d.png"
        attribute e3a:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e3a.png"
        attribute e3b:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e3b.png"
        attribute e4a:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4a.png"
        attribute e4b:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4b.png"
        attribute e4c:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4c.png"
        attribute e4d:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4d.png"
        attribute e4e:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e4e.png"
        attribute e0a:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e0a.png"
        attribute e0b:
            "mod_assets/MPT/sayori/sayori_turned_eyes_e0b.png"



    group eyebrows:


        attribute brow default if_any(["neut","happ","lsur","flus","shoc"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1a.png"
        attribute brow default if_any(["sad","cry","pani","yand","nerv"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1b.png"
        attribute brow default if_any(["laug","vsur","worr","sedu"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1c.png"
        attribute brow default if_any(["anno","pout"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1d.png"
        attribute brow default if_any(["angr","vang"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1e.png"
        attribute brow default if_any(["curi","doub"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1f.png"


        attribute brow default if_any(["dist"]) if_all(["oe"]) if_not(["ce"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b2a.png"
        attribute brow default if_any(["dist"]) if_all(["ce"]) if_not(["oe"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b3c.png"



        attribute b1a:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1a.png"
        attribute b1b:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1b.png"
        attribute b1c:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1c.png"
        attribute b1d:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1d.png"
        attribute b1e:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1e.png"
        attribute b1f:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b1f.png"
        attribute b2a:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b2a.png"
        attribute b2b:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b2b.png"
        attribute b2c:
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b2c.png"
        attribute b3a if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b3a.png"
        attribute b3b if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b3b.png"
        attribute b3c if_any(["e1d","e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/sayori/sayori_turned_eyebrows_b3c.png"




    group special:

        attribute s_scream:
            "mod_assets/MPT/sayori/sayori_turned_special_scream.png"



layeredimage sayori tap: 

    group outfit:
        attribute uniform default:
            "mod_assets/MPT/sayori/sayori_tapping_uniform_bodybase.png"
        attribute casual:
            "mod_assets/MPT/sayori/sayori_tapping_casual_bodybase.png"

    always "mod_assets/MPT/sayori/sayori_tapping_facebase.png"



    group mood: 



        attribute nerv default null 
        attribute angr null 
        attribute dist null 
        attribute neut null 
        attribute pout null 



    group blush: 
        attribute nobl default null 
        attribute awkw null 
        attribute blus null 
        attribute blaw null 
        attribute bful null 



    group nose:


        attribute nose default if_any(["nobl"]):
            "mod_assets/MPT/sayori/sayori_tapping_nose_n1.png"
        attribute nose default if_any(["awkw"]):
            "mod_assets/MPT/sayori/sayori_tapping_nose_n2.png"
        attribute nose default if_any(["blus"]):
            "mod_assets/MPT/sayori/sayori_tapping_nose_n3.png"
        attribute nose default if_any(["blaw"]):
            "mod_assets/MPT/sayori/sayori_tapping_nose_n4.png"
        attribute nose default if_any(["bful"]):
            "mod_assets/MPT/sayori/sayori_tapping_nose_n5.png"


        attribute n1:
            "mod_assets/MPT/sayori/sayori_tapping_nose_n1.png"
        attribute n2:
            "mod_assets/MPT/sayori/sayori_tapping_nose_n2.png"
        attribute n3:
            "mod_assets/MPT/sayori/sayori_tapping_nose_n3.png"
        attribute n4:
            "mod_assets/MPT/sayori/sayori_tapping_nose_n4.png"
        attribute n5:
            "mod_assets/MPT/sayori/sayori_tapping_nose_n5.png"



    group mouth:


        attribute cm default if_any(["pout"]):
            "mod_assets/MPT/sayori/sayori_tapping_mouth_m2.png"
        attribute cm default if_any(["neut","nerv","angr","dist"]):
            "mod_assets/MPT/sayori/sayori_tapping_mouth_m3.png"


        attribute om if_any(["nerv"]):
            "mod_assets/MPT/sayori/sayori_tapping_mouth_m1.png"
        attribute om if_any(["neut","pout","angr","dist"]):
            "mod_assets/MPT/sayori/sayori_tapping_mouth_m4.png"



        attribute m1:
            "mod_assets/MPT/sayori/sayori_tapping_mouth_m1.png"
        attribute m2:
            "mod_assets/MPT/sayori/sayori_tapping_mouth_m2.png"
        attribute m3:
            "mod_assets/MPT/sayori/sayori_tapping_mouth_m3.png"
        attribute m4:
            "mod_assets/MPT/sayori/sayori_tapping_mouth_m4.png"



    group eyes if_not(["n5","bful"]):


        attribute oe default if_any(["neut","nerv"]):
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e1.png"
        attribute oe default if_any(["pout","dist"]):
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e2.png"
        attribute oe default if_any(["angr"]):
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e5.png"


        attribute ce if_any(["neut","nerv","pout","angr","dist"]):
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e6.png"



        attribute e1:
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e1.png"
        attribute e2:
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e2.png"
        attribute e3:
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e3.png"
        attribute e4:
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e4.png"
        attribute e5:
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e5.png"
        attribute e6:
            "mod_assets/MPT/sayori/sayori_tapping_eyes_e6.png"



    group eyebrows if_not(["n5","bful"]):


        attribute brow default if_any(["neut"]):
            "mod_assets/MPT/sayori/sayori_tapping_eyebrows_b3.png"
        attribute brow default if_any(["nerv","dist"]):
            "mod_assets/MPT/sayori/sayori_tapping_eyebrows_b1.png"
        attribute brow default if_any(["pout","angr"]):
            "mod_assets/MPT/sayori/sayori_tapping_eyebrows_b2.png"



        attribute b1:
            "mod_assets/MPT/sayori/sayori_tapping_eyebrows_b1.png"
        attribute b2:
            "mod_assets/MPT/sayori/sayori_tapping_eyebrows_b2.png"
        attribute b3:
            "mod_assets/MPT/sayori/sayori_tapping_eyebrows_b3.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
