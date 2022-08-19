from hello import hello 

def test_name():
    for name in ["harry","ron","peter"]:
        assert hello(f"{name}") == f"hello, {name}" # this is not returning anything so won't work test is bugged
                                     # modified code that return the f string containing hello is good.
def test_default():
    assert hello() == "hello, world"