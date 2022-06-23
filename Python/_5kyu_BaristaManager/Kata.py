from operator import itemgetter

def barista(coffees, c_machines):
    coffees.sort()
    machines=[] 
    for i in range(c_machines):
        machines.append([0,0])
    for time in coffees:
        if time == 0:
            continue
        machines[0][0] += time              #Wait for machine
        machines[0][1] += machines[0][0]    #Total time machine run
        machines[0][0] += 2                 #Increment wait for next brew
        machines.sort()
    return sum(list(map(itemgetter(1), machines)))
