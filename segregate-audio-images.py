import os
import shutil


def copy(extn, source_dir, destn_dir):

    files = os.listdir(source_dir)

    files = list(filter(lambda x:extn in x, files))

    if os.path.exists(destn_dir):
        shutil.rmtree(destn_dir)
        os.makedirs(destn_dir)
    else :
        print("Creating directory " + destn_dir)
        os.makedirs(destn_dir)

    for file in files:
        shutil.copyfile( source_dir + '/' + file , destn_dir + '/' + file)


directory_name = '19302270-project3'
img_directory = '19302270-images'
audio_directory = '19302270-audio'


copy('.png', directory_name, img_directory)
copy('.mp3', directory_name, audio_directory)







