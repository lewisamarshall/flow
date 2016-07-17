import ebb
from ebb.pipes import RectangularPipe
from ebb.fluids import Air
from ebb import Q

pipe = RectangularPipe(width=Q('1e-3 m'), height=Q('3e-4 m'), length=Q('2e-2 m'))
# pipe.resistance()
print(pipe.resistance(fluid=Air))
print(pipe.flow(fluid=Air, pressure=Q('0.1 psi')))
print(pipe.maximum_velocity(fluid=Air, pressure=Q('0.1 psi')))
print(pipe.reynolds(fluid=Air, pressure=Q('0.1 psi')))
