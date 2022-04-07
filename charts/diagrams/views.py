import random

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from random import randint


# Create your views here.

def index(request):
    # выручка
    labels_gain = ['2018', '2019']
    data_gain = [589, 627]

    # расходы
    labels_cost = ['2018', '2019']
    data_cost = [515, 545]

    # финансовый результат
    labels_fin_res = ['2018', '2019']
    data_fin_res = [73, 82]

    # рентабельность
    labels_rent = ['2018', '2019']
    data_rent = [12, 13]

    # график по грузам
    data_cargo_gain = [99.9, 4.6, 132.7, 24.3, 52.1, 17.4, 26.9, 20.3, 9.9, 87.2, 151.9]
    data_cargo_cost = [121.3, 3.6, 64.1, 22.9, 21.1, 16.4, 36.6, 14.8, 8.5, 55.4, 180.5]
    labels_cargo = ['Уголь каменный', 'Кокс', 'Нефтяные грузы', 'Руды', 'Черные металлы', 'Лесные грузы',
                    'Минерально-строительные', 'Удобрения', 'Холебные грузы', 'Прочие грузы', 'Грузы на своих осях']

    data_line = [-21.6, 1.0, 68.5, 1.4, 31.0, 1.1, -9.7, 5.6, 1.5, 31.8, -28.6]
    data_line_1 = []
    cord = 0
    for iter in data_line:
        cord = cord + iter
        data_line_1.append(round(cord, 2))

    # Факторы изменения выручки и расходов по всем категориям грузов
    data_gain_all_1 = [0, 588.7, 595, 630, 0]
    data_gain_all_2 = [588.7, 5, 120, 240, 870]
    labels_gain_all = ['2018', '', '', '', '2019']

    data_cost_all_1 = [0, 515.3, 535.3, 550, 550, 0]
    data_cost_all_2 = [515.3, 20, 100, 80, 200, 545]
    labels_cost_all = ['2018', '', '', '', '', '2019']

    polar_area_data = [452, 321, 241, 161, 154, 151, 142, 141, 134, 131]
    polar_area_data2 = [654, 697, 778, 803, 829, 863, 1144, 1287, 1359, 1373]
    labels_polar_area = ['Зауралье-Малорефтинская', 'Белово-Магнитогорск-Гр', 'Карталы 1-Соловей', 'Ерунаково-Соловей',
                         'Томусинская-Металлургическая', 'Прокопьевск-Магнитогорск-Гр.', 'Бирюлинская-Магнитогорск-Гр.',
                         'Заозерная-Жеребцово', 'Новокузнецк-Северный-Смычка', 'Междуреченск-Смычка',
                         'Чегдомын-Ванино']
    labels_polar_area2 = ['Ерунаково-Находка-Восточная', 'Байкаим-Ванино', 'Мереть-Находка-Восточная',
                          'Мульда-Череповец II', 'Ленинск-Кузнецкий II-Ванино ', 'Камышта - Ванино',
                          'Терентьевская-Ванино', 'Ленинск-Кузнецкий I-Ванино', 'Черногорские Копи -Ванино']

    fill_line_area_g = [1687, 2072, 1933, 1681, 1568, 1537, 1242, 1199, 1146, 1144]
    fill_line_area_o = [2761, 2432, 2736, 2377, 1939, 1854, 1658, 1170, 985, 1078]
    labels_fill_line_area = ['Ерунаково-Лужская', 'Междуреченск-Находка', 'Мереть-Находка-Восточная',
                             'Ерунаково-Находка-Восточная', 'Челутай-Ванино', 'Ерунаково -Мурманск ',
                             'Камышта-Находка-Восточная',
                             'Терентьевская-Рудня', 'Ерунаково-Соловей', 'Карталы I -Лужская']

    dynamic_bar_data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200,
                        210, 220, 230, 240, 250, 260, 270, 280, 290, 300]
    labels_dynamic_bar_data = ['Ноглики -Победино-Сахалинское', 'Ильинск-Сахалинский -Холмск',
                               'Победино-Сахалинское - Заозерное-Сахалин',
                               'Южно-Сахалинск -Взморье', 'Харанор -Приаргунск -Краснокаменск',
                               'Карпогоры -Архангельск-Гор.',
                               'Новочугуевка - Сибирцево', 'Заполярная -Кола', 'Охочевка -Кшень - О.п. 147 км',
                               'Взморье -Заозерное-Сахалинское', 'Муром - Ковров-Грузовой',
                               'Балашов-Пассажирский -Тамбов I',
                               'Бобрик Донской -Павелец-Сызранский -Ря', 'Орск-Сортировочный -Рудный Клад',
                               'Копытцево - Износки -Вязьма-Брянская',
                               'Каменногорск - Хийтола', 'Исакогорка -Северодвинск -Ненокса', 'Кузино -Калино',
                               'Микунь -Вендинга',
                               'Осолодино -Татарская', 'Готня -Белгород-Сумской', 'Галич -Кострома-Новая',
                               'Ледмозеро -Суккозеро',
                               'Сретенск -Куэнга', 'Ваенга -Мурманск', 'Белый Яр -Асино', 'Дунай -Смоляниново',
                               'Буденновск I -Благодарное',
                               'Корсаков -Южно-Сахалинск', 'Советск -Кутузово-Новое']
    don_data = [524, 329, 165, 150, 132, 514, 260, 163, 147, 130, 419, 230, 163]
    don_lable = ['Ноглики - Победино-Сахалинское', 'Ильинск-Сахалинский - Холмск',
                 'Победино-Сахалинское - Заозерное-Сахалин', 'Южно-Сахалинск - Взморье',
                 'Харанор - Приаргунск - Краснокаменск', 'Карпогоры - Архангельск-Гор.',
                 'Новочугуевка - Сибирцево', 'Заполярная - Кола', 'Охочевка - Кшень - О.п. 147 км',
                 'Взморье - Заозерное-Сахалинское']

    tab_iter = 1
    table = []
    while tab_iter <= 1000:
        table.append({'col1': random.choice(labels_dynamic_bar_data), 'col2': random.choice(labels_dynamic_bar_data),
                      'col3': random.choice(labels_dynamic_bar_data), 'col4': tab_iter})
        tab_iter = tab_iter + 1

    return render(request, 'diagrams/index.html', {'labels_gain': labels_gain,
                                                   'data_gain': data_gain,
                                                   'labels_cost': labels_cost,
                                                   'data_cost': data_cost,
                                                   'labels_fin_res': labels_fin_res,
                                                   'data_fin_res': data_fin_res,
                                                   'labels_rent': labels_rent,
                                                   'data_rent': data_rent,
                                                   'data_cargo_gain': data_cargo_gain,
                                                   'data_cargo_cost': data_cargo_cost,
                                                   'labels_cargo': labels_cargo,
                                                   'data_line': data_line_1,
                                                   'data_gain_all_1': data_gain_all_1,
                                                   'data_gain_all_2': data_gain_all_2,
                                                   'labels_gain_all': labels_gain_all,
                                                   'data_cost_all_1': data_cost_all_1,
                                                   'data_cost_all_2': data_cost_all_2,
                                                   'labels_cost_all': labels_cost_all,
                                                   'polar_area_data': polar_area_data,
                                                   'labels_polar_area': labels_polar_area,
                                                   'polar_area_data2': polar_area_data2,
                                                   'labels_polar_area2': labels_polar_area2,
                                                   'fill_line_area_g': fill_line_area_g,
                                                   'fill_line_area_o': fill_line_area_o,
                                                   'labels_fill_line_area': labels_fill_line_area,
                                                   'dynamic_bar_data': dynamic_bar_data,
                                                   'labels_dynamic_bar_data': labels_dynamic_bar_data,
                                                   'don_data': don_data,
                                                   'don_lable': don_lable,
                                                   'table': table
                                                   })


def update_data(request):
    ajax_data = []
    iterator = 30
    while iterator >= 0:
        ajax_data.append(randint(1, 1000))
        iterator -= 1

    response = {'ajax_data': ajax_data}
    return JsonResponse(response)


def update_color(request):
    ajax_color = []
    iterator = 30
    while iterator >= 0:
        RGB = 'rgb(' + str(randint(1, 255)) + ',' + str(randint(1, 255)) + ',' + str(randint(1, 255)) + ')'
        ajax_color.append(RGB)
        iterator -= 1

    response = {'ajax_color': ajax_color}
    return JsonResponse(response)


def data_table(request):
    print('OK')
    ajax_table = {

    }

    response = {'ajax_color': ajax_table}
    return JsonResponse(response)
