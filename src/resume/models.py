from django.db import models


class Job(models.Model):
    company_name = models.CharField('company name', max_length=100)
    company_site = models.URLField('company site')

    start_dt = models.DateField('start date')
    end_dt = models.DateField('end date')

    title = models.CharField(max_length=50)
    product = models.TextField(help_text='leading or attend projects, markdown')
    duties = models.CharField(max_length=100)
    tech_stack = models.TextField(help_text='technology stack, markdown')

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'job'
        verbose_name_plural = 'jobs'
        ordering = ['-start_dt']


class Education(models.Model):
    school_name = models.CharField('school name', max_length=100)
    school_site = models.URLField('school website')

    start_dt = models.DateField('start date')
    end_dt = models.DateField('end date')

    degree = models.CharField(max_length=20, help_text='Bachelor, Master, Doctor')
    major = models.CharField('school major', max_length=100)
    course = models.TextField('major course')

    def __str__(self):
        return self.school_name

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'
        ordering = ['start_dt']
