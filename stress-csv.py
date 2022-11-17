import sys
import csv
from ukrainian_word_stress import Stressifier, StressSymbol


if __name__ == "__main__":
    stressify = Stressifier(stress_symbol=StressSymbol.CombiningAcuteAccent)
    with open(sys.argv[1], newline="") as csvfile:
        csvreader = list(csv.reader(csvfile, delimiter=","))
        for row in csvreader:
            print(stressify(row[0]) + "," + ",".join(row[1:]))
