# scroller demo

from fonts import JONNY_FIVE
import picounicorn
from time import sleep
import math
import framebuf

FRAMEBUFFER_WIDTH = 100
FRAMEBUFFER_HEIGHT = 7

picounicorn.init()

class Scroller():
 
    buffer = None
    speed = 1
    offset = 0
    gap = 1
    hue = 1.0
    saturation = 1.0
    brightness = 1.0
    position = 100

    def hsv2rgb(self, hue, sat, val):
        """ Returns the RGB of Hue Saturation and Brightnes values """
    
        i = math.floor(hue * 6)
        f = hue * 6 - i
        p = val * (1 - sat)
        q = val * (1 - f * sat)
        t = val * (1 - (1 - f) * sat)

        r, g, b = [
            (val, t, p),
            (q, val, p),
            (p, val, t),
            (p, q, val),
            (t, p, val),
            (val, p, q),
        ][int(i % 6)]
        r = int(r*255)
        g = int(g*255)
        b = int(b*255)
        
        return r, g, b
    
    def rgb2hsv(self, r:int, g:int, b:int):
        """ Returns the Hue Saturation and Value of RGB values """
        h = 0
        s = 0
        v = 0
        # constrain the values to the range 0 to 1
        r_normal, g_normal, b_normal,  = r / 255, g / 255, b / 255
        cmax = max(r_normal, g_normal, b_normal)
        cmin = min(r_normal, g_normal, b_normal)
        delta = cmax - cmin
        
        # Hue calculation
        if(delta ==0):
            h = 0
        elif (cmax == r_normal):
            h = (60 * (((g_normal - b_normal) / delta) % 6))
        elif (cmax == g_normal):
            h = (60 * (((b_normal - r_normal) / delta) + 2))
        elif (cmax == b_normal):
            h = (60 * (((r_normal - g_normal) / delta) + 4))
        
        # Saturation calculation
        if cmax== 0:
            s = 0
        else:
            s = delta / cmax
            
        # Value calculation
        v = cmax

        return h, s, v 
    
    def clear(self):
        for col in range(16):
            for row in range(7):
                picounicorn.set_pixel(col, row, 0, 0, 0)
        
    def zfill(self, text, digits):
        """ fills a number string with leading zeros"""
        filled_text = ''
        str_length = len(text)
        zeros_to_add = digits - str_length
        
        if str_length > 0:
            zeros = ""
            for _ in range(zeros_to_add):
                zeros= zeros + "0"
        filled_text = zeros + text
#         print(f'text:{text}, digits: {digits}, filled_text: {filled_text}')
        return filled_text
        
    def draw_char_to_frame(self, character, frame, font, glyph, pos):
        length = font.widths.get(glyph)
        
#         print(f'length is:{length}')
        for row in range(0,5):
            char = str(bin(character[row]))
#             print(f'character: {character}, char: {char}')
            
            for col in range (0,length):
                x = col+self.offset+pos
                y = row+1
                
                # clear gap
                if x+1 < 16 and x+1 > -1:
                    frame.pixel(x+1,y,1)
#                     picounicorn.set_pixel(x+1, y, 0, 0, 0)
                
                # write pixel
                if x < 16 and x > -1:
                    character_string = str(bin(character[row])).replace('0b','')
                    character_string = self.zfill(character_string,length)
                    
#                     print(f'char string: {character_string}')
                    if character_string[col] == '1':
#                         picounicorn.set_pixel(x, y, r, g, b)
                        frame.pixel(x,y,1)
                        
                    else:
#                         picounicorn.set_pixel(x, y, 0, 0, 0)
                        frame.pixel(x,y,0)
        
        self.offset += length + self.gap
        self.frame = frame
#         return frame
        
    def update(self, position):
#         self.position -= 1
        self.position = position
        if self.position <0:
            self.position = 100
        self.show_frame(position)
        print(f"position is: {self.position}")
    
    def build_frame(self,font, message):
        """ returns a frame buffer to be displayed by show_frame """
        frame = framebuf.FrameBuffer(bytearray(100 * 7 * 1), 100, 7, framebuf.MONO_HMSB)
        
        for character in message:

            if character in font.characters:

                self.draw_char_to_frame(font.characters.get(character), frame, font, glyph=character, pos=1)                
       
        self.offset = 0
        
        self.frame = frame


    def show_frame(self,pos):
        frame = self.frame
#         pos = self.position
    
        for row in range(FRAMEBUFFER_HEIGHT):
            for col in range(FRAMEBUFFER_WIDTH):
                print(f'col:{col}, row:{row}, position{pos}')
                if col+pos < FRAMEBUFFER_WIDTH+pos and col+pos > 0:
                    if frame.pixel(col,row) == 1:
                        print(f'col: {col},row:{row}, pos:{pos}')
                        picounicorn.set_pixel(col+pos,row,255,255,255)
                    
    def display_character(self, character, glyph, pos, font):
        r,g,b = self.hsv2rgb(self.hue, self.saturation, self.brightness)
        
        #find the max length of the string
#         length = self.__find_character_width(character)
 
#         print(f'widths: {font.widths.get(character)}')
        length = font.widths.get(glyph)
        
#         print(f'length is:{length}')
        for row in range(0,5):
            char = str(bin(character[row]))
#             print(f'character: {character}, char: {char}')
            
            for col in range (0,length):
                x = col+self.offset+pos
                y = row+1
                
                # clear gap
                if x+1 < 16 and x+1 > -1:
                    picounicorn.set_pixel(x+1, y, 0, 0, 0)
                
                # write pixel
                if x < 16 and x > -1:
                    character_string = str(bin(character[row])).replace('0b','')
                    character_string = self.zfill(character_string,length)
                    
#                     print(f'char string: {character_string}')
                    if character_string[col] == '1':
                        picounicorn.set_pixel(x, y, r, g, b)
                        
                    else:
                        picounicorn.set_pixel(x, y, 0, 0, 0)
        
        self.offset += length + self.gap
       
    
    def show_message(self, message, position, hue:None, font):
        if hue is None:
            hue = 1.0
        self.hue = hue    
#         print(f"message is {message}")
        for character in message:
#             print(character)
            if character in font.characters:
#                 print(f"Character: {character}")
                self.display_character(font.characters.get(character), character, position, font)                
#            
        self.offset = 0
    

