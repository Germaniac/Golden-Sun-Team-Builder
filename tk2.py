import tkinter as tk
from decimal import Decimal

root=tk.Tk()
root.title('Golden Sun Team Builder')
root.iconbitmap('icon.ico')
color=root.cget('bg')

venus=tk.PhotoImage(file='venus.gif')
mars=tk.PhotoImage(file='mars.gif')
jupiter=tk.PhotoImage(file='jupiter.gif')
mercury=tk.PhotoImage(file='mercury.gif')
none=tk.PhotoImage(file='none.gif')

range1=tk.PhotoImage(file='1.gif')
range3=tk.PhotoImage(file='3.gif')
range5=tk.PhotoImage(file='5.gif')
range7=tk.PhotoImage(file='7.gif')
rangeall=tk.PhotoImage(file='all.gif')

names=['Isaac','Garet','Ivan','Mia','Felix','Jenna','Sheba','Piers']
stats=[[790,250,388,166,396,3],
       [830,238,373,179,349,2],
       [719,288,344,155,419,4],
       [751,280,359,163,369,5],
       [810,244,392,168,382,2],
       [770,265,366,165,392,4],
       [735,284,351,159,407,5],
       [798,248,370,173,359,3]]
boosts={'None':[1.0,1.0,1.0,1.0,1.0,1.0],
        'Slayer':[1.9,1.2,1.5,1.4,1.5,1.0],
        'Hero':[1.9,1.2,1.4,1.5,1.1,1.0],
        'Sorcerer':[1.5,1.8,1.2,1.3,1.7,1.1],
        'Angel':[1.6,1.7,1.3,1.4,1.2,1.3],
        'Justice':[1.7,1.6,1.4,1.4,1.6,0.9],
        'Admiral':[1.9,1.3,1.4,1.4,1.3,1.2],
        'Chaos Lord':[2.0,1.2,1.7,1.4,1.6,0.7],
        'Wizard':[1.7,1.9,1.3,1.4,1.8,1.2],
        'War Adept (Venus)':[1.9,1.7,1.5,1.4,1.7,0.9],
        'Conjurer (Venus)':[1.7,1.6,1.4,1.3,1.6,0.9],
        'War Adept (Mars)':[1.9,1.7,1.5,1.4,1.7,0.9],
        'Conjurer (Mars)':[1.7,1.6,1.4,1.3,1.6,0.9],
        'Protector':[1.9,1.4,1.5,1.5,1.4,1.2],
        'Guardian':[1.7,1.3,1.4,1.4,1.3,1.2],
        'Radiant':[1.9,1.4,1.5,1.5,1.4,1.2],
        'Luminier':[1.7,1.3,1.4,1.4,1.3,1.2],
        'Oracle (Jupiter)':[1.7,1.8,1.4,1.4,1.6,1.0],
        'Druid (Jupiter)':[1.5,1.7,1.3,1.3,1.5,1.0],
        'Oracle (Mercury)':[1.7,1.8,1.4,1.4,1.6,1.0],
        'Druid (Mercury)':[1.5,1.7,1.3,1.3,1.5,1.0],
        'Guru (Jupiter)':[1.7,1.7,1.4,1.5,1.7,1.2],
        'Fire Monk':[1.5,1.6,1.3,1.4,1.6,1.2],
        'Guru (Mercury)':[1.7,1.7,1.4,1.5,1.7,1.2],
        'Water Monk':[1.5,1.6,1.3,1.4,1.6,1.2],
        'Master':[2.0,1.6,1.7,1.4,1.9,0.8],
        'Ninja (Venus)':[1.6,1.4,1.5,1.2,1.7,0.8],
        'Ninja (Mars)':[1.6,1.4,1.5,1.2,1.7,0.8],
        'Ronin':[2.1,1.4,1.6,1.5,1.5,0.9],
        'Dark Mage':[1.7,1.9,1.4,1.4,1.7,0.9],
        'Medium (Jupiter)':[1.3,1.7,1.2,1.2,1.5,0.9],
        'Medium (Mercury)':[1.3,1.7,1.2,1.2,1.5,0.9],
        'Pure Mage':[1.7,1.9,1.4,1.4,1.6,1.3],
        'Warlock':[1.7,1.8,1.4,1.4,1.8,1.2],
        'Ranger (Jupiter)':[1.3,1.6,1.2,1.2,1.6,1.2],
        'Ranger (Mercury)':[1.3,1.6,1.2,1.2,1.6,1.2],
        'Paladin':[2.0,1.5,1.6,1.6,1.3,1.3],
        'Dragoon (Venus)':[1.6,1.3,1.4,1.4,1.1,1.3],
        'Dragoon (Mars)':[1.6,1.3,1.4,1.4,1.1,1.3],
        'Acrobat':[1.9,1.2,1.4,1.4,1.6,1.2],
        'Beast Lord':[1.9,1.1,1.5,1.5,1.2,0.8],
        'Necromage':[1.6,1.9,1.3,1.3,1.7,0.9]}
