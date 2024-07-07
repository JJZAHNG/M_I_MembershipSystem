from django.db import models
from utils.common_model import BaseModel


class AdminUser(BaseModel):
    username = models.CharField(max_length=255, verbose_name='管理员用户名')
    password = models.CharField(max_length=255, verbose_name='管理员密码')

    class Meta:
        db_table = 'mi_admin_user'


class User(BaseModel):
    username = models.CharField(max_length=255, verbose_name='用户名')
    email = models.EmailField(verbose_name='邮箱')
    phone = models.CharField(max_length=11, verbose_name='用户手机号', unique=True)
    points = models.IntegerField(verbose_name='用户积分')
    sex_choice = (
        (0, '男'),
        (1, '女'),
        (2, '保密'),
    )
    sex = models.IntegerField(verbose_name='性别', choices=sex_choice, default=2)
    avatar = models.ImageField(upload_to='avatar/user/', verbose_name='头像', default='avatar/user/default.png')

    class Meta:
        db_table = 'mi_user'


class Student(BaseModel):
    name = models.CharField(max_length=255, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    sex_choice = (
        (0, '男'),
        (1, '女'),
        (2, '保密'),
    )
    sex = models.IntegerField(verbose_name='性别', choices=sex_choice, default=2)
    grade_choice = (
        (1, '小学'),
        (2, '初中'),
        (3, '高中'),
    )
    grade = models.IntegerField(verbose_name='年级段', choices=grade_choice)
    avatar = models.ImageField(upload_to='avatar/stu/', verbose_name='头像', default='avatar/stu/default.png')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='家长', null=True, blank=True)
    course = models.ManyToManyField('course.Course', verbose_name='学生课程', db_table='mi_student_course')

    class Meta:
        db_table = 'mi_student'


class Teacher(BaseModel):
    name = models.CharField(max_length=255, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    phone = models.CharField(max_length=11, verbose_name='教师手机号', unique=True)
    sex_choice = (
        (0, '男'),
        (1, '女'),
        (2, '保密'),
    )
    sex = models.IntegerField(verbose_name='性别', choices=sex_choice, default=2)
    avatar = models.ImageField(upload_to='avatar/teacher/', verbose_name='头像', default='avatar/teacher/default.png')

    class Meta:
        db_table = 'mi_teacher'
