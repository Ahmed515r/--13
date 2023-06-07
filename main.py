num = 0
numSp = 0
aa = 100
def on_pulsed_p0_high():
  
    pass
pins.on_pulsed(DigitalPin.P0, PulseValue.HIGH, on_pulsed_p0_high)

def on_button_pressed_a():
    global numSp
    numSp = numSp**2
    basic.show_number(numSp)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_ad():
   global numSp
   global aa
   if numSp >= aa:
       basic.show_string("yas!")
   elif numSp < aa:
       basic.show_string("no")
input.on_button_pressed(Button.AB, on_button_pressed_ad)