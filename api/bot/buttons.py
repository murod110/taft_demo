from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='🪡🧶 Tufting'),
            KeyboardButton(text="🖨 Printed")
        ],
        [
            KeyboardButton(text="🏟 Grass"),
            KeyboardButton(text="🛁 Bath Mats")
        ],
        
        [
            KeyboardButton(text="🌐 Our Website")
        ]
    ]
)