# Quantum Programming Languages — Learning Lab

An evolving portfolio based on the [Quantum Programming Languages course](https://psiket.com/en/courses/quantum-language) offered by PsiKet Academy. Browse the concepts and their associated examples by **scientific topic**.

## Progress checklist

**How to read this:** A checked **course topic** means it has been covered in class. A checked **personal milestone** will mean I have studied, reproduced and verified the work myself. The two are tracked separately.

### Topics covered in class

- [x] [Quantum Foundations & Gates](topics/quantum-foundations-and-gates.md) — states, measurement, entanglement and gates
- [x] [Photonic & Continuous-Variable Computing](topics/photonic-continuous-variables.md) — optical states and Gaussian operations
- [x] [Adiabatic Optimization](topics/adiabatic-optimization.md) — Ising/QUBO, Max-Cut and routing formulations
- [x] [Qiskit Circuits & Simulation](topics/qiskit-circuits.md) — circuit construction, GHZ and measurement
- [x] [Oracle Algorithms](topics/oracle-algorithms.md) — Bernstein–Vazirani, Simon and GF(2)
- [x] [Variational & Hybrid Algorithms](topics/variational-algorithms.md) — parameterized circuits and introductory VQE

### Personal learning roadmap

**Foundation review**
- [ ] Explain quantum states, gates, measurement and entanglement; work through a small circuit by hand.
- [ ] Review optical CV states and Gaussian operations with a worked example.
- [ ] Derive and classically verify a small Max-Cut Ising/QUBO model.

**Reproduce and verify**
- [ ] Run the GHZ circuit and check expected measurement outcomes.
- [ ] Rebuild Bernstein–Vazirani and test different hidden strings and bit orders.
- [ ] Build a Simon oracle and solve measurement equations over GF(2).
- [ ] Run the one-qubit VQE, verify the minimum against exact diagonalization, and explore sampling effects.

**Go beyond the examples**
- [ ] Design an original experiment, compare with a classical baseline and document reproducible results.

### Further course modules

The published course outline also includes these directions, which are not yet represented as completed practical work here:

- [ ] Extended Qiskit work: noise-aware simulation and quantum machine learning.
- [ ] PennyLane: parameterized quantum circuits, discrete/continuous variables and quantum ML.
- [ ] D-Wave Ocean: Ising/QUBO optimization workflows and graph/logistics examples.

*The checklist advances when work is actually covered or verified, rather than against arbitrary dates. Last reviewed: 16 October 2026.*

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
