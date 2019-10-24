from flask import Flask, request
from flask_cors import CORS
from syntaxer import Syntax
from CodeContainer import CodeContainer

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
  return "Hello, World!"

@app.route('/image', methods=['POST'])
def getImage():
  data = request.get_json(force=True)
  print(data)
  colors = Syntax.getPigments(data["text"], data["languaje"], data["style"])

  canvasWidth = 500
  canvasHeight = 500

  codeContainer = CodeContainer((int(data["width"]), int(data["height"])), (int(data["background_color"]["r"]), int(data["background_color"]["g"]), int(data["background_color"]["b"])), colors, int(data["text_size"]))

  y = 1
  x = 0
  for i in range(len(data["text"])):
    x, y = codeContainer.drawChar(data["text"], i, x, y)

  codeContainer.img.save("lol.jpg",quality=100) 
  return "succeso da"
  
  