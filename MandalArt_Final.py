import turtle
import random
import time
# Initialize turtle
pen = turtle.Turtle()
pen.setheading(90)
pen.pensize(1)
pen.speed(20)

# Universal variables
LINE1, LINE2 = "~" * 36, "~" * 24
colors = ["darkred", "red", "yellow", "darkgreen", "green", "lightgreen", "darkblue", "blue", "purple"]
angles = list(range(1,362))

# Function to get user input
def get_input(response, values):
    while True:
        value = input(response).strip().lower()
        if value in values:
            return value

# Function to draw a Mandala

def draw_mandala_random():
    for times in range(36):
        pen.color("green")
        pen.circle(100)
        pen.color("yellow")
        pen.forward(200)
        pen.forward(50)
        pen.left(120)
        pen.color("red")
        pen.forward(100)
        pen.right(120)
        pen.left(170)
        pen.left(20)
        pen.forward(15)


def draw_mandala_custom(size, cl, fd, rt, custom_colors):
    for _ in range(36):
        selection = random.choice(custom_colors)
        pen.color(selection)
        pen.circle(cl)
        pen.color(selection)
        pen.forward(fd)
        pen.forward(fd)
        pen.left(120)
        pen.color(selection)
        pen.forward(fd)
        pen.right(rt)
        pen.left(170)
        pen.left(20)
        pen.forward(fd)

# Main function
def main():
    print(LINE1 + "\nWelcome to Mandala ART Creator\n" + LINE1)
    while True:
        name = input("What is your name? ")
        # Check if the input contains only alphabets
        if name.isalpha():
            break  # Exit the loop if the input is valid
        else:
            print("Invalid input. Please use only alphabets.")
            

    print(f"{name}, In this Mandala Art Creator, you get to choose the size and colors of your art, or can have the computer generated random one \n{LINE2}")
    time.sleep(1)
    ready = input("Are you ready or not? ")

    if ready[0].lower() == "y":
        answer = get_input("Would you like to use our random creator function or our custom function? {random/custom} ", {"random", "custom"})

        # Universal variables
        size = random.uniform(1.5, 2.5)
        fd = 75 * size
        rt = random.uniform(115, 125)

        if answer == "random":
            
            draw_mandala_random()

        elif answer == "custom":
            print(LINE2 + "\nYou can choose any colors from this list for your Mandala: \nDarkred, red, yellow, darkgreen, green, lightgreen, darkblue, blue, purple")
            color1 = get_input("What is the first color? ", colors)
            color2 = get_input("What is the second color? ", colors)
            color3 = get_input("What is the third color? ", colors)
            custom_colors = [color1, color2, color3]

            while True:
                cl = input("What angle would you like your Mandala to turn at? ")
                # Check if the input contains space or enter
                if (cl==""):
                    cl=0
                if 1 <= int(cl) <= 360:
                    break   # Exit the loop if the input is valid
                else:
                    print("Please enter an angle within the range of 1 to 360.")
            draw_mandala_custom(size,int(cl), fd, rt, custom_colors)
        print(LINE2 + "\nInitializing...")
        print("Determining features... \nColor... \nSize...")
        time.sleep(3)
        print(LINE1 + f"\nYour final result should be drawing as of this point!\nThanks for using the generator, {name}!")    
            

        

    else:
        print("Come and use the custom generator later!")

if __name__ == "__main__":
    main()
    turtle.mainloop()
