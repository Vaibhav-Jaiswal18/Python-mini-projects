import turtle

WIDTH, HEIGHT = 500,500 

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title('Turtle Racing!')
def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("This is not numeric...Try Again!")
            continue

        if 2<= racers <= 10:
            return racers
        else:
            print("Number not in range 2-10...Try Again!")

get_number_of_racers()