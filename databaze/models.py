from django.db import models



class Zanr(models.Model):
    nazev = models.CharField(max_length=50, verbose_name="Název")

    def __str__(self):
        return self.nazev

    class Meta:

        verbose_name = 'Zanr',
        verbose_name_plural = 'Zanry'

class Umelec(models.Model):
    jmeno = models.CharField(max_length=100, verbose_name="Jméno")
    datum_zalozeni = models.IntegerField(max_length=4,blank=True, null=True,
                                verbose_name="Datum vzniku")

    class Meta:

        verbose_name = 'Umelec',
        verbose_name_plural = 'Umelci'

    def __str__(self):
        return self.jmeno

class Song(models.Model):
    nazev_song = models.CharField(max_length=100, verbose_name="Název")
    datum_vydani = models.DateField(blank=True, null=True,
                                verbose_name="Datum vydání")
    zanr = models.ManyToManyField(Zanr)
    umelec = models.ManyToManyField(Umelec)

    class Meta:

        verbose_name = 'Song',
        verbose_name_plural = 'Songs'

    def __str__(self):
        return self.nazev_song



