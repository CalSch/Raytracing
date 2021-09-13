import math
from c_types import *

def vecAdd(vec1, vec2):
  return vec3(
    vec1.x+vec2.x,
    vec1.y+vec2.y,
    vec1.z+vec2.z)
def vecMultiply(vec,i):
  return vec3(vec.x*i, vec.y*i, vec.z*i)
def dist3(p1,p2):
  return math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2+(p2.z-p1.z)**2)
def CheckSphere(sphere,pos):
  return dist3(sphere.pos, pos)<=sphere.radius
def CheckRect(pos,size,p):
  return (
    p.x>pos.x and
    p.x<pos.x+size.x and
    p.y>pos.y and
    p.y<pos.y+size.y and
    p.z>pos.z and
    p.z<pos.z+size.z
  )
def posToAngle(x,y,fov,WIDTH,HEIGHT):
  i=(x-WIDTH/2)/(WIDTH/2)
  j=(y-HEIGHT/2)/(HEIGHT/2)
  return (i*fov,j*fov)