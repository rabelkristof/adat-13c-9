"""Automatikus tesztek a Feladatkártya #2-höz. A CI lefuttatja a notebookot, és a mentett tiszta adatot ellenőrzi."""
import re
from pathlib import Path

import nbformat
import pandas as pd
import pytest
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

ROOT = Path(__file__).resolve().parent.parent
NOTEBOOK = ROOT / "adattisztitas.ipynb"
TISZTA = ROOT / "data" / "hivasok_tiszta.csv"

VART_SOROK = 214
VART_ATLAG = 688.6


@pytest.fixture(scope="session")
def tiszta():
    assert NOTEBOOK.exists(), "Hiányzik az adattisztitas.ipynb (a Colabból ugyanezen a néven mentsd vissza)."
    nb = nbformat.read(NOTEBOOK, as_version=4)
    try:
        NotebookClient(nb, timeout=180, kernel_name="python3",
                       resources={"metadata": {"path": str(ROOT)}}).execute()
    except CellExecutionError as e:
        utolso = re.sub(r"\x1b\[[0-9;]*m", "", str(e)).strip().splitlines()[-1]
        pytest.fail(f"A notebook hibával állt le: {utolso}", pytrace=False)
    assert TISZTA.exists(), "A notebook nem mentette el a data/hivasok_tiszta.csv fájlt."
    return pd.read_csv(TISZTA)


def test_nincs_duplikalt_sor(tiszta):
    assert not tiszta.duplicated().any()
    assert tiszta["hivas_id"].is_unique


def test_egyseges_modellnevek(tiszta):
    assert set(tiszta["modell"]) == {"kisebb", "nagyobb"}


def test_sikeres_nulla_vagy_egy(tiszta):
    assert set(tiszta["sikeres"]) <= {0, 1}


def test_valaszido_tartomanyban_es_teljes(tiszta):
    assert tiszta["valaszido_ms"].notna().all()
    assert tiszta["valaszido_ms"].between(50, 10_000).all()


def test_normalizalas(tiszta):
    assert tiszta["valaszido_norm"].min() == pytest.approx(0)
    assert tiszta["valaszido_norm"].max() == pytest.approx(1)


def test_sorok_szama_es_atlag(tiszta):
    assert len(tiszta) == VART_SOROK, f"{len(tiszta)} sor maradt, {VART_SOROK} kellene: nézd át a lépések sorrendjét."
    assert tiszta["valaszido_ms"].mean() == pytest.approx(VART_ATLAG, abs=0.1)
