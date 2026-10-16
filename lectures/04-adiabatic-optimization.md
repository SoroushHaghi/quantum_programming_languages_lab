# 04 — Adiabatic computing and optimization

[← Course overview](../README.md) · [← Previous](03-continuous-variables.md) · [Next →](05-qiskit-circuits.md)

**Topics:** The adiabatic theorem, time-dependent Hamiltonian interpolation, spectral gaps, annealing schedules, Ising couplings, QUBO formulations, graph optimization and hardware embedding.

**How the course develops:** Computation moves from circuit sequences to **encoding a problem in a final Hamiltonian** and searching for a low-energy configuration through gradual evolution.

**Class material:**
- **Max-Cut:** A small graph, bit assignments and the connection between a graph cut and a ZZ interaction.
- **Traveling Salesperson Problem:** City–position encoding, route constraints and penalty terms.
- **Practical limits:** Spectral gap, number of binary variables and restricted hardware connectivity.

**Intended outcome:** Understand the mathematical mapping from a combinatorial objective to an Ising/QUBO energy function, and why a valid mapping does not automatically imply practical speedup.
