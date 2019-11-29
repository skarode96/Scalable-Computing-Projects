import os
import csv

common_folder = './19302270-project3/'

image_pred_file = './prod-captcha.txt'
audio_pred_file = './audio/audio-captcha-solve.txt'

output_filename = './submissions/submitty_prediction_v2.csv'

image_pred = {}
f1 = open(image_pred_file)
reader = csv.reader(f1)
for filename, text in reader:
    image_pred.update({
        filename: text
    })
f1.close()

audio_pred = {}
f1 = open(audio_pred_file)
reader = csv.reader(f1)
for filename, text, in reader:
    filename = filename.replace('.png', '.mp3')
    audio_pred.update({
        filename: text
    })
f1.close()


output_predict = []

for filename in os.listdir(common_folder):
    if filename in image_pred:
        output_predict.append({
            'filename': filename,
            'text': image_pred[filename]
        })
    elif filename in audio_pred:
        output_predict.append({
            'filename': filename,
            'text': audio_pred[filename]
        })
    else:
        output_predict.append({
            'filename': filename,
            'text': '00000000'
        })

f1 = open(output_filename, 'w')
writer = csv.DictWriter(f1, fieldnames=['filename', 'text'])
writer.writerows(output_predict)
f1.close()