import time

import python_imagesearch.imagesearch
import cv2
import pyautogui
import getmac
from getmac import get_mac_address as gma
dosya=open("data/info/cf/bilgi.txt","r")



if gma()==dosya.readline(17) or gma()==dosya.readline(17) or gma()==dosya.readline(17) or gma()==dosya.readline(17):
 print("Bot çalışıyor")

 while True:
  cords= python_imagesearch.imagesearch.imagesearch("Capture.PNG")
  if cords[0] !=-1:
   time.sleep(4)
   print("Evet'e tıklandı")
   pyautogui.leftClick(cords[0],cords[1])

else:
  print("Lütfen programı satın alınız.")
  time.sleep(10)