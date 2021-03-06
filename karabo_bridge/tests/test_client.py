from itertools import islice

import numpy as np
import pytest

from karabo_bridge import Client


def test_get_frame(sim_server):
    c = Client(sim_server)
    data, metadata = c.next()
    assert 'SPB_DET_AGIPD1M-1/DET/0CH0:xtdf' in data
    assert 'SPB_DET_AGIPD1M-1/DET/0CH0:xtdf' in metadata


def test_protocol_1(sim_server_version_1):
    c = Client(sim_server_version_1)
    data, metadata = c.next()
    assert 'SPB_DET_AGIPD1M-1/DET/0CH0:xtdf' in data
    assert 'SPB_DET_AGIPD1M-1/DET/0CH0:xtdf' in metadata
    assert all('metadata' in src for src in data.values())


def test_pull_socket(sim_server):
    with pytest.raises(NotImplementedError) as info:
        c = Client(sim_server, sock='PULL')


def test_pickle(sim_server_pickle):
    c = Client(sim_server_pickle, ser='pickle')
    data, metadata = c.next()
    assert isinstance(data, dict)
    assert isinstance(metadata, dict)
    image = data['SPB_DET_AGIPD1M-1/DET/0CH0:xtdf']['image.data']
    assert isinstance(image, np.ndarray)


def test_context_manager(sim_server):
    with Client(sim_server) as c:
        data, metadata = c.next()
    assert 'SPB_DET_AGIPD1M-1/DET/0CH0:xtdf' in data
    assert 'SPB_DET_AGIPD1M-1/DET/0CH0:xtdf' in metadata
    assert c._context.closed


def test_iterator(sim_server):
    c = Client(sim_server)
    for i, (data, metadata) in enumerate(islice(c, 3)):
        trainId = metadata['SPB_DET_AGIPD1M-1/DET/0CH0:xtdf']['timestamp.tid']
        assert trainId == 10000000000 + i
