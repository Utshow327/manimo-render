from manim import *

class TwelveSecondScene(Scene):
    def construct(self):
        # 1. Setup objects
        circle = Circle(radius=2, color=BLUE)
        text = Text("12 Second Timer", font_size=36).to_edge(UP)

        # 2. Start Animations
        # Animation 1: Write text (2 seconds)
        self.play(Write(text), run_time=2)
        
        # Animation 2: Create circle (2 seconds)
        self.play(Create(circle), run_time=2)
        
        # Animation 3: Transform circle to square (2 seconds)
        square = Square(side_length=3, color=RED)
        self.play(ReplacementTransform(circle, square), run_time=2)
        
        # Animation 4: Rotate the square (3 seconds)
        self.play(Rotate(square, angle=PI*2), run_time=3)
        
        # 5. Final Wait (1 second)
        # Total so far: 2 + 2 + 2 + 3 = 9 seconds. 
        # We need 3 more seconds to reach 12.
        self.wait(3)