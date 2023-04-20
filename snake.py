from turtle import Turtle

# constants in python have to declare in all uppercase
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

starting_positions = [(0, 0), (0, 20), (0, 40)]


class Snake:
    def __init__(self):
        self.segments = []
        self.make_segment()
        self.head = self.segments[0]

    def make_segment(self):
        for position in starting_positions:
            self.add_segments(position)

    def add_segments(self, position):
        new_segments = Turtle(shape="square")
        new_segments.color("white")
        new_segments.penup()
        new_segments.goto(position)
        self.segments.append(new_segments)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):

        for seg_count in range(len(self.segments) - 1, 0, -1):
            new_x_cor = self.segments[seg_count - 1].xcor()
            new_y_cor = self.segments[seg_count - 1].ycor()
            self.segments[seg_count].goto(new_x_cor, new_y_cor)
        self.segments[0].forward(MOVE_DISTANCE)

    def reset(self):
        self.segments.clear()
        self.make_segment()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
