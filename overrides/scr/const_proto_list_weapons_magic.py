import const_proto_weapon

PROTOS_WEAPON_SIMPLE_MELEE_LIGHT_PLUS_1 = [\
	const_proto_weapon.PROTO_WEAPON_DAGGER_PLUS_1 \
	, const_proto_weapon.PROTO_WEAPON_MACE_LIGHT_PLUS_1 \
	]

PROTOS_WEAPON_SIMPLE_MELEE_ONE_HANDED_PLUS_1 = [\
	const_proto_weapon.PROTO_WEAPON_MORNINGSTAR_PLUS_1 \
	, const_proto_weapon.PROTO_WEAPON_MACE_LIGHT_PLUS_1 \
	]

PROTOS_WEAPON_SIMPLE_MELEE_TWO_HANDED_PLUS_1 = [\
	const_proto_weapon.PROTO_WEAPON_SPEAR_PLUS_1 \
	, ]

PROTOS_WEAPON_SIMPLE_MELEE_PLUS_1 = PROTOS_WEAPON_SIMPLE_MELEE_LIGHT_PLUS_1 + PROTOS_WEAPON_SIMPLE_MELEE_ONE_HANDED_PLUS_1 + PROTOS_WEAPON_SIMPLE_MELEE_TWO_HANDED_PLUS_1

PROTOS_WEAPON_SIMPLE_RANGED_PLUS_1 = list()

PROTOS_WEAPON_SIMPLE_PLUS_1 = PROTOS_WEAPON_SIMPLE_MELEE_PLUS_1# + PROTOS_WEAPON_SIMPLE_RANGED_PLUS_1

PROTOS_WEAPON_MARTIAL_MELEE_LIGHT_PLUS_1 = [\
	const_proto_weapon.PROTO_WEAPON_SHORTSWORD_PLUS_1 \
	, ]

PROTOS_WEAPON_MARTIAL_MELEE_ONE_HANDED_PLUS_1 = [\
	const_proto_weapon.PROTO_BATTLEAXE_PLUS_1 \
	, const_proto_weapon.PROTO_LONGSWORD_PLUS_1 \
	, const_proto_weapon.PROTO_SCIMITAR_PLUS_1 \
	, const_proto_weapon.PROTO_WEAPON_WARHAMMER_PLUS_1 \
	]

PROTOS_WEAPON_MARTIAL_MELEE_TWO_HANDED_PLUS_1 = [\
	const_proto_weapon.PROTO_WEAPON_FALCHION_PLUS_1 \
	, const_proto_weapon.PROTO_WEAPON_GREATAXE_PLUS_1 \
	, const_proto_weapon.PROTO_WEAPON_GREATSWORD_PLUS_1 \
	, const_proto_weapon.PROTO_WEAPON_GLAIVE_PLUS_1 \
	]

PROTOS_WEAPON_MARTIAL_MELEE_PLUS_1 = PROTOS_WEAPON_MARTIAL_MELEE_LIGHT_PLUS_1 + PROTOS_WEAPON_MARTIAL_MELEE_ONE_HANDED_PLUS_1 + PROTOS_WEAPON_MARTIAL_MELEE_TWO_HANDED_PLUS_1

PROTOS_WEAPON_MARTIAL_RANGED_PLUS_1 = [\
	const_proto_weapon.PROTO_WEAPON_LONGBOW_PLUS_1 \
	, const_proto_weapon.PROTO_WEAPON_SHORTBOW_PLUS_1 \
	, const_proto_weapon.PROTO_AMMO_ARROW_QUIVER \
	]

PROTOS_WEAPON_MARTIAL_PLUS_1 = PROTOS_WEAPON_MARTIAL_MELEE_PLUS_1 + PROTOS_WEAPON_MARTIAL_RANGED_PLUS_1

PROTOS_WEAPON_EXOTIC_MELEE_LIGHT_PLUS_1 = list()

PROTOS_WEAPON_EXOTIC_MELEE_ONE_HANDED_PLUS_1 = [\
	const_proto_weapon.PROTO_WEAPON_SWORD_BASTARD_PLUS_1 \
	, ]

PROTOS_WEAPON_EXOTIC_MELEE_TWO_HANDED_PLUS_1 = [\
	const_proto_weapon.PROTO_WEAPON_SPIKED_CHAIN_PLUS_1 \
	, ]

