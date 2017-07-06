#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Templates(object):
    BANNER = """ᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛ
                        ______ _           _        ___            _  ______ _                 _                           
                        | ___ \ |         | |      / _ \          | | | ___ \ |               | |_                         
                        | |_/ / |_   _ ___| |__   / /_\ \_ __   __| | | |_/ / | ___   ___   __| (_)                        
                        |  __/| | | | / __| '_ \  |  _  | '_ \ / _` | | ___ \ |/ _ \ / _ \ / _` |                          
                        | |   | | |_| \__ \ | | | | | | | | | | (_| | | |_/ / | (_) | (_) | (_| |_                         
                        \_|   |_|\__,_|___/_| |_| \_| |_/_| |_|\__,_| \____/|_|\___/ \___/ \__,_(_)                        
                                                                                                                           
                                                                                                                           
 _____ _                          _              _____ _               _     _____                           _             
/  __ \ |                        | |            /  ___| |             | |   |  __ \                         | |            
| /  \/ |__   __ _ _ __ __ _  ___| |_ ___ _ __  \ `--.| |__   ___  ___| |_  | |  \/ ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| |   | '_ \ / _` | '__/ _` |/ __| __/ _ \ '__|  `--. \ '_ \ / _ \/ _ \ __| | | __ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| \__/\ | | | (_| | | | (_| | (__| ||  __/ |    /\__/ / | | |  __/  __/ |_  | |_\ \  __/ | | |  __/ | | (_| | || (_) | |   
 \____/_| |_|\__,_|_|  \__,_|\___|\__\___|_|    \____/|_| |_|\___|\___|\__|  \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|   
ᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛ"""

    BANNER_THEWELL = """ᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛ\n
                             _____ _            _    _      _ _ 
                            |_   _| |          | |  | |    | | |
                              | | | |__   ___  | |  | | ___| | |
                              | | | '_ \ / _ \ | |/\| |/ _ \ | |
                              | | | | | |  __/ \  /\  /  __/ | |
                              \_/ |_| |_|\___|  \/  \/ \___|_|_|
                                                                
            
  ᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗘᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛᗛ"""

    INTRO = "\n \nᗘᗘᗘ FOREWORD:\n" \
            "        The Plush and Blood Roleplaying system was designed around two core concepts, story telling and immersed player characters.\n" \
            "Any RP’r out there reading this is right about now tallying up how they can manipulate and twink the system.  That is not\n" \
            "the purpose of the PB:RP.  The purpose of the PB:RP is to play a character within a well constructed story.  Abuse and \n" \
            "manipulation of the system is a sign of a player that is not mature enough to put aside their ego and allow themselves \n" \
            "to be absorbed into the world for good or bad.  The point here is not get the best rolls, the highest stat or the most\n" \
            "powerful character.  \n \n" \
            "        The point here is to play. Storytelling is a core feature and GM’s should be ready for the players\n" \
            "to wreck all sorts of mischief within their well-outlined story.  I for one speaking as a seasoned GM can tell you that\n" \
            "no matter how well the story is planned ahead of time the players will almost certainly derail the train, set fire to it\n" \
            "and kill themselves in a cave-in... *AHEM*... \n" \
            "        When all they needed to do was follow the tracks.  GM’s should be quick of wit and mighty in their imagination. Players\n" \
            "should respect the story for the most part but at the same time play their characters.  Mary-sue and God-mode are not RP. \n" \
            "Being cool, dark, and edged with angst are not RP. We’d all love to run around in black leather, high kicking light switches,\n" \
            "and shooting flies from the air, but we are not our characters.  A mature player should play their character with \n" \
            "conviction no matter their own personal feelings.  A Lawful Good character should NEVER agree with a Lawful Evil one.  \n" \
            "A character with an INT of 2 cannot figure out the trap even though it is clear to you.  A character of low CHA is never\n" \
            "going to woo.  A character with the Blind FLAW is surely going to infuriate the GM… \n \n" \
            "        Whether you are a Player or a GM the main goal is to have fun.  Enjoy the story, enjoy the actions that cause it \n" \
            "to develop down paths never considered, enjoy the relationships built within and without. \n \n" \
            "        And as I have always said, a GM will never kill their players, but will allow the players to kill themselves. When I ask\n" \
            " you “Are you sure?” this is a non too subtle hint that you may want to think on your actions one more time.  Doesn’t\n" \
            " mean that you are wrong, but those words are a reprise.  \n \n" \
            "        You are stuffed animals in a world on the brink of collapse.  Whether you live in Utopia, serve the Broken Circle,\n" \
            "fight to remain free, prowl the wastes, or are just trying to survive, always remember who you are.\n \n" \
            "Welcome to Plush and Blood.\n \n-Corey “TiredOrangeCat” Messer ᗛᗛᗛ\n \n" \
            "ᗘᗘᗘ Each player starts with 42 points. As they progress through the game they will earn more points to put into \n" \
            "various stats/skills.  There is no traditional level system, rather as points are distributed to the player. The player \n" \
            "can then spend these points on their characters to enhance skills, stats, or in cases the GM deems acceptable, \n" \
            "purchase MERITS. ᗛᗛᗛ\n \n"

    NAME = "\n \nᗘᗘᗘ Your name, everyone needs a name.This is what the people will shout when they parade you through the streets \n" \
           "or tighten the noose about your neck. ᗛᗛᗛ \n \n" \
           "ᗘᗘᗘ Name: "

    SEX = "\n \nᗘᗘᗘ Do you have a bill and two bits, or a wallet?  We could go into the whole gender identity thing but really that \n" \
          "is better left for your long character description. ᗛᗛᗛ \n \n" \
          "ᗘᗘᗘ Sex: "

    SPECIES = "\n \nᗘᗘᗘ Birds of a feather, stripes and spots, short faced or long there is something to be said about one’s species.\n" \
              "One can lambast the stereotypes labeled upon the fangs and claws of some or chastise the typecast fallacy of the meek \n" \
              "in others. Suffice to say every species comes with its benefits and its baggage. For more details on the benefits of \n" \
              "each species enter [LAND] or [AIR] ᗛᗛᗛ \n \n" \
              "ᗘᗘᗘ Species List: "

    SPECIES_SELECT = 'ᗘᗘᗘPlease enter a species, \n [SWITCH] to switch Species Lists,\n [CANCEL] to return to you character sheet. \n \n ᗘᗘᗘ '

    HEALTH_POINTS = "\n \nᗘᗘᗘ This is generated primarily by your Con score. Your Health starts off as a direct copy of your Con score. \n" \
                    "3 Con = 3 Health. This can be raised by various merits/skills or by spending extra points to raise your health. \n" \
                    "Each HP costs 4 points.  The maximum HP achievable is 10, if you purchase anything over the max it becomes a marker. \n" \
                    "Once you have three health markers you are considered to have gained 1 natural SOAK. For every three markers \n" \
                    "after that you gain 1 additional natural SOAK up to a MAX of 3. Markers do not count as health. \n" \
                    "Natural SOAK stacks with Armor SOAK. ᗛᗛᗛ \n \n \nᗘᗘᗘHit Point Cost is based on your Natural HP. Please adjust accordingly."

    STATS = "\n \nᗘᗘᗘ Everyone starts with one freebie point in each stat, only by GM discretion or character specific circumstances can a STAT \n" \
            "be 0 or negative (Players cannot recoup the cost of a STAT by lowering it at creation) (see Negative STATS). For every \n" \
            "point you spend after correlates to the cost of the number. For example, lets say I want to raise my STR (strength),  \n \n" \
            "ᗘᗘ STR 1\n \nTo raise it to level 2 I need to put two points into it.  \n \nᗘᗘSTR 2\n \n   " \
            "To raise it to level 3 I need to put an additional 3 points into it.  \n \nᗘᗘSTR 3\n \n " \
            "  So raising STR to level 3 I have now spent 5 of my total points leaving me with 37 points. This goes for All STATs and Skills.\n " \
            "For an easy reminder here’s a table:  \n \nᗘᗘlv1 - 1 point (unless its a STAT then its free)\nᗘᗘ lv2 - 2 points \nᗘᗘlv3 - 3 points \n" \
            "ᗘᗘlv4 - 4 points\nᗘᗘ lv5 - 5 points\n \n" \
            "  So if you want to raise on of your STAT’s up to lv5 you will need to put 14 points into it.  \n" \
            "With a Racial Bonus, STATS are calculated like so,  \n \n Free Point + Racial Point + spent points  \n \nᗘᗘex. Cat (DEX+1)\n \nᗘᗘ  0 0 - - - DEX  \n \n" \
            "Both the free point and racial point are added first, then you can spend points to raise it. A third point still costs 3, \n" \
            "a fourth 4, and a fifth 5. So it will still cost you 12 points to raise it from lv2 to lv5 ᗛᗛᗛ \n \n"

    STUFFING = "\n \nᗘᗘᗘ This is the thing that keeps you what you are. The end all of your life force. Your HP can be reduced to 0 and if you \n" \
               "have enough STUFFING you may be brought back to life. A Plush starts out with 10 STUFFING points. Every 10 years (after \n" \
               "the age of 10) they lose 1 point. If your HP is reduced to 0 you lose 1 point. If you are grievously wounded (missing \n" \
               "limb, shotgun blast, bomb) you lose 1 point. STUFFING points cannot normally be restored. If your STUFFING is reduced to \n" \
               "5, you will lose a major STAT point and 1 HP. If your STUFFING is reduced to 3, you will lose an additional stat point \n" \
               "and HP. If your STUFFING falls to 0 your character is nothing more then a pile of tattered rags. There are only a few \n" \
               "Master Weavers that can restore one or two STUFFING points. But they are all under Brown’s control. ᗛᗛᗛ\n \n"

    FACTIONS = "\n \nᗘᗘᗘ UNSTUFFEDᗛᗛᗛ  \n" \
               "- BROKEN CIRCLE \n" \
               "– President Brown RENEWED CIRCLE \n" \
               "- Rebels (Cromwell pre fall of New Camelot) UTOPIAN \n" \
               "- Civilian (most of them under Brown) KINGS OF THE LAND \n" \
               "- Disbanded THE MEEK \n" \
               "- Disbanded NIGHT MARKET \n" \
               "- Underground/Black Market INVISIBLE BLADE \n" \
               "- Assassins Guild LIBERATI ARCANUM \n" \
               "- Mages Guild (very rare not available for campaign) KEEPERS OF KNOWLEDGE \n" \
               "- Historians Guild/Archeologists/Scholars \n" \
               "- None \n \n " \
               "-ᗘᗘᗘMEMORY’S THREADSᗛᗛᗛ " \
               "- COALITION \n" \
               "- COLLAND \n" \
               "- CONVOY: ASH FUR \n" \
               "- CONVOY: BELAMY’S BUGGERERS \n" \
               "- CONVOY: CITY STALKERS \n" \
               "- SLAVER: HARRISVILLE \n" \
               "- SLAVER: NATHAN’S ATOL \n" \
               "- ORDER OF CYD \n \n" \
               "ᗘᗘᗘ Enter your Faction: "

    ALIGNMENT = "\n \nᗘᗘᗘ The fundamental question, good, evil, neutral. \n" \
                "There are nine classical Alignments to choose from to fit your character.  \n" \
                "[LG] Lawful Good - Will never do wrong, the good guy, incorruptible (Police). \n" \
                "[NG] Neutral Good - The good guy, always tries to do what's right (Typical Hero). \n" \
                "[CG] Chaotic Good - Will do anything in the name of good (Rebel)\n" \
                "  [LN] Lawful Neutral – Order beyond concepts of good and evil (Judge). \n" \
                "[TN] True Neutral – Impartial observer of the world. \n" \
                "[CN] Chaotic Neutral - Follows his own heart, shirks rules and traditions, free spirit.\n" \
                "  [LE] Lawful Evil - Evil with a set code, idealistic (Dictator). \n" \
                "[NE] Neutral Evil - Neither bound by any sort of honor or tradition nor disorganized and pointlessly violent (Mercenary). \n" \
                "[CE] Chaotic Evil - Evil for evils sake, crazy and will go out of their way to torture and maim (Psychopath).ᗛᗛᗛ \n \n" \
                "ᗘᗘᗘ Enter your Alignment: "

    SKILLS = "This is a large part of what makes your character unique.  A character’s skill set can ultimately determine their \n" \
             "success or failure during a scenario.  One will never find what they are looking for without a successful Investigation\n" \
             " check.  One will never peacefully haggle a price without Persuasion.  One will not come out of a bar fight without\n " \
             "Brawl.  These Skills are an extension of your POCC/SOCC and your character’s personality.   Choose them wisely but at \n" \
             "the same time keep your character in mind.  You are not playing to win the mainipulate-the-skill-tree game, you are\n" \
             "RPing your character.  Do you have useless skills? I know I do, maybe your character has her fair share as well.\n \n Much" \
             "like the STATS, SKILLS are purchased in the same manor, however you will always have to buy your first point in a skill.\n \n" \
             "ᗘᗘᗘ Enter Skill you'd like to adjust: (Enter 'cancel' to exit skills)"

    SKILLS_SELECT = "ᗘᗘᗘ Enter Skill you'd like to adjust: \n[CANCEL] to exit skills)\nᗘᗘᗘ"

    SKILLS_STATS_ADJUST = "\nᗘᗘᗘ Enter a number [1 - 5] ᗘᗘᗘ "

    POCC = "ᗘᗘ PRIMARY OCCUPATIONS : (bonuses are added directly to your skills) \n" \
           "ᗘᗘᗘ [SOLDIER] -(+1 Fire +1 Sur)\n" \
           "ᗘᗘᗘ [MEDIC] -(+1 Med +1 Academics)\n" \
           "ᗘᗘᗘ [TECH] -(+1 Computers +1 Sci)\n" \
           "ᗘᗘᗘ [LAW ENFORCEMENT] -(+1 Fire +1 Investigation)\n" \
           "ᗘᗘᗘ [CRIMINAL] -(+1 Larceny +1 Streetwise)\n" \
           "ᗘᗘᗘ [OCCULTISTS] -(+1 Occult +1 Investigation)\n" \
           "ᗘᗘᗘ [SCHOLAR] -(+1 Academics +1 Science)\n" \
           "ᗘᗘᗘ [PSI] -(+1 Concentration +1 Empathy)\n" \
           "ᗘᗘᗘ [MAGE] -(+1 Concentration +1 Academics)\n" \
           "ᗘᗘᗘ [ATHLETE] -(+2 Athletics)"

    SELECT_POCC = "\nᗘᗘᗘ Please select a Primary Occupation or [CANCEL] ᗘᗘ "
    SELECT_SOCC = "\nᗘᗘᗘ Please select a Specialist Occupation or [CANCEL] ᗘᗘ "
    SELECT_SOCC_ERROR = "\nᗘᗘᗘ No Primary Occupation [POCC] has been selected.\n  " \
                        "Please select a POCC before selecting a Specialist Occupation.\n" \
                        "Press [ENTER] to return to the character sheet."


    GET_MERITS = '\nᗘᗘᗘ Please select a Merits list to view [MENTAL] [PHYSICAL] [SOCIAL] [CANCEL]: '
    GET_FLAWS = '\nᗘᗘᗘ Please select a Flaws list to view [MENTAL] [PHYSICAL] [STATS] [CANCEL]: '

    SELECT_MF = "\nᗘᗘ [CHANGE LIST], [CANCEL] or Enter Merit:"

    NO_EXP_MSG = "\nᗘᗘᗘ You do not have sufficient experience points remaining. Press ENTER to continue."

    VALID_ENTRY = "\nᗘᗘᗘ Please enter a valid entry."

    GOODBYE = "\nᗘᗘᗘ Thank you for using the Plush and Blood: Character Sheet Generator."

    CONTINUE = 'ᗛᗛᗛ Press Return to continue ᗘᗘᗘ'
    

