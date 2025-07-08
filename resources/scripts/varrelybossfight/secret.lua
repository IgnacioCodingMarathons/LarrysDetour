function Script()
    pp=pickyPrompt(["Stun for 30 seconds","SHOOT HIM FUCKING 17 TRILLION TIMES"])
    if pp="SHOOT HIM FUCKING 17 TRILLION TIMES" then
        executeFrom("varrely","stun",{"stunnedHowMuch":60})
        playAnimation("larry","villainSHOOTFUCKING17BILLIONTIMES") -- SHOOT HIM 17 BILLION TIMES WHAT THE FUCK
        if waitForAnimation("larry","villainSHOOTFUCKING17BILLIONTIMES") then setProperty("varrely","health",0) end
    else if pp="Stun for 30 seconds" then executeFrom("varrely","stun",{"stunnedHowMuch":60}) end
end