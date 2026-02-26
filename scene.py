from manim import *

class MainScene(Scene):
    def construct(self):
        text = Text("Hello Manimo!", font_size=72)
        self.play(Write(text))
        self.wait(2)