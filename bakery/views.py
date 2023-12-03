from django.contrib.auth import authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Bakery
from django.contrib import messages
from django.db.models import Q
from users.models import User
from .forms import BakeryWriteForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils import timezone
from users.decorators import *


class BakeryListView(ListView):
    model = Bakery
    paginate_by = 5
    template_name = 'bakery/bakery_list.html'  # DEFAULT : <app_label>/</model_name>_list.html
    context_object_name = 'bakery_list'        # DEFAULT : <model_name>_list

    def get_queryset(self):
        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get('type', '')
        bakery_list = Bakery.objects.order_by('-id')

        if search_keyword:
            if len(search_keyword) > 1:
                if search_type == 'all':
                    search_bakery_list = bakery_list.filter(
                        Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword) | Q(
                            writer__user_id__icontains=search_keyword))
                elif search_type == 'title_content':
                    search_bakery_list = bakery_list.filter(
                        Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword))
                elif search_type == 'title':
                    search_bakery_list = bakery_list.filter(title__icontains=search_keyword)
                elif search_type == 'content':
                    search_bakery_list = bakery_list.filter(content__icontains=search_keyword)
                elif search_type == 'writer':
                    search_bakery_list = bakery_list.filter(writer__user_id__icontains=search_keyword)

                return search_bakery_list
            else:
                messages.error(self.request, '검색어는 2글자 이상 입력해주세요.')
        return bakery_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get('type', '')

        if len(search_keyword) > 1:
            context['q'] = search_keyword
        context['type'] = search_type

        return context


def bakery_detail_view(request, pk):
    bakery = Bakery.objects.get(pk=pk)
    context = {
        'bakery': bakery,
    }

    return render(request, 'bakery/bakery_detail.html', context)

"""
@login_required
def bakery_detail_view(request, pk):
    bakery = get_object_or_404(Bakery, pk=pk)

    if request.user == review.writer:
        review_auth = True
    else:
        review_auth = False

    context = {
        'bakery': bakery,
        'bakery_auth': bakery_auth,
    }
    return render(request, 'bakery/bakery_detail.html', context)
"""

@login_required
@admin_required
def bakery_register_view(request):
    if request.method == "POST":
        name = request.POST['name']
        info = request.POST['info']
        hp = request.POST['hp']
        operated_date = request.POST['operated_date']
        address = request.POST['address']
#        form = BakeryWriteForm(request.POST)
#        user = request.session['user_id']
#        user_id = User.objects.get(user_id=user)

        bakery = Bakery.objects.create (
            name = name,
            info = info,
            hp = hp,
            operated_date = operated_date,
            address = address
        )

#        if form.is_valid():
#            review = form.save(commit=False)
#            review.writer = user_id
#            review.save()
        return redirect('bakery:bakery_list')
    else:
#        form = BakeryWriteForm()
        return render(request, 'bakery/bakery_register.html')


@login_required
@admin_required
def bakery_edit_view(request, pk):
    bakery = Bakery.objects.get(id=pk)

    if request.method == 'POST':
        if request.user.level == '1':
            form = BakeryWriteForm(request.POST, instance=bakery)
            if form.is_valid():
                bakery = form.save(commit=False)
                bakery.save()
                messages.success(request, "수정되었습니다.")
                return redirect('/bakery/'+str(pk))
    else:
        bakery = Bakery.objects.get(id=pk)
        if request.user.level == '1':
            form = BakeryWriteForm(instance=bakery)
            context = {
                'form': form,
                'edit': '수정하기',
            }
            return render(request, 'bakery/bakery_register.html', context)
        else:
            messages.error(request, "본인 게시글이 아닙니다.")
            return redirect('/bakery/'+str(pk))


@login_required
@admin_required
def bakery_delete_view(request, pk):
    bakery = Bakery.objects.get(id=pk)
    if request.user.level == '1':
        bakery.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('/bakery/')
    else:
        messages.error(request, "본인 게시글이 아닙니다.")
        return redirect('/bakery/' + str(pk))
