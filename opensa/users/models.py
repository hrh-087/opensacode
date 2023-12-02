# coding:utf-8
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from rest_framework.authtoken.models import Token

USER_LEVEL_TYPE = (
    (0, 'View'),
    (1, 'Exec'),
    (2, 'Delete'),
)


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **kwargs):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        Token.objects.create(user=user)
        return user

    def create_superuser(self, email, username, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
                                password=password,
                                username=username,
                                )
        user.level = 2
        user.is_superuser = True
        user.save(using=self._db)
        Token.objects.create(user=user)
        return user


class DepartMent(models.Model):
    """ 部门表 """
    name = models.CharField(max_length=64, unique=True, verbose_name='DepartMent Name')
    comment = models.CharField(max_length=255, blank=True, null=True, verbose_name='DepartMent Comment')
    permission = models.ManyToManyField(to='PermissionList', blank=True, verbose_name="Permission List")

    class Meta:
        db_table = "department"
        verbose_name = 'DepartMent Manage'
        verbose_name_plural = 'DepartMent Manage'

    def __str__(self):
        return self.name

    @property
    def user_list(self):
        user_name = DepartMent.objects.get(name=self.name)
        return user_name.userprofile_set.all()


class MenuList(models.Model):
    """ 菜单表 """
    router_name = models.CharField(max_length=32, blank=True, null=True, verbose_name="Menu Name")
    menu_name = models.CharField(max_length=32, blank=True, null=True, verbose_name="First Menu")
    parent = models.ForeignKey(to='self', blank=True, null=True, verbose_name='Menu Parent', on_delete=models.CASCADE)

    class Meta:
        db_table = "menuList"
        verbose_name = 'Menu Manage'
        verbose_name_plural = 'Menu Manage'

    def __str__(self):
        return "{}->{}".format(self.menu_name, self.router_name)


class PermissionList(models.Model):
    """ 权限表 """
    name = models.CharField(max_length=64, unique=True, verbose_name='Permission Name')
    url_name = models.CharField(max_length=32, unique=True, blank=True, null=True, verbose_name='Url Name')
    url = models.CharField(max_length=255, unique=True, blank=True, null=True, verbose_name='Permission Url')
    menu = models.ManyToManyField(to="MenuList", blank=True, verbose_name="Menu Manager")

    class Meta:
        db_table = "permissionList"
        verbose_name = 'Permission Manage'
        verbose_name_plural = 'Permission Manage'

    def __str__(self):
        return '{}({})'.format(self.name, self.url)


class RoleList(models.Model):
    """ 角色表 """
    name = models.CharField(max_length=64, unique=True, verbose_name='RoleName')
    permission = models.ManyToManyField(to='PermissionList', blank=True, verbose_name='Permission List')

    class Meta:
        db_table = "rolelist"
        verbose_name = 'Role Manage'
        verbose_name_plural = 'Role Manage'

    def __str__(self):
        return self.name


# 用户表
class UserProfile(AbstractBaseUser):
    """ 用户表 """
    email = models.EmailField(
        verbose_name='Email Address',
        max_length=255,
        unique=True,
    )

    username = models.CharField(max_length=32, verbose_name="UserName")
    token = models.CharField(max_length=128, default=None, blank=True, null=True, verbose_name="Token")
    department = models.ForeignKey(to="DepartMent", blank=True, null=True, on_delete=models.SET_NULL,
                                   verbose_name='User Department')
    mobile = models.CharField(max_length=32, default=None, blank=True, null=True, verbose_name='Mobile Phone')
    # project = models.ManyToManyField(to="Project", default=None, blank=True, verbose_name="User Project")
    level = models.IntegerField(choices=USER_LEVEL_TYPE, default=0, blank=True, verbose_name='User Level')
    role = models.ForeignKey(to="RoleList", null=True, blank=True, on_delete=models.SET_NULL,
                             verbose_name="User Role", related_name='users')
    avatar = models.CharField(default="user.png", max_length=64, blank=True, verbose_name="User Avatar")
    is_active = models.BooleanField(default=True, verbose_name='Active')
    is_superuser = models.BooleanField(default=False, verbose_name='User Type')
    limit = models.IntegerField(default=0, blank=True, verbose_name='Login Limit')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Create By')
    login_date = models.DateTimeField(blank=True, null=True, verbose_name='Login By')
    valid_date = models.DateTimeField(blank=True, null=True, verbose_name='Valid Date')
    comment = models.CharField(max_length=128, blank=True, null=True, verbose_name='User Comment')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = "userprofile"
        verbose_name = 'User Manage'
        verbose_name_plural = "User Manage"

    def __str__(self):
        return self.email

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_perms(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_superuser

    objects = UserManager()
