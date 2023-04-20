import sys

digit = float(sys.argv[1].replace(',', '.'))
if digit < 0:
    print("Це від'ємне число")
elif digit == 0:
    print("Це нуль")
else:
    print("Це додатне число")