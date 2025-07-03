import os
import random
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
hero_list = [[30, 20, 50],
            [50, 30, 20],
            [20, 50, 30]]

problem_list = [
    [40, 20, 40],  
    [60, 10, 30],  
    [25, 5,  70],  
    [20, 60, 20],  
    [35, 15, 50],  
    [55, 35, 10],  
    [50, 30, 20],  
    [30, 50, 20],  
    [20, 20, 60],  
    [15, 70, 15],  
]
problem_set = [
''' Vault 88 Gone Loud  
Clowns, hostages, explosives, livestreams. The crew’s wild—but the leader?  
Chillingly calm. You’ll need a silver tongue and steady nerves before it all blows.''',
'''Dronepocalypse at SkyMall  
Drones swarm like hornets. Dodging them takes brains, reflexes—and no panic  
when shopping bags explode.''',
''' Glamageddon: Red Carpet Riot  
Flash mobs sob, celebs cry in couture, paparazzi swarm. Calm it down,  
spin the story, and drop a killer one-liner for the feeds.''',
'''Pit Fight Pandemonium  
Rage-jacked fighters. Electrified cages. A brick-tossing crowd.  
Subtlety’s dead—go loud or go home in pieces.''',
''' Midnight Gala Gone Ghost  
No entry. No prints. Just whispers, glitches, and lipstick on a mirror  
that wasn’t there. You’ll need stealth, brains, and ice-cold composure.''',
'''BioLab Blackout: Subject 47 Breach  
AI’s down. Power’s out. One chamber's open—and something's loose.  
Bring brains, nerves, and legs fast enough to live.''',
'''Skystrike: Lightning Protocol  
A rogue satellite rains EM hell. Civilians panic, systems fail.  
You’ll need tech skills—and serious crowd control.''',
'''Sewer Saints’ Salvation Day  
Fanatics with bombs and holy mold hold the sewers. Their prophet rants  
in riddles. Talk them down—or scare them into silence.''',
'''Live Love Hostage  
The crowd thinks it’s a show. The crew’s panicking. The villains quote  
fanfic. Get in, play along, and rewrite the ending—with flair.''',
'''The Thing in the Traffic  
A radioactive brute laughs as it hurls food trucks. Cars crash, people run.  
No time for talk—stop it fast.'''
]

def result(heronum, pronum):
    score = 100 - (abs(hero_list[heronum][0] - problem_list[pronum][0]) +
    abs(hero_list[heronum][1] - problem_list[pronum][1]) +
    abs(hero_list[heronum][2] - problem_list[pronum][2]))
    return score

print('''> SYSTEM ONLINE_   
> TEAM ID: INFAMOUS IMPETUS
> STATUS: STANDBY  
> BBC PROTOCOL LOADED ✓  
> CHARACTERS: CAPT. CAPTIVATING | CANNY GRANNY | DAWN OF BRAWN

:: ENGAGE | DISPATCH | IMPACT ::''')
player_name = input(''':: Please input your Dispatcher Codename to begin ::
> USERNAME: ''')
print(f"> Codename recognized: [Dispatcher: {player_name}]")
print("> ACCESS LEVEL: FIELD COMMAND AUTHORIZED\n")
introduction = input(''':: Do you understand your assigned role within INFAMOUS IMPETUS? ::
TYPE Y/N: ''').lower()
while introduction == 'n':
    if introduction == 'n':
        print('''> SYSTEM BRIEFING:  
You are a Dispatcher — the mind behind the mission.  
You won’t fight. You’ll command.  

Every crisis you face must be handled with Brain, Brawn, or Charm.  
Your job is to analyze, decide, and deploy the right hero.  

Make the right call — save the day.  
Make the wrong one — deal with the fallout.
''')
    introduction = input(''':: Do you understand your assigned role within INFAMOUS IMPETUS? ::
TYPE Y/N: ''').lower()
    if introduction == 'y':
        clear()


briefing = input('''> ROLE CONFIRMED_  
> Welcome, Dispatcher.

:: You are now officially authorized to command INFAMOUS IMPETUS operations. ::

> Would you like a briefing on the heroes under your command?
TYPE Y/N: ''').lower()
while briefing =='y':
    if briefing == 'y':
        print('''
Captain Captivating (41 M)-
BRAIN: 30% | BRAWN: 20% | CHARM: 50%
Once a war hero, he was pulled from the brink after a mission went wrong.  
Officially: healed.  
Unofficially: experimented on with charm-boosting tech and bio-repair.
Now he’s a walking PR machine — calming crowds, smiling through gunfire,  
and selling hope like it's bottled water.
He just says, “They fixed me… sort of.”
Note-
“Don’t send him where things need smashing. Send him where things need selling.”
“Turns enemy mobs into fan clubs if you give him a second to talk.”
“Terrible at puzzles. Flirts with bombs.”

Canny Granny (Unknown Age F)-
BRAIN: 50% | BRAWN: 30% | CHARM: 20%
Centuries-old vampire — drained blood and wisdom alike.  
Got bored, turned herself in one night.  
Now the government keeps her on a leash (sort of).
Prefers night missions, hates small talk,  
and calls smartphones “glowstones of distraction.”
Note-
"Operates solo. Assign missions, then get out of her way.”
“Best way to describe is cold and ominous.”
“Avoid daylight ops unless you enjoy being called crispy bait.”

Dawn of Brawn (27 F)-
BRAIN: 20% | BRAWN: 50% | CHARM: 30%
Raised in the Iron Quarter — forged in street fights and rigged rings.  
A reactor blast nearly wiped it out. She survived, dragging others out,  
soaking up raw energy.
Now she’s a walking wrecking ball.  
Doesn’t talk much. Doesn’t need to.
Note-
“Ideal for demolition missions. Or stubborn doors.”
“Keep comms short. She doesn’t do pep talks.”
“Once punched a runaway truck into a U-turn.”
''')
    briefing = input('''
> Would you like a briefing on the heroes under your command?
TYPE Y/N: ''').lower()
    if briefing == 'n':
        clear()



cunt = 'y'
count = 0
while cunt == 'y':
    gennum = random.randint(0,9)
    print(problem_set[gennum])
    heronum = int(input(''':: SITUATION PROFILE UPLOADED  
:: Resources Available: 3 Operatives  
:: Select Operative for Deployment

[1] Captain Captivating  
[2] Canny Granny  
[3] Dawn of Brawn
    
                        
>> Enter Selection (1-3): '''))
    score = result(heronum-1, gennum)
    if score >= 80:
        print("Success.")
        count = 0
    elif 60 <= score < 80:
        print("Partial Success.")
    else:
        print("Failure.")
        count += 1
    
    if count == 3:
        clear()
        print('''
:: ALERT ::
Three consecutive failures logged.

:: DISPATCH ACCESS REVOKED ::
You’ve been relieved of duty, Dispatcher.

INFAMOUS IMPETUS will now proceed under secondary protocol.
''')
        break


    cunt = input(''':: NEW INCIDENT DETECTED :: 
:: Threat Level: Active  ::
Proceed to next mission? (Y/N) ''').lower()






