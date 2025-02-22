STATUS_BIT_FIELD = {
    0x4: "Asleep",
    0x8: "Poisoned",
    0x10: "Burned",
    0x20: "Frozen",
    0x40: "Paralyzed",
}

TYPE_MAP = {
    0x00: "Normal",
    0x01: "Fighting",
    0x02: "Flying",
    0x03: "Poison",
    0x04: "Ground",
    0x05: "Rock",
    0x07: "Bug",
    0x08: "Ghost",
    0x14: "Fire",
    0x15: "Water",
    0x16: "Grass",
    0x17: "Electric",
    0x18: "Psychic",
    0x19: "Ice",
    0x1A: "Dragon",
}


GEN_1_SPECIES = [
    "",
    "Rhydon",
    "Kangaskhan",
    "Nidoran",
    "Clefairy",
    "Spearow",
    "Voltorb",
    "Nidoking",
    "Slowbro",
    "Ivysaur",
    "Exeggutor",
    "Lickitung",
    "Exeggcute",
    "Grimer",
    "Gengar",
    "Nidoran",
    "Nidoqueen",
    "Cubone",
    "Rhyhorn",
    "Lapras",
    "Arcanine",
    "Mew",
    "Gyarados",
    "Shellder",
    "Tentacool",
    "Gastly",
    "Scyther",
    "Staryu",
    "Blastoise",
    "Pinsir",
    "Tangela",
    "MissingNo",
    "MissingNo",
    "Growlithe",
    "Onix",
    "Fearow",
    "Pidgey",
    "Slowpoke",
    "Kadabra",
    "Graveler",
    "Chansey",
    "Machoke",
    "Mr. Mime",
    "Hitmonlee",
    "Hitmonchan",
    "Arbok",
    "Parasect",
    "Psyduck",
    "Drowzee",
    "Golem",
    "MissingNo",
    "Magmar",
    "MissingNo",
    "Electabuzz",
    "Magneton",
    "Koffing",
    "MissingNo",
    "Mankey",
    "Seel",
    "Diglett",
    "Tauros",
    "MissingNo",
    "MissingNo",
    "MissingNo",
    "Farfetch'd",
    "Venonat",
    "Dragonite",
    "MissingNo",
    "MissingNo",
    "MissingNo",
    "Doduo",
    "Poliwag",
    "Jynx",
    "Moltres",
    "Articuno",
    "Zapdos",
    "Ditto",
    "Meowth",
    "Krabby",
    "MissingNo",
    "MissingNo",
    "MissingNo",
    "Vulpix",
    "Ninetales",
    "Pikachu",
    "Raichu",
    "MissingNo",
    "MissingNo",
    "Dratini",
    "Dragonair",
    "Kabuto",
    "Kabutops",
    "Horsea",
    "Seadra",
    "MissingNo",
    "MissingNo",
    "Sandshrew",
    "Sandslash",
    "Omanyte",
    "Omastar",
    "Jigglypuff",
    "Wigglytuff",
    "Eevee",
    "Flareon",
    "Jolteon",
    "Vaporeon",
    "Machop",
    "Zubat",
    "Ekans",
    "Paras",
    "Poliwhirl",
    "Poliwrath",
    "Weedle",
    "Kakuna",
    "Beedrill",
    "MissingNo",
    "Dodrio",
    "Primeape",
    "Dugtrio",
    "Venomoth",
    "Dewgong",
    "MissingNo",
    "MissingNo",
    "Caterpie",
    "Metapod",
    "Butterfree",
    "Machamp",
    "MissingNo",
    "Golduck",
    "Hypno",
    "Golbat",
    "Mewtwo",
    "Snorlax",
    "Magikarp",
    "MissingNo",
    "MissingNo",
    "Muk",
    "MissingNo",
    "Kingler",
    "Cloyster",
    "MissingNo",
    "Electrode",
    "Clefable",
    "Weezing",
    "Persian",
    "Marowak",
    "MissingNo",
    "Haunter",
    "Abra",
    "Alakazam",
    "Pidgeotto",
    "Pidgeot",
    "Starmie",
    "Bulbasaur",
    "Venusaur",
    "Tentacruel",
    "MissingNo",
    "Goldeen",
    "Seaking",
    "MissingNo",
    "MissingNo",
    "MissingNo",
    "MissingNo",
    "Ponyta",
    "Rapidash",
    "Rattata",
    "Raticate",
    "Nidorino",
    "Nidorina",
    "Geodude",
    "Porygon",
    "Aerodactyl",
    "MissingNo",
    "Magnemite",
    "MissingNo",
    "MissingNo",
    "Charmander",
    "Squirtle",
    "Charmeleon",
    "Wartortle",
    "Charizard",
    "MissingNo",
    "MissingNo",
    "MissingNo",
    "MissingNo",
    "Oddish",
    "Gloom",
    "Vileplume",
    "Bellsprout",
    "Weepinbell",
    "Victreebel",
]

