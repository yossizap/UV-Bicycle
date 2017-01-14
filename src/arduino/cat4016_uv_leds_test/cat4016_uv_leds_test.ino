#include "cat4016.h"

#define LEDS_COUNT		(32)

uint8_t leds_buffer[(LEDS_COUNT + 7) / 8] = {0};


void refresh_leds() {
	cat4016_write(leds_buffer, sizeof(leds_buffer));
}

void led_pattern() {
	static uint8_t i = 0;
	if (i)
		leds_buffer[(i - 1) / 8] |= 1 << ((i - 1) % 8);
	else
		memset(leds_buffer, 0, sizeof(leds_buffer));
	refresh_leds();

	if (++i > LEDS_COUNT) i = 0;
}

void setup() {
	cat4016_setup();
}

void loop() {
	led_pattern();
	delay(100);
}
