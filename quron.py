# quron bot
from aiogram import Bot, types, executor, Dispatcher
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
# from deep_translator import GoogleTranslator
# from gtts import gTTS
import requests
from datetime import datetime
# from pydub import AudioSegment


class opinions(StatesGroup):
	your=State()


class sura(StatesGroup):
	Surah=State()


class oyat(StatesGroup):
	Oyat=State()	


class prayer(StatesGroup):
	location=State()


sana=datetime.now().strftime('%d.%m.%Y')
API_KEY='44897350213456a971743686'

keyboard=[
	'Audio', #0
	'Sura', #1
	'Oyat', #2
	'Sajda', #4
	"Barchasi to'g'risida ma'lumot", #5
    '🆘 Yordam/Help', #-3
    '📬 Fikr va mulohaza', #-2
   	"❌ Bekor qilish" #-1
   ]
suralar=['Al-Faatiha', 'Al-Baqara', 'Aal-i-Imraan', 'An-Nisaa', 'Al-Maaida', "Al-An'aam", "Al-A'raaf", 'Al-Anfaal', 'At-Tawba', 'Yunus', 'Hud', 'Yusuf', "Ar-Ra'd", 'Ibrahim', 'Al-Hijr', 'An-Nahl', 'Al-Israa', 'Al-Kahf', 'Maryam', 'Taa-Haa', 'Al-Anbiyaa', 'Al-Hajj', 'Al-Muminoon', 'An-Noor', 'Al-Furqaan', "Ash-Shu'araa", 'An-Naml', 'Al-Qasas', 'Al-Ankaboot', 'Ar-Room', 'Luqman', 'As-Sajda', 'Al-Ahzaab', 'Saba', 'Faatir', 'Yaseen', 'As-Saaffaat', 'Saad', 'Az-Zumar', 'Ghafir', 'Fussilat', 'Ash-Shura', 'Az-Zukhruf', 'Ad-Dukhaan', 'Al-Jaathiya', 'Al-Ahqaf', 'Muhammad', 'Al-Fath', 'Al-Hujuraat', 'Qaaf', 'Adh-Dhaariyat', 'At-Tur', 'An-Najm', 'Al-Qamar', 'Ar-Rahmaan', 'Al-Waaqia', 'Al-Hadid', 'Al-Mujaadila', 'Al-Hashr', 'Al-Mumtahana', 'As-Saff', "Al-Jumu'a", 'Al-Munaafiqoon', 'At-Taghaabun', 'At-Talaaq', 'At-Tahrim', 'Al-Mulk', 'Al-Qalam', 'Al-Haaqqa', "Al-Ma'aarij", 'Nooh', 'Al-Jinn', 'Al-Muzzammil', 'Al-Muddaththir', 'Al-Qiyaama', 'Al-Insaan', 'Al-Mursalaat', 'An-Naba', "An-Naazi'aat", 'Abasa', 'At-Takwir', 'Al-Infitaar', 'Al-Mutaffifin', 'Al-Inshiqaaq', 'Al-Burooj', 'At-Taariq', "Al-A'laa", 'Al-Ghaashiya', 'Al-Fajr', 'Al-Balad', 'Ash-Shams', 'Al-Lail', 'Ad-Dhuhaa', 'Ash-Sharh', 'At-Tin', 'Al-Alaq', 'Al-Qadr', 'Al-Bayyina', 'Az-Zalzala', 'Al-Aadiyaat', "Al-Qaari'a", 'At-Takaathur', 'Al-Asr', 'Al-Humaza', 'Al-Fil', 'Quraish', "Al-Maa'un", 'Al-Kawthar', 'Al-Kaafiroon', 'An-Nasr', 'Al-Masad', 'Al-Ikhlaas', 'Al-Falaq', 'An-Naas']
bekor=types.ReplyKeyboardMarkup(resize_keyboard=True)
bekor.add(keyboard[-1])

