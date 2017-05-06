arduino_test.ino:
=================

lines 6, 7, 8:
#define DRAW_SPEED_MS		(70)	/* time between draw of new led line (vertical pixels) */
#define CHAR_SPACE_MS		(90)	/* time to turn off leds after each char is draw */
#define RIGHT_TO_LEFT		(false)	/* draw the chars from left or right */

change those numbers to control the draw speed and diraction.

lines 21, 22, 23:
// leds_test(); /* run led test (all on, last to first, all off) */
_right_to_left = false; text_draw_text("Hello World"); delay(1000); /* draw english text */
_right_to_left = true; text_draw_text(HEB_HELLO_WORLD); delay(1000); /* draw hebrew text */

comment or uncomment (// befor line), for led test:
leds_test(); /* run led test (all on, last to first, all off) */
// _right_to_left = false; text_draw_text("Hello World"); delay(1000); /* draw english text */
// _right_to_left = true; text_draw_text(HEB_HELLO_WORLD); delay(1000); /* draw hebrew text */


leds.h:
=======

line 7:
// #define USE_LENS_LED

uncomment if using musium lens leds configuration (led gruop of 3)
