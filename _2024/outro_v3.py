from manim import *

# Improved readability and logic compared to "outro_v2.py"
# PR made on Manim CE Github for these custom animations

class AddTextLetterByLetterWithCursor(AddTextLetterByLetter):
    """Similar to :class:`~.AddTextLetterByLetter` , but with an additional cursor mobject at the end.
    Parameters
    ----------
    time_per_char
        Frequency of appearance of the letters.
    cursor
        :class:`~.Mobject` shown after the last added letter.
    buff
        Controls how far away the cursor is to the right of the last added letter.
    keep_cursor_y
        If ``True``, the cursor's y-coordinate is set to the center of the ``Text`` and remains the same throughout the animation. Otherwise, it is set to the center of the last added letter.
    leave_cursor_on
        Whether to show the cursor after the animation.
    kwargs
        Additional arguments to be passed to the :class:`~.AddTextLetterByLetter` constructor.
    .. tip::
        This is currently only possible for class:`~.Text` and not for class:`~.MathTex`.
    Examples
    --------
    .. manim:: TypingAnimation
        class TypingAnimation(Scene):
            def construct(self):
                text = Text("Typing", color=PURPLE).scale(1.5).to_edge(LEFT)
                cursor = Rectangle(
                    color = GREY_A,
                    fill_color = GREY_A,
                    fill_opacity = 1.0,
                    height = 1.1,
                    width = 0.5,
                ).move_to(text[0]) # Position the cursor
                self.play(Blink(cursor, how_many_times=2))
                self.play(AddTextLetterByLetterWithCursor(text, cursor, leave_cursor_on=False)) # Turning off the cursor is important
                self.play(Blink(cursor, how_many_times=3))
                self.play(RemoveTextLetterByLetterWithCursor(text, cursor))
                self.play(Blink(cursor, how_many_times=2, ends_with_off=True))
    """

    def __init__(
        self,
        text: Text,
        cursor: Mobject,
        buff: float = 0.1,
        keep_cursor_y: bool = True,
        leave_cursor_on: bool = True,
        suspend_mobject_updating: bool = False,
        int_func: Callable[[np.ndarray], np.ndarray] = np.ceil,
        rate_func: Callable[[float], float] = linear,
        time_per_char: float = 0.1,
        run_time: float | None = None,
        reverse_rate_function=False,
        introducer=True,
        **kwargs,
    ) -> None:
        self.cursor = cursor
        self.buff = buff
        self.keep_cursor_y = keep_cursor_y
        self.leave_cursor_on = leave_cursor_on
        super().__init__(
            text,
            suspend_mobject_updating=suspend_mobject_updating,
            int_func=int_func,
            rate_func=rate_func,
            time_per_char=time_per_char,
            run_time=run_time,
            reverse_rate_function=reverse_rate_function,
            introducer=introducer,
            **kwargs,
        )

    def begin(self) -> None:
        self.y_cursor = self.cursor.get_y()
        self.cursor.initial_position = self.mobject.get_center()
        if self.keep_cursor_y:
            self.cursor.set_y(self.y_cursor)

        self.cursor.set_opacity(0)
        self.mobject.add(self.cursor)
        super().begin()

    def finish(self) -> None:
        if self.leave_cursor_on:
            self.cursor.set_opacity(1)
        else:
            self.cursor.set_opacity(0)
            self.mobject.remove(self.cursor)
        super().finish()

    def clean_up_from_scene(self, scene: Scene) -> None:
        if not self.leave_cursor_on:
            scene.remove(self.cursor)
        super().clean_up_from_scene(scene)

    def update_submobject_list(self, index: int) -> None:
        for mobj in self.all_submobs[:index]:
            mobj.set_opacity(1)

        for mobj in self.all_submobs[index:]:
            mobj.set_opacity(0)

        if index != 0:
            self.cursor.next_to(
                self.all_submobs[index - 1], RIGHT, buff=self.buff
            ).set_y(self.cursor.initial_position[1])
        else:
            self.cursor.move_to(self.all_submobs[0]).set_y(
                self.cursor.initial_position[1]
            )

        if self.keep_cursor_y:
            self.cursor.set_y(self.y_cursor)
        self.cursor.set_opacity(1)


