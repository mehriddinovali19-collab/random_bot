from telegram.ext import CallbackContext
from telegram import ReplyKeyboardMarkup, KeyboardButton
import requests

def start(update, context: CallbackContext):
    update.message.reply_text(
        text="Choose the Animal:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Dog"),
                    KeyboardButton(text="Cat"),
                ]
            ],
            resize_keyboard=True
        )
    )


def dog_image(update, context):
    response = requests.get("https://dog.ceo/api/breeds/image/random", timeout=10)
    data = response.json()
    if data.get("status") == "success":
        update.message.reply_photo(
            photo=data["message"]
        )

    else:
        update.message.reply_text(
            "Rasm topilmadi."
        )


def cat_image(update, context):
    response = requests.get(
        "https://api.thecatapi.com/v1/images/search",
        timeout=10
    )
    data = response.json()

    if data and len(data) > 0:
        update.message.reply_photo(photo=data[0]["url"])
    else:
        update.message.reply_text("Rasm topilmadi.")