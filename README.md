<div align="center">
<img src="logo.png" height="450" width="700"></img>
</div>

# J.a.r.v.i.s - 0.7.0 ru.
###### Python tilida ishlab chiqarilgan.

 -`Salom mening ismim Akrom bu loyihani ishlash uchun juda kop vaqtim ketkan va nixoyat men uni omaga xavola qilishga qaror qildim
 kop funcsiyali "Ovozli yordamchi" yani Jarvis toliq tayor boldi men oylashimcha albata unu yana takomilashtirsa boladi bunda lekin
 sizlarning ham yordamlaringiz kerak boladi agar shu loyixa 20 🤩 yuldiz yigsa albata keyingi versiyasini chiqarishga harakat qilaman 
 va undan oldingi versiyalarini ham omaga tahdim qilaman bu loyiha faqat Python dasturlash tilida yozilgan agar sizda Python ornatilmanag 
 bolsa uni ornatip oling bolmasam proektni ishga tushirishingiz qiyinlaship ketishi munkin 😊 agar siz Python dasturlash tili boyicha va 
 eng zor 'Django', 'Flask', 'FastApi', 'FastUi' va shunga ohshash frameworlar undan tashqari dasturlashga oyid boshqa bilimlarga ega bolishni 
 istasangiz unda mening shahsiy telegram kanalimga obuna boling:
 "`-
### Akrom / Blog -- (https://t.me/+4Ta1Q9nao-g2ZWFi) 

##### Ustunliklar:
-`Online va offline ovozni micraphondan oqip olish kop funksilar ishtiroki, sozlanuvchanlik, kompyuterni boshqarish, ikki hil ovoz 1 defaul audio orqali ikkinchisi 
kompyuter operatsion sistemasidagi rus tilida matini ovozga aylantirish, brauzer orqali sorovlar jonatish va shunga ohshash boshqa funksiyalar`-

---

## Ishga tushirish:
#### Eslatma: 
Proekt faqat Windows operatsion sistemasi ga moslashtirilgan.

---

#### Proekt ichida '.env' nomli fayil yarating va uning ichiga quyidagi sozlamalarni joylang:
~~~python
TELEGRAM_DIR = "your telegram path"
YOUTUBE_DIR = "your YouTube path"
GOOGLE_DIR = "C:/Program Files (x86)/Google/Chrome/Application/chrome" # example
BROWSER_DIR = "your browser path"
MUSICS_DIR = "your music files dir"
~~~
#### Modularni ornatish. Terminalni ochip quyidagi kbuyruqlarni kiriting:
###### modular ogir bolishi munkin shu sabapli biroz kutishiz munkin.
~~~shell
pip install --upgrade pip 
pip install -r requirements.txt
~~~
#### Asosiy fayilni ishga tushirish:
~~~shell
python main.py
~~~
-`Agar siz barchasini togri qilgan bolsangiz hamasi ishga tushishi kerak noboda ishga tushira olmagan bolsangiz biz bilan 
boglansangiz boladi sizga jovob berishmagan bolsak demak sizni habarizni hali oqishmagan yoki ichtimoyiy tarmoq bilan muamoga 
duch kelgan bolishimiz munkin albata bizni togri tushinasiz degan umitaman.`-

#### Telegram - (https://t.me/RustamovAkrom2007)
#### Sozlamalar:
###### Eslatip otama sozlamar (settings.py) joyida Jarvis(ovozli yordamchingizni) ozizga moslashtirip olishingiz munkin.

~~~python
# settings.py
...
ASISTENT_NAMES = ("джарвис", "чарльз") # Activlashtiradigan soz:
...
~~~
#### Ovozli buyruqlar yaml fayli:
~~~yaml
music: # musikani yoqadi
  - давай музыку
  - музыка
  - яндекс музыка
  - включи музыку
  - открой музыку
  - послушаем музыку
  - хочу музыку
  - врубай музло
  - включи что-то послушать
  - давай что-то послушаем
  - поставь музыку
  - 
music_next: # Keyingi musika
  - следующий трек
  - следующая мелодия
  - следующая песня
  - переключи трек
  - переключи музыку
  - переключи мелодию
  - переключи песню
  - следующая музыка
  - 
music_off: # musikani ochirish
  - выключи музыку
  - отруби музыку
  - убери музыку
  - отключи музыку
  - закрой музыку
  - останови музыку
  - хватит музыки
  - 
