#ifndef LEDS_H
#define LEDS_H

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

void leds_write(uint32_t led_bitmask) {
	union {
		uint32_t bitmask = 0;
		uint8_t buffer[4];
	} cat4016;

	for (uint8_t i = 0; i < ARRAY_SIZE(LEDS_MAPPING); i++, led_bitmask >>= 1)
		if (led_bitmask & 0x0001)
			cat4016.bitmask |= LEDS_MAPPING[i];

	cat4016_write(cat4016.buffer, sizeof(cat4016.buffer));
}

void leds_test() {
	uint32_t led_bitmask = (uint32_t)2 << ARRAY_SIZE(LEDS_MAPPING);

	leds_write(led_bitmask - 1);
	delay(1000);
	do {
		led_bitmask >>= 1;
		leds_write(led_bitmask);
		delay(700);
	} while (led_bitmask);
}

void leds_init() {
	cat4016_setup();
	leds_write(0);
}

#endif /* LEDS_H */
