from manim import *

class MainScene(Scene):
    def construct(self):
        self.camera.background_color = "#2b2b2b"

        # Create a circle
        circle = Circle(radius=2, color="#ffffff")

        # Add the circle to the scene
        self.add(circle)

        # Animate the circle growing
        self.play(circle.animate.scale(1.1), run_time=2)

        # Create a square
        square = Square(side_length=4, color="#ff0000")

        # Add the square to the scene
        self.add(square)

        # Animate the square rotating
        self.play(Rotate(square, angle=PI/2), run_time=2)

        # Create a triangle
        triangle = Triangle(side_length=4, color="#00ff00")

        # Add the triangle to the scene
        self.add(triangle)

        # Animate the triangle moving up
        self.play(triangle.animate.shift(UP*2), run_time=2)

        # Create a rectangle
        rectangle = Rectangle(width=4, height=2, color="#0000ff")

        # Add the rectangle to the scene
        self.add(rectangle)

        # Animate the rectangle scaling down
        self.play(rectangle.animate.scale(0.5), run_time=2)

        # Create an ellipse
        ellipse = Ellipse(width=4, height=2, color="#ffff00")

        # Add the ellipse to the scene
        self.add(ellipse)

        # Animate the ellipse rotating
        self.play(Rotate(ellipse, angle=PI/2), run_time=2)

        # Create a polygon
        polygon = Polygon([(-2, -2, 0), (2, -2, 0), (2, 2, 0), (-2, 2, 0)], color="#ff00ff")

        # Add the polygon to the scene
        self.add(polygon)

        # Animate the polygon moving down
        self.play(polygon.animate.shift(DOWN*2), run_time=2)

        # Create a line
        line = Line(start=(-4, 0, 0), end=(4, 0, 0), color="#00ffff")

        # Add the line to the scene
        self.add(line)

        # Animate the line scaling up
        self.play(line.animate.scale(1.5), run_time=2)

        # Create a dot
        dot = Dot(point=(0, 0, 0), color="#ffffff")

        # Add the dot to the scene
        self.add(dot)

        # Animate the dot moving right
        self.play(dot.animate.shift(RIGHT*2), run_time=2)

        # Create a star
        star = Star(n=5, outer_radius=2, inner_radius=1, color="#ff0000")

        # Add the star to the scene
        self.add(star)

        # Animate the star rotating
        self.play(Rotate(star, angle=PI/2), run_time=2)

        # Create a regular polygon
        regular_polygon = RegularPolygon(n=6, radius=2, color="#00ff00")

        # Add the regular polygon to the scene
        self.add(regular_polygon)

        # Animate the regular polygon moving up
        self.play(regular_polygon.animate.shift(UP*2), run_time=2)

        # Create an annulus
        annulus = Annulus(inner_radius=1, outer_radius=2, color="#0000ff")

        # Add the annulus to the scene
        self.add(annulus)

        # Animate the annulus scaling down
        self.play(annulus.animate.scale(0.5), run_time=2)

        # Create a sector
        sector = Sector(inner_radius=1, outer_radius=2, angle=PI/2, color="#ffff00")

        # Add the sector to the scene
        self.add(sector)

        # Animate the sector rotating
        self.play(Rotate(sector, angle=PI/2), run_time=2)

        # Create a tangent line
        tangent_line = Line(start=(-2, 0, 0), end=(2, 0, 0), color="#ff00ff")

        # Add the tangent line to the scene
        self.add(tangent_line)

        # Animate the tangent line moving down
        self.play(tangent_line.animate.shift(DOWN*2), run_time=2)

        # Create a cubic Bezier curve
        cubic_bezier_curve = CubicBezier(start=(0, 0, 0), end=(4, 0, 0), anchor1=(2, -2, 0), anchor2=(2, 2, 0), color="#00ffff")

        # Add the cubic Bezier curve to the scene
        self.add(cubic_bezier_curve)

        # Animate the cubic Bezier curve scaling up
        self.play(cubic_bezier_curve.animate.scale(1.5), run_time=2)

        # Create a quadratic Bezier curve
        quadratic_bezier_curve = QuadraticBezier(start=(0, 0, 0), end=(4, 0, 0), anchor=(2, -2, 0), color="#ffffff")

        # Add the quadratic Bezier curve to the scene
        self.add(quadratic_bezier_curve)

        # Animate the quadratic Bezier curve moving right
        self.play(quadratic_bezier_curve.animate.shift(RIGHT*2), run_time=2)

        # Create a function graph
        function_graph = FunctionGraph(lambda x: x**2, x_min=-4, x_max=4, color="#ff0000")

        # Add the function graph to the scene
        self.add(function_graph)

        # Animate the function graph rotating
        self.play(Rotate(function_graph, angle=PI/2), run_time=2)

        # Create a parametric curve
        parametric_curve = ParametricCurve(lambda t: [t**2, t, 0], t_min=-2, t_max=2, color="#00ff00")

        # Add the parametric curve to the scene
        self.add(parametric_curve)

        # Animate the parametric curve moving up
        self.play(parametric_curve.animate.shift(UP*2), run_time=2)

        # Create a three-dimensional surface
        surface = Surface(lambda u, v: [u, v, u**2 + v**2], u_min=-2, u_max=2, v_min=-2, v_max=2, color="#0000ff")

        # Add the surface to the scene
        self.add(surface)

        # Animate the surface scaling down
        self.play(surface.animate.scale(0.5), run_time=2)

        # Create a three-dimensional curve
        curve = ParametricCurve(lambda t: [t, t**2, t**3], t_min=-2, t_max=2, color="#ffff00")

        # Add the curve to the scene
        self.add(curve)

        # Animate the curve rotating
        self.play(Rotate(curve, angle=PI/2), run_time=2)

        # Create a three-dimensional dot
        dot_3d = Dot3D(point=(0, 0, 0), color="#ff00ff")

        # Add the dot to the scene
        self.add(dot_3d)

        # Animate the dot moving right
        self.play(dot_3d.animate.shift(RIGHT*2), run_time=2)

        # Create a three-dimensional line
        line_3d = Line3D(start=(-2, -2, -2), end=(2, 2, 2), color="#00ffff")

        # Add the line to the scene
        self.add(line_3d)

        # Animate the line scaling up
        self.play(line_3d.animate.scale(1.5), run_time=2)

        # Create a three-dimensional plane
        plane = Plane(color="#ffffff")

        # Add the plane to the scene
        self.add(plane)

        # Animate the plane rotating
        self.play(Rotate(plane, angle=PI/2), run_time=2)

        self.wait(60)

        self.play(*[FadeOut(obj) for obj in self.mobjects], run_time=2)

        self.wait(2)