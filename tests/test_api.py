import pytest
import sys

sys.path.insert(1, "C:\\Users\\frane\\PycharmProjects\\ChessApp")
from main import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


class TestKingAPI:
    def test_valid_moves_king(self, client):
        url: str = "/api/v1/king/e4"

        response = client.get(url)

        assert response.status_code == 200

    def test_validate_move_king(self, client):
        url: str = "/api/v1/king/e4/d5"

        response = client.get(url)

        assert response.status_code == 200

    def test_invalid_moves_king(self, client):
        url: str = "/api/v1/king/e20"

        response = client.get(url)

        assert response.status_code == 409

    def test_invalid_validate_move_king(self, client):
        url: str = "/api/v1/king/e4/e30"

        response = client.get(url)

        assert response.status_code == 409


class TestQueenAPI:
    def test_valid_moves_queen(self, client):
        url: str = "/api/v1/queen/h3"

        response = client.get(url)

        assert response.status_code == 200

    def test_validate_move_king(self, client):
        url: str = "/api/v1/queen/h3/h4"

        response = client.get(url)

        assert response.status_code == 200

    def test_invalid_moves_queen(self, client):
        url: str = "/api/v1/queen/h20"

        response = client.get(url)

        assert response.status_code == 409

    def test_invalid_validate_move_queen(self, client):
        url: str = "/api/v1/queen/h3/a30"

        response = client.get(url)

        assert response.status_code == 409


class TestRookAPI:
    def test_valid_moves_rook(self, client):
        url: str = "/api/v1/rook/b1"

        response = client.get(url)

        assert response.status_code == 200

    def test_validate_move_rook(self, client):
        url: str = "/api/v1/rook/b1/b5"

        response = client.get(url)

        assert response.status_code == 200

    def test_invalid_moves_rook(self, client):
        url: str = "/api/v1/rook/e20"

        response = client.get(url)

        assert response.status_code == 409

    def test_invalid_validate_move_rook(self, client):
        url: str = "/api/v1/rook/e4/e30"

        response = client.get(url)

        assert response.status_code == 409


class TestBishopAPI:
    def test_valid_moves_bishop(self, client):
        url: str = "/api/v1/bishop/f5"

        response = client.get(url)

        assert response.status_code == 200

    def test_validate_move_bishop(self, client):
        url: str = "/api/v1/bishop/f5/e6"

        response = client.get(url)

        assert response.status_code == 200

    def test_invalid_moves_bishop(self, client):
        url: str = "/api/v1/bishop/c25"

        response = client.get(url)

        assert response.status_code == 409

    def test_invalid_validate_move_bishop(self, client):
        url: str = "/api/v1/bishop/f5/e30"

        response = client.get(url)

        assert response.status_code == 409


class TestKnightAPI:
    def test_valid_moves_knight(self, client):
        url: str = "/api/v1/knight/c5"

        response = client.get(url)

        assert response.status_code == 200

    def test_validate_move_knight(self, client):
        url: str = "/api/v1/knight/c5/a4"

        response = client.get(url)

        assert response.status_code == 200

    def test_invalid_moves_knight(self, client):
        url: str = "/api/v1/knight/d30"

        response = client.get(url)

        assert response.status_code == 409

    def test_invalid_validate_move_knight(self, client):
        url: str = "/api/v1/knight/c5/d30"

        response = client.get(url)

        assert response.status_code == 409


class TestPawnAPI:
    def test_valid_moves_pawn(self, client):
        url: str = "/api/v1/pawn/c5"

        response = client.get(url)

        assert response.status_code == 200

        url: str = "/api/v2/pawn/c5"

        response = client.get(url)

        assert response.status_code == 200

    def test_validate_move_pawn(self, client):
        url: str = "/api/v1/pawn/c5/c4"

        response = client.get(url)

        assert response.status_code == 200

        url: str = "api/v2/pawn/c5/c6"

        response = client.get(url)

        assert response.status_code == 200

    def test_invalid_moves_pawn(self, client):
        url: str = "/api/v1/pawn/c30"

        response = client.get(url)

        assert response.status_code == 409

        url: str = "/api/v2/pawn/c30"

        response = client.get(url)

        assert response.status_code == 409

    def test_invalid_validate_move_pawn(self, client):
        url: str = "/api/v1/pawn/c5/d30"

        response = client.get(url)

        assert response.status_code == 409

        url: str = "/api/v2/pawn/c5/d30"

        response = client.get(url)

        assert response.status_code == 409

    def test_version_pawn(self, client):
        url: str = "/api/v5/pawn/c5/d30"

        response = client.get(url)

        assert response.status_code == 409


class TestAPI:
    def test_not_found_page(self, client):
        url: str = "/api/v2/figure/c5/d30"

        response = client.get(url)

        assert response.status_code == 404

        url: str = "/api/v1/some_word/c5/"

        response = client.get(url)

        assert response.status_code == 404

        url: str = "/api"

        response = client.get(url)

        assert response.status_code == 404
