# Testing implementation for goober's "this is" cog (which creates images similar to Spotify's "this is" albums)
from PIL import Image, ImageDraw, ImageFont

image = Image.new("RGB", (512, 512), 0xffffff)
image.paste((148, 255, 41), (0, round(image.size[1]/2), image.size[0], image.size[1]))

header = ImageFont.truetype("resotyc-Regular.ttf", 54)
artistfont = ImageFont.truetype("gevher-black.otf", 58)

draw = ImageDraw.Draw(image)

text = "THIS IS"
artist = "Drake"

draw.text((image.size[0]/2 - header.getlength(text)/2, 32), text, font=header, fill="black")
draw.text((image.size[0]/2 - artistfont.getlength(artist)/2, 430), artist, font=artistfont, fill="black")

artist = Image.open("image.png")
ratio = artist.height / artist.width
artist = artist.resize((360, round(360*ratio)))

spotify = Image.open("spotify.png").convert("RGBA")
spotify = spotify.resize((50,50))

(x,y) = image.size[0]//2 - artist.size[0]//2, image.size[0] // 2 - artist.size[1]//2
image.paste(artist, (x,y, x+artist.width, y+artist.height))
image.paste(spotify, (16,16, 50+16, 50+16), spotify)

image.show()
