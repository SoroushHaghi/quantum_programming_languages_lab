"""Lecture 05: illustrative Qiskit reconstruction of the GHZ classroom topic.

New AI-assisted example, not instructor source or verified student work.
Uses a local statevector sampler; no real quantum device is involved.
Requires qiskit with StatevectorSampler.
"""

from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler


def main() -> None:
    circuit = QuantumCircuit(3)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.cx(1, 2)

    measured = circuit.copy()
    measured.measure_all()

    shots = 1024
    sampler = StatevectorSampler(seed=7)
    result = sampler.run([measured], shots=shots).result()
    counts = result[0].data.meas.get_counts()

    # The ideal GHZ state yields only 000 and 111.
    assert sum(counts.values()) == shots
    assert set(counts) <= {"000", "111"}
    print("GHZ measurement counts:", counts)


if __name__ == "__main__":
    main()
