from manim import *

# ---------- FORCE 9:16 FORMAT ----------
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
# ---------------------------------------

class HowPlanesFly(Scene):
    def construct(self):

        # TITLE
        title = Text("How Planes Fly", font_size=70)
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))
        self.wait(1)

        # PLANE
        body = Rectangle(width=4, height=0.6)
        body.set_fill(BLUE, opacity=1)

        wing = Polygon(
            [-2, 0.3, 0],
            [2, 0.3, 0],
            [0, 1.3, 0]
        )
        wing.set_fill(YELLOW, opacity=1)

        plane = VGroup(body, wing)
        plane.move_to(ORIGIN)

        self.play(FadeIn(plane))
        self.wait(2)

        # AIRFLOW (LONGER VISUAL)
        airflow = VGroup()
        for y in [2.5, 2, 1.5, -1.5, -2, -2.5]:
            arrow = Arrow(
                start=[-6, y, 0],
                end=[6, y, 0],
                buff=0
            )
            airflow.add(arrow)

        self.play(LaggedStart(*[GrowArrow(a) for a in airflow], lag_ratio=0.2))
        self.wait(3)

        # LIFT
        lift_arrow = Arrow(
            plane.get_center(),
            plane.get_center() + UP * 4,
            color=GREEN,
            buff=0
        )
        lift_text = Text("Lift", color=GREEN).next_to(lift_arrow, UP)

        self.play(GrowArrow(lift_arrow), Write(lift_text))
        self.wait(4)

        # GRAVITY
        gravity_arrow = Arrow(
            plane.get_center(),
            plane.get_center() + DOWN * 4,
            color=RED,
            buff=0
        )
        gravity_text = Text("Gravity", color=RED).next_to(gravity_arrow, DOWN)

        self.play(GrowArrow(gravity_arrow), Write(gravity_text))
        self.wait(4)

        # THRUST
        thrust_arrow = Arrow(
            plane.get_center(),
            plane.get_center() + RIGHT * 5,
            color=ORANGE,
            buff=0
        )
        thrust_text = Text("Thrust", color=ORANGE).next_to(thrust_arrow, RIGHT)

        self.play(GrowArrow(thrust_arrow), Write(thrust_text))
        self.wait(4)

        # DRAG
        drag_arrow = Arrow(
            plane.get_center(),
            plane.get_center() + LEFT * 5,
            color=PURPLE,
            buff=0
        )
        drag_text = Text("Drag", color=PURPLE).next_to(drag_arrow, LEFT)

        self.play(GrowArrow(drag_arrow), Write(drag_text))
        self.wait(4)

        # FINAL FLY UP (LONG MOTION)
        self.play(
            plane.animate.shift(UP * 5 + RIGHT * 2),
            run_time=6
        )
        self.wait(3)

        self.play(
            FadeOut(VGroup(
                plane, airflow,
                lift_arrow, gravity_arrow,
                thrust_arrow, drag_arrow,
                lift_text, gravity_text,
                thrust_text, drag_text,
                title
            )),
            run_time=3
        )
        self.wait(2)