import tkinter as tk # імпорт модуля для графічного інтерфейсу користувача (gui)
from datetime import datetime # імпорт модуля для роботи з датою
from dateutil.relativedelta import relativedelta # сторонній модуль для роботи з часом
                                         # relativedelta коректно віднімає одну дату від іншої




# функція що виконує основні обчислення на основі введених користувачем данних і поточним часом
def calc_date():
    global running # робить змінну "running" глобальною тобто її можна змінити всередині функції а також вона є тою самою змінною що і в основному блоку
    if not running: # running maє початкове значення "False"; ця умова перевіряє чи running має значення "False"
        return ''' взагалі хз що робить але без неї працює '''
    birthday = datetime(int(year_entry.get()), int(month_entry.get()), int(day_entry.get())) # змінна birthday має тип данний datetime приймає значення з рядків tk.Entry(root)
    years = relativedelta(years=int(end_entry.get())) # years є типом elativedelta і приймає значення з рядків tk.Entry(root) я використаю цю змінну потім щою коректно додати роки до birthday

    deadhday = birthday + years # кінцева дата що є сумою дати народження і років які користувач планує прожити

    current_time = datetime.now() # присвоїмо змінній current_time поточний час
    remaining = relativedelta(deadhday, current_time) # віднімаємо від кінцевої дати поточний час щоб дізнатись скільки часу лишилось і присвоюємо це значення змінній remaining

    remaining1 = deadhday - current_time # relativedelta(deadhday, current_time) дає більш точну різницю а remaining = deadhday - current_time різницю в днях
    remaining2 = remaining1.days * 24 + remaining1.seconds // 3600 # щоб дізнитися скільки годин лишилося ми множимо дні на 24 і додаємо добуток секунд на 3600 без залишку
    remaining3 = remaining1.total_seconds() # переводимо в секунди remaining1 за допомогою меетоду total_seconds()
    remaining3 = int(remaining3) # переводимо секунди в звичайне число

# метод .set встановить в змінну label_text значення з f-рядка
    label_text.set(f"{remaining.years} років, {remaining.months} місяців, {remaining.days} днів, {remaining.hours} годин, {remaining.minutes} хвилин, {remaining.seconds} секунд,")


    label2_text.set(f"{remaining1.days:,} днів")
    label3_text.set(f"{remaining2:,} годин")
    label4_text.set(f"{remaining3:,} секунд")

    root.after(1000, calc_date) # функція буде викликати себе кожну секунду
                        # вона викликається навіть якщо running == False але нічого не робить

# функція реалізує зберігання данних що ввів користувач в файл config
def save():
    global year_entry, month_entry, day_entry, end_entry # оголосимо глобальні змінні що ввів користувач з допомогою поля tk.Entry(root)
    with open('config.txt', 'w') as f: # відкриває файл config.txt в режимі запису 'w', якщо в файлі є дані їх буде перезаписано, якщо немає файла, його буде створено. f дає доступ на редагування
        # додаємо в файл year_entry, month_entry, day_entry, end_entry
        f.write(year_entry.get() + '\n')
        f.write(month_entry.get() + '\n')
        f.write(day_entry.get() + '\n')
        f.write(end_entry.get() + '\n')



# Функція, яка згортає/розгортає всі віджети в списку widgets_to_toggle
def toggle_widgets():
    global running
    if running: # якщо running == True
        running = False
        fold_button.config(text="Обчислити")  # .config() метод що дозволяє змінювати атрибути віджета
        root.geometry("400x350") # змінемо розмір вікна
    else:
        running = True
        fold_button.config(text="Налаштувати")
        root.geometry("400x120")
        calc_date()

    for widget in widgets_to_toggle: # widget це кожен віджет з списку widgets_to_toggle
        if widget.winfo_manager() == "": # метод winfo_manager() перевіряє чи віджет відображається повертає ім'я менеджера геометрії віджета; якщо він не відображений, то ім'я менеджера геометрії буде порожнім рядком
            widget.pack() #Якщо віджет не відображений, то він буде відображений за допомогою методу pack()
        else:
            widget.pack_forget() #Інакше віджет буде прибраний за допомогою методу pack_forget()







