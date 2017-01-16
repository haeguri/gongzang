from markdownx.fields import MarkdownxFormField
from main.models import Article
from django.forms import ModelForm

class ArticleForm(ModelForm):
    body = MarkdownxFormField()

    class Meta:
        model = Article
        fields = "__all__"