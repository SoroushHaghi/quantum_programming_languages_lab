# Quantum Programming Languages — Learning Lab

An evolving portfolio based on the [Quantum Programming Languages course](https://psiket.com/en/courses/quantum-language) offered by PsiKet Academy. Browse the concepts and their associated examples by **scientific topic**.

## Explore the topics

| Area | Focus |
| --- | --- |
| [Quantum Foundations & Gates](topics/quantum-foundations-and-gates.md) | Quantum states, measurement, qubits, entanglement and gates |
| [Photonic & Continuous-Variable Computing](topics/photonic-continuous-variables.md) | Optical states, Gaussian operations and boson sampling |
| [Adiabatic Optimization](topics/adiabatic-optimization.md) | Hamiltonian evolution, spectral gaps, Max-Cut and Ising/QUBO |
| [Qiskit Circuits & Simulation](topics/qiskit-circuits.md) | Circuit construction, GHZ, transpilation and measurements |
| [Oracle Algorithms](topics/oracle-algorithms.md) | Bernstein–Vazirani, Simon, phase kickback and GF(2) |
| [Variational & Hybrid Algorithms](topics/variational-algorithms.md) | Parameterized circuits, VQE and classical optimization |

The topics follow a logical progression from foundations to implementation. They are not organized by lecture number.

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
