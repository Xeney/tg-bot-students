### README для проекта "Kash-Bot"

### Описание

Kash-Bot — это Telegram-бот, предназначенный для управления списком студентов. С помощью этого бота пользователи могут добавлять, удалять и просматривать студентов, а также получать справочную информацию по доступным командам.

### Установка

### Требования

- Python 3.7 или выше

- Библиотеки:

- python-telegram-bot

- logging

### Установка зависимостей

Для установки необходимых библиотек используйте pip:

```
pip install python-telegram-bot
```

### Настройка

- Создайте новый бот в Telegram через BotFather и получите токен вашего бота.

- В файле с кодом замените строку:

```
TOKEN = "TOKEN"
```

на ваш токен.

### Использование

### Запуск бота

Чтобы запустить бота, выполните следующий код:

```
python main.py
```

### Доступные команды

Вот список команд, доступных для использования в боте:
- /start - приветственное сообщение с информацией о командах.

- /help - список доступных команд.

- /add  - добавление студента в список.

- /remove  - удаление студента из списка.

- /list - просмотр списка студентов.

### Примеры команд

- Чтобы добавить студента:

```
/add Иван
```
- Чтобы удалить студента:

```
/remove Иван
```
- Чтобы просмотреть список студентов:

```
/list
```

### Обработка текстовых сообщений

Если пользователь отправит любое текстовое сообщение, которое не является командой, бот ответит, что не понял это сообщение, и предложит использовать команду /help.

### Логи

Все действия бота будут записываться в файл info.log для дальнейшего анализа.

### Лицензия

Этот проект открыт под лицензией MIT. Пожалуйста, обратитесь к файлу LICENSE для более подробной информации.
