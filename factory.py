#from adapter import MDTrajAdapter, MDAnalysisAdapter
from traj_adapter import TrajectoryAdapter

_toolkits = {}

def register(toolkit_name, toolkit_class):
        if not issubclass(toolkit_class, TrajectoryAdapter):
            raise TypeError("{0} is not a TrajectoryAdapter".format(toolkit_class))
        _toolkits[toolkit_name] = toolkit_class

def trajectory_factory(trajectory_toolkit, **kwargs):
    """
    4. This works, but we could use a dictionary instead
    """
    # if trajectory_toolkit == "MDTraj":
    #     traj_analysis = MDTrajAdapter(kwargs["filename"])
    #
    # elif trajectory_toolkit == "MDAnalysis":
    #     traj_analysis = MDAnalysisAdapter(kwargs["filename"])
    #
    # else:
    #      print("Toolkit not available")
    #
    # return traj_analysis

    """
    6. This works, but we could use a registry to keep track of the toolkits
    """

    # traj_toolkits = {"MDTraj": MDTrajAdapter, "MDAnalysis": MDAnalysisAdapter}
    #
    # if trajectory_toolkit not in traj_toolkits:
    #     raise TypeError("Toolkit not found...")
    #
    # cls = traj_toolkits[trajectory_toolkit]
    # traj_analysis = cls(kwargs["filename"])
    #
    # return traj_analysis

    """
    dkfsja
    """

    if trajectory_toolkit not in _toolkits.keys():
        raise TypeError("Toolkit not found...")

    traj_analysis = _toolkits[trajectory_toolkit](kwargs["filename"])

    return traj_analysis
