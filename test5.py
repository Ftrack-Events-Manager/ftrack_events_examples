# -*- coding: utf-8 -*-
"""
@author: LiaoKong
@time: 2021/08/29 17:28 
"""
from ftrack_events_helper import subscribe, logger


@subscribe(priority=50)
def test5(session, event):
    logger.exception('这是test5的log')


@subscribe()
def test6(session, event):
    logger.info('这是test6的log')
