from typing import List
from typing import Union

from matplotlib.figure import Figure
from pytm import AbstractExercise
from pytm import Latex
from pytm import Option
from pytm import Output


class Exercise(AbstractExercise):
    def start(self) -> Output:
        return self.output \
            .add_paragraph(Latex(r'''
            Mit diesem Tool können Sie die mittlere Wärmekapazität (Cp) und Entropie-Temperaturfunktion (s0) der 
            idealen Gase (Air, $\mathrm{N_{2}*}$, $\mathrm{N_{2}}$, $\mathrm{O_{2}}$, $\mathrm{CO_{2}}$, 
            $\mathrm{H_{2}O}$, $\mathrm{SO_{2}}$) bei einer Temperatur zwischen -60 und 2'200 °C bestimmen. 
            ''')) \
            .add_option_group(name='gas',
                              label=Latex(r'Gas'),
                              options=[
                                  Option('Air', Latex(r'Air'), True),
                                  Option('N2s', Latex(r'Luftstickstoff')),
                                  Option('N2', Latex(r'$\mathrm{N_{2}}$')),
                                  Option('O2', Latex(r'$\mathrm{O_{2}}$')),
                                  Option('CO2', Latex(r'$\mathrm{CO_{2}}$')),
                                  Option('H2O', Latex(r'$\mathrm{H_{2}O}$')),
                                  Option('SO2', Latex(r'$\mathrm{SO_{2}}$')),
                              ]) \
            .add_number_field(name='temp',
                              label=Latex(r'Tragen Sie die Temperatur ein, in °C'),
                              min_value=-60,
                              max_value=2200,
                              step=0.01) \
            .add_action('Submit', self.action, var1='test 42')

    def action(self, option: List[int], text: float, var1: str = None) -> Output:
        table: List[List[Union[str, Latex]]] = [['#ID', 'Value']]
        table += list(map(lambda idx: [idx, Latex(r'$\mathrm{NO_2}$')], range(1, 10)))
        return self.output \
            .add_paragraph('%s %s %d' % (text, var1, option[0])) \
            .add_latex(r'''
            \section{Mathematical Formulae}
            
            Math is typeset using KaTeX. Inline math:
            $
            f(x) = \int_{-\infty}^\infty \hat f(\xi)\,e^{2 \pi i \xi x} \, d\xi
            $
            as well as display math is supported:
            $$
            f(n) = \begin{cases} \frac{n}{2}, & \text{if } n\text{ is even} \\ 3n+1, & \text{if } n\text{ is odd} \end{cases}
            $$
            ''') \
            .add_table(table) \
            .add_number_field('text', 'Text', text) \
            .add_action('Go to figure', self.figure)

    def figure(self) -> Output:
        figure: Figure = Figure()
        figure.subplot_mosaic("AB;CC")

        return self.output \
            .add_score(0.42) \
            .add_figure(figure) \
            .add_action('Back to start', self.start)
