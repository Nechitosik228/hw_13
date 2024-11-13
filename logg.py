import logging


logging.basicConfig(level=logging.INFO)


requests_logger = logging.getLogger("requests")
requests_handler = logging.FileHandler("requests.log")
requests_formatter = logging.Formatter("%(message)s")
requests_handler.setFormatter(requests_formatter)
requests_logger.addHandler(requests_handler)