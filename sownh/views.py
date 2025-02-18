from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Project, Category, News, CategoryNews, CaseCard  # Импортируем модель Project из нашего приложения
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail


# Create your views here.
def index(request):
    all_news = News.objects.all()  # Получаем все новости
    case_cards = CaseCard.objects.all()
    return render(request, 'base.html', {'all_news': all_news, 'case_cards': case_cards} )

def case_detail(request, case_id):
    case = get_object_or_404(CaseCard, pk=case_id)
    return render(request, 'case_detail.html', {'case': case})

def news_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'news_detail.html', {'news': news})


def page2(request):
    categories = Category.objects.all()  # Получаем все категории
    selected_category = request.GET.get('category')  # Получаем выбранную категорию из запроса

    if selected_category:  # Если категория была выбрана
        projects = Project.objects.filter(category__name=selected_category)  # Фильтруем проекты по выбранной категории
    else:
        projects = Project.objects.all()  # Если категория не была выбрана, показываем все проекты

    paginator = Paginator(projects, 3)  # Показывать 5 проектов на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index2.html', {
        'projects': page_obj,
        'categories': categories,
        'selected_category': selected_category,
    })
def page3(request):
    categories = CategoryNews.objects.all()
    selected_category = request.GET.get('category')

    if selected_category:
        filtered_news = News.objects.filter(category__name=selected_category)
    else:
        filtered_news = News.objects.all()

    paginator = Paginator(filtered_news, 4)  # Показывать 5 новостей на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'page3.1.html', {
        'categories': categories,
        'page_obj': page_obj,
        'selected_category': selected_category,
    })

def page4(request):
    return render(request, 'page4.html')


def page5(request):
    return render(request, 'page5.html')




def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']

            # Тело письма
            message = f'Имя: {name}\nНомер телефона: {phone}'

            # Отправка письма
            send_mail(
                'Контактная форма',  # Тема письма
                message,  # Сообщение
                'danilka_1971@mail.ru',  # Отправитель
                ['danilka_1971@mail.ru'],  # Получатель
                fail_silently=False,
            )

            # Перенаправление с параметром success=1
            return redirect('/?success=1')
    else:
        form = ContactForm()

    return render(request, 'base.html', {'form': form})

