# Quantum Programming Languages — Learning Lab

A public guide to my ongoing study of [Quantum Programming Languages](https://psiket.com/en/courses/quantum-language) with PsiKet Academy: **what each lecture covered, which examples were discussed, and what each stage is meant to achieve.**

## Explore the lectures

| Lecture | Topics | Details |
| --- | --- | --- |
| 01 | Quantum states, measurement and computation models | [Explore](lectures/01-foundations.md) |
| 02 | Qubits, entanglement and quantum gates | [Explore](lectures/02-qubits-gates.md) |
| 03 | Continuous-variable and photonic computing | [Explore](lectures/03-continuous-variables.md) |
| 04 | Adiabatic computing, Ising/QUBO and optimization | [Explore](lectures/04-adiabatic-optimization.md) |
| 05 | Qiskit circuits, simulation and GHZ | [Explore](lectures/05-qiskit-circuits.md) |
| 06 | Bernstein–Vazirani and Simon's algorithm | [Explore](lectures/06-oracle-algorithms.md) |
| 07 | Simon recap and hybrid VQE | [Explore](lectures/07-variational-vqe.md) |

**Course coverage:** Lectures 01–07 (16 October 2026).

## Code and development

The [Qiskit examples](examples/) are AI-assisted study reconstructions of GHZ, Bernstein–Vazirani and VQE. They are not copies of instructor notebooks or evidence of personally validated student implementations. Independent code, tests and experiments will be added as completed.

**Run the study examples** (Python environment with Qiskit, NumPy and SciPy):

```bash
python -m pip install qiskit numpy scipy
python examples/05_ghz.py
python examples/06_bernstein_vazirani.py
python examples/07_vqe.py
```

The mathematical checks have been reviewed, but Qiskit execution in a complete SDK environment remains to be verified.

Original classroom materials and my full private study notes are not distributed here. This is an independent learning record, not an official course repository.
