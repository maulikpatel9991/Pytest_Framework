
import logging
def custom_logger():
    logger = logging.getLogger("maulik")
    logger.setLevel(logging.DEBUG)
    fileHandler = logging.FileHandler("Reports/data_log.log", mode='a')
    fileHandler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s',
                                  datefmt='%d/%m/%y %I:%M:%S %p %A')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger
