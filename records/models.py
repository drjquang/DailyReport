from django.db import models


class Record(models.Model):
    machine_no = models.CharField(max_length=3)
    problem = models.TextField()
    solution = models.TextField(blank=True)
    done_by = models.CharField(max_length=64)
    supervised_by = models.CharField(max_length=64)
    datestamp = models.DateField()
    timestamp = models.TimeField()

    def __str__(self):
        return '{} - at {} and {}, machine no {} got problem. ' \
               'It was solved by {} and supervised by {}'\
            .format(self.id, self.datestamp, self.timestamp, self.machine_no,
                    self.done_by, self.supervised_by)
