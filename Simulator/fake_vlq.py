# March 17, 2026 calibration data from VLQ
#
# Copyright 2022-2025 Qiskit on IQM developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Fake backend for IQM's 24-qubit VLQ architecture."""

from __future__ import annotations

from iqm.iqm_client import StaticQuantumArchitecture
from iqm.qiskit_iqm.fake_backends.iqm_fake_backend import IQMErrorProfile, IQMFakeBackend


def FakeVLQ() -> IQMFakeBackend:
    """Return IQMFakeBackend instance representing IQM's VLQ architecture."""
    architecture = StaticQuantumArchitecture(
        dut_label="FakeVLQ",
        qubits=["QB1", "QB2", "QB3", "QB4", "QB5", "QB6", "QB7", "QB8", "QB9", "QB10", "QB11", "QB12", "QB13", "QB14", "QB15", "QB16", "QB17", "QB18", "QB19", "QB20", "QB21", "QB22", "QB23", "QB24"],
        computational_resonators=["CR1"],
        connectivity=[
            ("CR1", "QB1"),
            ("CR1", "QB2"),
            ("CR1", "QB3"),
            ("CR1", "QB4"),
            ("CR1", "QB5"),
            ("CR1", "QB6"),
            ("CR1", "QB7"),
            ("CR1", "QB8"),
            ("CR1", "QB9"),
            ("CR1", "QB10"),
            ("CR1", "QB11"),
            ("CR1", "QB12"),
            ("CR1", "QB13"),
            ("CR1", "QB14"),
            ("CR1", "QB15"),
            ("CR1", "QB16"),
            ("CR1", "QB17"),
            ("CR1", "QB18"),
            ("CR1", "QB19"),
            ("CR1", "QB20"),
            ("CR1", "QB21"),
            ("CR1", "QB22"),
            ("CR1", "QB23"),
            ("CR1", "QB24"),
        ],
    )
    error_profile = IQMErrorProfile(
        t1s={
            "CR1": 29814.7,
            "QB1": 56045.2,
            "QB2": 28729.9,
            "QB3": 14851.5,
            "QB4": 46265.7,
            "QB5": 57696.6,
            "QB6": 40583.2,
            "QB7": 29192.0,
            "QB8": 38211.8,
            "QB9": 46878.0,
            "QB10": 13875.1,
            "QB11": 51104.7,
            "QB12": 38616.3,
            "QB13": 26429.5,
            "QB14": 40202.9,
            "QB15": 24569.9,
            "QB16": 33320.0,
            "QB17": 44884.3,
            "QB18": 23783.5,
            "QB19": 37904.1,
            "QB20": 43738.6,
            "QB21": 32227.6,
            "QB22": 41627.0,
            "QB23": 30612.1,
            "QB24": 32437.0,            
        },
        t2s={
            "CR1": 29814.7,
            "QB1": 11239.2,
            "QB2": 15242.3,
            "QB3": 6077.3,
            "QB4": 11035.0,
            "QB5": 14255.0,
            "QB6": 12630.0,
            "QB7": 13889.0,
            "QB8": 9170.8,
            "QB9":  9473.1,
            "QB10": 10501.1,
            "QB11": 10618.5,
            "QB12": 13293.6,
            "QB13": 6709.4,
            "QB14": 12630.0,
            "QB15": 12633.8,
            "QB16": 13851.6,
            "QB17": 14455.5,
            "QB18": 9903.4,
            "QB19": 10948.8,
            "QB20": 17564.0,
            "QB21": 13208.1,
            "QB22": 15476.7,
            "QB23": 17537.6,
            "QB24": 12227.4,
        },
        single_qubit_gate_depolarizing_error_parameters={
            "prx": {
                "QB1": 0.01004,
                "QB2": 0.01586,
                "QB3": 0.00121,
                "QB4": 0.00218,
                "QB5": 0.00172,
                "QB6": 0.00232,
                "QB7": 0.00096,
                "QB8": 0.00222,
                "QB9": 0.00098,
                "QB10": 0.00121,
                "QB11": 0.00102,
                "QB12": 0.00157,
                "QB13": 0.0011,
                "QB14": 0.03532,
                "QB15": 0.00085,
                "QB16": 0.00128,
                "QB17": 0.00124,
                "QB18": 0.00058,
                "QB19": 0.00125,
                "QB20": 0.00058,
                "QB21": 0.0013,
                "QB22": 0.0008,
                "QB23": 0.00192,
                "QB24": 0.0027,
            }
        },
        two_qubit_gate_depolarizing_error_parameters={
            "cz": {
                ("QB1", "CR1"): 0.005743,
                ("QB2", "CR1"): 0.060690,
                ("QB3", "CR1"): 0.012595,
                ("QB4", "CR1"): 0.007504,
                ("QB5", "CR1"): 0.005700,
                ("QB6", "CR1"): 0.044717,
                ("QB7", "CR1"): 0.005157,
                ("QB8", "CR1"): 0.007602,
                ("QB9", "CR1"): 0.007248,
                ("QB10", "CR1"): 0.011908,
                ("QB11", "CR1"): 0.007327,
                ("QB12", "CR1"): 0.005934,
                ("QB13", "CR1"): 0.005665,
                ("QB14", "CR1"): 0.111660,
                ("QB15", "CR1"): 0.004772,
                ("QB16", "CR1"): 0.021655,
                ("QB17", "CR1"): 0.006845,
                ("QB18", "CR1"): 0.026027,
                ("QB19", "CR1"): 0.005808,
                ("QB20", "CR1"): 0.358012,
                ("QB21", "CR1"): 0.015436,
                ("QB22", "CR1"): 0.006003,
                ("QB23", "CR1"): 0.004907,
                ("QB24", "CR1"): 0.006182,
            },
            "move": {
                ("QB1", "CR1"): 0.000659,
                ("QB2", "CR1"): 0.001453,
                ("QB3", "CR1"): 0.020023,
                ("QB4", "CR1"): 0.001523,
                ("QB5", "CR1"): 0.001287,
                ("QB6", "CR1"): 0.000998,
                ("QB7", "CR1"): 0.099595,
                ("QB8", "CR1"): 0.003081,
                ("QB9", "CR1"): 0.001481,
                ("QB10", "CR1"): 0.002812,
                ("QB11", "CR1"): 0.000970,
                ("QB12", "CR1"): 0.004332,
                ("QB13", "CR1"): 0.001165,
                ("QB14", "CR1"): 0.007962,
                ("QB15", "CR1"): 0.004231,
                ("QB16", "CR1"): 0.002013,
                ("QB17", "CR1"): 0.001451,
                ("QB18", "CR1"): 0.001123,
                ("QB19", "CR1"): 0.001912,
                ("QB20", "CR1"): 0.001385,
                ("QB21", "CR1"): 0.003157,
                ("QB22", "CR1"): 0.001503,
                ("QB23", "CR1"): 0.001453,
                ("QB24", "CR1"): 0.002493,
            },
        },
        single_qubit_gate_durations={"prx": 32.0},
        two_qubit_gate_durations={"cz": 88.0, "move": 64.0},
        readout_errors={
            "QB1": {"0": 0.016, "1": 0.0665},
            "QB2": {"0": 0.0305, "1": 0.058},
            "QB3": {"0": 0.0095, "1": 0.022},
            "QB4": {"0": 0.0255, "1": 0.0225},
            "QB5": {"0": 0.0285, "1": 0.037},
            "QB6": {"0": 0.0195, "1": 0.061},
            "QB7": {"0": 0.032, "1": 0.0275},
            "QB8": {"0": 0.041, "1": 0.038},
            "QB9": {"0": 0.043, "1": 0.0365},
            "QB10": {"0": 0.019, "1": 0.033},
            "QB11": {"0": 0.0095, "1": 0.0155},
            "QB12": {"0": 0.009, "1": 0.0135},
            "QB13": {"0": 0.0155, "1": 0.011},
            "QB14": {"0": 0.016, "1": 0.205},
            "QB15": {"0": 0.004, "1": 0.016},
            "QB16": {"0": 0.0225, "1": 0.024},
            "QB17": {"0": 0.0215, "1": 0.026},
            "QB18": {"0": 0.0165, "1": 0.019},
            "QB19": {"0": 0.0075, "1": 0.024},
            "QB20": {"0": 0.014, "1": 0.0205},
            "QB21": {"0": 0.0075, "1": 0.0195},
            "QB22": {"0": 0.0225, "1": 0.033},
            "QB23": {"0": 0.0055, "1": 0.0135},
            "QB24": {"0": 0.017, "1": 0.0255},
        },
        name="VLQ",
    )

    return IQMFakeBackend(architecture, error_profile, name="FakeVLQBackend")


