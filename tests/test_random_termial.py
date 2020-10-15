#!/usr/bin/env python3
# termial-random
# Copyright(C) 2020 Fridolin Pokorny
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
# type: ignore

from hypothesis import given
from hypothesis.strategies import integers
import pytest
import termial_random


def test_seed():
    """Test setting seed."""
    termial_random.seed(10)
    assert termial_random.random(42) == 7


def test_seed_init():
    """Test initializing seed."""
    termial_random.seed_init()
    assert termial_random.random(42) > 0


def test_type_error():
    """Test passing bad integer."""
    with pytest.raises(TypeError):
        termial_random.random("some-string-goes-here")


@given(integers(min_value=1, max_value=1024),)
def test_random_termial(n: int) -> None:
    """Compute random termial function value."""
    x = termial_random.random(n)
    assert 0 <= x < n


@pytest.mark.skip(reason="This is not implemented")
@given(integers(min_value=-1024, max_value=-1),)
def test_random_termial_negative_error(n: int) -> None:
    """Test error out when random termial is used wih negative or zero value."""
    # with pytest.raises(ValueError):
    #     termial_random.random(n)
