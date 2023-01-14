makecode = 0

def on_gesture_shake():
    global makecode
    makecode = randint(0, 2)
    if 0 == makecode:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif 1 == makecode:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
