from google.protobuf.symbol_database import Default
import pyshorteners
import eel

eel.init('web')
s=pyshorteners.Shortener()



@eel.expose
def generate_qr(data):
    
    outputText = s.tinyurl.short(data)
    
    return outputText



eel.start('index.html', size=(1000, 600))


