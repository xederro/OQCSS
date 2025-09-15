Basics of quantum gates
2 types of computers
universal -> quantum gate based
QUBO -> QAC - all at once

quantum bit
superposition - 1/0 decided during measurement (collapse of quantum state) with 1/2 probability (hadamrd gate)

2qubit entanglement
qubit can be represented by 2x2 matrix, 2^n would be the size of matrix that operates on n qbits

adiabatic quantum computing

quantum tunneling

qubic unconstraid binary optimisation
sum(aixi) + sum(bijxixj) <- qubic part, this is the only way to solve by quantum annealing
0.0003ms


hubo
higher-order ubo

gate-based
identity gate - doesn't change the qubit
10
01

hadamard gate - superposition transform so 1 or 0
11
1-1 \*1/sqrt(2)

pauli gates - rotates the qubit 180deg, all other gates can be represented by this gate
x
01
10
y
0-i
i0
z
10
0-1

phase related gates - adds pgase shift to |1> without changing probability amplitudes
p(g)
10
0$e^{-ig}$




quantum usecases
qiskit optimisation package - gold standard

ansatz (example)

shores algorithm

its better not to add more than 2000 gates bsc probability goes brr
