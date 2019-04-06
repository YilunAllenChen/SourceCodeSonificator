import random
from psonic import *
from threading import Thread

extensionBeatMap = {
    "java": [0.5, 0.5, 1],
    "cpp": [0.25, 0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.25],
    "c": [0.25, 0.125, 0.125],
    "py": [0.25, 0.125, 0.125, 0.25, 0.25, 1.25]
}

def composer(extension):
    drumsThread = Thread(target=drums, args=(extensionBeatMap[extension],))
    drumsThread.start()

def guitar(rootNote, quality):
    use_synth(PLUCK)
    c = chord(rootNote, quality)
    while True:
        s = random.choice([0.125,0.25,0.5])
        for i in range(8):
            r = random.choice([0.125, 0.25, 1, 2])
            play(c, release = r)
            sleep(s)

def drums(sleepTime):
    while True:
        for i in sleepTime:
            sample(DRUM_BASS_HARD, rate=0.5, amp=0.5)
            sleep(i)

# drumsThread = Thread(target=drums, args=([0.25, 0.125, 0.125],))
# guitarThread = Thread(target=guitar, args=(E3, MAJOR))
# guitarThread2 = Thread(target=guitar, args=(G3, MAJOR))
# guitarThread3 = Thread(target=guitar, args=(C3, MAJOR))

# drumsThread.start()
# guitarThread.start()
# guitarThread2.start()

composer("cpp")
while True:
    pass
