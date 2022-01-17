import os
import cv2
import PIL
import ascii_magic
from PIL import Image
from glob import glob
from math import floor
from time import sleep

class Video:
  def __init__(self, videoPath, outputPath='./data', char='@'):
    self.videoPath = videoPath
    self.outputPath = outputPath
    self.dimensionsTerminal = os.popen('stty size', 'r').read().split() # rows, columns
    self.char = char
    self.framesPixel = []
  
  def getFrames(self):
    videoCapture = cv2.VideoCapture(self.videoPath)
    success,image = videoCapture.read()
    frame = 1
    baseFrameName = 'frame'
    while success:
      cv2.imwrite(f'./data/frame-{frame}.jpg', image)      
      success,image = videoCapture.read()
      print(f'[GET FRAMES] frame-{frame}.jpg \033[F')
      frame += 1
  
  def convertToAscii(self):
    row, column = self.dimensionsTerminal
    charsToLinePrevious = '\033[F'*int(row)
    frames = glob(f'{self.outputPath}/*')
    for i in range(len(frames)):
      frameName = f'{self.outputPath}/frame-{i+1}.jpg'
      myart = ascii_magic.from_image_file(frameName, columns=int(column), back=ascii_magic.Back.BLACK)
      ascii_magic.to_terminal(myart)
      print(f'{charsToLinePrevious}')

videoPath = './example/example.mp4'

a = Video(videoPath)
a.getFrames()
a.convertToAscii()