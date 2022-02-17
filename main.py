from models import King, Queen, Rook, Bishop, Knight, Pawn, board
from flask import Flask
from flask_restful import Resource, Api

app = Flask("ChessApp")
api = Api(app)


def is_field(current_field: str) -> bool:
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == current_field:
                return True

    return False


class KingAPIMoves(Resource):
    def get(self, current_field: str):
        if is_field(current_field):
            obj: King = King(current_field)

            data: dict = {
                "availableMoves": obj.list_available_moves(),
                "error": None,
                "figure": "king",
                "currentField": current_field,
            }

            return data, 200

        else:
            data: dict = {
                "available": [],
                "error": "Field does not exists",
                "figure": "king",
                "currentField": current_field,
            }

            return data, 409


class KingAPIValidate(Resource):
    def get(self, current_field: str, dest_field: str):
        if is_field(current_field):
            obj: King = King(current_field)

            if obj.validate_move(dest_field):
                data: dict = {
                    "move": "valid",
                    "figure": "king",
                    "error": None,
                    "currentField": current_field,
                    "destField": dest_field,
                }

                return data, 200

            else:
                data: dict = {
                    "move": "invalid",
                    "figure": "king",
                    "error": "Current move is not permitted",
                    "currentField": current_field,
                    "destField": dest_field,
                }

                return data, 409

        else:
            data: dict = {
                "available": [],
                "error": "Field does not exists",
                "figure": "king",
                "currentField": current_field,
                "destField": dest_field,
            }

            return data, 409


class QueenAPIMoves(Resource):
    def get(self, current_field: str):
        if is_field(current_field):
            obj: Queen = Queen(current_field)

            data: dict = {
                "availableMoves": obj.list_available_moves(),
                "error": None,
                "figure": "queen",
                "currentField": current_field,
            }

            return data, 200

        else:
            data: dict = {
                "available": [],
                "error": "Field does not exists",
                "figure": "queen",
                "currentField": current_field,
            }

            return data, 409


class QueenAPIValidate(Resource):
    def get(self, current_field: str, dest_field: str):
        if is_field(current_field):
            obj: Queen = Queen(current_field)

            if obj.validate_move(dest_field):
                data: dict = {
                    "move": "valid",
                    "figure": "queen",
                    "error": None,
                    "currentField": current_field,
                    "destField": dest_field,
                }

                return data, 200

            else:
                data: dict = {
                    "move": "invalid",
                    "figure": "queen",
                    "error": "Current move is not permitted",
                    "currentField": current_field,
                    "destField": dest_field,
                }

                return data, 409

        else:
            data: dict = {
                "available": [],
                "error": "Field does not exists",
                "figure": "queen",
                "currentField": current_field,
                "destField": dest_field,
            }

            return data, 409


class RookAPIMoves(Resource):
    def get(self, current_field: str):
        if is_field(current_field):
            obj: Rook = Rook(current_field)

            data: dict = {
                "availableMoves": obj.list_available_moves(),
                "error": None,
                "figure": "rook",
                "currentField": current_field,
            }

            return data, 200

        else:
            data: dict = {
                "available": [],
                "error": "Field does not exists",
                "figure": "rook",
                "currentField": current_field,
            }

            return data, 409


class RookAPIValidate(Resource):
    def get(self, current_field: str, dest_field: str):
        if is_field(current_field):
            obj: Rook = Rook(current_field)

            if obj.validate_move(dest_field):
                data: dict = {
                    "move": "valid",
                    "figure": "rook",
                    "error": None,
                    "currentField": current_field,
                    "destField": dest_field,
                }

                return data, 200

            else:
                data: dict = {
                    "move": "invalid",
                    "figure": "rook",
                    "error": "Current move is not permitted",
                    "currentField": current_field,
                    "destField": dest_field,
                }

                return data, 409

        else:
            data: dict = {
                "available": [],
                "error": "Field does not exists",
                "figure": "rook",
                "currentField": current_field,
                "destField": dest_field,
            }

            return data, 409


class BishopAPIMoves(Resource):
    def get(self, current_field: str):
        if is_field(current_field):
            obj: Bishop = Bishop(current_field)

            data: dict = {
                "availableMoves": obj.list_available_moves(),
                "error": None,
                "figure": "bishop",
                "currentField": current_field,
            }

            return data, 200

        else:
            data: dict = {
                "available": [],
                "error": "Field does not exists",
                "figure": "bishop",
                "currentField": current_field,
            }

            return data, 409


class BishopAPIValidate(Resource):
    def get(self, current_field: str, dest_field: str):
        if is_field(current_field):
            obj: Bishop = Bishop(current_field)

            if obj.validate_move(dest_field):
                data: dict = {
                    "move": "valid",
                    "figure": "bishop",
                    "error": None,
                    "currentField": current_field,
                    "destField": dest_field,
                }

                return data, 200

            else:
                data: dict = {
                    "move": "invalid",
                    "figure": "bishop",
                    "error": "Current move is not permitted",
                    "currentField": current_field,
                    "destField": dest_field,
                }

                return data, 409

        else:
            data: dict = {
                "available": [],
                "error": "Field does not exists",
                "figure": "bishop",
                "currentField": current_field,
                "destField": dest_field,
            }

            return data, 409


