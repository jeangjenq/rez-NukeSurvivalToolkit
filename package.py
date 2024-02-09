name = "nuke_st"
version = "231101"
authors = [
    "Tony Lyons",
    "Ben McEwan",
    "Adrian Pueyo"
]

description = \
    """
    The Nuke Survival Toolkit is a hand-picked selection of nuke gizmos
    collected from all over the web organized into 1 easy to install toolbar.    
    """

build_command = "python {root}/build.py"

requires = []

_category = "ext"

def commands():
    env.NUKE_PATH.append("{root}/NukeSurvivalToolkit")