import pytest

import run


@pytest.fixture()
def test_post():
    app = run.app
    return app.test_post
