from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext.filters import Filters
from settings import settings
from handler import (
    start,
    dog_image,
    cat_image
)



def main():
    updater = Updater(token=settings.TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        handler=CommandHandler(command='start', callback=start)
    )
    dispatcher.add_handler(
        handler=MessageHandler(filters=Filters.text("Dog"), callback=dog_image)

    )
    dispatcher.add_handler(
        handler=MessageHandler(filters=Filters.text("Cat"), callback=cat_image)
    )
    
    updater.start_polling()
    updater.idle()





if __name__== "__main__":
    main()