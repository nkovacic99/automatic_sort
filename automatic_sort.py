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
movies = list()

PATH = '/home/omen/Downloads/'

iskalne_zahteve = [['.txt', '.docx', '.dcx', '.pdf', '.doc'], ['.jpg', '.png', '.jpeg'], ['.mp3'], ['.mkv', '.mp4', '1080p', '720p']]
downloads_folder = os.listdir("/home/omen/Downloads")


downloads_folder.remove('documents')
downloads_folder.remove('pictures')
downloads_folder.remove('music')
downloads_folder.remove('other')

for datoteka in downloads_folder:
    for ext in iskalne_zahteve[0]:
        if ext in str(datoteka):
            documents.append(datoteka)
    for ext in iskalne_zahteve[1]:
        if ext in str(datoteka):
            pictures.append(datoteka)
    for ext in iskalne_zahteve[2]:
        if ext in str(datoteka):
            music.append(datoteka)
    for ext in iskalne_zahteve[3]:
        if ext in str(datoteka):
            movies.append(datoteka)
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