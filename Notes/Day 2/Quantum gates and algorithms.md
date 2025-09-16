quantum gates

quantum algorithm
bcs of entanglement we can have up to exponential speedup. bcs of the solving all states at once

grover's quantum search algorithm 1/2N -> sqrt(N)

Fault Tolerant quantum computing is a future, bcs we have to have 10^9 qubits to achieve 6s 9 of accuracy
NISQ (noisy intermediate scale quantum) computers

1. quantum state is a vector |p> = C^n where n is positive integer. 
2. for physical quantity a there is coresponding Hermitian matrix A -> A^T (a dagger) = A
3. energy of the system i Hamiltonian of the system it tels the state |p> how to evolve in time
   shrodinger equation

qbit gate and quantum circuit
its operation that changes the state of the qbit, so changes vector to another vector. the matrix. these are always revesible bcs U^T*U = 1


## one cubit gate

**X** = bitflip not
**Y** = 0->i|0>, 1->-i|1>
**Z** = change phase, 0->0, 1->-1
**Hadamard gate** https://www.iqmacademy.com/curriculum/workshop-en-1.html
maps 0 and 1 to superposition states
**identity gate**
does nothing

tensor product of matrices


applying from right to left! if multiple to entangled

## Two qubit gates
CNOT = chooses two qbits, does nothing to x, flips y if x is 1
1000
0001
0010
0100


any n-qubit unitary gate can be decomposed into one-cubit gate and cnot gate

## NISQ Computer

a hybrid algorithm
state -> **ansatz (quantum cirquit)** -measurement-> cost function -> optimizer
these types of algorithms are noise resilient and it allows to study bigger problems

ansatze - the collection of states, we can change the parrameters to change the space


encode the problem you want to solve
cost function should be the energy of the system since it naturally (Hamiltonian) wants to be in lowest state

### Classical optimiser
gradient-based optimiser 
particle swarm based optimiser

what is variatonal quantum algorithm
Variational principle

cost function <p({ti})|H|p({ti})> <- the energy in that state

### variational quantum eigensolver VQE

### adiabatic quantum computing
there are no quantum gates, these are use only to optimize (D-wave), by finding lowest energy of system (cost function)
we prepare very simple state, for example all qbits the same, and gradually change the hamiltonian, to the one we care about. doing i very slowly we end up in lowest state of the eigenstate of H1
adiobatic -> slow

Ht=1-t/T\*H0+t/T\*H1

### QAOA quantum annealing optimisation algorithm

