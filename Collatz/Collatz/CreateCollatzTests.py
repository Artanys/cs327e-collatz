import random

x = 0
with open ( "RunCollatz.in", "w" ) as file:
    while x < 1000:
        a = random.randint ( 1, 1000000 )
        b = random.randint ( 1, 1000000 )
        file.write ( str ( a ) + " " + str ( b ) + "\n" )
        x += 1