from django.db import models


def attachment_path(instance, filename):
    return "databaze/" + str(instance.album.id) + "/attachments/" + filename


class Zanr(models.Model):
    nazev = models.CharField(max_length=50, verbose_name="Název")

    def __str__(self):
        return self.nazev

    class Meta:
        verbose_name = 'Zanr',
        verbose_name_plural = 'Zanry'


class Umelec(models.Model):
    jmeno = models.CharField(max_length=100, verbose_name="Jméno")
    datum_zalozeni = models.IntegerField(blank=True, null=True,
                                         verbose_name="Datum vzniku")
    popis = models.TextField(blank=True, null=True, verbose_name="Popis")

    class Meta:
        verbose_name = 'Umelec',
        verbose_name_plural = 'Umelci'

    def __str__(self):
        return self.jmeno

class Album(models.Model):
    nazev_album = models.CharField(max_length=100, verbose_name="Název")
    datum_vydani = models.DateField(blank=True, null=True,
                                    verbose_name="Datum vydání")

    zanr = models.ManyToManyField(Zanr)
    umelec = models.ManyToManyField(Umelec)

    class Meta:
        verbose_name = 'Album',
        verbose_name_plural = 'Alba'

    def __str__(self):
        return self.nazev_album


class Song(models.Model):
    nazev_song = models.CharField(max_length=100, verbose_name="Název")
    datum_vydani = models.DateField(blank=True, null=True,
                                    verbose_name="Datum vydání")
    text = models.TextField(blank=True, null=True, verbose_name="Text")
    zanr = models.ManyToManyField(Zanr)
    umelec = models.ManyToManyField(Umelec)
    album = models.ManyToManyField(Album)


    class Meta:
        verbose_name = 'Song',
        verbose_name_plural = 'Songs'

    def __str__(self):
        return self.nazev_song


class Attachment(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    last_update = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to=attachment_path, null=True, verbose_name="File")
    TYPE_OF_ATTACHMENT = (
        ('audio', 'Audio'),
        ('image', 'Image'),
        ('text', 'Text'),
        ('video', 'Video'),
        ('other', 'Other'),
    )

    type = models.CharField(max_length=5, choices=TYPE_OF_ATTACHMENT, blank=True, default='image',
                            help_text='Select allowed attachment type', verbose_name="Attachment type")

    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-last_update", "type"]

    def __str__(self):
        return f"{self.title}, ({self.type})"
