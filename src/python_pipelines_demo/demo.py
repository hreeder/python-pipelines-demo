def decorate_christmas_tree(color: str = "Red"):
    """Decorates the christmas tree

    Args:
      color: What color tinsel to use
    """

    return f"Tree has {color} tinsel"


def add_baubles(count):
    """Add some baubles."""
    return ["bauble" for _ in range(count)]
