from manim import *

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

    .. tip::
        This is currently only possible for class:`~.Text` and not for class:`~.MathTex`.


    Examples
    --------

    .. manim:: InsertingTextExample
        :ref_classes: Blink

        class InsertingTextExample(Scene):
            def construct(self):
                text = Text("Inserting", color=PURPLE).scale(1.5).to_edge(LEFT)
                cursor = Rectangle(
                    color = GREY_A,
                    fill_color = GREY_A,
                    fill_opacity = 1.0,
                    height = 1.1,
                    width = 0.5,
                ).move_to(text[0]) # Position the cursor

                self.play(AddTextLetterByLetterWithCursor(text, cursor))
                self.play(Blink(cursor, blinks=2))

    """

    def __init__(
        self,
        text: Text,
        cursor: Mobject,
        buff: float = 0.1,
        keep_cursor_y: bool = True,
        leave_cursor_on: bool = True,
        time_per_char: float = 0.07,
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
            time_per_char=time_per_char,
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

    .. tip::
        This is currently only possible for class:`~.Text` and not for class:`~.MathTex`.


    Examples
    --------

    .. manim:: DeletingTextExample
        :ref_classes: Blink

        class DeletingTextExample(Scene):
            def construct(self):
                text = Text("Deleting", color=PURPLE).scale(1.5).to_edge(LEFT)
                cursor = Rectangle(
                    color = GREY_A,
                    fill_color = GREY_A,
                    fill_opacity = 1.0,
                    height = 1.1,
                    width = 0.5,
                ).move_to(text[0]) # Position the cursor

                self.play(RemoveTextLetterByLetterWithCursor(text, cursor))
                self.play(Blink(cursor, blinks=2))

    """

    def __init__(
        self,
        text: Text,
        cursor: VMobject | None = None,
        time_per_char: float = 0.03,
        reverse_rate_function=True,
        introducer=False,
        remover=True,
        **kwargs,
    ) -> None:
        super().__init__(
            text,
            cursor=cursor,
            time_per_char=time_per_char,
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
    blinks
        The number of blinks
    hide_at_end
        Whether to hide the mobject at the end of the animation.
    kwargs
        Additional arguments to be passed to the :class:`~.Succession` constructor.

    Examples
    --------

    .. manim:: BlinkingExample

        class BlinkingExample(Scene):
            def construct(self):
                text = Text("Blinking").scale(1.5)
                self.add(text)
                self.play(Blink(text, blinks=3))

    """

    def __init__(
        self,
        mobject: Mobject,
        time_on: float = 0.5,
        time_off: float = 0.5,
        blinks: int = 1,
        hide_at_end: bool = False,
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
        ] * blinks

        if not hide_at_end:
            animations.append(
                UpdateFromFunc(
                    mobject,
                    update_function=lambda mob: mob.set_opacity(1.0),
                    run_time=time_on,
                ),
            )

        super().__init__(*animations, **kwargs)
