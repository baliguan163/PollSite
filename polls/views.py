from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

    def vote(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form.
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

            # 代码解释：
            #
            # request.POST, request.GET： 分别可获得POST或GET方法的参数值，如上
            # request.POST['choice']
            # 可取得POST请求中，name值为choice的Value值。若POST参数中没有choice，则会产生KeyError。
            #
            # HttpResponseRedirect：重定向跳转，提交成功后进行自动重定向跳转是web开发的一个良好实践。防止数据提交两次。

        #
        #     {{forloop.counter}}:
        #     for 循环次数
        #
        # { % csrf_token %}: 解决POST请求跨域问题
        # Cross
        # Site
        # Request
        # Forgeries
        #
        # { % if %}  { % endif %}:判断
        #
        # { %
        # for %} {% endfor %}:循环
        #

# get_object_or_404(),get_list_or_404() 当获取不到对象时，返回404页面