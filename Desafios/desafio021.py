from pydub import AudioSegment
from pydub.playback import play

msc = AudioSegment.from_mp3('/home/gabriel/python/ex021.mp3')

play(msc)
