from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Priority(BaseModel):
    #priority_id = models.IntegerField(max_length=15)
    name = models.CharField(max_length=100)

    class Meta:
            verbose_name = "Priority"
            verbose_name_plural = "Priorities"

    def __str__(self):
        return self.name

class Category(BaseModel):
    #category_id = models.IntegerField(max_length=15)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Task(BaseModel):
    #task_id = models.IntegerField(max_length=15)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    deadline = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[
            ("Pending", "Pending"),
            ("In Progress", "In Progress"),
            ("Completed", "Completed"),
        ],
        default="Pending"
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)

    def __str__(self):
        return self.title 

class Note(BaseModel):
    #note_id = models.IntegerField(max_length=15)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)

    def __str__(self):
        return f"Note for {self.task.title}"

class SubTask(BaseModel):
    #subtask_id = models.IntegerField(max_length=15)
    parent_task = models.ForeignKey(Task, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    status = models.CharField(
            max_length=20,
            choices=[
                ("Pending", "Pending"),
                ("In Progress", "In Progress"),
                ("Completed", "Completed"),
            ],
            default="Pending"
        )

    def __str__(self):
        return self.title

