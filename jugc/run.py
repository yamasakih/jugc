from subprocess import Popen
from subprocess import STDOUT
import tempfile

n_cpus: int = 4
with tempfile.TemporaryDirectory() as temp_dir:
    command = [
        'jug', 'execute', 'subprocess.py', '--will-cite', '--verbose=INFO',
        '--jugdir', temp_dir
    ]
    for _ in range(n_cpus):
        Popen(command, stderr=STDOUT)
