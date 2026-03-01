from manim import *
import numpy as np

config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920

class VectorFieldsExplainer(Scene):
    def construct(self):
        self.camera.background_color = "#000000"
        
        # Gravitational Field
        self.show_gravitational_field()
        
        # Electric Field
        self.show_electric_field()
        
        # Magnetic Field
        self.show_magnetic_field()
    
    def show_gravitational_field(self):
        # Title
        grav_title = Text("GRAVITATIONAL FIELD", font_size=56, weight=BOLD)
        grav_title.set_color_by_gradient(ORANGE, RED)
        grav_title.to_edge(UP, buff=0.5)
        
        desc = Text("Mass attracts mass", font_size=28, color=GRAY_A)
        desc.next_to(grav_title, DOWN, buff=0.3)
        
        self.play(
            Write(grav_title, run_time=1),
            FadeIn(desc, shift=DOWN*0.2)
        )
        self.wait(0.5)
        
        # Central mass (planet/star)
        center = ORIGIN + UP*0.3
        planet = Circle(radius=0.5, color=ORANGE, fill_opacity=1, stroke_width=0)
        planet.move_to(center)
        planet.set_sheen(-0.8, UP)
        
        # Glow effect
        glow_layers = VGroup()
        for i in range(5):
            glow = Circle(radius=0.5 + i*0.15, color=ORANGE, fill_opacity=0.1/(i+1), stroke_width=0)
            glow.move_to(center)
            glow_layers.add(glow)
        
        self.play(
            FadeIn(planet, scale=0.5),
            FadeIn(glow_layers, lag_ratio=0.2),
            run_time=1.2
        )
        self.wait(0.3)
        
        # Radial gravitational field vectors pointing INWARD
        field_vectors = VGroup()
        for r in np.linspace(1.2, 3.5, 8):
            num_vectors = int(12 * r)
            for i in range(num_vectors):
                angle = (i / num_vectors) * 2 * PI
                pos = center + r * np.array([np.cos(angle), np.sin(angle), 0])
                
                # Vector points TOWARD center (attraction)
                direction = center - pos
                dist = np.linalg.norm(direction)
                if dist > 0:
                    direction = direction / dist
                    
                # Length inversely proportional to distance squared
                length = 0.5 / (r**1.5)
                end = pos + direction * length
                
                # Color fades with distance
                color = interpolate_color(RED, ORANGE, (r - 1.2) / 2.3)
                arrow = Arrow(pos, end, buff=0, stroke_width=4, 
                            color=color, max_tip_length_to_length_ratio=0.3)
                field_vectors.add(arrow)
        
        self.play(
            LaggedStart(*[GrowArrow(arrow) for arrow in field_vectors],
                       lag_ratio=0.008, run_time=2)
        )
        self.wait(0.5)
        
        # Test mass orbiting
        test_mass = Dot(radius=0.12, color=BLUE)
        test_mass.set_sheen(-0.5, UP)
        orbit_radius = 2.2
        test_mass.move_to(center + RIGHT * orbit_radius)
        
        trail = TracedPath(test_mass.get_center, stroke_width=2, stroke_color=BLUE, stroke_opacity=0.6)
        self.add(trail)
        
        self.play(FadeIn(test_mass, scale=0.5))
        
        # Orbit animation
        self.play(
            Rotate(test_mass, angle=4*PI, about_point=center, run_time=4, rate_func=linear)
        )
        self.wait(0.3)
        
        # Add another falling mass
        falling_mass = Dot(radius=0.1, color=YELLOW)
        falling_mass.set_sheen(-0.5, UP)
        falling_mass.move_to(center + UP*3.5 + RIGHT*1)
        
        falling_trail = TracedPath(falling_mass.get_center, stroke_width=2, stroke_color=YELLOW, stroke_opacity=0.6)
        self.add(falling_trail)
        
        self.play(FadeIn(falling_mass, scale=0.5))
        
        # Fall toward planet in spiral
        fall_path = []
        current_angle = np.arctan2(1, 3.5)
        current_r = np.sqrt(1**2 + 3.5**2)
        
        for i in range(60):
            current_r -= 0.04
            current_angle += 0.08
            if current_r < 0.6:
                current_r = 0.6
            pos = center + current_r * np.array([np.cos(current_angle), np.sin(current_angle), 0])
            fall_path.append(pos)
        
        self.play(
            MoveAlongPath(falling_mass, VMobject().set_points_as_corners(fall_path)),
            Rotate(test_mass, angle=2*PI, about_point=center, rate_func=linear),
            run_time=2.5
        )
        self.wait(0.5)
        
        # Formula
        formula = MathTex(
            r"\vec{F} = -\frac{GMm}{r^2}\hat{r}",
            font_size=48,
            color=ORANGE
        )
        formula.to_edge(DOWN, buff=0.8)
        formula_box = SurroundingRectangle(formula, buff=0.25, color=ORANGE, stroke_width=2)
        
        self.play(
            Write(formula),
            Create(formula_box),
            run_time=1.2
        )
        self.wait(1.2)
        
        self.play(
            FadeOut(grav_title),
            FadeOut(desc),
            FadeOut(planet),
            FadeOut(glow_layers),
            FadeOut(field_vectors),
            FadeOut(test_mass),
            FadeOut(falling_mass),
            FadeOut(trail),
            FadeOut(falling_trail),
            FadeOut(formula),
            FadeOut(formula_box),
            run_time=1
        )
        self.wait(0.3)
    
    def show_electric_field(self):
        # Title
        elec_title = Text("ELECTRIC FIELD", font_size=56, weight=BOLD)
        elec_title.set_color_by_gradient(BLUE, PURPLE)
        elec_title.to_edge(UP, buff=0.5)
        
        desc = Text("Opposite charges attract", font_size=28, color=GRAY_A)
        desc.next_to(elec_title, DOWN, buff=0.3)
        
        self.play(
            Write(elec_title, run_time=1),
            FadeIn(desc, shift=DOWN*0.2)
        )
        self.wait(0.5)
        
        # Positive charge on left
        pos_charge_center = LEFT * 2 + UP * 0.5
        pos_charge = Circle(radius=0.4, color=RED, fill_opacity=1, stroke_width=3, stroke_color=WHITE)
        pos_charge.move_to(pos_charge_center)
        pos_label = Text("+", font_size=80, color=WHITE, weight=BOLD)
        pos_label.move_to(pos_charge_center)
        
        # Negative charge on right
        neg_charge_center = RIGHT * 2 + UP * 0.5
        neg_charge = Circle(radius=0.4, color=BLUE, fill_opacity=1, stroke_width=3, stroke_color=WHITE)
        neg_charge.move_to(neg_charge_center)
        neg_label = Text("−", font_size=80, color=WHITE, weight=BOLD)
        neg_label.move_to(neg_charge_center)
        
        # Electric glow
        pos_glow = VGroup()
        for i in range(4):
            g = Circle(radius=0.4 + i*0.2, color=RED, fill_opacity=0.08/(i+1), stroke_width=0)
            g.move_to(pos_charge_center)
            pos_glow.add(g)
        
        neg_glow = VGroup()
        for i in range(4):
            g = Circle(radius=0.4 + i*0.2, color=BLUE, fill_opacity=0.08/(i+1), stroke_width=0)
            g.move_to(neg_charge_center)
            neg_glow.add(g)
        
        self.play(
            FadeIn(pos_charge, scale=0.5),
            FadeIn(neg_charge, scale=0.5),
            FadeIn(pos_glow, lag_ratio=0.2),
            FadeIn(neg_glow, lag_ratio=0.2),
            run_time=1
        )
        self.play(
            Write(pos_label),
            Write(neg_label)
        )
        self.wait(0.4)
        
        # Electric field lines (dipole field)
        field_lines = VGroup()
        
        # Lines from positive to negative
        num_lines = 16
        for i in range(num_lines):
            angle = (i / num_lines) * 2 * PI
            
            # Start from positive charge
            start_point = pos_charge_center + 0.5 * np.array([np.cos(angle), np.sin(angle), 0])
            
            # Create curved path to negative charge
            points = [start_point]
            current_pos = start_point.copy()
            
            for step in range(40):
                # Calculate field at current position
                to_pos = pos_charge_center - current_pos
                to_neg = neg_charge_center - current_pos
                
                dist_pos = np.linalg.norm(to_pos)
                dist_neg = np.linalg.norm(to_neg)
                
                if dist_pos > 0.1 and dist_neg > 0.1:
                    field_pos = -to_pos / (dist_pos**2.5)
                    field_neg = to_neg / (dist_neg**2.5)
                    total_field = field_pos + field_neg
                    
                    # Normalize
                    mag = np.linalg.norm(total_field)
                    if mag > 0.01:
                        total_field = total_field / mag
                        current_pos += total_field * 0.08
                        points.append(current_pos.copy())
                    else:
                        break
                    
                    # Stop if reached negative charge
                    if dist_neg < 0.6:
                        break
                else:
                    break
            
            if len(points) > 5:
                line = VMobject(stroke_width=2.5)
                line.set_points_as_corners(points)
                line.set_color_by_gradient(RED, PURPLE, BLUE)
                field_lines.add(line)
        
        self.play(
            LaggedStart(*[Create(line) for line in field_lines],
                       lag_ratio=0.05, run_time=2.5)
        )
        self.wait(0.5)
        
        # Test charges moving
        test_positive = Dot(radius=0.1, color=YELLOW)
        test_positive.move_to(UP * 3 + LEFT * 0.5)
        test_pos_label = Text("+", font_size=30, color=WHITE)
        test_pos_label.move_to(test_positive.get_center())
        
        test_negative = Dot(radius=0.1, color=TEAL)
        test_negative.move_to(DOWN * 2.5 + RIGHT * 0.5)
        test_neg_label = Text("−", font_size=30, color=WHITE)
        test_neg_label.move_to(test_negative.get_center())
        
        self.play(
            FadeIn(test_positive, scale=0.5),
            FadeIn(test_negative, scale=0.5),
            FadeIn(test_pos_label),
            FadeIn(test_neg_label)
        )
        
        # Move test charges
        # Positive test charge: repelled by + , attracted to -
        pos_target = RIGHT * 1.5 + DOWN * 0.3
        # Negative test charge: attracted to +, repelled by -
        neg_target = LEFT * 1.5 + UP * 1.3
        
        self.play(
            test_positive.animate.move_to(pos_target),
            test_pos_label.animate.move_to(pos_target),
            test_negative.animate.move_to(neg_target),
            test_neg_label.animate.move_to(neg_target),
            run_time=2,
            rate_func=smooth
        )
        self.wait(0.5)
        
        # Formula
        formula = MathTex(
            r"\vec{E} = \frac{kQ}{r^2}\hat{r}",
            font_size=48,
            color=PURPLE
        )
        formula.to_edge(DOWN, buff=0.8)
        formula_box = SurroundingRectangle(formula, buff=0.25, color=PURPLE, stroke_width=2)
        
        self.play(
            Write(formula),
            Create(formula_box),
            run_time=1.2
        )
        self.wait(1.2)
        
        self.play(
            FadeOut(elec_title),
            FadeOut(desc),
            FadeOut(pos_charge),
            FadeOut(neg_charge),
            FadeOut(pos_label),
            FadeOut(neg_label),
            FadeOut(pos_glow),
            FadeOut(neg_glow),
            FadeOut(field_lines),
            FadeOut(test_positive),
            FadeOut(test_negative),
            FadeOut(test_pos_label),
            FadeOut(test_neg_label),
            FadeOut(formula),
            FadeOut(formula_box),
            run_time=1
        )
        self.wait(0.3)
    
    def show_magnetic_field(self):
        # Title
        mag_title = Text("MAGNETIC FIELD", font_size=56, weight=BOLD)
        mag_title.set_color_by_gradient(GREEN, TEAL)
        mag_title.to_edge(UP, buff=0.5)
        
        desc = Text("Moving charges create fields", font_size=28, color=GRAY_A)
        desc.next_to(mag_title, DOWN, buff=0.3)
        
        self.play(
            Write(mag_title, run_time=1),
            FadeIn(desc, shift=DOWN*0.2)
        )
        self.wait(0.5)
        
        # Wire with current (vertical)
        wire_top = UP * 3.5
        wire_bottom = DOWN * 3.5
        wire = Line(wire_top, wire_bottom, stroke_width=8, color=GRAY)
        
        self.play(Create(wire))
        self.wait(0.3)
        
        # Current arrow
        current_arrow = Arrow(UP*2.5, UP*1.5, buff=0, stroke_width=6, color=YELLOW, max_tip_length_to_length_ratio=0.3)
        current_label = Text("I", font_size=36, color=YELLOW, weight=BOLD)
        current_label.next_to(current_arrow, RIGHT, buff=0.2)
        
        self.play(
            GrowArrow(current_arrow),
            Write(current_label)
        )
        self.wait(0.3)
        
        # Electrons flowing (animation)
        electrons = VGroup()
        for i in range(12):
            y_pos = 3.5 - i * 0.6
            electron = Dot(point=[0, y_pos, 0], radius=0.08, color=BLUE)
            electron.set_sheen(-0.5, UP)
            electrons.add(electron)
        
        self.play(FadeIn(electrons, lag_ratio=0.1))
        
        # Animate electrons flowing down
        for _ in range(2):
            self.play(
                electrons.animate.shift(DOWN * 3.6),
                run_time=1.5,
                rate_func=linear
            )
            electrons.shift(UP * 3.6)
        
        self.wait(0.3)
        
        # Circular magnetic field lines (right-hand rule)
        field_circles = VGroup()
        for radius in np.linspace(0.8, 3.2, 8):
            circle = Circle(radius=radius, color=GREEN, stroke_width=3)
            circle.set_stroke(opacity=0.7)
            
            # Add directional arrows (counterclockwise when current goes up)
            # Since current goes down in our case, circles go clockwise
            num_arrows = int(4 * radius)
            for i in range(num_arrows):
                angle = (i / num_arrows) * 2 * PI
                pos = radius * np.array([np.cos(angle), np.sin(angle), 0])
                
                # Tangent direction (clockwise)
                tangent_angle = angle - PI/2
                tangent = 0.15 * np.array([np.cos(tangent_angle), np.sin(tangent_angle), 0])
                
                arrow = Arrow(pos - tangent/2, pos + tangent/2, buff=0, 
                            stroke_width=2.5, color=TEAL, max_tip_length_to_length_ratio=0.4)
                field_circles.add(arrow)
            
            field_circles.add(circle)
        
        self.play(
            LaggedStart(*[Create(obj) if isinstance(obj, Circle) else GrowArrow(obj) 
                         for obj in field_circles],
                       lag_ratio=0.01, run_time=2.5)
        )
        
        # Continue electron flow
        self.play(
            electrons.animate.shift(DOWN * 3.6),
            run_time=1.5,
            rate_func=linear
        )
        electrons.shift(UP * 3.6)
        
        self.wait(0.5)
        
        # Add compass needles showing field direction
        compasses = VGroup()
        compass_positions = [
            LEFT*2 + UP*1.5,
            RIGHT*2 + UP*1.5,
            LEFT*2 + DOWN*1.5,
            RIGHT*2 + DOWN*1.5,
        ]
        
        for pos in compass_positions:
            # Calculate magnetic field direction at this point
            # Field circles clockwise, so tangent is perpendicular to radius
            radius_vec = pos
            angle = np.arctan2(pos[1], pos[0])
            field_angle = angle - PI/2
            
            needle = Arrow(
                pos - 0.3*np.array([np.cos(field_angle), np.sin(field_angle), 0]),
                pos + 0.3*np.array([np.cos(field_angle), np.sin(field_angle), 0]),
                buff=0,
                stroke_width=4,
                color=RED,
                max_tip_length_to_length_ratio=0.25
            )
            
            compass_circle = Circle(radius=0.4, stroke_width=2, color=WHITE)
            compass_circle.move_to(pos)
            
            compasses.add(VGroup(compass_circle, needle))
        
        self.play(
            LaggedStart(*[FadeIn(comp, scale=0.5) for comp in compasses],
                       lag_ratio=0.2, run_time=1.5)
        )
        self.wait(0.5)
        
        # Reverse current direction
        reverse_arrow = Arrow(UP*1.5, UP*2.5, buff=0, stroke_width=6, color=YELLOW, max_tip_length_to_length_ratio=0.3)
        
        self.play(
            Transform(current_arrow, reverse_arrow),
            electrons.animate.shift(UP * 3.6),
            run_time=1,
            rate_func=smooth
        )
        
        # Flip compass needles
        for comp in compasses:
            needle = comp[1]
            self.play(
                Rotate(needle, angle=PI, about_point=needle.get_center()),
                run_time=0.6
            )
        
        self.wait(0.5)
        
        # Formula
        formula = MathTex(
            r"\vec{B} = \frac{\mu_0 I}{2\pi r}\hat{\theta}",
            font_size=48,
            color=GREEN
        )
        formula.to_edge(DOWN, buff=0.8)
        formula_box = SurroundingRectangle(formula, buff=0.25, color=GREEN, stroke_width=2)
        
        self.play(
            Write(formula),
            Create(formula_box),
            run_time=1.2
        )
        self.wait(1.2)
        
        self.play(
            FadeOut(mag_title),
            FadeOut(desc),
            FadeOut(wire),
            FadeOut(current_arrow),
            FadeOut(current_label),
            FadeOut(electrons),
            FadeOut(field_circles),
            FadeOut(compasses),
            FadeOut(formula),
            FadeOut(formula_box),
            run_time=1
        )
        self.wait(0.5)