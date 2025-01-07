# # This is for skip
#
# import pytest
#
# @pytest.mark.skip # this will skip the test
# def test_demo1(reason = "not included"):
#     assert True
#
# def test_demo2():
#     assert True
#
#     ============================================

#This is marking skip

import pytest
import sys

@pytest.mark.windows1
def test_windows_1():
    assert True

@pytest.mark.windows2
def test_windows2():
    assert True

@pytest.mark.mac1
def test_mac1():
     assert True

@pytest.mark.mac2
def test_mac2():
     assert True

