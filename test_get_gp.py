# -*- coding: utf-8 -*-
import pytest
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_get_gp(app):
    app.login(username="admin", password="L0giK@17")
    app.open_gov_programs_page()
    app.select_version_gp()
    app.select_root_structural_element()