PROTOS_WEAPON_EXOTIC_MELEE_PLUS_1 = PROTOS_WEAPON_EXOTIC_MELEE_LIGHT_PLUS_1 + PROTOS_WEAPON_EXOTIC_MELEE_ONE_HANDED_PLUS_1 + PROTOS_WEAPON_EXOTIC_MELEE_TWO_HANDED_PLUS_1

PROTOS_WEAPON_EXOTIC_RANGED_PLUS_1 = [\
	const_proto_weapon.PROTO_WEAPON_CROSSBOW_REPEATING_LIGHT_PLUS_1 \
	, ]

PROTOS_WEAPON_EXOTIC_PLUS_1 = PROTOS_WEAPON_EXOTIC_MELEE_PLUS_1 + PROTOS_WEAPON_EXOTIC_RANGED_PLUS_1

PROTOS_WEAPON_PLUS_1 = PROTOS_WEAPON_SIMPLE_PLUS_1 + PROTOS_WEAPON_MARTIAL_PLUS_1+ PROTOS_WEAPON_EXOTIC_PLUS_1

#==============================================================
# PLUS_2

PROTOS_WEAPON_SIMPLE_MELEE_LIGHT_PLUS_2 = [\
	const_proto_weapon.PROTO_WEAPON_DAGGER_PLUS_2 \
	, ]

PROTOS_WEAPON_SIMPLE_MELEE_ONE_HANDED_PLUS_2 = []

PROTOS_WEAPON_SIMPLE_MELEE_TWO_HANDED_PLUS_2 = [\
	const_proto_weapon.PROTO_WEAPON_LONGSPEAR_PLUS_2 \
	, ]

PROTOS_WEAPON_SIMPLE_MELEE_PLUS_2 = PROTOS_WEAPON_SIMPLE_MELEE_LIGHT_PLUS_2 + PROTOS_WEAPON_SIMPLE_MELEE_ONE_HANDED_PLUS_2 + PROTOS_WEAPON_SIMPLE_MELEE_TWO_HANDED_PLUS_2

PROTOS_WEAPON_SIMPLE_RANGED_PLUS_2 = []

PROTOS_WEAPON_SIMPLE_PLUS_2 = PROTOS_WEAPON_SIMPLE_MELEE_PLUS_2 + PROTOS_WEAPON_SIMPLE_RANGED_PLUS_2

PROTOS_WEAPON_MARTIAL_MELEE_LIGHT_PLUS_2 = [\
	const_proto_weapon.PROTO_WEAPON_KUKRI_PLUS_2 \
	, const_proto_weapon.PROTO_WEAPON_SHORTSWORD_PLUS_2 \
	]

PROTOS_WEAPON_MARTIAL_MELEE_ONE_HANDED_PLUS_2 = [\
	const_proto_weapon.PROTO_FLAIL_PLUS_2 \
	, const_proto_weapon.PROTO_LONGSWORD_PLUS_2 \
	, const_proto_weapon.PROTO_RAPIER_PLUS_2 \
	, const_proto_weapon.PROTO_SCIMITAR_PLUS_2 \
	, const_proto_weapon.PROTO_WEAPON_WARHAMMER_PLUS_2 \
	]

PROTOS_WEAPON_MARTIAL_MELEE_TWO_HANDED_PLUS_2 = [\
	const_proto_weapon.PROTO_WEAPON_FALCHION_PLUS_2 \
	, const_proto_weapon.PROTO_WEAPON_GREATAXE_PLUS_2 \
	, const_proto_weapon.PROTO_WEAPON_HALBERD_PLUS_2 \
	]

PROTOS_WEAPON_MARTIAL_MELEE_PLUS_2 = PROTOS_WEAPON_MARTIAL_MELEE_LIGHT_PLUS_2 + PROTOS_WEAPON_MARTIAL_MELEE_ONE_HANDED_PLUS_2 + PROTOS_WEAPON_MARTIAL_MELEE_TWO_HANDED_PLUS_2

PROTOS_WEAPON_MARTIAL_RANGED_PLUS_2 = [\
	const_proto_weapon.PROTO_WEAPON_LONGBOW_PLUS_2 \
	, ]

