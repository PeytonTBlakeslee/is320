# impoted turtle for writing or drawing 
# a picture 
from random import random
import turtle as tri
import random as rand


    
    

#-----game configuration----

# sh = shape, c = color, fc = fillcolor

# The set variables, sh, c, fc
sh = "triangle"
c = "pink"
fc = "pink"

# Sets the shapesize, color, and headings 
# in the right areas.
tri.shapesize(1)
tri.shape(sh)
tri.fillcolor(fc)
tri.setheading(90)
 
def onclick(): 
 ()
if (tri.onclick):
 x2 = rand.randint (-250,250) 
 y2 = rand.randint (-300, 300)
 def change_posit():
  (x2,y2)
 
def tri_clicked(a,b):
 change_posit
 tri.penup()
 tri.goto(x2,y2)
 tri.pendown()

tri.onclick(tri_clicked)

wn = tri.Screen()
wn.mainloop()
