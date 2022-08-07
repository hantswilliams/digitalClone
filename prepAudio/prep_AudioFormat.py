import ffmpeg

fileLocation = '/Users/hantswilliams/Documents/development/python_projects/Audio2Head/demo/audio/clips/rajivClassrecordingOriginal.m4a'
outputLocation = '/Users/hantswilliams/Documents/development/python_projects/Audio2Head/demo/audio/rajivClassrecordingOriginal2.wav'

stream = ffmpeg.input(fileLocation)
stream = ffmpeg.output(stream, outputLocation)
ffmpeg.run(stream)