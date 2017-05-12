#include "leds.h"
#include "graphics.h"
#include "heb_5x7.h"
#include "texts.h"
#include "bitmaps.h"

/******************************************/
#define DRAW_SPEED_MS		(70)		/* time between draw of new led line (vertical pixels) */
#define CHAR_SPACE_MS		(90)		/* time to turn off leds after each char is draw */
#define RIGHT_TO_LEFT		(true)		/* draw the chars from left or right */
#define SERIAL_BAUD_RATE	(115200)
/******************************************/

void setup() {
	Serial.begin(SERIAL_BAUD_RATE);
	Serial.setTimeout(50);
	leds_init();
	graphics_set_font(heb_5x7);
	graphics_set_draw(DRAW_SPEED_MS, CHAR_SPACE_MS, RIGHT_TO_LEFT);
}

void loop() {
	// graphics_test(); /* run led test (all on, last to first, all off) */
	// _right_to_left = false; graphics_draw_text("Hello World"); delay(1000); /* draw english text */
	// _right_to_left = true; graphics_draw_text(HEB_HELLO_WORLD); delay(1000); /* draw hebrew text */
	// for (uint8_t i = _font_first_char; i < (_font_first_char + _font_char_count); i++) text_draw_char(i); /* draw all font */
	// graphics_draw_bitmap(arad_paint);
	graphics_draw_text(HEB_HELLO_WORLD);
	delay(3000);
	// if (Serial.available()) leds_set(Serial.parseInt());
}
