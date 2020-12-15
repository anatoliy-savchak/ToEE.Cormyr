# Weapon Price pattern - Masterwork: +300, Enchantment +1: +2000, Enchantment +2: +8000, Enchantment +3: +18000, Enchantment +4: +32000, Enchantment +5: +50000
# Silver: Ammunition +2 gp, Light weapon +20 gp, One-handed weapon, or one head of a double weapon +90 gp, Two-handed weapon, or both heads of a double weapon +180 gp.
# Staff: 375 gp x the level of the highest-level spell x the level of the caster (min 8), plus 75% of the value of the next most costly
# ability (281.25 gp x the level of the spell x the level of the caster), plus one-half of the value of any other abilities (187.5 gp x thel evel of the spell x the level of the caster).

# Simple Light Melee Weapons
PROTO_WEAPON_DAGGER = 4060 # Cost: 2 gp, Dmg: 1d4
PROTO_WEAPON_DAGGER_MASTERWORK = 4155 # Cost: 302 gp, Dmg: 1d4, Masterwork
PROTO_WEAPON_DAGGER_PLUS_1 = 4058 # Cost: 2302 gp, Dmg: 1d4+1, Ench: +1
PROTO_WEAPON_DAGGER_PLUS_2 = 4057 # Cost: 8302 gp, Dmg: 1d4+2, Ench: +2
PROTO_WEAPON_DAGGER_PLUS_2_OF_VENOM = 4112 # Cost: 8302 gp, Dmg: 1d4+2, Ench: +2, Poison. DMG 226

PROTO_WEAPON_DAGGER_THROWING = 4059 # Cost: 2 gp, Dmg: 1d4
PROTO_WEAPON_DAGGER_THROWING_MASTERWORK = 4155 # Cost: 302 gp, Dmg: 1d4, Masterwork

PROTO_WEAPON_MACE_LIGHT = 4071 # Cost: 5 gp, Dmg: 1d6
PROTO_WEAPON_MACE_LIGHT_MASTERWORK = 4169 # Cost: 305 gp, Dmg: 1d6, Masterwork
PROTO_WEAPON_MACE_LIGHT_MASTERWORK_SILVER = 4496 # Cost: 120 !!! (325=5+300+20) gp, Dmg: 1d6, Masterwork, Weapon Silver
PROTO_WEAPON_MACE_LIGHT_PLUS_1 = 4109 # Cost: 2305 gp, Dmg: 1d6+1, Ench: +1
PROTO_WEAPON_MACE_LIGHT_PLUS_3_OF_SMITING = 4124 # Cost: 2000 (!!! = 20,000) gp, Dmg: 1d6+1, Ench: +3, Rod of Smiting (Silver, 4x crit for 25 times); Troika
PROTO_WEAPON_MACE_LIGHT_PLUS_1_FROST = 4251 # Chilled Light Mace, Cost: 4305 (!!! 305+8000=8305) gp, Dmg: 1d6+1+1d6 cold, Ench: +1, Weapon Frost

PROTO_WEAPON_SICKLE = 4236 # Cost: 6 gp, Dmg: 1d6
PROTO_WEAPON_SICKLE_MASTERWORK = 4237 # Cost: 306 gp, Dmg: 1d6, Masterwork

# Simple One-Handed Melee Weapons
PROTO_WEAPON_CLUB = 4074 # Cost: 0 gp, Dmg: 1d6
PROTO_WEAPON_CLUB_MASTERWORK = 4172 # Cost: 300 gp, Dmg: 1d6

PROTO_WEAPON_MORNINGSTAR = 4070 # Cost: 8 gp, Dmg: 1d8
PROTO_WEAPON_MORNINGSTAR_MASTERWORK = 4168 # Cost: 8 gp, Dmg: 1d8
PROTO_WEAPON_MORNINGSTAR_PLUS_1 = 4193 # Cost: 2,308 gp, Dmg: 1d8+1, Ench: +1

