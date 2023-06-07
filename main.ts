let num = 0
let numSp = 0
let aa = 100
pins.onPulsed(DigitalPin.P0, PulseValue.High, function on_pulsed_p0_high() {
    
})
function on_button_pressed_a() {
    
    numSp = numSp ** 2
    basic.showNumber(numSp)
    input.onButtonPressed(Button.A, function on_button_pressed_a2() {
        
    })
}

