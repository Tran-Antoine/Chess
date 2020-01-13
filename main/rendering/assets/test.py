from PIL import Image

img = Image.open("white/pawn.png")


new = Image.new(img.mode, img.size)
new.putdata(img.getdata())
new.save('test.png')