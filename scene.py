from manim import *

class TheStoryOfLines(Scene):
    def construct(self):
        self.intro_sequence()
        self.history_sequence()
        self.mechanics_sequence()
        self.the_real_why_sequence()
        self.outro_sequence()

    def intro_sequence(self):
        # Title Card
        title = Text("The Power of the Straight Line", font_size=48, color=BLUE)
        subtitle = Text("Why do we even learn this?", font_size=32).next_to(title, DOWN)
        
        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(3) # Imagine narrator speaking here
        
        self.play(FadeOut(title), FadeOut(subtitle))

        # The big question
        question = Text("What problem does a line solve?", font_size=40)
        self.play(Write(question))
        self.wait(3)
        self.play(FadeOut(question))

    def history_sequence(self):
        # Section 1: History
        history_title = Text("Part 1: How did this happen?", font_size=36, color=YELLOW).to_edge(UP)
        self.play(FadeIn(history_title, shift=DOWN))

        # Geometry vs Algebra
        geo_text = Text("Geometry (Shapes)", font_size=30).shift(LEFT * 3)
        alg_text = Text("Algebra (Numbers)", font_size=30).shift(RIGHT * 3)
        
        triangle = Triangle(color=GREEN).next_to(geo_text, DOWN)
        equations = MathTex("2x + 4 = 10").next_to(alg_text, DOWN)

        self.play(Write(geo_text), Create(triangle))
        self.wait(2)
        self.play(Write(alg_text), Write(equations))
        self.wait(2)

        # Descartes bridges the gap
        bridge_text = Text("René Descartes built a bridge.", font_size=24, color=LIGHT_PINK).shift(DOWN * 2)
        self.play(Write(bridge_text))
        self.wait(3)

        # Transform into a coordinate plane
        plane = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-4, 4, 1],
            background_line_style={"stroke_opacity": 0.4}
        )
        
        self.play(
            FadeOut(geo_text, triangle, alg_text, equations, bridge_text),
            Create(plane),
            run_time=3
        )
        self.wait(3)
        self.play(FadeOut(plane), FadeOut(history_title))

    def mechanics_sequence(self):
        # Section 2: How they work
        mech_title = Text("Part 2: How do they work?", font_size=36, color=YELLOW).to_edge(UP)
        self.play(FadeIn(mech_title, shift=DOWN))

        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": WHITE},
        )
        self.play(Create(axes), run_time=2)

        # The famous equation
        equation = MathTex("y", "=", "m", "x", "+", "b", font_size=48)
        equation.to_corner(UL).shift(DOWN)
        equation.set_color_by_tex("m", RED)
        equation.set_color_by_tex("b", GREEN)
        
        self.play(Write(equation))
        self.wait(2)

        # Demonstrating 'b' (y-intercept)
        b_text = Text("b = The Start (y-intercept)", font_size=24, color=GREEN).next_to(equation, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(b_text, shift=RIGHT))
        
        dot = Dot(point=axes.c2p(0, 1), color=GREEN)
        self.play(Create(dot))
        self.wait(2)

        # Demonstrating 'm' (slope)
        m_text = Text("m = The Trend (Rate of Change)", font_size=24, color=RED).next_to(b_text, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(m_text, shift=RIGHT))

        # Drawing the line
        line = axes.plot(lambda x: 0.5 * x + 1, color=BLUE)
        self.play(Create(line), run_time=3)
        self.wait(4)

        # Show slope step (Rise over Run)
        p1 = axes.c2p(0, 1)
        p2 = axes.c2p(2, 2)
        run_line = Line(p1, axes.c2p(2, 1), color=YELLOW)
        rise_line = Line(axes.c2p(2, 1), p2, color=ORANGE)
        
        self.play(Create(run_line))
        self.play(Create(rise_line))
        self.wait(3)

        self.play(
            FadeOut(axes, line, dot, equation, b_text, m_text, run_line, rise_line, mech_title)
        )

    def the_real_why_sequence(self):
        # Section 3: The ultimate purpose
        why_title = Text("Part 3: The Ultimate Trick", font_size=36, color=YELLOW).to_edge(UP)
        self.play(FadeIn(why_title, shift=DOWN))

        truth_text = Text("The real world is curvy and complex.", font_size=30)
        self.play(Write(truth_text))
        self.wait(2)
        self.play(truth_text.animate.to_edge(UP).shift(DOWN))

        # Create a complex curve
        axes = Axes(x_range=[-3, 3], y_range=[-2, 8], x_length=8, y_length=5)
        curve = axes.plot(lambda x: x**2, color=PURPLE)
        
        self.play(Create(axes))
        self.play(Create(curve), run_time=3)
        self.wait(2)

        zoom_text = Text("But if you zoom in enough...", font_size=24).next_to(truth_text, DOWN)
        self.play(Write(zoom_text))

        # Tangent line concept (Calculus preview)
        tracker = ValueTracker(-2)
        
        tangent_line = always_redraw(
            lambda: axes.get_secant_slope_group(
                x=tracker.get_value(),
                graph=curve,
                dx=0.01,
                secant_line_color=GREEN,
                secant_line_length=4
            )
        )
        
        moving_dot = always_redraw(
            lambda: Dot(axes.c2p(tracker.get_value(), tracker.get_value()**2), color=YELLOW)
        )

        self.play(Create(tangent_line), Create(moving_dot))
        self.wait(1)
        
        # Animate the tangent line moving along the curve
        self.play(tracker.animate.set_value(2), run_time=6, rate_func=there_and_back)
        self.wait(2)

        calc_text = Text("Everything looks like a straight line.", font_size=30, color=GREEN).next_to(zoom_text, DOWN)
        self.play(Write(calc_text))
        self.wait(4)

        self.play(FadeOut(VGroup(axes, curve, tangent_line, moving_dot, truth_text, zoom_text, calc_text, why_title)))

    def outro_sequence(self):
        # Conclusion
        final_text = Text("Lines are how we predict the future.", font_size=36, color=BLUE)
        sub_final = Text("They turn chaos into predictable patterns.", font_size=28).next_to(final_text, DOWN)
        
        self.play(Write(final_text))
        self.play(FadeIn(sub_final, shift=UP))
        self.wait(5)
        
        self.play(FadeOut(final_text), FadeOut(sub_final))