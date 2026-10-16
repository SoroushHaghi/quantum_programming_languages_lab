"""Lecture 07: minimal VQE-style parameter optimization, rebuilt as a study example.

New AI-assisted illustrative implementation, not the instructor notebook.
This uses exact statevector expectations rather than finite-shot estimates;
it does not demonstrate a physical quantum-hardware advantage.
Requires qiskit, numpy and scipy.
"""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp, Statevector
from scipy.optimize import minimize


def main() -> None:
    # A one-qubit classroom Hamiltonian: H = 2 X - Z.
    hamiltonian = SparsePauliOp.from_list([("X", 2.0), ("Z", -1.0)])

    def expectation(parameters: np.ndarray) -> float:
        circuit = QuantumCircuit(1)
        circuit.ry(float(parameters[0]), 0)
        state = Statevector.from_instruction(circuit)
        return float(np.real(state.expectation_value(hamiltonian)))

    optimum = minimize(
        expectation,
        x0=np.array([0.0]),
        method="COBYLA",
        options={"maxiter": 500, "tol": 1e-10},
    )

    # Independent mathematical reference, using the 2x2 matrix.
    exact_matrix = np.array([[-1.0, 2.0], [2.0, 1.0]])
    exact_ground_energy = float(np.linalg.eigvalsh(exact_matrix)[0])

    assert abs(optimum.fun - exact_ground_energy) < 1e-5
    print("Estimated minimum energy:", round(float(optimum.fun), 8))
    print("Exact ground energy:    ", round(exact_ground_energy, 8))
    print("Expected:               ", round(-np.sqrt(5.0), 8))


if __name__ == "__main__":
    main()