GEN_1_ITEMS = [
    "",
    "Master Ball",
    "Ultra Ball",
    "Great Ball",
    "Poké Ball",
    "Town Map",
    "Bicycle",
    "?????",
    "Safari Ball",
    "Pokédex",
    "Moon Stone",
    "Antidote",
    "Burn Heal",
    "Ice Heal",
    "Awakening",
    "Parlyz Heal",
    "Full Restore",
    "Max Potion",
    "Hyper Potion",
    "Super Potion",
    "Potion",
    "BoulderBadge",
    "CascadeBadge",
    "ThunderBadge",
    "RainbowBadge",
    "SoulBadge",
    "MarshBadge",
    "VolcanoBadge",
    "EarthBadge",
    "Escape Rope",
    "Repel",
    "Old Amber",
    "Fire Stone",
    "Thunderstone",
    "Water Stone",
    "HP Up",
    "Protein",
    "Iron",
    "Carbos",
    "Calcium",
    "Rare Candy",
    "Dome Fossil",
    "Helix Fossil",
    "Secret Key",
    "?????",
    "Bike Voucher",
    "X Accuracy",
    "Leaf Stone",
    "Card Key",
    "Nugget",
    "PP Up*",
    "Poké Doll",
    "Full Heal",
    "Revive",
    "Max Revive",
    "Guard Spec.",
    "Super Repel",
    "Max Repel",
    "Dire Hit",
    "Coin",
    "Fresh Water",
    "Soda Pop",
    "Lemonade",
    "S.S. Ticket",
    "Gold Teeth",
    "X Attack",
    "X Defend",
    "X Speed",
    "X Special",
    "Coin Case",
    "Oak's Parcel",
    "Itemfinder",
    "Silph Scope",
    "Poké Flute",
    "Lift Key",
    "Exp. All",
    "Old Rod",
    "Good Rod",
    "Super Rod",
    "PP Up",
    "Ether",
    "Max Ether",
    "Elixer",
    "Max Elixer",
    "HM01",
    "HM02",
    "HM03",
    "HM04",
    "HM05",
    "TM01",
    "TM02",
    "TM03",
    "TM04",
    "TM05",
    "TM06",
    "TM07",
    "TM08",
    "TM09",
    "TM10",
    "TM11",
    "TM12",
    "TM13",
    "TM14",
    "TM15",
    "TM16",
    "TM17",
    "TM18",
    "TM19",
    "TM20",
    "TM21",
    "TM22",
    "TM23",
    "TM24",
    "TM25",
    "TM26",
    "TM27",
    "TM28",
    "TM29",
    "TM30",
    "TM31",
    "TM32",
    "TM33",
    "TM34",
    "TM35",
    "TM36",
    "TM37",
    "TM38",
    "TM39",
    "TM40",
    "TM41",
    "TM42",
    "TM43",
    "TM44",
    "TM45",
    "TM46",
    "TM47",
    "TM48",
    "TM49",
    "TM50",
    "TM51",
    "TM52",
    "TM53",
    "TM54",
    "TM55",
]

