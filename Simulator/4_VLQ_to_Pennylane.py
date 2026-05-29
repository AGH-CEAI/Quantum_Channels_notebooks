import marimo

__generated_with = "0.23.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import pennylane as qml
    from qiskit import QuantumCircuit, transpile
    import numpy as np
    from fake_vlq import FakeVLQ

    # 1. Define the number of qubits and the device
    n_qubits = 4
    dev = qml.device("default.qubit", wires=n_qubits)

    # 3. Create the QNode
    @qml.qnode(dev)
    def circuit(inputs, weights):
        qml.AngleEmbedding(inputs, wires=range(n_qubits))
        qml.BasicEntanglerLayers(weights, wires=range(n_qubits))
        return qml.probs(wires=range(n_qubits))

    # 4. Prepare parameters
    # AngleEmbedding requires 1 input per qubit
    inputs = np.array([np.pi/4, np.pi/3, np.pi/2, np.pi/6]) 
    # BasicEntanglerLayers shape is (n_layers, n_qubits)
    weights = np.array([[0.1, -0.2, 0.5, np.pi/4]]) 

    # ==========================================
    # PENNYLANE EXECUTION
    # ==========================================
    pl_probs = circuit(inputs, weights)
    print("PennyLane Probs:", pl_probs)

    # ==========================================
    # CONVERT TO QISKIT
    # ==========================================
    # You must pass the parameters to to_openqasm so it can unroll the circuit
    qasm_string = qml.to_openqasm(circuit)(inputs, weights)

    # Load into Qiskit
    logical_circuit = QuantumCircuit.from_qasm_str(qasm_string)

    # Initialize the backend (contains topology and native gates info)
    backend = FakeVLQ()

    # Transpile (Routing + Decomposition)
    # Qiskit automatically detects the lack of direct connection and routes
    # the signal through the resonator using a sequence of CZ gates and rotations.
    transpiled_circuit = transpile(
        logical_circuit,
        backend=backend,
        optimization_level=3 # Level 3 optimally selects the best physical qubits
    )


    return logical_circuit, transpiled_circuit


@app.cell
def _(logical_circuit):
    print("\nQiskit Circuit:")
    print(logical_circuit.draw(output='text'))
    return


@app.cell
def _(transpiled_circuit):
    print("\nQiskit Circuit:")
    print(transpiled_circuit.draw(output='text', fold=-1))
    return


if __name__ == "__main__":
    app.run()
