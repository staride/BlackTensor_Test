from flask import request
from flask_restful import Resource, reqparse
from flask import jsonify
import json

from com_blacktensor.cop.emo.model.emotion_dao import EmotionDao, StockNewsDao
from com_blacktensor.cop.emo.model.emotion_dfo import EmotionDfo
from com_blacktensor.cop.emo.model.emotion_kdd import EmotionKdd
from com_blacktensor.cop.emo.model.emotion_dto import EmotionVo
from com_blacktensor.cop.emo.model.emotion_dto import EmotionDto
# ============================================================
# ==================                     =====================
# ==================      Resourcing     =====================
# ==================                     =====================
# ============================================================
class Emotion(Resource):
    def __init__(self):
        self.dao = EmotionDao()

    @staticmethod
    def post():
        print(f'[ Emotion Signup Resource Enter ] ')
        body = request.get_json()
        emotion = EmotionDto(**body)
        EmotionDao.save(emotion)
        
        return {'emotion': str(emotion)}, 200

    def get(self):
        result = EmotionDao().find_all()
        # with open('word.json', 'w', encoding='utf-8') as make_file:
        #     json.dump(result, make_file, ensure_ascii=False, indent='\t')
        return jsonify([item.json for item in result])
        # return jsonify(str(result))


class StockNews(Resource):
    def __init__(self):
        self.dao = StockNewsDao()

    def get(self):
        result = self.dao.find_all()
        return jsonify([item.json for item in result])