# Qubits ranked by composite calibration score (lower = better). Sum of:
# prx depol + cz depol + move depol + avg readout + 30ns/T2 coherence weight.
# Computed from the March 17, 2026 calibration above. See docstring below.
_VLQ_QUBITS_BEST_FIRST = (
    "QB23", "QB15", "QB11", "QB12", "QB13", "QB19",
    "QB24", "QB17", "QB21", "QB4",  "QB22", "QB5",
    "QB10", "QB18", "QB16", "QB9",  "QB3",  "QB8",
    "QB1",  "QB6",  "QB2",  "QB7",  "QB14", "QB20",
)


def FakeVLQ_small(n_qubits: int = 12) -> IQMFakeBackend:
    """Return a smaller ``IQMFakeBackend`` built from the ``n_qubits`` best
    VLQ qubits plus the CR1 resonator.

    "Best" is the composite ranking stored in ``_VLQ_QUBITS_BEST_FIRST``
    (prx + cz + move depol errors, readout, and T2 coherence all weighted
    equally). The top of that list (QB23, QB15, QB11, ...) has the lowest
    combined noise across gate types.

    The returned backend reuses the VLQ calibration entries for the selected
    qubits unchanged -- it's a topological slice, not a re-fit. This makes it
    suitable as a drop-in for ``FakeVLQ()`` when density-matrix simulation
    requires ``qubits + resonators <= ~15`` (16 GB cap at the default
    ``exact_noisy_probabilities`` setting).

    Args:
        n_qubits: How many qubits to keep (1..24). Defaults to 12 -- the
            largest round number that stays under the 13-total-qubit cap
            (12 qubits + 1 CR1) comfortably below the 16 GB density-matrix
            memory threshold.

    Raises:
        ValueError: if ``n_qubits`` is outside ``[1, 24]``.
    """
    if not 1 <= n_qubits <= 24:
        raise ValueError(f"n_qubits must be in [1, 24], got {n_qubits}")

    full = FakeVLQ()
    full_arch = full._IQMFakeBackend__sqa  # type: ignore[attr-defined]
    full_profile = full._IQMFakeBackend__error_profile  # type: ignore[attr-defined]
    selected = list(_VLQ_QUBITS_BEST_FIRST[:n_qubits])

    architecture = StaticQuantumArchitecture(
        dut_label=f"FakeVLQ-small-{n_qubits}",
        qubits=selected,
        computational_resonators=list(full_arch.computational_resonators),
        connectivity=[("CR1", q) for q in selected],
    )

    keep_qb = set(selected) | set(full_arch.computational_resonators)
    error_profile = IQMErrorProfile(
        t1s={c: full_profile.t1s[c] for c in keep_qb},
        t2s={c: full_profile.t2s[c] for c in keep_qb},
        single_qubit_gate_depolarizing_error_parameters={
            "prx": {q: full_profile.single_qubit_gate_depolarizing_error_parameters["prx"][q]
                    for q in selected},
        },
        two_qubit_gate_depolarizing_error_parameters={
            "cz": {(q, "CR1"): full_profile.two_qubit_gate_depolarizing_error_parameters["cz"][(q, "CR1")]
                   for q in selected},
            "move": {(q, "CR1"): full_profile.two_qubit_gate_depolarizing_error_parameters["move"][(q, "CR1")]
                     for q in selected},
        },
        single_qubit_gate_durations=dict(full_profile.single_qubit_gate_durations),
        two_qubit_gate_durations=dict(full_profile.two_qubit_gate_durations),
        readout_errors={q: dict(full_profile.readout_errors[q]) for q in selected},
        name=f"VLQ-small-{n_qubits}",
    )

    return IQMFakeBackend(architecture, error_profile, name=f"FakeVLQ-small-{n_qubits}")
