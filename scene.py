from manim import *

class MainScene(Scene):
    def construct(self):
        # Set the aspect ratio to 16:9
        self.camera.aspect_ratio = 16/9

        # Create a circle to represent the ball
        ball = Circle(radius=0.5, color=BLUE, fill_opacity=1)

        # Add the ball to the scene
        self.add(ball)

        # Set the initial position of the ball
        ball.shift(UP * 3)

        # Set the gravity
        gravity = 0.1

        # Set the initial velocity of the ball
        velocity = 0

        # Create a floor for the ball to bounce off
        floor = Line(LEFT * 8, RIGHT * 8, color=GREY)

        # Add the floor to the scene
        self.add(floor)

        # Animate the ball bouncing
        self.play(
            ball.animate.shift(DOWN * 3),
            rate_func=linear,
            run_time=3
        )

        for _ in range(10):
            # Animate the ball falling
            self.play(
                ball.animate.shift(DOWN * 2),
                rate_func=linear,
                run_time=1.5
            )

            # Animate the ball bouncing back up
            self.play(
                ball.animate.shift(UP * 2),
                rate_func=linear,
                run_time=1.5
            )