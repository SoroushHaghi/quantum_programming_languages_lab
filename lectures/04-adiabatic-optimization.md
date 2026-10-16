# 04 — Adiabatic computing and optimization

[← Course overview](../README.md) · [← Previous](03-continuous-variables.md) · [Next →](05-qiskit-circuits.md)

**Topics:** The adiabatic theorem, time-dependent Hamiltonian interpolation, avoided crossings and minimum spectral gaps, annealing schedules, Ising couplings, QUBO formulations, graph optimization and hardware embedding.

**How the course develops:** Computation moves from circuit sequences to **encoding a problem in a final Hamiltonian** and searching for a low-energy configuration through gradual evolution.

**Class material:**
- **Annealing schedule:** Avoided crossings, local slowing near a small gap, and the Grover-search connection.
- **Max-Cut:** A small graph, bit assignments and the connection between a graph cut and a ZZ interaction.
- **Traveling Salesperson Problem:** One-hot city–time variables, route-length objective, visit/position constraints and quadratic penalties.
- **Practical limits:** Small spectral gaps, variable scaling and restricted hardware connectivity.

**Intended outcome:** Map a small combinatorial problem to an Ising/QUBO energy function and identify the constraints of practical implementation.
