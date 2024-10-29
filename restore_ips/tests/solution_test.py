from solution import Solution


def test_example_1():
    s = "25525511135"
    res = Solution().restoreIpAddresses(s)
    expected = ["255.255.11.135", "255.255.111.35"]
    assert len(res) == len(expected)
    for c in ["255.255.11.135", "255.255.111.35"]:
        assert c in res


def test_example_2():
    s = "0000"
    res = Solution().restoreIpAddresses(s)
    expected = ["0.0.0.0"]
    assert len(res) == len(expected)
    for c in ["0.0.0.0"]:
        assert c in res


def test_example_3():
    s = "101023"
    res = Solution().restoreIpAddresses(s)
    expected = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
    assert len(res) == len(expected)
    for c in expected:
        assert c in res
