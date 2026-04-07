from manim import *

class MainScene(Scene):
    def construct(self):
        # Create a title for the scene
        title = Text("Manim Animation", font_size=72).set_color(BLUE)
        self.play(Write(title), run_time=2)
        self.wait(2)

        # Create some text to animate
        text1 = Text("This is some text to animate.", font_size=36).set_color(RED)
        text2 = Text("This is some more text to animate.", font_size=36).set_color(GREEN)
        text3 = Text("And this is even more text to animate.", font_size=36).set_color(YELLOW)
        text4 = Text("We can keep adding more and more text.", font_size=36).set_color(PURPLE)
        text5 = Text("The animation will keep going and going.", font_size=36).set_color(ORANGE)

        # Animate the text
        self.play(Write(text1), run_time=2)
        self.wait(2)
        self.play(FadeOut(text1), run_time=1)
        self.wait(1)
        self.play(Write(text2), run_time=2)
        self.wait(2)
        self.play(FadeOut(text2), run_time=1)
        self.wait(1)
        self.play(Write(text3), run_time=2)
        self.wait(2)
        self.play(FadeOut(text3), run_time=1)
        self.wait(1)
        self.play(Write(text4), run_time=2)
        self.wait(2)
        self.play(FadeOut(text4), run_time=1)
        self.wait(1)
        self.play(Write(text5), run_time=2)
        self.wait(2)
        self.play(FadeOut(text5), run_time=1)
        self.wait(1)

        # Create some shapes to animate
        circle = Circle(radius=1.5, color=BLUE)
        square = Square(side_length=3, color=RED)
        triangle = Triangle(color=YELLOW)

        # Animate the shapes
        self.play(Create(circle), run_time=2)
        self.wait(2)
        self.play(FadeOut(circle), run_time=1)
        self.wait(1)
        self.play(Create(square), run_time=2)
        self.wait(2)
        self.play(FadeOut(square), run_time=1)
        self.wait(1)
        self.play(Create(triangle), run_time=2)
        self.wait(2)
        self.play(FadeOut(triangle), run_time=1)
        self.wait(1)

        # Create a graph to animate
        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 10, 2],
            x_length=6,
            y_length=6,
            axis_config={"include_tip": False},
        )
        graph = axes.plot(lambda x: x**2, x_range=[0, 10], color=GREEN)

        # Animate the graph
        self.play(Create(axes), run_time=2)
        self.wait(2)
        self.play(Create(graph), run_time=2)
        self.wait(2)
        self.play(FadeOut(axes), run_time=1)
        self.play(FadeOut(graph), run_time=1)
        self.wait(1)

        # Create a 3D object to animate
        sphere = Sphere(radius=1.5, resolution=20).set_color(BLUE)

        # Animate the 3D object
        self.play(Create(sphere), run_time=2)
        self.wait(2)
        self.play(Rotate(sphere, angle=PI/2), run_time=2)
        self.wait(2)
        self.play(FadeOut(sphere), run_time=1)
        self.wait(1)

        # Create some more text to animate
        text6 = Text("We can keep adding more and more text.", font_size=36).set_color(PURPLE)
        text7 = Text("The animation will keep going and going.", font_size=36).set_color(ORANGE)
        text8 = Text("And this is even more text to animate.", font_size=36).set_color(YELLOW)
        text9 = Text("This is some more text to animate.", font_size=36).set_color(GREEN)
        text10 = Text("This is some text to animate.", font_size=36).set_color(RED)

        # Animate the text
        self.play(Write(text6), run_time=2)
        self.wait(2)
        self.play(FadeOut(text6), run_time=1)
        self.wait(1)
        self.play(Write(text7), run_time=2)
        self.wait(2)
        self.play(FadeOut(text7), run_time=1)
        self.wait(1)
        self.play(Write(text8), run_time=2)
        self.wait(2)
        self.play(FadeOut(text8), run_time=1)
        self.wait(1)
        self.play(Write(text9), run_time=2)
        self.wait(2)
        self.play(FadeOut(text9), run_time=1)
        self.wait(1)
        self.play(Write(text10), run_time=2)
        self.wait(2)
        self.play(FadeOut(text10), run_time=1)
        self.wait(1)

        # Create a table to animate
        table = Table(
            [
                ["Column 1", "Column 2", "Column 3"],
                ["Row 1", "Cell 1", "Cell 2"],
                ["Row 2", "Cell 3", "Cell 4"],
            ],
            row_labels=[Text("Row")],
            col_labels=[Text("Column 1"), Text("Column 2"), Text("Column 3")],
        )

        # Animate the table
        self.play(Create(table), run_time=2)
        self.wait(2)
        self.play(FadeOut(table), run_time=1)
        self.wait(1)

        # Create a matrix to animate
        matrix = Matrix(
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
            element_to_mobject=lambda x: Text(str(x)),
        )

        # Animate the matrix
        self.play(Create(matrix), run_time=2)
        self.wait(2)
        self.play(FadeOut(matrix), run_time=1)
        self.wait(1)

        # Create a final title for the scene
        final_title = Text("The End", font_size=72).set_color(BLUE)
        self.play(Write(final_title), run_time=2)
        self.wait(2)