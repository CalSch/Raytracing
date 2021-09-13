import math
import datetime
import threading
import time
from PIL import Image
from c_types import *
from c_util import *
from c_ray import *

WIDTH=250
HEIGHT=200
DEBUG=True
FOV=45*(math.pi/180)
DEPTH_MULTIPLYER=1

img=Image.new('RGB', (WIDTH,HEIGHT), (0,0,0))
pix=img.load()

scene=[
  Sphere(vec3(0,20,0), 10, (255,0,0)),
  Rect(vec3(5,15,0), vec3(10,2,10), (0,255,0))
]
cam=vec3(-10,-5,-10)

def rtx(x: int, y: int):
  (rx,ry)=posToAngle(x,y,FOV,WIDTH,HEIGHT)
  ray=Ray(cam,vec3((x/FOV),1,(y/FOV)),0.1,scene)
  (collided, obj)=ray.run()

  if collided:
    return (
      int(obj.color[0]-ray.dist*10),
      int(obj.color[1]-ray.dist*10),
      int(obj.color[2]-ray.dist*10)
    )

  return (int(ray.dist*DEPTH_MULTIPLYER),int(ray.dist*DEPTH_MULTIPLYER),int(ray.dist*DEPTH_MULTIPLYER))



def worker(x: int, y: int):
  if DEBUG:
    print(f"Worker started at {x}, {y}")
  pix[x,y]=rtx(x,y)
  

start=datetime.datetime.now()
for y in range(HEIGHT):
  for x in range(WIDTH):
    thread = threading.Thread(target=worker, args=(x,y,))
    thread.start()
    # if DEBUG:
    #   print(f"Processing pixel at ({x},{y})")
    # pix[x,y]=rtx(x,y)
    if DEBUG and (y*WIDTH+x)%(WIDTH*5)==0:
      print("saving")
      img.save("out.png")

print("Done!")
img.save("out.png")
end=datetime.datetime.now()
print("Completed in "+str((end-start).seconds)+" seconds!")