from c_util import *
from c_types import *

class Ray:
  def __init__(self,pos: vec3, slope: vec3, step: float,objs):
    self.pos: vec3=pos
    self.slope: vec3=slope
    self.step: float=step
    self.objs=objs
    self.dist=0
  def move(self):
    self.pos=vecAdd(self.pos, vecMultiply(self.slope,self.step))
    self.dist+=self.step
  def check(self):
    collided=False
    colObj=None

    for obj in self.objs:
      if type(obj)==Sphere:
        collided=CheckSphere(obj, self.pos)
      elif type(obj)==Rect:
        collided=CheckRect(obj.pos, obj.size, self.pos)
      if collided:
        colObj=obj
        break
    
    return (collided,obj)
  def run(self):
    collided=False
    obj=None
    while (not collided) and (self.dist<50):
      self.move()
      (collided, obj)=self.check()
    return (collided, obj)