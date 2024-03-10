from manim import *

class VSCode(Scene):
    def construct(self):
        CUSTOM_BLUE = ManimColor.from_hex("#23a9f2", alpha=1.0)

        code = Text("Code", color=CUSTOM_BLUE).scale(2)
        visual_studio = Text("Visual Studio", color=CUSTOM_BLUE).scale(2)
        vs = Text("VS", color=CUSTOM_BLUE).scale(2)

        all = VGroup(visual_studio, code).arrange(RIGHT, buff=0.55)

        self.play(Write(all), run_time=0.8)
        self.wait(1.0)

        self.play(TransformMatchingShapes(visual_studio, vs), run_time=0.8)

        all = VGroup(vs, code)
        self.play(all.animate(run_time=0.8).arrange(RIGHT, buff=0.25))

        self.wait(1.0)
        return super().construct()