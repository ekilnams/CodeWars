def barista(coffees):
    coffees.sort()
    wait = 0
    total = 0
    for time in coffees:
        wait += time
        total += wait
        wait += 2
    return total
