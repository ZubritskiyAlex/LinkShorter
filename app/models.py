from django.db import models
from django.contrib.auth. models import User
from hashlib import md5


class URL(models.Model):
    current_url = models.URLField(max_length=200)
    striped_url = models.URLField(max_length=40)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return f"{self.current_url}-{self.owner}-{self.striped_url}"


    def save(self, *args, **kwargs):
        if not self._id:
            self.striped_url = f"http://{md5(self.current_url.encode()).hexdigest()[:25]}"
        url = URL.objects.filter(current_url=self.current_url)
        url = {'url': url}
        if url:
            self.striped_url = url['url'][0].striped_url
        return super().save(*args, **kwargs)