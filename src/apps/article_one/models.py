from django.db import models as m

class ArticleContent (m.Model):
    article_one_content = m.TextField(null=True, blank=True)

