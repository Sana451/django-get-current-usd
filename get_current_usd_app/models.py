from django.db import models


class Rate(models.Model):
    rate = models.DecimalField("result of rate request", max_digits=7, decimal_places=4)
    request_datetime = models.DateTimeField("request date and time")

    def __str__(self):
        return f"Rate {self.rate} was saved {self.request_datetime}"

    class Meta:
        ordering = ["-request_datetime"]
