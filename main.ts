let makecode = 0
input.onGesture(Gesture.Shake, function () {
    makecode = randint(0, 2)
    if (0 == makecode) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (1 == makecode) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
})
