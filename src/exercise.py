from typing import List

from matplotlib.figure import Figure
from matplotlib.pyplot import Axes
from pytm import AbstractExercise
from pytm import Latex
from pytm import Option
from pytm import Output

from .helpers import *


class Exercise(AbstractExercise):
    def start(self, gas: float = None, temp: str = None) -> Output:
        options: List[Option] = list(map(lambda opt: Option(opt[0], opt[1], opt[0] == gas), self._get_option_map()))

        return self.output \
            .add_paragraph(Latex(r'''
            Mit diesem Tool können Sie die mittlere Wärmekapazität (Cp) und Entropie-Temperaturfunktion (s0) der 
            idealen Gase (Air, $\mathrm{N_{2}*}$, $\mathrm{N_{2}}$, $\mathrm{O_{2}}$, $\mathrm{CO_{2}}$, 
            $\mathrm{H_{2}O}$, $\mathrm{SO_{2}}$) bei einer Temperatur zwischen -60 und 2'200 °C bestimmen. 
            ''')) \
            .add_option_group(name='gas',
                              label=Latex(r'Ideales Gas auswählen'),
                              options=options) \
            .add_number_field(name='temp',
                              label=Latex(r'Tragen Sie die Temperatur ein, in °C'),
                              value=temp,
                              min_value=-60,
                              max_value=2200,
                              step=0.01) \
            .add_action('Submit', self.calculate)

    def calculate(self, gas: str, temp: float) -> Output:
        gas_config = list(filter(lambda config: config[0] == gas, self._get_option_map()))[0]

        cp_command = gas_config[2]
        cp = np.around(cp_command(temp), 4)

        s0_command = gas_config[3]
        s0 = np.around(s0_command(temp), 4)

        # Plotting the data
        temp_range = np.linspace(-50, 2200, 200)  # the range of data is -60 °C  to 2'200 °C

        figure: Figure = Figure()

        plot1: Axes = figure.add_subplot(2, 1, 1)
        plot1.plot(temp_range, cp_command(temp_range), label=cp_command.__name__)
        plot1.set_title('Cp_averages from 0 °C to t(°C)')
        plot1.set_xlabel('Final Temperature [deg C]')
        plot1.set_ylabel('Cp_ave in kJ/(kg K)')
        plot1.legend(loc='best')
        plot1.grid()

        plot2 = figure.add_subplot(2, 1, 2)
        plot2.plot(temp_range, s0_command(temp_range), label=s0_command.__name__)
        plot2.set_title('s0-Function')
        plot2.set_xlabel('Final Temperature [deg C]')
        plot2.set_ylabel('s0 Function in kJ/(kg K)')
        plot2.legend(loc='best')
        plot2.grid()

        figure.tight_layout()

        return self.output \
            .add_paragraph(Latex(r'''
            Die mittlere Wärmekapazität Cp für {gas} im Bereich 0°C bis {temp} °C ist: {cp} in kJ/(kg K).
            '''.format(gas=gas, temp=temp, cp=cp))) \
            .add_paragraph(Latex(r'''
            Die  Entropie-Temperaturfunktion s0 für {gas} bei {temp} °C ist: {s0} in kJ/(kg K).
            '''.format(gas=gas, temp=temp, s0=s0))) \
            .add_figure(figure) \
            .add_action('Back to start', self.start, gas=gas, temp=temp)

    @staticmethod
    def _get_option_map() -> list:
        return [
            ['Air', Latex(r'Air'), Cp_ave_Air, s_abs_Air],
            ['N2s', Latex(r'Luftstickstoff'), Cp_ave_N2s, s_abs_N2s],
            ['N2', Latex(r'$\mathrm{N_{2}}$'), Cp_ave_N2, s_abs_N2],
            ['O2', Latex(r'$\mathrm{O_{2}}$'), Cp_ave_O2, s_abs_O2],
            ['CO2', Latex(r'$\mathrm{CO_{2}}$'), Cp_ave_CO2, s_abs_CO2],
            ['H2O', Latex(r'$\mathrm{H_{2}O}$'), Cp_ave_H2O, s_abs_H2O],
            ['SO2', Latex(r'$\mathrm{SO_{2}}$'), Cp_ave_SO2, s_abs_SO2],
        ]
