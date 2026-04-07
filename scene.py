from manim import *

class SolarSystem(Scene):
    def construct(self):
        # 1. Configuration & Colors
        sun_color = YELLOW
        planet_data = [
            {"name": "Mercury", "dist": 1.5, "radius": 0.1, "color": GRAY, "speed": 4.1},
            {"name": "Venus",   "dist": 2.2, "radius": 0.15, "color": ORANGE, "speed": 1.6},
            {"name": "Earth",   "dist": 3.2, "radius": 0.16, "color": BLUE, "speed": 1.0},
            {"name": "Mars",    "dist": 4.2, "radius": 0.12, "color": RED, "speed": 0.5},
        ]

        # 2. Create the Sun
        sun = Dot(radius=0.4, color=sun_color)
        sun.add(GlowDot(color=sun_color)) # Adds a soft glow effect
        sun_label = Text("Sun", font_size=20).next_to(sun, UP)
        
        self.add(sun)
        self.play(FadeIn(sun), Write(sun_label))
        self.play(FadeOut(sun_label))

        # 3. Create Planets and Orbits
        planets = []
        for data in planet_data:
            # Create the orbit path (visual guide)
            orbit = Circle(radius=data["dist"], color=WHITE, stroke_opacity=0.2)
            
            # Create the planet
            planet = Dot(radius=data["radius"], color=data["color"])
            planet.move_to(orbit.point_from_proportion(0))
            
            # Add a trace (the "tail" behind the planet)
            trace = TracedPath(planet.get_center, stroke_opacity=0.5, stroke_color=data["color"])
            
            self.add(orbit, trace, planet)
            planets.append((planet, data["dist"], data["speed"]))

        # 4. Animation Logic
        # We use an updater to make them rotate at different speeds
        def update_planet(mob, dt, dist, speed):
            # Calculate new angle based on time delta and speed
            # The value 'dt' is the time between frames
            mob.theta = getattr(mob, "theta", 0) + speed * dt
            new_pos = [dist * np.cos(mob.theta), dist * np.sin(mob.theta), 0]
            mob.move_to(new_pos)

        for p, d, s in planets:
            p.add_updater(lambda m, dt, d=d, s=s: update_planet(m, dt, d, s))

        # Run the animation for 10 seconds
        self.wait(10)