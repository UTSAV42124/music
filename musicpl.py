from pygame import mixer
from tkinter import *
import webbrowser

root = Tk()
root.geometry("600x300")

mixer.init()
playlist = ["song1.mp3", "song2.mp3", "song3.mp3"]
current_song_index = 0
mixer.music.load(playlist[current_song_index])


def pause():
    mixer.music.pause()


def play():
    mixer.music.play()


def resume():
    mixer.music.unpause()


def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(playlist)
    mixer.music.load(playlist[current_song_index])
    mixer.music.play()


def previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(playlist)
    mixer.music.load(playlist[current_song_index])
    mixer.music.play()


def open_gaana():
    webbrowser.open("https://gaana.com")

Label(root, text="Welcome to music player", font="lucidia 30 bold").pack()
Button(text="Play", command=play).place(x=200, y=100)
Button(text="Pause", command=pause).place(x=250, y=100)
Button(text="Resume", command=resume).place(x=310, y=100)
Button(text="Previous", command=previous_song).place(x=370, y=100)
Button(text="Next", command=next_song).place(x=450, y=100)
Button(text="Quit", command=quit).place(x=520, y=100)
Button(text="Go to Gaana.com", command=open_gaana).place(x=250, y=150)

root.mainloop()