PROTOS_WEAPON_MARTIAL_PLUS_2 = PROTOS_WEAPON_MARTIAL_MELEE_PLUS_2 + PROTOS_WEAPON_MARTIAL_RANGED_PLUS_2

PROTOS_WEAPON_EXOTIC_MELEE_LIGHT_PLUS_2 = []

PROTOS_WEAPON_EXOTIC_MELEE_ONE_HANDED_PLUS_2 = [\
	const_proto_weapon.PROTO_WEAPON_SWORD_BASTARD_PLUS_2 \
	, const_proto_weapon.PROTO_WEAPON_WARAXE_DWARVEN_PLUS_2 \
	]

PROTOS_WEAPON_EXOTIC_MELEE_TWO_HANDED_PLUS_2 = [\
	const_proto_weapon.PROTO_WEAPON_SPIKED_CHAIN_PLUS_2 \
	, const_proto_weapon.PROTO_WEAPON_HAMMER_GNOME_HOOKED_PLUS_2 \
	]

PROTOS_WEAPON_EXOTIC_MELEE_PLUS_2 = PROTOS_WEAPON_EXOTIC_MELEE_LIGHT_PLUS_2 + PROTOS_WEAPON_EXOTIC_MELEE_ONE_HANDED_PLUS_2 + PROTOS_WEAPON_EXOTIC_MELEE_TWO_HANDED_PLUS_2

PROTOS_WEAPON_EXOTIC_RANGED_PLUS_2 = []

PROTOS_WEAPON_EXOTIC_PLUS_2 = PROTOS_WEAPON_EXOTIC_MELEE_PLUS_2 + PROTOS_WEAPON_EXOTIC_RANGED_PLUS_2

PROTOS_WEAPON_PLUS_2 = PROTOS_WEAPON_SIMPLE_PLUS_2 + PROTOS_WEAPON_MARTIAL_PLUS_2 + PROTOS_WEAPON_EXOTIC_PLUS_2

#==============================================================
# PROP_2

PROTOS_WEAPON_SIMPLE_MELEE_LIGHT_PROP_2 = []
PROTOS_WEAPON_SIMPLE_MELEE_ONE_HANDED_PROP_2 = []
PROTOS_WEAPON_SIMPLE_MELEE_TWO_HANDED_PROP_2 = []
PROTOS_WEAPON_SIMPLE_MELEE_PROP_2 = PROTOS_WEAPON_SIMPLE_MELEE_LIGHT_PROP_2 + PROTOS_WEAPON_SIMPLE_MELEE_ONE_HANDED_PROP_2 + PROTOS_WEAPON_SIMPLE_MELEE_TWO_HANDED_PROP_2

PROTOS_WEAPON_SIMPLE_RANGED_PROP_2 = [\
	const_proto_weapon.PROTO_WEAPON_CROSSBOW_LIGHT_PLUS_1_FROST \
	, const_proto_weapon.PROTO_WEAPON_CROSSBOW_LIGHT_PLUS_1_FLAMING \
	, const_proto_weapon.PROTO_WEAPON_CROSSBOW_LIGHT_PLUS_1_SHOCK \
	]
PROTOS_WEAPON_SIMPLE_PROP_2 = PROTOS_WEAPON_SIMPLE_MELEE_PROP_2 + PROTOS_WEAPON_SIMPLE_RANGED_PROP_2

PROTOS_WEAPON_MARTIAL_MELEE_LIGHT_PROP_2 = []
PROTOS_WEAPON_MARTIAL_MELEE_ONE_HANDED_PROP_2 = [\
	const_proto_weapon.PROTO_LONGSWORD_PLUS_2_FLAMING
	, ]
PROTOS_WEAPON_MARTIAL_MELEE_TWO_HANDED_PROP_2 = []
PROTOS_WEAPON_MARTIAL_MELEE_PROP_2 = PROTOS_WEAPON_MARTIAL_MELEE_LIGHT_PROP_2 + PROTOS_WEAPON_MARTIAL_MELEE_ONE_HANDED_PROP_2 + PROTOS_WEAPON_MARTIAL_MELEE_TWO_HANDED_PROP_2

PROTOS_WEAPON_MARTIAL_RANGED_PROP_2 = [const_proto_weapon.PROTO_WEAPON_LONGBOW_PLUS_1_FLAMING\
	, const_proto_weapon.PROTO_WEAPON_LONGBOW_PLUS_1_FROST\
	, ]
