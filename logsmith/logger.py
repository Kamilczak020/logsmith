import re
import sys
import colorama
import datetime

colorama.init()

class Logsmith:
  def __init__(self, format = '[{level}] {time} | {message}', transports = [sys.stdout]):
    self.format = format
    self.transports = transports
    self.replacements = {}

  def info(self, message): 
    self.__log('INFO', message)

  def warn(self, message):
    self.__log('WARN', message)

  def error(self, message):
    self.__log('ERROR', message)

  def __log(self, level, message):
    for transport in self.transports:
      transport.write(self.__formatMessage(level, message))

  def __formatMessage(self, level, message):
    formatted_message = self.format

    for key, replacement in self.replacements.items():
      formatted_message = formatted_message.replace(key, replacement)

    if level == 'ERROR':
      formatted_message = formatted_message.replace('{level}', colorama.Fore.RED + 'ERROR' + colorama.Style.RESET_ALL)
    elif level == 'WARN':
      formatted_message = formatted_message.replace('{level}', colorama.Fore.YELLOW + 'WARNING' + colorama.Style.RESET_ALL)
    elif level == 'INFO':
      formatted_message = formatted_message.replace('{level}', colorama.Fore.BLUE + 'INFO' + colorama.Style.RESET_ALL)

    formatted_message = formatted_message.replace('{time}', str(datetime.datetime.now()))
    formatted_message = formatted_message.replace('{message}', message)
    formatted_message += '\r\n'
    
    return formatted_message

logger = Logsmith()
logger.error('WOW!')