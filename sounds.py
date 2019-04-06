import random
from psonic import *
from multiprocessing import Process
from extract import extract

extensionBeatMap = {
    "java": [0.5, 0.5, 1],
    "cpp": [0.25, 0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.25],
    "c": [0.25, 0.125, 0.125],
    "py": [0.25, 0.125, 0.125, 0.25, 0.25, 1.25]
}

def guitar(rootNote, quality):
    use_synth(PLUCK)
    c = chord(rootNote, quality)
    while True:
        s = random.choice([0.125,0.25,0.5])
        r = random.choice([0.125, 0.25, 1, 2])
        play(c, release = r)
        sleep(s)

def piano(rootNote, quality):
    use_synth(PIANO)
    c = chord(rootNote, quality)
    while True:
        s = random.choice([0.125,0.25,0.5])
        r = random.choice([0.125, 0.25, 1, 2])
        play(c, release = r)
        sleep(s)

def guitar(rootNote, quality):
    use_synth(PLUCK)
    c = chord(rootNote, quality)
    while True:
        s = random.choice([0.125,0.25,0.5])
        r = random.choice([0.125, 0.25, 1, 2])
        play(c, release = r)
        sleep(s)

keywordFuncMap = {
    "in": guitar,
    # "while":
    # "if":
    # "else":
    # "class":
    # "def":
}

def composer(extension, keywords):
    drumsProcess = Process(target=drums, args=(extensionBeatMap[extension],))
    drumsProcess.start()
    
    keyList = [*keywords]
    keyList.sort()
    for i in keyList:
        word = keywords[i]
        if "in" in word:
            guitarProcess = Process(target=keywordFuncMap["in"], args=(E3, MAJOR))
            guitarProcess.start()
            sleep(0.25)
            guitarProcess.terminate()
        
        # if 
        
        
    



def drums(sleepTime):
    while True:
        for i in sleepTime:
            sample(DRUM_BASS_HARD, rate=0.5, amp=0.5)
            sleep(i)

# drumsProcess = Process(target=drums, args=([0.25, 0.125, 0.125],))
# guitarProcess = Process(target=guitar, args=(E3, MAJOR))
# guitarProcess2 = Process(target=guitar, args=(G3, MAJOR))
# guitarProcess3 = Process(target=guitar, args=(C3, MAJOR))

# drumsProcess.start()
# guitarProcess.start()
# guitarProcess2.start()

composer("java", extract("./Grep.java"))
while True:
    pass
