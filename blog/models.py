from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.utils.translation import ugettext as _


#TODO:
#   Image - отдельная модель многие ко многим(?)
# - Category image 
# - Post image
# - Fat Models, thin View, stupid Template!


class Category(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    slug = models.SlugField(max_length=50, unique=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return '{}'.format(self.title)
    
    def get_absolute_url(self):
        return reverse(kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=150, db_index=True)
    text = models.TextField('Текст', blank=True, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    published_date = models.DateTimeField(blank=True, null=True)

    publishTrue = models.BooleanField(default=True, db_index=True, verbose_name=_('Publish'))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField('Краткое описание', max_length=250, blank=True)
    
    #!Изображение сохраняется, 
    #нужно вывести -> views 
    #и thumbnail -> admin
    img = models.ImageField(upload_to='media/images', 
                      blank=True, 
                      db_index=True,
                      verbose_name=_('Image'))

    def __str__(self):
        return '{}'.format(self.title)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('-published_date',)


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField('Автор', max_length=100)
    text = models.TextField('Текст')
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save

    def __str__(self):
        return '{}'.format(self.text)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Image(models.Model):
    name = models.CharField('Тайтл', max_length=25, unique=True)


class Sort(models.Model):
    pass


class Search(models.Model):
    pass


