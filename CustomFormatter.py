from pygments.formatter import Formatter
import json
from pygments.styles import STYLE_MAP
from pygments.styles import get_all_styles


class CustomFormatter(Formatter):
    def __init__(self, **options):
        Formatter.__init__(self, **options)

        # create a dict of (start, end) tuples that wrap the
        # value of a token so that we can use it in the format
        # method later
        self.styles = {}

        # we iterate over the `_styles` attribute of a style item
        # that contains the parsed style values.
        
        for token, style in self.style:
            self.styles[token] = style

    def format(self, tokensource, outfile):
        colors = {}
        index = 0
        for ttype, value in tokensource:
            if(ttype in self.styles):
                for i in range(index, index + len(value)):
                    values = self.styles[ttype]["color"]
                    if values == None:
                        colors[i] = (0, 0, 0)
                    else: 
                        colors[i] = tuple(int(values[i:i+2], 16) for i in (0, 2, 4))
                    index += 1
        outfile.write(json.dumps(colors))
    