PROTO_WEAPON_MACE_HEAVY = 4068 # Cost: 12 gp, Dmg: 1d8
PROTO_WEAPON_MACE_HEAVY_MASTERWORK = 4166 # Cost: 312 gp, Dmg: 1d8, Masterwork
PROTO_WEAPON_MACE_HEAVY_PLUS_1_HOLY = 4220 # Cost: 18,315 gp, Dmg: 1d8+2d6, Ench: +1, Holy
PROTO_WEAPON_MACE_HEAVY_PLUS_1_UNHOLY = 4496 # Cost: 18,315 gp, Dmg: 1d8+2d6, Ench: +1, Unholy
PROTO_WEAPON_MACE_HEAVY_PLUS_3_UNHOLY = 4450 # Mace of Midnighte. Cost: 5,000 (!!!) gp, Dmg: 1d8+2d6, Ench: +3, Unholy
PROTO_WEAPON_MACE_HEAVY_ARTIFACT_MAJOR_CUTHBERT = 4504 # Cost: 18,315 gp (!!! =>100,000) gp, Dmg: 1d8+2d6+2d8+2d6, Ench: +5, Weapon Holy, Weapon Disruption, Weapon Lawful

PROTO_WEAPON_SHORTSPEAR = 4116 # Cost: 1 gp, Dmg: 1d6
PROTO_WEAPON_SHORTSPEAR_MASTERWORK = 4183 # Cost: 301 gp, Dmg: 1d6, Masterwork

# Simple Two-Handed Melee Weapons
PROTO_WEAPON_LONGSPEAR = 4194 # Cost: 5 gp, Dmg: 1d8
PROTO_WEAPON_LONGSPEAR_MASTERWORK = 4196 # Cost: 305 gp, Dmg: 1d8, Masterwork
PROTO_WEAPON_LONGSPEAR_PLUS_2 = 4252 # Cost: 8,305 gp, Dmg: 1d8+2, Ench: +2

PROTO_WEAPON_QUARTERSTAFF = 4241 # Cost: 5 gp, Dmg: 1d6
PROTO_WEAPON_QUARTERSTAFF_MASTERWORK = 4179 # Cost: 305 gp, Dmg: 1d6, Masterwork
PROTO_WEAPON_QUARTERSTAFF_PLUS_3_STAFF_OF_STRIKING = 4125 # Cost: 2000 (!!! 18,305+~2k) gp, Dmg: 1d6, Ench: +3, Staff of Striking, Troika
PROTO_WEAPON_QUARTERSTAFF_MASTERWORK_STAFF_OF_SIZE_ALTERATION = 4309 # Cost: 6500 (!!! 6250+305) gp, Dmg: 1d6, Masterwork, Enalrge Person, Shrink, Troika

PROTO_WEAPON_SPEAR = 4117 # Cost: 8 gp, Dmg: 1d8
PROTO_WEAPON_SPEAR_MASTERWORK = 4184 # Cost: 308 gp, Dmg: 1d8, Masterwork
PROTO_WEAPON_SPEAR_PLUS_1 = 4121 # Cost: 2002 (!!! 2308) gp, Dmg: 1d8, Ench: +1

# Simple Ranged Weapons
PROTO_WEAPON_JAVELIN = 4123 # Cost: 1 gp, Dmg: 1d6
PROTO_WEAPON_JAVELIN_MASTERWORK = 4187 # Cost: 301 gp, Dmg: 1d6, Masterwork
PROTO_WEAPON_JAVELIN_OF_LIGHTNING = 4134 # Cost: 751 (!!! 1500) gp, Dmg: 1d6, Lightning Bolt

PROTO_WEAPON_CROSSBOW_HEAVY = 4097 # Cost: 50 gp, Dmg: 1d10
PROTO_WEAPON_CROSSBOW_HEAVY_MASTERWORK = 4178 # Cost: 350 gp, Dmg: 1d10, Masterwork
#PROTO_WEAPON_CROSSBOW_HEAVY_PLUS_1 = 4475 # Cost: 2350 gp, Dmg: 1d10, Ench: +1 TODO instead of distance
PROTO_WEAPON_CROSSBOW_HEAVY_PLUS_1_HOLY = 4465 # Cost: 8350 gp, Dmg: 1d10, Ench: +1, Weapon Holy
PROTO_WEAPON_CROSSBOW_HEAVY_PLUS_1_UNHOLY = 4467 # Cost: 8350 gp, Dmg: 1d10, Ench: +1, Weapon Unholy

