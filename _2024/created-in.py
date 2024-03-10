from manim import *

class CreatedIn(Scene):
    def construct(self):
        ############################################################
        YEAR = 1991
        BEFORE = 2
        AFTER = 4
        YEAR_FONT='Noto Sans'
        YEAR_FONT_SIZE = 24
        YEAR_COLOR = ManimColor.from_hex("#23a9f2", alpha=1.0)

        BAR_WIDTH = 15
        BAR_COLOR = ManimColor.from_hex("#23a9f2", alpha=1.0)
        MARKERS_BUFF = 0.35

        UP_DISTANCE = 10
        UP_TIME = 1

        INDICATE_SHIFT = UP*0.4 + RIGHT*0.7
        INDICATE_SCALE = 1.7

        ############################################################
        start_point = Dot().to_corner(DL, buff=0).shift(RIGHT*0.8)
        bar = Line(
            start=np.array([start_point.get_x(), start_point.get_y() - 1, 0]),
            end=np.array([start_point.get_x(), start_point.get_y() - 20, 0]),
        )
        bar.stroke_width = BAR_WIDTH
        bar.set_color(BAR_COLOR)

        big_markers = []
        markers = VGroup()
        for i in range(BEFORE + AFTER + 1):
            big = Line().set_length(0.2).next_to(bar, RIGHT, buff=0.2)
            big.stroke_width = 3
            if len(markers) > 0:
                big.next_to(markers[-1], DOWN, buff=MARKERS_BUFF)
            big_markers.append(big)
            markers.add(big)

            for j in range(4):
                small = Line().set_length(0.1)
                small.stroke_width = 2
                small.next_to(markers[-1], DOWN, buff=MARKERS_BUFF)
                markers.add(small)

        for m in markers:
            m.align_to(markers[0], LEFT)

        markers.align_to(bar, UP).shift(DOWN)

        years = [
            Text(str(i), font=YEAR_FONT, font_size=YEAR_FONT_SIZE, weight=BOLD, color=WHITE)
            for i in range(YEAR - BEFORE, YEAR + AFTER + 1)
        ]
        years[BEFORE].set_color(YEAR_COLOR)

        for i, y in enumerate(years):
            y.next_to(big_markers[i], buff=0.5)

        for y in years:
            y.align_to(years[0], LEFT)

        all = VGroup(bar, markers, *years)
        self.add(all)
        self.play(all.animate(run_time=UP_TIME).shift(UP*UP_DISTANCE))

        year_marker = Line().set_length(2.6).move_to(big_markers[BEFORE]).align_to(big_markers[BEFORE], LEFT)
        year_marker.stroke_width = 6
        year_marker.set_color(YEAR_COLOR)

        years[BEFORE].generate_target()
        years[BEFORE].target.shift(INDICATE_SHIFT).scale(INDICATE_SCALE)

        year_arrow = Triangle(color=WHITE, fill_color=WHITE, fill_opacity=1)
        year_arrow.rotate(30*DEGREES).scale(0.08)
        year_arrow.next_to(years[BEFORE].target, LEFT, buff=0.4)

        self.play(
            Transform(big_markers[BEFORE], year_marker),
            FadeIn(year_arrow, shift=RIGHT),
            MoveToTarget(years[BEFORE]),
        )

        self.wait(0.1)
        return super().construct()