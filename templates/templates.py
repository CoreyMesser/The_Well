# ᗘᗘᗘᗛᗛᗛ
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

    INTRO = "\n \nᗘᗘᗘ Each player starts with 42 points. As they progress through the game they will earn more points to put into \n" \
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

    HEALTH_POINTS = "\n \nᗘᗘᗘ This is generated primarily by your Con score. Your Health starts off as a direct copy of your Con score. \n" \
                    "3 Con = 3 Health. This can be raised by various merits/skills or by spending extra points to raise your health. \n" \
                    "Each HP costs 4 points.  The maximum HP achievable is 10, if you purchase anything over the max it becomes a marker. \n" \
                    "Once you have three health markers you are considered to have gained 1 natural SOAK. For every three markers \n" \
                    "after that you gain 1 additional natural SOAK up to a MAX of 3. Markers do not count as health. \n" \
                    "Natural SOAK stacks with Armor SOAK. ᗛᗛᗛ \n \n"

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

    def print_char_sheet(self, character_dict):
        sheet = "[NAME]    NAME:  {name} \n" \
                "[SPECIES] SPECIES:  {species} \n" \
                "          SPECIES SZIE:  {species_size} \n" \
                "[SEX]     SEX: {sex} \n" \
                "[ FACTION] FACTION:  {faction} \n" \
                "[ALG]     ALIGNMENT:  {alg} \n" \
                "[POCC]    PRIMARY OCCUPATION: {pocc} \n" \
                " [SOCC]    SECOND OCCUPATION:  {socc} \n" \
                "\n" \
                "  [HP]      HP: {hp} \n" \
                "[STUFF]   STUFFING: {stuffing} \n" \
                "          SANITY: {sanity} \n" \
                "          SOAK: {soak} \n" \
                "\n" \
                "  ᗘᗘᗘ STATS:  ᗛᗛᗛ\n" \
                "[STR]     STR: {str} \n" \
                " [INT]     INT: {int} \n" \
                "[DEX]     DEX: {dex} \n" \
                " [CON]     CON: {con} \n" \
                " [WIS]     WIS: {wis} \n" \
                " [CHA]     CHA: {cha} \n" \
                "\n" \
                "  ᗘᗘᗘ SKILLS:  ᗛᗛᗛ\n" \
                "   [SKILLS]  SKILLS: {skills}\n" \
                "[MERITS]  MERITS: {merits}\n" \
                "[FLAWS]   FLAWS: {flaws}\n \n" \
                "ᗘᗘᗘ XP POINTS TOTAL {exp_total} ᗛᗛᗛ\n" \
                "ᗘᗘᗘ XP POINTS REMAINING {exp_remaining} ᗛᗛᗛ\n".format(**character_dict)
        return sheet

    def print_species_list(self, species):
        species_class = self.species_dict[species]
        for k in species_class:
            print(k, species_class[k])

    species_dict = {'LAND': {'APE': ['M/O', 1, 'wis'],
                             'BADGER': ['M/O', 1, 'con'],
                             'BEAR': ['L/O', 1, 'str'],
                             'BOVINE': ['L/H', 1, 'con'],
                             'BOAR': ['M/H', 1, 'hp'],
                             'CAT': ['M/C', 1, 'dex'],
                             'CAMEL': ['L/H', 2, 'con'],
                             'CHEETAH': ['M/C', 2, 'dex'],
                             'DOG': ['M/C', 1, 'dex'],
                             'DEER': ['M/H', 1, 'cha'],
                             'ELEPHANT': ['L/H', 2, 'wis'],
                             'EMU': ['M/H', 1, 'dex'],
                             'FERRET': ['M/H', 1, 'dex'],
                             'FOX': ['M/O', 1, 'cha'],
                             'GIRAFFE': ['L/H', 1, 'wis'],
                             'GOAT': ['M/H', 1, 'wis'],
                             'HAMSTER': ['S/H', 1, 'con'],
                             'HIPPO': ['L/H', 1, 'con'],
                             'HORSE': ['L/H', 1, 'str'],
                             'HYENA': ['M/C', 1, 'con'],
                             'KANGAROO': ['M/H', 1, 'con'],
                             ' KOALA': ['M/H', 1, 'wis'],
                             'LEMUR': ['M/H', 1, 'wis'],
                             'LEOPARD': ['M/C', 1, 'dex'],
                             'LION': ['M/C', 1, 'str'],
                             'LYNX': ['M/C', 1, 'con'],
                             'MANED WOLF': ['M/C', 1, 'dex'],
                             'MEERKAT': ['S/H', 1, 'dex'],
                             'MICE': ['S/H', 1, 'dex'],
                             'MINK': ['S/H', 1, 'cha'],
                             'MONGOOSE': ['S/H', 1, 'dex'],
                             'MONKEY': ['M/O', 1, 'int'],
                             'OSTRICH': ['M/H', 1, 'con'],
                             'OTTER': ['M/O', 1, 'con'],
                             'PIG': ['M/H', 1, 'con'],
                             'PLATYPUS': ['M/H', 1, 'con'],
                             'PUMA': ['M/C', 1, 'dex'],
                             'RABBIT': ['M/H', 1, 'dex'],
                             'RACCOON': ['M/O', 1, 'int'],
                             'RAT': ['M/O', 1, 'dex'],
                             'RED PANDA': ['M/O', 1, 'int'],
                             'RHINO': ['L/H', 1, 'str'],
                             'SEAL': ['M/C', 1, 'con'],
                             'SHREW': ['S/H', 1, 'int'],
                             'SLOTH': ['M/H', 1, 'con'],
                             'SKUNK': ['M/H', 1, 'con'],
                             'SQUIRREL': ['M/H', 1, 'dex'],
                             'TIGER': ['M/C', 1, 'str'],
                             'TURTLE': ['M/O', 1, 'soak'],
                             'WEASEL': ['M/C', 1, 'dex'],
                             'WOLF': ['M/C', 1, 'int'],
                             'ZEBRA': ['L/H', 1, 'wis']
                             },
                    'AIR': {'BAT': ['S/O', 1, 'dex'],
                            'BALD/WHITE TAILED EAGLE': ['L/C', 1, 'str'],
                            'BLUE BIRD': ['S/H', 1, 'int'],
                            'BLUE JAY': ['M/H', 1, 'int'],
                            ' CARDINAL': ['M/H', 1, 'int'],
                            'CHICKEN': ['M/H', 1, 'con'],
                            'CRANE': ['M/H', 1, 'int'],
                            ' CROW': ['M/O', 1, 'con'],
                            ' DOVE': ['S/H', 1, 'cha'],
                            'DUCK': ['M/H', 1, 'wis'],
                            'EAGLE': ['M/C', 1, 'str'],
                            'FLAMINGO': ['M/H', 1, 'cha'],
                            'GRAY JAY': ['M/H', 1, 'con'],
                            'HERON': ['M/H', 1, 'wis'],
                            'HUMMINGBIRD': ['S/H', -1, 'con'],
                            'SEA EAGLE': ['L/C', 1, 'con'],
                            ' SEAGULL': ['M/C', 1, 'dex'],
                            ' SWAN': ['M/H', 1, 'cha'],
                            'SWALLOW': ['S/H', 1, 'dex'],
                            'PENGUIN': ['M/C', 1, 'int'],
                            'PEACOCK': ['M/H', 1, 'cha'],
                            'PUFFIN': ['M/C', 1, 'cha'],
                            'RAVEN': ['M/O', 1, 'int'],
                            ' RED TAIL HAWK': ['M/C', 1, 'str']
                            }
                    }

    skills_dict = {"MENTAL ": {"Academics ": 0,
                               "Computer ": 0,
                               "Concentration ": 0,
                               "Crafting ": 0,
                               "Investigation ": 0,
                               "Medicine ": 0,
                               "Occult ": 0,
                               "Politics ": 0,
                               "Science  ": 0
                               },
                   "PHYSICAL ": {"Athletics": 0,
                                 "Brawl ": 0,
                                 "Demolitions ": 0,
                                 "Drive ": 0,
                                 "Firearms ": 0,
                                 "Larceny ": 0,
                                 "Ranged Weaponry ": 0,
                                 "Ride ": 0,
                                 "Stealth ": 0,
                                 "Survival": 0,
                                 "Weaponry  ": 0
                                 },
                   "SOCIAL ": {"Animal Kinship ": 0,
                               "Bluff ": 0,
                               "Empathy ": 0,
                               "Expression ": 0,
                               "Intimidate ": 0,
                               "Persuasion ": 0,
                               "Social Contacts ": 0,
                               "Streetwise ": 0,
                               "Subterfuge ": 0
                               }
                   }

    PRIMARY_OCC = []
    SECONDARY_OCC = []
