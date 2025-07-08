function Script() 
    Player.footstepSound = 2
    if Place.exists("feind") and Place.getObj("feind").isDying then
        playAnimation("feind",true,"dying")
        Place.music = "snowy/panic.wav"
    else
        playAnimation("feind",true,"normal")
        Place.music = "snowy/normal.wav"
    end
    if not Place.exists("feind") then
        addObject("noFeindSign",0,-20)
    end
end