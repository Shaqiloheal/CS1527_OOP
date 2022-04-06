class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception('Invalid file format')
        self.filename = filename

class MP3File(AudioFile):
    ext = 'mp3'
    def play(self):
        print('playing as mp3')

class WavFile(AudioFile):
    ext = 'wav'
    def play(self):
        print('playing as wav')

class Foo:
    """Duck Typing example"""
    def __init__(self, some_string):
        if not some_string.startswith('foo.'):
            raise Exception('Invalid foo thing')
        self.some_string = some_string
    
    def play(self):
        print('doing something as foo')


mp3 = MP3File('myfile.mp3')
mp3.play()

wav = WavFile('anofile.wav')
wav.play()

#nofile = MP3File('thisfile.abc')
#nofile.play()

foobar = Foo('foo.thing')
foobar.play()