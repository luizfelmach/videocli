import os
import cv2
import PIL
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
      print(f'[GET FRAMES] frame-{frame}.jpg')
      frame += 1

  def resizeFrames(self):
    frames = glob(f'{self.outputPath}/*')
    for frame in frames:
      frameIterator = Image.open(frame)
      width, height = frameIterator.size
      ratio = width / height
      newHeight = int(self.dimensionsTerminal[0])
      newWidth = floor(ratio * newHeight)
      frameResized = frameIterator.resize((newWidth, newHeight))
      print(f'[RESIZE FRAMES] {frame}')
      frameResized.save(frame)

  def getColorFrames(self):
    frames = glob(f'{self.outputPath}/*')
    for frame in frames:
      frameIterator = Image.open(frame)
      pixelsColor = frameIterator.load()
      print(f'[GET COLOR FRAMES] {frame}')
      self.framesPixel.append(pixelsColor)

  def printFrames(self):
    os.system('clear')
    row, column = self.dimensionsTerminal
    # print(row, column)
    # print(self.framesPixel[0][59,33])
    countFrames = 0
    for frame in self.framesPixel:
      for r in range(int(row)):
        for c in range(60):
          rgb = frame[c, r]
          print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(rgb[0], rgb[1], rgb[2], self.char), end='', flush=True)
      os.system('clear')
      if (countFrames % 30 == 0):
        sleep(1)
      countFrames += 1

a = Video('videoPath')
a.getFrames()
a.resizeFrames()
a.getColorFrames()
a.printFrames()