class RemoveTextLetterByLetterWithCursor(AddTextLetterByLetterWithCursor):
    """Similar to :class:`~.RemoveTextLetterByLetter` , but with an additional cursor mobject at the end.
    Parameters
    ----------
    time_per_char
        Frequency of appearance of the letters.
    cursor
        :class:`~.Mobject` shown after the last added letter.
    buff
        Controls how far away the cursor is to the right of the last added letter.
    keep_cursor_y
        If ``True``, the cursor's y-coordinate is set to the center of the ``Text`` and remains the same throughout the animation. Otherwise, it is set to the center of the last added letter.
    leave_cursor_on
        Whether to show the cursor after the animation.
    kwargs
        Additional arguments to be passed to the :class:`~.AddTextLetterByLetter` constructor.
    .. tip::
        This is currently only possible for class:`~.Text` and not for class:`~.MathTex`.
    Examples
    --------
    .. manim:: TypingAnimation
        class TypingAnimation(Scene):
            def construct(self):
                text = Text("Typing", color=PURPLE).scale(1.5).to_edge(LEFT)
                cursor = Rectangle(
                    color = GREY_A,
                    fill_color = GREY_A,
                    fill_opacity = 1.0,
                    height = 1.1,
                    width = 0.5,
                ).move_to(text[0]) # Position the cursor
                self.play(Blink(cursor, how_many_times=2))
                self.play(AddTextLetterByLetterWithCursor(text, cursor, leave_cursor_on=False)) # Turning off the cursor is important
                self.play(Blink(cursor, how_many_times=3))
                self.play(RemoveTextLetterByLetterWithCursor(text, cursor))
                self.play(Blink(cursor, how_many_times=2, ends_with_off=True))
    """

    def __init__(
        self,
        text: Text,
        cursor: VMobject | None = None,
        buff: float = 0.1,
        keep_cursor_y: bool = True,
        leave_cursor_on: bool = True,
        suspend_mobject_updating: bool = False,
        int_func: Callable[[np.ndarray], np.ndarray] = np.ceil,
        rate_func: Callable[[float], float] = linear,
        time_per_char: float = 0.1,
        run_time: float | None = None,
        reverse_rate_function=True,
        introducer=False,
        remover=True,
        **kwargs,
    ) -> None:
        super().__init__(
            text,
            cursor=cursor,
            buff=buff,
            keep_cursor_y=keep_cursor_y,
            leave_cursor_on=leave_cursor_on,
            suspend_mobject_updating=suspend_mobject_updating,
            int_func=int_func,
            rate_func=rate_func,
            time_per_char=time_per_char,
            run_time=run_time,
            reverse_rate_function=reverse_rate_function,
            introducer=introducer,
            remover=remover,
            **kwargs,
        )


class Blink(Succession):
    """Blink the mobject.
    Parameters
    ----------
    mobject
        The mobject to be blinked.
    time_on
        The duration that the mobject is shown for one blink.
    time_off
        The duration that the mobject is hidden for one blink.
    how_many_times
        The number of blinks
    ends_with_off
        Whether to show or hide the mobject at the end of the animation.
    kwargs
        Additional arguments to be passed to the :class:`~.Succession` constructor.
    Examples
    --------
    .. manim:: BlinkingCursor
        class BlinkingCursor(Scene):
            def construct(self):
                text = Text("Typing", color=PURPLE).scale(1.5)
                cursor = Rectangle(
                    color = GREY_A,
                    fill_color = GREY_A,
                    fill_opacity = 1.0,
                    height = 1.1,
                    width = 0.5,
                ).next_to(text, buff=0.1)
                self.add(text)
                self.play(Blink(cursor, how_many_times=3))
    """

    def __init__(
        self,
        mobject: Mobject,
        time_on: float = 0.5,
        time_off: float = 0.5,
        how_many_times: int = 1,
        ends_with_off: bool = False,
        **kwargs
    ):
        animations = [
            UpdateFromFunc(
                mobject,
                update_function=lambda mob: mob.set_opacity(1.0),
                run_time=time_on,
            ),
            UpdateFromFunc(
                mobject,
                update_function=lambda mob: mob.set_opacity(0.0),
                run_time=time_off,
            ),
        ] * how_many_times

        if not ends_with_off:
            animations.append(
                UpdateFromFunc(
                    mobject,
                    update_function=lambda mob: mob.set_opacity(1.0),
                    run_time=time_on,
                ),
            )

        super().__init__(*animations, **kwargs)


class Outro(Scene):
    def construct(self):
        INSERT_TIME_PER_CHAR = 0.08
        DELETE_TIME_PER_CHAR = 0.06
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

        self.wait(1.0)
        self.play(AddTextLetterByLetterWithCursor(name, cursor, time_per_char=INSERT_TIME_PER_CHAR, leave_cursor_on=False))
        self.play(Blink(cursor, how_many_times=2))

        self.play(RemoveTextLetterByLetterWithCursor(name[3:], cursor, time_per_char=DELETE_TIME_PER_CHAR))
        self.play(Blink(cursor, how_many_times=1))
        
        self.play(AddTextLetterByLetterWithCursor(slogan, cursor, time_per_char=INSERT_TIME_PER_CHAR, leave_cursor_on=False))
        self.play(Blink(cursor, how_many_times=2))

        self.play(RemoveTextLetterByLetterWithCursor(slogan, cursor, time_per_char=DELETE_TIME_PER_CHAR))
        self.play(RemoveTextLetterByLetterWithCursor(name[:3], cursor))
        self.play(Blink(cursor, how_many_times=2, ends_with_off=True))

        self.wait(1.0)
        return super().construct()