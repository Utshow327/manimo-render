from manimlib import *

class InteractiveExample(Scene):
    def construct(self):
        # Create a circle
        circle = Circle(color=BLUE)

        # Create text
        text = Text("Hello bro 😎")

        # Show circle
        self.play(ShowCreation(circle))

        # Move circle
        self.play(circle.animate.shift(RIGHT * 2))

        # Show text
        self.play(Write(text))

        # Wait so you can see it
        self.wait()