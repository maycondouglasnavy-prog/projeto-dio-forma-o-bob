# tests/test_geo_explorer.py
# Test suite for the Geo-Explorer project.

import json
import os
import pytest


DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")


def load_trilhas():
    """Load the trilhas.json data file."""
    with open(os.path.join(DATA_DIR, "trilhas.json"), encoding="utf-8") as f:
        return json.load(f)


class TestTrilhasJSON:
    """Tests for the trilhas.json data file structure."""

    def test_json_is_valid(self):
        """trilhas.json must be parseable and not empty."""
        data = load_trilhas()
        assert data is not None

    def test_top_level_keys(self):
        """Root object must have 'trilhas' and 'metadata' keys."""
        data = load_trilhas()
        assert "trilhas" in data
        assert "metadata" in data

    def test_trilhas_count(self):
        """Must contain exactly 3 study trails."""
        data = load_trilhas()
        assert len(data["trilhas"]) == 3

    def test_trilha_required_fields(self):
        """Each trail must have id, tecnologia, descricao and niveis."""
        data = load_trilhas()
        for trilha in data["trilhas"]:
            assert "id" in trilha
            assert "tecnologia" in trilha
            assert "descricao" in trilha
            assert "niveis" in trilha

    def test_each_trilha_has_three_levels(self):
        """Each trail must have exactly 3 difficulty levels."""
        data = load_trilhas()
        expected_levels = {"Iniciante", "Intermediário", "Avançado"}
        for trilha in data["trilhas"]:
            level_names = {n["nivel"] for n in trilha["niveis"]}
            assert level_names == expected_levels, (
                f"Trail '{trilha['id']}' is missing levels: "
                f"{expected_levels - level_names}"
            )

    def test_each_nivel_has_modulos_and_desafio(self):
        """Each level must have modulos and desafio_pratico."""
        data = load_trilhas()
        for trilha in data["trilhas"]:
            for nivel in trilha["niveis"]:
                assert "modulos" in nivel, (
                    f"Level '{nivel['nivel']}' in '{trilha['id']}' missing 'modulos'"
                )
                assert "desafio_pratico" in nivel, (
                    f"Level '{nivel['nivel']}' in '{trilha['id']}' missing 'desafio_pratico'"
                )

    def test_modulos_have_required_fields(self):
        """Each module must have id, titulo, descricao and duracao_horas."""
        data = load_trilhas()
        for trilha in data["trilhas"]:
            for nivel in trilha["niveis"]:
                for modulo in nivel["modulos"]:
                    for field in ("id", "titulo", "descricao", "duracao_horas"):
                        assert field in modulo, (
                            f"Module in '{trilha['id']}/{nivel['nivel']}' missing '{field}'"
                        )

    def test_desafio_has_criterios(self):
        """Each practical challenge must include a non-empty criterios list."""
        data = load_trilhas()
        for trilha in data["trilhas"]:
            for nivel in trilha["niveis"]:
                desafio = nivel["desafio_pratico"]
                assert "criterios" in desafio
                assert len(desafio["criterios"]) > 0

    def test_tempo_estimado_is_positive(self):
        """Estimated study time must be a positive number."""
        data = load_trilhas()
        for trilha in data["trilhas"]:
            for nivel in trilha["niveis"]:
                assert nivel["tempo_estimado_horas"] > 0