PROTO_WEAPON_CROSSBOW_LIGHT = 4096 # Cost: 30 gp, Dmg: 1d8
PROTO_WEAPON_CROSSBOW_LIGHT_MASTERWORK = 4177 # Cost: 330 gp, Dmg: 1d8, Masterwork
#PROTO_WEAPON_CROSSBOW_LIGHT_PLUS_1 = 4474 # Cost: 2335 gp, Dmg: 1d8, Ench: +1 TODO instead of distance
PROTO_WEAPON_CROSSBOW_LIGHT_PLUS_1_FROST = 4468 # Cost: 8335 gp, Dmg: 1d8, Ench: +1, Weapon Frost
PROTO_WEAPON_CROSSBOW_LIGHT_PLUS_1_FLAMING = 4469 # Cost: 8335 gp, Dmg: 1d8, Ench: +1, Weapon Flaming
PROTO_WEAPON_CROSSBOW_LIGHT_PLUS_1_SHOCK = 4470 # Cost: 8335 gp, Dmg: 1d8, Ench: +1, Weapon Shock
PROTO_WEAPON_CROSSBOW_LIGHT_PLUS_1_AXIOMATIC = 4462 # Cost: 8335 gp, Dmg: 1d8, Ench: +1, Weapon Lawful
PROTO_WEAPON_CROSSBOW_LIGHT_PLUS_1_ANARCHIC = 4463 # Cost: 8335 gp, Dmg: 1d8, Ench: +1, Weapon Chaotic
PROTO_WEAPON_CROSSBOW_LIGHT_PLUS_1_HOLY = 4464 # Cost: 8335 gp, Dmg: 1d8, Ench: +1, Weapon Holy
PROTO_WEAPON_CROSSBOW_LIGHT_PLUS_1_UNHOLY = 4466 # Cost: 8335 gp, Dmg: 1d8, Ench: +1, Weapon Unholy

PROTO_AMMO_BOLT_QUIVER = 5005
PROTO_AMMO_BOLT_QUIVER_DROW_SLEEP = 5023

PROTO_WEAPON_DART = 4127 # Cost: 0.05 gp, Dmg: 1d4
PROTO_WEAPON_DART_MASTERWORK = 4188 # Cost: 6.5 !!! gp, Dmg: 1d4, Masterwork

PROTO_WEAPON_SLING = 4115 # Cost: 0 gp, Dmg: 1d4
PROTO_WEAPON_SLING_MASTERWORK = 4182 # Cost: 300 gp, Dmg: 1d4
PROTO_AMMO_BULLET_POUCH = 5007

# Martial Light Melee Weapons
PROTO_WEAPON_HAMMER_LIGHT = 4076 # Cost 1 gp, Dmg: 1d4
PROTO_WEAPON_HAMMER_LIGHT_MASTERWORK = 4174 # Cost 301 gp, Dmg: 1d4

PROTO_WEAPON_HANDAXE = 4067 # Cost 6 gp, Dmg: 1d6
PROTO_WEAPON_HANDAXE_MASTERWORK = 4165 # Cost 306 gp, Dmg: 1d6, Masterwork

PROTO_WEAPON_KUKRI = 4624 # Cost 8 gp, Dmg: 1d4
PROTO_WEAPON_KUKRI_MASTERWORK = 4216 # Cost 308 gp, Dmg: 1d4, Masterwork
PROTO_WEAPON_KUKRI_PLUS_2 = 4245 # Cost 8308 gp, Dmg: 1d4, Ench: +2

