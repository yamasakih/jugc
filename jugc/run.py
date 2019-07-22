import subprocess
import tempfile

n_cpus: int = 2
with tempfile.TemporaryDirectory() as temp_dir:
    command = ['jug', 'execute', '_jugc.py', '--jugdir', f'{temp_dir}']
    print(command)
    for _ in range(n_cpus):
        # subprocess.call(command)
        subprocess.Popen(command)
