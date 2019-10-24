from PIL import Image, ImageDraw, ImageFont
from textutils import getTextWidth

class CodeContainer():

    def __init__(self, size: tuple, background: tuple, colors: dict, text_size: int):
        self.size = size
        self.width, self.height = size
        self.background = background
        self.colors = colors
        self.img = Image.new('RGB', self.size, self.background)
        self.draw = ImageDraw.Draw(self.img)
        self.text_size = text_size
        self.font = ImageFont.truetype("DroidSansMono.ttf", self.text_size)
        self.line = 1
        self.draw.text((self.text_size - 10, 5), str(self.line), fill=(128, 128, 128), font=self.font)

    def drawChar(self, text, charIndex, x, y, color=None):
        if(not color):
          color = (255,255,255)
          if str(charIndex) in self.colors:
              color = self.colors[str(charIndex)]

        width = getTextWidth(text[charIndex], self.text_size)

        if(y+5 >= self.height - 40 or (text[charIndex] == '\n' and  y+5+26 >= self.height - 40)):
            auxImg = Image.new('RGB', self.size, self.background)
            auxImg.paste(self.img, (0, -10))
            self.img = auxImg.copy()
            self.draw = ImageDraw.Draw(self.img)
            y -= 10
        
        if text[charIndex] == '\n':
            y += self.text_size + 10
            x = 1
            self.line += 1
            self.draw.text((self.text_size - 10, y+5), str(self.line), fill=(128, 128, 128), font=self.font)
            return x, y
        

        self.draw.text((x+self.text_size/0.4, y+5), text[charIndex], fill=tuple(color), font=self.font)
        
        x = x + width
        x += 1 

        return x, y

        
    
