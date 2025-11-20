import numpy as np
from scipy.optimize import minimize
from src.bem import bem_power

def objective(x, N, R, rho, Vbins, weights):
    chords = x[:N]
    twists = x[N:2*N]
    total = 0.0
    for V, w in zip(Vbins, weights):
        total += bem_power(chords, twists, R, rho, V) * w
    return -total

def run_baseline():
    N = 8
    chords = np.linspace(1.0, 0.2, N)
    twists = np.linspace(10.0, 0.0, N)
    print("Baseline chords:", chords)
    print("Baseline twists:", twists)

if __name__ == "__main__":
    run_baseline()
