from manim import *

class MainScene(Scene):
    def construct(self):
        # Introduction
        intro_text = Text("How Planes Fly", font_size=64)
        self.play(Create(intro_text), run_time=2)
        self.wait(1)
        self.play(FadeOut(intro_text), run_time=1)

        # Basic Principle: Lift
        lift_text = Text("Lift", font_size=48)
        self.play(Create(lift_text), run_time=1)
        self.wait(1)
        wing_shape = Polygon([-2, -1, 0], [2, -1, 0], [2, 1, 0], [-2, 1, 0], color=BLUE)
        self.play(Create(wing_shape), run_time=1)
        self.wait(1)
        air_flow = Arrow([-3, 0, 0], [3, 0, 0], color=RED)
        self.play(Create(air_flow), run_time=1)
        self.wait(1)
        lift_arrow = Arrow([0, -1, 0], [0, 1, 0], color=GREEN)
        self.play(Create(lift_arrow), run_time=1)
        self.wait(1)
        self.play(FadeOut(lift_text), FadeOut(wing_shape), FadeOut(air_flow), FadeOut(lift_arrow), run_time=1)

        # Basic Principle: Thrust
        thrust_text = Text("Thrust", font_size=48)
        self.play(Create(thrust_text), run_time=1)
        self.wait(1)
        engine_shape = Circle(radius=0.5, color=YELLOW)
        self.play(Create(engine_shape), run_time=1)
        self.wait(1)
        thrust_arrow = Arrow([0, 0, 0], [2, 0, 0], color=ORANGE)
        self.play(Create(thrust_arrow), run_time=1)
        self.wait(1)
        self.play(FadeOut(thrust_text), FadeOut(engine_shape), FadeOut(thrust_arrow), run_time=1)

        # Basic Principle: Drag
        drag_text = Text("Drag", font_size=48)
        self.play(Create(drag_text), run_time=1)
        self.wait(1)
        drag_arrow = Arrow([0, 0, 0], [-2, 0, 0], color=PURPLE)
        self.play(Create(drag_arrow), run_time=1)
        self.wait(1)
        self.play(FadeOut(drag_text), FadeOut(drag_arrow), run_time=1)

        # Advanced: Control Surfaces
        control_surfaces_text = Text("Control Surfaces", font_size=48)
        self.play(Create(control_surfaces_text), run_time=1)
        self.wait(1)
        aileron_shape = Rectangle(width=1, height=0.5, color=BLUE)
        self.play(Create(aileron_shape), run_time=1)
        self.wait(1)
        elevator_shape = Rectangle(width=1, height=0.5, color=RED)
        self.play(Create(elevator_shape), run_time=1)
        self.wait(1)
        rudder_shape = Rectangle(width=1, height=0.5, color=YELLOW)
        self.play(Create(rudder_shape), run_time=1)
        self.wait(1)
        self.play(FadeOut(control_surfaces_text), FadeOut(aileron_shape), FadeOut(elevator_shape), FadeOut(rudder_shape), run_time=1)

        # Advanced: Aerodynamics
        aerodynamics_text = Text("Aerodynamics", font_size=48)
        self.play(Create(aerodynamics_text), run_time=1)
        self.wait(1)
        airfoil_shape = ParametricCurve(lambda t: [t, 0.2*t**2, 0], t_min=-2, t_max=2, color=GREEN)
        self.play(Create(airfoil_shape), run_time=1)
        self.wait(1)
        boundary_layer = Rectangle(width=2, height=0.1, color=ORANGE)
        self.play(Create(boundary_layer), run_time=1)
        self.wait(1)
        self.play(FadeOut(aerodynamics_text), FadeOut(airfoil_shape), FadeOut(boundary_layer), run_time=1)

        # Advanced: Flight Envelope
        flight_envelope_text = Text("Flight Envelope", font_size=48)
        self.play(Create(flight_envelope_text), run_time=1)
        self.wait(1)
        envelope_shape = Circle(radius=2, color=BLUE)
        self.play(Create(envelope_shape), run_time=1)
        self.wait(1)
        stall_line = Line([-2, 0, 0], [2, 0, 0], color=RED)
        self.play(Create(stall_line), run_time=1)
        self.wait(1)
        self.play(FadeOut(flight_envelope_text), FadeOut(envelope_shape), FadeOut(stall_line), run_time=1)

        # Conclusion
        conclusion_text = Text("How Planes Fly: A Comprehensive Guide", font_size=48)
        self.play(Create(conclusion_text), run_time=2)
        self.wait(5)
        self.play(FadeOut(conclusion_text), run_time=2)
        self.wait(15)