PROTO_WEAPON_SHORTSWORD = 4049 # Cost: 10 gp, Dmg: 1d6
PROTO_WEAPON_SHORTSWORD_MASTERWORK = 4159 # Cost: 310 gp, Dmg: 1d6, Masterwork
PROTO_WEAPON_SHORTSWORD_PLUS_1 = 4126 # Cost 2310 gp, Dmg: 1d6, Ench: +1
PROTO_WEAPON_SHORTSWORD_PLUS_2 = 4161 # Cost 8310 gp, Dmg: 1d6, Ench: +2

# Martial One-Handed Melee Weapons
PROTO_BATTLEAXE = 4114 # Cost 10gp, Dmg: 1d8
PROTO_BATTLEAXE_MASTERWORK = 4181 # Cost 310gp, Dmg: 1d8, Masterwork
PROTO_BATTLEAXE_PLUS_1 = 4098 # Cost 2310gp, Dmg: 1d8, Ench: +1

PROTO_FLAIL = 4408 # Cost 8gp, Dmg: 1d8
PROTO_FLAIL_MASTERWORK = 4444 # Cost 308gp, Dmg: 1d8, Masterwork
PROTO_FLAIL_PLUS_2 = 4255 # Cost 8308gp, Dmg: 1d8, Ench: +2

PROTO_LONGSWORD = 4036 # Cost 15
PROTO_LONGSWORD_MASTERWORK = 4132 # Cost 315
PROTO_LONGSWORD_PLUS_1 = 4081 # Cost 2315 gp, Dmg: 1d8, Ench: +1
PROTO_LONGSWORD_PLUS_1_FLAMING = 4028 # Cost 8315 gp, Dmg: 1d8, Ench: +1, Weapon Flaming
PROTO_LONGSWORD_PLUS_1_HOLY = 4028 # Cost 18315 gp, Dmg: 1d8+2d6, Ench: +1, Weapon Holy
PROTO_LONGSWORD_PLUS_2 = 4082 # Cost 8315 gp, Dmg: 1d8, Ench: +2
PROTO_LONGSWORD_PLUS_2_FLAMING = 4248 # Smelted Longsword. Cost 10315 (!!! 18315) gp, Dmg: 1d8, Ench: +2, Weapon Flaming
PROTO_LONGSWORD_PLUS_3 = 4083 # Cost 18315 gp, Dmg: 1d8, Ench: +3
PROTO_LONGSWORD_PLUS_4 = 4084 # Cost 32315 gp, Dmg: 1d8, Ench: +4
PROTO_LONGSWORD_PLUS_5 = 4085 # Cost 50315 gp, Dmg: 1d8, Ench: +5

PROTO_RAPIER = 4009 # Cost 20gp, Dmg: 1d6
PROTO_RAPIER_MASTERWORK = 4156 # Cost 320gp, Dmg: 1d6, Masterwork
PROTO_RAPIER_PLUS_2 = 4500 # Cost 8315 gp, Dmg: 1d6, Ench: +2

PROTO_SCIMITAR = 4045 # Cost 15gp, Dmg: 1d6
PROTO_SCIMITAR_MASTERWORK = 4414 # Cost 315gp, Dmg: 1d6, Masterwork
PROTO_SCIMITAR_PLUS_1 = 4047 # Cost 2315 gp, Dmg: 1d6, Ench: +1
PROTO_SCIMITAR_PLUS_2 = 4256 # Cost 8315 gp, Dmg: 1d6, Ench: +2

PROTO_WEAPON_PICK_HEAVY = 4069 # Cost 8gp, Dmg: 1d6
PROTO_WEAPON_PICK_HEAVY_MASTERWORK = 4167 # Cost 308gp, Dmg: 1d6 , Masterwork

PROTO_WEAPON_TRIDENT = 4413 # Cost
PROTO_WEAPON_TRIDENT_MASTERWORK = 4706 # Cost
PROTO_WEAPON_TRIDENT_PLUS_1 = 4716 # Cost

