from manim import *

class MainScene(Scene):
    def construct(self):
        # Introduction
        intro_text = Text("Gravity: The Force that Shapes Our Universe", font_size=48)
        self.play(Create(intro_text), run_time=2)
        self.wait(2)
        self.play(FadeOut(intro_text), run_time=2)

        # Section 1: What is Gravity?
        section1_text = Text("What is Gravity?", font_size=36)
        self.play(Create(section1_text), run_time=1)
        self.wait(1)
        self.play(FadeOut(section1_text), run_time=1)

        earth = Sphere(radius=1, color=BLUE)
        self.play(Create(earth), run_time=2)
        self.wait(1)
        gravity_arrow = Arrow(start=earth.get_center(), end=earth.get_center() + DOWN, color=RED)
        self.play(Create(gravity_arrow), run_time=1)
        self.wait(2)
        self.play(FadeOut(earth), FadeOut(gravity_arrow), run_time=2)

        # Section 2: Gravity and Mass
        section2_text = Text("Gravity and Mass", font_size=36)
        self.play(Create(section2_text), run_time=1)
        self.wait(1)
        self.play(FadeOut(section2_text), run_time=1)

        mass1 = Circle(radius=0.5, color=YELLOW)
        mass2 = Circle(radius=0.5, color=YELLOW)
        self.play(Create(mass1), Create(mass2), run_time=2)
        self.play(mass1.animate.shift(LEFT * 2), mass2.animate.shift(RIGHT * 2), run_time=2)
        gravity_arrow1 = Arrow(start=mass1.get_center(), end=mass2.get_center(), color=RED)
        gravity_arrow2 = Arrow(start=mass2.get_center(), end=mass1.get_center(), color=RED)
        self.play(Create(gravity_arrow1), Create(gravity_arrow2), run_time=1)
        self.wait(2)
        self.play(FadeOut(mass1), FadeOut(mass2), FadeOut(gravity_arrow1), FadeOut(gravity_arrow2), run_time=2)

        # Section 3: Gravity and Distance
        section3_text = Text("Gravity and Distance", font_size=36)
        self.play(Create(section3_text), run_time=1)
        self.wait(1)
        self.play(FadeOut(section3_text), run_time=1)

        mass3 = Circle(radius=0.5, color=YELLOW)
        mass4 = Circle(radius=0.5, color=YELLOW)
        self.play(Create(mass3), Create(mass4), run_time=2)
        self.play(mass3.animate.shift(LEFT * 2), mass4.animate.shift(RIGHT * 2), run_time=2)
        gravity_arrow3 = Arrow(start=mass3.get_center(), end=mass4.get_center(), color=RED)
        gravity_arrow4 = Arrow(start=mass4.get_center(), end=mass3.get_center(), color=RED)
        self.play(Create(gravity_arrow3), Create(gravity_arrow4), run_time=1)
        self.play(mass3.animate.shift(LEFT * 2), mass4.animate.shift(RIGHT * 2), run_time=2)
        self.wait(1)
        self.play(FadeOut(mass3), FadeOut(mass4), FadeOut(gravity_arrow3), FadeOut(gravity_arrow4), run_time=2)

        # Section 4: Gravity and Orbit
        section4_text = Text("Gravity and Orbit", font_size=36)
        self.play(Create(section4_text), run_time=1)
        self.wait(1)
        self.play(FadeOut(section4_text), run_time=1)

        sun = Circle(radius=1, color=YELLOW)
        earth_orbit = Circle(radius=2, color=BLUE)
        self.play(Create(sun), Create(earth_orbit), run_time=2)
        earth = Circle(radius=0.5, color=BLUE)
        self.play(Create(earth), run_time=1)
        self.play(MoveAlongPath(earth, earth_orbit), run_time=4)
        self.wait(1)
        self.play(FadeOut(sun), FadeOut(earth_orbit), FadeOut(earth), run_time=2)

        # Conclusion
        conclusion_text = Text("Conclusion: Gravity is the force that shapes our universe", font_size=36)
        self.play(Create(conclusion_text), run_time=2)
        self.wait(2)
        self.play(FadeOut(conclusion_text), run_time=2)
        self.wait(15)