music_prev: # Oldingi musika
  - предыдущая музыка
  - предыдущий трек
  - предыдущая мелодия
  - предыдущая песня
  - верни трек
  - верни мелодию
  - верни песню
  - верни прошлый трек
  - верни прошлую мелодию
  - верни прошлую песню
  - верни прошлую музыку
  - верни то что играло
  - давай предыдущий трек
  - переключи музыку обратно
  - переключи на прошлый трек
  - переключи на прошлую мелодию
  - переключи на прошлую песню
  - 
'off': # Programani toxtatish
  - выключись
  - вырубись
  - завершить работу
  - закройся
  - отключись
  - заверши свою работу
  - на сегодня хватит
  - выгрузи себя из памяти
  - ты мне надоел
  - пора спать
  - 
open_browser: # Browserni ochish
  - открой браузер
  - запусти браузер
  - открой гугл хром
  - гугл хром
  - 
open_google: # Googleni ochis
  - открой гугл
  - гугл
  - запусти гугл
  - 
open_youtube: # YouTubeni ochis
  - открой ютуб
  - ютуб
  - запусти ютуб
  - 
open_telegram: # Telegramni ochis
  - открой telegram
  - зайди в telegram
  - в телеграмме
  - 
sound_off: # Ovoxzni ochirish
  - выключи звук
  - беззвучный режим
  - режим без звука
  - отключи звук
  - 
sound_on: # Ovozni yoqish
  - включи звук
  - режим со звуком
  - верни звук
  - 
sound_min: # Ovozni pasaytirish
  - звук на минимум
  - громкость на минимум
  - убавь звук
  - сделай потише
  - убавь громоксть
  - поставь звук на минимум
  - поставь громкость на минимум
  - установи звук на минимум
  - установи громкость на минимум
  - минимальный уровень громкости
  - 
sound_max: # Ovozni kotarish
  - звук сто
  - громкость сто
  - поставь звук на сто
  - поставь громкость на сто
  - установи звук на сто
  - установи громкость на сто
  - громкость на максимум
  - установи громкость на максимум
  - звук на максимум
  - полная громкость
  - полный уровень громкости
  - 
sound_50: # Ovoz meyorida
  - звук пятьдесят
  - громкость пятьдесят
  - поставь звук на пятьдесят
  - поставь громкость на пятьдесят
  - установи звук на пятьдесят
  - установи громкость на пятьдесят
  - громкость на середину
  - средний уровень громкости
  - поставь звук на середину
  - установи громкость на середину
  - средний уровень громкости

stupid: # Kamsitish
  - ты дурак
  - ты дебил
  - ты глупый
  - ты тупой
  - ты безмозглый
  - ты плохой
  - хотя ты дурак
  - 
thanks: # Maqtash
  - спасибо
  - молодец
  - респект
  - ты супер
  - отличная работа
  - ты крут
  - ты большой молодец
  - ты реально крут
  - ты афигенный
  - ты хороший
  - хотя ты молодец
screenshot: # Ekrani rasimga olish
  - ahk_path: Asistent/ahk\screenshot.exe
  - сделай скриншот
  - сделай снимок экрана
  - сними экран
blocking: # Kompyuterni bloklash
  - ahk_path: Asistent/ahk\blocking.exe
  - заблокируй компьютер
  - заблокируй комп
sleep: # Kompyuterni ochirish
  - ahk_path: Asistent/ahk\sleep.exe
  - спящий режим
  - ждущий режим
  - иди поспи
empty_trash: # Korzinkani tozalash
  - ahk_path: Asistent/ahk\empty_trash.exe
  - очисти корзину
  - почисти корзину
  - очистка корзины
clipboard: # Bufer obmeni ochish
  - ahk_path: Asistent/ahk\clipboard.exe
  - открой буфер обмена
  - покажи буфер обмена
  - запусти буфер обмена
  - буфер обмена
set_language: # Tilni ozgartirish
  - ahk_path: Asistent/ahk\set_language.exe
  - измени язык
  - смени раскладку
  - поменяй раскладку
  - смени язык
  - поменяй язык
  - переключи на русский
  - переключи на английский
  - смени раскладку на русскую
  - поменяй раскладку на русскую
  - поменяй раскладку на английскую
  - смени раскладку на английскую
  - смени язык на русский
  - поменяй язык на русский
  - смени язык на английский
  - поменяй язык на английский
rool_up_windows: # Hamma oynalarni kozdan yopish
  - ahk_path: Asistent/ahk\roll_up_windows.exe
  - сверни все окна
  - сверни окна
task_manager_open: # Dispetcherni ochish
  - ahk_path: Asistent/ahk\task_manager_open.exe
  - запусти диспетчер задач
  - открой диспетчер задач
  - диспетчер задач

~~~

---
