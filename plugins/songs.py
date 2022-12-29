import os
from funcs.download import Descargar
from pyrogram import Client as Medusa, filters
from pyrogram.types import Message
from pyrogram.errors.exceptions import MessageNotModified
from youtubesearchpython import VideosSearch


text = (
  'لا أستطيع تحديد المقطع الذي تريد \n '
  'استخدم كلمات دلالية أكثر دقة \n '
)

descargar = Descargar('downloads/')

@Medusa.on_message(
    filters.command(['get'],prefixes=['/', '!'])
    & (filters.group | filters.private)
    & ~ filters.edited)
async def song_dl(_, msg: Message):

    if len(msg.command) == 1:
        return await msg.reply(text=text, parse_mode='md')

    r_text = await msg.reply('جاري المعالجة')
    url = msg.text.split(None, 1)[1]
    url = extract_the_url(url=url)
    
    if url == 0:return await r_text.edit('لم أستطع إيجاد هذا المقطع . جرب استخدام كلمات دلالية أخرى')

    await r_text.edit('يتم التنزيل...')

    ytinfo = descargar.get_song(url)

    if ytinfo == 0:
        await r_text.edit(f'حدث خطأ ما:(')
        return

    try:
        await r_text.edit_text('يتم الرفع...')
    except MessageNotModified:
        pass

    await msg.reply_audio(
            audio=f'downloads/{ytinfo.title.replace("/","|")}-{ytinfo.video_id}.mp3', 
            thumb='src/Medusa320px.png',
            duration=int(ytinfo.length),
            performer=str(ytinfo.author),
            title=f'{str(ytinfo.title)}',
            caption=f"<a href='{url}'>__{ytinfo.title}__</a>\n\n__تم تحميله بواسطة @audmergbot__"
        )

    await r_text.delete()
    os.remove(f'downloads/{ytinfo.title.replace("/","|")}-{ytinfo.video_id}.mp3')



def extract_the_url(url: str):
    '''جاري استخراج عنوان الفيديو'''

    v = VideosSearch(url, limit=1)
    v_result = v.result()

    if not v_result['result']:
        return 0
    url = v_result['result'][0]['link']
    return url
