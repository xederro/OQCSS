Q: what is the state of a given quantum system



### Testing problems
(X,A) <- measurable space, X probability, A events
O paramether set
PV - probability measures : V in O
(X, A, {PV : V in 0}) is called experiment / statistical model.

special case:
E=(X, A, {P,Q})
binary experiment <- simplest setting

testing problem for experiment E is given by a deomposition O0 union O1 = O of the parameter space O and coresponding null hypothesis
H0: Pv. V in O0 so probabilities Pv when V in O0
or alternative 
H1: Pv. V in O1 so probabilities Pv when V in O1

simple jipothesis testing problem refering to binary experimets 
E=(X, A, {P,Q})
H0=P vs H1=Q

main focis on simple hypothesis testing problems

many fundamental testing problems can be reduced to this case

Q: what is the testing problem
testing problem s represent optimisation problems where the optimisation gas to be done on the set of tests F
A test is a measurable function f:X->\[0,1\], We denote the set of tests on (X,A)

$\alpha$ level tests
we optimise $\int f(x) dQ = sup(f)$ 
with condition $\int f(x) dP <= \alpha$ 
where $\alpha \in (0,1)$ best case close to 0


![Drawing 2025-09-17 09.28.37.excalidraw](Drawing%202025-09-17%2009.28.37.excalidraw.md)