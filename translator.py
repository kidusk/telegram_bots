from googletrans import Translator

translator = Translator()

def Translate(inp):
    return translator._translate(inp, dest="am", src="en")[0][0][0]

