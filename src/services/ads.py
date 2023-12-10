from flask import request, jsonify, Blueprint, Response
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError

from src.db.database import connection
from src.db.models import Advertisement
from sqlalchemy import select, ScalarResult
from src.schemas.ads import AdUpdateSchema, ADCreateSchema


ads_router = Blueprint("ads_router", __name__, url_prefix="/ads")


@ads_router.route("/", methods=["GET"])
def get_ads():
    """
    Получить все объявления
    """
    stm = select(Advertisement)
    with connection as conn:
        ads: ScalarResult = conn.session.scalars(stm).unique().all()
    result = []
    for ad in ads:
        result.append(ad.to_dict())
    return jsonify(result)


@ads_router.route("/add", methods=["POST"])
def add_new_ad():
    """
    Добавить новый объявление
    """
    try:
        validated_ad = ADCreateSchema(**request.json)
    except ValidationError as err:
        return jsonify({"status": "error", "description": err.errors()})

    new_ad = Advertisement(**validated_ad.dict())

    with connection as conn:
        try:
            conn.session.add(new_ad)
            conn.session.commit()
            return jsonify({"status": "ok", "data": new_ad.to_dict()})
        except SQLAlchemyError as err:
            print(err)
            return jsonify(
                {
                    "status": "error",
                    "description": "Произошла ошибка при добавлении объявления",
                }
            )


@ads_router.route("/edit/<int:ad_id>", methods=["PATCH"])
def update_ad(ad_id: int):
    """
    Обновить объявление
    """
    try:
        updated_ad = AdUpdateSchema(**request.json)
    except ValidationError as err:
        return jsonify({"status": "error", "description": err.errors()})

    with connection as conn:
        ad = conn.session.get(Advertisement, ad_id)
        if not ad:
            return jsonify({"status": "error", "description": "Ad not found"})
        for field, value in updated_ad.dict(exclude_unset=True).items():
            setattr(ad, field, value)
        conn.session.add(ad)
        conn.session.commit()
        conn.session.refresh(ad)
    return jsonify(ad.to_dict())


@ads_router.route("/delete/<int:ad_id>", methods=["DELETE"])
def delete_ad(ad_id: int) -> Response:
    """
    Удалить объявление
    """
    with connection as conn:
        ad = conn.session.get(Advertisement, ad_id)
        if ad:
            conn.session.delete(ad)
            conn.session.commit()
            return Response(status=204)
        return jsonify({"status": "error", "description": "Ad not found"})
