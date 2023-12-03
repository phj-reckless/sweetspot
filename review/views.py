from django.contrib.auth import authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Review
from django.contrib import messages
from django.db.models import Q
from users.models import User
from .forms import ReviewWriteForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils import timezone


class ReviewListView(ListView):
    model = Review
    paginate_by = 5
    template_name = 'review/review_list.html'  # DEFAULT : <app_label>/</model_name>_list.html
    context_object_name = 'review_list'        # DEFAULT : <model_name>_list

    def get_queryset(self):
        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get('type', '')
        review_list = Review.objects.order_by('-id')

        if search_keyword:
            if len(search_keyword) > 1:
                if search_type == 'all':
                    search_review_list = review_list.filter(
                        Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword) | Q(
                            writer__user_id__icontains=search_keyword))
                elif search_type == 'title_content':
                    search_review_list = review_list.filter(
                        Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword))
                elif search_type == 'title':
                    search_review_list = review_list.filter(title__icontains=search_keyword)
                elif search_type == 'content':
                    search_review_list = review_list.filter(content__icontains=search_keyword)
                elif search_type == 'writer':
                    search_review_list = review_list.filter(writer__user_id__icontains=search_keyword)

                return search_review_list
            else:
                messages.error(self.request, '검색어는 2글자 이상 입력해주세요.')
        return review_list

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


def review_detail_view(request, pk):
    review = get_object_or_404(Review, pk=pk)

    if request.user == review.writer:
        review_auth = True
    else:
        review_auth = False

    context = {
        'review': review,
        'review_auth': review_auth,
    }
    return render(request, 'review/review_detail.html', context)

@login_required
def review_write_view(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
#        form = ReviewWriteForm(request.POST)
#        user = request.session['user_id']
#        user_id = User.objects.get(user_id=user)

        review = Review.objects.create (
            title = title,
            content = content,
            writer = request.user
        )

#        if form.is_valid():
#            review = form.save(commit=False)
#            review.writer = user_id
#            review.save()
        return redirect('review:review_list')
    else:
#        form = ReviewWriteForm()
        return render(request, 'review/review_write.html')


@login_required
def review_edit_view(request, pk):
    review = Review.objects.get(id=pk)

    if request.method == 'POST':
        if review.writer == request.user or request.user.level == '1':
            form = ReviewWriteForm(request.POST, instance=review)
            if form.is_valid():
                review = form.save(commit=False)
                review.save()
                messages.success(request, "수정되었습니다.")
                return redirect('/review/'+str(pk))
    else:
        review = Review.objects.get(id=pk)
        if review.writer == request.user or request.user.level == '1':
            form = ReviewWriteForm(instance=review)
            context = {
                'form': form,
                'edit': '수정하기',
            }
            return render(request, 'review/review_write.html', context)
        else:
            messages.error(request, "본인 게시글이 아닙니다.")
            return redirect('/review/'+str(pk))


@login_required
def review_delete_view(request, pk):
    review = Review.objects.get(id=pk)
    if review.writer == request.user or request.user.level == '1':
        review.delete()
        messages.success(request, "삭제되었습니다.")
        return redirect('/review/')
    else:
        messages.error(request, "본인 게시글이 아닙니다.")
        return redirect('/review/' + str(pk))
