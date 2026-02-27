from manim import *

class SimpleAnimation(Scene):
    def construct(self):
            # Create text
                    title = Text("Simple Manim Animation")
                            self.play(Write(title))
                                    self.wait(1)

                                            # Move text to top
                                                    self.play(title.animate.to_edge(UP))

                                                            # Create a circle
                                                                    circle = Circle()
                                                                            self.play(Create(circle))
                                                                                    self.wait(1)

                                                                                            # Transform circle into square
                                                                                                    square = Square()
                                                                                                            self.play(Transform(circle, square))
                                                                                                                    self.wait(1)

                                                                                                                            # Fade everything out
                                                                                                                                    self.play(FadeOut(title), FadeOut(circle))
                                                                                                                                            self.wait(1)