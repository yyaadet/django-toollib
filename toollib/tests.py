#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

from django.core import mail
from django.test import TestCase
from toollib.email import send_mail, send_html_template_email


class EmailTestCases(TestCase):
    """test email

    """

    def test_send_email_not_use_thread(self):
        send_mail("subject_not_use_thread", "body_not_use_thread", ["test@funshion.com"], [], False)
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, 'subject_not_use_thread')
        self.assertEquals(mail.outbox[0].body, 'body_not_use_thread')

    def test_send_email_use_thread(self):
        send_mail("subject_use_thread", "body_use_thread", ["test@funshion.com"], [], True)
        time.sleep(1)
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, 'subject_use_thread')
        self.assertEquals(mail.outbox[0].body, 'body_use_thread')

    def test_send_html_template_email(self):
        send_html_template_email("test", 'email.html', {'username':'test'}, ["hucj@funshion.com"], [], False)

class RenderTestCases(TestCase):

    def test_render_json(self):
        pass