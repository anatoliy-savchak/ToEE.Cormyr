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