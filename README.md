# Pico Unicorn Scroller
I've created this scroller code as I wanted to display messages across the Pimoroni Pico Unicorn Pack display, by [Pimoroni](https://shop.pimoroni.com/products/pico-unicorn-pack)

I've created a couple of files to make this super flexible:
* `scroller.py` - the class that does all the heavy lifting to display and scroll text on the display
* `fonts.py` - contains a list of fonts that you can use on the scroller (work in progress)
* `demo.py` - a simple demo of the code in action

---

**NOTE**
The `Fonts.py` is a work in progress, currently each character is individually assigned as a variable and then defined as an array of strings. There is then a ***lot*** of `if` statements
to choose which character to display. This is not efficient. Now that it works in principle, I can pack the binary digits for each character into a couple of bytes rather than strings of characters.
The `if` statements can be replaced by a `if character in fonts:` line instead and then display with a single line: `character_display(font.get(character))`.

- Make it work
- Make it right
- Make it fast
