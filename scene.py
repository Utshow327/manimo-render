from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.0
config.frame_width = 14.0 * 9 / 16
config.background_color = WHITE

class ThermodynamicsLaws(Scene):
    def construct(self):
        self.zeroth_law()
        self.wait(0.4)
        
        self.first_law()
        self.wait(0.4)
        
        self.second_law()
        self.wait(0.4)
        
        self.third_law()
        self.wait(0.4)
    
    def zeroth_law(self):
        law_title = Text("Zeroth Law", font_size=52, weight=BOLD)
        law_title.set_color_by_gradient(BLUE, TEAL, GREEN)
        law_title.to_edge(UP, buff=0.6)
        
        subtitle = Text("Thermal Equilibrium", font_size=30, color=DARK_GRAY)
        subtitle.next_to(law_title, DOWN, buff=0.3)
        
        self.play(
            Write(law_title, run_time=1),
            FadeIn(subtitle, shift=DOWN*0.3),
            run_time=1.2
        )
        self.wait(0.3)
        
        # Three systems with moving particles
        system_a = Circle(radius=1, stroke_width=5)
        system_a.set_stroke(RED)
        system_a.set_fill(RED, opacity=0.05)
        
        system_b = Circle(radius=1, stroke_width=5)
        system_b.set_stroke(RED)
        system_b.set_fill(RED, opacity=0.05)
        
        system_c = Circle(radius=1, stroke_width=5)
        system_c.set_stroke(BLUE)
        system_c.set_fill(BLUE, opacity=0.05)
        
        system_a.move_to(UP * 2.5)
        system_b.move_to(DOWN * 0.5)
        system_c.move_to(DOWN * 4)
        
        label_a = Text("A", font_size=36, weight=BOLD)
        label_a.set_color_by_gradient(RED, ORANGE)
        label_a.move_to(system_a.get_center() + LEFT*1.6)
        
        label_b = Text("B", font_size=36, weight=BOLD)
        label_b.set_color_by_gradient(RED, ORANGE)
        label_b.move_to(system_b.get_center() + LEFT*1.6)
        
        label_c = Text("C", font_size=36, weight=BOLD)
        label_c.set_color_by_gradient(BLUE, TEAL)
        label_c.move_to(system_c.get_center() + LEFT*1.6)
        
        # Fast moving particles for hot
        particles_a = VGroup()
        for _ in range(8):
            p = Dot(radius=0.1)
            p.set_color_by_gradient(RED, ORANGE)
            angle = np.random.uniform(0, TAU)
            p.move_to(system_a.get_center() + np.array([np.cos(angle), np.sin(angle), 0]) * 0.6)
            particles_a.add(p)
        
        particles_b = VGroup()
        for _ in range(8):
            p = Dot(radius=0.1)
            p.set_color_by_gradient(RED, ORANGE)
            angle = np.random.uniform(0, TAU)
            p.move_to(system_b.get_center() + np.array([np.cos(angle), np.sin(angle), 0]) * 0.6)
            particles_b.add(p)
        
        # Slow moving particles for cold
        particles_c = VGroup()
        for _ in range(8):
            p = Dot(radius=0.1)
            p.set_color_by_gradient(BLUE, TEAL)
            angle = np.random.uniform(0, TAU)
            p.move_to(system_c.get_center() + np.array([np.cos(angle), np.sin(angle), 0]) * 0.6)
            particles_c.add(p)
        
        self.play(
            Create(system_a),
            Create(system_b),
            Create(system_c),
            Write(label_a),
            Write(label_b),
            Write(label_c),
            LaggedStartMap(FadeIn, particles_a, scale=0.3, lag_ratio=0.1),
            LaggedStartMap(FadeIn, particles_b, scale=0.3, lag_ratio=0.1),
            LaggedStartMap(FadeIn, particles_c, scale=0.3, lag_ratio=0.1),
            run_time=1.5
        )
        
        # Animate particles moving
        def update_particles(particles, center, speed):
            for p in particles:
                angle = np.random.uniform(0, TAU)
                radius = np.random.uniform(0.3, 0.8)
                p.move_to(center + np.array([np.cos(angle), np.sin(angle), 0]) * radius)
        
        # A and B equilibrium
        contact_ab = Line(
            system_a.get_bottom(),
            system_b.get_top(),
            stroke_width=8
        )
        contact_ab.set_color_by_gradient(RED, ORANGE, YELLOW)
        
        self.play(
            Create(contact_ab),
            run_time=0.8
        )
        
        # Heat flow animation
        for _ in range(3):
            self.play(
                *[p.animate.shift(UP*np.random.uniform(-0.15, 0.15) + RIGHT*np.random.uniform(-0.15, 0.15)) for p in particles_a],
                *[p.animate.shift(UP*np.random.uniform(-0.15, 0.15) + RIGHT*np.random.uniform(-0.15, 0.15)) for p in particles_b],
                *[p.animate.shift(UP*np.random.uniform(-0.08, 0.08) + RIGHT*np.random.uniform(-0.08, 0.08)) for p in particles_c],
                run_time=0.4
            )
        
        eq_ab = Text("A = B", font_size=28, weight=BOLD)
        eq_ab.set_color_by_gradient(RED, ORANGE)
        eq_ab.next_to(contact_ab, RIGHT, buff=0.3)
        
        self.play(Write(eq_ab), run_time=0.6)
        
        # B and C equilibrium
        contact_bc = Line(
            system_b.get_bottom(),
            system_c.get_top(),
            stroke_width=8
        )
        contact_bc.set_color_by_gradient(ORANGE, YELLOW, TEAL)
        
        self.play(
            Create(contact_bc),
            run_time=0.8
        )
        
        # C heats up
        new_particles_c = VGroup()
        for _ in range(8):
            p = Dot(radius=0.1)
            p.set_color_by_gradient(RED, ORANGE)
            angle = np.random.uniform(0, TAU)
            p.move_to(system_c.get_center() + np.array([np.cos(angle), np.sin(angle), 0]) * 0.6)
            new_particles_c.add(p)
        
        self.play(
            system_c.animate.set_stroke(RED).set_fill(RED, opacity=0.05),
            Transform(particles_c, new_particles_c),
            label_c.animate.set_color_by_gradient(RED, ORANGE),
            run_time=1.5
        )
        
        for _ in range(3):
            self.play(
                *[p.animate.shift(UP*np.random.uniform(-0.15, 0.15) + RIGHT*np.random.uniform(-0.15, 0.15)) for p in particles_a],
                *[p.animate.shift(UP*np.random.uniform(-0.15, 0.15) + RIGHT*np.random.uniform(-0.15, 0.15)) for p in particles_b],
                *[p.animate.shift(UP*np.random.uniform(-0.15, 0.15) + RIGHT*np.random.uniform(-0.15, 0.15)) for p in particles_c],
                run_time=0.4
            )
        
        eq_bc = Text("B = C", font_size=28, weight=BOLD)
        eq_bc.set_color_by_gradient(ORANGE, RED)
        eq_bc.next_to(contact_bc, RIGHT, buff=0.3)
        
        self.play(Write(eq_bc), run_time=0.6)
        self.wait(0.5)
        
        # Therefore A = C
        conclusion = Text("∴ A = C", font_size=36, weight=BOLD)
        conclusion.set_color_by_gradient(ORANGE, RED, MAROON)
        conclusion.to_edge(DOWN, buff=1)
        
        self.play(Write(conclusion, run_time=1))
        self.wait(0.8)
        
        self.play(
            *[FadeOut(mob, scale=0.7) for mob in self.mobjects],
            run_time=1
        )
    
    def first_law(self):
        law_title = Text("First Law", font_size=52, weight=BOLD)
        law_title.set_color_by_gradient(PURPLE, PINK, MAROON)
        law_title.to_edge(UP, buff=0.6)
        
        subtitle = Text("Energy Conservation", font_size=30, color=DARK_GRAY)
        subtitle.next_to(law_title, DOWN, buff=0.3)
        
        self.play(
            Write(law_title, run_time=1),
            FadeIn(subtitle, shift=DOWN*0.3),
            run_time=1.2
        )
        self.wait(0.3)
        
        equation = MathTex(
            r"\Delta U", "=", "Q", "-", "W",
            font_size=65,
            color=BLACK
        )
        equation.move_to(UP * 1.5)
        equation[0].set_color_by_gradient(PURPLE, PINK)
        equation[2].set_color_by_gradient(RED, ORANGE)
        equation[4].set_color_by_gradient(BLUE, TEAL)
        
        self.play(Write(equation, run_time=1.5))
        self.wait(0.4)
        
        # Visual system
        system = RoundedRectangle(
            width=5, height=3.5,
            corner_radius=0.4,
            stroke_width=6
        )
        system.set_stroke(PURPLE)
        system.set_fill(PURPLE, opacity=0.08)
        system.move_to(DOWN * 2)
        
        # Internal particles
        internal_particles = VGroup()
        for _ in range(12):
            p = Dot(radius=0.12)
            p.set_color_by_gradient(PURPLE, PINK)
            x = np.random.uniform(-2, 2)
            y = np.random.uniform(-1.3, 1.3)
            p.move_to(system.get_center() + RIGHT*x + UP*y)
            internal_particles.add(p)
        
        self.play(
            equation.animate.scale(0.6).move_to(UP * 0.8),
            Create(system),
            LaggedStartMap(FadeIn, internal_particles, scale=0.3, lag_ratio=0.05),
            run_time=1.5
        )
        
        # Heat input - particles entering
        heat_label = Text("Heat In (Q)", font_size=28, weight=BOLD)
        heat_label.set_color_by_gradient(RED, ORANGE)
        heat_label.next_to(system, LEFT, buff=1.2).shift(UP*0.5)
        
        self.play(Write(heat_label), run_time=0.8)
        
        for i in range(4):
            heat_particle = Dot(radius=0.12)
            heat_particle.set_color_by_gradient(RED, ORANGE)
            heat_particle.move_to(system.get_left() + LEFT*1.5 + UP*np.random.uniform(-0.5, 0.5))
            
            self.play(
                FadeIn(heat_particle, scale=0.3),
                heat_particle.animate.move_to(system.get_center() + RIGHT*np.random.uniform(-1.5, 1.5) + UP*np.random.uniform(-1, 1)),
                *[p.animate.shift(UP*np.random.uniform(-0.1, 0.1) + RIGHT*np.random.uniform(-0.1, 0.1)) for p in internal_particles],
                system.animate.set_fill(PURPLE, opacity=0.15),
                run_time=0.6
            )
            internal_particles.add(heat_particle)
        
        # Work output - piston movement
        piston = Rectangle(width=0.4, height=2.5, stroke_width=5)
        piston.set_stroke(BLUE)
        piston.set_fill(BLUE, opacity=0.3)
        piston.next_to(system, RIGHT, buff=0)
        
        work_label = Text("Work Out (W)", font_size=28, weight=BOLD)
        work_label.set_color_by_gradient(BLUE, TEAL)
        work_label.next_to(piston, RIGHT, buff=0.8)
        
        self.play(
            FadeIn(piston, shift=LEFT*0.3),
            Write(work_label),
            run_time=1
        )
        
        # Piston moves as particles push
        for _ in range(3):
            self.play(
                piston.animate.shift(RIGHT*0.25),
                *[p.animate.shift(UP*np.random.uniform(-0.15, 0.15) + RIGHT*np.random.uniform(-0.1, 0.2)) for p in internal_particles],
                run_time=0.5
            )
            self.play(
                piston.animate.shift(LEFT*0.1),
                *[p.animate.shift(UP*np.random.uniform(-0.1, 0.1) + LEFT*np.random.uniform(0, 0.1)) for p in internal_particles],
                run_time=0.3
            )
        
        self.wait(0.8)
        
        self.play(
            *[FadeOut(mob, scale=0.7) for mob in self.mobjects],
            run_time=1
        )
    
    def second_law(self):
        law_title = Text("Second Law", font_size=52, weight=BOLD)
        law_title.set_color_by_gradient(ORANGE, RED, MAROON)
        law_title.to_edge(UP, buff=0.6)
        
        subtitle = Text("Entropy Increases", font_size=30, color=DARK_GRAY)
        subtitle.next_to(law_title, DOWN, buff=0.3)
        
        self.play(
            Write(law_title, run_time=1),
            FadeIn(subtitle, shift=DOWN*0.3),
            run_time=1.2
        )
        self.wait(0.3)
        
        entropy_eq = MathTex(
            r"\Delta S \geq 0",
            font_size=65,
            color=BLACK
        )
        entropy_eq.set_color_by_gradient(ORANGE, RED)
        entropy_eq.move_to(UP * 1.2)
        
        self.play(Write(entropy_eq, run_time=1.5))
        self.wait(0.4)
        
        # Ordered state
        ordered_box = Square(side_length=3, stroke_width=4)
        ordered_box.set_stroke(BLUE)
        ordered_box.set_fill(BLUE, opacity=0.05)
        ordered_box.move_to(UP * 0.3 + LEFT * 1.8)
        
        ordered_label = Text("Ordered", font_size=28, weight=BOLD)
        ordered_label.set_color_by_gradient(BLUE, TEAL)
        ordered_label.next_to(ordered_box, UP, buff=0.3)
        
        ordered_particles = VGroup()
        for i in range(4):
            for j in range(4):
                p = Dot(radius=0.12)
                p.set_color_by_gradient(BLUE, TEAL)
                p.move_to(ordered_box.get_center() + RIGHT*(j-1.5)*0.5 + UP*(i-1.5)*0.5)
                ordered_particles.add(p)
        
        self.play(
            entropy_eq.animate.scale(0.7).move_to(UP * 0.5),
            Create(ordered_box),
            Write(ordered_label),
            LaggedStartMap(FadeIn, ordered_particles, scale=0.3, lag_ratio=0.04),
            run_time=1.5
        )
        
        # Disordered state
        disordered_box = Square(side_length=3, stroke_width=4)
        disordered_box.set_stroke(RED)
        disordered_box.set_fill(RED, opacity=0.05)
        disordered_box.move_to(UP * 0.3 + RIGHT * 1.8)
        
        disordered_label = Text("Disordered", font_size=28, weight=BOLD)
        disordered_label.set_color_by_gradient(RED, ORANGE)
        disordered_label.next_to(disordered_box, UP, buff=0.3)
        
        disordered_particles = VGroup()
        import random
        random.seed(42)
        for _ in range(16):
            p = Dot(radius=0.12)
            p.set_color_by_gradient(RED, ORANGE)
            x = random.uniform(-1.2, 1.2)
            y = random.uniform(-1.2, 1.2)
            p.move_to(disordered_box.get_center() + RIGHT*x + UP*y)
            disordered_particles.add(p)
        
        self.play(
            Create(disordered_box),
            Write(disordered_label),
            LaggedStartMap(FadeIn, disordered_particles, scale=0.3, lag_ratio=0.04),
            run_time=1.5
        )
        
        # Arrow showing direction
        arrow = Arrow(
            ordered_box.get_right() + RIGHT*0.2,
            disordered_box.get_left() + LEFT*0.2,
            stroke_width=10,
            max_tip_length_to_length_ratio=0.3
        )
        arrow.set_color_by_gradient(ORANGE, RED)
        
        time_label = Text("Time →", font_size=32, weight=BOLD)
        time_label.set_color_by_gradient(ORANGE, RED)
        time_label.next_to(arrow, DOWN, buff=0.3)
        
        self.play(
            GrowArrow(arrow),
            Write(time_label),
            run_time=1.2
        )
        
        # Animate transition
        for _ in range(4):
            self.play(
                *[p.animate.shift(UP*np.random.uniform(-0.12, 0.12) + RIGHT*np.random.uniform(-0.12, 0.12)) for p in ordered_particles],
                *[p.animate.shift(UP*np.random.uniform(-0.15, 0.15) + RIGHT*np.random.uniform(-0.15, 0.15)) for p in disordered_particles],
                run_time=0.4
            )
        
        # Drop of ink in water visualization
        ink_demo = Circle(radius=1.5, stroke_width=4)
        ink_demo.set_stroke(GRAY)
        ink_demo.set_fill(GRAY, opacity=0.05)
        ink_demo.move_to(DOWN * 3.5)
        
        ink_label = Text("Ink Drop", font_size=26, color=DARK_GRAY)
        ink_label.next_to(ink_demo, DOWN, buff=0.3)
        
        # Concentrated ink
        ink_drop = Dot(radius=0.2, color=PURPLE)
        ink_drop.move_to(ink_demo.get_center())
        
        self.play(
            Create(ink_demo),
            Write(ink_label),
            FadeIn(ink_drop, scale=0.5),
            run_time=1
        )
        
        # Ink spreads
        spread_particles = VGroup()
        for _ in range(20):
            p = Dot(radius=0.08)
            p.set_color_by_gradient(PURPLE, PINK)
            p.move_to(ink_demo.get_center())
            spread_particles.add(p)
        
        self.play(
            FadeOut(ink_drop),
            *[p.animate.move_to(ink_demo.get_center() + 
                np.array([np.cos(i*TAU/20), np.sin(i*TAU/20), 0]) * np.random.uniform(0.5, 1.2))
                for i, p in enumerate(spread_particles)],
            ink_demo.animate.set_fill(PURPLE, opacity=0.15),
            run_time=2
        )
        
        self.wait(0.8)
        
        self.play(
            *[FadeOut(mob, scale=0.7) for mob in self.mobjects],
            run_time=1
        )
    
    def third_law(self):
        law_title = Text("Third Law", font_size=52, weight=BOLD)
        law_title.set_color_by_gradient(TEAL, GREEN, BLUE)
        law_title.to_edge(UP, buff=0.6)
        
        subtitle = Text("Absolute Zero", font_size=30, color=DARK_GRAY)
        subtitle.next_to(law_title, DOWN, buff=0.3)
        
        self.play(
            Write(law_title, run_time=1),
            FadeIn(subtitle, shift=DOWN*0.3),
            run_time=1.2
        )
        self.wait(0.3)
        
        concept = MathTex(
            r"T \to 0 \text{ K} \Rightarrow S \to 0",
            font_size=55,
            color=BLACK
        )
        concept.set_color_by_gradient(BLUE, TEAL, GREEN)
        concept.move_to(UP * 1.2)
        
        self.play(Write(concept, run_time=2))
        self.wait(0.4)
        
        # Temperature scale with particle motion
        temp_systems = VGroup()
        
        # Hot system
        hot_sys = Circle(radius=0.9, stroke_width=4)
        hot_sys.set_stroke(RED)
        hot_sys.set_fill(RED, opacity=0.1)
        hot_sys.move_to(UP * 0.5 + LEFT * 2.2)
        
        hot_label = Text("300 K", font_size=26, weight=BOLD)
        hot_label.set_color_by_gradient(RED, ORANGE)
        hot_label.next_to(hot_sys, DOWN, buff=0.3)
        
        hot_particles = VGroup()
        for _ in range(10):
            p = Dot(radius=0.08)
            p.set_color_by_gradient(RED, ORANGE)
            angle = np.random.uniform(0, TAU)
            p.move_to(hot_sys.get_center() + np.array([np.cos(angle), np.sin(angle), 0]) * 0.5)
            hot_particles.add(p)
        
        # Warm system
        warm_sys = Circle(radius=0.9, stroke_width=4)
        warm_sys.set_stroke(ORANGE)
        warm_sys.set_fill(ORANGE, opacity=0.1)
        warm_sys.move_to(DOWN * 1.5 + LEFT * 2.2)
        
        warm_label = Text("150 K", font_size=26, weight=BOLD)
        warm_label.set_color_by_gradient(ORANGE, YELLOW)
        warm_label.next_to(warm_sys, DOWN, buff=0.3)
        
        warm_particles = VGroup()
        for _ in range(10):
            p = Dot(radius=0.08)
            p.set_color_by_gradient(ORANGE, YELLOW)
            angle = np.random.uniform(0, TAU)
            p.move_to(warm_sys.get_center() + np.array([np.cos(angle), np.sin(angle), 0]) * 0.4)
            warm_particles.add(p)
        
        # Cold system
        cold_sys = Circle(radius=0.9, stroke_width=4)
        cold_sys.set_stroke(BLUE)
        cold_sys.set_fill(BLUE, opacity=0.1)
        cold_sys.move_to(DOWN * 3.5 + LEFT * 2.2)
        
        cold_label = Text("50 K", font_size=26, weight=BOLD)
        cold_label.set_color_by_gradient(BLUE, TEAL)
        cold_label.next_to(cold_sys, DOWN, buff=0.3)
        
        cold_particles = VGroup()
        for _ in range(10):
            p = Dot(radius=0.08)
            p.set_color_by_gradient(BLUE, TEAL)
            angle = np.random.uniform(0, TAU)
            p.move_to(cold_sys.get_center() + np.array([np.cos(angle), np.sin(angle), 0]) * 0.25)
            cold_particles.add(p)
        
        # Absolute zero
        zero_sys = Circle(radius=0.9, stroke_width=4)
        zero_sys.set_stroke(TEAL)
        zero_sys.set_fill(TEAL, opacity=0.1)
        zero_sys.move_to(DOWN * 5.5 + LEFT * 2.2)
        
        zero_label = Text("0 K", font_size=26, weight=BOLD)
        zero_label.set_color_by_gradient(TEAL, GREEN)
        zero_label.next_to(zero_sys, DOWN, buff=0.3)
        
        zero_particles = VGroup()
        for i in range(10):
            p = Dot(radius=0.08)
            p.set_color_by_gradient(TEAL, GREEN)
            angle = i * TAU / 10
            p.move_to(zero_sys.get_center() + np.array([np.cos(angle), np.sin(angle), 0]) * 0.15)
            zero_particles.add(p)
        
        self.play(
            concept.animate.scale(0.65).move_to(UP * 0.7),
            run_time=0.8
        )
        
        # Show hot system
        self.play(
            Create(hot_sys),
            Write(hot_label),
            LaggedStartMap(FadeIn, hot_particles, scale=0.3, lag_ratio=0.05),
            run_time=1
        )
        
        # Particles move fast
        for _ in range(3):
            self.play(
                *[p.animate.shift(UP*np.random.uniform(-0.2, 0.2) + RIGHT*np.random.uniform(-0.2, 0.2)) for p in hot_particles],
                run_time=0.3
            )
        
        # Show warm system
        self.play(
            Create(warm_sys),
            Write(warm_label),
            LaggedStartMap(FadeIn, warm_particles, scale=0.3, lag_ratio=0.05),
            run_time=1
        )
        
        # Particles move medium
        for _ in range(3):
            self.play(
                *[p.animate.shift(UP*np.random.uniform(-0.15, 0.15) + RIGHT*np.random.uniform(-0.15, 0.15)) for p in hot_particles],
                *[p.animate.shift(UP*np.random.uniform(-0.12, 0.12) + RIGHT*np.random.uniform(-0.12, 0.12)) for p in warm_particles],
                run_time=0.3
            )
        
        # Show cold system
        self.play(
            Create(cold_sys),
            Write(cold_label),
            LaggedStartMap(FadeIn, cold_particles, scale=0.3, lag_ratio=0.05),
            run_time=1
        )
        
        # Particles move slow
        for _ in range(3):
            self.play(
                *[p.animate.shift(UP*np.random.uniform(-0.15, 0.15) + RIGHT*np.random.uniform(-0.15, 0.15)) for p in hot_particles],
                *[p.animate.shift(UP*np.random.uniform(-0.12, 0.12) + RIGHT*np.random.uniform(-0.12, 0.12)) for p in warm_particles],
                *[p.animate.shift(UP*np.random.uniform(-0.06, 0.06) + RIGHT*np.random.uniform(-0.06, 0.06)) for p in cold_particles],
                run_time=0.3
            )
        
        # Show absolute zero
        self.play(
            Create(zero_sys),
            Write(zero_label),
            LaggedStartMap(FadeIn, zero_particles, scale=0.3, lag_ratio=0.05),
            run_time=1
        )
        
        # Particles barely move then stop
        for _ in range(2):
            self.play(
                *[p.animate.shift(UP*np.random.uniform(-0.15, 0.15) + RIGHT*np.random.uniform(-0.15, 0.15)) for p in hot_particles],
                *[p.animate.shift(UP*np.random.uniform(-0.12, 0.12) + RIGHT*np.random.uniform(-0.12, 0.12)) for p in warm_particles],
                *[p.animate.shift(UP*np.random.uniform(-0.06, 0.06) + RIGHT*np.random.uniform(-0.06, 0.06)) for p in cold_particles],
                *[p.animate.shift(UP*np.random.uniform(-0.02, 0.02) + RIGHT*np.random.uniform(-0.02, 0.02)) for p in zero_particles],
                run_time=0.3
            )
        
        # Final state - all particles stop at absolute zero
        self.play(
            *[p.animate.shift(UP*np.random.uniform(-0.15, 0.15) + RIGHT*np.random.uniform(-0.15, 0.15)) for p in hot_particles],
            *[p.animate.shift(UP*np.random.uniform(-0.12, 0.12) + RIGHT*np.random.uniform(-0.12, 0.12)) for p in warm_particles],
            *[p.animate.shift(UP*np.random.uniform(-0.06, 0.06) + RIGHT*np.random.uniform(-0.06, 0.06)) for p in cold_particles],
            zero_sys.animate.set_fill(TEAL, opacity=0.2),
            run_time=0.5
        )
        
        # Highlight no motion at absolute zero
        zero_glow = Circle(radius=1.1, stroke_width=0)
        zero_glow.set_fill(TEAL, opacity=0.3)
        zero_glow.move_to(zero_sys.get_center())
        
        no_motion = Text("No Motion\nZero Entropy", font_size=28, weight=BOLD)
        no_motion.set_color_by_gradient(TEAL, GREEN)
        no_motion.move_to(RIGHT * 1.8 + DOWN * 5.5)
        
        arrow_to_zero = Arrow(
            no_motion.get_left(),
            zero_sys.get_right(),
            stroke_width=6
        )
        arrow_to_zero.set_color_by_gradient(TEAL, GREEN)
        
        self.play(
            FadeIn(zero_glow, scale=0.8),
            GrowArrow(arrow_to_zero),
            Write(no_motion),
            run_time=1.5
        )
        
        self.play(
            zero_glow.animate.scale(1.3).set_opacity(0),
            run_time=1
        )
        
        self.wait(1)
        
        self.play(
            *[FadeOut(mob, scale=0.7) for mob in self.mobjects],
            run_time=1
        )