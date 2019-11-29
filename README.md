## Steps
1. Run segregate-audio-images.py to separate audio and images captcha files
2. cd Captcha Images
    1. run Generate.py 
    2. run train.py
    3. run classify.py
3. cd ../Captcha-Audio
    1. run audio_generate.py
    2. run convertmp3tospectra.py
    3. run  train-rgb.py
    4. run classify-rgb.py
4. run  Merge-audio-images-output.py
   