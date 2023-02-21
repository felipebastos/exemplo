""" Testa o módulo app.

Digamos que trabalhamos com TDD.
"""

from ambiente.app import exemplo


def test_if_app_passes():
    """Testa se app passa nos critérios.

    Um teste como esse documenta o próprio projeto.
    """
    assert exemplo(2, 3) == 5
