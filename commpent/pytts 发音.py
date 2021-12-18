import pyttsx3
engine = pyttsx3.init()
def onStart(name):
    print ('starting', name)
def onWord(name, location, length):
    print ('word', name, location, length)
def onEnd(name, completed):
     print ('finishing', name, completed)
     if name == 'fox':
        engine.say('What a lazy dog!', 'dog')
     elif name == 'dog':
          engine.endLoop()

engine = pyttsx3.init()
engine.say(' 你好，世界上的东西还有什么发', 'dog')
engine.startLoop()