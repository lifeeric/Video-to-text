# Video-to-text
Creating transcript from video to text using python.



## How to run
First of all, you have to create virtual env and install all the packages:

```sh
$ python3 -m venv env
$ pip install -r requirements.txt
```
Boom. now copy the video to this directroy and pass the video name as shell parameter:

```sh
$ python app.py <video_file.extention>
$ python app.py learn-python3.mp4
```

it will generate a new file containing transcript and will delete video file.
