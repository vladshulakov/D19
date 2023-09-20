from django.contrib.auth.models import User
from django.db import models
from django.core.mail import send_mail
from django.conf import settings

tanks = 'TNK'
hils = 'HIL'
dd = 'DD'
merchants = 'MCH'
guild_masters = 'GMA'
quest_givers = 'QMA'
blacksmiths = 'BLM'
tanners = 'TAN'
potion_makers = 'PMK'
spell_masters = 'SMA'

CATEGORY = [
    (tanks, 'Танки'),
    (hils, 'Хилы'),
    (dd, 'ДД'),
    (merchants, 'Торговцы'),
    (guild_masters, 'Гилдмастеры'),
    (quest_givers, 'Квестгиверы'),
    (blacksmiths, 'Кузнецы'),
    (tanners, 'Кожевники'),
    (potion_makers, 'Зельевары'),
    (spell_masters, 'Мастера заклинаний'),
]


class Post(models.Model):
    post_title = models.CharField(max_length=255)
    post_text = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=3, choices=CATEGORY, default=tanks)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.post_title


class Reply(models.Model):
    reply_text = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    accepted = models.BooleanField(default=False)

    def send_notification_email(self):
        subject = 'Отклик на ваше объявление'
        message = f'Здравствуйте!\n\nНа ваше объявление "{self.post}" появился новый отклик.\n\nС уважением,\nВаш сайт.'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [self.post.user.email]

        send_mail(subject, message, from_email, recipient_list)

    def send_accepted_email(self):
        subject = 'Ваш отклик принят'
        message = f'Здравствуйте!\n\nВаш отклик "{self.reply_text[:15]}" принят.\n\nС уважением,\nВаш сайт.'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [self.user.email]

        send_mail(subject, message, from_email, recipient_list)

    def accept(self):
        self.accepted = True
        self.send_accepted_email()

    def __str__(self):
        return self.reply_text