class KnightAPIMoves(Resource):
    def get(self, current_field: str):
        if is_field(current_field):
            obj: Knight = Knight(current_field)

            data: dict = {
                "availableMoves": obj.list_available_moves(),
                "error": None,
                "figure": "knight",
                "currentField": current_field,
            }

            return data, 200

        else:
            data: dict = {
                "available": [],
                "error": "Field does not exists",
                "figure": "knight",
                "currentField": current_field,
            }

            return data, 409


class KnightAPIValidate(Resource):
    def get(self, current_field: str, dest_field: str):
        if is_field(current_field):
            obj: Knight = Knight(current_field)

            if obj.validate_move(dest_field):
                data: dict = {
                    "move": "valid",
                    "figure": "knight",
                    "error": None,
                    "currentField": current_field,
                    "destField": dest_field,
                }

                return data, 200

            else:
                data: dict = {
                    "move": "invalid",
                    "figure": "knight",
                    "error": "Current move is not permitted",
                    "currentField": current_field,
                    "destField": dest_field,
                }

                return data, 409

        else:
            data: dict = {
                "available": [],
                "error": "Field does not exists",
                "figure": "knight",
                "currentField": current_field,
                "destField": dest_field,
            }

            return data, 409


class PawnAPIMoves(Resource):
    def get(self, version: str, current_field: str):
        if is_field(current_field) and (version == "v1" or version == "v2"):
            obj: Pawn = Pawn(current_field)

            data: dict = {
                "availableMoves": obj.list_available_moves(key=version),
                "error": None,
                "figure": "king",
                "currentField": current_field,
            }

            return data, 200

        elif not is_field(current_field):
            data: dict = {
                "available": [],
                "error": "Field does not exists",
                "figure": "king",
                "currentField": current_field,
            }

            return data, 409

        else:
            data: dict = {
                "available": [],
                "error": "Wrong version",
                "figure": "pawn",
                "currentField": current_field,
            }

            return data, 409


class PawnAPIValidate(Resource):
    def get(self, version: str, current_field: str, dest_field: str):
        if is_field(current_field) and (version == "v1" or version == "v2"):
            obj: Pawn = Pawn(current_field)

            if obj.validate_move(dest_field, key=version):
                data: dict = {
                    "move": "valid",
                    "figure": "pawn",
                    "error": None,
                    "currentField": current_field,
                    "destField": dest_field,
                }

                return data, 200

            else:
                data: dict = {
                    "move": "invalid",
                    "figure": "pawn",
                    "error": "Current move is not permitted",
                    "currentField": current_field,
                    "destField": dest_field,
                }

                return data, 409

        elif not is_field(current_field):
            data: dict = {
                "available": [],
                "error": "Field does not exists",
                "figure": "pawn",
                "currentField": current_field,
            }

            return data, 409

        else:
            data: dict = {
                "available": [],
                "error": "Wrong version",
                "figure": "pawn",
                "currentField": current_field,
            }

            return data, 409


api.add_resource(
    KingAPIMoves,
    "/api/v1/king/<current_field>",
    endpoint="king-moves"
)

api.add_resource(
    KingAPIValidate,
    "/api/v1/king/<current_field>/<dest_field>",
    endpoint="king-validate",
)

api.add_resource(
    QueenAPIMoves,
    "/api/v1/queen/<current_field>",
    endpoint="queen-moves"

)

api.add_resource(
    QueenAPIValidate,
    "/api/v1/queen/<current_field>/<dest_field>",
    endpoint="queen-validate",
)

api.add_resource(
    RookAPIMoves,
    "/api/v1/rook/<current_field>",
    endpoint="rook-moves"
)

api.add_resource(
    RookAPIValidate,
    "/api/v1/rook/<current_field>/<dest_field>",
    endpoint="rook-validate",
)

api.add_resource(
    BishopAPIMoves, "/api/v1/bishop/<current_field>", endpoint="bishop-moves"
)

api.add_resource(
    BishopAPIValidate,
    "/api/v1/bishop/<current_field>/<dest_field>",
    endpoint="bishop-validate",
)

api.add_resource(
    KnightAPIMoves, "/api/v1/knight/<current_field>", endpoint="knight-moves"
)

api.add_resource(
    KnightAPIValidate,
    "/api/v1/knight/<current_field>/<dest_field>",
    endpoint="knight-validate",
)

api.add_resource(
    PawnAPIMoves, "/api/<version>/pawn/<current_field>", endpoint="pawn-moves"
)

api.add_resource(
    PawnAPIValidate,
    "/api/<version>/pawn/<current_field>/<dest_field>",
    endpoint="pawn-validate",
)

if __name__ == "__main__":
    app.run()
