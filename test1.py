# -*- coding: utf-8 -*-
"""
@author: LiaoKong
@time: 2021/08/29 17:28 
"""
from ftrack_events_helper import subscribe, logger, run_test_server


@subscribe()
def test1(session, event):
    logger.info('这是test1的log')


if __name__ == '__main__':
    run_test_server()
