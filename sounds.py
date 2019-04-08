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


def generateNote(chorus):
    res = []
    list1 = [C2,C3,C4,D3,D4,E2,E3,E4,F3,G2,G3,G4,A2,A3,A4,B3]
    list2 = [Cs2,Cs3,Cs4,F2,F3,F4,Gs2,Gs3,Gs4,C2,C3,C4,]
    list3 = [Ab2,Ab3,Ab4,B2,B3,B4,Eb2,Eb3,Eb4,Gb2,Gb3,Gb4]
    lists = [list1,list2,list3]
    for i in range(random.choice(range(2, 8))):
        res.append(random.choice(lists[chorus]))
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
    chorus = (2+len(keywords))%3
    keyList = [*keywords]
    total = keyList[-1]
    print("Composing now...")

    for i in keyList:
        word = keywords[i]
        print("Progress: " + str(int(i)/int(total) * 100)[0:4] + "%")

        for j in range(len(allKeywords)):
            if allKeywords[j] in word:
                process = Process(target=instruments[j%3], args=(generateNote(chorus),))
                processQueue.put(process)
                process.start() 
                sleep(2)
        size = processQueue.qsize()
        for i in range (math.ceil(size/(2 if size > 4 else 3))):
            if not processQueue.empty():
                current = processQueue.get()
                current.terminate()


def drums(sleepTime):
    while True:
        for i in sleepTime:
            sample(DRUM_BASS_HARD, amp=1.5, rate=0.5)
            sleep(i)

filepath = input("Please enter file path: ")

extension = filepath.split('.')[-1]

composer(extension, extract(filepath))
while True:
    pass
