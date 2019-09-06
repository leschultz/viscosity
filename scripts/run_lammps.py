'''
Use the installed version of lammps to run multiple simulations.
'''

import subprocess
import sys
import os

runpath = sys.argv[1]  # The path for all runs to be executed
program = sys.argv[2]  # The lammps binary
runname = sys.argv[3]  # The standard lammps input file name

# Count the available runs
runs = []
count = 0
for path, subdirs, files in os.walk(runpath):
    if runname not in files:
        continue

    runs.append(path)
    count += 1

countnew = 1
for path in runs:

    print('Running ('+str(countnew)+'/'+str(count)+'): '+path)

    subprocess.run(
                   program.split(' ')+['-in', runname],
                   cwd=path,
                   stdout=open(os.devnull, 'wb')
                   )

    countnew += 1
