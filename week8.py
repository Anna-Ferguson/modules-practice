import pattern_functions as p

def main():
    p.setup
    playagain = True
    while playagain:
        print("[1] Rectangle Pattern")
        print("[2] Circle Pattern")
        print("[3] Super Pattern")
        pattern = input("Which pattern would you like, 1, 2, or 3?  ")
        p.setup()
        if pattern == "1":
            x=int(input("Starting X position: "))
            y = int(input("Y: "))
            offset = int(input("Offset: "))
            height = int(input("Height: "))
            width = int(input("Width: "))
            count = int(input("Count: "))
            rotation = int(input("Rotation: "))
            p.drawAllrectangles(x, y, width, height, rotation, offset, count)
        
        elif pattern == "2":
            x = int(input("Starting X Position: "))
            y = int(input("Y: "))
            offset = int(input("Offset: "))
            count = int(input("Count: "))
            radius = int(input("Radius: "))
            p.drawcircle(x,y,offset, count, radius)

        elif pattern == "3":
            x = int(input("Starting X Position: "))
            y = int(input("Y: "))
            offset = int(input("Offset: "))
            height = int(input("Height: "))
            width = int(input("Width: "))
            count = int(input("Count: "))
            rotation = int(input("Rotation: "))
            radius = int(input("Radius: "))
            p.superpattern(x,y,width,height,rotation,offset,count,radius)

        ans = input("Would you like to play again?")

        if ans == "yes" or ans == "y" or ans == "YES" or ans == "Yes":
            clear = input("Would you like to clear the board?")
            playagain = True
            if clear == "yes" or clear == "y" or clear =="YES" or clear == "Yes":
                p.reset()
        elif ans == "no" or ans == "NO" or ans == "n" or ans == "No":
            playagain = False
            p.done()

    print("Thanks for playing!")

main()







