from django.db import models

# Create your models here.


# Course model
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    # RELATIONS
    job_codes = models.ManyToManyField("job.jobCode", related_name="course_job_codes+")
    school = models.ForeignKey(
        "authentication.school", on_delete=models.CASCADE, related_name="course_school+"
    )

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
