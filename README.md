# Quantum Programming Languages — Learning Lab

An independent record of the [Quantum Programming Languages course](https://psiket.com/en/courses/quantum-language) offered by PsiKet Academy. This repository documents the lecture sequence and will gradually include my own reproducible implementations and experiments.

**Current course coverage:** Lectures 1–7 (16 October 2026). **Independent code:** Not yet published.

## Learning trajectory

Foundations → qubit-based and optical computing → adiabatic optimization → Qiskit circuits → quantum algorithms → hybrid variational methods.

## Lectures and learning objectives

### 01 — Quantum foundations
**Covered:** Linear algebra, quantum states, Dirac notation, unitary/Hermitian operators, measurement, Hamiltonians and time evolution. Introduced discrete-variable, continuous-variable, gate-based, measurement-based and adiabatic computation.
**Objective:** Understand the state–operation–measurement model and the main approaches to quantum computing.

### 02 — Qubits and quantum gates
**Covered:** Bloch sphere, tensor products, entanglement, Pauli rotations, spin dynamics, CNOT, CZ and SWAP. Circuit and Bell-state examples.
**Objective:** Connect physical qubit evolution to elementary quantum circuits.

### 03 — Continuous-variable computing
**Covered:** Optical modes, quadratures, Fock/coherent/squeezed states, phase-space representations, Gaussian operations and boson sampling.
**Objective:** Distinguish photonic continuous-variable computation from qubit-based models.

### 04 — Adiabatic optimization
**Covered:** Hamiltonian interpolation, spectral gaps, quantum annealing, Max-Cut, Ising/QUBO encoding, traveling-salesperson constraints and hardware limitations.
**Objective:** Understand how discrete optimization problems can be expressed as Hamiltonian energy minimization.

### 05 — Qiskit programming
**Covered:** Building circuits, standard gates, GHZ-state preparation, simulation, transpilation, measurement shots and the introduction to Bernstein–Vazirani.
**Objective:** Follow a complete quantum-circuit simulation workflow.

### 06 — Oracle-based quantum algorithms
**Covered:** Bernstein–Vazirani, Boolean oracles, phase kickback, Simon's hidden XOR-period problem and GF(2) decoding.
**Class demonstration:** Qiskit Bernstein–Vazirani circuit and histogram. Simon implementation was a classroom assignment.
**Objective:** Explain how interference can expose hidden structure in an oracle.

### 07 — Simon recap and VQE
**Covered:** Simon oracle clarification, parameterized circuits, expectation values, classical optimization and the variational quantum eigensolver.
**Class material:** A small Qiskit VQE notebook; additional handout material on ansatz design and Pauli measurements.
**Objective:** Understand the hybrid quantum–classical optimization loop and its verification on small examples.

## Progress and next steps

The seven lectures above have been documented in private study notes. My systematic review and independent execution of the classroom examples are the next stage; I am **not** claiming personally verified implementations or experimental results yet.

Upcoming additions will be student-written code, correctness tests, and original experiments, each identified by its actual contribution and evidence.

The course outline also mentions PennyLane and D-Wave Ocean as later topics; they are **not** represented as completed implementations here.

*This is an independent learning portfolio, not an official course distribution. Original classroom notebooks, slides, recordings and private notes remain private.*
