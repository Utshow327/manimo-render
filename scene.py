from manim import *

class MainScene(Scene):
    def construct(self):
        # Introduction
        intro_text = Text("Fourier Transform", font_size=64)
        self.play(FadeIn(intro_text))
        self.wait(2)
        self.play(FadeOut(intro_text))

        # Time domain signal
        time_domain_signal = Axes(
            x_range=[0, 10, 1],
            y_range=[-1, 1, 0.5],
            x_length=8,
            y_length=4,
            axis_config={"include_tip": False},
        )
        time_domain_signal_graph = time_domain_signal.plot(
            lambda x: np.sin(x) + 0.5 * np.sin(3 * x), x_range=[0, 10, 0.01], color=BLUE
        )
        time_domain_signal_text = Text("Time Domain Signal", font_size=32)
        time_domain_signal_text.next_to(time_domain_signal, UP)
        self.play(FadeIn(time_domain_signal), Create(time_domain_signal_graph), FadeIn(time_domain_signal_text))
        self.wait(2)

        # Frequency domain signal
        frequency_domain_signal = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 2, 0.5],
            x_length=8,
            y_length=4,
            axis_config={"include_tip": False},
        )
        frequency_domain_signal_graph = frequency_domain_signal.plot(
            lambda x: np.abs(np.fft.fft(np.sin(np.linspace(0, 10, 1000)) + 0.5 * np.sin(3 * np.linspace(0, 10, 1000)))),
            x_range=[0, 10, 0.01],
            color=RED,
        )
        frequency_domain_signal_text = Text("Frequency Domain Signal", font_size=32)
        frequency_domain_signal_text.next_to(frequency_domain_signal, UP)
        self.play(
            Transform(time_domain_signal, frequency_domain_signal),
            Transform(time_domain_signal_graph, frequency_domain_signal_graph),
            Transform(time_domain_signal_text, frequency_domain_signal_text),
        )
        self.wait(2)

        # Transform explanation
        transform_explanation_text = Text("Fourier Transform: Time → Frequency", font_size=48)
        self.play(FadeIn(transform_explanation_text))
        self.wait(2)
        self.play(FadeOut(transform_explanation_text))

        # Inverse Fourier Transform
        inverse_fourier_transform_text = Text("Inverse Fourier Transform: Frequency → Time", font_size=48)
        self.play(FadeIn(inverse_fourier_transform_text))
        self.wait(2)
        self.play(FadeOut(inverse_fourier_transform_text))

        # Example of Fourier Transform application
        example_text = Text("Example: Filtering a Signal", font_size=48)
        self.play(FadeIn(example_text))
        self.wait(2)

        # Filtering a signal
        signal = Axes(
            x_range=[0, 10, 1],
            y_range=[-1, 1, 0.5],
            x_length=8,
            y_length=4,
            axis_config={"include_tip": False},
        )
        signal_graph = signal.plot(
            lambda x: np.sin(x) + 0.5 * np.sin(3 * x) + 0.1 * np.sin(10 * x), x_range=[0, 10, 0.01], color=BLUE
        )
        filtered_signal = Axes(
            x_range=[0, 10, 1],
            y_range=[-1, 1, 0.5],
            x_length=8,
            y_length=4,
            axis_config={"include_tip": False},
        )
        filtered_signal_graph = filtered_signal.plot(
            lambda x: np.sin(x) + 0.5 * np.sin(3 * x), x_range=[0, 10, 0.01], color=RED
        )
        self.play(FadeIn(signal), Create(signal_graph))
        self.wait(2)
        self.play(
            Transform(signal, filtered_signal),
            Transform(signal_graph, filtered_signal_graph),
        )
        self.wait(2)

        # Conclusion
        conclusion_text = Text("Conclusion: Fourier Transform is a powerful tool for signal processing", font_size=48)
        self.play(FadeIn(conclusion_text))
        self.wait(2)
        self.play(FadeOut(conclusion_text))

        self.wait(15)