djinn=[{'Chaos Lord':[2,7,0,0],
        'Protector':[2,0,0,7],
        'War Adept (Venus)':[2,0,7,0],
        'Druid (Mercury)':[1,0,0,7],
        'Druid (Jupiter)':[1,0,7,0],
        'Paladin':[0,4,0,5],
        'Master':[0,4,5,0],
        'Ronin':[0,5,4,0],
        'Medium (Mercury)':[0,0,3,6],
        'Medium (Jupiter)':[0,0,6,3],
        'Acrobat':[0,3,3,3],
        'Beast Lord':[0,3,3,3],
        'Necromage':[0,3,3,3]},
       {'Chaos Lord':[7,2,0,0],
        'War Adept (Mars)':[0,2,7,0],
        'Radiant':[0,2,0,7],
        'Fire Monk':[0,1,7,0],
        'Water Monk':[0,1,0,7],
        'Master':[4,0,5,0],
        'Paladin':[4,0,0,5],
        'Ronin':[5,0,4,0],
        'Ranger (Jupiter)':[0,0,6,3],
        'Ranger (Mercury)':[0,0,3,6],
        'Acrobat':[3,0,3,3],
        'Beast Lord':[3,0,3,3],
        'Necromage':[3,0,3,3]},
       {'Wizard':[0,0,2,7],
        'Guru (Jupiter)':[0,7,2,0],
        'Oracle (Jupiter)':[7,0,2,0],
        'Conjurer (Mars)':[0,7,1,0],
        'Conjurer (Venus)':[7,0,1,0],
        'Warlock':[0,5,0,4],
        'Dark Mage':[5,0,0,4],
        'Pure Mage':[4,0,0,5],
        'Ninja (Mars)':[3,6,0,0],
        'Ninja (Venus)':[6,3,0,0],
        'Acrobat':[3,3,0,3],
        'Beast Lord':[3,3,0,3],
        'Necromage':[3,3,0,3]},
       {'Wizard':[0,0,7,2],
        'Oracle (Mercury)':[7,0,0,2],
        'Guru (Mercury)':[0,7,0,2],
        'Guardian':[7,0,0,1],
        'Luminier':[0,7,0,1],
        'Dark Mage':[5,0,4,0],
        'Warlock':[0,5,4,0],
        'Pure Mage':[4,0,5,0],
        'Dragoon (Venus)':[6,3,0,0],
        'Dragoon (Mars)':[3,6,0,0],
        'Acrobat':[3,3,3,0],
        'Beast Lord':[3,3,3,0],
        'Necromage':[3,3,3,0]},
       {'None':[0,0,0,0],
        'Slayer':[8,0,0,0],
        'Hero':[0,8,0,0],
        'Sorcerer':[0,0,8,0],
        'Angel':[0,0,0,8],
        'Justice':[0,8,0,0],
        'Admiral':[0,0,0,8]}]
mono=['Slayer',
      'Hero',
      'Sorcerer',
      'Angel',
      'Slayer',
      'Justice',
      'Sorcerer',
      'Admiral',
      'None']
