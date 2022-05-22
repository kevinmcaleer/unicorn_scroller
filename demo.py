# Scroller Demo
# Kevin McAleer May 2022

from time import sleep
from scroller import Scroller
from fonts import JONNY_FIVE

# create a message to display
message = "Hey! @kevmac - Robot Makers"

# create a scroller 0bject
scroll = Scroller()

# set the hue colour (0 is red etc)
hue = 0

font = JONNY_FIVE()
scroll.clear()
scroll.build_frame(message=message, font=font)
while True or KeyboardInterrupt:
    for position in range(16,-100,-1):
        if hue <=1 or hue == 0:
            hue += 0.01
        else: hue = 0
#         if scroll.brightness ==1 or scroll.brightness >= 0.1:
#             scroll.brightness -= 0.1
#         else: scroll.brightness = 1

#         scroll.show_message(message, position, hue, font)
        
        scroll.show_frame(position)
        scroll.update(position)
        sleep(0.05)

scroll.clear()