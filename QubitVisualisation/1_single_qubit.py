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
    from qutip import Bloch, about, basis, mesolve, sigmam, sigmax, sigmay, sigmaz,Qobj
    import matplotlib.figure



    return Bloch, Qobj, mesolve, mo, np, sigmax, sigmay, sigmaz


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #**Single Qubit System**

    State of the one-qubit system can be represented in form of the equation using only two degrees of freedom $\theta$ and $\phi$:

    $$ \ket q = \mathrm{cos} ( \frac{\theta}{2})\ket 0 + \mathrm{sin}(\frac{\theta}{2}) e^{i\phi}\ket 1  $$

    In the below cells you can use sliders to try different values of $\theta$ and $\phi$. Check how the visualisation of the state changes on the Bloch sphere.
    """)
    return


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
def _(Bloch, Qobj, np, phi, theta):
    # Prepare quantum state
    q = Qobj([[np.cos(theta.value/2)], [np.sin(theta.value/2)*np.exp(complex(0,phi.value))]])

    # Visualise quantum state on the Bloch sphere
    sphere_init = Bloch()
    sphere_init.add_states([q])
    sphere_init.render()
    sphere_init.fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##**Qubit Dynamics: Decoherence**

    This notebook simulates the time evolution of a single qubit driven by a continuous-wave pulse using **QuTiP**. It demonstrates how to precisely control the number of qubit flips and compares an ideal, noiseless system with a realistic, noisy environment.

    ###**Overview**
    The simulation uses a driven Hamiltonian $H = \frac{\Delta}{2} \sigma_x$ to induce continuous rotations (Rabi oscillations) between the $|0\rangle$ and $|1\rangle$ states. By strictly defining the simulation duration as $t = \frac{n\pi}{\Delta}$, we can execute exactly $n$ qubit flips ( $\pi$-pulses).

    The results of both the ideal and noisy simulations are visualized side-by-side on Bloch spheres using Marimo's layout tools.

    ###**Features**
    * **Precise Control:** Parameterized execution to perform exactly $n$ flips.
    * **Decoherence Modeling:** Simulates energy relaxation using a $\sigma_z$ collapse operator.
    * **Comparative Analysis:** Runs both clean (ideal) and noisy simulations simultaneously.
    * **3D Visualization:** Renders side-by-side Bloch spheres to compare the expectation values of the Pauli operators ($\sigma_x, \sigma_y, \sigma_z$).
    """)
    return


@app.cell
def _(Bloch, mesolve, np, sigmax, sigmay, sigmaz):
    def solve_evolution(n_executions, g, initial_state):
        delta = 2 * np.pi
        H = delta / 2.0 * sigmax()
        t_end = (n_executions * np.pi) / delta
        tlist = np.linspace(0, t_end, 100)
        expect_ops = [sigmax(), sigmay(), sigmaz()]
        c_ops_noisy = [np.sqrt(g) * sigmaz()]
        result_noisy = mesolve(H, initial_state, tlist, c_ops_noisy, e_ops=expect_ops)
        return result_noisy

    # --- Shared Plotting Function ---
    def plot_dynamics(result_obj, initial_state):
        # Extract and convert expectation values
        exp_sx, exp_sy, exp_sz = [np.array(e) for e in result_obj.expect]

        # Create Bloch sphere plot
        sphere = Bloch()
        sphere.add_points([exp_sx, exp_sy, exp_sz], meth="l")
        sphere.add_states(initial_state)
        sphere.render()
        return sphere.fig

    return plot_dynamics, solve_evolution


@app.cell
def _(mo, np):
    # Define sliders
    n_executions = mo.ui.slider(start=0, stop=100, label="number of SigmaX gate executions", value=1, step=1)
    g = mo.ui.slider(start=0, stop=1, label="g noise level", value=0.25, step=0.01)
    theta_b = mo.ui.slider(start=0.0, stop=2*np.pi, label="θ", value=np.pi/2, step=0.001)
    phi_b = mo.ui.slider(start=0.0, stop=2*np.pi, label="ϕ", value=0, step=0.001)

    return g, n_executions, phi_b, theta_b


@app.cell
def _(g, mo, n_executions, phi_b, theta_b):

    mo.output.append(mo.hstack([theta_b, mo.md(f"Has value: {theta_b.value}")]))
    mo.output.append(mo.hstack([phi_b, mo.md(f"Has value: {phi_b.value}")]))
    mo.output.append(mo.hstack([g, mo.md(f"Has value: {g.value}")]))
    mo.output.append(mo.hstack([n_executions, mo.md(f"Has value: {n_executions.value}")]))
    return


@app.cell
def _(
    Qobj,
    g,
    mo,
    n_executions,
    np,
    phi_b,
    plot_dynamics,
    solve_evolution,
    theta_b,
):
    psi = Qobj([[np.cos(theta_b.value/2)], [np.sin(theta_b.value/2)*np.exp(complex(0,phi_b.value))]])
    result_noisya = solve_evolution(n_executions.value, g.value, psi)
    result_clean = solve_evolution(n_executions.value, 0, psi)

    # --- 1. Noisy Version ---
    fig_noisy = plot_dynamics(result_noisya, psi)

    # --- 2. Clean Version (No Noise) ---
    fig_clean = plot_dynamics(result_clean, psi)

    mo.hstack([fig_noisy, fig_clean], justify="space-around")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
