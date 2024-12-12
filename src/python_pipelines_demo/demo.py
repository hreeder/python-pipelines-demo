import collections
import datetime
import os

import python_pipelines_demo


def decorate_christmas_tree(color: str):
    """Decorates the christmas tree

    Args:
      color: What color tinsel to use
    """

    os.chmod("/tmp/foobar", 0o666)
    return f"Tree has {color} tinsel"
