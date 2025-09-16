quantum computing uses quantum physics to store, process and transfer information
pendulum
spaghetti computer - soring in 2n+2 complexity, O(n) instead of O(n^2) bcs of phisics (push to the table, got largest)
moore's law - the current cpus have problem with the size of an atom
better energy effitiency
there are ptoblem p np np-hard, and aparently quantum easy
quantum parallelism
not all algorithms can be improved, physical system cannot be all-purpose
quantum algorithms: grover's database search, shor's factorization
right now we have noisy intermidiate scal quantum computers
reduce noise:
shield from radiation, light, vibration (also internal - temperature) etc.
quantum error correction, multiple physical cubits = one logical cubits

# what is quantum computing
**IQM academy** / ibm quantum platform / pennylane
understanding quantum technologies
qbit (quantum bit) - 2d complex vector
|0> = (1,0) |1> = (0,1)
| > dirac's ket notation
|$\psi$=p> = a1|0> + a2|1> <- superposition
quantum state cannot be copied!
norm ||p>| =sqrt(<p|p>)=sqrt(|a0|^2+|a1|^2) <- normalised

|p> =cosd/2|0> + $e^{i\psi}$sind/2|1>

IQM uses transmon

a0^2 -> probability you get 0, a1^2 probabilisty you gate 1
(|0> + |1>)/sqrt(2) = uniform distribution of 0s and 1s

its in state psi not 0 not 1, only during the measurement the sate 0 and 1 is defined




**multi qubit systems and entanglement**
having 2 cubits we could write it in |0>|1> or |01>
nothing propagates so its not faster than light
two cubit state is C^4
the only way to entagle is to have one qbit decide on second one, so (|00>+|01>)/sqrt(2) is not entangled but (|10>+|01>)/sqrt(2) is
product state is oposite of entangled
