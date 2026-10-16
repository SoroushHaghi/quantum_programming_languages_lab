# 05 — First steps in Qiskit

[← Course overview](../README.md) · [← Previous](04-adiabatic-optimization.md) · [Next →](06-oracle-algorithms.md)

**Topics:** Gate-model circuit construction, controlled operations, circuit composition, transpilation, simulator backends, measurement shots and outcome counts, qubit/bit ordering, and phase interference.

**How the course develops:** Earlier gates and entanglement ideas become programmatic circuit operations. Bernstein–Vazirani introduces the oracle-algorithm viewpoint.

**Class examples:**
- Building small gate circuits and preparing a three-qubit **GHZ state**.
- Simulating measurement outcomes, interpreting histograms and distinguishing finite-shot fluctuations from ideal probabilities.
- Introducing the Bernstein–Vazirani problem and its circuit structure.
- DiVincenzo criteria connecting programmable gates, qubit initialization, coherence and measurement to physical devices.

**Study example:** [GHZ circuit in Qiskit](../examples/05_ghz.py).

**Intended outcome:** Know the basic circuit → simulate → measure workflow, including what measured counts do and do not prove.

