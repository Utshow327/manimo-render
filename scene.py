from manim import *

class MainScene(Scene):
    def construct(self):
        # Create a square with side length a
        square_a = Square(side_length=4, color=BLUE)
        square_a.shift(LEFT * 2)

        # Create a square with side length b
        square_b = Square(side_length=3, color=RED)
        square_b.shift(RIGHT * 2)

        # Create a square with side length c (hypotenuse)
        square_c = Square(side_length=5, color=YELLOW)
        square_c.shift(DOWN * 2)

        # Create right triangle
        triangle = Polygon(ORIGIN, UP * 4, RIGHT * 3, color=GREEN, fill_opacity=0.5)
        triangle.shift(LEFT * 0.5 + UP * 0.5)

        # Create labels
        label_a = Text("a", font_size=24).next_to(square_a, UP)
        label_b = Text("b", font_size=24).next_to(square_b, UP)
        label_c = Text("c", font_size=24).next_to(square_c, UP)
        label_triangle = Text("a^2 + b^2 = c^2", font_size=24).next_to(triangle, DOWN)

        # Animations
        self.play(FadeIn(square_a), FadeIn(square_b), FadeIn(square_c))
        self.play(Create(triangle), FadeIn(label_a), FadeIn(label_b), FadeIn(label_c))
        self.play(Write(label_triangle))
        self.play(triangle.animate.shift(UP * 1.5), label_triangle.animate.shift(UP * 1.5))
        self.play(square_a.animate.shift(UP * 1), square_b.animate.shift(UP * 1))
        self.play(square_a.animate.scale(0.5), square_b.animate.scale(0.5))
        self.play(triangle.animate.scale(0.5), label_triangle.animate.scale(0.5))
        self.wait(15)