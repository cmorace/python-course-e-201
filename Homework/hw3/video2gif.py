from moviepy.editor import VideoFileClip
dir = '/Users/charles/Documents/python-course-e-201/Homework/hw3/'
clip = VideoFileClip(dir+'part3.mp4')
clip.write_gif(dir+'part3.gif')