from config import API_ID, API_HASH, BOT_TOKEN, BOT_NAME
from pyrogram import Client, filters, idle
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery
)

Medusa = Client(
    session_name=BOT_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root='plugins')
)


PMTEXT = (
    "السلام عليكم . أنا بوت أقوم بتحميل الدروس الصوتية من يوتيوب  "
    "فقط اكتب اسم الدرس الذي تريد مسبوقاً بـ /get  "
    " مثلاً /get السنة لعبدالله بن أحمد 01 الخليفي  "
    " لبقية البوتات هنا https://t.me/ibnAlQyyim/1120 "
    " لدعم استمرار المشروع هنا http://paypal.me/kelectronic89"
)
PMKEYBOARD = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                'Help ❓', callback_data='help_callback'),
            InlineKeyboardButton('عن البوت ❕', callback_data='about')
        ],
        [
            InlineKeyboardButton(
                'إضافة لجروب  🎊', url='http:t.me/audmergbot?startgroup=true')  # Replace the `MedusaMousikibot` with your bot username
        ]
    ]
)
HELPTEXT = (
   'كما قلت سابقاً . فقط اسكتب اسم الدرس مسبوقاً بالأمر__ /get __ \n'
)
ABOUTTEXT = (
     "__السلام عليكم . أنا بوت أقوم بتحميل الدروس الصوتية من يوتيوب  "
    "فقط اكتب اسم الدرس الذي تريد مسبوقاً بـ /get  "
    " مثلاً /get السنة لعبدالله بن أحمد 01 الخليفي "
    " لبقية البوتات هنا https://t.me/ibnAlQyyim/1120 "
    " لدعم استمرار المشروع هنا http://paypal.me/kelectronic89 __ "
)


@Medusa.on_message(
    filters.command(['start', 'help'], ['/', '!'])
    & (filters.private | filters.group)
    & ~ filters.edited
)
async def start_cmd(_, msg: Message):
    ''' Response for /start command (private or groupe) '''

    if msg.chat.type == 'private':
        await msg.reply(
            text=(
    "السلام عليكم . أنا بوت أقوم بتحميل الدروس الصوتية من يوتيوب  "
    "فقط اكتب اسم الدرس الذي تريد مسبوقاً بـ /get  "
    " مثلاً /get السنة لعبدالله بن أحمد 01 الخليفي  "
    " لبقية البوتات هنا https://t.me/ibnAlQyyim/1120 "
    " لدعم استمرار المشروع هنا http://paypal.me/kelectronic89"
)
            reply_markup=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                'Help ❓', callback_data='help_callback'),
            InlineKeyboardButton('عن البوت ❕', callback_data='about')
        ],
        [
            InlineKeyboardButton(
                'إضافة لجروب  🎊', url='http:t.me/audmergbot?startgroup=true')  # Replace the `MedusaMousikibot` with your bot username
        ]
    ]
)
        )
    else:
        await msg.reply(
            text='أنا أعمل . لمعرفة طريقة استعمالي . زرني على الخاص',
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text='أضفني كأدمن في الجروب  :)',
                            # Replace the `MedusaMousikibot` with your bot username
                            url=f't.me/audmergbot?start=help'
                        )
                    ]
                ]
            )
        )


@Medusa.on_callback_query()
async def callback_handling(_, query: CallbackQuery):
    ''' Response for Callback queries '''

    q_data = query.data
    q_id = query.id

    if q_data == 'menu_1':
        await Medusa.answer_callback_query(q_id, 'Main Menu!')
        await query.message.edit(
            text=PMTEXT,
            reply_markup=PMKEYBOARD,
            disable_web_page_preview=True
        )

    elif q_data == 'help_callback':
        await Medusa.answer_callback_query(q_id, 'Help Menu!')
        await query.message.edit(text=HELPTEXT,
                                 parse_mode='md',
                                 reply_markup=InlineKeyboardMarkup(
                                     [
                                         [
                                             InlineKeyboardButton(
                                                 text="Back",
                                                 callback_data='menu_1',
                                             )
                                         ]
                                     ]
                                 ),
                                 )

    elif q_data == 'about':
        await Medusa.answer_callback_query(q_id, text='About Menu!')
        await query.message.edit(
            text=ABOUTTEXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            'Back', callback_data='menu_1')
                    ]
                ]
            )
        )




Medusa.start()
print('Medusa is starting....')
idle()
print('Medusa is aborting...')
Medusa.stop()
