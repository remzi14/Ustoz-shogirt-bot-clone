from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove, ParseMode

from data.config import ADMINS
from keyboards.default.menyu import javob_state
from loader import dp,bot
from states.ishjoyi import Ishkerak



@dp.message_handler(text='Ish joyi kerak')
async def select_menu(message:types.Message):
    text=f"<b>Ish joyi topish uchun ariza berish</b>\n\n"
    text+=f"Hozir sizga bir necha savollar beriladi. \n"
    text+=f"Har biriga javob bering.  \n"
    text+=f"Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va   \n"
    text+=f"arizangiz Adminga yuboriladi. \n"

    await message.answer(text)
    await message.answer('<b>Ism, familiyangizni kiriting?</b>')
    await Ishkerak.ism_familya.set()

#ism familya holati

@dp.message_handler(state=Ishkerak.ism_familya)
async def ism_familya (message:types.Message,state:FSMContext):
    ism_familya=message.text
    await state.update_data(
        {
            'ism_familya':ism_familya
        }
    )
    await Ishkerak.yosh.set()
    await message.answer('<b> 🕑 Yosh:</b>\n\nYoshingizni kiriting? \nMasalan, 19')


#yosh kiritish holati
@dp.message_handler(state=Ishkerak.yosh)
async def ism_familya (message:types.Message,state:FSMContext):
    yosh=message.text
    await state.update_data(
        {
            'yosh':yosh
        }
    )
    await Ishkerak.texno.set()
    text=f"<b>📚 Texnologiya:</b>\n\n"
    text+=f"Talab qilinadigan texnologiyalarni kiriting?\n"
    text+=f"Texnologiya nomlarini vergul bilan ajrating. Masalan, \n"
    text+=f"Java, C++, C#\n"
    await message.answer(text)



#Texnologiya kiritish holati
@dp.message_handler(state=Ishkerak.texno)
async def ism_familya (message:types.Message,state:FSMContext):
    texnologiya=message.text
    await state.update_data(
        {
            'texnologiya':texnologiya
        }
    )
    await Ishkerak.aloqa.set()
    text=f"<b>📞 Aloqa: </b>\n\n"
    text+=f"Bog`lanish uchun raqamingizni kiriting?\n"
    text+=f"Masalan, +998 90 123 45 67 \n"
    await message.answer(text)



#aloq kiritish holati
@dp.message_handler(state=Ishkerak.aloqa)
async def ism_familya (message:types.Message,state:FSMContext):
    aloqa=message.text
    await state.update_data(
        {
            'aloqa':aloqa
        }
    )
    await Ishkerak.hudud.set()
    text=f"<b>🌐 Hudud:  </b>\n\n"
    text+=f"Qaysi hududdansiz?\n"
    text+=f"Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.\n"
    await message.answer(text)


#Hudud kiritish holati
@dp.message_handler(state=Ishkerak.hudud)
async def ism_familya (message:types.Message,state:FSMContext):
    hudud=message.text
    await state.update_data(
        {
            'hudud':hudud
        }
    )
    await Ishkerak.narxi.set()
    text=f"<b>💰 Narxi:</b>\n\n"
    text+=f"Tolov qilasizmi yoki Tekinmi?\n"
    text+=f"Kerak bo`lsa, Summani kiriting?\n"
    await message.answer(text)

#narxi uchun handler
@dp.message_handler(state=Ishkerak.narxi)
async def ism_familya (message:types.Message,state:FSMContext):
    narxi=message.text
    await state.update_data(
        {
            'narxi':narxi
        }
    )
    await Ishkerak.kasbi.set()
    text=f"<b>👨🏻‍💻 Kasbi: </b>\n\n"
    text+=f"Ishlaysizmi yoki o`qiysizmi?\n"
    text+=f"Masalan, Talaba\n"
    await message.answer(text)


#kasbi uchun handler
@dp.message_handler(state=Ishkerak.kasbi)
async def ism_familya (message:types.Message,state:FSMContext):
    kasbi=message.text
    await state.update_data(
        {
            'kasbi':kasbi
        }
    )
    await Ishkerak.murojat_vaqti.set()
    text=f"<b>🕰 Murojaat qilish vaqti: </b>\n\n"
    text+=f"Qaysi vaqtda murojaat qilish mumkin?\n"
    text+=f"Masalan, 9:00 - 18:00\n"
    await message.answer(text)



