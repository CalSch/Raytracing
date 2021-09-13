# class Color:
#   def __init__(self,r: int, g: int, b: int):
#     self.r: int=r
#     self.g: int=g
#     self.b: int=b
class vec3:
  def __init__(self,x: float, y:float, z:float):
    self.x: float=x
    self.y: float=y
    self.z: float=z
class Sphere:
  def __init__(self,pos: vec3, radius: float, color: tuple):
    self.pos: vec3=pos
    self.radius: float=radius
    self.color: tuple=color
class Rect:
  def __init__(self,pos,size,color):
    self.pos=pos
    self.size=size
    self.color=color