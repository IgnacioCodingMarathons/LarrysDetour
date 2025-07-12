function Script()
    if World.feindDying then
        if Player.holds("Giant Apple") then
            if dialogue(("feind","sqcomplete","snowy/sq complete.wav")) then end
            playAnimation("feind",true,"normal")
            writeToSave("feindSaved","boolean",true)
            World.feindSaved = true
            World.feindDying = false
            achievement("Fiend Care.ach")
            dropItem("feind","heart",6)
            dropItem("feind","apple",2)
            giveLives(3)
        else if dialogue(("feind","noapple","snowy/no apple.wav")) then end
    else if dialogue(("feind","hi","snowy/hi.wav")) then end
end