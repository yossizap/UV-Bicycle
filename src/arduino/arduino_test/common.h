#ifndef COMMON_H
#define COMMON_H

#ifndef cbi
	#define cbi(sfr, bit)	(_SFR_BYTE(sfr) &= ~_BV(bit))
#endif
#ifndef sbi
	#define sbi(sfr, bit)	(_SFR_BYTE(sfr) |= _BV(bit))
#endif

#define ARRAY_SIZE(x)		(sizeof(x) / sizeof(*x))

#endif /* COMMON_H */
