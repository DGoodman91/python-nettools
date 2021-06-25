import subprocess

cmd = "ping -c1 127.0.0."

for x in range (0,255):
    p = subprocess.Popen(cmd+str(x), shell=True, stderr=subprocess.PIPE)

    while True:
        out = p.stderr.read(1)
        if out == '' and p.poll() != None:
            break
        if out != '':
            p.stdout.write(out)
            p.stdout.flush()