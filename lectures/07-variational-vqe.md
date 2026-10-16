# 07 — From Simon's oracle to VQE

[← Course overview](../README.md) · [← Previous](06-oracle-algorithms.md)

**Topics:** Simon oracle clarification, parameterized quantum circuits (ansätze), Pauli expectation values, the variational principle, classical optimizers and hybrid quantum–classical algorithms.

**How the course develops:** After oracle-based algorithms, the lecture introduces a different workflow: the **classical optimizer chooses circuit parameters**, a quantum circuit evaluates a candidate state, and the optimizer adjusts the parameters.

**Class examples:**
- Revisiting Simon's XOR oracle construction and bit ordering.
- A one-qubit **VQE** example using the Hamiltonian \(H=2X-Z\), an \(R_y\) ansatz and classical optimization, with exact reference ground energy \(-\sqrt{5}\).
- Accompanying handout material on ansatz design, Pauli-basis measurement and shot precision.

**Study example:** [One-qubit VQE in Qiskit](../examples/07_vqe.py).

**Intended outcome:** Understand the ansatz–energy–optimizer loop and how a small VQE calculation can be compared with exact diagonalization.