#murojat vaqti uchun handler
@dp.message_handler(state=Ishkerak.murojat_vaqti)
async def ism_familya (message:types.Message,state:FSMContext):
    murojat_vaqti=message.text
    await state.update_data(
        {
            'murojat_vaqti':murojat_vaqti
        }
    )
    await Ishkerak.maqsad.set()
    text=f"<b>🔎 Maqsad:  </b>\n\n"
    text+=f"Maqsadingizni qisqacha yozib bering.\n"
    await message.answer(text)


@dp.message_handler(state=Ishkerak.maqsad)
async def ism_familya (message:types.Message,state:FSMContext):
    maqsad=message.text
    await state.update_data(
        {
            'maqsad':maqsad
        }
    )

    # Ma'lumotlarni o'qiymiz
    user_data=await state.get_data()
    ism_familya=user_data.get('ism_familya')
    yosh=user_data.get('yosh')
    texnologiya=user_data.get('texnologiya')
    aloqa=user_data.get('aloqa')
    hudud=user_data.get('hudud')
    narxi=user_data.get('narxi')
    kasbi=user_data.get('kasbi')
    murojat_vaqti=user_data.get('murojat_vaqti')
    maqsad=user_data.get('maqsad')

    #foydalanuvchiga xabar chiqaramiz
    text=f"<b>Ish joyi kerak:</b>\n\n"
    text+=f"👨‍💼 Xodim: {ism_familya}\n"
    text+=f"🕑 Yosh: {yosh}\n"
    text+=f"📚 Texnologiya: {texnologiya}\n"
    text+=f"📞 Aloqa:  {aloqa}\n"
    text+=f"🌐 Hudud:  {hudud}\n"
    text+=f"💰 Narxi   {narxi}\n"
    text+=f"👨🏻‍💻 Kasbi: {kasbi}\n"
    text+=f"🕰 Murojaat qilish vaqti:{murojat_vaqti}\n"
    text+=f"🔎 Maqsad: {maqsad}\n"

    await Ishkerak.ha_yoq.set()
    await message.answer(text)
    await message.answer("Barcha ma'lumotlar to'g'rimi?",reply_markup=javob_state)

#Foydalanuvchidan javobni olish
@dp.message_handler(state=Ishkerak.ha_yoq)
async def ha_yoq_handler(message: types.Message, state: FSMContext):
    javob = message.text.lower()


    if javob == "ha":
        user_data = await state.get_data()
        #foydalanuvchi haqida ma'lumot
        mention=message.from_user.get_mention()
        ism_familya = user_data.get('ism_familya')
        yosh = user_data.get('yosh')
        texnologiya = user_data.get('texnologiya')
        aloqa = user_data.get('aloqa')
        hudud = user_data.get('hudud')
        narxi = user_data.get('narxi')
        kasbi = user_data.get('kasbi')
        murojat_vaqti = user_data.get('murojat_vaqti')
        maqsad = user_data.get('maqsad')

        text = f"<b>Ish joyi kerak:</b>\n\n"
        text += f"👨‍💼 Xodim: {ism_familya}\n"
        text += f"🕑 Yosh: {yosh}\n"
        text += f"📚 Texnologiya: {texnologiya}\n"
        text += f"📞 Aloqa:  {aloqa}\n"
        text += f"🌐 Hudud:  {hudud}\n"
        text += f"💰 Narxi:   {narxi}\n"
        text += f"👨🏻‍💻 Kasbi: {kasbi}\n"
        text += f"🕰 Murojaat qilish vaqti: {murojat_vaqti}\n"
        text += f"🔎 Maqsad: {maqsad}\n"

        await message.answer("Qabul qilindi, adminga yuborildi", reply_markup=ReplyKeyboardRemove())

        # Bu joyda ma'lumotlarni adminga yuborishni qo'shing
        admin_id = ADMINS[0] # O'zgartiring, admin_id ni olish uchun /id buyrug'ini ishlatishingiz mumkin

        await bot.send_message(admin_id, f"Foydalanuvchi {mention} quyidagi anketani to'ldirdi:")
        await bot.send_message(admin_id, text,parse_mode=ParseMode.HTML)

    elif javob == "yo'q":
        await message.answer("Qabul qilinmadi", reply_markup=ReplyKeyboardRemove())
        await state.finish()

    else:
        await message.answer("Noto'g'ri javob. Iltimos, 'ha' yoki 'yo'q' deb javob bering.")



