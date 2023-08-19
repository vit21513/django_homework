from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page visit')
    # лог выыодится  одновремеено в консоль и файл
    return HttpResponse("""<div align="center"><h1><font color="blue">Это главная страница</font>
                         </h1>  <p><h3>Она демонстрирует возможности фреймворка Джанго 
                        'из коробки' рабочий сайт всего лишь за пару строк </h3></p>
                        <font color="red"<h5>2023 год </h5></font></div>""")


def about(request):
    logger.info('about page visit')
    return HttpResponse("""<div align="center"><h1> Cтраница О нас </h1> <p><h3>Мы сами мало что знаем о нас </h3></p>
                         <p><h4> По этому здесь ничего нет  </h4></p></div>""")
