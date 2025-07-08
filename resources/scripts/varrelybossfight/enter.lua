function Script()
    Place.music = "varrely/boss.wav"
    dialogue("varrely","start","varrely/start.wav")
    World.healthBars = true
    executeFrom("varrely","startChaseSequence",{})
end