import qiskit
import bluequbit
from math import pi

bq_client = bluequbit.init("<token>")

qc_qiskit = qiskit.QuantumCircuit(4)

qc_qiskit.h(0)
qc_qiskit.x(1)
qc_qiskit.x(2)
qc_qiskit.h(3)
#qc_qiskit.x(0)
#qc_qiskit.x(3)
qc_qiskit.ry(0.8*pi,0)
qc_qiskit.ry(0.8*pi,1)
qc_qiskit.ry(0.8*pi,2)
qc_qiskit.ry(0.8*pi,3)


job_result = bq_client.run(qc_qiskit, job_name="solution1_2025")

# state_vector = job_result.get_statevector()
# print(state_vector)