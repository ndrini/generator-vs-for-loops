#!/bin/python3
import pytest
from t3 import ping_pong


@pytest.mark.parametrize('s,r',
                         [(3,
                           [1, 2, 'Ping']
                           ),
                          (15,
                          [1, 2, 'Ping', 4, 'Pong', 'Ping',
                           7, 8, 'Ping', 'Pong', 11, 'Ping',
                           13, 14, 'PingPong', ])],
                         )
def test_ping_pong(s, r):
    assert ping_pong(s) == r