kirish=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
kirish.add(*keyboard[:-1])

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()
API_TOKEN = '6251228035:AAFgOHzFDCTyZ9GeM0lRRFmP1y5ex3ZxpaM'
admin_id = 5509036572
# 6135585871
# 6332016043:AAE1IT0kp97Zj2T7-WCwOR1IZtFhaj-MZKY
bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot, storage=storage)

#tarjimaurl=requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-alauddinmansour").json()

#start
@dp.message_handler(commands=['start'])
async def salom(message):
	await message.answer("Assalomu alaykum, kerakli boʻlimni tanlang.", reply_markup=kirish)
	if f'{message.from_user.username}'!='None':
		j=f'\n@{message.from_user.username}'
	else:
		j='\nFoydalanuvchi nomi yo\'q'
	await bot.send_message(admin_id,f"{message.from_user.full_name}" + j)
#help
@dp.message_handler(lambda message: message.text == keyboard[-3])
async def help(message):
	await message.answer(f"Assalomu alaykum, {message.from_user.full_name}.\nMen @Universal_MB_bot uchun qoʻshimcha botman. \nFoydalanish uchun kerakli bo'limlarni tanlang. \n\nAdmin: @Dolunay_MB_bot")

@dp.message_handler(lambda message: message.text==keyboard[-1], state='*')
async def back(message: types.Message, state: FSMContext):
	await state.finish()
	await message.answer('Asosiy menyu', reply_markup=kirish)
# opinion
@dp.message_handler(lambda message: message.text==keyboard[-2], state='*')
async def opinion(message: types.Message, state: FSMContext):
	await state.finish()
	await message.answer('Har qanday savol, takliflar va boshqa turdagi murojaatlaringizni yozib qoldiring:', reply_markup=bekor)
	await opinions.your.set()

@dp.message_handler(state=opinions.your)
async def Fikr(message: types.Message, state: FSMContext):
	await state.update_data(fikri=message.text)
	xabar=f"{message.from_user.full_name} \n" + message.text
	await bot.send_message('6135585871', xabar)
	await message.answer("Murojaatingiz uchun rahmat. \nMurojaatingiz qabul qilindi. Adminlar ko'rib chiqib tez orada javob yuboradi." , reply_markup=kirish)	
	await state.reset_state(with_data=True)
#suralar
@dp.message_handler(lambda message: message.text==keyboard[1], state='*')
async def surah(message: types.Message, state: FSMContext):
	j="""1 Al-Faatiha
2 Al-Baqara
3 Aal-i-Imraan
4 An-Nisaa
5 Al-Maaida
6 Al-An'aam
7 Al-A'raaf
8 Al-Anfaal
9 At-Tawba
10 Yunus
11 Hud
12 Yusuf
13 Ar-Ra'd
14 Ibrahim
15 Al-Hijr
16 An-Nahl
17 Al-Israa
18 Al-Kahf
19 Maryam
20 Taa-Haa
21 Al-Anbiyaa
22 Al-Hajj
23 Al-Muminoon
24 An-Noor
25 Al-Furqaan
26 Ash-Shu'araa
27 An-Naml
28 Al-Qasas
29 Al-Ankaboot
30 Ar-Room
31 Luqman
32 As-Sajda
33 Al-Ahzaab
34 Saba
35 Faatir
36 Yaseen
37 As-Saaffaat
38 Saad
39 Az-Zumar
40 Ghafir
41 Fussilat
42 Ash-Shura
43 Az-Zukhruf
44 Ad-Dukhaan
45 Al-Jaathiya
46 Al-Ahqaf
47 Muhammad
48 Al-Fath
49 Al-Hujuraat
50 Qaaf
51 Adh-Dhaariyat
52 At-Tur
53 An-Najm
54 Al-Qamar
55 Ar-Rahmaan
56 Al-Waaqia
57 Al-Hadid
58 Al-Mujaadila
59 Al-Hashr
60 Al-Mumtahana
61 As-Saff
62 Al-Jumu'a
63 Al-Munaafiqoon
64 At-Taghaabun
65 At-Talaaq
66 At-Tahrim
67 Al-Mulk
68 Al-Qalam
69 Al-Haaqqa
70 Al-Ma'aarij
71 Nooh
72 Al-Jinn
73 Al-Muzzammil
74 Al-Muddaththir
75 Al-Qiyaama
76 Al-Insaan
77 Al-Mursalaat
78 An-Naba
79 An-Naazi'aat
80 Abasa
81 At-Takwir
82 Al-Infitaar
83 Al-Mutaffifin
84 Al-Inshiqaaq
85 Al-Burooj
86 At-Taariq
87 Al-A'laa
88 Al-Ghaashiya
89 Al-Fajr
90 Al-Balad
91 Ash-Shams
92 Al-Lail
93 Ad-Dhuhaa
94 Ash-Sharh
95 At-Tin
96 Al-Alaq
97 Al-Qadr
98 Al-Bayyina
99 Az-Zalzala
100 Al-Aadiyaat
101 Al-Qaari'a
102 At-Takaathur
103 Al-Asr
104 Al-Humaza
105 Al-Fil
106 Quraish
107 Al-Maa'un
108 Al-Kawthar
109 Al-Kaafiroon
110 An-Nasr
111 Al-Masad
112 Al-Ikhlaas
113 Al-Falaq
114 An-Naas
Kerakli suraning nomerini yozing! """
	await message.answer(j, reply_markup=bekor)
	await sura.Surah.set()