GEN_1_MOVES = [
    "", # Index 0 is no move learnt
    "Pound",
    "Karate Chop",
    "Double Slap",
    "Comet Punch",
    "Mega Punch",
    "Pay Day",
    "Fire Punch",
    "Ice Punch",
    "Thunder Punch",
    "Scratch",
    "Vise Grip",
    "Guillotine",
    "Razor Wind",
    "Swords Dance",
    "Cut",
    "Gust",
    "Wing Attack",
    "Whirlwind",
    "Fly",
    "Bind",
    "Slam",
    "Vine Whip",
    "Stomp",
    "Double Kick",
    "Mega Kick",
    "Jump Kick",
    "Rolling Kick",
    "Sand Attack",
    "Headbutt",
    "Horn Attack",
    "Fury Attack",
    "Horn Drill",
    "Tackle",
    "Body Slam",
    "Wrap",
    "Take Down",
    "Thrash",
    "Double-Edge",
    "Tail Whip",
    "Poison Sting",
    "Twineedle",
    "Pin Missile",
    "Leer",
    "Bite",
    "Growl",
    "Roar",
    "Sing",
    "Supersonic",
    "Sonic Boom",
    "Disable",
    "Acid",
    "Ember",
    "Flamethrower",
    "Mist",
    "Water Gun",
    "Hydro Pump",
    "Surf",
    "Ice Beam",
    "Blizzard",
    "Psybeam",
    "Bubble Beam",
    "Aurora Beam",
    "Hyper Beam",
    "Peck",
    "Drill Peck",
    "Submission",
    "Low Kick",
    "Counter",
    "Seismic Toss",
    "Strength",
    "Absorb",
    "Mega Drain",
    "Leech Seed",
    "Growth",
    "Razor Leaf",
    "Solar Beam",
    "Poison Powder",
    "Stun Spore",
    "Sleep Powder",
    "Petal Dance",
    "String Shot",
    "Dragon Rage",
    "Fire Spin",
    "Thunder Shock",
    "Thunderbolt",
    "Thunder Wave",
    "Thunder",
    "Rock Throw",
    "Earthquake",
    "Fissure",
    "Dig",
    "Toxic",
    "Confusion",
    "Psychic",
    "Hypnosis",
    "Meditate",
    "Agility",
    "Quick Attack",
    "Rage",
    "Teleport",
    "Night Shade",
    "Mimic",
    "Screech",
    "Double Team",
    "Recover",
    "Harden",
    "Minimize",
    "Smokescreen",
    "Confuse Ray",
    "Withdraw",
    "Defense Curl",
    "Barrier",
    "Light Screen",
    "Haze",
    "Reflect",
    "Focus Energy",
    "Bide",
    "Metronome",
    "Mirror Move",
    "Self-Destruct",
    "Egg Bomb",
    "Lick",
    "Smog",
    "Sludge",
    "Bone Club",
    "Fire Blast",
    "Waterfall",
    "Clamp",
    "Swift",
    "Skull Bash",
    "Spike Cannon",
    "Constrict",
    "Amnesia",
    "Kinesis",
    "Soft-Boiled",
    "High Jump Kick",
    "Glare",
    "Dream Eater",
    "Poison Gas",
    "Barrage",
    "Leech Life",
    "Lovely Kiss",
    "Sky Attack",
    "Transform",
    "Bubble",
    "Dizzy Punch",
    "Spore",
    "Flash",
    "Psywave",
    "Splash",
    "Acid Armor",
    "Crabhammer",
    "Explosion",
    "Fury Swipes",
    "Bonemerang",
    "Rest",
    "Rock Slide",
    "Hyper Fang",
    "Sharpen",
    "Conversion",
    "Tri Attack",
    "Super Fang",
    "Slash",
    "Substitute",
    "Struggle",
]