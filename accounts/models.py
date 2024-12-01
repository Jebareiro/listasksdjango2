from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, username=None, **extra_fields):
        """
        Crea y guarda un usuario con el correo electrónico y la contraseña.
        """
        if not email:
            raise ValueError(_('El correo electrónico debe ser proporcionado'))
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, username=None, **extra_fields):
        """
        Crea un superusuario con el correo electrónico y la contraseña.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Asegurarse de que el superusuario tenga estos campos
        return self.create_user(email, password, username, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), max_length=150, unique=True, blank=True, null=True)  # Campo opcional
    age = models.PositiveIntegerField(_('age'), default=0, blank=True)
    is_admin = models.BooleanField(default=False)  # Este campo es opcional
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()

    # Establecer 'email' como el campo principal para login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'age']  # Incluye campos adicionales si es necesario, por ejemplo 'age'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'users'
        swappable = 'AUTH_USER_MODEL'

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        from django.core.mail import send_mail
        send_mail(subject, message, from_email, [self.email], **kwargs)
