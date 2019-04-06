import random
import queue
import math
from psonic import *
from multiprocessing import Process
from extract import extract

allKeywords = ['True', 'while', 'else', 'int', 'extern', 'assert', 'return', 'typedef', 'interface', 'signed', 'short', 'import', 'def', 'throw', 'native', 'transient', 'throws', 'register', 'try', 'void', 'unsigned', 'extends', 'break', 'default', 'this', 'enum', 'None', 'float', 'from', 'yield', 'False', 'boolean', 'synchronized', 'implements', 'struct', 'raise', 'case', 'double', 'await', 'continue', 'abstract', 'new', 'for', 'in', 'elif', 'super', 'goto', 'with', 'private', 'is', 'as', 'volatile', 'protected', 'and', 'not', 'pass', 'final', 'lambda', 'global', 'public', 'if', 'strictfp', 'del', 'char', 'union', 'instanceof', 'auto', 'async', '_Packed', 'byte', 'nonlocal', 'catch', 'long', 'finally', 'sizeof', 'or', 'class', 'switch', 'static', 'except', 'package', 'const','do']
extensionBeatMap = {
    "java": [0.5, 0.5, 1],
    "cpp": [0.25, 0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.125, 0.125, 0.25, 0.25],
    "c": [0.25, 0.125, 0.125],
    "py": [0.25, 0.125, 0.125, 0.25, 0.25, 1.25]
}


def generateNote():
    res = []
    for i in range(random.choice(range(2, 8))):
        res.append(random.choice([C2,C3,C4,D3,D4,E2,E3,E4,F3,G2,G3,G4,A2,A3,A4,B3]))
    return res

processQueue = queue.Queue()

def guitar(noteList):
    use_synth(PLUCK)
    while True:
        r = random.choice([0.125, 0.25, 1, 2])
        # play_pattern_timed(noteList, 2*[0.25,0.125,0.25,0.125,0.125,0.125,0.25,0.25], release=r)
        play(noteList, release=r)
        sleep(0.25)

def bell(noteList):
    use_synth(PRETTY_BELL)
    while True:
        r = random.choice([0.125, 0.25, 1, 2])
        play_pattern_timed(noteList, [0.25,0.25,0.5], release=r)


def piano(noteList):
    use_synth(PIANO)
#     # while True:
#     #     r = random.choice([0.125, 0.25, 1, 2])
#     #     play_pattern_timed(noteList, [0.5,0.25], release=r)
    t = [0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25]
    while True:
        for (i, x) in zip(t, noteList):
            r = random.choice([0.5,1])
            play(x, release=r, amp=1.5)
            sleep(i)
        
instruments = [guitar, piano, bell]


def composer(extension, keywords):
    drumsProcess = Process(target=drums, args=(extensionBeatMap[extension],))
    drumsProcess.start()
    
    keyList = [*keywords]
    for i in keyList:
        word = keywords[i]
        print(i)
        for j in range(len(allKeywords)):
            if allKeywords[j] in word:
                process = Process(target=instruments[j%3], args=(generateNote(),))
                processQueue.put(process)
                process.start()
                
                sleep(2)
            


        # if "if" in word:
        #     guitarProcess = Process(target=keywordFuncMap["in"], args=([C3, E3, G3],))
        #     processQueue.put(guitarProcess)
        #     guitarProcess.start()
        #     sleep(2)
        # if "as" in word:
        #     guitarProcess = Process(target=keywordFuncMap["in"], args=([C2],))
        #     processQueue.put(guitarProcess)
        #     guitarProcess.start()
        #     sleep(0.5)
        # if "in" in word:
        #     guitarProcess = Process(target=piano, args=(C3, MAJOR))
        #     guitarProcess.start()
        #     sleep(0.75)
        #     guitarProcess.terminate()
        size = processQueue.qsize()
        for i in range (math.ceil(size/(3 if size > 5 else 4))):
            if not processQueue.empty():
                current = processQueue.get()
                current.terminate()


def drums(sleepTime):
    while True:
        for i in sleepTime:
            sample(DRUM_BASS_HARD, amp=1.5, rate=0.5)
            sleep(i)


composer("py", extract("/Users/h339667/Documents/fixit/fixitmobile/app/src/main/java/com/honeywell/fixit/PastRequests.java"))
while True:
    pass
