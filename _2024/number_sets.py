from manim import *

class NumberSets(MovingCameraScene):
    def construct(self):
        # Natural numbers

        # Add in 0 -> 3
        # Add in extras and slide camera
        # Re-slide camera and remove extras
        # Add in natural number line

        labeled_dots = [
            VGroup(
                Dot(np.array([n, 0, 0]), radius=0.12, z_index=3),
                MathTex(str(int(n))),
            ).arrange(DOWN, buff=0.5).shift(RIGHT * n)
            for n in [0, 1, 2, 3]
        ]

        for ld in labeled_dots:
            self.play(GrowFromCenter(ld[0]), run_time=0.5)
            self.play(Write(ld[1]), run_time=0.5)

        # 4...49 (44 objects)
        # indices: 0...45
        extra_labeled_dots = [
            VGroup(
                Dot(np.array([n, 0, 0]), radius=0.12, z_index=3),
                Tex(str(int(n))),
            ).arrange(DOWN, buff=0.5).shift(RIGHT * n)
            for n in range(4, 50, 1)
        ]

        # Slide camera
        self.camera.frame.save_state()
        self.camera.frame.generate_target()
        self.camera.frame.target.move_to(extra_labeled_dots[38])

        # Trials and errors
        # Version 1:
        # cam: 3.0, smooth
        # grow dots: 0.2
        # group lag: 0.2, rush_into

        # Version 2:
        # cam: 5.5, ease_in_out_quad
        # grow dots: 0.4
        # group lag: 0.2, rush_into

        self.play(
            MoveToTarget(self.camera.frame, rate_func=rate_functions.ease_in_out_quad, run_time=5.5),
            AnimationGroup(
                *[GrowFromCenter(ld, run_time=0.4) for ld in extra_labeled_dots],
                lag_ratio=0.2, rate_func=rush_into,
            ),
        )
        self.wait(1.5)

        # Re-slide camera
        self.play(Restore(self.camera.frame), run_time=2.0, rate_func=smooth)
        self.wait(1.0)

        # Scale down natural dots
        # Remove extras
        self.play(
            *[ld[0].animate.scale(0.5) for ld in labeled_dots],
            FadeOut(*extra_labeled_dots),
            run_time = 0.8,
        )
        # Re-position labels of natural dots
        self.play(
            *[ld.animate.arrange(DOWN, buff=0.5).shift(RIGHT * ld[0].get_x()) for ld in labeled_dots],
            run_time = 0.5,
        )

        # Number line (natural)
        number_line = DashedLine(
            start = labeled_dots[0][0].get_center(),
            end = extra_labeled_dots[0][0].get_center(), 
            dash_length = 0.4, 
            dashed_ratio = 0.5, 
            stroke_color = YELLOW, 
            stroke_opacity = 0.8,
        ).add_tip(ArrowTriangleFilledTip(color=YELLOW, fill_opacity=0.8))

        label = MathTex(r"\mathbb{N}").scale(1.5).align_to(number_line, RIGHT).shift(UP + RIGHT * 0.5)
        title = Text("Natural Numbers").to_edge(UP)

        self.play(
            GrowFromEdge(number_line, LEFT),
            run_time = 1.5,
        )
        self.play(
            Write(label),
            Write(title),
            run_time = 1.0,
        )
        self.wait(1.0)

        # Negative integers
        negative_labeled_dots = [
            VGroup(
                Dot(np.array([n, 0, 0]), radius=0.12, z_index=3).scale(0.5),
                MathTex(str(int(n))),
            ).arrange(DOWN, buff=0.5).shift(RIGHT * n)
            for n in [-1, -2, -3, -4]
        ]
        # Re-position negative labels
        for nld in negative_labeled_dots:
            nld[1].shift(LEFT * 0.12)

        # Add in negative integers
        for i, ld in enumerate(labeled_dots[1:]):
            self.play(ReplacementTransform(ld.copy(), negative_labeled_dots[i], path_arc=60*DEGREES))
        self.wait(1.0)

        # Extend number line (integers)
        extended_number_line = DashedLine(
            start = negative_labeled_dots[-1][0].get_center(),
            end = extra_labeled_dots[0][0].get_center(),
            dash_length = 0.3,
            dashed_ratio = 0.5,
            stroke_color = YELLOW, 
            stroke_opacity = 0.8,
        ).add_tip(ArrowTriangleFilledTip(color=YELLOW, fill_opacity=0.8))

        integer_label = MathTex(r"\mathbb{Z}").scale(1.5).move_to(label)
        integer_title = Text("Integers").to_edge(UP)

        self.play(
            Transform(number_line, extended_number_line, run_time=2.0),
            Transform(label, integer_label, run_time=1.0),
            Transform(title, integer_title, run_time=1.0),
            #run_time = 2.0,
        )
        self.wait(1.0)

        self.play(FadeOut(title), run_time=1.0)
        self.wait(1.0)

        # Zoom in
        # Also scale down labels
        texs = []
        for ld in labeled_dots + negative_labeled_dots[:-1]:
            texs.append(ld[1])
            ld[1].save_state()

        self.play(
            self.camera.frame.animate.scale(0.7).shift(UP),
            *[tex.animate.scale(0.7) for tex in texs],
            label.animate.scale(0.7),
            run_time = 1.0,
        )

        # Rational
        # Add in fractions
        rational_dots = [
            Dot(np.array([r, 0, 0]), radius=0.12, z_index=3, color=BLUE).scale(0.5).match_y(labeled_dots[0][0])
            for r in [-3/2, 1/3]
        ]

        # -3/2 label
        mthree_over_two = MathTex(r"-3", r"\over", r"2").align_to(self.camera.frame, UL).shift(RIGHT*0.5 + DOWN*0.5)
        equals = MathTex(r"= -1.5").next_to(mthree_over_two, RIGHT)

        self.play(
            Succession(
                ReplacementTransform(negative_labeled_dots[2][1].copy(), mthree_over_two[0], run_time=1.0),
                GrowFromEdge(mthree_over_two[1], LEFT, run_time=1.0),
                ReplacementTransform(labeled_dots[2][1].copy(), mthree_over_two[2], run_time=1.0),
                Write(equals, run_time=1.0),
                Wait(run_time=1.0),
            )
            #run_time = 5.0,
        )
        self.play(
            FadeOut(equals),
            mthree_over_two.animate.scale(0.7).next_to(rational_dots[0], UP),
            GrowFromCenter(rational_dots[0]),
            run_time = 2.0,
        )
        self.wait(1.0)

        # 1/3 label
        one_over_three = MathTex(r"1", r"\over", r"3").align_to(self.camera.frame, UL).shift(RIGHT*0.5 + DOWN*0.5)
        equals = MathTex(r"= 1.33333 \ldots", r"= 1.(3)").next_to(one_over_three, RIGHT)

        self.play(
            Succession(
                ReplacementTransform(labeled_dots[1][1].copy(), one_over_three[0], run_time=1.0),
                GrowFromEdge(one_over_three[1], LEFT, run_time=1.0),
                ReplacementTransform(labeled_dots[3][1].copy(), one_over_three[2], run_time=1.0),
                Write(equals[0], run_time=1.0),
                Wait(run_time=1.0),
                Write(equals[1], run_time=1.0),
                Wait(run_time=1.0),
            )
            #run_time 7.0,
        )

        self.play(
            FadeOut(equals),
            one_over_three.animate.scale(0.7).next_to(rational_dots[1], UP),
            GrowFromCenter(rational_dots[1]),
            run_time = 2.0,
        )
        self.wait(1.0)

        # Add more fractions into the line
        extra_rational_texs = [
            MathTex(tex).align_to(self.camera.frame, UL).shift(RIGHT*0.5 + DOWN*0.5)
            for tex in [
                r"-1 \over 2",
                r"4 \over 3",
                r"-5 \over 2",
                r"5 \over 2",
            ]
        ]
        extra_rational_dots = [
            Dot(RIGHT*num, radius=0.12, z_index=3, color=BLUE).scale(0.5).match_y(labeled_dots[0][0])
            for num in [
                -1/2,
                4/3,
                -5/2,
                5/2,
            ]
        ]

        for tex, dot in zip(extra_rational_texs, extra_rational_dots):
            self.play(Write(tex), run_time=0.5)
            self.wait(1.0)
            self.play(FadeTransform(tex, dot), run_time=1.0)
            self.wait(0.5)

        # Increase number line's density (rational)
        # while fading out fraction dots
        denser_number_line = DashedLine(
            start = negative_labeled_dots[-1][0].get_center(),
            end = extra_labeled_dots[0][0].get_center(),
            dash_length = 0.2,
            dashed_ratio = 0.6,
            stroke_color = ORANGE,
            stroke_opacity = 0.9,
        ).add_tip(ArrowTriangleFilledTip(color=ORANGE, fill_opacity=0.9))

        rational_label = MathTex(r"\mathbb{Q}").move_to(label) # does NOT have to scale(0.7)
        title = Text("Rational Numbers").scale(0.7).to_edge(UP)
        self.play(
            Transform(label, rational_label, run_time=1.0),
            Write(title, run_time=1.0),
            FadeOut(mthree_over_two, one_over_three, *rational_dots, *extra_rational_dots, run_time=4.0),
            Transform(number_line, denser_number_line, run_time=4.0),
            #run_time = 4.0,
        )
        self.wait(1.0)

        self.play(FadeOut(title), run_time=1.0)

        # Real
        # Add in irrational numbers
        to_be_faded_out = []

        # sqrt(2)
        a = Line(start=labeled_dots[0][0].get_center(), end=labeled_dots[1][0].get_center(), color=GREEN)
        b = Line(start=a.get_end(), end=a.get_end() + UP, color=GREEN)
        c = Line(start=b.get_end(), end=a.get_start(), color=GREEN)
        c_rotated = c.copy()
        c_rotated.generate_target()
        c_rotated.target.rotate(about_point=labeled_dots[0][0].get_center(), angle=-PI/4)
        arc = DashedVMobject(ArcBetweenPoints(radius=np.sqrt(2), arc_center=a.get_start(), end=c.get_start(), start=c_rotated.target.get_start()))

        self.play(
            Succession(
                GrowFromPoint(a, a.get_start(), run_time=0.5),
                GrowFromPoint(b, b.get_start(), run_time=0.5),
                GrowFromPoint(c, c.get_start(), run_time=0.5),
            )
            #run_time = 1.5,
        )

        right_angle = RightAngle(a, b, quadrant=(-1, 1), length=0.15, color=GREEN)
        show_side_length = VGroup(
            DashedLine(start=b.get_start(), end=b.get_end()).add_tip(tip_length=0.1, tip_width=0.1).add_tip(tip_length=0.1, tip_width=0.1, at_start=True),
            MathTex("1").scale(0.7),
        ).arrange(RIGHT, buff=0.2).next_to(b, RIGHT, buff=0.1)

        self.play(
            Write(right_angle),
            Write(show_side_length),
            run_time=0.5,
        )
        self.wait(1.0)
        self.play(FadeOut(show_side_length), run_time=1.0)
        self.wait(1.0)

        sqrt_two = MathTex(r"\sqrt{2}", r"= 1.4142135623\ldots").align_to(self.camera.frame, UL).shift(RIGHT*0.5 + DOWN*0.5)
        sqrt_two_dot = Dot(np.array([1.4, 0, 0]), radius=0.12, z_index=3, color=BLUE).scale(0.5).match_y(labeled_dots[0][0])

        show_hypotenuse_length = VGroup(
            sqrt_two[0].copy().scale(0.7),
            DashedLine(start=c.get_start(), end=c.get_end())\
            .add_tip(tip_length=0.1, tip_width=0.1)\
            .add_tip(tip_length=0.1, tip_width=0.1, at_start=True),
        ).arrange(RIGHT, buff=0.0).next_to(c, LEFT, buff=0).shift(UP*0.1 + RIGHT*0.8)

        show_hypotenuse_length[0].shift(UP*0.2 + RIGHT*0.2)

        self.play(Write(show_hypotenuse_length), run_time=1.0)
        self.wait(1.0)
        self.play(
            FadeOut(show_hypotenuse_length[1]),
            ReplacementTransform(show_hypotenuse_length[0], sqrt_two[0]),
            run_time = 1.0,
        )
        self.play(Write(sqrt_two[1]), run_time=1.0)
        self.wait(1.0)

        c_copy = c.copy()
        self.play(
            Rotate(c_copy, about_point=labeled_dots[0][0].get_center(), angle=-PI/4),
            Write(arc, reverse=True, remover=False),
            run_time=1.0,
        )
        self.play(
            LaggedStart(
                GrowFromCenter(sqrt_two_dot, run_time=1.0),
                FadeOut(a, b, c, right_angle, arc, c_copy, run_time=1.0),
                lag_ratio=0.8,
            ),
            #run_time = 1.8,
        )
        self.wait(1.0)
        to_be_faded_out.append(sqrt_two_dot)

        self.play(
            sqrt_two[0].animate.scale(0.7).next_to(sqrt_two_dot, UP),
            FadeOut(sqrt_two[1]),
            run_time = 1.5,
        )
        self.wait(1.0)
        to_be_faded_out.append(sqrt_two[0])

        # pi
        circle = Circle(radius=0.5, color=GREEN).next_to(negative_labeled_dots[0][0], UP*2).shift(RIGHT*0.5)
        diameter = Line(start=negative_labeled_dots[0][0].get_center(), end=labeled_dots[0][0].get_center(), color=GREEN)
        self.play(FadeIn(diameter), run_time=0.5)
        self.wait(0.5)

        diameter.generate_target()
        diameter.target.become(Line(start=circle.points[15], end=circle.points[0], color=GREEN))
        self.play(MoveToTarget(diameter))
        self.wait(0.5)

        self.play(Write(circle))
        self.wait(0.5)

        radius = Line(start=circle.get_center(), end=circle.points[0], color=GREEN)
        self.play(ReplacementTransform(diameter, radius))
        self.wait(1.0)

        radius.add_updater(lambda mob: mob.become(Line(start=circle.get_center(), end=circle.points[0], color=GREEN)))
        self.play(
            circle.animate().match_y(labeled_dots[0][0]).shift(RIGHT*0.5 + UP*0.5),
            run_time = 1.0,
        )
        self.wait(0.5)

        into_line = Line(start=labeled_dots[0][0].get_center(), end=labeled_dots[0][0].get_center() + LEFT*3.2, color=GREEN).match_y(labeled_dots[0][0])

        circle.add_updater(lambda mob: mob.rotate(1.99*DEGREES)) # 60fps, 3 seconds => 180fps => 2 degrees/frame
        self.play(
            circle.animate.shift(LEFT*3.2),
            GrowFromEdge(into_line, RIGHT),
            rate_func = linear,
            run_time = 3.0,
        )
        circle.clear_updaters()
        self.wait(1.0)

        mpi_dot = Dot(np.array([-3.2, 0, 0]), radius=0.12, z_index=3, color=BLUE).scale(0.5).match_y(labeled_dots[0][0])
        mpi = MathTex(r"-\pi").scale(0.7).next_to(mpi_dot, UP).shift(LEFT*0.12)

        self.play(
            LaggedStart(
                GrowFromCenter(mpi_dot, run_time=1.0),
                FadeOut(circle, radius, into_line, run_time=1.0),
                lag_ratio=0.8,
            ),
            #run_time = 1.8,
        )
        self.wait(1.0)
        to_be_faded_out.append(mpi_dot)

        self.play(FadeIn(mpi, shift=DOWN), run_time=1.0)
        self.wait(1.0)
        to_be_faded_out.append(mpi)

        mpi_copy = mpi.copy()
        pi = MathTex(r"\pi", r"= 3.1415926535\ldots").align_to(self.camera.frame, UL).shift(RIGHT*0.5 + DOWN*0.5)

        self.play(
            Succession(
                ReplacementTransform(mpi_copy, pi[0], run_time=1.0),
                Write(pi[1], run_time=1.0),
            )
            #run_time = 2.0
        )
        self.wait(1.0)

        self.play(FadeOut(pi), run_time=1.0)
        self.wait(1.0)

        # Extra irrationals
        irrational_texs = [
            MathTex(*tex).align_to(self.camera.frame, UL).shift(RIGHT*0.5 + DOWN*0.5)
            for tex in [
                [r"e", r"= 2.7182818284\ldots"],
                [r"-\varphi", r"= -1.6180339887\ldots"],
            ]
        ]
        irrational_dots = [
            Dot(np.array([r, 0, 0]), radius=0.12, z_index=3, color=BLUE).scale(0.5).match_y(labeled_dots[0][0])
            for r in [
                2.7, # e
                -1.6, # golden ratio
            ]
        ]

        for i, pair in enumerate(zip(irrational_texs, irrational_dots)):
            tex, dot = pair
            self.play(Write(tex), run_time=1.0)
            self.wait(1.0)

            self.play(
                tex[0].animate.scale(0.7).next_to(dot, UP),
                FadeOut(tex[1]),
                GrowFromCenter(dot), 
                run_time=1.0
            )
            self.wait(1.0)
            to_be_faded_out.append(tex[0])
            to_be_faded_out.append(dot)

        # Fill in number line (real)
        # while fading out irrational dots
        # For some reason, if dashed_ratio == 1.0 add_tip() doesn't work (bug?)
        # so let's do a 2-step transformation
        denser_number_line = DashedLine(
            start = negative_labeled_dots[-1][0].get_center(),
            end = extra_labeled_dots[0][0].get_center(),
            dash_length = 0.1,
            dashed_ratio = 0.9,
            stroke_color = RED,
            stroke_opacity = 1.0,
        ).add_tip(ArrowTriangleFilledTip(color=RED))

        continuous_number_line = Line(
            start = negative_labeled_dots[-1][0].get_center(),
            end = extra_labeled_dots[0][0].get_center(),
            stroke_color = RED,
            stroke_opacity = 1.0,
        ).add_tip(ArrowTriangleFilledTip(color=RED))

        real_label = MathTex(r"\mathbb{R}").move_to(label) # does NOT have to scale(0.7)
        title = Text("Real Numbers").scale(0.7).to_edge(UP)

        self.play(
            Write(title, run_time=1.0),
            Transform(label, real_label, run_time=1.0),
            FadeOut(*to_be_faded_out, run_time=2.0),
            Transform(number_line, denser_number_line, run_time=2.0),
        )
        self.play(FadeTransform(number_line, continuous_number_line), run_time=1.0)
        self.wait(1.0)

        self.play(FadeOut(title), run_time=1.0)
        self.wait(1.0)

        # Zoom back out
        # Re-scale labels appropriately
        self.play(
            Restore(self.camera.frame),
            *[Restore(tex) for tex in texs],
            label.animate.scale(1.0 / 0.7),
            run_time = 1.0,
        )
        self.wait(1.0)
        return super().construct()