from django.shortcuts import render
import math
from django.core.paginator import Paginator
from .models import Boardtbl


# Create your views here.

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