PROTOS_WEAPON_MARTIAL_PROP_2 = PROTOS_WEAPON_MARTIAL_MELEE_PROP_2 + PROTOS_WEAPON_MARTIAL_RANGED_PROP_2
PROTOS_WEAPON_EXOTIC_MELEE_LIGHT_PROP_2 = []
PROTOS_WEAPON_EXOTIC_MELEE_ONE_HANDED_PROP_2 = []
PROTOS_WEAPON_EXOTIC_MELEE_TWO_HANDED_PROP_2 = [\
	const_proto_weapon.PROTO_WEAPON_SPIKED_CHAIN_PLUS_1_FLAMING
	, ]
PROTOS_WEAPON_EXOTIC_MELEE_PROP_2 = PROTOS_WEAPON_EXOTIC_MELEE_LIGHT_PROP_2 + PROTOS_WEAPON_EXOTIC_MELEE_ONE_HANDED_PROP_2 + PROTOS_WEAPON_EXOTIC_MELEE_TWO_HANDED_PROP_2
PROTOS_WEAPON_EXOTIC_RANGED_PROP_2 = []
PROTOS_WEAPON_EXOTIC_PROP_2 = PROTOS_WEAPON_EXOTIC_MELEE_PROP_2 + PROTOS_WEAPON_EXOTIC_RANGED_PROP_2

PROTOS_WEAPON_PROP_2 = PROTOS_WEAPON_SIMPLE_PROP_2 + PROTOS_WEAPON_MARTIAL_PROP_2 + PROTOS_WEAPON_EXOTIC_PROP_2

PROTOS_WEAPON_MINOR = PROTOS_WEAPON_PLUS_1 + PROTOS_WEAPON_PLUS_2 + PROTOS_WEAPON_PROP_2

#==============================================================
# PROP_3

PROTOS_WEAPON_SIMPLE_MELEE_LIGHT_PROP_3 = []
PROTOS_WEAPON_SIMPLE_MELEE_ONE_HANDED_PROP_3 = [\
	const_proto_weapon.PROTO_WEAPON_MACE_HEAVY_PLUS_1_HOLY \
	, const_proto_weapon.PROTO_WEAPON_MACE_HEAVY_PLUS_1_UNHOLY \
	]

PROTOS_WEAPON_SIMPLE_MELEE_TWO_HANDED_PROP_3 = []

PROTOS_WEAPON_SIMPLE_MELEE_PROP_3 = PROTOS_WEAPON_SIMPLE_MELEE_LIGHT_PROP_3 + PROTOS_WEAPON_SIMPLE_MELEE_ONE_HANDED_PROP_3 + PROTOS_WEAPON_SIMPLE_MELEE_TWO_HANDED_PROP_3

PROTOS_WEAPON_SIMPLE_RANGED_PROP_3 = [\
	const_proto_weapon.PROTO_WEAPON_CROSSBOW_HEAVY_PLUS_1_HOLY \
	, const_proto_weapon.PROTO_WEAPON_CROSSBOW_HEAVY_PLUS_1_UNHOLY \
	, const_proto_weapon.PROTO_WEAPON_CROSSBOW_LIGHT_PLUS_1_HOLY \
	, const_proto_weapon.PROTO_WEAPON_CROSSBOW_LIGHT_PLUS_1_UNHOLY \
	, const_proto_weapon.PROTO_WEAPON_CROSSBOW_LIGHT_PLUS_1_AXIOMATIC \
	, const_proto_weapon.PROTO_WEAPON_CROSSBOW_LIGHT_PLUS_1_ANARCHIC
	]

PROTOS_WEAPON_SIMPLE_PROP_3 = PROTOS_WEAPON_SIMPLE_MELEE_PROP_3 + PROTOS_WEAPON_SIMPLE_RANGED_PROP_3

PROTOS_WEAPON_MARTIAL_MELEE_LIGHT_PROP_3 = []

PROTOS_WEAPON_MARTIAL_MELEE_ONE_HANDED_PROP_3 = [\
	const_proto_weapon.PROTO_LONGSWORD_PLUS_1_HOLY
	, ]

