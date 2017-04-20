# -*- coding: utf-8 -*-
import os
from django.db import models


class Document(models.Model):
	docfile = models.ImageField(upload_to='documents')
	
