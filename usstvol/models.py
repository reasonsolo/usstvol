# -*- encoding:utf-8 -*-
from django.db import models
from django.conf import settings
from datetime import datetime
import uuid
import os

MAX_LEN = 255
CHOICE_LEN = 5
MAX_DIGITS = 20
DECIMAL_PLACES = 5

class Applicant(models.Model):
  name = models.CharField('姓名', max_length = MAX_LEN)
  GENDER_CHOICES = (
    ('M', '男'),
    ('F', '女'),
    )
  gender = models.CharField('性别', default = 'M', max_length = CHOICE_LEN,
    choices = GENDER_CHOICES)
  studentid = models.CharField('学号', max_length = MAX_LEN)
  SCHOOL_CHOICES = (
    ('NYDL', '能源与动力工程学院'),
    )
  school = models.CharField('学院', max_length = CHOICE_LEN,
    choices = SCHOOL_CHOICES)
  major = models.CharField('专业', max_length = MAX_LEN)
  cellphone = models.CharField('手机', max_length = MAX_LEN)
  idnumber = models.CharField('身份证号', max_length = MAX_LEN)
  grade = models.CharField('年级', max_length = MAX_LEN)
  height = models.DecimalField('身高', max_digits = MAX_DIGITS,
    decimal_places = DECIMAL_PLACES)
  email = models.EmailField('邮箱')
  applytime = models.DateTimeField('申请时间', default = datetime.now())
  event = models.ForeignKey('Event', null = True, blank = True, verbose_name = '项目')

  def get_image_path(instance, filename):
    try:
      ext = file.split('.')[:-1]
    except Exception:
      ext = 'jpg'
    return os.path.join('applicants', '%s.%s' % (uuid.uuid4(), ext))

  image = models.ImageField('照片', upload_to=get_image_path)

  def get_image(self):
    return os.path.join(settings.MEDIA_URL, self.image.url)


  def image_thumb(self):
    return '<img src="%s" width="50px" height="50px" />' %  \
      self.get_image()
  image_thumb.allow_tags = True
  image_thumb.short_description = u'照片'

  def __unicode__(self):
    return self.name + self.studentid


class Event(models.Model):
  name = models.CharField('姓名', max_length = MAX_LEN)
  starttime = models.DateTimeField('开始时间', default = datetime.now())
  endtime = models.DateTimeField('结束时间', default = datetime.now())
  APPLY_CHOICES = (
      ('Y', '可报名'),
      ('N', '不可报名'),
  )
  state = models.CharField('状态', default = 'Y', choices = APPLY_CHOICES, max_length = CHOICE_LEN)

  def __unicode__(self):
    return self.name
