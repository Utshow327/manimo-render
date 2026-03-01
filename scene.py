from manim import *
import numpy as np

# Configure for 9:16 aspect ratio (shorts format)
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0
config.background_color = WHITE

class InvestigativeAnimation(Scene):
    def construct(self):
        # Color system: Blue to purple gradient
        GRADIENT_START = "#4A90E2"  # Soft blue
        GRADIENT_END = "#9B59B6"    # Soft purple
        ACCENT_1 = "#5DADE2"        # Light blue
        ACCENT_2 = "#AF7AC5"        # Light purple
        GRADIENT_MID = "#7A7FD9"    # Mid purple-blue
        
        # Helper function to create gradient fills
        def create_gradient_fill(mobject, start_color=GRADIENT_START, end_color=GRADIENT_END):
            mobject.set_fill(color=[start_color, end_color], opacity=0.8)
            mobject.set_stroke(width=0)
            return mobject
        
        # Scene 1: Single human silhouette with floating creative shapes
        # Duration: ~5 seconds
        
        # Create human silhouette
        silhouette = self.create_human_silhouette().scale(1.5)
        silhouette.move_to(UP * 2)
        create_gradient_fill(silhouette)
        
        # Create floating abstract shapes representing creativity and music
        creative_shapes = VGroup()
        for i in range(8):
            if i % 3 == 0:
                shape = Circle(radius=0.2 + np.random.random() * 0.12)
            elif i % 3 == 1:
                shape = RoundedRectangle(
                    width=0.4 + np.random.random() * 0.2,
                    height=0.3 + np.random.random() * 0.15,
                    corner_radius=0.06
                )
            else:
                shape = RegularPolygon(n=6, radius=0.18 + np.random.random() * 0.1)
            
            create_gradient_fill(shape, ACCENT_1, ACCENT_2)
            angle = i * 2 * PI / 8
            radius = 2.5 + np.random.random() * 0.6
            shape.move_to(silhouette.get_center() + np.array([
                radius * np.cos(angle),
                radius * np.sin(angle),
                0
            ]))
            creative_shapes.add(shape)
        
        # Animate scene 1
        self.play(
            FadeIn(silhouette, scale=0.95),
            run_time=1.5,
            rate_func=smooth
        )
        self.play(
            LaggedStart(*[
                FadeIn(shape, scale=0.8)
                for shape in creative_shapes
            ], lag_ratio=0.15),
            run_time=2,
            rate_func=smooth
        )
        
        # Floating animation
        floating_anims = []
        for shape in creative_shapes:
            original_pos = shape.get_center()
            offset = np.array([
                (np.random.random() - 0.5) * 0.3,
                (np.random.random() - 0.5) * 0.3,
                0
            ])
            floating_anims.append(
                shape.animate.shift(offset).set_opacity(0.9)
            )
        
        self.play(
            *floating_anims,
            run_time=2,
            rate_func=there_and_back
        )
        
        # Scene 2: Transition to abstract documents emerging
        # Duration: ~4 seconds
        
        # Create abstract document shapes
        documents = VGroup()
        for i in range(12):
            doc = RoundedRectangle(
                width=1.5,
                height=2.0,
                corner_radius=0.1
            )
            create_gradient_fill(doc, GRADIENT_START, GRADIENT_MID)
            
            # Position in a scattered formation (vertical spread)
            row = i // 3
            col = i % 3
            x_pos = (col - 1) * 2.5 + (np.random.random() - 0.5) * 0.5
            y_pos = (2 - row) * 3.5 + (np.random.random() - 0.5) * 0.5
            doc.move_to(np.array([x_pos, y_pos, 0]))
            doc.set_opacity(0)
            documents.add(doc)
        
        # Fade out creative shapes and silhouette while documents emerge
        self.play(
            LaggedStart(*[
                FadeOut(shape, scale=0.9)
                for shape in creative_shapes
            ], lag_ratio=0.1),
            silhouette.animate.scale(0.85).set_opacity(0.3),
            run_time=1.5,
            rate_func=smooth
        )
        
        self.play(
            LaggedStart(*[
                doc.animate.set_opacity(0.8).scale(0.95)
                for doc in documents
            ], lag_ratio=0.08),
            run_time=2.5,
            rate_func=smooth
        )
        
        # Scene 3: Documents stack and float to center
        # Duration: ~4 seconds
        
        # Create stacking positions
        stack_center = UP * 1
        stack_positions = []
        for i in range(12):
            row = i // 3
            col = i % 3
            offset = np.array([
                (col - 1) * 0.2,
                (2 - row) * 0.18,
                0
            ])
            stack_positions.append(stack_center + offset)
        
        # Animate documents moving to stack
        self.play(
            silhouette.animate.set_opacity(0).scale(0.5),
            run_time=0.8,
            rate_func=smooth
        )
        self.remove(silhouette)
        
        stack_anims = []
        for doc, pos in zip(documents, stack_positions):
            stack_anims.append(
                doc.animate.move_to(pos).rotate(
                    (np.random.random() - 0.5) * 0.1
                )
            )
        
        self.play(
            *stack_anims,
            run_time=2.5,
            rate_func=smooth
        )
        
        # Gentle floating motion
        self.play(
            documents.animate.shift(UP * 0.1),
            run_time=1,
            rate_func=there_and_back
        )
        
        # Scene 4: Documents move to focal area for examination
        # Duration: ~3 seconds
        
        # Create examination area (subtle glow effect)
        examination_area = Circle(radius=3.2)
        examination_area.set_fill(color=[ACCENT_1, GRADIENT_MID], opacity=0.1)
        examination_area.set_stroke(color=GRADIENT_MID, width=2, opacity=0.3)
        
        self.play(
            FadeIn(examination_area, scale=0.98),
            documents.animate.arrange_in_grid(rows=4, cols=3, buff=0.3).move_to(UP * 1),
            run_time=2.5,
            rate_func=smooth
        )
        
        self.wait(0.5)
        
        # Scene 5: Asset transfer - flowing shapes from one cluster to another
        # Duration: ~5 seconds
        
        # Fade out documents and examination area
        self.play(
            FadeOut(documents, scale=0.95),
            FadeOut(examination_area, scale=1.02),
            run_time=1.5,
            rate_func=smooth
        )
        
        # Create source cluster (top)
        source_cluster = VGroup()
        for i in range(6):
            shape = Circle(radius=0.3 + np.random.random() * 0.12)
            create_gradient_fill(shape, GRADIENT_START, GRADIENT_MID)
            angle = i * PI / 3
            radius = 0.7
            shape.move_to(UP * 4.5 + np.array([
                radius * np.cos(angle),
                radius * np.sin(angle),
                0
            ]))
            source_cluster.add(shape)
        
        # Create destination cluster (bottom)
        dest_cluster = VGroup()
        for i in range(6):
            shape = Circle(radius=0.3 + np.random.random() * 0.12)
            create_gradient_fill(shape, GRADIENT_MID, GRADIENT_END)
            angle = i * PI / 3 + PI / 6
            radius = 0.7
            shape.move_to(DOWN * 4.5 + np.array([
                radius * np.cos(angle),
                radius * np.sin(angle),
                0
            ]))
            dest_cluster.add(shape)
        
        # Create flowing assets
        flowing_assets = VGroup()
        for i in range(5):
            asset = Circle(radius=0.18)
            create_gradient_fill(asset, ACCENT_1, ACCENT_2)
            asset.move_to(UP * 4.5)
            asset.set_opacity(0)
            flowing_assets.add(asset)
        
        # Animate clusters appearing
        self.play(
            LaggedStart(*[
                FadeIn(shape, scale=0.9)
                for shape in source_cluster
            ], lag_ratio=0.1),
            LaggedStart(*[
                FadeIn(shape, scale=0.9)
                for shape in dest_cluster
            ], lag_ratio=0.1),
            run_time=1.5,
            rate_func=smooth
        )
        
        # Create glowing gradient path (vertical)
        path = CubicBezier(
            UP * 4.5,
            UP * 2 + LEFT * 1.5,
            DOWN * 2 + RIGHT * 1.5,
            DOWN * 4.5
        )
        path.set_stroke(color=[ACCENT_1, GRADIENT_MID, ACCENT_2], width=5, opacity=0.4)
        
        self.play(
            Create(path),
            run_time=1.5,
            rate_func=smooth
        )
        
        # Animate assets flowing along path
        for asset in flowing_assets:
            self.play(
                FadeIn(asset, scale=0.8),
                MoveAlongPath(asset, path),
                FadeOut(asset, scale=1.1),
                run_time=1.2,
                rate_func=smooth
            )
        
        # Scene 6: Secondary cluster showing connection
        # Duration: ~4 seconds
        
        # Create connected cluster (appears to the side of destination)
        connected_cluster = VGroup()
        for i in range(4):
            shape = RoundedRectangle(width=0.5, height=0.4, corner_radius=0.1)
            create_gradient_fill(shape, GRADIENT_END, ACCENT_2)
            angle = i * PI / 2
            radius = 0.6
            shape.move_to(DOWN * 4.5 + RIGHT * 3 + np.array([
                radius * np.cos(angle),
                radius * np.sin(angle),
                0
            ]))
            connected_cluster.add(shape)
        
        # Connection lines
        connection_lines = VGroup()
        for shape in connected_cluster:
            line = Line(
                dest_cluster.get_center(),
                shape.get_center(),
                buff=0.3
            )
            line.set_stroke(color=[GRADIENT_MID, GRADIENT_END], width=3, opacity=0.3)
            connection_lines.add(line)
        
        self.play(
            FadeOut(path, scale=1.02),
            run_time=0.5,
            rate_func=smooth
        )
        
        self.play(
            LaggedStart(*[
                Create(line)
                for line in connection_lines
            ], lag_ratio=0.15),
            run_time=1.5,
            rate_func=smooth
        )
        
        self.play(
            LaggedStart(*[
                FadeIn(shape, scale=0.9)
                for shape in connected_cluster
            ], lag_ratio=0.1),
            run_time=1.5,
            rate_func=smooth
        )
        
        self.wait(0.5)
        
        # Scene 7: Public structure with private flow
        # Duration: ~5 seconds
        
        # Fade out previous elements
        self.play(
            FadeOut(source_cluster, scale=0.95),
            FadeOut(dest_cluster, scale=0.95),
            FadeOut(connected_cluster, scale=0.95),
            FadeOut(connection_lines, scale=0.95),
            run_time=1.5,
            rate_func=smooth
        )
        
        # Create public-facing structure (open form)
        public_structure = VGroup()
        outer_ring = Circle(radius=2.5)
        outer_ring.set_stroke(color=[GRADIENT_START, GRADIENT_MID], width=5, opacity=0.6)
        outer_ring.set_fill(opacity=0)
        public_structure.add(outer_ring)
        
        for i in range(6):
            pillar = RoundedRectangle(width=0.4, height=1.2, corner_radius=0.06)
            create_gradient_fill(pillar, ACCENT_1, GRADIENT_MID)
            angle = i * PI / 3
            pillar.move_to(np.array([
                2.5 * np.cos(angle),
                2.5 * np.sin(angle),
                0
            ]))
            pillar.rotate(angle + PI / 2)
            public_structure.add(pillar)
        
        public_structure.move_to(UP * 3.5)
        
        # Create private enclosed space
        private_space = VGroup()
        private_box = RoundedRectangle(width=3.0, height=3.0, corner_radius=0.25)
        create_gradient_fill(private_box, GRADIENT_MID, GRADIENT_END)
        private_box.set_opacity(0.6)
        
        lock_shape = Circle(radius=0.5)
        create_gradient_fill(lock_shape, GRADIENT_END, ACCENT_2)
        lock_shape.move_to(private_box.get_center())
        
        private_space.add(private_box, lock_shape)
        private_space.move_to(DOWN * 3.5)
        
        # Animate structures appearing
        self.play(
            FadeIn(public_structure, scale=0.95),
            FadeIn(private_space, scale=0.95),
            run_time=2,
            rate_func=smooth
        )
        
        # Create flow from public to private (vertical)
        flow_path = Line(UP * 3.5, DOWN * 3.5)
        flow_path.set_stroke(width=0)
        
        flowing_particles = VGroup()
        for i in range(8):
            particle = Circle(radius=0.12)
            create_gradient_fill(particle, ACCENT_1, ACCENT_2)
            particle.move_to(UP * 3.5)
            particle.set_opacity(0)
            flowing_particles.add(particle)
        
        # Animate particles flowing
        for i, particle in enumerate(flowing_particles):
            self.play(
                FadeIn(particle, scale=0.8),
                particle.animate.move_to(DOWN * 3.5),
                FadeOut(particle, scale=1.1),
                run_time=0.8,
                rate_func=smooth
            )
            if i < len(flowing_particles) - 1:
                self.wait(0.15)
        
        # Scene 8: Handshake motion
        # Duration: ~4 seconds
        
        # Fade out structures
        self.play(
            FadeOut(public_structure, scale=0.95),
            FadeOut(private_space, scale=0.95),
            run_time=1.5,
            rate_func=smooth
        )
        
        # Create abstract hands
        left_hand = self.create_abstract_hand().move_to(UP * 4)
        create_gradient_fill(left_hand, GRADIENT_START, GRADIENT_MID)
        left_hand.rotate(PI / 2)
        
        right_hand = self.create_abstract_hand().move_to(DOWN * 4)
        right_hand.rotate(-PI / 2)
        create_gradient_fill(right_hand, GRADIENT_MID, GRADIENT_END)
        
        # Animate handshake
        self.play(
            FadeIn(left_hand, scale=0.95),
            FadeIn(right_hand, scale=0.95),
            run_time=1,
            rate_func=smooth
        )
        
        self.play(
            left_hand.animate.move_to(UP * 0.8),
            right_hand.animate.move_to(DOWN * 0.8),
            run_time=1.5,
            rate_func=smooth
        )
        
        # Glow effect at connection
        glow = Circle(radius=0.6)
        glow.set_fill(color=[ACCENT_1, ACCENT_2], opacity=0.2)
        glow.set_stroke(width=0)
        glow.move_to(ORIGIN)
        
        self.play(
            FadeIn(glow, scale=0.8),
            run_time=0.5,
            rate_func=smooth
        )
        
        self.play(
            glow.animate.scale(1.5).set_opacity(0),
            run_time=1,
            rate_func=smooth
        )
        self.remove(glow)
        
        # Hands separate
        self.play(
            left_hand.animate.move_to(UP * 4),
            right_hand.animate.move_to(DOWN * 4),
            run_time=1.5,
            rate_func=smooth
        )
        
        self.play(
            FadeOut(left_hand, scale=0.95),
            FadeOut(right_hand, scale=0.95),
            run_time=1,
            rate_func=smooth
        )
        
        # Scene 9: Final scene - documents settling from above
        # Duration: ~5 seconds
        
        # Create final documents
        final_documents = VGroup()
        for i in range(20):
            doc = RoundedRectangle(
                width=1.0,
                height=1.4,
                corner_radius=0.08
            )
            create_gradient_fill(doc, GRADIENT_START, GRADIENT_END)
            
            # Start position above screen (arranged in columns for vertical format)
            row = i // 4
            col = i % 4
            start_x = (col - 1.5) * 1.4
            start_y = 10 + row * 1.8
            doc.move_to(np.array([start_x, start_y, 0]))
            
            final_documents.add(doc)
        
        # Animate documents falling and settling
        self.play(
            LaggedStart(*[
                FadeIn(doc, scale=0.95)
                for doc in final_documents
            ], lag_ratio=0.05),
            run_time=1.5,
            rate_func=smooth
        )
        
        # Calculate final positions (vertical grid arrangement)
        final_positions = []
        for i in range(20):
            row = i // 4
            col = i % 4
            x = (col - 1.5) * 1.4 + (np.random.random() - 0.5) * 0.2
            y = (3 - row) * 1.8 + (np.random.random() - 0.5) * 0.2
            final_positions.append(np.array([x, y, 0]))
        
        # Settle animation
        settle_anims = []
        for doc, pos in zip(final_documents, final_positions):
            settle_anims.append(
                doc.animate.move_to(pos).rotate(
                    (np.random.random() - 0.5) * 0.15
                )
            )
        
        self.play(
            *settle_anims,
            run_time=2.5,
            rate_func=smooth
        )
        
        # Camera slowly zooms in slightly
        self.play(
            final_documents.animate.scale(1.08),
            run_time=2,
            rate_func=smooth
        )
        
        # Hold final frame
        self.wait(1.5)
        
        # Elegant fade out
        self.play(
            FadeOut(final_documents, scale=1.02),
            run_time=2,
            rate_func=smooth
        )
        
        self.wait(0.5)
    
    def create_human_silhouette(self):
        """Create a simplified human silhouette"""
        silhouette = VGroup()
        
        # Head
        head = Circle(radius=0.3)
        head.move_to(UP * 1.2)
        
        # Body
        body = RoundedRectangle(width=0.8, height=1.2, corner_radius=0.1)
        body.move_to(DOWN * 0.1)
        
        # Arms
        left_arm = RoundedRectangle(width=0.25, height=0.9, corner_radius=0.08)
        left_arm.move_to(LEFT * 0.6 + DOWN * 0.1)
        left_arm.rotate(PI / 8)
        
        right_arm = RoundedRectangle(width=0.25, height=0.9, corner_radius=0.08)
        right_arm.move_to(RIGHT * 0.6 + DOWN * 0.1)
        right_arm.rotate(-PI / 8)
        
        # Legs
        left_leg = RoundedRectangle(width=0.3, height=1, corner_radius=0.08)
        left_leg.move_to(LEFT * 0.25 + DOWN * 1.3)
        
        right_leg = RoundedRectangle(width=0.3, height=1, corner_radius=0.08)
        right_leg.move_to(RIGHT * 0.25 + DOWN * 1.3)
        
        silhouette.add(head, body, left_arm, right_arm, left_leg, right_leg)
        
        return silhouette
    
    def create_abstract_hand(self):
        """Create an abstract hand shape"""
        hand = VGroup()
        
        # Palm
        palm = RoundedRectangle(width=0.6, height=0.8, corner_radius=0.1)
        
        # Fingers (simplified)
        finger1 = RoundedRectangle(width=0.15, height=0.5, corner_radius=0.05)
        finger1.move_to(palm.get_top() + UP * 0.25 + LEFT * 0.2)
        
        finger2 = RoundedRectangle(width=0.15, height=0.6, corner_radius=0.05)
        finger2.move_to(palm.get_top() + UP * 0.3)
        
        finger3 = RoundedRectangle(width=0.15, height=0.5, corner_radius=0.05)
        finger3.move_to(palm.get_top() + UP * 0.25 + RIGHT * 0.2)
        
        # Thumb
        thumb = RoundedRectangle(width=0.15, height=0.4, corner_radius=0.05)
        thumb.move_to(palm.get_left() + LEFT * 0.15 + DOWN * 0.1)
        thumb.rotate(PI / 4)
        
        hand.add(palm, finger1, finger2, finger3, thumb)
        
        return hand