import marimo

__generated_with = "0.20.4"
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



    return Bloch, Qobj, mo, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Single Qubit System**

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
    sphere = Bloch()
    q = Qobj([[np.cos(theta.value/2)], [np.sin(theta.value/2)*np.exp(complex(0,phi.value))]])
    sphere.add_states([q])
    sphere.render()
    sphere.fig
    return


if __name__ == "__main__":
    app.run()
