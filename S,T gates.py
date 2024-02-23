from qiskit.visualization import plot_histogram,array_to_latex, plot_bloch_multivector,plot_state_city,plot_state_qsphere
from qiskit.visualization import visualize_transition
from qiskit import *

qc= QuantumCircuit(4,4)

qc.x(0)
qc.x(3)

 # visualize_transition(qc,trace=True) -> This wont work beacuse this is used to visualize only one qubit circuits
qc.measure(0,0)  # We are trying to measure the first qubit and it falls back to first classical bit
qc.barrier()
qc.measure(3,3) # Similar fashion 4th qubit to 4th classical bit

qc.draw("mpl")

qc= QuantumCircuit(4,4) 

qc.x(0)
qc.x(3)
#Here after applying gates we dont need to worry about measuring each qubit individually insteal we can use the measure_all() it will take care
qc.measure_all()  
qc.draw("mpl")

qc= QuantumCircuit(4,4)
#We are trying to apply different gates and seeing what will be the results
qc.x(0)
qc.y(0)
qc.x(3)

qc.measure_all()
qc.draw("mpl")

#S Gate
# !pip install seaborn
qc= QuantumCircuit(1,1)
qc.h(0)
qc.s(0)
# qc.measure_all()


qc.draw("mpl")

visualize_transition(qc,trace=True)

plot_state_city(qc,color=['purple','green'])
plot_state_qsphere(qc)

"""##SDG GATE

"""

qc= QuantumCircuit(1,1)
qc.h(0)
qc.sdg(0)


# qc.measure_all()
qc.draw("mpl")

visualize_transition(qc,trace=True)

"""## T gate

"""

qc= QuantumCircuit(1,1)
qc.h(0)
qc.t(0)


# qc.measure_all()
qc.draw("mpl")
visualize_transition(qc,trace=True)


"""## TDG gate - T Dagger"""

qc= QuantumCircuit(1,1)
qc.h(0)
qc.tdg(0)


# qc.measure_all()
qc.draw("mpl")


visualize_transition(qc,trace=True)

import qiskit_aer

from qiskit_aer import *

Aer.backends()

simulator=Aer.get_backend('statevector_simulator')

result=simulator.run(qc).result()
sv=result.get_statevector()
print(sv)


array_to_latex(sv)



qc.draw(output='mpl')


plot_bloch_multivector(sv)












