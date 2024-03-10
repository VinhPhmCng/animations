from manim import *
from typing_animation import AddTextLetterByLetterWithCursor, RemoveTextLetterByLetterWithCursor, Blink

#config.disable_caching = True

class TOC(Scene):
    def construct(self):
        CUSTOM_PURPLE = ManimColor.from_hex("#d787d7", alpha=1.0)

        title = Text(
            "AN INTRODUCTION TO THE SERIES",
            color=CUSTOM_PURPLE,
            font="monospace",
            font_size=40,
        ).to_edge(UP)

        cursor = Rectangle(
            color = GREY_A,
            fill_color = GREY_A,
            fill_opacity = 1.0,
            height = 0.7,
            width = 0.35,
        ).move_to(title[0]) # Position the cursor

        sections = VGroup(*[
            Text(t, font="monospace").scale(1.0) for t in [
                "1. Introduction",
                "2. Our Programming Environment",
            ]
        ]).arrange(DOWN, buff=1.3).shift(UP*0.5)

        sections[0].set_color(BLUE_A)
        sections[1].set_color(GREEN_A)

        for t in sections:
            t.to_edge(LEFT, buff=1.0)

        self.play(Blink(cursor, blinks=2))
        self.play(AddTextLetterByLetterWithCursor(title, cursor, leave_cursor_on=False))
        self.wait(1.0)
                
        self.play(
            FadeIn(*sections, shift=RIGHT*5),
            Blink(cursor, hide_at_end=True),
        )
        self.wait(0.5)

        extras = [
            Text(t, font="monospace").scale(0.6) for t in [
                "Code cell",
                "Terminal",
                "Output",
            ] 
        ] 

        extras[0].next_to(sections[1], DOWN, buff=1.0).shift(LEFT*3.0).rotate_about_origin(3*DEGREES).set_color(YELLOW_A)
        extras[1].next_to(sections[1], DOWN, buff=2.0).rotate_about_origin(-5*DEGREES).set_color(PURPLE_A)
        extras[2].next_to(sections[1], DOWN, buff=1.3).shift(RIGHT*3.0).rotate_about_origin(2*DEGREES).set_color(GREEN_A)

        self.play(FadeIn(*extras, shift=DOWN))

        self.wait(1.5)
        self.play(
            FadeOut(*sections, shift=RIGHT*5),
            FadeOut(*extras, shift=RIGHT*5),
        )

        self.wait(0.5) #
        cursor.set_opacity(1)
        self.wait(0.5)
        self.play(RemoveTextLetterByLetterWithCursor(title, cursor))

        title = Text(
            "FUNDAMENTAL CONCEPTS OF PROGRAMMING",
            color=CUSTOM_PURPLE,
            font="monospace",
            font_size=40,
        ).to_edge(UP)
        cursor.move_to(title[0])

        self.wait(0.7)
        self.play(AddTextLetterByLetterWithCursor(title, cursor, leave_cursor_on=False))
        self.wait(1.0)

        sections = VGroup(*[
            Text(t, font="monospace").scale(0.8) for t in [
                "3. Programming Languages",
                "4. Comments",
                "5. Variables",
                "6. Data Types",
            ]
        ]).arrange(DOWN, buff=1.1).shift(DOWN*0.5)

        sections[0].set_color(GREY_A)
        sections[1].set_color(GOLD_A)
        sections[2].set_color(RED_D)
        sections[3].set_color(TEAL_A)

        for t in sections:
            t.to_edge(LEFT, buff=1.0)

        self.play(
            FadeIn(*sections, shift=UP*5),
            Blink(cursor, hide_at_end=True),
        )
        self.wait(2.5) #
        fadeouts = FadeOut(*sections, shift=UP*5)

        sections = VGroup(*[
            Text(t, font="monospace").scale(0.8) for t in [
                "7. Data Structures",
                "8. Operators",
                "9. Attributes",
                "10. Functions",
            ]
        ]).arrange(DOWN, buff=1.1).shift(DOWN*0.5)

        sections[0].set_color(GREEN_A)
        sections[1].set_color(GOLD_A)
        sections[2].set_color(MAROON_A)
        sections[3].set_color(BLUE_B)

        for t in sections:
            t.to_edge(LEFT, buff=1.0)

        self.play(
            fadeouts,
            FadeIn(*sections, shift=UP*5),
            Blink(cursor, hide_at_end=True),
        )
        self.wait(2.5) #

        cursor.set_opacity(1)
        self.wait(0.5)
        self.play(
            FadeOut(*sections, shift=UP*5),
            RemoveTextLetterByLetterWithCursor(title, cursor, leave_cursor_on=False)
        )

        title = Text(
            "PERSONAL EXPERIENCES",
            color=CUSTOM_PURPLE,
            font="monospace",
            font_size=40,
        ).to_edge(UP)

        self.wait(0.7)
        cursor.move_to(title[0])
        self.play(AddTextLetterByLetterWithCursor(title, cursor, leave_cursor_on=False))

        sections = VGroup(*[
            Text(t, font="monospace") for t in [
                "Fix Errors",
                "Choose PL",
                "The Tutorial Hell",
                "Have Fun",
                "Best Practices",
                "Virtual Env",
                "CLI",
            ]
        ])

        sections[0].scale(0.8).move_to(np.array([-3, 2.2, 0])).rotate_about_origin(7*DEGREES).set_color(BLUE_B)
        sections[1].scale(0.7).move_to(np.array([3, 1.4, 0])).rotate_about_origin(-3*DEGREES).set_color(GOLD_A)
        sections[2].scale(0.6).move_to(np.array([-1, 0.6, 0])).rotate_about_origin(4*DEGREES).set_color(GREEN_A)
        sections[3].scale(0.9).move_to(np.array([1, -0.3, 0])).rotate_about_origin(-6*DEGREES).set_color(MAROON_A)
        sections[4].scale(0.7).move_to(np.array([-2.0, -1.2, 0])).rotate_about_origin(2*DEGREES).set_color(PURPLE_A)
        sections[5].scale(0.6).move_to(np.array([2.0, -2.1, 0])).rotate_about_origin(0*DEGREES).set_color(RED_A)
        sections[6].scale(0.8).move_to(np.array([-2.5, -2.8, 0])).rotate_about_origin(5*DEGREES).set_color(YELLOW_A)

        self.wait(0.7)
        self.play(
            SpiralIn(sections, run_time=2.5),
            Blink(cursor, hide_at_end=True),
        )
        self.wait(1.0)

        #for s in sections:
            #self.play(Indicate(s, scale_factor=1.5))
            #self.wait(1.0)

        self.wait(1.0)
        cursor.set_opacity(1)
        self.wait(0.5)
        self.play(
            RemoveTextLetterByLetterWithCursor(title, cursor),
            FadeOut(sections),
        )

        title = Text(
            "MORE FUNDAMENTAL CONCEPTS",
            color=CUSTOM_PURPLE,
            font="monospace",
            font_size=40,
        ).to_edge(UP)
        cursor.move_to(title[0])

        #self.wait(0.7)
        self.play(AddTextLetterByLetterWithCursor(title, cursor, leave_cursor_on=False))

        sections = VGroup(*[
            Text(t, font="monospace") for t in [
                "If-else",
                "Loops",
                "Scopes",
                "Classes",
                "Modularity",
                "Algorithms",
                "OOP",
            ]
        ])

        sections[0].scale(0.7).move_to(np.array([3, 2.2, 0])).rotate_about_origin(-7*DEGREES).set_color(GREEN_A)
        sections[1].scale(0.9).move_to(np.array([-3, 1.4, 0])).rotate_about_origin(3*DEGREES).set_color(PURPLE_A)
        sections[2].scale(0.7).move_to(np.array([1, 0.6, 0])).rotate_about_origin(-4*DEGREES).set_color(BLUE_B)
        sections[3].scale(0.9).move_to(np.array([-1, -0.3, 0])).rotate_about_origin(6*DEGREES).set_color(MAROON_A)
        sections[4].scale(0.6).move_to(np.array([2.0, -1.2, 0])).rotate_about_origin(-2*DEGREES).set_color(GOLD_A)
        sections[5].scale(0.6).move_to(np.array([-2.0, -2.1, 0])).rotate_about_origin(0*DEGREES).set_color(YELLOW_A)
        sections[6].scale(0.9).move_to(np.array([2.5, -2.8, 0])).rotate_about_origin(-5*DEGREES).set_color(RED_A)

        self.wait(0.7)
        self.play(
            SpiralIn(sections, run_time=2.5),
            Blink(cursor, hide_at_end=True),
        )

        #for s in sections:
            #self.play(Indicate(s, scale_factor=1.5))
            #self.wait(1.0)

        self.wait(1.0)

        self.play(FadeOut(*self.mobjects))
        return super().construct()