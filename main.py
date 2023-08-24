import turtle
import time

class Window:
    """Initialize the main window"""
    def __init__(self):
        self.window = turtle.Screen()
        self.window.bgcolor("white")
        self.window.title("test-turtle-py")
        self.window.setup(width=800, height=600)

    def listen(self, Snake):
        self.listen()
        self.onkeypress(Snake.move_left, "Left")
        self.onkeypress(Snake.move_right, "Right")
        self.onkeypress(Snake.move_up, "Up")
        self.onkeypress(Snake.move_down, "Down")

class Snake:
    """A snake which is controlled by player"""
    #  "left" == left, "right" == right, "up" == up, "down" == down
    direction = 0 

    def __init__(self):
        """Setup to make the snake"""
        self.snake = turtle.Turtle()
        self.snake.shape("square")
        self.snake.color("green")
        #snake.penup()
        #snake.goto(0, 0)
        self.snake.direction = "Stop"

    def move_left():
        if self.direction != "right":
            self.direction = "left"

    def move_right():
        if self.direction != "left":
            self.direction = "right"

    def move_up():
        if self.direction != "down":
            self.direction = "up"

    def move_down():
        if self.direction != "up":
            self.direction = "down"


class Debugger:
    """A Debugger, print all variables to console"""
    def __init__(self):
        pass

    def print_all_variables(self, Snake):
        print(Snake.direction)

if __name__ == "__main__":
    window = Window()
    snake = Snake()
    window.listen(snake)
    debugger = Debugger()
    while True:
        debugger.print_all_variables(snake)
        time.sleep(1)

    turtle.mainloop()
