"""this program plays musical notes using the pygame library
     The default sampling rate for the pygame mixer is 44100 per second.

     MIDI note numbers are a standard way to represent musical pitches
     in the context of electronic music and MIDI technology. MIDI note
     numbers are used to represent notes in a chromatic scale and are
     widely used in MIDI devices, software, and musical notation.
     The MIDI note number system assigns integer values to each note in the chromatic scale.
     The standard range of MIDI note numbers is from 0 to 127, covering several octaves.

"""
import time
import pygame as pg
import numpy as np

pg.init()
pg.mixer.init()

# read the notes list file into notes_list
notes_file = open("notes_list.txt")
file_contents = notes_file.read()
notes_file.close()
notes_list = file_contents.splitlines()

# create a midi notes file from notes_list
midi_notes_dictionary = {}
for i in range(len(notes_list)):
    dict_key = notes_list[i]
    midi_note_number = i + 12
    frequency = 440.0 * (2 ** ((midi_note_number - 69) / 12.0))
    midi_notes_dictionary[dict_key] = [midi_note_number, frequency]
    if i == 36 or i == 50:
        print(f'key = {dict_key}  midi note number = {midi_note_number}  frequency = {frequency}')

# print(midi_notes_dictionary)


def synth(frequency, duration=1000.0, sampling_rate=44100, volume=.5):
    # print('line 39   ', frequency)
    # Calculate the number of frames in the audio
    frames = int(duration * sampling_rate)

    # Generate a cosine wave for the specified frequency
    sound_array = np.cos(2 * np.pi * frequency * np.linspace(0, duration, frames))
    # print('function synth arr = ', sound_array)

    # Scale the audio data to a 16-bit signed integer format
    sound = np.asarray([32767 * sound_array, 32767 * sound_array]).T.astype(np.int16)
    # print('function synth sound =  ', sound)

    # Create a Pygame sound object from the audio data
    sound = pg.sndarray.make_sound(sound.copy())
    sound.play()
    sound.set_volume(volume)
    time.sleep(2)
    sound.fadeout(1)

    return sound


# play some notes by naming the note and giving it a duration
synth(midi_notes_dictionary['C4'][1], 1000)
synth(midi_notes_dictionary['D4'][1], 1000)
synth(midi_notes_dictionary['E4'][1], 1000)

tones = ['C4', 'C4', 'F4', 'F4', 'B4', 'A4']
amplitude = .5
for note in tones:
    print(note)
    freq = midi_notes_dictionary[note][1]
    snd = synth(freq, duration=22, volume=amplitude)
    amplitude = amplitude / 2


