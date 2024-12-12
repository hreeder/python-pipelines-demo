import python_pipelines_demo.demo


def test_christmas_tree_has_tinsel():
    assert "red tinsel" in demo.decorate_christmas_tree("red")
