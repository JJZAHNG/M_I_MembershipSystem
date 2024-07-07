from django.db import models
from utils.common_model import BaseModel


class CourseSort(BaseModel):
    grade_choice = (
        (1, '小学'),
        (2, '初中'),
        (3, '高中'),
    )
    grade = models.IntegerField(verbose_name='年级段', choices=grade_choice)
    sort_choice = (
        (1, '主题日'),
        (2, '技能训练'),
        (3, '营地训练'),
        (4, '课题孵化'),
        (5, '参赛辅导'),
        (6, '热推拼盘'),
    )
    sort = models.IntegerField(verbose_name='课程分类', choices=sort_choice)
    points = models.IntegerField(verbose_name='课程积分')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='课程分类价格')

    class Meta:
        db_table = 'mi_course_sort'


class Course(BaseModel):
    name = models.CharField(max_length=255, verbose_name='课程名称')
    total_hour = models.IntegerField(verbose_name='总课时')
    completed = models.IntegerField(verbose_name='已完成课时')
    count = models.IntegerField(verbose_name='总人数')
    applicant = models.IntegerField(verbose_name='报名人数')
    start_time = models.DateTimeField(verbose_name='开课时间')
    end_time = models.DateTimeField(verbose_name='结课时间')
    cover = models.ImageField(upload_to='course/cover/', verbose_name='课程封面')
    description = models.TextField(verbose_name='课程描述')
    status_choices = (
        (0, '未开始'),
        (1, '进行中'),
        (2, '已结束')
    )
    status = models.IntegerField(verbose_name='课程状态', choices=status_choices, default=0)
    course_sort = models.ForeignKey(CourseSort, on_delete=models.SET_NULL, verbose_name='课程分类', null=True,
                                    blank=True)
    teacher = models.ForeignKey('user.Teacher', on_delete=models.SET_NULL, verbose_name='课程讲师', null=True,
                                blank=True)

    class Meta:
        db_table = 'mi_course'


class Tag(BaseModel):
    name = models.CharField(max_length=255, verbose_name='标签名称')
    course = models.ManyToManyField(Course, verbose_name='课程标签', db_table='mi_tag_course')

    class Meta:
        db_table = 'mi_tag'


class Profile(BaseModel):
    profile = models.FileField(verbose_name='课程文件', upload_to='course/profile/')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='课程', null=True,
                               blank=True)

    class Meta:
        db_table = 'mi_profile'


class Chapter(BaseModel):
    name = models.CharField(max_length=255, verbose_name='章节名称')
    hour = models.IntegerField(verbose_name='章节课时')
    start_time = models.DateTimeField(verbose_name='章节开始')
    end_time = models.DateTimeField(verbose_name='章节结束')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='课程', null=True,
                               blank=True)

    class Meta:
        db_table = 'mi_chapter'


class HomeWork(BaseModel):
    name = models.CharField(max_length=255, verbose_name='作业名称')
    start_time = models.DateTimeField(verbose_name='作业开始')
    end_time = models.DateTimeField(verbose_name='作业结束')
    status = models.IntegerField(verbose_name='作业状态', choices=((0, '未开始'), (1, '进行中'), (2, '已结束')),
                                 default=0)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='课程', null=True,
                               blank=True)
    topic = models.ManyToManyField('Topic', verbose_name='题目', help_text='作业与题目多对多')

    class Meta:
        db_table = 'mi_homework'


class Topic(BaseModel):
    name = models.CharField(max_length=255, verbose_name='题目名称')
    type_choices = (
        (0, '单选题'),
        (1, '多选题'),
        (2, '判断题'),
        (3, '简答题'),
    )
    type = models.IntegerField(verbose_name='题目类型', choices=type_choices)
    course = models.ManyToManyField(Course, verbose_name='课程', db_table='mi_topic_course')
    score = models.IntegerField(verbose_name='题目分数')
    op_a = models.CharField(max_length=255, verbose_name='选项A', null=True, blank=True)
    op_b = models.CharField(max_length=255, verbose_name='选项B', null=True, blank=True)
    op_c = models.CharField(max_length=255, verbose_name='选项C', null=True, blank=True)
    op_d = models.CharField(max_length=255, verbose_name='选项D', null=True, blank=True)

    class Meta:
        db_table = 'mi_topic'


class Answer(BaseModel):
    homework = models.ForeignKey('HomeWork', on_delete=models.SET_NULL, verbose_name='作业', null=True,
                                 blank=True)
    topic = models.ForeignKey('Topic', on_delete=models.SET_NULL, verbose_name='题目', null=True,
                              blank=True)
    student = models.ForeignKey('user.Student', on_delete=models.SET_NULL, verbose_name='学生', null=True,
                                blank=True)
    answer = models.TextField(verbose_name='学生答案')
    result = models.IntegerField(verbose_name='学生答案结果', choices=((0, '未批改'), (1, '正确'), (2, '错误')),
                                 default=0)

    class Meta:
        db_table = 'mi_answer'
