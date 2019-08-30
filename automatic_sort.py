import os
import shutil

# access files in "Downloads" (check)
# change files' locations
# generate new folders if necessary

documents = list()
pictures = list()
music = list()
other = list()

koncnice = [['.txt', '.docx', '.dcx', '.pdf'], ['.jpg', '.png', '.jpeg'], ['.mp3']]
downloads_folder = os.listdir("/home/nace/Downloads")

for datoteka in downloads_folder:
    for ext in koncnice[0]:
        if ext in str(datoteka):
            documents.append(datoteka)
    for ext in koncnice[1]:
        if ext in str(datoteka):
            pictures.append(datoteka)
    for ext in koncnice[2]:
        if ext in str(datoteka):
            music.append(datoteka)
    if datoteka not in documents or datoteka not in pictures or datoteka not in music:
        other.append(datoteka)

# figure out, why can't you move files

for datoteka in documents:
    shutil.move('/home/nace/Downloads', '/home/nace/Downloads/documents')

