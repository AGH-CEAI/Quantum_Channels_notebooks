import marimo

__generated_with = "0.23.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pennylane as qml
    from qiskit_aer import AerSimulator
    from qiskit import QuantumCircuit, transpile
    import matplotlib.pyplot as plt

    from fake_vlq import FakeVLQ

    return AerSimulator, FakeVLQ, QuantumCircuit, plt, transpile


@app.cell
def _(FakeVLQ, QuantumCircuit, transpile):
    # 1. Initialize the backend (contains topology and native gates info)
    backend = FakeVLQ()

    # 2. Create a clean logical circuit (e.g., Bell state)
    # No need to worry about the resonator at this stage - just define pure logic
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1) # Gate between two logical qubits
    qc.measure_all()

    # 3. Transpile (Routing + Decomposition)
    # Qiskit automatically detects the lack of direct connection and routes
    # the signal through the resonator using a sequence of CZ gates and rotations.
    compiled_circuit = transpile(
        qc,
        backend=backend,
        optimization_level=3 # Level 3 optimally selects the best physical qubits
    )


    return backend, compiled_circuit, qc


@app.cell
def _(qc):
    print("Circuit before transpilation on FakeVLQ:")
    print(qc.draw(output='text'))
    print("\nLogical gates used:", qc.count_ops())
    return


@app.cell
def _(compiled_circuit):
    # 4. Visualize the result
    print("Circuit after transpilation on FakeVLQ:")
    print(compiled_circuit.draw(output='text'))

    # 5. Check the native gates used
    print("\nPhysical gates used:", compiled_circuit.count_ops())
    return


@app.cell
def _(AerSimulator, plt, qc):
    # 2. NOISELESS Simulation (Ideal math)
    ideal_sim = AerSimulator() 
    ideal_result = ideal_sim.run(qc, shots=1024).result()
    noiseless_counts = ideal_result.get_counts()

    # Define the exact order for the x-axis
    ordered_keys = ['00', '01', '10', '11']

    # Extract values in that order, defaulting to 0 if the key is missing
    ordered_noiseless_values = [noiseless_counts.get(key, 0) for key in ordered_keys]

    # Plot the bars
    plt.bar(ordered_keys, ordered_noiseless_values, color='g')

    # Label the axes and add a title
    plt.xlabel("Measured State")
    plt.ylabel("Number of Shots")
    plt.title("Ideal Circuit Distribution")

    plt.show()
    return (ordered_keys,)


@app.cell
def _(backend, compiled_circuit, ordered_keys, plt):
    # 3. NOISY Simulation (Uses FakeVLQ's T1/T2, gate errors, and readout errors)
    noisy_result = backend.run(compiled_circuit, shots=1024).result()
    noisy_counts = noisy_result.get_counts()
    plt.bar(noisy_counts.keys(), noisy_counts.values(), color='g')

    # Extract values in that order, defaulting to 0 if the key is missing
    ordered_noisy_values = [noisy_counts.get(key, 0) for key in ordered_keys]

    # Plot the bars
    plt.bar(ordered_keys, ordered_noisy_values, color='g')

    # Label the axes and add a title
    plt.xlabel("Measured State")
    plt.ylabel("Number of Shots")
    plt.title("Ideal Circuit Distribution")

    plt.show()
    return


if __name__ == "__main__":
    app.run()
