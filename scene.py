from manim import *

class MainScene(Scene):
    def construct(self):
        # Create a cricket field
        field = Circle(radius=5, color=GREEN, stroke_width=2)
        self.add(field)

        # Create wickets
        wicket1 = Rectangle(width=0.5, height=1, color=WHITE, stroke_width=2)
        wicket1.shift(4*RIGHT)
        wicket2 = Rectangle(width=0.5, height=1, color=WHITE, stroke_width=2)
        wicket2.shift(4*LEFT)
        self.add(wicket1, wicket2)

        # Create players
        player1 = Circle(radius=0.2, color=BLUE, stroke_width=2)
        player1.shift(3*RIGHT)
        player2 = Circle(radius=0.2, color=RED, stroke_width=2)
        player2.shift(3*LEFT)
        player3 = Circle(radius=0.2, color=YELLOW, stroke_width=2)
        player3.shift(2*UP)
        player4 = Circle(radius=0.2, color=PURPLE, stroke_width=2)
        player4.shift(2*DOWN)
        self.add(player1, player2, player3, player4)

        # Animate players running
        self.play(MoveAlongPath(player1, line_start=player1.get_center(), end=player2.get_center(), stroke_width=2, color=BLUE), 
                  MoveAlongPath(player2, line_start=player2.get_center(), end=player1.get_center(), stroke_width=2, color=RED), 
                  MoveAlongPath(player3, line_start=player3.get_center(), end=player4.get_center(), stroke_width=2, color=YELLOW), 
                  MoveAlongPath(player4, line_start=player4.get_center(), end=player3.get_center(), stroke_width=2, color=PURPLE), 
                  rate_func=linear, run_time=2)

        # Animate ball being thrown
        ball = Circle(radius=0.1, color=WHITE, stroke_width=2)
        ball.shift(2*UP)
        self.add(ball)
        self.play(MoveAlongPath(ball, line_start=ball.get_center(), end=player1.get_center(), stroke_width=2, color=WHITE), 
                  rate_func=linear, run_time=1)

        # Animate players catching ball
        self.play(MoveAlongPath(player1, line_start=player1.get_center(), end=ball.get_center(), stroke_width=2, color=BLUE), 
                  rate_func=linear, run_time=0.5)
        self.play(FadeOut(ball), rate_func=linear, run_time=0.5)

        # Animate players celebrating
        self.play(Rotate(player1, angle=PI/2), Rotate(player2, angle=PI/2), 
                  Rotate(player3, angle=PI/2), Rotate(player4, angle=PI/2), 
                  rate_func=linear, run_time=1)