PROTO_WEAPON_WARHAMMER = 4077 # Cost 312 gp, Dmg: 1d6 , Masterwork
PROTO_WEAPON_WARHAMMER_MASTERWORK = 4175 # Cost 312 gp, Dmg: 1d6 , Masterwork
PROTO_WEAPON_WARHAMMER_PLUS_1 = 4078 # Cost 2312 gp, Dmg: 1d6 , Ench: +1
PROTO_WEAPON_WARHAMMER_PLUS_2 = 4079 # Cost 8312 gp, Dmg: 1d6 , Ench: +2

# Martial Two-Handed Melee Weapons
PROTO_WEAPON_FALCHION = 4026 # Cost 75 gp, 2d4 18-20/x2
PROTO_WEAPON_FALCHION_MASTERWORK = 4158 # Cost 375 gp, Dmg: 2d4, Masterwork
PROTO_WEAPON_FALCHION_PLUS_1 = 4447 # Cost 2375 gp, Dmg: 2d4, Ench: +1
PROTO_WEAPON_FALCHION_PLUS_2 = 4448 # Cost 8375 gp, Dmg: 2d4, Ench: +2

PROTO_WEAPON_GLAIVE = 4118 # Cost 8 gp
PROTO_WEAPON_GLAIVE_MASTERWORK = 4185 # Cost 308 gp
PROTO_WEAPON_GLAIVE_PLUS_1 = 4718 # Cost 2308 gp

PROTO_WEAPON_GREATAXE = 4064 # Cost 20 gp, Dmg: 1d12
PROTO_WEAPON_GREATAXE_MASTERWORK = 4065 # Cost 320 gp, Dmg: 1d12, Masterwork
PROTO_WEAPON_GREATAXE_PLUS_1 = 4708 # Cost 2320 gp, Dmg: 1d12, Ench: +1
PROTO_WEAPON_GREATAXE_PLUS_1_HOLY = 4221 # Cost 18320 gp, Dmg: 1d12, Ench: +1, Weapon Holy
PROTO_WEAPON_GREATAXE_PLUS_2 = 4254 # Cost 8320 gp, Dmg: 1d12, Ench: +2

PROTO_WEAPON_GREATCLUB = 4066 # Cost: 5 gp, Dmg: 1d10
PROTO_WEAPON_GREATCLUB_MASTERWORK = 4164 # Cost: 305 gp, Dmg: 1d10, Masterwork

PROTO_WEAPON_FLAIL_HEAVY = 4207 # Cost: 15 gp, Dmg: 1d10
PROTO_WEAPON_FLAIL_HEAVY_MASTERWORK = 4208 # Cost: 315 gp, Dmg: 1d10, Masterwork

PROTO_WEAPON_GREATSWORD = 4010 # Cost: 50 gp, Dmg: 2d6
PROTO_WEAPON_GREATSWORD_MASTERWORK = 4012 # Cost: 350 gp, Dmg: 2d6, Masterwork
PROTO_WEAPON_GREATSWORD_PLUS_1 = 4715 # Cost 2350gp, Dmg: 2d6, Ecnh: +1
PROTO_WEAPON_GREATSWORD_PLUS1_FLAMING = 4711 # Cost 8350gp

PROTO_WEAPON_GUISARME = 4113 # Cost 9 gp, Dmg: 2d4
PROTO_WEAPON_GUISARME_MASTERWORK = 4180 # Cost 309 gp, Dmg: 2d4, Masterwork

PROTO_WEAPON_HALBERD = 4412 # Cost 20 gp, Dmg: 1d10
PROTO_WEAPON_HALBERD_MASTERWORK = 4707 # Cost 320 gp, Dmg: 1d10, Masterwork
PROTO_WEAPON_HALBERD_PLUS_2 = 4253 # Cost 8310 gp, Dmg: 1d10, Ench: +2

PROTO_WEAPON_RANSEUR = 4119 # Cost 10 gp, Dmg: 2d4
PROTO_WEAPON_RANSEUR_MASTERWORK = 4186 # Cost 10 gp, Dmg: 2d4, Masterwork
PROTO_WEAPON_RANSEUR_PLUS_1_HOLY = 4219 # Cost 18315 gp, Dmg: 2d4, Ench: +1, Weapon Holy

