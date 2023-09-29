from PyQt5.QtCore import QTime
win_x, win_y = 200, 100
win_width, win_height = 1000, 600

txt_hello = 'Добро пожаловать в программу по определению состояния здоровья!'
txt_next = 'Начать'
txt_instruction = ('Данное приложение позволит Вам по тесту Руфье провести первичную диагностику вашего здоровья.\n'
'Проба руфье представляет собой  нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.\n'
'У испытуемого, находящегостя в положении лёжа на спине в течение 5 мин, определяют частоту пульса за 15 секунд;\n'
'затем в течение 45 секунд испутемый выполняет 30 приседаний.\n'
'После окончания нагрузки испытуемы ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд,\n'
'а потом - за последние 15 секунд первой минуты периода востановления.\n'
'Важно! Если в процессе выполнения испытания вы почувствуете себя плохо (появится головокружение, шум в \n'
'ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.') 
txt_title = 'Здоровье'
txt_name = 'Введите Ф.И.'
txt_hintname = "Ф.И."
txt_hintage = "0"
txt_test1 = 'Лягте на спину и замерьте пульс за 15 секунд. Нажмите на кнопку "Начать первый тест", чтобы запустить таймер.\nРезультат запишите в соответствующее поле.'
txt_test2 = 'Выполните 30 приседаний за 45 секунд. Для этого нажмите на кнопку "Начать делать приседания",\nчтобы запустить счётчик приседаний.'
txt_test3 = ''' Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд. \n нажмите кнопку
секунды без замера пульсаций. Результаты запишите в соответствующие поля.'''
txt_sendresults = 'Отправить результаты'
txt_sendresults1 = 'Измерить пульс'
txt_sendresults2 = 'Начать делать приседания'
txt_sendresults3 = 'Измерить пульс (по правилу)'
txt_hinttest1 = '0'
txt_hinttest2 = '0'
txt_hinttest3 = '0'
txt_starttest1 = 'Начать первый тест'
txt_starttest2 = 'Начать делать приседания'
txt_starttest3 = 'Начать финальный тест'
time = QTime(0, 0, 15)
txt_timer = time.toString("hh:mm:ss")
txt_age = 'Полных лет:'
txt_finalwin = 'Результаты'
txt_index = 'Индекс Руфье:'
txt_workheart = 'Работоспособность сердца:'
txt_res1 = "низкая. Срочно обратитесь к врачу!"
txt_res2 = "удовлетворительная. Желатильно проконсультируйтесь у врача."
txt_res3 = "средняя. Возможно, Вам стоит обследоваться у врача"
txt_res4 = "выше среднего. У вас всё отлично, Вы не нуждатесь в консультации врача" 
txt_res5 = "высокая. Вы полностью здоровы."