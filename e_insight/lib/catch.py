import logging

LOG = logging.getLogger(__name__)


def catch_default(default_value):
    def catch(function):
        def inner(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
                return result
            except Exception as e:
                LOG.error("call %s, args %s, kwargs %s, err %s, use default %s", function, args, kwargs, e,
                          default_value)
                return default_value

        return inner

    return catch