PROTO_WEAPON_SCYTHE = 4170 # Cost 18 gp, Dmg: 2d4
PROTO_WEAPON_SCYTHE_MASTERWORK = 4170 # Cost 318 gp, Dmg: 2d4, Masterwork

# Martial Ranged Weapons
PROTO_WEAPON_LONGBOW = 4087 # Cost: 30 gp, Dmg: 1d8
PROTO_WEAPON_LONGBOW_COMPOSITE_12 = 4300 # Cost: 100 gp, Dmg: 1d8+1
PROTO_WEAPON_LONGBOW_COMPOSITE_14 = 4195 # Cost: 100 gp, Dmg: 1d8+2
PROTO_WEAPON_LONGBOW_COMPOSITE_16 = 4301 # Cost: 100 gp, Dmg: 1d8+3

PROTO_WEAPON_LONGBOW_MASTERWORK = 4176 # Cost: 330 gp, Dmg: 1d8
PROTO_WEAPON_LONGBOW_COMPOSITE_12_MASTERWORK = 4304 # Cost: 400 gp, Dmg: 1d8+1
PROTO_WEAPON_LONGBOW_COMPOSITE_14_MASTERWORK = 4305 # Cost: 400 gp, Dmg: 1d8+2
PROTO_WEAPON_LONGBOW_COMPOSITE_16_MASTERWORK = 4306 # Cost: 400 gp, Dmg: 1d8+3

PROTO_WEAPON_LONGBOW_PLUS_1 = 4191 # Cost: 2375 gp, Dmg: 1d8, Ench: +1
PROTO_WEAPON_LONGBOW_COMPOSITE_16_PLUS1 = 4717 # Cost: 2700 gp, Dmg: 1d8+4
PROTO_WEAPON_LONGBOW_PLUS_2 = 4299 # Cost: 8375 gp, Dmg: 1d8, Ench: +1
PROTO_WEAPON_LONGBOW_PLUS_1_FLAMING = 4348 # Cost: 8375 gp, Dmg: 1d8, Ench: +1, Weapon Flaming
PROTO_WEAPON_LONGBOW_PLUS_1_FROST = 4108 # Cost: 8375 gp, Dmg: 1d8, Ench: +1, Weapon Frost
PROTO_WEAPON_LONGBOW_PLUS_2_FROST = 4349 # Cost: 18375 gp, Dmg: 1d8, Ench: +2, Weapon Frost

PROTO_WEAPON_SHORTBOW = 4201 # Cost: 30 gp, Dmg: 1d6
PROTO_WEAPON_SHORTBOW_MASTERWORK = 4202 # Cost: 330 gp, Dmg: 1d6, Masterwork
PROTO_WEAPON_SHORTBOW_COMPOSITE_12_MASTERWORK = 4307 # Cost: 450 gp, Dmg: 1d6, Masterwork
PROTO_WEAPON_SHORTBOW_PLUS_1 = 4461 # Cost: 2330 gp, Dmg: 1d6, Ench: +1

PROTO_AMMO_ARROW_QUIVER = 5004
PROTO_AMMO_ARROW_QUIVER_OF_PIXIE_SLEEP_ARROWS = 5021

# Exotic Light Melee Weapons
PROTO_WEAPON_SPIKED_KAMA = 4604 # Cost 2 gp, Dmg: 1d6
PROTO_WEAPON_SPIKED_KAMA_MASTERWORK = 4605 # Cost 302 gp, Dmg: 1d6, Masterwork

PROTO_WEAPON_SPIKED_SIANGHAM = 4626 # Cost 302 gp !!!, Dmg: 1d6 
PROTO_WEAPON_SPIKED_SIANGHAM_MASTERWORK = 4625 # Cost 302 gp, Dmg: 1d6, Masterwork

