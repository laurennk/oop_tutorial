# import mdtraj as md
# import MDAnalysis as mda
# import numpy as np
import sys

from factory import trajectory_factory
from adapter import *
from traj_adapter import TrajectoryAdapter

toolkit = sys.argv[1]

"""
2. This works for the adapter but could be simplified
"""
# if toolkit == "MDTraj":
#     """
#     1. If this was just a script for me to use this might work
#     """
#     # print("mdtraj:")
#     #
#     # trajectory = md.load_pdb("protein.pdb")
#     #
#     # print(10*md.compute_center_of_mass(trajectory))
#     # print(10*md.compute_rg(trajectory))
#
#     traj_analysis = MDTrajAdapter("protein.pdb")
#
#     print(traj_analysis.compute_center_of_mass())
#     print(traj_analysis.compute_radius_of_gyration())
#
#
#
# elif toolkit == "MDAnalysis":
#     """
#     1. If this was just a script for me to use this might work
#     """
#     # print("\nMDAnalysis:")
#     #
#     # universe = mda.Universe("protein.pdb")
#     #
#     # mass_by_frame = np.ndarray(shape=(len(universe.trajectory), 3))
#     # rg_by_frame = np.empty(len(universe.trajectory))
#     #
#     # for ts in universe.trajectory:
#     #     mass_by_frame[ts.frame] = universe.atoms.center_of_mass(compound="segments")
#     #     rg_by_frame[ts.frame] = universe.atoms.radius_of_gyration()
#     #
#     # print(mass_by_frame)
#     # print(rg_by_frame)
#
#
#
#     traj_analysis = MDAnalysisAdapter("protein.pdb")
#
#     print(traj_analysis.compute_center_of_mass())
#     print(traj_analysis.compute_radius_of_gyration())
#
# else:
#     print("Toolkit not available")

"""
3. This is how adapters can be used directly,
but this could also be simplified using a factory
"""

# if toolkit == "MDTraj":
#     traj_analysis = MDTrajAdapter("protein.pdb")
#
# elif toolkit == "MDAnalysis":
#     traj_analysis = MDAnalysisAdapter("protein.pdb")
#
# else:
#     print("Toolkit not available")
#
# print(traj_analysis.compute_center_of_mass())
# print(traj_analysis.compute_radius_of_gyration())

"""
5. This is now using a factory
"""

traj_analysis = trajectory_factory(toolkit, filename="protein.pdb")

print(traj_analysis.compute_center_of_mass())
print(traj_analysis.compute_radius_of_gyration())
