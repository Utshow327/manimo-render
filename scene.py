from manim import *

class MainScene(Scene):
    def construct(self):
        # Introduction
        intro_text = Text("Conics: An Introduction")
        self.play(Write(intro_text))
        self.wait(2)
        self.play(FadeOut(intro_text))

        # Conic Sections
        conic_sections_text = Text("Conic Sections")
        self.play(Write(conic_sections_text))
        self.wait(2)
        self.play(FadeOut(conic_sections_text))

        # Circle
        circle_text = Text("Circle: The set of all points that are at a fixed distance (radius) from a center point.")
        self.play(Write(circle_text))
        self.wait(2)
        self.play(FadeOut(circle_text))

        circle = Circle(radius=2, color=BLUE)
        self.play(Create(circle))
        self.wait(2)
        self.play(FadeOut(circle))

        # Ellipse
        ellipse_text = Text("Ellipse: The set of all points for which the sum of the distances to two fixed points (foci) is constant.")
        self.play(Write(ellipse_text))
        self.wait(2)
        self.play(FadeOut(ellipse_text))

        ellipse = Ellipse(width=4, height=2, color=RED)
        self.play(Create(ellipse))
        self.wait(2)
        self.play(FadeOut(ellipse))

        # Parabola
        parabola_text = Text("Parabola: The set of all points that are equidistant to a fixed point (focus) and a fixed line (directrix).")
        self.play(Write(parabola_text))
        self.wait(2)
        self.play(FadeOut(parabola_text))

        parabola = FunctionGraph(lambda x: x**2, x_min=-2, x_max=2, color=YELLOW)
        self.play(Create(parabola))
        self.wait(2)
        self.play(FadeOut(parabola))

        # Hyperbola
        hyperbola_text = Text("Hyperbola: The set of all points for which the difference of the distances to two fixed points (foci) is constant.")
        self.play(Write(hyperbola_text))
        self.wait(2)
        self.play(FadeOut(hyperbola_text))

        hyperbola = FunctionGraph(lambda x: 1/x, x_min=0.1, x_max=2, color=GREEN)
        self.play(Create(hyperbola))
        self.wait(2)
        self.play(FadeOut(hyperbola))

        # Conclusion
        conclusion_text = Text("Conclusion: Conic sections are fundamental concepts in mathematics and physics, and understanding them is essential for various applications.")
        self.play(Write(conclusion_text))
        self.wait(2)
        self.play(FadeOut(conclusion_text))