psynergy={'Quake':[venus,range3,4,'Attack with a powerful quake','Deals 12 base damage'],
          'Earthquake':[venus,range5,7,'Attack with a mighty tremor','Deals 35 base damage'],
          'Quake Sphere':[venus,range7,15,'Attack with a massive quake','Deals 65 base damage'],
          'Growth':[venus,range1,4,'Attack with wild plants','Deals 25 base damage\nCan be used out of battle to turn saplings into vines'],
          'Mad Growth':[venus,range3,10,'Attack with ferocious plants','Deals 60 base damage'],
          'Wild Growth':[venus,range5,19,'Attack with giant plants','Deals 110 base damage'],
          'Rockfall':[venus,range3,5,'Attack with a blast of rocks','Deals 30 base damage'],
          'Rockslide':[venus,range5,15,'Attack with a blast of rocks','Deals 90 base damage'],
          'Avalanche':[venus,range5,30,'Attack with a blast of rocks','Deals 160 base damage'],
          'Thorn':[venus,range3,6,'Attack with stabbing thorns','Deals 35 base damage'],
          'Briar':[venus,range3,11,'Attack with sharpened briars','Deals 70 base damage'],
          'Nettle':[venus,range5,23,'Attack with stinging nettles','Deals 140 base damage'],
          'Spire':[venus,range1,5,'Attack with an earthen spire','Deals 40 base damage'],
          'Clay Spire':[venus,range3,13,'Attack with an earthen spire','Deals 85 base damage'],
          'Stone Spire':[venus,range3,22,'Attack with an earthen spire','Deals 160 base damage'],
          'Gaia':[venus,range3,7,'Attack with the earth\'s might','Deals 40 base damage'],
          'Mother Gaia':[venus,range5,17,'Attack with the earth\'s might','Deals 100 base damage'],
          'Grand Gaia':[venus,range5,32,'Attack with the earth\'s might','Deals 200 base damage'],
          'Punji':[venus,range3,7,'Attack with a bamboo weapon','Deals 45 base damage'],
          'Punji Trap':[venus,range3,13,'Attack with a bamboo weapon','Deals 85 base damage'],
          'Punji Strike':[venus,range5,24,'Attack with a bamboo weapon','Deals 150 base damage'],
          'Demon Night':[venus,range3,12,'Unleash a myriad of monsters','Deals 60 base damage'],
          'Thorny Grave':[venus,range3,24,'Summon a loathsome fiend','Deals 170 base damage'],
          'Bramble Card':[venus,range3,22,'Throw a card of the Thorn suit','Deals 130 base damage'],
          'Helm Splitter':[venus,range1,8,'Paralyze a foe with a mighty blow','Attack +30 Venus-based damage\nMay instantly fell the enemy'],
          'Skull Splitter':[venus,range1,8,'Annihilate a foe by crushing the skull','Attack +30 Venus-based damage\nMay instantly fell the enemy'],
          'Ragnarok':[venus,range1,7,'Strike with a massive sword','Attack +35 Venus-based damage'],
          'Odyssey':[venus,range1,18,'Pierce a foe with a colossal sword','Attack +95 Venus-based damage'],
          'Dinox':[venus,range1,3,'Attack with sharpened fangs','Attack +40 Venus-based damage'],
          'Troll':[venus,range1,3,'Attack with fiendish might','Attack +45 Venus-based damage'],
          'Minotaur':[venus,range1,10,'Attack with a mighty axe','Attack +90 Venus-based damage'],
          'Living Armor':[venus,range1,17,'Attack with a big axe','Attack +130 Venus-based damage'],
          'Grand Golem':[venus,range1,22,'Attack with a fist of stone','Attack +150 Venus-based damage'],
          'Sabre Dance':[venus,range1,7,'Attack with dancing blades','Attack x1.5 Venus-based damage'],
          'Annihilation':[venus,range1,18,'Attempt to annihilate a foe','Attack x1.5 Venus-based damage\nMay instantly fell the enemy'],
          'Call Demon':[venus,range1,13,'Strike with a demon\'s fury','Attack x1.9 Venus-based damage\nMay reduce the enemy\'s HP to 1'],
          'Cure':[venus,range1,3,'Restore 70 HP','Restores 70 base HP\nCan be used outside of battle'],
          'Cure Well':[venus,range1,7,'Restore 150 HP','Restores 150 base HP\nCan be used outside of battle'],
          'Potent Cure':[venus,range1,16,'Restore 300 HP','Restores 300 base HP\nCan be used outside of battle'],
          'Revive':[venus,range1,15,'Revive a downed ally','Restores a downed Adept to full HP\nCan be used outside of battle'],
          'Lich':[venus,range1,10,'Revive an ally with the undead\'s aid','Restores a downed Adept to full HP'],
          'Haunt':[venus,range3,5,'Haunt a foe with an evil spirit','May inflict the enemy with the haunt status effect'],
          'Curse':[venus,range1,6,'Draw the Spirit of Death to a foe','May inflict the enemy with the death curse status effect'],
          'Condemn':[venus,range1,8,'Disable your enemy with evil power','May instantly fell the enemy'],
          'Death Card':[venus,range1,8,'Call the Reaper to claim your foes','May instantly fell the enemy'],
          'Fear Puppet':[venus,range3,7,'Paralyze your foes with fear','May stun the enemy'],
          'Catch':[venus,None,1,'Grab light objects from afar','Used outside of battle to pick up certain items remotely, usually off trees'],
          'Carry':[venus,None,2,'Lift and move light objects','Used outside of battle to levitate certain blocks and drop them into an adjacent space'],
          'Scoop':[venus,None,1,'Dig in soft ground','Used outside of battle to dig in sand, revealing buried objects'],
          'Tremor':[venus,None,1,'Shake objects left and right','Used outside of battle to shake certain objects, knocking items out of them'],
          'Grind':[venus,None,2,'Pulverise large objects','Used outside of battle to destroy certain obstacles'],
          'Sand':[venus,None,2,'Melt into sand','Used outside of battle to turn the party into sand, allowing greater mobility in dungeons'],
          'Retreat':[venus,None,6,'Return to the dungeon\'s entrance','Used outside of battle, within dungeons, to instantly return to the last entrance used'],
          'Flare':[mars,range3,4,'Attack with flaring flames','Deals 15 base damage'],
          'Flare Wall':[mars,range3,7,'Attack with searing flames','Deals 40 base damage'],
          'Flare Storm':[mars,range3,12,'Attack with incinerating flames','Deals 80 base damage'],
          'Blast':[mars,range3,5,'Attack with an explosive blast','Deals 25 base damage'],
          'Mad Blast':[mars,range3,9,'Attack with an explosive blast','Deals 50 base damage'],
          'Fiery Blast':[mars,range5,19,'Attack with an explosive blast','Deals 110 base damage'],
          'Fire Bomb':[mars,range3,5,'Attack with a bomb blast','Deals 35 base damage'],
          'Cluster Bomb':[mars,range5,11,'Attack with a bomb blast','Deals 65 base damage'],
          'Carpet Bomb':[mars,range7,29,'Attack with a bomb blast','Deals 130 base damage'],
          'Fire':[mars,range3,6,'Attack with a scorching fireball','Deals 35 base damage'],
          'Fireball':[mars,range5,12,'Attack with a scorching fireball','Deals 65 base damage'],
          'Inferno':[mars,range5,23,'Attack with a scorching fireball','Deals 140 base damage'],
          'Lava Shower':[mars,range1,4,'Attack with a volcano\'s might','Deals 40 base damage'],
          'Molten Bath':[mars,range3,12,'Attack with a volcano\'s might','Deals 70 base damage'],
          'Magma Storm':[mars,range5,27,'Attack with a volcano\'s might','Deals 120 base damage'],
          'Blast':[mars,range3,7,'Attack with a massive explosion','Deals 40 base damage'],
          'Nova':[mars,range5,13,'Attack with a massive explosion','Deals 70 base damage'],
          'Supernova':[mars,range7,31,'Attack with a massive explosion','Deals 150 base damage'],
          'Juggle':[mars,range3,7,'Skillfully toss balls of flame','Deals 40 base damage'],
          'Heat Juggle':[mars,range5,13,'Skillfully toss balls of flame','Deals 75 base damage'],
          'Fiery Juggle':[mars,range5,25,'Skillfully toss balls of flame','Deals 150 base damage'],
          'Salamander':[mars,range3,7,'Call forth a fiery reptile\'s breath','Deals 45 base damage\nDeals less damage to secondary targets than normal'],
          'Cerberus':[mars,range3,7,'Attack with the soul\'s fire','Deals 50 base damage\nDeals less damage to secondary targets than normal'],
          'Chimera':[mars,range3,7,'Attack a foe with a fiery blast','Deals 55 base damage\nDeals less damage to secondary targets than normal'],
          'Macetail':[mars,range3,7,'Attack foes with a fiery blast','Deals 70 base damage\nDeals less damage to secondary targets than normal'],
          'Beam':[mars,range3,7,'Attack with a searing heat beam','Deals 45 base damage',],
          'Cycle Beam':[mars,range5,14,'Attack with a searing heat beam','Deals 80 base damage',],
          'Searing Beam':[mars,range7,36,'Attack with a searing heat beam','Deals 170 base damage',],
          'Volcano':[mars,range1,6,'Attack with volcanic might','Deals 45 base damage'],
          'Eruption':[mars,range3,14,'Attack with volcanic might','Deals 90 base damage'],
          'Pyroclasm':[mars,range5,29,'Attack with volcanic might','Deals 180 base damage'],
          'Raging Heat':[mars,range3,9,'Call forth the fires of the pit','Deals 45 base damage'],
          'Fiery Abyss':[mars,range5,18,'Call forth the fires of the pit','Deals 90 base damage'],
          'Dire Inferno':[mars,range7,32,'Call forth the fires of the pit','Deals 200 base damage'],
          'Fume':[mars,range1,6,'Attack with a plume of flames','Deals 50 base damage'],
          'Serpent Fume':[mars,range1,14,'Attack with a plume of flames','Deals 130 base damage'],
          'Dragon Fume':[mars,range1,35,'Attack with a plume of flames','Deals 230 base damage'],
          'Flame Card':[mars,range3,11,'Throw a card of the flame suit','Deals 60 base damage'],
          'Dragon Cloud':[mars,range1,6,'Strike an enemy with dragon cloud','Deals 80 base damage'],
          'Epicenter':[mars,range1,33,'Strike an enemy with dragon cloud','Deals 210 base damage'],
          'Fire Breath':[mars,range3,13,'Attack with a sheet of flames','Deals 85 base damage\nDoes less damage to secondary targets than usual'],
          'Wyvern':[mars,range3,17,'Attack foes with fiery breath','Deals 120 base damage\nDoes less damage to secondary targets than usual'],
          'Fire Dragon':[mars,range3,17,'Attack foes with a fiery blast','Deals 140 base damage\nDoes less damage to secondary targets than usual'],
          'Heat Wave':[mars,range1,6,'Attack with fiery bolts','Attack +33 Mars-based damage'],
          'Liquifier':[mars,range1,17,'Sieze and enemy with the fires of truth','Attack +90 Mars-based damage'],
          'Planet Diver':[mars,range1,7,'Leap skyward and lunge onto a foe','Attack +36 Mars-based damage'],
          'Planetary':[mars,range1,19,'Strike a foe with fire from the heaven','Attack +98 Mars-based damage'],
          'Aura':[mars,rangeall,7,'Restore 50 HP to the whole party','Restores 50 HP to the whole party\nCan be used outside of battle'],
          'Healing Aura':[mars,rangeall,11,'Restore 100 HP to the whole party','Restores 100 HP to the whole party\nCan be used outside of battle'],
          'Cool Aura':[mars,rangeall,16,'Restore 200 HP to the whole party','Restores 200 HP to the whole party\nCan be used outside of battle'],
          'Manticore':[mars,rangeall,18,'Restore 300HP with cleansing flame','Restores 300 HP to the whole party'],
          'Phoenix':[mars,range1,10,'Revive and ally with the phoenix\'s fire','Revives a downed Adept to full health'],
          'Sword Card':[mars,range1,6,'Reduce a foe\'s attack','May lower the enemy\'s attack by 25%'],
          'Impair':[mars,range1,4,'Drop enemy\'s Defense','May lower the enemy\'s defense by 25%'],
          'Debilitate':[mars,rangeall,4,'Drop enemy party\'s Defense','May lower the enemy\'s defense by 12.5%'],
          'Guard':[mars,range1,3,'Boost ally\'s Defense','Raises an ally\'s defense by 25%'],
          'Protect':[mars,rangeall,5,'Boost party\'s Defense','Raises the party\'s defense by 12.5%'],
          'Guardian':[mars,range1,3,'Boost Defense with divine might','Raises an ally\'s defense by 25%'],
          'Protector':[mars,rangeall,5,'Boost Defense with divine might','Raises the party\'s defense by 12.5%'],
          'Move':[mars,None,2,'Move an object on the ground','Used on certain objects to move them one space from up to one space away'],
          'Pound':[mars,None,2,'Drive objects into the ground','Used on certain pillars to flatten them'],
          'Burst':[mars,None,2,'Break cracked objects','Used on certain objects to make them explode'],
          'Blaze':[mars,None,1,'Manipulate flames','Used on fires to project them over a short distance'],
          'Gale':[jupiter,range3,3,'Attack with the wind\'s might','Deals 18 base damage\nCan be used out of battle to blow away green bushes'],
          'Typhoon':[jupiter,range5,13,'Attack with the wind\'s might','Deals 78 base damage'],
          'Hurricane':[jupiter,range5,25,'Attack with the wind\'s might','Deals 150 base damage'],
          'Bolt':[jupiter,range1,4,'Attack with a lightning bolt','Deals 20 base damage'],
          'Flash Bolt':[jupiter,range3,7,'Attack with a lightning bolt','Deals 40 base damage'],
          'Blue Bolt':[jupiter,range3,14,'Attack with a lightning bolt','Deals 90 base damage'],
          'Whirlwind':[jupiter,range3,5,'Attack with a swirling tornado','Deals 20 base damage\nCan be used out of battle to blow away green bushes'],
          'Tornado':[jupiter,range5,14,'Attack with a mighty tornado','Deals 80 base damage'],
          'Tempest':[jupiter,range5,27,'Attack with a fearsome windstorm','Deals 160 base damage'],
          'Slash':[jupiter,range1,4,'Attack with a blade of focused air','Deals 25 base damage'],
          'Wind Slash':[jupiter,range3,9,'Attack with a blade of focused air','Deals 50 base damage'],
          'Sonic Slash':[jupiter,range5,20,'Attack with a blade of focused air','Deals 120 base damage'],
          'Ray':[jupiter,range3,6,'Attack with a magnetic storm','Deals 35 base damage'],
          'Storm Ray':[jupiter,range3,10,'Attack with a magnetic storm','Deals 65 base damage'],
          'Destruct Ray':[jupiter,range3,21,'Attack with a magnetic storm','Deals 150 base damage'],
          'Plasma':[jupiter,range3,8,'Attack with a barrage of bolts','Deals 45 base damage'],
          'Shine Plasma':[jupiter,range5,18,'Attack with a barrage of bolts','Deals 100 base damage'],
          'Spark Plasma':[jupiter,range7,37,'Attack with a barrage of bolts','Deals 180 base damage'],
          'Thunderclap':[jupiter,range3,9,'Attack with the storm\'s fury','Deals 50 base damage'],
          'Thunderbolt':[jupiter,range5,19,'Attack with the storm\'s fury','Deals 110 base damage'],
          'Thunderstorm':[jupiter,range7,39,'Attack with the storm\'s fury','Deals 190 base damage'],
          'Drain':[jupiter,range1,3,'Drain enemy\'s HP into yourself','Deals 50 base damage'],
          'Psy Drain':[jupiter,range1,0,'Drain enemy\'s PP into yourself','Deals 15 base damage'],
          'Thunder Card':[jupiter,range3,17,'Throw a card of the Thunder suit','Deals 100 base damage'],
          'Poison Flow':[jupiter,range5,28,'Conjure a blast of poisoned wind','Deals 125 base damage\nMay inflict targets with venom'],
          'Shuriken':[jupiter,range3,8,'Attack with a huge throwing knife','Attack x0.8 Jupiter-based damage (all targets are hit for equal damage)'],
          'Astral Blast':[jupiter,range1,5,'Attack with celestial force','Attack +32 Jupiter-based damage'],
          'Thunder Mine':[jupiter,range1,16,'Attack with ball lightning','Attack +85 Jupiter-based damage'],
          'Backstab':[jupiter,range1,16,'Attack a foe from behind','Attack +35 Jupiter-based damage\nMay kill target in one hit'],
          'Death Plunge':[jupiter,range1,14,'Plunge your weapon into a foe','Attack +40 Jupiter-based damage\nMay stun the target'],
          'Death Leap':[jupiter,range1,22,'Beat a foe with a strange fan','Attack +110 Jupiter-based damage\nMay stun the target'],
          'Emu':[jupiter,range1,10,'Call a giant bird to claw a foe','Attack +75 Jupiter-based damage'],
          'Harpy':[jupiter,range1,10,'Attack with boosted morale','Attack +80 Jupiter-based damage'],
          'Gryphon':[jupiter,range1,10,'Attack with a razor-sharp beak''Attack +85 Jupiter-based damage'],
          'Ghost Soldier':[jupiter,range1,22,'Attack with phantom javelins','Attack +170 base damage\nMay ignore half of the target\'s defense'],
          'Whiplash':[jupiter,range1,6,'Attack with a whip','Attack x1.4 Jupiter-based damage'],
          'Quick Strike':[jupiter,range1,12,'Blind an enemy with a rapid strike','Attack x1.8 Jupiter-based damage'],
          'Call Dullahan':[jupiter,range1,21,'Strike with the dullahan\'s might','Attack x3 Jupiter-based damage'],
          'Impact':[jupiter,range1,7,'Boost ally\'s Attack','Raises target\'s attack by 25%'],
          'High Impact':[jupiter,rangeall,12,'Boost party\'s Attack','Raises targets\' attack by 12.5%'],
          'Demon Spear':[jupiter,range1,7,'Boost attack with a heavenly blade','Raises target\'s attack by 25%'],
          'Angel Spear':[jupiter,rangeall,12,'Boost attack with a heavenly blade','Raises targets\' attack by 12.5%'],
          'Ward':[jupiter,range1,3,'Boost Resistance','Raises target\'s resistance by 40'],
          'Resist':[jupiter,rangeall,5,'Boost Resistance','Raises targets\' resistance by 20'],
          'Magic Shell':[jupiter,range1,3,'Boost Elemental Resistance','Raises target\'s resistance by 40'],
          'Magic Shield':[jupiter,rangeall,5,'Boost Elemental Resistance','Raises targets\' resistance by 20'],
          'Dull':[jupiter,range1,6,'Drop enemy Attack','Lowers target\'s attack by 25%'],
          'Blunt':[jupiter,range3,11,'Drop enemy Attack','Lowers targets\' attack by 12.5%'],
          'Weaken':[jupiter,range1,4,'Drop enemy\'s Resistance','Lowers target\'s resistance by 40',],
          'Enfeeble':[jupiter,range3,6,'Drop enemy party\'s Resistance','Lowers targets\' resistance by 20',],
          'Sleep':[jupiter,range3,5,'Lull multiple foes to sleep','May put targets to sleep'],
          'Sleep Card':[jupiter,range3,5,'Put a foe to sleep','May put targets to sleep'],
          'Bind':[jupiter,range1,4,'Block a foe\'s Psynergy','May seal the target\'s Psynergy'],
          'Delude':[jupiter,range3,4,'Wrap multiple foes in Delusion','May delude the targets'],
          'Mist':[jupiter,range3,4,'Wrap a foe in a cloud of delusion','May delude the targets'],
          'Baffle Card':[jupiter,range3,4,'Envelop foes in an illusion','May delude the targets'],
          'Mind Read':[jupiter,None,1,'Read someone\'s mind','Used out of battle to read the minds of NPCs'],
          'Reveal':[jupiter,None,1,'Perceive hidden truths','Used out of battle to dispel mirages, see hidden doors, etc.'],
          'Halt':[jupiter,None,2,'Stop a moving object','Used out of battle to stop some moving objects\nUseless in The Lost Age'],
          'Lash':[jupiter,None,1,'Lift and move very light objects','Used out of battle to tie ropes'],
          'Cyclone':[jupiter,None,2,'Conjure wind to scatter weeds','Used out of battle to blow away weeds'],
          'Hover':[jupiter,None,2,'Hover in the air','Used out of battle on special panels to float in the air'],
          'Teleport':[jupiter,None,3,'Teleport at will','Used out of battle to teleport between special patterns or to previously visited towns'],
          'Frost':[mercury,range3,5,'Attack with frigid blasts','Deals 20 base damage\nCan be used out of battle to create ice pillars ice from puddles'],
          'Tundra':[mercury,range3,8,'Attack with frigid blasts','Deals 45 base damage'],
          'Glacier':[mercury,range3,15,'Attack with frigid blasts','Deals 100 base damage'],
          'Douse':[mercury,range3,5,'Attack with a surge of water','Deals 25 base damage\nCan be used out of battle to create localised rain'],
          'Drench':[mercury,range3,10,'Attack with a torrent of water','Deals 60 base damage'],
          'Deluge':[mercury,range5,20,'Attack with a deadly flood','Deals 120 base damage'],
          'Froth':[mercury,range3,5,'Attack with frothing bubbles','Deals 28 base damage'],
          'Froth Sphere':[mercury,range5,12,'Attack with frenzied bubbles','Deals 65 base damage'],
          'Froth Spiral':[mercury,range5,31,'Attack with a bubble vortex','Deals 150 base damage'],
          'Ice':[mercury,range1,5,'Attack with spikes of ice','Deals 35 base damage'],
          'Ice Horn':[mercury,range3,11,'Attack with spikes of ice','Deals 70 base damage'],
          'Ice Missile':[mercury,range3,23,'Attack with spikes of ice','Deals 160 base damage'],
          'Cool':[mercury,range3,6,'Attack with freezing cold','Deals 35 base damage'],
          'Supercool':[mercury,range5,14,'Attack with freezing cold','Deals 80 base damage'],
          'Megacool':[mercury,range7,33,'Attack with freezing cold','Deals 180 base damage'],
          'Prism':[mercury,range3,7,'Attack with ice crystals','Deals 40 base damage'],
          'Hail Prism':[mercury,range5,7,'Attack with ice crystals','Deals 90 base damage'],
          'Freeze Prism':[mercury,range5,7,'Attack with ice crystals','Deals 190 base damage'],
          'Call Zombie':[mercury,range1,5,'Command a zombie to strike a foe','Deals 40 base damage'],
          'Blue Dragon':[mercury,range5,17,'Attack with an icy blast','Deals 130 base damage\nDeals less damage to secondary targets than usual'],
          'Frost Card':[mercury,range3,28,'Throw a card of the Ice suit','Deals 175 base damage'],
          'Cutting Edge':[mercury,range1,5,'Inflict damage with a shock wave','Attack +32 Mercury-based damage'],
          'Plume Edge':[mercury,range1,15,'Attack with a foaming geyser','Attack +80 Mercury-based damage'],
          'Diamond Dust':[mercury,range1,6,'Attack with crystalline ice','Attack +34 Mercury-based damage'],
          'Diamond Berg':[mercury,range1,17,'Freeze and crush a foe','Attack +92 Mercury-based damage'],
          'Ply':[mercury,range1,4,'Recover 100 HP with faith\'s power','Restores 100 base HP\nCan be used outside of battle'],
          'Ply Well':[mercury,range1,8,'Recover 200 HP with faith\'s power','Restores 200 base HP\nCan be used outside of battle'],
          'Pure Ply':[mercury,range1,12,'Recover 1000 HP with faith\'s power','Restores 1000 base HP\nCan be used outside of battle'],
          'Pixie':[mercury,range1,5,'Conjure pixies to restore 115 HP','Restores 115 base HP'],
          'Faery':[mercury,range1,5,'Conjure faeries to restore 120 HP','Restores 120 base HP'],
          'Weird Nymph':[mercury,range1,5,'Conjure pixies to restore 125 HP','Restores 125 base HP'],
          'Succubus':[mercury,range1,9,'Conjure faeries to restore 250 HP','Restores 250 base HP'],
          'Wish':[mercury,rangeall,9,'Restore 80 HP to the whole party','Restores 80 base HP to the whole party\nCan be used outside of battle'],
          'Wish Well':[mercury,rangeall,13,'Restore 160 HP to the whole party','Restores 160 base HP to the whole party\nCan be used outside of battle'],
          'Pure Wish':[mercury,rangeall,20,'Restore 400 HP to the whole party','Restores 400 base HP to the whole party\nCan be used outside of battle'],
          'Elder Wood':[mercury,rangeall,14,'Restore 170 HP to all allies','Restores 170 base HP to the whole party'],
          'Estre Wood':[mercury,rangeall,14,'Restore 180 HP to all allies','Restores 180 base HP to the whole party'],
          'Cure Poison':[mercury,range1,2,'Cleanse the body of poison','Removes Poison\nCan be used outside of battle'],
          'Restore':[mercury,range1,3,'Remove sleep, stun, and delusion','Removes Sleep, Stun, Delusion and Curse'],
          'Break':[mercury,rangeall,5,'Eliminate an enemy\'s bonuses','Removes the enemy party\'s statistical buffs'],
          'Avoid':[mercury,None,'Encounter fewer monsters','Used out of battle to lower the rate of enemy encounters'],
          'Lift':[mercury,None,2,'Lift an object vertically','Used out of battle to lift certain boulders off the ground'],
          'Cloak':[mercury,None,1,'Hide away in shadows','Used out of battle to vanish into shadows\nUseless in The Lost Age'],
          'Parch':[mercury,None,2,'Evaporate standing water','Used out of battle to dry out pools of still water'],
          'Wild Wolf':[none,range1,3,'Call on a feral ally\'s aid','Attack +30 base damage'],
          'Orc':[none,range1,3,'Attack with your body\'s mass','Attack +35 base damage'],
          'Roc':[none,range1,22,'Strike with the sweep of a mighty wing','Attack +140 base damage'],
          'Force':[none,None,2,'Strike a distant object','Used out of battle to strike some distant objects']}

