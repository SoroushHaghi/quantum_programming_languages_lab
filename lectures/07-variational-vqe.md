# 07 — From Simon's oracle to VQE

[← Course overview](../README.md) · [← Previous](06-oracle-algorithms.md)

**Topics:** Simon oracle clarification, parameterized quantum circuits (ansätze), energy expectation values, the variational principle, classical optimizers and hybrid quantum–classical algorithms.

**How the course develops:** After oracle-based algorithms, the lecture introduces a different workflow: the **classical optimizer chooses circuit parameters**, a quantum circuit evaluates a candidate state, and the optimizer adjusts the parameters.

**Class examples:**
- Revisiting Simon's XOR oracle construction and bit ordering.
- A small **Variational Quantum Eigensolver (VQE)** using Qiskit, a one-qubit Hamiltonian and numerical optimization.
- Accompanying handout material on ansatz design, Pauli-basis measurement and shot precision.

**Explore code:** [Minimal VQE Qiskit reconstruction](../examples/07_vqe.py) — independently written, AI-assisted illustrative code using exact statevector expectations; **not** a copy of the instructor notebook or a finite-shot hardware experiment.

**Intended outcome:** Understand the ansatz–energy–optimizer loop and how a small VQE calculation can be compared with exact diagonalization.
