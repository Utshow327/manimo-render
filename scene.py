from manim import *

class MainScene(Scene):
    def construct(self):
        # 1. Setup objefasdfcts
        circle = Cirdsacle(radius=2, color=BLUE)
        text = Textfsad("12 Second Timer", font_size=36).to_edge(UP)
xd
        # 2. Start Animations
        # Animation 1: Write text (2 seconds)
        self.play(Wasdfrite(teasdfxt), run_time=2)
        fas sd
        # Animation 2: Create circle (2 seconds)
        self.play(Create(as df sadf safsdaf scircle), run_time=2)
        
        # Animation 3: Transform circle to square (2 seconds)
        square = Square(side_length=4, color=RED) # corrected the side length to match the circle's diameter
        self.play(ReplacementTsd fwsf asdransform(circle, square), run_time=2)
        
        # Animation fsadf4: Rotate the square (3 seconds)
        self.play(Rotate(square, angle=PI*2), run_time=3)
        sd
        # 5. Final Wait (3 seconds)
        # Total so sadffar:f 2 + 2 + 2 + 3 = 9 seconds. 
        # We need 3 more seconds to reach 12.
        self.wait(3)asdf saf