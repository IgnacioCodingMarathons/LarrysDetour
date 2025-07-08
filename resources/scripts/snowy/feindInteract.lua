function Script()
    if World.feindDying then
        if Player.holds("Giant Apple") then
            dialogue("feind","sqcomplete","snowy/sq complete.wav")
            playAnimation("feind",true,"normal")
            writeToSave("feindSaved","boolean",true)
            World.feindSaved = true
            World.feindDying = false
            achievement("Fiend Care.ach")
            dropItem("feind","heart",6)
            dropItem("feind","apple",2)
            giveLives(3)
        else dialogue("feind","noapple","snowy/no apple.wav") end
    else dialogue("feind","hi","snowy/hi.wav") end
end