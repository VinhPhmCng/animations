from manim import *

class BP4(Scene):
    def construct(self):
        def reset():
            self.play(
                *[FadeOut(mob)for mob in self.mobjects],
                run_time=0.5,
            )

        CUSTOM_PURPLE = ManimColor.from_hex("#d787d7", alpha=1.0)
        COMMENT_COLOR = ManimColor.from_hex("#F8C795", alpha=1.0)

        # Comments
        txt1 = Text("COMMENTS", font="Monospace", color=CUSTOM_PURPLE).scale(1.2)
        #txt1.to_edge(LEFT)
        txt1.scale(2).shift(UP*2)
        self.play(Write(txt1, run_time=1.2, stroke_color=CUSTOM_PURPLE))

        comment = SVGMobject("images/comment.svg")
        comment.submobjects[0].set_color(COMMENT_COLOR).stroke_width = 0
        comment.submobjects[1].set_color(COMMENT_COLOR).stroke_width = 0
        comment.submobjects[2].set_color(COMMENT_COLOR).stroke_width = 0
        comment.submobjects[3].set_color(COMMENT_COLOR).stroke_width = 0

        #comment.scale(0.4)
        comment.next_to(txt1, DOWN, buff=1)

        self.play(Write(comment))
        self.wait(1)
        reset()

        # Definition
        txt1 = Text("A COMMENT", font="Monospace", color=CUSTOM_PURPLE).scale(1.2)
        defi = VGroup(
            Text("is a piece of plain text that", font="Monospace").scale(0.7),
            Text("will NOT be executed.", font="Monospace").scale(0.7),
        ).arrange(DOWN, buff=0.5)

        self.play(Write(txt1, run_time=0.8, stroke_color=CUSTOM_PURPLE))
        self.play(txt1.animate(run_time=0.5).shift(UP*1.5))

        defi.next_to(txt1, DOWN, buff=0.8)

        self.play(Create(defi, run_time=1.2))
        reset()

        # Individual activity
        txt1 = Text("INDIVIDUAL ACTIVITY", font="Monospace", color=CUSTOM_PURPLE)
        self.play(Write(txt1, run_time=1, stroke_color=CUSTOM_PURPLE))

        self.wait(0.5)

        # Team activity
        coder1 = ImageMobject("images/coding-1-trans.png")
        coder2 = ImageMobject("images/coding-2-trans.png").scale(0.5).shift(LEFT*3 + DOWN*1.5)
        coder3 = ImageMobject("images/coding-3-trans.png").scale(0.5).shift(RIGHT*3 + DOWN*1.5)

        txt1.to_edge(UP)
        self.add(coder1, txt1)
        self.wait(1)

        coder1.generate_target()
        coder1.target.scale(0.5)
        coder1.target.shift(UP*1.8)

        self.play(
            MoveToTarget(coder1),
            FadeIn(coder2, shift=DOWN),
            FadeIn(coder3, shift=DOWN),
        )

        txt2 = Text("TEAM ACTIVITY", font="Monospace", color=CUSTOM_PURPLE).move_to(txt1)
        self.play(Transform(txt1, txt2))

        self.play(Circumscribe(txt2[0:4], color=GREEN))

        self.wait(0.5)
        reset()

        # Past present future
        past = ImageMobject("images/coding-1-trans.png").scale(0.5).shift(LEFT*5 + UP*2)
        present = ImageMobject("images/medium-monitor-trans.png").scale(0.5).shift(UP*2)
        future = ImageMobject("images/big-monitor-trans.png").scale(0.5).shift(RIGHT*5 + UP*2)

        middle_color = ManimColor.from_hex("#a9b771", alpha=1)
        dots = [Dot() for i in range(3)]
        dots[0].next_to(past, DOWN, buff=0.7).set_color(GREEN).set_z_index(2)
        dots[1].next_to(present, DOWN, buff=0.7).set_color(middle_color).set_z_index(2)
        dots[2].next_to(future, DOWN, buff=0.7).set_color(CUSTOM_PURPLE).set_z_index(2)

        p2p = Line(
            start=dots[1].get_center(),
            end=dots[0].get_center(),
            stroke_color=[middle_color, GREEN],
        )
        p2f = Line(
            start=dots[1].get_center(),
            end=dots[2].get_center(),
            stroke_color=[PURPLE, middle_color],
        ) 

        txts = [
            Text("NOOB", font="Monospace", color=GREEN).scale(0.9).next_to(dots[0], DOWN, buff=0.7),
            Text("NON-NOOB", font="Monospace", color=middle_color).scale(0.8).next_to(dots[1], DOWN, buff=0.7),
            Text("CAN GOOGLE", font="Monospace", color=CUSTOM_PURPLE).scale(0.7).next_to(dots[2], DOWN, buff=0.7),
        ]
        txts[0].match_y(txts[1])
        txts[2].match_y(txts[1])

        self.play(FadeIn(present, shift=DOWN, run_time=1.2))

        self.play(
            SpinInFromNothing(dots[1], run_time=0.4),
            GrowFromEdge(p2p, RIGHT, run_time=0.8),
        )
        self.play(
            SpinInFromNothing(dots[0], run_time=0.4),
            FadeIn(past, shift=DOWN, run_time=0.8)
        )

        self.play(
            GrowFromEdge(p2f, LEFT, run_time=0.8),
        )
        self.play(
            SpinInFromNothing(dots[2], run_time=0.4),
            FadeIn(future, shift=DOWN, run_time=0.8)
        )

        self.wait(0.7)
        self.play(Succession(
            Write(txts[0], stroke_color=GREEN, run_time=0.8),
            Write(txts[1], stroke_color=middle_color, run_time=0.8),
            Write(txts[2], stroke_color=CUSTOM_PURPLE, run_time=0.8),
        ))

        self.wait(0.5)
        reset()

        # Two approaches
        txt1 = Text("TWO WAYS", font="Monospace", color=CUSTOM_PURPLE).scale(1.5)

        self.play(Write(txt1, stroke_color=CUSTOM_PURPLE))
        self.play(ApplyWave(txt1))

        txt2 = Text("Write code that is:", font="Monospace", color=CUSTOM_PURPLE)
        txt2.scale(1.2).to_edge(UP, buff=0.8)

        txt3 = Text("1. SELF-EXPLANATORY", font="Monospace", color=GREEN)
        txt4 = Text("2. ACCOMPANIED BY SUFFICIENT CONTEXT", font="Monospace", color=COMMENT_COLOR).scale(0.8)

        #txt3.next_to(txt1, DOWN, buff=0.8)
        #txt4.next_to(txt3, DOWN, buff=0.6)

        txt3.shift(UP*0.8)
        txt4.shift(DOWN*1.2)

        self.wait(0.5)
        self.play(
            Transform(txt1, txt2, run_time=0.6),
            Write(txt3, stroke_color=GREEN),
        )

        self.wait(0.5)
        self.play(Write(txt4, stroke_color=COMMENT_COLOR))

        self.wait(1)
        
        ## At frame 269
        ## First approach
        self.play(
            txt3.animate(run_time=0.8).to_edge(UP, buff=0.8),
            FadeOut(txt1, txt4, run_time=0.4),
        )
        self.wait(1)

        ## Second approach
        txt4.to_edge(UP, buff=0.8)
        self.play(ReplacementTransform(txt3, txt4))
        self.wait(1)

        reset()

        # Short animation
        circle = Circle(color=RED, fill_opacity=1)
        circle.scale(1.5)
        self.play(Write(circle))
        self.wait(0.5)
        self.play(FadeToColor(circle, BLUE))
        self.wait(0.5)
        self.play(Unwrite(circle))
        self.wait(0.1)

        reset()

        # Braces
        reference = ImageMobject("images/comments-example.png")
        #self.add(reference)

        brace1 = BraceBetweenPoints([3, 0.3, 0], [3, 2.3, 0], )
        brace2 = BraceBetweenPoints([2, -2.15, 0], [2, -0.15, 0], )
        #self.add(brace1, brace2)

        txt1 = Text("COMMENTS", font="Monospace", color=COMMENT_COLOR).scale(0.8).next_to(brace1, buff=0.5)
        txt2 = Text("ACTUAL CODE", font="Monospace", color=CUSTOM_PURPLE).scale(0.7).next_to(brace2, buff=0.5)
        #self.add(txt1, txt2)

        self.play(
            FadeIn(brace1, shift=RIGHT, run_time=0.6),
            Write(txt1),
        )

        self.wait(0.5)
        self.play(
            FadeIn(brace2, shift=RIGHT, run_time=0.6),
            Write(txt2),
        )

        # At frame 089
        txt3 = VGroup(
            Text("LINE", font="Monospace", color=COMMENT_COLOR),
            Text("COMMENTS", font="Monospace", color=COMMENT_COLOR),
        ).arrange(DOWN).scale(0.7).move_to(txt1)
        txt4 = VGroup(
            Text("BLOCK", font="Monospace", color=COMMENT_COLOR),
            Text("COMMENTS", font="Monospace", color=COMMENT_COLOR),
        ).arrange(DOWN).scale(0.7).move_to(txt1)

        self.wait(0.5)
        self.play(
            Transform(txt1, txt3),
        )

        self.wait(0.5)
        self.play(
            Transform(txt1, txt4),
        )
        self.wait(0.5)

        reset()

        # Definition
        txt1 = Text("COMMENTS", font="Monospace", color=COMMENT_COLOR).scale(1.2)
        defi1 = VGroup(
            Text("are pieces of plain text that", font="Monospace").scale(0.7),
            Text("will not be executed.", font="Monospace").scale(0.7),
        ).arrange(DOWN, buff=0.4)

        defi2 = VGroup(
            Text("help us write readable code, improving", font="Monospace").scale(0.6),
            Text("communication and cooperation.", font="Monospace").scale(0.6),
        ).arrange(DOWN, buff=0.4)

        self.play(Write(txt1, run_time=0.8, stroke_color=COMMENT_COLOR))
        self.play(txt1.animate(run_time=0.5).shift(UP*2))

        defi1.next_to(txt1, DOWN, buff=0.8)
        defi2.next_to(defi1, DOWN, buff=0.8)

        self.play(Create(defi1, run_time=1.2))

        self.wait(0.5)
        self.play(Create(defi2, run_time=1.2))

        self.wait(0.5)

        reset()

        # Comment out short animation
        circle = Circle(color=RED, fill_opacity=1)
        circle.scale(1.5)
        self.play(Write(circle))
        self.wait(0.5)
        self.play(Unwrite(circle))
        self.wait(0.1)

        reset()

        # Indicate line comments
        reference = ImageMobject("images/ref.png")
        #self.add(reference)

        number_signs = Rectangle(
            color=GREEN,
            height=2.2,
            width=0.5,
        ).shift(LEFT*4.95 + UP*0.95)
        #self.add(number_signs)

        lines = VGroup(
            Line(
                start=[-4.6, 1.62, 0],
                end=[-1, 1.62, 0],
                color=GREEN,
            ),
            Line(
                start=[-4.6, 1.05, 0], # -0.57
                end=[0, 1.05, 0],
                color=GREEN,
            ),
            Line(
                start=[-4.6, 0.48, 0],
                end=[1.25, 0.48, 0],
                color=GREEN,
            ),
            Line(
                start=[-4.6, -0.09, 0],
                end=[-1.8, -0.09, 0],
                color=GREEN,
            ),
        )
        #self.add(lines)

        self.play(ShowPassingFlash(number_signs, time_width=1))
        self.wait(0.5)

        self.play(LaggedStart(
            *[ShowPassingFlash(l, time_width=1) for l in lines],
            lag_ratio=0.5,
            run_time=2,
        ))

        return super().construct()