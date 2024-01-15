import sounddevice as sd
from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt


@dataclass
class NotesTable:
    C7: float = 2093.005


sample_rate = 44100      # Sample rate
period = 0.2   # Duration of recording

plt.ion()


def on_close(event):
    print('Application closed!')
    exit()


fig, ax = plt.subplots(1, 2)
fig.canvas.mpl_connect('close_event', on_close)

while True:
    myrecording = sd.rec(int(period * sample_rate), samplerate=sample_rate, channels=1).T[0]
    sd.wait()  # Wait until recording is finished

    N = len(myrecording)
    x_range = np.arange(N)
    fourier = np.fft.fft(myrecording)
    print(fourier.shape)

    ax[0].clear()
    ax[1].clear()
    ax[0].plot(x_range / sample_rate, myrecording)
    ax[1].set_xscale('log')
    ax[1].plot((x_range / period)[:int(NotesTable.C7 * period)],
               (fourier.real**2 + fourier.imag**2)[:int(NotesTable.C7 * period)])
    plt.pause(0.05)
