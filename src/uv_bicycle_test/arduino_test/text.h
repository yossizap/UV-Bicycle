#ifndef TEXT_H
#define TEXT_H

#include "leds.h"

#define FONT_HEIGHT			(0)
#define FONT_FIRST_CHAR		(1)
#define FONT_CHAR_COUNT 	(2)
#define FONT_TABLE	    	(3)
#define FONT_TABLE_ROWS 	(3)
#define FONT_TABLE_MSB  	(1)
#define FONT_TABLE_LSB  	(2)

//{ Hebrew letters
#define ALEF		0x80
#define BET			0x81
#define GIMEL		0x82
#define DALED		0x83
#define HEY			0x84
#define VAV			0x85
#define ZAIN		0x86
#define HET			0x87
#define TET			0x88
#define YOD			0x89
#define HAF_SOFIT	0x8A
#define HAF			0x8B
#define LAMED		0x8C
#define MEM_SOFIT	0x8D
#define MEM			0x8E
#define NON_SOFIT	0x8F
#define NON			0x90
#define SAMECH		0x91
#define AIN			0x92
#define PEY_SOFIT 	0x93
#define PEY			0x94
#define ZADIK_SOFIT 0x95
#define ZADIK		0x96
#define KOF			0x97
#define REISH		0x98
#define SHEN		0x99
#define TAF			0x9A
//}


uint8_t * _font = NULL;
uint8_t _font_height;
uint8_t _font_bytes;
uint8_t _font_first_char;
uint8_t _font_char_count;
uint16_t _draw_speed_ms;
uint16_t _char_space_ms;
bool _right_to_left;

#define fontbyte(x)   pgm_read_byte(&_font[x])  

void text_draw_char(uint8_t ch) {
	if (ch < _font_first_char || ch >= (_font_first_char + _font_char_count))
		return;

	uint16_t index = FONT_TABLE + (ch - _font_first_char) * FONT_TABLE_ROWS; // char table index
	uint8_t width = fontbyte(index);
	uint16_t leds_bitmask;

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

void text_draw_text(uint8_t * text) {
	uint8_t stl = strlen(text);
	if (stl == 0) return;
	while (stl--)
		text_draw_char(*text++);
}

void text_set_font(uint8_t * font) {
	_font = font;
	_font_height = fontbyte(FONT_HEIGHT);
	_font_bytes = (_font_height + 7) / 8;
	_font_first_char = fontbyte(FONT_FIRST_CHAR);
	_font_char_count = fontbyte(FONT_CHAR_COUNT);
}

void text_set_draw(uint16_t draw_speed_ms, uint16_t char_space_ms, bool right_to_left) {
	_draw_speed_ms = draw_speed_ms;
	_char_space_ms = char_space_ms;
	_right_to_left = right_to_left;
}

#endif /* TEXT_H */
