from manim import *

class MathEq(Scene):
    def construct(self):
        dist = MathTex(r"d=202.57\space m", font_size=50)
        time = MathTex(r"t=20.066\space s", font_size=50)
        eq1 = MathTex(r"v = 202.57\space m\space /\space 20.066\space s", font_size=50)
        eq2 = MathTex(r"v = 10.095\space m/s", font_size=50)
        eq3 = MathTex(r"v = 10.095\space m/s\space\times 3.6", font_size=50)
        eq4 = MathTex(r"v = 36.342\space km/h", font_size=50)

        self.play(Write(dist.shift(UP*2)))
        self.play(Write(time.shift(UP)))

        for i, eq in enumerate([eq1, eq2, eq3, eq4]):
            self.play(Write(eq.shift(DOWN*i)))
        
        self.wait(3)
            
