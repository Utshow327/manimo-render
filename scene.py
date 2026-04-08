from manim import *

class HowPlanesFly(Scene):
    def construct(self):

            # Title
                    title = Text("How Planes Fly")
                            title.to_edge(UP)
                                    self.play(Write(title))
                                            self.wait(1)

                                                    # Simple plane (body + wing)
                                                            body = Rectangle(width=4, height=0.6)
                                                                    body.set_fill(BLUE, opacity=1)

                                                                            wing = Polygon(
                                                                                        [-2, 0.3, 0],
                                                                                                    [2, 0.3, 0],
                                                                                                                [0, 1.2, 0]
                                                                                                                        )
                                                                                                                                wing.set_fill(YELLOW, opacity=1)

                                                                                                                                        plane = VGroup(body, wing)
                                                                                                                                                plane.move_to(ORIGIN)

                                                                                                                                                        self.play(FadeIn(plane))
                                                                                                                                                                self.wait(1)

                                                                                                                                                                        # Airflow arrows
                                                                                                                                                                                arrow_top = Arrow(LEFT*5 + UP*2, RIGHT*5 + UP*2, buff=0)
                                                                                                                                                                                        arrow_bottom = Arrow(LEFT*5 + DOWN*1.5, RIGHT*5 + DOWN*1.5