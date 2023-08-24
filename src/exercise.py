
from typing import List
import random
from matplotlib.figure import Figure
from matplotlib.pyplot import Axes
from pytmlib import AbstractExercise
from pytmlib import Latex
from pytmlib import Output
import numpy as np

max = [3.1,4.2,5.3]
step = [0.1,0.2,0.3]
z = [0,1,2]

class Exercise(AbstractExercise):
    @property
    def version(self) -> str:
        return "1.0.0"

    def start(self, schnittpunkt: str = None,counter: int = 0) -> Output:
        if counter == 0:
            i = random.choice(z)
            a = np.arange(step[i], max[i], step[i])

        return self.output \
            .add_paragraph(Latex(f'''Gegeben ist ein Vektor a: [{a[0]}, {round(a[1],2)}, {round(a[2],2)},...{round(a[-1],2)}]\n
              und zwei Gleichungen:\n 
              - $\mathrm b_i$ = $\mathrm a_i$ * $\mathrm a_i$ \n
              - $\mathrm c_i$ = $\mathrm a_i$ + $\mathrm a_i$\n
              ''')) \
            .add_number_field(name='schnittpunkt',
                              label=Latex(r'ab welchem Wert von $\mathrm a_i$ ist $\mathrm b_i$ grösser als'
                                          r' $\mathrm c_i$?'),
                              value=schnittpunkt,
                              min_value=0,
                              max_value=2200,
                              step=0.01) \
            .add_action('Lösung', self.calculate,a=a)\
            .add_action("Analytischer Lösungsweg",self.analytic_solution)


    def analytic_solution(self,schnittpunkt: float):
        return self.output \
            .add_image(".\static\Analytic_solution.PNG") \
            .add_action('Back to start', self.start, schnittpunkt=schnittpunkt)


    def calculate(self, schnittpunkt: float, a:float) -> Output:

        # Berechne die Vektoren b und c
        b = a ** 2
        c = a + a

        # Finde den Schnittpunkt
        try:
            intersection_index = np.where(b >= c)[0][0]
        except:
            intersection_index = np.where(b > c)[0][0]

        intersection_a = a[intersection_index]
        intersection_b = b[intersection_index]
        intersection_c = c[intersection_index]

        # Überprüfen des Resultats
        if intersection_a == schnittpunkt:
            answ = "Richtig"
        else:
            answ = "Falsch, schauen Sie sich das Diagramm mit dem Plot an"

        fig_width_size= 10
        fig_height_size= 5

        figure: Figure = Figure()
        plot1: Axes = figure.add_subplot(1,1,1)
        # Plotte die Kurven
        plot1.plot(a, b,"x", label='b = a^2')
        plot1.plot(a, c,"o", label='c = a + a')
        plot1.scatter(intersection_a, intersection_b, color='red', label=f'b>c ab einem Wert von:'
                                                                         f' {round(intersection_a,3)}')

        # Beschriftungen
        plot1.set_xlabel('a')
        plot1.set_ylabel('Wert')
        plot1.legend()
        plot1.grid()
        figure.set_figwidth(fig_width_size)
        figure.set_figheight(fig_height_size)
        figure.tight_layout()

        return self.output \
            .add_paragraph(Latex(f''' {answ}''')) \
            .add_figure(figure) \
            .add_action('Back to start', self.start, schnittpunkt=schnittpunkt)

