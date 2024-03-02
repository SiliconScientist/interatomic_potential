from ase import units
from ase.md.langevin import Langevin
from ase.io import read, write
import numpy as np
import time
from mace.calculators import MACECalculator

calculator = MACECalculator(
    model_paths="/u/averyhill/Github/interatomic_potential/checkpoints/MACE_model_run-123.model",
    device="cuda",
)
init_conf = read(
    "/projects/bchg/averyhill/interatomic_potential/data/long_md/LatticeNew200/test_atoms200.xyz",
    "0",
)
init_conf.set_calculator(calculator)
dyn = Langevin(init_conf, 0.5 * units.fs, temperature_K=310, friction=5e-3)


def write_frame():
    dyn.atoms.write(
        "/projects/bchg/averyhill/interatomic_potential/data/md_latticeNew200.xyz",
        append=True,
    )


dyn.attach(write_frame, interval=50)
dyn.run(100)
print("MD finished!")
