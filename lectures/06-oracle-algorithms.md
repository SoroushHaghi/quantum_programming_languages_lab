# 06 — Bernstein–Vazirani and Simon's algorithm

[← Course overview](../README.md) · [← Previous](05-qiskit-circuits.md) · [Next →](07-variational-vqe.md)

**Topics:** Hidden-string problems, Boolean and reversible quantum oracles, Hadamard interference, phase kickback, Bernstein–Vazirani oracle-query complexity, Simon's hidden XOR period, and linear equations and Gaussian elimination over GF(2).

**How the course develops:** The emphasis shifts from drawing circuits to seeing **how oracle structure makes a measured bit string informative**.

**Class examples:**
- **Bernstein–Vazirani:** A four-bit Qiskit oracle constructed from CNOT gates, followed by a measurement histogram.
- **Simon:** The XOR-period promise and two-register circuit are introduced; oracle construction and GF(2) decoding are assigned exercises.

**Study example:** [Bernstein–Vazirani circuit in Qiskit](../examples/06_bernstein_vazirani.py).

**Intended outcome:** Explain what phase kickback does, what a BV result reveals, and why Simon requires multiple measurements and classical linear algebra.
