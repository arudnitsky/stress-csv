#!/opt/homebrew/bin/python3
import sys
import csv
from ukrainian_word_stress import Stressifier, StressSymbol

if __name__ == "__main__":
    stressify = Stressifier(stress_symbol=StressSymbol.CombiningAcuteAccent)

    if len(sys.argv) != 1:
        inf = open(sys.argv[1])
    else:
        inf = sys.stdin

    csvreader = list(csv.reader(inf, delimiter=","))
    for row in csvreader:
        if row[0][0] != "#":
            print(stressify(row[0]), end="")
            fieldCount = len(row) - 1
            for index in range(0, len(row) - 1):
                print("," + row[index + 1], end="")
            print()

    if inf is not sys.stdin:
        inf.close()
