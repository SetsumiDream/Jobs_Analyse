from django.shortcuts import render


def test(request):
    return render(request, 'travel/从近到远.html')


def near_to_far(request):
    return render(request, 'travel/从近到远.html')


def cheap_to_expensive(request):
    return render(request, 'travel/价格从低到高.html')


def expensive_to_cheap(request):
    return render(request, 'travel/价格从高到低.html')


def common_more_to_less(request):
    return render(request, 'travel/评论从高到低.html')


def detail(request):
    return render(request, 'travel/详情页数据.html')


def smart_sort(request):
    return render(request, 'travel/智能排序.html')