# Exotic One-Handed Melee Weapons
PROTO_WEAPON_SWORD_BASTARD = 4015 # Cost: 35 gp, Dmg: 1d10
PROTO_WEAPON_SWORD_BASTARD_MASTERWORK = 4157 # Cost: 335 gp, Dmg: 1d10, Masterwork
PROTO_WEAPON_SWORD_BASTARD_PLUS_1 = 4443 # Cost: 2335 gp, Dmg: 1d10, Ench: +1
PROTO_WEAPON_SWORD_BASTARD_PLUS_2 = 4257 # Cost: 8335 gp, Dmg: 1d10, Ench: +2
PROTO_WEAPON_SWORD_BASTARD_PLUS_1_HOLY = 4598 # Cost: 18335 gp, Dmg: 1d10, Ench: +1, Weapon Holy

PROTO_WEAPON_WARAXE_DWARVEN = 4063 # Cost: 30 gp, Dmg: 1d10
PROTO_WEAPON_WARAXE_DWARVEN_MASTERWORK = 4163 # Cost: 330 gp, Dmg: 1d10, Masterwork
PROTO_WEAPON_WARAXE_DWARVEN_PLUS_2 = 4258 # Cost: 8330 gp, Dmg: 1d10, Ench: +2

# Exotic Two-Handed Melee Weapons
PROTO_WEAPON_DOUBLEAXE_ORC = 4344 # Cost: 120 !!! gp, Dmg: 1d8/1d8
PROTO_WEAPON_DOUBLEAXE_ORC_MASTERWORK = 4163 # Cost: 280 !!! gp, Dmg: 1d8/1d8, Masterwork
PROTO_WEAPON_DOUBLEAXE_ORC_PLUS_3_UNHOLY = 4086 # Cost: 50660 gp, Dmg: 1d8/1d8, Ench: +3, Weapon Unholy

PROTO_WEAPON_SPIKED_CHAIN = 4209 # Cost: 25 gp, Dmg: 2d4
PROTO_WEAPON_SPIKED_CHAIN_MASTERWORK = 4210 # Cost: 325 gp, Dmg: 2d4, Masterwork
PROTO_WEAPON_SPIKED_CHAIN_PLUS_1 = 4709 # Cost 2325 gp, Dmg: 2d4, Ench: +1
PROTO_WEAPON_SPIKED_CHAIN_PLUS_1_FLAMING = 4249 # Scalded Spiked Chain. Cost 4325 (!!! 8325) gp, Dmg: 2d4, Ench: +1, Weapon Flaming
PROTO_WEAPON_SPIKED_CHAIN_PLUS_1_HOLY = 4249 # Thorned Chains of Love +1. Cost 18325 gp, Dmg: 2d4, Ench: +1, Weapon Holy
PROTO_WEAPON_SPIKED_CHAIN_PLUS_2 = 4263 # Cost 8325 gp, Dmg: 2d4, Ench: +1

PROTO_WEAPON_HAMMER_GNOME_HOOKED = 4075 # Cost: 20 gp, Dmg: 1d8/1d6
PROTO_WEAPON_HAMMER_GNOME_HOOKED_MASTERWORK = 4173 # Cost: 320 gp, Dmg: 1d8/1d6
PROTO_WEAPON_HAMMER_GNOME_HOOKED_PLUS_2 = 4259 # Cost: 8620 gp, Dmg: 1d8/1d6, Ench: +2

# Exotic Ranged Weapons
PROTO_WEAPON_CROSSBOW_REPEATING_LIGHT = 4494 # Cost: 250 gp, Dmg: 1d8
PROTO_WEAPON_CROSSBOW_REPEATING_LIGHT_MASTERWORK = 4489 # Cost: 550 gp, Dmg: 1d8, Masterwork
PROTO_WEAPON_CROSSBOW_REPEATING_LIGHT_PLUS_1 = 4130 # Wonnilon's Repeating Light Crossbow +1. Cost: 2335 gp, Dmg: 1d8, Ench: +1

PROTO_WEAPON_SHURIKEN = 4211 # Cost: 1 gp, Dmg: 1d2
PROTO_WEAPON_SHURIKEN_MASTERWORK = 4212 # Cost: 7 !!! gp, Dmg: 1d2, Masterwork

# Misc
PROTO_WEAPON_FLIND_PLUS1 = 4713 # Cost 2308 gp, Ench: +1

