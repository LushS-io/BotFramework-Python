# Adapter to the Telegram Messenger

from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount, ActionTypes


def TelegramBot(ActivityHandler):
    def __init__(self, name, age):
          self.name = name
      self.age = age
