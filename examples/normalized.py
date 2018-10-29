"""https://i.imgur.com/Dlve8rJ.png"""

import random
from time import sleep

from oscilloscope import Osc


# turn on normalization
osc = Osc(normalize=True)


@osc.signal
def increasing_signal(state):
    delta = 1

    while True:
        state.draw(random.randint(-delta, delta))
        delta += 5
        sleep(0.01)


osc.start()