class CharacterControlTemplates(object):
    
    PLAYER_CHOICE = "\n\nᗘᗘᗘ What do you do? [HELP] for directions ᗘᗘᗘ "
    PLAYER_HELP = "ᗘᗘᗘ Interaction: \n" \
                  "[LOOK] - Take a gander and get a lay of the land. \n" \
                  "[SEARCH] - Take the time to investigate with your search skill. \n" \
                  "[USE] - Attempt to use an object or item. \n" \
                  "[TAKE] - Attempt to take an object or item. \n\n" \
                  "Navigation: \n" \
                  "[TURN] - Turn a direction you would like to face in order to search or move. \n" \
                  "[MOVE] - Move in increments based on your movement rate. \n" \
                  "[CLIMB] - Attempt to climb a surface. \n" \
                  "[JUMP] - Attempt to jump. \n\n" \
                  "Character Management:\n" \
                  "[INVENTORY] - Access your characters inventory. \n" \
                  "[EQUIP] - Attempt to equip an item. \n" \
                  "[UNEQUIP] - Place an equipped item back in your inventory. \n" \
                  "Combat:" \
                  "[ATTACK] - Use your currently equipped weapon to attack. \n" \
                  "[BLOCK] - Attempt to block the next attack. \n" \
                  "[FLEE] - Attempt to flee the battle. \n" \
                  "ᗛᗛᗛ"

    PLAYER_DIRECTIONS = "ᗘᗘᗘ [WEST], [EAST], [NORTH], [SOUTH] ᗛᗛᗛ"

    PLAYER_MOVE = "num, or num:direction.  ex. 1 or 1:WEST"

    PLAYER_LOOK = "ᗘᗘᗘ [LEFT], [RIGHT], [FORWARD], [BACKWARDS], [AROUND], at [OBJECT] ᗛᗛᗛ"


# ᗘᗘᗘᗛᗛᗛ