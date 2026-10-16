# 06 — Bernstein–Vazirani and Simon's algorithm

[← Course overview](../README.md) · [← Previous](05-qiskit-circuits.md) · [Next →](07-variational-vqe.md)

**Topics:** Hidden-string problems, Boolean and reversible quantum oracles, Hadamard interference, phase kickback, the Bernstein–Vazirani query model, Simon's hidden XOR period and linear equations over GF(2).

**How the course develops:** The emphasis shifts from drawing circuits to seeing **how oracle structure makes a measured bit string informative**.

**Class examples:**
- **Bernstein–Vazirani:** A Qiskit circuit constructs the oracle from CNOT gates and produces a measurement histogram.
- **Simon:** The two-register circuit and the XOR-promise are explained; implementing the oracle and recovering the hidden mask with GF(2) post-processing are assigned exercises, **not** a completed classroom notebook.

**Explore code:** [Bernstein–Vazirani Qiskit reconstruction](../examples/06_bernstein_vazirani.py) — newly written study code, not a reproduction of the instructor's source file.

**Intended outcome:** Explain what phase kickback does, what a BV result reveals, and why Simon requires multiple measurements and classical linear algebra.