@dp.message_handler(lambda message: message.text.isdigit(), state=sura.Surah)
async def oyatlar(message: types.Message, state: FSMContext):
	response = requests.get('http://api.alquran.cloud/v1/quran/ar.alafasy').json()
	surahs = response['data']['surahs']
	a=''
	for i in surahs:
		if suralar[int(message.text)-1]==i['englishName']:
			k=0
			for j in i['ayahs']:
				a+=j['text']+'\n'
				k+=1
	if len(a)>4000:
		for i in range(4000, len(a), 4000):
			await message.answer(a[i-4000:i+1])
		if len(a)%4000!=0:
			i=len(a)%4000
			await message.answer(a[-i:])


# oyatlar
@dp.message_handler(lambda message: message.text == keyboard[2], state='*')
async def first(message: types.Message, state: FSMContext):
	await bot.send_message(message.chat.id,"Izlayotgan oyatingizni manzilini kiriting: \nMasalan, 1:1 (Birinchi sura, birinchi oyat)", reply_markup=bekor)
	await oyat.Oyat.set()


@dp.message_handler(lambda message: message.text.replace(':', '').isdigit(), state=oyat.Oyat)
async def third(message: types.Message, state: FSMContext):
	response = requests.get('http://api.alquran.cloud/v1/quran/ar.alafasy').json()
	surahs = response['data']['surahs']
	a=message.text.split(':')
	n,m=a[0],a[1]
	try:
		surah_name = suralar[int(n)-1]
	except IndexError:
		surah_name = ''
	if surah_name:
		ayahs = []
		for surah in surahs:
			if surah['englishName'] == surah_name:
				for ayah in surah['ayahs']:
					if int(ayah['numberInSurah']) == int(m):
						ayahs = surah['ayahs']
						break
		try:
			ayah = ayahs[int(m) - 1]
		except Exception as err:
			ayah = ''
		if ayah:
			tarjimaurl = requests.get(
				"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-alauddinmansour.json").json()
			for i in tarjimaurl['quran']:
				if i['chapter'] == int(n) and i['verse'] == int(m):
					t = f"{i['text']}"
					await message.answer(f"{ayah['text']} \n\n {t}", reply_markup=bekor)
					await message.answer_audio(ayah['audio'], reply_markup=bekor)
		else:
			await message.answer('Siz izlagan oyat topilmadi. Sura yoki oyat nomerini qayta tekshiring.',
								 reply_markup=bekor)
	else:
		await message.answer("Sura raqamini notoʻgʻri kiritdingiz. Suralar 114 ta.")


if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)
