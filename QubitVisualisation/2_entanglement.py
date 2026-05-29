import marimo

__generated_with = "0.23.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import cmath
    import marimo as mo
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    from qutip import Bloch, about, basis, mesolve, sigmam, sigmax, sigmay, sigmaz,Qobj, tensor, entropy_vn
    import matplotlib.figure



    return Bloch, basis, entropy_vn, mo, np, tensor


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # **Entangled Qubit System**

    When qubits are entangled, their individual states cannot be described independently. If we observe only one qubit in an entangled pair—ignoring the other—the quantum information shared between them is lost to the local observer. This "lost" information manifests as noise or classical uncertainty, reducing the single qubit to a mixed state. Visually, this means the state vector loses its purity and shrinks into the interior of the Bloch sphere.

    ### Example 1

    Let's explore this behavior using a parameterized two-qubit state:

    $$\Large \ket{\psi} = \cos(\frac{\theta}{2})\ket{00} + \sin(\frac{\theta}{2})e^{i\phi}\ket{11}$$

    Use the sliders below to adjust $\theta$ and $\phi$. Notice how changing the parameters of the full two-qubit system affects the reduced state of the single qubit, altering its position and length inside the Bloch sphere.
    """)
    return


@app.cell
def _(Bloch, basis, entropy_vn, mo, np, tensor):
    def example_1(theta_val, phi_val):
        # Define |00> and |11>
        state_00 = tensor(basis(2, 0), basis(2, 0))
        state_11 = tensor(basis(2, 1), basis(2, 1))
    
        amp_00 = np.cos(theta_val/2)
        amp_11 = np.sin(theta_val/2) * np.exp(1j * phi_val)
    
        # Create the parameterized entangled state
        entangled_q = amp_00 * state_00 + amp_11 * state_11
    
        # Extract state of only one qubit
        qubit_0 = entangled_q.ptrace(0)
    
        # Calculate entanglement entropy (base 2 for bits)
        entropy_a = entropy_vn(qubit_0, base=2)
    
        # Visualise quantum state on the Bloch sphere
        sphere_init = Bloch()
        sphere_init.add_states([qubit_0])
        sphere_init.render()
        bloch_sphere_a = sphere_init.fig 
        # Split into two separate elements
        equation_a = mo.md(rf"$$ \huge \ket{{\psi}} = {amp_00:.2f}\ket{{00}} + {amp_11:.2f}\ket{{11}} $$")
        entropy_a_text = mo.md(f"### **Entanglement Entropy:** {entropy_a:.3f} bits")
    
        # Stack the equation and text vertically, centered
        right_side_a = mo.vstack([equation_a, entropy_a_text], align="center")
        return [bloch_sphere_a, right_side_a]

    return (example_1,)


@app.cell
def _(mo, np):
    theta = mo.ui.slider(start=0.0, stop=2*np.pi, label="θ", value=np.pi/2, step=0.001)
    phi = mo.ui.slider(start=0.0, stop=2*np.pi, label="ϕ", value=0, step=0.001)
    return phi, theta


@app.cell
def _(mo, phi, theta):
    mo.md("sa")
    mo.output.append(mo.hstack([theta, mo.md(f"Has value: {theta.value}")]))
    mo.output.append(mo.hstack([phi, mo.md(f"Has value: {phi.value}")]))
    return


@app.cell
def _(example_1, mo, phi, theta):
    # Place the Bloch sphere and the stacked text side-by-side
    visual_1 = example_1(theta.value,phi.value)
    mo.hstack(visual_1, justify="space-around", align="center")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Example 2

    Now let's examine a superposition involving three basis states, controlled by a single parameter $\theta$:

    $$\Large \ket{\psi} = \cos{\theta} \ket{00} + \frac{\sin{\theta}}{\sqrt{2}} \ket{01} + \frac{\sin{\theta}}{\sqrt{2}}\ket{10}$$

    Use the slider below to adjust $\theta$. Observe how changing this parameter shifts the balance of the full system and affects the purity and position of the single reduced qubit on the Bloch sphere.
    """)
    return


@app.cell
def _(Bloch, basis, entropy_vn, mo, np, tensor):
    def example_2(theta_val):
        # 1. Define the three basis states
        state_b_00 = tensor(basis(2, 0), basis(2, 0))
        state_b_01 = tensor(basis(2, 0), basis(2, 1))
        state_b_10 = tensor(basis(2, 1), basis(2, 0))
    
        # 2. Calculate the coefficients (ensure it stays normalized)
        c_00 = np.cos(theta_val)
        c_01 = np.sin(theta_val) / np.sqrt(2)
        c_10 = np.sin(theta_val) / np.sqrt(2)
    
        # 3. Combine them into one state
        entangled_q3 = c_00 * state_b_00 + c_01 * state_b_01 + c_10 * state_b_10
    
        # Extract state of only one qubit and calculate the entropy
        qubit_b_0 = entangled_q3.ptrace(0)
        entropy_b = entropy_vn(qubit_b_0, base=2)
    
        # Visualise quantum state on the Bloch sphere
        sphere_b_init = Bloch()
        sphere_b_init.add_states([qubit_b_0])
        sphere_b_init.render()
        bloch_sphere_b = sphere_b_init.fig
        # Split into two separate elements
        equation_b = mo.md(rf"$$ \huge \ket{{\psi}} = {c_00:.2f}\ket{{00}} + {c_01:.2f}\ket{{01}} + {c_10:.2f}\ket{{10}} $$")
        entropy_b_text = mo.md(f"### **Entanglement Entropy:** {entropy_b:.3f} bits")
    
        # Stack them vertically next to Bloch sphere
        right_side_b = mo.vstack([equation_b, entropy_b_text], align="center")
        return [bloch_sphere_b, right_side_b]

    return (example_2,)


@app.cell
def _(mo, np):
    theta_b = mo.ui.slider(start=0.0, stop=2*np.pi, label="θ", value=np.pi/2, step=0.001)
    return (theta_b,)


@app.cell
def _(mo, theta_b):
    mo.output.append(mo.hstack([theta_b, mo.md(f"Has value: {theta_b.value}")]))
    return


@app.cell
def _(example_2, mo, theta_b):
    visual_2 = example_2(theta_b.value)
    mo.hstack(visual_2, justify="space-around", align="center")
    return


if __name__ == "__main__":
    app.run()
