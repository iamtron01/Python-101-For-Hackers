import sys

print(sys.platform)

for line in sys.stdin:
    if line.strip() == 'exit':
        break
    sys.stdout.write(
        'You entered: ' + line)
    
import time

for i in range(0, 51):
    time.sleep(0.1)
    sys.stdout.write("{} [{}{}]\r"
        .format(i, '#'*i, "."*(50-i)))
    sys.stdout.flush()
sys.stdout.write("\n")

print(sys.path)
print(sys.modules)