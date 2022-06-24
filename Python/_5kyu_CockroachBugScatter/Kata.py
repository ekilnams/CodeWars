def traverse_wall(coord, holes, pos_dir, hole_counts):
    closest = None
    if pos_dir:
        for hole in holes:
            if hole[0] >= coord:
                if closest == None or hole[0] < closest[0]:
                    closest = hole
    else:
         for hole in holes:
            if hole[0] <= coord:
                if closest == None or hole[0] > closest[0]:
                    closest = hole
    if closest != None:
        hole_counts[closest[1]] += 1
        return False
    return True

def cockroaches(room):
    hole_counts = [0,0,0,0,0,0,0,0,0,0]
    holes_top = []
    holes_left = []
    holes_bottom = []
    holes_right = []

    bugs_up = []
    bugs_left = []
    bugs_down = []
    bugs_right = []

    width = len(room[0])
    height = len(room)

    for y in range(height):
        for x in range(width):
            character = room[y][x]

            #Store bug data
            if character.isalpha():
                if character == "U":
                    bugs_up.append(x)
                elif character == "L":
                    bugs_left.append(y)
                elif character == "D":
                    bugs_down.append(x)
                elif character == "R":
                    bugs_right.append(y)
                continue

            #Store hole data
            if character.isdigit():
                if y == 0:
                    holes_top.append((x, int(character)))
                elif x == 0:
                    holes_left.append((y, int(character)))
                elif y == height-1:
                    holes_bottom.append((x, int(character)))
                elif x == width-1:
                    holes_right.append((y, int(character)))

    #print("HOLES")
    #print("Top", holes_top)
    #print("Left", holes_left)
    #print("Bottom", holes_bottom)
    #print("Right", holes_right)
    #print("BUGS")
    #print("Up", bugs_up)
    #print("Left", bugs_left)
    #print("Down", bugs_down)
    #print("Right", bugs_right)

    for bug in bugs_up:
        if traverse_wall(bug, holes_top, False, hole_counts):
            if traverse_wall(0, holes_left, True, hole_counts):
                if traverse_wall(0, holes_bottom, True, hole_counts):
                    if traverse_wall(height-1, holes_right, False, hole_counts):
                        traverse_wall(width-1, holes_top, False, hole_counts)

    for bug in bugs_left:
        if traverse_wall(bug, holes_left, True, hole_counts):
            if traverse_wall(0, holes_bottom, True, hole_counts):
                if traverse_wall(height-1, holes_right, False, hole_counts):
                    if traverse_wall(width-1, holes_top, False, hole_counts):
                        traverse_wall(0, holes_left, True, hole_counts)

    for bug in bugs_down:
        if traverse_wall(bug, holes_bottom, True, hole_counts):
            if traverse_wall(height-1, holes_right, False, hole_counts):
                if traverse_wall(width-1, holes_top, False, hole_counts):
                    if traverse_wall(0, holes_left, True, hole_counts):
                        traverse_wall(0, holes_bottom, True, hole_counts)

    for bug in bugs_right:
        if traverse_wall(bug, holes_right, False, hole_counts):
            if traverse_wall(width-1, holes_top, False, hole_counts):
                if traverse_wall(0, holes_left, True, hole_counts):
                    if traverse_wall(0, holes_bottom, True, hole_counts):
                        traverse_wall(height-1, holes_right, False, hole_counts)

    return hole_counts
