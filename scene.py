from manim import *

class BasicAnimation(Scene):
    def construct(self):
            # 1. Create our objects (Mobjects)
                    square = Square(color=BLUE, fill_opacity=0.5)
                            circle = Circle(color=PINK, fill_opacity=0.8)
                                    text = Text("Hello, Manim!", font_size=36).to_edge(UP)

                                            # 2. Define the animations
                                                    self.play(Write(text))        # Draw the text
                                                            self.play(Create(square))     # Draw the square
                                                                    self.wait(1)                  # Pause for a second
                                                                            
                                                                                    # 3. Transform the square into the circle
                                                                                            self.play(ReplacementTransform(square, circle))
                                                                                                    self.wait(1)
                                                                                                            
                                                                                                                    # 4. Fade everything out
                                                                                                                            self.play(FadeOut(circle), FadeOut(text))
                                                                                                                            