team=[]

teamdjinn=tk.Frame(root)
teamdjinn.grid(row=0,column=0,columnspan=4,sticky='n')

tk.Label(teamdjinn,image=venus).grid(row=0,column=0,sticky='e')
tk.Label(teamdjinn,image=mars).grid(row=0,column=2,sticky='e')
tk.Label(teamdjinn,image=jupiter).grid(row=0,column=4,sticky='e')
tk.Label(teamdjinn,image=mercury).grid(row=0,column=6,sticky='e')

teamvenus=tk.Label(teamdjinn,width=2)
teammars=tk.Label(teamdjinn,width=2)
teamjupiter=tk.Label(teamdjinn,width=2)
teammercury=tk.Label(teamdjinn,width=2)

teamvenus.grid(row=0,column=1,sticky='w')
teammars.grid(row=0,column=3,sticky='w')
teamjupiter.grid(row=0,column=5,sticky='w')
teammercury.grid(row=0,column=7,sticky='w')

def updateteam():
    curteamdjinn=list(map(sum,zip(*[x.curdjinn for x in team])))
    bg=[color,color,color,color]
    if curteamdjinn[0]>18:
        bg[0]='red'
    if curteamdjinn[1]>18:
        bg[1]='red'
    if curteamdjinn[2]>18:
        bg[2]='red'
    if curteamdjinn[3]>18:
        bg[3]='red'
    teamvenus.config(text=str(curteamdjinn[0]),bg=bg[0])
    teammars.config(text=str(curteamdjinn[1]),bg=bg[1])
    teamjupiter.config(text=str(curteamdjinn[2]),bg=bg[2])
    teammercury.config(text=str(curteamdjinn[3]),bg=bg[3])

