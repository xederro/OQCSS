### transpilation

unit matrix -> high-level quantum cirquit
high-level quantum cirquit -> low-level quantum cirquit
low-level quantum cirquit -> schedule of pulses

steps:
1. init - unroll custom instruction to one- and two- qbit gates
2. layout - map virtual qbits to physical qbits
3. routing - inject SWAP gates to make the circuit compatible with coupling
4. translation - translate to native gates of QPU
5. optimisation - make the circuit better
6. scheduling - add delay to schedule gate execution

