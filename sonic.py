from psonic import *
from random import choice

tick = Message()

@in_thread
def random_riff():
    use_synth(PROPHET)
    sc = scale(E3, MINOR)
    while True:
        s = random.choice([0.125,0.25,0.5])
        tick.sync()
        for i in range(8):
            r = random.choice([0.125, 0.25, 1, 2])
            n = random.choice(sc)
            co = random.randint(30,100)
            play(n, release = r, cutoff = co)
            sleep(s)

@in_thread
def random_guitar():
    use_synth(PLUCK)
    chord1 = chord(E4, MAJOR)
    while True:
        s = random.choice([0.125,0.25,0.5])
        tick.sync()
        for i in range(8):
            r = random.choice([0.125, 0.25, 1, 2])
            # n = random.choice(sc)
            co = random.randint(30,100)
            play(chord1, release = r, cutoff = co)
            sleep(s)

@in_thread
def drums():
    while True:
        tick.cue()
        for i in range(16):
            r = random.randrange(1,10)
            sample(DRUM_BASS_HARD, rate=r)
            sleep(0.125)

random_riff()
drums()
random_guitar()