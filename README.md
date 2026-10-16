# Quantum Programming Languages — Learning Lab

An evolving portfolio based on the [Quantum Programming Languages course](https://psiket.com/en/courses/quantum-language) offered by PsiKet Academy. Browse the concepts and their associated examples by **scientific topic**.

## Progress checklist

Checked items have been **covered in class**; unchecked items are **upcoming course syllabus**, not personal assignments or claims of proficiency.

### Topics already covered

- [x] [Quantum Foundations & Gates](topics/quantum-foundations-and-gates.md) — quantum states, measurement, entanglement and gates
- [x] [Photonic & Continuous-Variable Computing](topics/photonic-continuous-variables.md) — optical states and Gaussian operations
- [x] [Adiabatic Optimization](topics/adiabatic-optimization.md) — Ising/QUBO, Max-Cut and routing formulations
- [x] [Qiskit Circuits & Simulation](topics/qiskit-circuits.md) — circuit construction, GHZ and measurement
- [x] [Oracle Algorithms](topics/oracle-algorithms.md) — Bernstein–Vazirani, Simon and GF(2)
- [x] [Variational & Hybrid Algorithms](topics/variational-algorithms.md) — parameterized circuits and introductory VQE

### Upcoming course topics

**Advanced Qiskit**
- [ ] Noise models and noisy quantum-circuit simulation
- [ ] Quantum machine learning concepts and algorithms

**PennyLane**
- [ ] Parameterized and dynamic quantum circuits
- [ ] Discrete-variable and continuous-variable programming
- [ ] Quantum machine learning with hybrid quantum–classical models

**D-Wave Ocean**
- [ ] Ising/QUBO modeling and quantum-annealing workflows
- [ ] Graph, routing and logistics optimization examples

**Course project**
- [ ] Problem formulation, quantum-oriented implementation and comparison with classical methods

*Upcoming items follow the published course outline. Exact teaching order and dates may change; boxes are checked only when the relevant content has actually been taught.*

## Code examples

- [GHZ state](examples/ghz_state.py)
- [Bernstein–Vazirani](examples/bernstein_vazirani.py)
- [Variational Quantum Eigensolver](examples/vqe.py)

These are AI-assisted educational reconstructions of course examples—not redistributed instructor files or independently verified student implementations. Personally completed work and experiments will be added with evidence.

To try them locally (Qiskit, NumPy and SciPy):

```bash
python -m pip install qiskit numpy scipy
python examples/ghz_state.py
python examples/bernstein_vazirani.py
python examples/vqe.py
```

Execution under a complete Qiskit SDK environment has not yet been verified. Instructor materials and private notes remain private. This is an independent portfolio, not an official course repository.