PROTOS_WEAPON_MARTIAL_MELEE_TWO_HANDED_PROP_3 = [\
	const_proto_weapon.PROTO_WEAPON_GREATAXE_PLUS_1_HOLY \
	, const_proto_weapon.PROTO_WEAPON_RANSEUR_PLUS_1_HOLY
	]

PROTOS_WEAPON_MARTIAL_MELEE_PROP_3 = PROTOS_WEAPON_MARTIAL_MELEE_LIGHT_PROP_3 + PROTOS_WEAPON_MARTIAL_MELEE_ONE_HANDED_PROP_3 + PROTOS_WEAPON_MARTIAL_MELEE_TWO_HANDED_PROP_3

PROTOS_WEAPON_MARTIAL_RANGED_PROP_3 = []

PROTOS_WEAPON_MARTIAL_PROP_3 = PROTOS_WEAPON_MARTIAL_MELEE_PROP_3 + PROTOS_WEAPON_MARTIAL_RANGED_PROP_3

PROTOS_WEAPON_EXOTIC_MELEE_LIGHT_PROP_3 = []

PROTOS_WEAPON_EXOTIC_MELEE_ONE_HANDED_PROP_3 = [\
	const_proto_weapon.PROTO_WEAPON_SWORD_BASTARD_PLUS_1_HOLY
	, ]

PROTOS_WEAPON_EXOTIC_MELEE_TWO_HANDED_PROP_3 = [\
	const_proto_weapon.PROTO_WEAPON_SPIKED_CHAIN_PLUS_1_HOLY
	, ]

PROTOS_WEAPON_EXOTIC_MELEE_PROP_3 = PROTOS_WEAPON_EXOTIC_MELEE_LIGHT_PROP_3 + PROTOS_WEAPON_EXOTIC_MELEE_ONE_HANDED_PROP_3 + PROTOS_WEAPON_EXOTIC_MELEE_TWO_HANDED_PROP_3

PROTOS_WEAPON_EXOTIC_RANGED_PROP_3 = []

PROTOS_WEAPON_EXOTIC_PROP_3 = PROTOS_WEAPON_EXOTIC_MELEE_PROP_3 + PROTOS_WEAPON_EXOTIC_RANGED_PROP_3

PROTOS_WEAPON_PROP_3 = PROTOS_WEAPON_SIMPLE_PROP_3 + PROTOS_WEAPON_MARTIAL_PROP_3 + PROTOS_WEAPON_EXOTIC_PROP_3

#==============================================================
# PLUS_3

PROTOS_WEAPON_SIMPLE_MELEE_LIGHT_PLUS_3 = []
PROTOS_WEAPON_SIMPLE_MELEE_ONE_HANDED_PLUS_3 = []
PROTOS_WEAPON_SIMPLE_MELEE_TWO_HANDED_PLUS_3 = []
PROTOS_WEAPON_SIMPLE_MELEE_PLUS_3 = PROTOS_WEAPON_SIMPLE_MELEE_LIGHT_PLUS_3 + PROTOS_WEAPON_SIMPLE_MELEE_ONE_HANDED_PLUS_3 + PROTOS_WEAPON_SIMPLE_MELEE_TWO_HANDED_PLUS_3
PROTOS_WEAPON_SIMPLE_RANGED_PLUS_3 = []
PROTOS_WEAPON_SIMPLE_PLUS_3 = PROTOS_WEAPON_SIMPLE_MELEE_PLUS_3 + PROTOS_WEAPON_SIMPLE_RANGED_PLUS_3
PROTOS_WEAPON_MARTIAL_MELEE_LIGHT_PLUS_3 = []

PROTOS_WEAPON_MARTIAL_MELEE_ONE_HANDED_PLUS_3 = [\
	const_proto_weapon.PROTO_LONGSWORD_PLUS_3 \
	, ]