try:
    running = False # використовується в def calc_date() і def toggle_widgets()

    root = tk.Tk() # створимо об'єкт Tk(), що є головним вікном
    root.geometry("400x120+300+50") # налаштуємо розмір і відступ від краю екрану
    root.title("memento_mori") # встановимо заголовок

    photo =tk.PhotoImage(file="Pixilart - Minecraft Skeleton by LinkinTheChainz.png") # cтворимо об'єкт PhotoImage з картинки
    root.iconphoto(False, photo) # встановимо іконку False вказує, що це не мініатюрна іконка, а другий аргумент photo передає саму іконку. Тобто, коли вікно програми буде відображатися в панелі завдань або на панелі задач вашої операційної системи, то буде відображено зазначену іконку

    # Створити список, в якому будуть зберігатися всі віджети, що будуть згортатися/розгортатися
    widgets_to_toggle = []

    # Кнопка, яка згортає/розгортає всі віджети в списку widgets_to_toggle
    fold_button = tk.Button(root, text="налаштування", command=toggle_widgets)
    fold_button.pack()










    year_label = tk.Label(root, text="Рік") # Віджет-мітка використовується для відображення текстової інформації в графічному інтерфейсі користувача
    year_label.pack() # Ця команда використовується для розміщення (пакування) віджета
    year_entry = tk.Entry(root) #створює віджет для введення тексту. Введені дані користувача можуть бути використані для обчислення часу до події
    year_entry.pack()
    '''widgets_to_toggle це список, в якому зберігаються всі віджети, які потрібно згортати/розгортати при натисканні на кнопку "Налаштувати"/"Обчислити".

year_label - це Label, який містить текст "Рік".
Запис widgets_to_toggle.append(year_label) додає year_label до списку widgets_to_toggle, щоб згодом згортати/розгортати його разом з іншими віджетами.'''

    widgets_to_toggle.append(year_label)
    widgets_to_toggle.append(year_entry)

    '''Цей код відкриває файл config.txt у режимі читання і зчитує всі рядки в змінну lines.
Далі з першого рядка отримується рік та вставляється в поле year_entry за допомогою методу insert() з параметрами 0 (позиція для вставки) та зчитаного року.
Метод strip() видаляє зайві пробіли з початку та кінця рядку. Рядок зчитується за допомогою методу readlines(), який повертає список рядків, що міститься у файлі.'''
    with open('config.txt', 'r') as f:
        lines = f.readlines()
        year = lines[0].strip()
        year_entry.insert(0, year)


    month_label = tk.Label(root, text="Місяць")
    month_label.pack()
    month_entry = tk.Entry(root)
    month_entry.pack()
    widgets_to_toggle.append(month_label)
    widgets_to_toggle.append(month_entry)
    with open('config.txt', 'r') as f:
        lines = f.readlines()
        month = lines[1].strip()
        month_entry.insert(0, month)

    day_label = tk.Label(root, text="День")
    day_label.pack()
    day_entry = tk.Entry(root)
    day_entry.pack()
    widgets_to_toggle.append(day_label)
    widgets_to_toggle.append(day_entry)
    with open('config.txt', 'r') as f:
        lines = f.readlines()
        day = lines[2].strip()
        day_entry.insert(0, day)

    end_label = tk.Label(root, text="Скільки років плануєте прожити")
    end_label.pack()
    end_entry = tk.Entry(root)
    end_entry.pack()
    widgets_to_toggle.append(end_label)
    widgets_to_toggle.append(end_entry)
    with open('config.txt', 'r') as f:
        lines = f.readlines()
        end = lines[3].strip()
        end_entry.insert(0, end)

    warning = tk.Label(root, text='''Будьте обережні з неправильними датами
    якщо виникне помилка, будуть повернуті налаштування
     за замовчуванням після перезапуску програми''')
    warning.pack()
    widgets_to_toggle.append(warning)

    save_button = tk.Button(root, text="Зберегти", command=save)
    save_button.pack()
    widgets_to_toggle.append(save_button)




#Цей код створює мітку (label) у головному вікні програми (root), яка буде відображати текст, встановлений у змінну label_text.

#tk.StringVar() - це клас для зберігання рядків, які можуть змінюватись. В даному випадку, змінна label_text є екземпляром цього класу і містить порожній рядок в початковий момент часу (label_text.set("")).

#tk.Label() - це клас для створення міток у Tkinter. Перший аргумент цього класу (root в даному випадку) вказує на те, у якому вікні мітка буде розміщена. Другий аргумент (textvariable=label_text) вказує на те, яку змінну слід використовувати для відображення тексту мітки. Після створення мітки вона додається до головного вікна методом .pack().
    label_text = tk.StringVar()
    label_text.set("")
    label = tk.Label(root, textvariable=label_text)
    label.pack()

    label2_text = tk.StringVar()
    label2_text.set("")
    label2 = tk.Label(root, textvariable=label2_text)
    label2.pack()

    label3_text = tk.StringVar()
    label3_text.set("")
    label3 = tk.Label(root, textvariable=label3_text)
    label3.pack()

    label4_text = tk.StringVar()
    label4_text.set("")
    label4 = tk.Label(root, textvariable=label4_text)
    label4.pack()

    toggle_widgets() # програма запуститься з згорнутими віджетами
    root.mainloop()
except:
    with open('config.txt', 'w') as f:
        f.write('') # якщо виникне помилка ми очистимо config
    with open('config.txt', 'r') as f:
        content = f.read()
        if not content: # якщо файл порожній
            print("Файл порожній, або неправильна дата.")
            print("Повернено налаштування за замовчуванням")

            with open('config.txt', 'w') as f: # ми запишемо в нього стандартні значення
                f.write("2000" + '\n')
                f.write("1" + '\n')
                f.write("1" + '\n')
                f.write("70")

