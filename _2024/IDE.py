from manim import *

class IDE(Scene):
    def construct(self):
        CUSTOM_BLUE = ManimColor.from_hex("#23a9f2", alpha=1.0)
        txt = VGroup(
            *[Text(t, color=CUSTOM_BLUE).scale(1.3) for t in [
                "Integrated", "Development", "Environment"
            ]]
        ).arrange(DOWN, buff=0.7)

        for t in txt:
            t.to_edge(LEFT, buff=1.0)

        self.play(Write(txt, stroke_color=CUSTOM_BLUE))
        self.wait(1.0)

        self.play(FadeOut(*txt[0][1:], *txt[1][1:], *txt[2][1:]))

        initials = VGroup(txt[0][0], txt[1][0], txt[2][0])
        self.play(initials.animate.arrange(RIGHT, buff=0.1).to_edge(LEFT, buff=1.0))

        self.wait(1.0)
        self.play(FadeOut(initials))
        return super().construct()