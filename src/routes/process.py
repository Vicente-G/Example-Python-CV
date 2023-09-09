from flask import Request, Response, jsonify
from jsonschema import ValidationError

from src.process import main


def response(req: Request) -> tuple[Response, int]:
    try:
        return jsonify(main(req.get_json())), 200
    except (ValueError, ValidationError) as error:
        return jsonify({"error": str(error)}), 400
    except KeyError as error:
        return jsonify({"error": str(error)}), 500
