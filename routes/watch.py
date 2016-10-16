# -*- coding: utf-8 -*-
from flask import request, Blueprint

import json
from flask_login import login_required, current_user
from service.watch import watch_service

import logging

logger = logging.getLogger(__name__)

watch_api = Blueprint('watch', __name__)

@watch_api.route('/favorite/bangumi/<bangumi_id>', methods=['POST'])
@login_required
def favorite_bangumi(bangumi_id):
    data = json.loads(request.get_data(True, as_text=True))
    logger.debug(data)
    return watch_service.favorite_bangumi(bangumi_id, current_user.id, data['status'])


@watch_api.route('/favorite/episode/<episode_id>', methods=['POST'])
@login_required
def favorite_episode(episode_id):
    data = json.loads(request.get_data(True, as_text=True))
    return watch_service.favorite_episode(data['bangumi_id'], episode_id, current_user.id, data['status'])


@watch_api.route('/history/<episode_id>', methods=['POST'])
@login_required
def episode_history(episode_id):
    data = json.loads(request.get_data(True, as_text=True))
    return watch_service.episode_history(data['bangumi_id'], episode_id=episode_id, user_id=current_user.id, last_watch_position=data['last_watch_position'], is_finished=data['is_finished'])

