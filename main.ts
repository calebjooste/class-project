let endstate = 0
let Counter = 0
let index = 4
while (Counter < endstate) {
    led.plot(Counter, 2)
    led.toggle(0, 0)
    led.toggle(0, 0)
    Counter += 1
}
