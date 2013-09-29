# -*- coding: utf8 -*-
import sys
import traceback


class ExceptionHelper(object):
    @staticmethod
    def write_traceback(message, logger):
        logger.error('%s' % message)
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            logger.error(line.strip())