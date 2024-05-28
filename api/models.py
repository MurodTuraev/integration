from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)


class Employee(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Ismi")
    last_name = models.CharField(max_length=255, verbose_name="Familiyasi")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefon")
    image_url = models.URLField(blank=True, null=True, verbose_name="Rasmga havola")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ishchi"
        verbose_name_plural = "Ishchilar royxati"