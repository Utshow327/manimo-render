from manim import *

class HowPlanesFly(Scene):
    def construct(self):
        # Set up 9:16 frame
        self.camera.frame_width = 6
        self.camera.frame_height = 10

        # Title
        title = Text("How Planes Fly", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Plane body
        plane_body = Rectangle(width=3, height=0.5, color=BLUE)
        wing = Triangle(width=3, height=0.2, color=YELLOW).next_to(plane_body, UP, buff=0)
        plane = VGroup(plane_body, wing).move_to(ORIGIN)
        self.play(FadeIn(plane))
        self.wait(1)

        # Airflow arrows above and below wing
        arrow_top = Arrow(start=LEFT*4, end=RIGHT*4, color=WHITE).next_to(wing, UP, buff=0.3)
        arrow_bottom = Arrow(start=LEFT*4, end=RIGHT*4, color=WHITE).next_to(wing, DOWN, buff=0.3)
        self.play(GrowArrow(arrow_top), GrowArrow(arrow_bottom))
        self.wait(1)

        # Labels for forces
        lift_label = Text("Lift ↑", font_size=36, color=GREEN).next_to(arrow_top, UP)
        gravity_label = Text("Gravity ↓", font_size=36, color=RED).next_to(arrow_bottom, DOWN)
        self.play(Write(lift_label), Write(gravity_label))
        self.wait(1)

        # Animate plane moving forward
        self.play(plane.animate.shift(RIGHT*3))
        self.wait(1)

        # Fade everything out
        self.play(
            *[FadeOut(mob) for mob in [plane, arrow_top, arrow_bottom, lift_label, gravity_label, title]]
        )
        self.wait(1)