PROTOS_WEAPON_MARTIAL_MELEE_TWO_HANDED_PLUS_3 = []
PROTOS_WEAPON_MARTIAL_MELEE_PLUS_3 = PROTOS_WEAPON_MARTIAL_MELEE_LIGHT_PLUS_3 + PROTOS_WEAPON_MARTIAL_MELEE_ONE_HANDED_PLUS_3 + PROTOS_WEAPON_MARTIAL_MELEE_TWO_HANDED_PLUS_3
PROTOS_WEAPON_MARTIAL_RANGED_PLUS_3 = []
PROTOS_WEAPON_MARTIAL_PLUS_3 = PROTOS_WEAPON_MARTIAL_MELEE_PLUS_3 + PROTOS_WEAPON_MARTIAL_RANGED_PLUS_3
PROTOS_WEAPON_EXOTIC_MELEE_LIGHT_PLUS_3 = []
PROTOS_WEAPON_EXOTIC_MELEE_ONE_HANDED_PLUS_3 = []
PROTOS_WEAPON_EXOTIC_MELEE_TWO_HANDED_PLUS_3 = []
PROTOS_WEAPON_EXOTIC_MELEE_PLUS_3 = PROTOS_WEAPON_EXOTIC_MELEE_LIGHT_PLUS_3 + PROTOS_WEAPON_EXOTIC_MELEE_ONE_HANDED_PLUS_3 + PROTOS_WEAPON_EXOTIC_MELEE_TWO_HANDED_PLUS_3
PROTOS_WEAPON_EXOTIC_RANGED_PLUS_3 = []
PROTOS_WEAPON_EXOTIC_PLUS_3 = PROTOS_WEAPON_EXOTIC_MELEE_PLUS_3 + PROTOS_WEAPON_EXOTIC_RANGED_PLUS_3

PROTOS_WEAPON_PLUS_3 = PROTOS_WEAPON_SIMPLE_PLUS_3 + PROTOS_WEAPON_MARTIAL_PLUS_3 + PROTOS_WEAPON_EXOTIC_PLUS_3
#==============================================================
# PROP_3

PROTOS_WEAPON_SIMPLE_MELEE_LIGHT_PROP_3 = []
PROTOS_WEAPON_SIMPLE_MELEE_ONE_HANDED_PROP_3 = []
PROTOS_WEAPON_SIMPLE_MELEE_TWO_HANDED_PROP_3 = []
PROTOS_WEAPON_SIMPLE_MELEE_PROP_3 = PROTOS_WEAPON_SIMPLE_MELEE_LIGHT_PROP_3 + PROTOS_WEAPON_SIMPLE_MELEE_ONE_HANDED_PROP_3 + PROTOS_WEAPON_SIMPLE_MELEE_TWO_HANDED_PROP_3
PROTOS_WEAPON_SIMPLE_RANGED_PROP_3 = []
PROTOS_WEAPON_SIMPLE_PROP_3 = PROTOS_WEAPON_SIMPLE_MELEE_PROP_3 + PROTOS_WEAPON_SIMPLE_RANGED_PROP_3
PROTOS_WEAPON_MARTIAL_MELEE_LIGHT_PROP_3 = []

PROTOS_WEAPON_MARTIAL_MELEE_ONE_HANDED_PROP_3 = [\
	const_proto_weapon.PROTO_LONGSWORD_PLUS_2_FLAMING \
	, ]

PROTOS_WEAPON_MARTIAL_MELEE_TWO_HANDED_PROP_3 = []
PROTOS_WEAPON_MARTIAL_MELEE_PROP_3 = PROTOS_WEAPON_MARTIAL_MELEE_LIGHT_PROP_3 + PROTOS_WEAPON_MARTIAL_MELEE_ONE_HANDED_PROP_3 + PROTOS_WEAPON_MARTIAL_MELEE_TWO_HANDED_PROP_3
PROTOS_WEAPON_MARTIAL_RANGED_PROP_3 = [\
	const_proto_weapon.PROTO_WEAPON_LONGBOW_PLUS_2_FROST \
	, ]
PROTOS_WEAPON_MARTIAL_PROP_3 = PROTOS_WEAPON_MARTIAL_MELEE_PROP_3 + PROTOS_WEAPON_MARTIAL_RANGED_PROP_3
PROTOS_WEAPON_EXOTIC_MELEE_LIGHT_PROP_3 = []
PROTOS_WEAPON_EXOTIC_MELEE_ONE_HANDED_PROP_3 = []
PROTOS_WEAPON_EXOTIC_MELEE_TWO_HANDED_PROP_3 = []
PROTOS_WEAPON_EXOTIC_MELEE_PROP_3 = PROTOS_WEAPON_EXOTIC_MELEE_LIGHT_PROP_3 + PROTOS_WEAPON_EXOTIC_MELEE_ONE_HANDED_PROP_3 + PROTOS_WEAPON_EXOTIC_MELEE_TWO_HANDED_PROP_3
PROTOS_WEAPON_EXOTIC_RANGED_PROP_3 = []
PROTOS_WEAPON_EXOTIC_PROP_3 = PROTOS_WEAPON_EXOTIC_MELEE_PROP_3 + PROTOS_WEAPON_EXOTIC_RANGED_PROP_3

