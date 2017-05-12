#ifndef GRAPHICS_H
#define GRAPHICS_H

#include "leds.h"

#define FONT_HEIGHT			(0)
#define FONT_FIRST_CHAR		(1)
#define FONT_CHAR_COUNT 	(2)
#define FONT_TABLE	    	(3)
#define FONT_TABLE_ROWS 	(3)
#define FONT_TABLE_MSB  	(1)
#define FONT_TABLE_LSB  	(2)

#define BITMAP_WIDTH  0
#define BITMAP_HEIGHT 1
#define BITMAP_TYPE   2
#define BITMAP_TABLE  3

#define fontbyte(x)   pgm_read_byte(&_font[x])  

uint8_t * _font = NULL;
uint8_t _font_height;
uint8_t _font_bytes;
uint8_t _font_first_char;
uint8_t _font_char_count;
uint16_t _draw_speed_ms;
uint16_t _char_space_ms;
bool _right_to_left;


void graphics_draw_bitmap(const uint8_t * bitmap) {
	uint16_t width =  bitmap[1] | (bitmap[2] << 8);
	uint16_t height =  bitmap[3] | (bitmap[4] << 8);
	uint8_t height_bytes = (height + 7) / 8;
	uint32_t leds_bitmask;
	
	for (uint16_t w = 0; w < width; w++) {
		leds_bitmask = 0;
		for (uint8_t h = 0; h < height_bytes; h++) {
			leds_bitmask <<= 8;
			leds_bitmask |= bitmap[5 + h * width + w];
		}
		leds_write(leds_bitmask);
		delay(_draw_speed_ms);
	}

	leds_write(0);
	delay(_char_space_ms);
}

void graphics_draw_char(uint8_t ch) {
	if (ch < _font_first_char || ch >= (_font_first_char + _font_char_count))
		return;

	uint16_t index = FONT_TABLE + (ch - _font_first_char) * FONT_TABLE_ROWS; // char table index
	uint8_t width = fontbyte(index);
	uint32_t leds_bitmask;

	index = ((uint16_t)fontbyte(index + FONT_TABLE_MSB) << 8) + fontbyte(index + FONT_TABLE_LSB); // char index
	for(uint8_t x = 0; x < width; x++) {
		leds_bitmask = 0;
		for(uint8_t y = 0; y < _font_bytes; y++) {
			leds_bitmask <<= 8;
			leds_bitmask |= fontbyte(index + y + (_right_to_left ? width - x - 1 : x) * _font_bytes);
		}
		leds_write(leds_bitmask);
		delay(_draw_speed_ms);
	}

	leds_write(0);
	delay(_char_space_ms);
}

void graphics_draw_text(uint8_t * text) {
	uint8_t stl = strlen(text);
	if (stl == 0) return;
	while (stl--)
		graphics_draw_char(*text++);
}

void graphics_test() {
	uint32_t led_bitmask = (uint32_t)2 << LEDS_COUNT;

	leds_write(led_bitmask - 1);
	delay(1000);
	do {
		led_bitmask >>= 1;
		leds_write(led_bitmask);
		delay(700);
	} while (led_bitmask);
}

void graphics_set_font(uint8_t * font) {
	_font = font;
	_font_height = fontbyte(FONT_HEIGHT);
	_font_bytes = (_font_height + 7) / 8;
	_font_first_char = fontbyte(FONT_FIRST_CHAR);
	_font_char_count = fontbyte(FONT_CHAR_COUNT);
}

void graphics_set_draw(uint16_t draw_speed_ms, uint16_t char_space_ms, bool right_to_left) {
	_draw_speed_ms = draw_speed_ms;
	_char_space_ms = char_space_ms;
	_right_to_left = right_to_left;
}

#endif /* GRAPHICS_H */
