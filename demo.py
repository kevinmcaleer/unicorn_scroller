message = "subs: 6668"

scroll = Scroller()
hue = 0

while True:
    for position in range(16,-len(message*(5+1)),-1):
        if hue <=1 or hue == 0:
            hue += 0.01
        else: hue = 0
#         if scroll.brightness ==1 or scroll.brightness >= 0.1:
#             scroll.brightness -= 0.1
#         else: scroll.brightness = 1
        scroll.show_message(message, position, hue)
        sleep(0.05)
#         scroll.clear()