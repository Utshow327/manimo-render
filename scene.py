from manim import *

class TwoBallsUp(Scene):
    def construct(self):
            ball1 = Circle(radius=0.4).shift(LEFT*2 + DOWN*3)
                    ball2 = Circle(radius=0.4).shift(RIGHT*2 + DOWN*3)

                            self.play(
                                        ball1.animate.shift(UP*6),
                                                    ball2.animate.shift(UP*6),
                                                                run_time=2,
                                                                            rate_func=smooth
                                                                                    )

                                                                                            self.wait()