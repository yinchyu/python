import os, time

read_path = "/tmp/pipe.in"
write_path = "/tmp/pipe.out"

if os.path.exists(read_path):
    os.remove(read_path)
if os.path.exists(write_path):
    os.remove(write_path)

os.mkfifo(write_path)
os.mkfifo(read_path)

rf = os.open(read_path, os.O_RDONLY)
wf = os.open(write_path, os.O_SYNC | os.O_CREAT | os.O_RDWR)

while True:
    s = os.read(rf, 1024)
    print "received msg: %s" % s
    if len(s) == 0:
        time.sleep(1)
        continue

    if "exit" in s:
        break

    os.write(wf, s)

os.close(rf)
os.close(wf)
