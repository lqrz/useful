class Logger(object):
    __instance = None

    def __init__(self):
        pass

    def __new__(cls, name=__name__,
                level=logging.DEBUG,
                output_path=os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
                                         'output', 'logs'), **kwargs):

        if not cls.__instance:
            cls.__instance = object.__new__(cls)
            cls.__configure_logger(name=name, level=level, output_path=output_path)

        return cls.__instance

    @classmethod
    def __configure_logger(cls, name, level, output_path):
	pass
