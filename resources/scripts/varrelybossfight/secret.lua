function Script()
    pp=pickyPrompt("This menu is a secret, but you found it. Now, would you like to either...",["Stun for 30 seconds","SHOOT HIM FUCKING 17 TRILLION TIMES"])
    if pp="SHOOT HIM FUCKING 17 TRILLION TIMES" then
        executeFrom("varrely","stun",{"stunnedHowMuch":60})
        playAnimation("larry","villainSHOOTFUCKING17BILLIONTIMES") -- SHOOT HIM 17 BILLION TIMES WHAT THE FUCK
        if waitForAnimation("larry","villainSHOOTFUCKING17BILLIONTIMES") then setProperty("varrely","health",0) end
    else if pp="Stun for 30 seconds" then executeFrom("varrely","stun",{"stunnedHowMuch":60}) end
end