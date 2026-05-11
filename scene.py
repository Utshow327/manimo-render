from manim import *

class MainScene(Scene):
    def construct(self):
        # Create the sun
        sun = Circle(color=YELLOW, radius=1.5)
        sun.set_fill(YELLOW, opacity=1)
        self.add(sun)

        # Create the planets
        mercury = Circle(color=GREY, radius=0.2)
        mercury.set_fill(GREY, opacity=1)
        mercury.shift(2 * LEFT)

        venus = Circle(color=WHITE, radius=0.4)
        venus.set_fill(WHITE, opacity=1)
        venus.shift(3.5 * LEFT)

        earth = Circle(color=BLUE, radius=0.5)
        earth.set_fill(BLUE, opacity=1)
        earth.shift(5 * LEFT)

        mars = Circle(color=RED, radius=0.3)
        mars.set_fill(RED, opacity=1)
        mars.shift(6.5 * LEFT)

        jupiter = Circle(color="#964B00", radius=1)
        jupiter.set_fill("#964B00", opacity=1)
        jupiter.shift(9 * LEFT)

        saturn = Circle(color="#C9C4B5", radius=0.8)
        saturn.set_fill("#C9C4B5", opacity=1)
        saturn.shift(11.5 * LEFT)

        uranus = Circle(color="#56B3FA", radius=0.6)
        uranus.set_fill("#56B3FA", opacity=1)
        uranus.shift(14 * LEFT)

        neptune = Circle(color="#2E4053", radius=0.5)
        neptune.set_fill("#2E4053", opacity=1)
        neptune.shift(16.5 * LEFT)

        # Create the orbits
        mercury_orbit = Circle(color=GREY, radius=2)
        mercury_orbit.set_stroke(width=0.5)

        venus_orbit = Circle(color=WHITE, radius=3.5)
        venus_orbit.set_stroke(width=0.5)

        earth_orbit = Circle(color=BLUE, radius=5)
        earth_orbit.set_stroke(width=0.5)

        mars_orbit = Circle(color=RED, radius=6.5)
        mars_orbit.set_stroke(width=0.5)

        jupiter_orbit = Circle(color="#964B00", radius=9)
        jupiter_orbit.set_stroke(width=0.5)

        saturn_orbit = Circle(color="#C9C4B5", radius=11.5)
        saturn_orbit.set_stroke(width=0.5)

        uranus_orbit = Circle(color="#56B3FA", radius=14)
        uranus_orbit.set_stroke(width=0.5)

        neptune_orbit = Circle(color="#2E4053", radius=16.5)
        neptune_orbit.set_stroke(width=0.5)

        # Add the planets and orbits to the scene
        self.add(mercury_orbit)
        self.add(venus_orbit)
        self.add(earth_orbit)
        self.add(mars_orbit)
        self.add(jupiter_orbit)
        self.add(saturn_orbit)
        self.add(uranus_orbit)
        self.add(neptune_orbit)

        self.add(mercury)
        self.add(venus)
        self.add(earth)
        self.add(mars)
        self.add(jupiter)
        self.add(saturn)
        self.add(uranus)
        self.add(neptune)

        # Animate the planets moving along their orbits
        self.play(MoveAlongPath(mercury, mercury_orbit), rate_func=linear, run_time=10)
        self.play(MoveAlongPath(venus, venus_orbit), rate_func=linear, run_time=15)
        self.play(MoveAlongPath(earth, earth_orbit), rate_func=linear, run_time=20)
        self.play(MoveAlongPath(mars, mars_orbit), rate_func=linear, run_time=25)
        self.play(MoveAlongPath(jupiter, jupiter_orbit), rate_func=linear, run_time=30)
        self.play(MoveAlongPath(saturn, saturn_orbit), rate_func=linear, run_time=35)
        self.play(MoveAlongPath(uranus, uranus_orbit), rate_func=linear, run_time=40)
        self.play(MoveAlongPath(neptune, neptune_orbit), rate_func=linear, run_time=45)

        self.wait(15)