import logging

class create_logs:
        @staticmethod
        def logs_generator():
            logging.basicConfig(filename = ".\\logs\\testarena.log", format = "%(asctime)s:%(levelname)s:%(message)s", datefmt = "%Y-%m-%d_%H:%M:%S", force=True)
            logger = logging.getLogger()
            logger.setLevel(logging.INFO)

            return logger