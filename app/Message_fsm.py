from aiogram.dispatcher.filters.state import State, StatesGroup

CHANNEL_NAME = -1234567890  # Or you can use this format "@channelname", only if you have public group

class MessageState(StatesGroup):
    message1 = State()
    message2 = State()
    message3 = State()
    message4 = State()
    message5 = State()
    message6 = State()
