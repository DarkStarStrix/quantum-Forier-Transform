# code a quantum forier transform and inverse quantum fourier transform in qiskit

# import statements
from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


# define the quantum fourier transform class
def plot(counts):
    plot_histogram(counts).show()


class QFT:
    def __init__(self, n):
        self.n = n
        self.circuit = QuantumCircuit(self.n, self.n)
        self.circuit.h(range(self.n))

    def qft(self):
        for i in range(self.n):
            for j in range(i):
                self.circuit
            self.circuit.h(i)

    def inverse_qft(self):
        for i in range(self.n):
            self.circuit.h(i)
            for j in range(i):
                self.circuit

    def measure(self):
        self.circuit.measure(range(self.n), range(self.n))

    def run(self):
        backend = Aer.get_backend('qasm_simulator')
        job = execute(self.circuit, backend, shots=1000)
        result = job.result()
        counts = result.get_counts()
        return counts

    def run_and_plot(self):
        counts = self.run()
        plots(counts)


# define the inverse quantum fourier transform class
def plots(counts):
    plot_histogram(counts).show()


class IQFT:
    def __init__(self, n):
        self.n = n
        self.circuit = QuantumCircuit(self.n, self.n)
        self.circuit.h(range(self.n))

    def inverse_qft(self):
        for i in range(self.n):
            self.circuit.h(i)
            for j in range(i):
                self.circuit

    def measure(self):
        self.circuit.measure(range(self.n), range(self.n))

    def run(self):
        backend = Aer.get_backend('qasm_simulator')
        job = execute(self.circuit, backend, shots=1000)
        result = job.result()
        counts = result.get_counts()
        return counts

    def run_and_plot(self):
        counts = self.run()
        plots(counts)


# define the main function plot the fourier transform and inverse fourier transform
def main():
    n = 4
    qft = QFT(n)
    qft.qft()
    qft.measure()
    qft.run_and_plot()
    iqft = IQFT(n)
    iqft.inverse_qft()
    iqft.measure()
    iqft.run_and_plot()


# call the main function
main()
