from pygments import highlight
from pygments.lexers import PythonLexer, JavascriptLexer
from pygments.lexers.python import Python3Lexer
from CustomFormatter import CustomFormatter
import json 


langujes = {
  "javascript": JavascriptLexer, 
  "python": Python3Lexer, 
}
class Syntax():

    @staticmethod
    def getPigments(text, languaje, style):
        colors = highlight(text, langujes[languaje](stripnl=False, tabsize=4), CustomFormatter(style=style))
        
        return json.loads(colors)