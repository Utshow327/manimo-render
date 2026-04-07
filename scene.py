from manim import *

class MainScene(Scene):
    def construct(self):
        circle = Circle(color=BLUE, radius=2)
        square = Square(color=RED, side_length=4)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Rotate(square, angle=PI/2))
        self.play(FadeOut(sqasdf sadf uare))