import os
os.system("clear")
track = input("URL? : ")
command = ('youtube-dl --extract-audio --audio-format mp3 ')
os.system(command + track)
