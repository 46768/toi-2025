import os
import sys
import subprocess

makeTemplate = '''sol : main.cpp
\tg++ -o sol main.cpp

.PHONY: run
run : sol
\t./sol
'''

mainfile = '''#include <iostream>

void solve() {
}

int main() {
\tint t;
\tstd::cin >> t;
\twhile(t--)solve();
}
'''

altfile = '''#include <iostream>

void solve() {
}

int main() {
\tsolve();
}
'''

if len(sys.argv) < 2:
    print("Usage: python util.py [NAME] (TYPE)")
    exit(1)
pname = sys.argv[1]

if len(sys.argv) == 3 and sys.argv[2] == 'run':
    subprocess.run(['make', 'run', '-C', f'./solutions/{pname}'])
    exit(0)

if os.path.exists(f'./solutions/{pname}/'):
    print(f"Problem {pname} exists, skipping")
    exit(1)


os.mkdir(f'./solutions/{pname}/')
mainF = open(f'./solutions/{pname}/main.cpp', 'w')
makeF = open(f'./solutions/{pname}/Makefile', 'w')
if len(sys.argv) == 2:
    mainF.write(mainfile)
elif len(sys.argv) == 3 and sys.argv[2] == 'alt':
    mainF.write(altfile)
makeF.write(makeTemplate.format(oname=pname))
