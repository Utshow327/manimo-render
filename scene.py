from manim import *

class MainScene(Scene):
    def construct(self):
        # Set the aspect ratio of the scene to 16:9
        self.set_aspect_ratio(16/9)

        # Create a sun at the center of the scene
        sun = Circle(color=YELLOW, radius=1)
        sun.set_fill(YELLOW)
        self.add(sun)

        # Create the planets
        mercury = Circle(color=GREY, radius=0.1)
        mercury.shift(2 * RIGHT)
        venus = Circle(color=WHITE, radius=0.2)
        venus.shift(4 * RIGHT)
        earth = Circle(color=BLUE, radius=0.3)
        earth.shift(6 * RIGHT)
        mars = Circle(color=RED, radius=0.2)
        mars.shift(8 * RIGHT)
        jupiter = Circle(color=ORANGE, radius=0.5)
        jupiter.shift(12 * RIGHT)
        saturn = Circle(color=YELLOW_E, radius=0.4)
        saturn.shift(16 * RIGHT)
        uranus = Circle(color=TEAL, radius=0.3)
        uranus.shift(20 * RIGHT)
        neptune = Circle(color=BLUE_E, radius=0.2)
        neptune.shift(24 * RIGHT)

        # Animate the planets moving around the sun
        self.play(
            mercury.animate.shift(2 * LEFT).run_time(2),
            venus.animate.shift(4 * LEFT).run_time(3),
            earth.animate.shift(6 * LEFT).run_time(4),
            mars.animate.shift(8 * LEFT).run_time(5),
            jupiter.animate.shift(12 * LEFT).run_time(6),
            saturn.animate.shift(16 * LEFT).run_time(7),
            uranus.animate.shift(20 * LEFT).run_time(8),
            neptune.animate.shift(24 * LEFT).run_time(9)
        )

        # Add the planets to the scene
        self.add(mercury, venus, earth, mars, jupiter, saturn, uranus, neptune)

        # Animate the planets moving in their orbits
        self.play(
            Rotate(mercury, about_point=ORIGIN, angle=2 * PI, run_time=10),
            Rotate(venus, about_point=ORIGIN, angle=2 * PI, run_time=15),
            Rotate(earth, about_point=ORIGIN, angle=2 * PI, run_time=20),
            Rotate(mars, about_point=ORIGIN, angle=2 * PI, run_time=25),
            Rotate(jupiter, about_point=ORIGIN, angle=2 * PI, run_time=30),
            Rotate(saturn, about_point=ORIGIN, angle=2 * PI, run_time=35),
            Rotate(uranus, about_point=ORIGIN, angle=2 * PI, run_time=40),
            Rotate(neptune, about_point=ORIGIN, angle=2 * PI, run_time=45)
        )