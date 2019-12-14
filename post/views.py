from django.shortcuts import render
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Boardtbl
from django.contrib.auth.models import User
from django.http import JsonResponse
import math


def index(request):
    posts = Boardtbl.objects.all().order_by('-id')
    paginator = Paginator(posts, 15)
    page = request.GET.get('page')

    if not page:
        page = 1

    contents = paginator.get_page(page)
    page_range = 5
    current_block = math.ceil(int(page) / page_range)
    start_block = (current_block - 1) * page_range
    end_block = start_block + page_range
    page_data = paginator.page_range[start_block:end_block]

    if int(current_block) == int(1):
        prev_page = 1
    else:
        prev_page = (current_block - int(1)) * int(page_range)

    context = {'contents': contents, 'page_data': page_data,
               'next_page': paginator.num_pages if paginator.num_pages < end_block + int(1) else end_block + int(1),
               'prev_page': prev_page}

    return render(request, 'index.html', context)


def content(request, id):
    board_content = Boardtbl.objects.filter(id=id)
    context = {'board_content': board_content}
    return render(request, 'content.html', context)


def writeform(request):
    return render(request, 'writeform.html')


def write(request):
    board_data = Boardtbl(title=request.POST.get('title'), content=request.POST.get('content'),
                          insert_id=User.objects.get(id='1'), insert_date=timezone.now())
    board_data.save()
    context = {'rtn': 'success'}
    return JsonResponse(context)
