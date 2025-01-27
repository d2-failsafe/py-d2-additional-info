from enum import Enum
from typing import List, Optional

from pydantic import BaseModel

from data.generated_enums import ItemCategoryHashes


class ActivityModeHash(int, Enum):
    智谋 = 1848252830
    打击 = 2394616003
    日落 = 3789021730
    熔炉竞技场 = 1164760504
    mayhem = 1264443021
    control = 3199098480
    breakthrough = 4033000329
    countdown = 1505888634
    elimination = 4078439804
    doubles = 3821502017
    supremacy = 910991990
    rumble = 157639802
    survival = 2239249083
    ironBanner = 1826469369
    dungeon = 608898761
    nightmareHunt = 332181804
    剧情 = 1686739444
    trials = 1673724806
    explore = 3497767639


class DestinationHash(int, Enum):
    EDZ = 697502628
    Nessus = 3607432451
    TangledShore = 3821439926
    DreamingCity = 1416096592
    Moon = 677774031
    Europa = 1729879943
    Cosmodrome = 3990611421


class DamageHash(int, Enum):
    Solar = 1847026933
    Arc = 2303181850
    Kinetic = 3373582085
    Void = 3454344768
    Stasis = 151347233


class KillType(int, Enum):
    Melee = 0
    Super = 1
    Grenade = 2
    Finisher = 3
    Precision = 4
    ClassAbilities = 5


class VendorHash(int, Enum):
    Petra = 1841717884


class BountyMetadata(BaseModel):
    ActivityMode: Optional[List[int]]
    Destination: Optional[List[int]]
    DamageType: Optional[List[int]]
    ItemCategory: Optional[List[int]]
    KillType: Optional[List[KillType]]


class matchTableModel(BaseModel):
    assign: BountyMetadata
    name: Optional[List[str]]
    desc: Optional[List[str]]
    obj: Optional[List[str]]
    type: Optional[List[str]]
    label: Optional[List[str]]
    vendorHashes: Optional[List[int]]


