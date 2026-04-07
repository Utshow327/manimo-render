from manim import *

class MainScene(Scene):
    def construct(self):
        # Create the Sun
        sun = Circle(color=YELLOW, radius=1.5)
        sun.set_fill(YELLOW, opacity=0.8)

        # Create the planets
        mercury = Circle(color=GREY, radius=0.2)
        mercury.set_fill(GREY, opacity=0.8)
        venus = Circle(color=WHITE, radius=0.4)
        venus.set_fill(WHITE, opacity=0.8)
        earth = Circle(color=BLUE, radius=0.5)
        earth.set_fill(BLUE, opacity=0.8)
        mars = Circle(color=RED, radius=0.3)
        mars.set_fill(RED, opacity=0.8)
        jupiter = Circle(color="#964B00", radius=1.2)
        jupiter.set_fill("#964B00", opacity=0.8)
        saturn = Circle(color="#FFD700", radius=1.0)
        saturn.set_fill("#FFD700", opacity=0.8)
        uranus = Circle(color="#ADD8E6", radius=0.8)
        uranus.set_fill("#ADD8E6", opacity=0.8)
        neptune = Circle(color="#0000FF", radius=0.6)
        neptune.set_fill("#0000FF", opacity=0.8)

        # Create the orbits
        mercury_orbit = Circle(color=WHITE, radius=2.5)
        mercury_orbit.set_stroke(width=0.5)
        venus_orbit = Circle(color=WHITE, radius=4.0)
        venus_orbit.set_stroke(width=0.5)
        earth_orbit = Circle(color=WHITE, radius=5.5)
        earth_orbit.set_stroke(width=0.5)
        mars_orbit = Circle(color=WHITE, radius=7.0)
        mars_orbit.set_stroke(width=0.5)
        jupiter_orbit = Circle(color=WHITE, radius=9.0)
        jupiter_orbit.set_stroke(width=0.5)
        saturn_orbit = Circle(color=WHITE, radius=11.0)
        saturn_orbit.set_stroke(width=0.5)
        uranus_orbit = Circle(color=WHITE, radius=13.0)
        uranus_orbit.set_stroke(width=0.5)
        neptune_orbit = Circle(color=WHITE, radius=15.0)
        neptune_orbit.set_stroke(width=0.5)

        # Add the Sun and the planets to the scene
        self.add(sun)

        # Add the planets to the scene
        self.add(mercury)
        self.add(venus)
        self.add(earth)
        self.add(mars)
        self.add(jupiter)
        self.add(saturn)
        self.add(uranus)
        self.add(neptune)

        # Add the orbits to the scene
        self.add(mercury_orbit)
        self.add(venus_orbit)
        self.add(earth_orbit)
        self.add(mars_orbit)
        self.add(jupiter_orbit)
        self.add(saturn_orbit)
        self.add(uranus_orbit)
        self.add(neptune_orbit)

        # Animate the planets along their orbits
        self.play(
            Rotate(mercury, about_point=ORIGIN, angle=10 * TAU, rate_func=linear, run_time=10),
            Rotate(venus, about_point=ORIGIN, angle=8 * TAU, rate_func=linear, run_time=15),
            Rotate(earth, about_point=ORIGIN, angle=6 * TAU, rate_func=linear, run_time=20),
            Rotate(mars, about_point=ORIGIN, angle=5 * TAU, rate_func=linear, run_time=25),
            Rotate(jupiter, about_point=ORIGIN, angle=3 * TAU, rate_func=linear, run_time=35),
            Rotate(saturn, about_point=ORIGIN, angle=2.5 * TAU, rate_func=linear, run_time=40),
            Rotate(uranus, about_point=ORIGIN, angle=2 * TAU, rate_func=linear, run_time=50),
            Rotate(neptune, about_point=ORIGIN, angle=1.5 * TAU, rate_func=linear, run_time=60),
        )

        # Set the camera to zoom out
        self.camera.frame.set_width(25)

        # Wait for 10 seconds before closing the scene
        self.wait(10)