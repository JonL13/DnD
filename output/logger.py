import logging
import time

class Logger:

  def storyLog(self, message):
    logging.basicConfig(level=logging.INFO, filename='story.log', filemode='a', format='%(asctime)s: %(message)s', datefmt='%d-%b-%y %H:%M')
    logging.info(message)
