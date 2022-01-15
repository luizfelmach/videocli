import os
import cv2
import PIL
from PIL import Image
from glob import glob
from math import floor

class Video:
  def __init__(self, videoPath, outputPath='./data'):
    self.videoPath = videoPath
    self.outputPath = outputPath
    self.dimensionsTerminal = os.popen('stty size', 'r').read().split() # rows, columns
  
  def getFrames(self):
    videoCapture = cv2.VideoCapture(self.videoPath)
    success,image = videoCapture.read()
    frame = 1
    baseFrameName = 'frame'
    while success:
      cv2.imwrite(f'./data/frame-{frame}.jpg', image)      
      success,image = videoCapture.read()
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
      frameResized.save(frame)

videoPath = '/home/luizfelipemachado/Documentos/teste.mov'

a = Video(videoPath)
# a.getFrames()
a.resizeFrames()