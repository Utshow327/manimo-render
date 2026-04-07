from manim import *

class MainScene(Scene):
    def construct(self):
        # Set the aspect ratio to 16:9
        self.camera.aspect_ratio = 16/9

        # Create a title for the scene
        title = Title("Conics: Circles, Ellipses, Parabolas, and Hyperbolas")
        self.play(Write(title))

        # Create a circle
        circle = Circle(radius=2, color=BLUE)
        self.play(FadeIn(circle))
        self.wait(1)
        self.play(FadeOut(circle))

        # Create an ellipse
        ellipse = Ellipse(width=4, height=2, color=GREEN)
        self.play(FadeIn(ellipse))
        self.wait(1)
        self.play(FadeOut(ellipse))

        # Create a parabola
        parabola = ParametricFunction(lambda t: (t**2, t), t_range=[-2, 2], color=RED)
        self.play(FadeIn(parabola))
        self.wait(1)
        self.play(FadeOut(parabola))

        # Create a hyperbola
        hyperbola = ParametricFunction(lambda t: (t, 1/t), t_range=[0.1, 10], color=YELLOW)
        self.play(FadeIn(hyperbola))
        self.wait(1)
        self.play(FadeOut(hyperbola))

        # Create a graph with multiple conics
        graph = VGroup(
            Circle(radius=1, color=BLUE).shift(LEFT * 3),
            Ellipse(width=2, height=1, color=GREEN).shift(UP * 2),
            ParametricFunction(lambda t: (t**2, t), t_range=[-2, 2], color=RED).shift(RIGHT * 2),
            ParametricFunction(lambda t: (t, 1/t), t_range=[0.1, 10], color=YELLOW).shift(DOWN * 2),
        )
        self.play(FadeIn(graph))
        self.wait(2)
        self.play(FadeOut(graph))

        # End the scene
        self.play(FadeOut(title))
        self.wait(1)