PROTOS_WEAPON_PROP_3 = PROTOS_WEAPON_SIMPLE_PROP_3 + PROTOS_WEAPON_MARTIAL_PROP_3 + PROTOS_WEAPON_EXOTIC_PROP_3
#==============================================================
# PLUS_4

PROTOS_WEAPON_SIMPLE_MELEE_LIGHT_PLUS_4 = []
PROTOS_WEAPON_SIMPLE_MELEE_ONE_HANDED_PLUS_4 = []
PROTOS_WEAPON_SIMPLE_MELEE_TWO_HANDED_PLUS_4 = []
PROTOS_WEAPON_SIMPLE_MELEE_PLUS_4 = PROTOS_WEAPON_SIMPLE_MELEE_LIGHT_PLUS_4 + PROTOS_WEAPON_SIMPLE_MELEE_ONE_HANDED_PLUS_4 + PROTOS_WEAPON_SIMPLE_MELEE_TWO_HANDED_PLUS_4
PROTOS_WEAPON_SIMPLE_RANGED_PLUS_4 = []
PROTOS_WEAPON_SIMPLE_PLUS_4 = PROTOS_WEAPON_SIMPLE_MELEE_PLUS_4 + PROTOS_WEAPON_SIMPLE_RANGED_PLUS_4
PROTOS_WEAPON_MARTIAL_MELEE_LIGHT_PLUS_4 = []

PROTOS_WEAPON_MARTIAL_MELEE_ONE_HANDED_PLUS_4 = [\
	const_proto_weapon.PROTO_LONGSWORD_PLUS_4 \
	, ]

PROTOS_WEAPON_MARTIAL_MELEE_TWO_HANDED_PLUS_4 = []
PROTOS_WEAPON_MARTIAL_MELEE_PLUS_4 = PROTOS_WEAPON_MARTIAL_MELEE_LIGHT_PLUS_4 + PROTOS_WEAPON_MARTIAL_MELEE_ONE_HANDED_PLUS_4 + PROTOS_WEAPON_MARTIAL_MELEE_TWO_HANDED_PLUS_4
PROTOS_WEAPON_MARTIAL_RANGED_PLUS_4 = []
PROTOS_WEAPON_MARTIAL_PLUS_4 = PROTOS_WEAPON_MARTIAL_MELEE_PLUS_4 + PROTOS_WEAPON_MARTIAL_RANGED_PLUS_4
PROTOS_WEAPON_EXOTIC_MELEE_LIGHT_PLUS_4 = []
PROTOS_WEAPON_EXOTIC_MELEE_ONE_HANDED_PLUS_4 = []
PROTOS_WEAPON_EXOTIC_MELEE_TWO_HANDED_PLUS_4 = []
PROTOS_WEAPON_EXOTIC_MELEE_PLUS_4 = PROTOS_WEAPON_EXOTIC_MELEE_LIGHT_PLUS_4 + PROTOS_WEAPON_EXOTIC_MELEE_ONE_HANDED_PLUS_4 + PROTOS_WEAPON_EXOTIC_MELEE_TWO_HANDED_PLUS_4
PROTOS_WEAPON_EXOTIC_RANGED_PLUS_4 = []
PROTOS_WEAPON_EXOTIC_PLUS_4 = PROTOS_WEAPON_EXOTIC_MELEE_PLUS_4 + PROTOS_WEAPON_EXOTIC_RANGED_PLUS_4

PROTOS_WEAPON_PLUS_4 = PROTOS_WEAPON_SIMPLE_PLUS_4 + PROTOS_WEAPON_MARTIAL_PLUS_4 + PROTOS_WEAPON_EXOTIC_PLUS_4

PROTOS_WEAPON_MEDIUM = PROTOS_WEAPON_PLUS_4 + PROTOS_WEAPON_PLUS_3 + PROTOS_WEAPON_PROP_3