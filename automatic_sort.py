import os
import shutil

# access files in "Downloads" (check)
# change files' locations (check)
# generate new folders if necessary (not necessary)
# automatic run

documents = list()
pictures = list()
music = list()
other = list()

PATH = '/home/nace/Downloads/'

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

# figure out, why can't you move files (check)

for datoteka in documents:
    shutil.move(PATH + datoteka, PATH + 'documents/' + datoteka)
for datoteka in pictures:
    shutil.move(PATH + datoteka, PATH + 'pictures/' + datoteka)
for datoteka in music:
    shutil.move(PATH + datoteka, PATH + 'music/' + datoteka)
for datoteka in other:
    shutil.move(PATH + datoteka, PATH + 'other/' + datoteka)