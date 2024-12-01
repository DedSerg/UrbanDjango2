from django.shortcuts import render

# Create your views here.
def platform_view(request):
    return render(request, 'platform.html')


def games_view(request, name_game=None, main_page=None):

    game_numer_1 = 'Скандинавский бой'
    game_numer_2 = 'Каркассон'
    game_numer_3 = 'Бэнг!'

    games = [game_numer_1, game_numer_2, game_numer_3]

    context = {
        'main_page': main_page,
        'name_game': games,

    }
    return render(request, 'games.html', context)


def cart_view(request):
    return render(request, 'cart.html')