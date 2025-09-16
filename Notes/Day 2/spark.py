from qiskit import QuantumCircuit, transpile
from iqm.qiskit_iqm import IQMProvider
import os

os.environ["IQM_TOKENS_FILE"] = r"/home/xederro/.cache/iqm-client-cli/tokens.json"

IQM_URL = "https://odra5.e-science.pl/station"  # ← wstaw URL, który dostałaś
provider = IQMProvider(IQM_URL)
backend = provider.get_backend()
qc = QuantumCircuit(3)
qc.h(0); qc.cx(0, 1); qc.cx(0, 2); qc.measure_all()
tqc = transpile(qc, backend=backend)
job = backend.run(tqc, shots=1000)
print("Job ID:", job.job_id())
result = job.result()
print(result.get_counts())

