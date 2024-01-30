from django.db import models


class News(models.Model):
    title = models.CharField(
        max_length=500
    )
    description = models.TextField(
        verbose_name="Описание",
    )
    image = models.ImageField(
        verbose_name="Картинки",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создание",
    )

    def str(self):
        return f"{self.title}"


class Images(models.Model):
        image = models.ImageField(
            upload_to="images/",
        )
        news = models.ForeignKey(
            News,
            on_delete=models.CASCADE,
            related_name="images",
        )


# class Images(models.Model):
#         image = models.ImageField(
#             upload_to="images/",
#         )
#         news = models.ForeignKey(
#             News,
#             on_delete=models.CASCADE,
#             related_name="images",
#         )


































# from django.db import models
#
#
# class News(models.Model):
#     title = models.CharField(
#         max_length=500
#     )
#     description = models.TextField(
#         verbose_name="Описание",
#     )
#     image = models.ImageField(
#         verbose_name="Картинки",
#     )
#     created_at = models.DateTimeField(
#         auto_now_add=True,
#         verbose_name="Дата создание",
#     )
#
#     def str(self):
#         return f"{self.title}"
#
#
# class Images(models.Model):
#         image = models.ImageField(
#             upload_to="images/",
#         )
#         news = models.ForeignKey(
#             News,
#             on_delete=models.CASCADE,
#             related_name="images",
#         )
#
#
#
#
#
#
#
#
#
#
#




# class News(models.Model):
#     title = models.CharField(max_length=500)
#     description = models.TextField()
#     image = models.ImageField(upload_to='news')
#
#     def str(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'News'
#         verbose_name_plural = 'News'
#