class char:
    def __init__(self,row,column):
        team.append(self)
        
        self.row=row
        self.column=column
        self.i=row*4+column
        self.curclass='None'
        self.curdjinn=djinn[4][self.curclass]
        self.img=tk.PhotoImage(file=names[self.i]+'.gif')

        self.frame=tk.Frame(root)
        self.frame.grid(row=self.row+1,column=self.column)

        self.mug=tk.Label(self.frame,image=self.img)
        self.mug.grid(row=0,column=0,sticky='e')
        self.mug.image=self.img

        self.djinnframe=tk.Frame(self.frame)
        self.djinnframe.grid(row=1,column=0,sticky='n')

        self.statsframe=tk.Frame(self.frame)
        self.statsframe.grid(row=0,column=1,rowspan=2,sticky='w')

        self.venusicon=tk.Label(self.djinnframe,image=venus).grid(row=0,column=0,sticky='e')
        self.marsicon=tk.Label(self.djinnframe,image=mars).grid(row=1,column=0,sticky='e')
        self.jupitericon=tk.Label(self.djinnframe,image=jupiter).grid(row=2,column=0,sticky='e')
        self.mercuryicon=tk.Label(self.djinnframe,image=mercury).grid(row=3,column=0,sticky='e')

        self.venusset=tk.Label(self.djinnframe)
        self.marsset=tk.Label(self.djinnframe)
        self.jupiterset=tk.Label(self.djinnframe)
        self.mercuryset=tk.Label(self.djinnframe)

        self.venusset.grid(row=0,column=1,sticky='w')
        self.marsset.grid(row=1,column=1,sticky='w')
        self.jupiterset.grid(row=2,column=1,sticky='w')
        self.mercuryset.grid(row=3,column=1,sticky='w')

        tk.Label(self.statsframe,text='HP').grid(row=0,column=0,sticky='w')
        tk.Label(self.statsframe,text='PP').grid(row=1,column=0,sticky='w')
        tk.Label(self.statsframe,text='ATK').grid(row=2,column=0,sticky='w')
        tk.Label(self.statsframe,text='DEF').grid(row=3,column=0,sticky='w')
        tk.Label(self.statsframe,text='AGI').grid(row=4,column=0,sticky='w')
        tk.Label(self.statsframe,text='LCK').grid(row=5,column=0,sticky='w')

        self.curhp=tk.Label(self.statsframe,width=3,anchor='e')
        self.curpp=tk.Label(self.statsframe,width=3,anchor='e')
        self.curatk=tk.Label(self.statsframe,width=3,anchor='e')
        self.curdef=tk.Label(self.statsframe,width=3,anchor='e')
        self.curagi=tk.Label(self.statsframe,width=3,anchor='e')
        self.curlck=tk.Label(self.statsframe,width=3,anchor='e')

        self.curhp.grid(row=0,column=1,sticky='ew')
        self.curpp.grid(row=1,column=1,sticky='ew')
        self.curatk.grid(row=2,column=1,sticky='ew')
        self.curdef.grid(row=3,column=1,sticky='ew')
        self.curagi.grid(row=4,column=1,sticky='ew')
        self.curlck.grid(row=5,column=1,sticky='ew')

        self.hpboost=tk.Label(self.statsframe)
        self.ppboost=tk.Label(self.statsframe)
        self.atkboost=tk.Label(self.statsframe)
        self.defboost=tk.Label(self.statsframe)
        self.agiboost=tk.Label(self.statsframe)
        self.lckboost=tk.Label(self.statsframe)

        self.hpboost.grid(row=0,column=2,sticky='e')
        self.ppboost.grid(row=1,column=2,sticky='e')
        self.atkboost.grid(row=2,column=2,sticky='e')
        self.defboost.grid(row=3,column=2,sticky='e')
        self.agiboost.grid(row=4,column=2,sticky='e')
        self.lckboost.grid(row=5,column=2,sticky='e')

        self.charclass=tk.StringVar(self.frame)
        self.charclass.set(self.curclass)
        self.classmenu=tk.OptionMenu(self.frame,self.charclass,'None',mono[self.i],*djinn[column],command=self.update)
        self.classmenu.config(width=15)
        self.classmenu.grid(row=2,column=0,columnspan=2,sticky='ew')

        self.update(self.curclass)

    def update(self,choice):
        element=self.column
        if choice in mono:
            element=4
        self.curdjinn=djinn[element][choice]
        updateteam()
        self.venusset.config(text=str(self.curdjinn[0]))
        self.marsset.config(text=str(self.curdjinn[1]))
        self.jupiterset.config(text=str(self.curdjinn[2]))
        self.mercuryset.config(text=str(self.curdjinn[3]))
        self.curhp.config(text=str(int(Decimal(str(stats[self.i][0]))*Decimal(str(boosts[choice][0])))))
        self.curpp.config(text=str(int(Decimal(str(stats[self.i][1]))*Decimal(str(boosts[choice][1])))))
        self.curatk.config(text=str(int(Decimal(str(stats[self.i][2]))*Decimal(str(boosts[choice][2])))))
        self.curdef.config(text=str(int(Decimal(str(stats[self.i][3]))*Decimal(str(boosts[choice][3])))))
        self.curagi.config(text=str(int(Decimal(str(stats[self.i][4]))*Decimal(str(boosts[choice][4])))))
        self.curlck.config(text=str(int(Decimal(str(stats[self.i][5]))*Decimal(str(boosts[choice][5])))))
        self.hpboost.config(text=str(int(Decimal(str(boosts[choice][0]))*Decimal('100')))+'%')
        self.ppboost.config(text=str(int(Decimal(str(boosts[choice][1]))*Decimal('100')))+'%')
        self.atkboost.config(text=str(int(Decimal(str(boosts[choice][2]))*Decimal('100')))+'%')
        self.defboost.config(text=str(int(Decimal(str(boosts[choice][3]))*Decimal('100')))+'%')
        self.agiboost.config(text=str(int(Decimal(str(boosts[choice][4]))*Decimal('100')))+'%')
        self.lckboost.config(text=str(int(Decimal(str(boosts[choice][5]))*Decimal('100')))+'%')

isaac=char(0,0)
garet=char(0,1)
ivan=char(0,2)
mia=char(0,3)
felix=char(1,0)
jenna=char(1,1)
sheba=char(1,2)
piers=char(1,3)

updateteam()

root.mainloop()
