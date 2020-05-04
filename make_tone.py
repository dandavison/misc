import numpy as np

def make_tone(frequency, duration, sampling_rate, play=False):
    cycles = frequency * duration
    time = np.linspace(0, 2 * cycles * math.pi, num=duration * sampling_rate)
    signal = np.sin(time)
    if play:
        import sounddevice
        sounddevice.play(signal, sampling_rate)
    return signal
