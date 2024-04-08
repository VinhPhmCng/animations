from manim import *

# All animations used in episode 3 - Programming Languages

class BP3(Scene):
    def construct(self):
        def reset():
            self.wait(1)
            self.play(
                *[FadeOut(mob)for mob in self.mobjects],
                run_time=0.5,
            )

        CUSTOM_PURPLE = ManimColor.from_hex("#d787d7", alpha=1.0)

        # Brainfuck example output
        out = Text("Hello world!", font="Monospace", color=CUSTOM_PURPLE)
        for l in out:
            self.play(FadeIn(l, shift=DOWN, run_time=0.5))
            self.wait(0.1)

        # Introduce Brainfuck
        CUSTOM_RED = ManimColor.from_hex("#ed193d", alpha=1.0)
        n = Text("Brainf*ck", font="Monospace", color=CUSTOM_RED).scale(1.3).shift(UP*1.5)
        self.play(Write(n, stroke_color=GRAY_A, run_time=0.8))

        commands = VGroup(*[
            Text(c, font="Monospace", color=GRAY_B)
            for c in ['>', '<', '+', '-', '.', ',', '[', ']']
        ])
        commands.arrange(RIGHT, buff=0.5).shift(DOWN)

        for c in commands:
            self.play(FadeIn(c, shift=DOWN, run_time=0.2))

        reset()

        # Introduce programming
        def symbols_background(mob, bg_color):
            r = mob.width / 2 + 0.15
            c = Circle(radius=0.5, color=bg_color, fill_opacity=1).set_z_index(-1)
            c.move_to(mob)
            return c
            
        colors = [
            MAROON_B, BLUE_C, RED_B, TEAL_D,
            TEAL_D, MAROON_B, BLUE_C, RED_B,
            RED_B, TEAL_D, MAROON_B, BLUE_C,
        ]

        symbol_texts = [
            Text(s, font="Monospace", color=WHITE)
            for s in [
                "()", "&", "*", ";",
                "#", "[]", "++", "!",
                "<>", "%", "{}", ":",
            ]
        ]
        symbols = VGroup(*symbol_texts)
        symbols.arrange_in_grid(cols=4, buff=1).to_edge(LEFT)
        backgrounds = list(map(symbols_background, symbol_texts, colors))
        symbols.add(*backgrounds)
        for i in range(12):
            self.play(
                SpinInFromNothing(symbol_texts[i], run_time=0.2),
                SpinInFromNothing(backgrounds[i], run_time=0.2),
            )

        def keywords_background(mob, bg_color):
            r = Rectangle(width=mob.width+0.1, height=0.8, color=bg_color, fill_opacity=1)
            r.set_z_index(-1)
            r.move_to(mob)
            return r
            
        colors = [
            BLUE_C, RED_B, TEAL_D,
            TEAL_D, MAROON_B, BLUE_C,
            RED_B, MAROON_B,
        ]

        reset()

        keyword_texts = [
            Text(k, font="Monospace", color=WHITE)
            for k in [
                "for", "while", "true",
                "if", "else", "false",
                "return", "continue",
            ]
        ]
        keywords = VGroup(*keyword_texts)
        keyword_texts[0].shift(UP).to_edge(LEFT)
        keyword_texts[1].next_to(keyword_texts[0], RIGHT, buff=0.5)
        keyword_texts[2].next_to(keyword_texts[1], RIGHT, buff=0.5)

        keyword_texts[3].next_to(keyword_texts[0], DOWN, buff=0.6).to_edge(LEFT)
        keyword_texts[4].next_to(keyword_texts[3], RIGHT, buff=0.5)
        keyword_texts[5].next_to(keyword_texts[4], RIGHT, buff=0.5)

        keyword_texts[6].next_to(keyword_texts[3], DOWN, buff=0.6).to_edge(LEFT)
        keyword_texts[7].next_to(keyword_texts[6], RIGHT, buff=0.5)

        backgrounds = list(map(keywords_background, keyword_texts, colors))
        for i in range(8):
            self.play(
                FadeIn(keyword_texts[i], shift=RIGHT, run_time=0.2),
                FadeIn(backgrounds[i], shift=RIGHT, run_time=0.2),
            )

        reset()

        # Popular languages
        py = SVGMobject("logos/python-logo-generic.svg")
        #print(len(py.submobjects)) # 10
        
        py.submobjects[0].set_color(GRAY_A)
        py.submobjects[1].set_color(GRAY_A)
        py.submobjects[2].set_color(GRAY_A)
        py.submobjects[3].set_color(GRAY_A)
        py.submobjects[4].set_color(GRAY_A)
        py.submobjects[5].set_color(GRAY_A)
        py.submobjects[6].set_color(ManimColor.from_hex("#FFD43B", alpha=1.0))
        py.submobjects[7].set_color(ManimColor.from_hex("#4B8BBE", alpha=1.0))
        py.submobjects[8].set_color(GRAY_A)
        py.submobjects[9].set_opacity(0)

        snakes = VGroup(
            py.submobjects[6].copy().set_color(ManimColor.from_hex("#4B8BBE", alpha=1.0)),
            py.submobjects[7].copy().set_color(ManimColor.from_hex("#FFD43B", alpha=1.0)),
        ).to_edge(UP, buff=1).shift(LEFT*2)

        self.play(Write(py, run_time=2))
        self.wait(0.2)
        self.play(Transform(py, snakes, run_time=1))

        cpp = SVGMobject("logos/cpp.svg").scale(0.9).shift(DOWN*0.5)
        self.play(Write(cpp, run_time=2))
        self.wait(0.2)
        self.play(cpp.animate.to_edge(UP, buff=1))

        js = SVGMobject("logos/javascript.svg").scale(0.9).shift(DOWN*1.5)
        js.generate_target()
        js.target.to_edge(UP, buff=1).shift(RIGHT*4.5)
        self.play(Write(js, run_time=2))
        self.wait(0.2)
        self.play(MoveToTarget(js))

        reset()

        # Definition
        txt1 = Text("A PROGRAMMING LANGUAGE", font="Monospace", color=CUSTOM_PURPLE).scale(1.2)
        defi = VGroup(
            Text("is a system of notation that", font="Monospace").scale(0.7),
            Text("helps humans create computer", font="Monospace").scale(0.7),
            Text("programs.", font="Monospace").scale(0.7),
        ).arrange(DOWN, buff=0.5)

        self.play(Write(txt1, run_time=0.8, stroke_color=CUSTOM_PURPLE))
        self.play(txt1.animate(run_time=0.5).shift(UP*1.5))

        defi.next_to(txt1, DOWN, buff=0.8)
        for t in defi:
            t.align_to(txt1, LEFT).shift(RIGHT)

        self.play(Create(defi, run_time=1.2))

        syn = Text("has a unique set of syntaxes.", font="Monospace").scale(0.7)

        txt1.generate_target()
        txt1.target.to_edge(UP, buff=0.8)
        syn.next_to(txt1.target, DOWN, buff=0.8)

        self.wait(1.0)
        self.play(
            MoveToTarget(txt1, run_time=0.8),
            FadeTransform(defi, syn, run_time=0.8),
        )

        # Symbols and keywords
        def keywords_background(mob, bg_color):
            r = Rectangle(width=mob.width+0.06, height=0.5, color=bg_color, fill_opacity=1)
            r.set_z_index(-1)
            r.move_to(mob)
            return r
            
        colors = [
            BLUE_C, RED_B, TEAL_D,
            TEAL_D, MAROON_B, BLUE_C,
            RED_B, MAROON_B,
        ]

        keyword_texts = [
            Text(k, font="Monospace", color=WHITE).scale(0.75)
            for k in [
                "for", "while", "true",
                "if", "else", "false",
                "return", "continue",
            ]
        ]
        #keywords = VGroup(*keyword_texts)
        keyword_texts[0].to_edge(LEFT, buff=1.5)
        keyword_texts[1].next_to(keyword_texts[0], RIGHT, buff=0.3)
        keyword_texts[2].next_to(keyword_texts[1], RIGHT, buff=0.3)

        keyword_texts[3].next_to(keyword_texts[0], DOWN, buff=0.6).to_edge(LEFT, buff=1.5)
        keyword_texts[4].next_to(keyword_texts[3], RIGHT, buff=0.3)
        keyword_texts[5].next_to(keyword_texts[4], RIGHT, buff=0.3)

        keyword_texts[6].next_to(keyword_texts[3], DOWN, buff=0.6).to_edge(LEFT, buff=1.5)
        keyword_texts[7].next_to(keyword_texts[6], RIGHT, buff=0.3)

        backgrounds = list(map(keywords_background, keyword_texts, colors))
        anims = []
        for i in range(8):
            grp = VGroup(keyword_texts[i], backgrounds[i])
            anims.append(FadeIn(grp, shift=RIGHT, run_time=0.2))

        ##
        def symbols_background(mob, bg_color):
            c = Circle(radius=0.3, color=bg_color, fill_opacity=1).set_z_index(-1)
            c.move_to(mob)
            return c
            
        colors = [
            MAROON_B, BLUE_C, RED_B, TEAL_D,
            TEAL_D, MAROON_B, BLUE_C, RED_B,
            RED_B, TEAL_D, MAROON_B, BLUE_C,
        ]

        symbol_texts = [
            Text(s, font="Monospace", color=WHITE).scale(0.75)
            for s in [
                "()", "&", "*", ";",
                "#", "[]", "++", "!",
                "<>", "%", "{}", ":",
            ]
        ]
        symbols = VGroup(*symbol_texts)
        symbols.arrange_in_grid(cols=4, buff=0.6).to_edge(RIGHT, buff=1.5)
        symbols.align_to(keyword_texts[0], UP)

        backgrounds = list(map(symbols_background, symbol_texts, colors))
        symbols.add(*backgrounds)
        #anims.append(SpiralIn(symbols, run_time=1))

        #self.play(Succession(*anims))

        self.wait(0.5)
        self.play(
            Succession(*anims),
            SpiralIn(symbols, run_time=1.6),
        )

        reset()

        # Good vs bad searches
        searches = ImageMobject("searches-fix.PNG", scale_to_resolution=QUALITIES["medium_quality"]["pixel_height"])
        searches.set_z_index(-3)
        self.add(searches)

        def new_search(t, w):
            text = Text(t, font="Monospace", font_size=18, color=BLACK)
            bg = Rectangle(width=w, height=0.32, color=GREEN_A, fill_opacity=1).set_z_index(-1)
            bg.move_to(text)
            bg.align_to(text, LEFT)
            bg.shift(LEFT*0.05 + UP*0.03)
            text.match_x(bg)

            all = VGroup(text, bg)
            return all

        def white_bg(w, h):
            return Rectangle(width=w, height=h, color=WHITE, fill_opacity=1).set_z_index(-2)

        game_dev = new_search("game dev", 2.012)
        game_dev.shift(UP*0.85 + RIGHT*0.87)
        bg = white_bg(game_dev.width, game_dev.height)
        bg.move_to(game_dev)
        bg.align_to(game_dev, LEFT)

        self.wait(0.6)
        self.play(
            FadeIn(bg, run_time=0.3),
            FadeIn(game_dev, shift=DOWN, run_time=0.8),
        )

        game_engine = new_search("game engine", 2.476)
        game_engine.shift(UP*0.1 + LEFT*2.07)
        bg = white_bg(game_engine.width+0.4, game_engine.height)
        bg.move_to(game_engine)

        self.wait(0.2)
        self.play(
            FadeIn(bg, run_time=0.3),
            FadeIn(game_engine, shift=DOWN, run_time=0.8),
        )

        beginners = new_search("for game dev beginners", 3.352)
        beginners.shift(DOWN*0.615 + RIGHT*1.735)
        bg = white_bg(beginners.width, beginners.height)
        bg.move_to(beginners)
        bg.align_to(beginners, LEFT)

        self.wait(0.2)
        self.play(
            FadeIn(bg, run_time=0.3),
            FadeIn(beginners, shift=UP, run_time=0.8),
        )

        web_dev = new_search("web dev", 2.012).move_to(game_dev).align_to(game_dev, LEFT)
        web_course = new_search("web dev tutorial", 2.476).move_to(game_engine)
        web_beginners = new_search("for web dev newbies", 3.352).move_to(beginners).align_to(beginners, LEFT)

        web_dev[0].align_to(game_dev[0], UP)
        web_course[0].align_to(game_engine[0], UP)
        web_beginners[0].align_to(beginners[0], UP)

        self.wait(1.2)
        self.play(
            FadeOut(game_dev[0], game_engine[0], beginners[0], shift=RIGHT),
            FadeIn(web_dev[0], web_course[0], web_beginners[0], shift=RIGHT),
            run_time=0.5,
        )

        
        deep_learning = new_search("deep learning", 2.012).move_to(web_dev).align_to(web_dev, LEFT)
        DL_course = new_search("DL course", 2.476).move_to(web_course)
        for_DL = new_search("for deep learning", 3.352).move_to(web_beginners).align_to(web_beginners, LEFT)

        deep_learning[0].align_to(web_dev[0], UP)
        DL_course[0].align_to(web_course[0], UP)
        for_DL[0].align_to(web_beginners[0], UP)

        self.wait(1.2)
        self.play(
            FadeOut(web_dev[0], web_course[0], web_beginners[0], shift=RIGHT),
            FadeIn(deep_learning[0], DL_course[0], for_DL[0], shift=RIGHT),
            run_time=0.5,
        )

        print(deep_learning[1].width) #2.012
        print(web_course[1].width) # 2.476
        print(beginners[1].width) #3.352

        reset()

        # Python vs C++
        py = SVGMobject("logos/python-logo-generic.svg")
        #print(len(py.submobjects)) # 10
        
        py.submobjects[0].set_color(GRAY_A)
        py.submobjects[1].set_color(GRAY_A)
        py.submobjects[2].set_color(GRAY_A)
        py.submobjects[3].set_color(GRAY_A)
        py.submobjects[4].set_color(GRAY_A)
        py.submobjects[5].set_color(GRAY_A)
        py.submobjects[6].set_color(ManimColor.from_hex("#FFD43B", alpha=1.0))
        py.submobjects[7].set_color(ManimColor.from_hex("#4B8BBE", alpha=1.0))
        py.submobjects[8].set_color(GRAY_A)
        py.submobjects[9].set_opacity(0)

        snakes = VGroup(
            py.submobjects[6].copy().set_color(ManimColor.from_hex("#4B8BBE", alpha=1.0)),
            py.submobjects[7].copy().set_color(ManimColor.from_hex("#FFD43B", alpha=1.0)),
        ).to_edge(UP, buff=0.7).shift(LEFT*1.11)

        self.play(Write(py, run_time=1))
        self.wait(0.2)
        self.play(Transform(py, snakes, run_time=1))

        cpp = SVGMobject("logos/cpp.svg").scale(0.9).shift(DOWN*0.5)
        self.play(Write(cpp, run_time=1))
        self.wait(0.2)

        center_line = Line()
        center_line = Line(
            start=np.array([0, 5, 0]),
            end=np.array([0, -5, 0]),
        )
        center_line.stroke_width = 5
        center_line.set_color(CUSTOM_PURPLE)

        self.wait(0.5)
        self.play(
            cpp.animate.to_edge(UP, buff=0.7).shift(RIGHT*3.7),
            GrowFromEdge(center_line, UP),
        )

        py_bullets = VGroup(*[
            Text(t, font="Monospace", color=YELLOW)
            for t in [
                "Higher level",
                "Dynamically typed",
                "Interpreted",
                "Automatic memory management",
            ]
        ])
        py_bullets[0].scale(0.7)
        py_bullets[1].scale(0.7)
        py_bullets[2].scale(0.7)
        py_bullets[3].scale(0.55)

        py_bullets[0].set_color(YELLOW_A)
        py_bullets[1].set_color(BLUE_A)
        py_bullets[2].set_color(RED_A)
        py_bullets[3].set_color(GREEN_A)

        py_bullets.arrange(DOWN, buff=0.7).shift(DOWN*1)
        for t in py_bullets:
            t.match_x(py)

        cpp_bullets = VGroup(*[
            Text(t, font="Monospace", color=YELLOW)
            for t in [
                "Lower level",
                "Statically typed",
                "Compiled",
                "Manual memory management",
            ]
        ])
        cpp_bullets[0].scale(0.7)
        cpp_bullets[1].scale(0.7)
        cpp_bullets[2].scale(0.7)
        cpp_bullets[3].scale(0.55)

        cpp_bullets[0].set_color(YELLOW_A)
        cpp_bullets[1].set_color(BLUE_A)
        cpp_bullets[2].set_color(RED_A)
        cpp_bullets[3].set_color(GREEN_A)

        cpp_bullets.arrange(DOWN, buff=0.7).shift(DOWN*1)
        for t in cpp_bullets:
            t.match_x(cpp)

        self.wait(0.5)
        fade_ins = [FadeIn(b, shift=RIGHT) for b in py_bullets]
        self.play(LaggedStart(*fade_ins, lag_ratio=0.2))

        self.wait(0.5)
        fade_ins = [FadeIn(b, shift=LEFT) for b in cpp_bullets]
        self.play(LaggedStart(*fade_ins, lag_ratio=0.2))

        self.wait(0.5)
        self.play(
            ShrinkToCenter(py_bullets[2]),
            ShrinkToCenter(py_bullets[3]),
            ShrinkToCenter(cpp_bullets[2]),
            ShrinkToCenter(cpp_bullets[3]),
        )

        self.wait(0.5)
        self.play(
            py_bullets[0].animate(run_time=0.6).shift(DOWN*0.5),
            py_bullets[1].animate(run_time=0.6).shift(DOWN*1.5),
            cpp_bullets[0].animate(run_time=0.6).shift(DOWN*0.5),
            cpp_bullets[1].animate(run_time=0.6).shift(DOWN*1.5),
        )

        self.wait(0.5)
        self.play(
            FadeOut(py_bullets[1], shift=LEFT),
            FadeOut(cpp_bullets[1], shift=RIGHT),
        )

        self.wait(0.5)
        self.play(
            py.animate(run_time=0.6).shift(DOWN),
            py_bullets[0].animate(run_time=0.6).shift(DOWN),
            cpp.animate(run_time=0.6).shift(DOWN),
            cpp_bullets[0].animate(run_time=0.6).shift(DOWN),
        )

        self.wait(0.5)
        self.play(FadeOut(py_bullets[0], cpp_bullets[0], run_time=0.6))

        self.play(
            py.animate.scale(0.3).to_edge(UP, buff=0.15),
            cpp.animate.scale(0.3).to_edge(UP, buff=0.15),
        )

        reset()

        # High levels example output
        lines = VGroup(*[Text(t, font="Monospace", font_size=24, color=GRAY_A) for t in [
            "0 is even",
            "1 is odd",
            "2 is even",
            "3 is odd",
            "4 is even",
            "5 is odd",
            "6 is even",
            "7 is odd",
            "8 is even",
            "9 is odd",
        ]])
        lines.arrange(DOWN, buff=0.3)

        for l in lines:
            l.to_edge(LEFT)

        self.play(LaggedStart(*[
            FadeIn(l, shift=RIGHT, run_time=0.6) for l in lines
        ], lag_ratio=0.2))

        self.wait(0.5)
        return super().construct()