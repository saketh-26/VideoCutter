
#install moviepy package -->pip install moviepy

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

#start_time ->such as if we need from 10:00 enter as 10*60 -->600 as we are converting to seconds
start_time = float(input('enter start time of number of seconds:'))

#end_time -->same how we enter from start_time
end_time = float(input('enter end time of number of seconds:'))

#give source video in the first argument 
ffmpeg_extract_subclip("video.mp4", start_time, end_time, targetname="test.mp4")
