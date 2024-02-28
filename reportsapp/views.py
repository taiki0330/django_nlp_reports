from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .models import GenreModel, CrimeModel, SuspectModel, VictimModel
from django.urls import reverse_lazy
from .services import generate_text
from .forms import TextInputForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy




# Create your views here.
class GenreList(ListView):
    model = GenreModel
    template_name = 'genre_list.html'

class CrimeList(ListView):
    model = CrimeModel
    template_name = 'crime_list.html'

    def get_queryset(self):
        return CrimeModel.objects.filter(genre_id=self.kwargs['genre_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre_id'] = self.kwargs['genre_id']
        return context

class CrimeDetail(DetailView):
    model = CrimeModel
    template_name = 'crime_detail.html'

    def get_queryset(self):
        """関連する容疑者と被害者の情報も取得する。"""
        return CrimeModel.objects.prefetch_related('suspectmodel_set', 'victimmodel_set')

class CrimeCreate(CreateView):
    model = CrimeModel
    fields = ['crime_name', 'crime_name_second', 'crime_start_date', 'crime_start_time', 'crime_end_date', 'crime_end_time', 'crime_place', 'crime_fact']
    template_name = 'crime_create.html'
    # success_url = reverse_lazy('crime')
    
    def form_valid(self, form):
        form.instance.genre_id = self.kwargs['genre_id']
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('crimes', kwargs={'genre_id': self.kwargs['genre_id']})

class SuspectDetail(DetailView):
    model = SuspectModel
    template_name = 'suspect_detail.html'

class VictimDetail(DetailView):
    model = VictimModel
    template_name = 'victim_detail.html'



class GenerateTextView(FormView):
    template_name = 'reportsapp/generate.html'
    form_class = TextInputForm
    success_url = reverse_lazy('generate_text')  # フォーム送信後にリダイレクトするURL

    def form_valid(self, form):
        # フォームのデータは有効です
        input_text = form.cleaned_data['input_text']
        # ここで入力テキストを加工するロジックを実装
        # 例: self.extra_context = {'generated_text': input_text + " processed"}
        self.extra_context = {'generated_text': input_text + " processed"}  # 簡易的な加工例
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # 既存のコンテキストデータを取得し、必要に応じてそれに追加します
        context = super().get_context_data(**kwargs)
        if self.extra_context is not None:
            context.update(self.extra_context)
        return context