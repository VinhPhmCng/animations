from manim import *

# Improved readability and logic compared to "outro.py"
class Outro(Scene):
    def construct(self):
        INSERT_TIME_PER_CHAR = 0.08
        DELETE_TIME_PER_CHAR = 0.06
        BLINK_TIME = 1.0
        CUSTOM_PURPLE = ManimColor.from_hex("#d787d7", alpha=1.0)
        CUSTOM_YELLOW = ManimColor.from_hex("#f0cd44", alpha=1.0)

        name = Text(
            "Devinh",
            font = "monospace",
            color = CUSTOM_PURPLE,
        ).scale(1.5).to_edge(LEFT)
        slogan = Text(
            "elop(yourself)",
            font = "monospace",
            color = CUSTOM_PURPLE,
            t2c = {"yourself":CUSTOM_YELLOW},
        ).scale(1.5).next_to(name[2], RIGHT, buff=0.08)
        cursor = Rectangle(
            color = GREY_A,
            fill_color = GREY_A,
            fill_opacity = 1.0,
            height = 1.1,
            width = 0.5,
        ).move_to(name[0]).shift(DOWN*0.06)

        def play_anim_cursor_insertion(char):
            self.play(
                AddTextLetterByLetter(char, time_per_char=INSERT_TIME_PER_CHAR),
                ApplyMethod(cursor.set_opacity, 1.0, run_time=0.0),
                ApplyMethod(cursor.shift, RIGHT*0.59, run_time=0.0),
            ) 

        def play_anim_cursor_deletion(char):
            self.play(
                Succession(
                    RemoveTextLetterByLetter(char, time_per_char=DELETE_TIME_PER_CHAR),
                    ApplyMethod(cursor.set_opacity, 1.0, run_time=0.0),
                    ApplyMethod(cursor.shift, LEFT*0.59, run_time=0.0),
                )
            ) 

        def play_anim_cursor_blink():
            self.play(
                Succession(
                    ApplyMethod(cursor.set_opacity, 1.0, run_time=0.0),
                    Wait(run_time=BLINK_TIME * 0.25),
                    ApplyMethod(cursor.set_opacity, 0.0, run_time=0.0),
                    Wait(run_time=BLINK_TIME * 0.5),
                    ApplyMethod(cursor.set_opacity, 1.0, run_time=0.0),
                    Wait(run_time=BLINK_TIME * 0.25),
                )
            )

        self.wait(1.0)
        self.add(cursor)
        self.wait(0.5)

        for char in name:
            play_anim_cursor_insertion(char)
        play_anim_cursor_blink()
        play_anim_cursor_blink()

        for char in reversed(name[3:]):
            play_anim_cursor_deletion(char)
        play_anim_cursor_blink()

        for char in slogan:
            play_anim_cursor_insertion(char)
        play_anim_cursor_blink()
        play_anim_cursor_blink()

        for char in reversed(slogan):
            play_anim_cursor_deletion(char)
        for char in reversed(name[:3]):
            play_anim_cursor_deletion(char)
        play_anim_cursor_blink()

        # Blink off
        self.play(
            Succession(
                ApplyMethod(cursor.set_opacity, 1.0, run_time=0.0),
                Wait(run_time=BLINK_TIME * 0.25),
                ApplyMethod(cursor.set_opacity, 0.0, run_time=0.0),
                Wait(run_time=BLINK_TIME * 1.0),
            )
        )
        return super().construct()