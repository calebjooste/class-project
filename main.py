endstate = 0
Counter = 0
index = 4
while Counter < endstate:
    led.plot(Counter, 2)
    led.toggle(0, 0)
    led.toggle(0, 0)
    Counter += 1
    basic.pause(1000)
Counter += 1
# unpin
while Counter < endstate:
    led.toggle(0, Counter)
    led.toggle(0, 0)
    led.plot(0, 2)
    Counter = 0
    basic.pause(200)