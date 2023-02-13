from manim import *
import math

def GetTexString(num: ValueTracker):
    return MathTex("f(x) = \\frac{"+str(math.ceil(num.get_value()))+"}{16-\pi}(cos(\pi\cdot x)-cos(4\cdot x))")

class FxPlotting(Scene):
    def construct(self):

        eqTracker = ValueTracker(20)
        eq = GetTexString(eqTracker)

        desc = Text("Beating Oscillation")
        desc.next_to(eq,DOWN)
        desc.scale(.4)

        self.play(Write(eq), Write(desc))
        self.play(eq.animate.shift(LEFT*4, UP*3).scale(.5), desc.animate.shift(LEFT*4, UP*3.6).scale(.5))

        axes = Axes(
            x_range=[-10, 10, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-10, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            y_axis_config={
                "numbers_to_include": np.arange(-5, 5.01, 1),
            },
            tips=False,
        )
        axes_labels = axes.get_axis_labels()

        dif_beating = axes.plot(lambda x: (eqTracker.get_value()/(16-np.pi))*(np.cos(np.pi*x)-np.cos(4*x)), color=RED)

        # cos_label = axes.get_graph_label(dif_beating, label="\\cos(x)")

        # vert_line = axes.get_vertical_line(
        #     axes.i2gp(TAU, dif_beating), color=YELLOW, line_func=Line
        # )
        # line_label = axes.get_graph_label(
        #     dif_beating, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
        # )

        eq.add_updater(lambda x: eq.become(GetTexString(eqTracker)))
        dif_beating.add_updater(lambda x: dif_beating.become(axes.plot(lambda x: (eqTracker.get_value()/(16-np.pi))*(np.cos(np.pi*x)-np.cos(4*x)), color=RED)))
        # eq.add_updater(lambda x: eq.save_state().become(GetTexString(eqTracker)).restore())


        plot = VGroup(axes)
        labels = VGroup(axes_labels)
        self.play(DrawBorderThenFill(plot),Write(labels))
        self.play(Write(dif_beating))
        self.play(eqTracker.animate.increment_value(60))
        self.wait(duration=3)

