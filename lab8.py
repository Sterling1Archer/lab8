from guizero import App, Slider, Text
from gpiozero import AngularServo, Servo
import time, math

def secondfunc():
    
    app.bg = "#00cc99"
    app.width = 200
    app.height= 120
    wanted_text = Text(app, "")
    wanted_text.text_size = 12
    wanted_text.font = "Times New Roman"
    wanted_text.text_color = "#000000"
    
    slider1 = Slider(app ,start=-100,command=slider_top_changed)
    slider2 = Slider(app ,start=-100,command=slider_bottom_changed)
   
    return app

def slider_top_changed(slider_value):
    print("Slider value: ",slider_value)
    angle = (int(slider_value)*0.45)+45
    angle = math.ceil(angle)
    print("Angle: ",angle)
    #time.sleep(1)
    s_top.angle = angle
    time.sleep(0.05)
    s_top.angle = None
    print("Angle2: ",s_top.angle)
    
def slider_bottom_changed(slider_value):
    print("Slider value: ",slider_value)
    angle = (int(slider_value)*0.45)+45
    angle = math.ceil(angle)
    print("Angle: ",angle)
    #time.sleep(1)
    s_base.angle = angle
    time.sleep(0.05)
    s_base.angle = None
    print("Angle2: ",s_base.angle)

if __name__ == '__main__':
    s_base = AngularServo(26, min_angle=0, max_angle=90)
    s_base.angle = None
    s_top = AngularServo(21, min_angle=0, max_angle=90)
    s_top.angle = None
    app = App("RC Servo Controller")
    app2 = secondfunc()
    
    app.display(app2)