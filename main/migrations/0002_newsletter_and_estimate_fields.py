# Generated manually

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        # Add Newsletter model
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='제목')),
                ('author', models.CharField(max_length=100, verbose_name='작성자')),
                ('content', models.TextField(verbose_name='내용')),
                ('image', models.ImageField(upload_to='newsletters/', verbose_name='이미지')),
                ('views', models.IntegerField(default=0, verbose_name='조회수')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일자')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일자')),
            ],
            options={
                'verbose_name': '뉴스레터',
                'verbose_name_plural': '뉴스레터',
                'ordering': ['-created_at'],
            },
        ),
        # Add fields to Estimate model
        migrations.AddField(
            model_name='estimate',
            name='category',
            field=models.CharField(choices=[('general', '일반'), ('specialized', '특화'), ('education', '교육')], default='general', max_length=20, verbose_name='사업분야'),
        ),
        migrations.AddField(
            model_name='estimate',
            name='company',
            field=models.CharField(default='', max_length=100, verbose_name='회사명'),
        ),
        migrations.AddField(
            model_name='estimate',
            name='email',
            field=models.EmailField(default='', max_length=254, verbose_name='이메일'),
        ),
        migrations.AddField(
            model_name='estimate',
            name='homepage',
            field=models.URLField(blank=True, null=True, verbose_name='홈페이지 URL'),
        ),
        migrations.AddField(
            model_name='estimate',
            name='phone',
            field=models.CharField(default='', max_length=20, verbose_name='연락처'),
        ),
    ]




