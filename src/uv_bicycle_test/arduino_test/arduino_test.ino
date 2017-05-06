#include "leds.h"
#include "text.h"
#include "heb_5x7.h"

/******************************************/
#define DRAW_SPEED_MS		(70)	/* time between draw of new led line (vertical pixels) */
#define CHAR_SPACE_MS		(90)	/* time to turn off leds after each char is draw */
#define RIGHT_TO_LEFT		(false)	/* draw the chars from left or right */
/******************************************/

// const uint8_t HEB_HELLO_WORLD[] = {MEM_SOFIT, LAMED, VAV, AIN, ' ', MEM_SOFIT, VAV, LAMED, SHEN, 0};
const uint8_t HEB_HELLO_WORLD[] = {SHEN, LAMED, VAV, MEM_SOFIT, ' ', AIN, VAV, LAMED, MEM_SOFIT, 0};
const uint8_t HEB_MAZAL_TOV[] = {MEM, ZAIN, LAMED, ' ', TET, VAV, BET, ' ', '!', 0};

void setup() {
	leds_init();
	text_set_font(heb_5x7);
	text_set_draw(DRAW_SPEED_MS, CHAR_SPACE_MS, RIGHT_TO_LEFT);
}

void loop() {
	leds_test(); /* run led test (all on, last to first, all off) */
	// _right_to_left = false; text_draw_text("Hello World"); delay(1000); /* draw english text */
	// _right_to_left = true; text_draw_text(HEB_HELLO_WORLD); delay(1000); /* draw hebrew text */
	for (uint8_t i = _font_first_char; i < (_font_first_char + _font_char_count); i++) text_draw_char(i); /* draw all font */
	delay(3000);
}
