# scroller demo

from fonts import *
import picounicorn
from time import sleep

picounicorn.init()

class Scroller():
 
    buffer = None
    speed = 1
    offset = 0
    gap = 1
    hue = 1.0
    saturation = 1.0
    brightness = 1.0
    
    def hsv_to_rgb(self,h, s, v):
        if s == 0.0:
            return v, v, v
        i = int(h * 6.0)
        f = (h * 6.0) - i
        p = v * (1.0 - s)
        q = v * (1.0 - s * f)
        t = v * (1.0 - s * (1.0 - f))
        i = i % 6
        if i == 0:
            return int(v), int(t), int(p)
        if i == 1:
            return int(q), int(v), int(p)
        if i == 2:
            return int(p), int(v), int(t)
        if i == 3:
            return int(p), int(q), int(v)
        if i == 4:
            return int(t), int(p), int(v)
        if i == 5:
            return int(v), int(p), int(q)
    
    def clear(self):
        for col in range(16):
            for row in range(7):
                picounicorn.set_pixel(col, row, 0, 0, 0)
    
#     def init_buffer(self, buffer, width, height):
#         for row in range(0, height):
#             new_row = []
#             for col in range(0, width):
#                 new_row.append('0')
# #                 print(f'row: {row}, col:{col}')
#             buffer.append(new_row)
#         return buffer
    
    def display_character(self, character,pos):
#         if self.offset+pos < 16:
#         print(character)
        r,g,b = self.hsv_to_rgb(self.hue, self.saturation, self.brightness)
        for row in range(0,5):
            length = len(character[0])
#             print(length)
            for col in range (0,length):
                x = col+self.offset+pos
                y = row+1
                if x < 16 and x > -1:
#                     print(f"row: {row}, col: {col}, x: {x}, y: {y}, char:{character[row][col]}, pos: {pos}, offset: {self.offset}")
                    if character[row][col] == '1':
#                         r = r * 255
#                         g = g * 255
#                         b = b * 255
#                         print(f'r:{r}, g:{g}, b:{b}')
                        picounicorn.set_pixel(x, y, r, g, b)
                        
                    else:
                        picounicorn.set_pixel(x, y, 0, 0, 0)
        self.offset += len(character[0]) + self.gap
#         print(self.offset)
       
    
    def show_message(self, message, position, hue:None):
        if hue is None:
            hue = 1.0
        self.hue = hue    
#         print(f"message is {message}")
        for character in message:
#             print(character)
            if character == 'a':
                self.display_character(a, position)
            if character == 'b':
                self.display_character(b, position)
            if character == 'c':
                self.display_character(c, position)
            if character == 'd':
                self.display_character(d, position)
            if character == 'e':
                self.display_character(e, position)
            if character == 'f':
                self.display_character(f, position)
            if character == 'g':
                self.display_character(g, position)
            if character == 'h':
                self.display_character(h, position)
            if character == 'i':
                self.display_character(i, position)
            if character == 'j':
                self.display_character(j, position)
            if character == 'k':
                self.display_character(k, position)
            if character == 'l':
                self.display_character(l, position)
            if character == 'm':
                self.display_character(m, position)
            if character == 'n':
                self.display_character(n, position)
            if character == 'o':
                self.display_character(o, position)
            if character == 'p':
                self.display_character(p, position)
            if character == 'q':
                self.display_character(q, position)
            if character == 'r':
                self.display_character(r, position)
            if character == 's':
                self.display_character(s, position)
            if character == 't':
                self.display_character(t, position)
            if character == 'u':
                self.display_character(u, position)
            if character == 'v':
                self.display_character(v, position)
            if character == 'w':
                self.display_character(w, position)
            if character == 'x':
                self.display_character(x, position)
            if character == 'y':
                self.display_character(y, position)
            if character == 'z':
                self.display_character(z, position)
            if character == ' ':
                self.display_character(space, position)
            if character == '1':
                self.display_character(one, position)
                
        self.offset = 0
    
message = "abcdefghijklmnopqrstuvwxyz 1"

scroll = Scroller()
hue = 0

while True:
    for position in range(16,-len(message*(5+1)),-1):
        if hue <=1:
            hue += 0.1
        else: hue == 0
        scroll.show_message(message, position, hue)
        sleep(0.03)
        scroll.clear()
