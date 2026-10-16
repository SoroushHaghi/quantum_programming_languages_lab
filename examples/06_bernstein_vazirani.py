"""Lecture 06: independent illustrative Bernstein–Vazirani reconstruction.

New AI-assisted study code inspired by the algorithm discussed in class.
Not the instructor's notebook, and not verified student implementation.
Requires qiskit with StatevectorSampler.
"""

from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler


def main() -> None:
    secret = "1011"
    n = len(secret)
    ancilla = n
    circuit = QuantumCircuit(n + 1, n)

    # The ancilla is |-> after X followed by H.
    circuit.x(ancilla)
    circuit.h(range(n + 1))

    # Qiskit displays bit n-1 on the left; qubit 0 is the rightmost bit.
    for qubit, bit in enumerate(reversed(secret)):
        if bit == "1":
            circuit.cx(qubit, ancilla)

    circuit.h(range(n))
    circuit.measure(range(n), range(n))

    shots = 256
    sampler = StatevectorSampler(seed=7)
    result = sampler.run([circuit], shots=shots).result()
    counts = result[0].data.c.get_counts()

    assert counts == {secret: shots}
    print("Recovered BV string:", next(iter(counts)))
    print("Measurement counts:", counts)


if __name__ == "__main__":
    main()
