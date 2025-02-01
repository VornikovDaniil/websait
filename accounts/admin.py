from django.contrib import admin
from .models import EmailVerificationCode, PasswordResetCode

admin.site.register(EmailVerificationCode)
admin.site.register(PasswordResetCode)