from manim import *
from enum import Enum

config.disable_caching = True

class CursorOperation(Enum):
    INSERTION = 1
    DELETION = 2
    BLINK_ON = 3
    BLINK_OFF = 4

class Intro(Scene):
    def construct(self):
        INSERT_TIME_PER_CHAR = 0.08
        DELETE_TIME_PER_CHAR = 0.06
        HALF_BLINK_TIME = 0.5

        CUSTOM_PURPLE = ManimColor.from_hex("#d787d7", alpha=1.0)
        CUSTOM_YELLOW = ManimColor.from_hex("#f0cd44", alpha=1.0)

        name = Text(
            "Devinh",
            font = "monospace",
            color = CUSTOM_PURPLE,
        ).scale(1.5).to_edge(LEFT).set_opacity(0.0)
        slogan = Text(
            "elop(yourself)",
            font = "monospace",
            color = CUSTOM_PURPLE,
            t2c = {"yourself":CUSTOM_YELLOW},
        ).scale(1.5).next_to(name[2], RIGHT, buff=0.08).set_opacity(0.0)
        cursor = Rectangle(
            color = GREY_A,
            fill_color = GREY_A,
            fill_opacity = 1.0,
            height = 1.1,
            width = 0.48,
        ).move_to(name[0]).shift(DOWN*0.06)
        save_y = cursor.get_y()

        # Doing this the dumb way cuz
        cursor_instructions = [
            [CursorOperation.INSERTION, 5],
            [CursorOperation.BLINK_OFF, 1],
            [CursorOperation.BLINK_ON, 1],
            [CursorOperation.BLINK_OFF, 1],
            [CursorOperation.BLINK_ON, 1],

            [CursorOperation.DELETION, 3],
            [CursorOperation.BLINK_OFF, 1],
            [CursorOperation.BLINK_ON, 1],

            [CursorOperation.INSERTION, 14],
            [CursorOperation.BLINK_OFF, 1],
            [CursorOperation.BLINK_ON, 1],
            [CursorOperation.BLINK_OFF, 1],
            [CursorOperation.BLINK_ON, 1],

            [CursorOperation.DELETION, 17],
            [CursorOperation.BLINK_OFF, 1],
            [CursorOperation.BLINK_ON, 1],
            [CursorOperation.BLINK_OFF, 1],
        ]

        cursor_timemap = []
        timemap_index = 0
        time = 0.0
        for instruction in cursor_instructions:
            for _ in range(instruction[1]):
                match instruction[0]:
                    case CursorOperation.INSERTION:
                        time += INSERT_TIME_PER_CHAR * 0.97
                    case CursorOperation.DELETION:
                        time += DELETE_TIME_PER_CHAR * 1.05
                    case CursorOperation.BLINK_ON:
                        time += HALF_BLINK_TIME
                    case CursorOperation.BLINK_OFF:
                        time += HALF_BLINK_TIME

                cursor_timemap.append([time, instruction[0]])

        time_elapsed = 0.0
        def cursor_updater(mob, dt):
            nonlocal time_elapsed
            nonlocal cursor_timemap
            nonlocal timemap_index

            if timemap_index == len(cursor_timemap):
                return

            time_elapsed += dt
            time = cursor_timemap[timemap_index][0]
            instruction = cursor_timemap[timemap_index][1]

            if time_elapsed >= time:
                timemap_index += 1

                nonlocal cursor
                match instruction:
                    case CursorOperation.INSERTION:
                        cursor.set_opacity(1.0)
                        cursor.shift(RIGHT*0.59)
                    case CursorOperation.DELETION:
                        cursor.set_opacity(1.0)
                        cursor.shift(LEFT*0.59)
                    case CursorOperation.BLINK_ON:
                        cursor.set_opacity(1.0)
                    case CursorOperation.BLINK_OFF:
                        cursor.set_opacity(0.0)

        self.wait(1.0)
        self.add(cursor)

        self.wait(0.5)
        cursor.next_to(name[0], RIGHT, buff=0.2)
        cursor.set_y(save_y)
        cursor.add_updater(cursor_updater)

        self.play(AddTextLetterByLetter(name, time_per_char=INSERT_TIME_PER_CHAR))
        self.wait(2.0)

        self.play(RemoveTextLetterByLetter(name[3:], time_per_char=DELETE_TIME_PER_CHAR, remover=False))
        self.wait(1.0)

        self.play(AddTextLetterByLetter(slogan, time_per_char=INSERT_TIME_PER_CHAR))
        self.wait(2.0)

        self.play(RemoveTextLetterByLetter(slogan, time_per_char=DELETE_TIME_PER_CHAR, remover=False))
        self.play(RemoveTextLetterByLetter(name[:3], time_per_char=DELETE_TIME_PER_CHAR, remover=False))
        self.wait(1.5)

        self.wait(1.0)
        return super().construct()