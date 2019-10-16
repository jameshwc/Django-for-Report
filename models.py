# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DownloadDownloadFile(models.Model):
    file = models.CharField(max_length=100)
    init_upload_time = models.DateTimeField()
    last_modified = models.DateTimeField()
    download_counter = models.IntegerField()
    name = models.CharField(max_length=30)
    filename = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'Download_download_file'


class No2NameNtuStudent(models.Model):
    department = models.CharField(max_length=30)
    student_no = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    chinese_name = models.CharField(max_length=50)
    english_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'No2Name_ntu_student'


class SystemDownloadLog(models.Model):
    date = models.DateTimeField()
    filename = models.ForeignKey(DownloadDownloadFile, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'System_download_log'


class SystemIpLog(models.Model):
    date = models.DateTimeField()
    ip = models.CharField(max_length=39)
    page = models.CharField(max_length=200)
    user = models.ForeignKey('UserUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'System_ip_log'


class SystemNo2NameQuerylog(models.Model):
    date = models.DateTimeField()
    query = models.CharField(max_length=50)
    query_type = models.CharField(max_length=30)
    user = models.ForeignKey('UserUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'System_no2name_querylog'


class SystemUpdateLog(models.Model):
    date = models.DateField()
    is_content = models.IntegerField()
    is_debug = models.IntegerField()
    detail = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'System_update_log'


class UserUser(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=64)
    student_id = models.CharField(max_length=20)
    email = models.CharField(max_length=254)
    is_verified = models.IntegerField()
    code = models.CharField(max_length=15)
    register_time = models.DateTimeField()
    verified_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User_user'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'
