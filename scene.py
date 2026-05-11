from manim import *

class MainScene(Scene):
    def construct(self):
        crash_text = Text("💥 Code Crashed", font_size=64, color=RED)
        self.play(Create(crash_text), run_time=1.5)
        self.wait(0.5)

        burned_text = Text("and Burned 😭", font_size=64, color=RED)
        self.play(Transform(crash_text, burned_text), run_time=1.5)
        self.wait(0.5)

        api_text = Text("API calls were wasted...", font_size=48, color=YELLOW)
        self.play(FadeIn(api_text), run_time=1)
        self.wait(0.5)

        warning_text = Text("Double-check your code", font_size=48, color=YELLOW)
        self.play(Transform(api_text, warning_text), run_time=1)
        self.wait(0.5)

        fix_text = Text("or hit 'Fix with AI'", font_size=48, color=BLUE)
        self.play(FadeIn(fix_text), run_time=1)
        self.wait(0.5)

        self.play(crash_text.animate.shift(UP*2), 
                  api_text.animate.shift(UP), 
                  fix_text.animate.shift(DOWN), 
                  run_time=1.5)
        self.wait(0.5)

        code_text = Text("Code", font_size=48, color=WHITE)
        self.play(FadeIn(code_text), run_time=1)
        self.wait(0.5)

        self.play(code_text.animate.scale(2), run_time=1)
        self.wait(0.5)

        self.play(Unwrite(code_text), run_time=1)
        self.wait(0.5)

        self.play(FadeOut(crash_text), FadeOut(api_text), FadeOut(fix_text), run_time=1.5)
        self.wait(1)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2)
        self.wait(15)