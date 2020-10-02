# Cameron Gillingham
# Class: CS20
# Date: Oct. 2, 2020
# Description: creates balloon that follows cursor


def setup():
    size(500, 500)
def draw():
    
    # Green Background
    background(7, 79, 22)
    
    # Balloon
    fill(mouseX, mouseY, 0)
    circle(mouseX-50, mouseY-50, 40)
    
    # Left Eye
    fill(mouseX, mouseY, 100)
    circle(mouseX-55, mouseY-55, 10)
    
    # Right Eye
    fill(mouseX, mouseY, 200)
    circle(mouseX-45, mouseY-55, 10)
  
    # Mouth
    fill(mouseX, mouseY, 150)
    arc(mouseX-50, mouseY-38, 15, 10, 20, 30)
   
    # Right Pupil
    fill(0, 0, 0)
    circle(mouseX-55, mouseY-55, 2)
   
    # Left Pupil
    fill(0, 0, 0)
    circle(mouseX-45, mouseY-55, 2)
    
    # String
    line(mouseX-50, mouseY-30, mouseX, mouseY)
