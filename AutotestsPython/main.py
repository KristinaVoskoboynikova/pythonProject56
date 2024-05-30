def name(a):
    name = a
    l = len(name)
    if l == 4:
        return "YES"
    else:
        return "NO"

a = "bing"
print(name(a))
def test_name0():
    a = "1234"
    assert name(a) == "YES"

def test_name1():
    a = "njiokm,"
    assert name(a) == "No"