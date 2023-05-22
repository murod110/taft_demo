import logging, wget
from api import create_user, create_feedback, get_product, get_carpet_id,get_palet,get_prod_id
from aiogram import Bot, Dispatcher, executor, types
from buttons import button
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.parts import paginate
from aiogram_dialog.widgets.kbd import ScrollingGroup


API_TOKEN = '6213765950:AAHL3l98zcSyeOA9TuhtOwCVYAVEe75af7w'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.", reply_markup=button)
    create_user(str(message.from_user.username),str(message.from_user.first_name),str(message.from_user.id))


@dp.message_handler(Text("🪡🧶 Tufting"))
async def echo(message: types.Message):
    dat = get_product(message.text)
    menu = InlineKeyboardMarkup(row_width=3)
    for k,v in dat.items():
        button = InlineKeyboardButton(text=k,callback_data=v,quantity=1)
        menu.insert(button)    
    await message.reply(f"Assalomu Aleykum Hurmatli Mijoz \n Bizning {message.text} Bo'limida \n quyidagi mahsulotlar mavjud",reply_markup=menu)

@dp.message_handler(Text("🖨 Printed"))
async def echo(message: types.Message):
    data = get_product(message.text)
    menu = InlineKeyboardMarkup(row_width=3)
    for k,v in data.items():
        button = InlineKeyboardButton(text=k,callback_data=v,quantity=1)
        menu.insert(button)    


    await message.reply(f"Assalomu Aleykum Hurmatli Mijoz \n Bizning {message.text} Bo'limida \n quyidagi mahsulotlar mavjud",reply_markup=menu)
    
@dp.message_handler(Text("🏟 Grass"))
async def echo(message: types.Message):
    data = get_product(message.text)
    menu = InlineKeyboardMarkup(row_width=3)
    for k,v in data.items():
        button = InlineKeyboardButton(text=k,callback_data=v,quantity=1)
        menu.insert(button)    


    await message.reply(f"Assalomu Aleykum Hurmatli Mijoz \n Bizning {message.text} Bo'limida \n quyidagi mahsulotlar mavjud",reply_markup=menu)

@dp.message_handler(Text("🛁 Bath Mats"))
async def echo(message: types.Message):
    data = get_product(message.text)
    menu = InlineKeyboardMarkup(row_width=3)
    for k,v in data.items():
        button = InlineKeyboardButton(text=k,callback_data=v,quantity=1)
        menu.insert(button)    


    await message.reply(f"Assalomu Aleykum Hurmatli Mijoz \n Bizning {message.text} Bo'limida \n quyidagi mahsulotlar mavjud",reply_markup=menu)


@dp.message_handler(Text('🌐 Our Website'))
async def Link(message: types.Message):
    await message.reply("https://92ec-84-54-84-188.in.ngrok.io")



@dp.callback_query_handler()
async def get_carpet(callback: types.CallbackQuery):
    d= []
    for c in callback.data:
        d.append(c)
    if d in ["0","1","2","2","4","5","6","7","8","9"]:
        carpet = get_carpet_id(int(callback.data))
        palet = get_palet(int(callback.data))
        menu = InlineKeyboardMarkup(row_width=3)
        for c in carpet:
            a = c["design"]["name"] + "_" + c["color"]
            button1 = InlineKeyboardButton(text=a,callback_data=c["design"]["name"],quantity=1)
            menu.insert(button1)
        await callback.message.reply(f"<b><i>{palet}</i> paletining dizaynlar tarkibi.</b>",reply_markup=menu,parse_mode='HTML')
    else:
        carpet = get_prod_id(callback.data)
        for c in carpet:
            file=wget.download(c['photo'])
            photo_url = types.InputFile(file)
            text = ""
            """for table in c["design"]['palet']['char']:
                text += f" <b>{table['name']}</b> \n"
                text += f"<b>Charakter</b>--------<b>Value</b>     \n"
                text += f"Pile------------------{table['pile']}       \n"
                text += f"Pile height---------{table['pile_height']}mm  \n"
                text += f"Yarn weight-------{table['yarn_weight']}gr     \n"
                text += f"Prim. basic--------{table['primary_basic']}\n"
                text += f"Second basic-----{table['secondary_basic']}     \n"
                text += f"Points------------{table['points']} \n"
                text += f"Total weight------{table['total_weight']}gr\n\n" """
            await bot.send_photo(chat_id=callback.from_user.id,photo=photo_url)   
    

    #text = f"Design:{carpet['design']} Color:{carpet['color']} {callback.data}"
    #file=wget.download(carpet['photo'])
    #photo_url = types.InputFile(file)
    #await bot.send_photo(chat_id=callback.from_user.id,photo=photo_url,caption=text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)