#ifndef LEDS_H
#define LEDS_H

/******************************************/
// #define USE_CAT4016
/******************************************/

#ifdef USE_CAT4016
	#include "cat4016.h"

	/******************************************/
	// #define USE_LENS_LED
	/******************************************/

	#ifdef USE_LENS_LED
		#define LED_GROUP_SIZE		(3)
	#else
		#define LED_GROUP_SIZE		(2)
	#endif
	#define LED_MAPPING(index)	((((uint32_t)1 << LED_GROUP_SIZE) - 1) << (index * LED_GROUP_SIZE))

	const uint32_t LEDS_MAPPING[] = {
	#ifdef USE_LENS_LED
		LED_MAPPING(0),
		LED_MAPPING(1),
		LED_MAPPING(2),
		LED_MAPPING(3),
		LED_MAPPING(4),
		LED_MAPPING(5) << 1,
		LED_MAPPING(6) << 1,
		LED_MAPPING(7) << 1,
		LED_MAPPING(8) << 1,
		LED_MAPPING(9) << 1,
	#else
		LED_MAPPING(0),
		LED_MAPPING(11),
		LED_MAPPING(2),
		LED_MAPPING(3),
		LED_MAPPING(10),
		LED_MAPPING(5),
		LED_MAPPING(6),
		LED_MAPPING(7),
		LED_MAPPING(8),
		LED_MAPPING(9),
	#endif
	};

	#define LEDS_COUNT			(ARRAY_SIZE(LEDS_MAPPING))
#else
	#define LEDS_COUNT			(10)
#endif

void leds_write(uint32_t led_bitmask) {
#ifdef USE_CAT4016
	union {
		uint32_t bitmask = 0;
		uint8_t buffer[4];
	} cat4016;

	for (uint8_t i = 0; i < LEDS_COUNT; i++, led_bitmask >>= 1)
		if (led_bitmask & 0x0001)
			cat4016.bitmask |= LEDS_MAPPING[i];

	cat4016_write(cat4016.buffer, sizeof(cat4016.buffer));
#else
	PORTD = (PORTD & 0x03) | ((led_bitmask & 0x003F) << 2);
	PORTB = (PORTB & 0xF0) | ((led_bitmask & 0x03C0) >> 6);
#endif
}

void leds_init() {
#ifdef USE_CAT4016
	cat4016_setup();
#else
	DDRD |= 0xFC;	/* (2 - 7 OUTPUT) */
	DDRB |= 0x0F;	/* (8 - 11 OUTPUT) */
#endif
	leds_write(0);
}

#endif /* LEDS_H */
