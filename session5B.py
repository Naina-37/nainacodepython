"""
    Another Brick in the Wall
    Who placed, the last brick and how many ?
    
    Mr. John -> Requirement | create a wall with 13 bricks

                        Bricks
    jack : 1            1
    joe  : 2            3

    jack : 2            5
    joe  : 4            9

    jack : 3            12
    joe  : 6            13   

    joe -> last brick
           1 brick 
           #last_person = ""

"""
number_brick = int(input("Enter the number of bricks you want: "))
total_bricks = 0
jack = 1
joe = 2
last_person =""
last_bricks = 0

while total_bricks < number_brick:
    if total_bricks < number_brick:
        total_bricks += jack
        last_person = "jack"
        last_bricks = jack
        jack += 1

    if total_bricks < number_brick:
        total_bricks += joe
        last_person = "joe"
        last_bricks = joe
        joe += 2

print("TOTAL BRICKS USED:", total_bricks)
print("Placed the last brick:", last_person)
print("Number of bricks placed by last person:", last_bricks)

