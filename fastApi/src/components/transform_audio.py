import ffmpeg
from io import BytesIO
from pydub import AudioSegment


def audio_converter_function(file_location, fileoutput_location):

    track = AudioSegment.from_file(file_location,  format= 'm4a')
    track.export(fileoutput_location, format='wav')
    
    return True