matchTableRaw = [
    # ActivityMode
    {
        "assign": {"ActivityMode": [ActivityModeHash.智谋]},
        "desc": ["gambit#i", "The Drifter"],
        "type": ["gambit#i"],
        "label": ["gambit"],
    },
    {
        "assign": {"ActivityMode": [ActivityModeHash.打击]},
        "desc": ["(?<!(?<!vanguard or )nightfall )strike#i"],
    },
    {"assign": {"ActivityMode": [ActivityModeHash.日落]}, "desc": ["nightfall#i"]},
    {
        "assign": {"ActivityMode": [ActivityModeHash.熔炉竞技场]},
        "desc": ["crucible(?! matches in)#i"],
        "type": ["crucible#i"],
        "label": ["bounties.crucible"],
    },
    # TODO: Roll up all crucible types into just crucible?
    {"assign": {"ActivityMode": [ActivityModeHash.control]}, "desc": ["Control"]},
    {"assign": {"ActivityMode": [ActivityModeHash.mayhem]}, "desc": ["Mayhem"]},
    {
        "assign": {"ActivityMode": [ActivityModeHash.breakthrough]},
        "desc": ["Breakthrough"],
    },
    {"assign": {"ActivityMode": [ActivityModeHash.doubles]}, "desc": ["Doubles"]},
    {"assign": {"ActivityMode": [ActivityModeHash.supremacy]}, "desc": ["Supremacy"]},
    {"assign": {"ActivityMode": [ActivityModeHash.countdown]}, "desc": ["Countdown"]},
    {
        "assign": {"ActivityMode": [ActivityModeHash.elimination]},
        "desc": ["Elimination"],
    },
    {"assign": {"ActivityMode": [ActivityModeHash.rumble]}, "desc": ["Rumble"]},
    {"assign": {"ActivityMode": [ActivityModeHash.survival]}, "desc": ["Survival"]},
    {
        "assign": {"ActivityMode": [ActivityModeHash.ironBanner]},
        "desc": ["iron banner#i"],
        "type": ["iron banner#i"],
        "label": ["bounties.iron_banner"],
    },
    {"assign": {"ActivityMode": [ActivityModeHash.dungeon]}, "desc": ["dungeon#i"]},
    {
        "assign": {"ActivityMode": [ActivityModeHash.nightmareHunt]},
        "desc": ["Nightmare Hunt"],
    },
    {"assign": {"ActivityMode": [ActivityModeHash.剧情]}, "desc": ["story mission"]},
    {
        "assign": {"ActivityMode": [ActivityModeHash.trials]},
        "desc": ["Trials of Osiris#i"],
        "type": ["Trials Bounty"],
        "label": ["trials.bounties"],
    },
    {"assign": {"ActivityMode": [ActivityModeHash.explore]}, "name": ["WANTED:"]},
    # Destinations
    {
        "assign": {"Destination": [DestinationHash.EDZ]},
        "desc": ["EDZ", "European Dead Zone", "Devrim Kay"],
        "label": ["bounties.destinations.edz"],
    },
    {
        "assign": {"Destination": [DestinationHash.Nessus]},
        "desc": ["Nessus", "Failsafe"],
        "label": ["bounties.destinations.myriad"],
    },
    {
        "assign": {"Destination": [DestinationHash.TangledShore]},
        "desc": ["Tangled Shore", "Jetsam of Saturn", "The Spider"],
    },
    {
        "assign": {"Destination": [DestinationHash.DreamingCity]},
        "desc": ["Dreaming City", "Oracle Engine", "plague.+well#i", "Petra Venj"],
        "obj": ["Ascendant Challenge#i", "Baryon Boughs"],
        "vendorHashes": [VendorHash.Petra],
    },
    {
        "assign": {"Destination": [DestinationHash.Moon]},
        "desc": ["Moon(?! grant no progress)", "Lectern of Enchantment", "Sanctuary"],
        "type": ["Moon Bounty"],
    },
    {
        "assign": {"Destination": [DestinationHash.Europa]},
        "desc": [
            "Europa",
            "Charon",
            "Cadmus Ridge",
            "Asterion Abyss",
            "Riis-Reborn",
            "Empire Hunt",
        ],
        "type": ["Europa Bounty"],
    },
    {
        "assign": {"Destination": [DestinationHash.Cosmodrome]},
        "desc": ["Cosmodrome"],
        "label": ["cosmodrome.bounties"],
    },
    # # enemyType
    # { "assign": { enemyType: 'Taken',                                         }, "desc": ["\btaken\b"],                                                        },
    # { "assign": { enemyType: 'Cabal',                                         }, "desc": ["\bcabal\b"],                                                        },
    # { "assign": { enemyType: 'Fallen',                                        }, "desc": ["\bfallen\b"],                                                       },
    # { "assign": { enemyType: 'Scorn',                                         }, "desc": ["\bscorn\b"],                                                        },
    # { "assign": { enemyType: 'Vex',                                           }, "desc": ["\bvex\b"],                                                          },
    # { "assign": { enemyType: 'Hive',                                          }, "desc": ["\bhive\b"],                                                         },
    # { "assign": { enemyType: 'Guardians',                                     }, "desc": ['guardians are worth',
    #                                                                                 "(defeat|opposing|enemy|other) guardians"],   },
    # { "assign": { enemyType: 'Minibosses',                                    }, "desc": ['minibosses'],                                                       },
    # { "assign": { enemyType: 'Bosses',                                        }, "desc": ["(?<!mini)bosses"],                                                  },
    # { "assign": { enemyType: 'HVT',                                           }, "desc": ['high-value targets'],                                               },
    {
        "assign": {
            "DamageType": [DamageHash.Solar],
        },
        "desc": ["Solar"],
        "obj": [r"\[Solar\]", "Solar damage"],
    },
    {
        "assign": {
            "DamageType": [DamageHash.Arc],
        },
        "desc": ["Arc"],
        "obj": [r"\[Arc\]", "Arc damage"],
    },
    {
        "assign": {
            "DamageType": [DamageHash.Void],
        },
        "desc": ["Void"],
        "obj": [r"\[Void\]", "Void damage"],
    },
    {
        "assign": {
            "DamageType": [DamageHash.Kinetic],
        },
        "desc": ["Kinetic"],
    },
    {
        "assign": {
            "DamageType": [DamageHash.Arc, DamageHash.Solar, DamageHash.Void],
        },
        "desc": ["Energy(?! weapons deal elemental damage)"],
    },
    {
        "assign": {
            "DamageType": [DamageHash.Stasis],
        },
        "desc": ["Stasis"],
        "obj": [
            r"\[Stasis\]",
            "(Stasis|Shatter) damage",
            "Stasis( Super)? final blows",
            "slowed#i",
            "frozen#i",
        ],
    },
    # Item Category
    {
        "assign": {"ItemCategory": [ItemCategoryHashes.自动步枪]},
        "desc": ["Auto Rifle"],
        "obj": ["Auto Rifle"],
    },
    {
        "assign": {"ItemCategory": [ItemCategoryHashes.弓箭]},
        "desc": ["Bow"],
        "obj": ["Bow"],
    },
    {
        "assign": {"ItemCategory": [ItemCategoryHashes.融合步枪]},
        "desc": ["(?<!Linear )Fusion Rifle"],
        "obj": [r"\[Fusion Rifle\]"],
    },
    {
        "assign": {"ItemCategory": [ItemCategoryHashes.榴弹发射器]},
        "desc": [
            "(?<!breechloaded|n-Heavy ammo|ic or Energy)(a(ny)?|with|Heavy|Power)? Grenade Launcher(s)?(?!(s)? that use Special ammo)",
        ],
        "obj": ["Grenade Launcher Multikills", r"\[Grenade Launcher\]"],
    },
    {
        "assign": {"ItemCategory": [-ItemCategoryHashes.榴弹发射器]},
        "desc": [
            "(?<!Heavy|Power)(breechloaded|non-Heavy ammo|Kinetic or Energy|a(ny)?|with)? Grenade Launcher(s)?(?!(s)? that use Heavy ammo)",
        ],
        "obj": [r"\[Special Grenade Launcher\]"],
    },
    {
        "assign": {"ItemCategory": [ItemCategoryHashes.手炮]},
        "desc": ["Hand Cannon"],
        "obj": ["Hand Cannon"],
    },
    {
        "assign": {"ItemCategory": [ItemCategoryHashes.线性融合步枪]},
        "desc": ["Linear Fusion Rifle"],
        "obj": ["Linear Fusion Rifle"],
    },
    {
        "assign": {"ItemCategory": [ItemCategoryHashes.机枪]},
        "desc": ["Machine Gun"],
        "obj": ["Machine Gun"],
    },
    {
        "assign": {"ItemCategory": [ItemCategoryHashes.脉冲步枪]},
        "desc": ["Pulse Rifle"],
        "obj": ["Pulse Rifle"],
    },
    {
        "assign": {"ItemCategory": [ItemCategoryHashes.火箭发射器]},
        "desc": ["Rocket Launcher"],
        "obj": ["Rocket Launcher"],
    },
    {
        "assign": {"ItemCategory": [ItemCategoryHashes.微型冲锋枪]},
        "desc": [r"\[SMG\]", "Submachine Gun"],
        "obj": [r"\[SMG\]"],
    },
    {
        "assign": {"ItemCategory": [ItemCategoryHashes.斥候步枪]},
        "desc": ["Scout Rifle"],
        "obj": ["Scout Rifle"],
    },
    {
        "assign": {"ItemCategory": [ItemCategoryHashes.霰弹枪]},
        "desc": ["Shotgun"],
        "obj": ["Shotgun"],
    },
    {
        "assign": {"ItemCategory": [ItemCategoryHashes.手枪]},
        "desc": ["Sidearm"],
        "obj": ["Sidearm"],
    },
    {
        "assign": {"ItemCategory": [ItemCategoryHashes.狙击步枪]},
        "desc": ["Sniper Rifle"],
        "obj": ["Sniper Rifle"],
    },
    {
        "assign": {"ItemCategory": [ItemCategoryHashes.刀剑]},
        "desc": ["Sword"],
        "obj": ["Sword"],
    },
    {
        "assign": {"ItemCategory": [ItemCategoryHashes.追踪步枪]},
        "desc": ["Trace Rifle"],
        "obj": ["Trace Rifle"],
    },
    # Kill Type
    {
        "assign": {"KillType": [KillType.Super]},
        "desc": ["(?<!Cast your )Super"],
        "obj": ["(?<!Cast your )Super"],
    },
    {
        "assign": {"KillType": [KillType.Finisher]},
        "desc": ["finisher#i"],
        "obj": ["finisher#i"],
    },
    {
        "assign": {"KillType": [KillType.Grenade]},
        "desc": ["grenade(?! launcher)#i"],
        "obj": ["grenade(?! launcher)#i"],
    },
    {"assign": {"KillType": [KillType.Melee]}, "desc": ["melee#i"], "obj": ["melee#i"]},
    {
        "assign": {"KillType": [KillType.Precision]},
        "desc": ["precision#i"],
        "obj": ["precision#i"],
    },
    {
        "assign": {"KillType": [KillType.ClassAbilities]},
        "desc": ["class abilities#i"],
        "obj": ["class abilities#i"],
    },
]

matchTable: List[matchTableModel] = [matchTableModel.parse_obj(i) for i in matchTableRaw]
