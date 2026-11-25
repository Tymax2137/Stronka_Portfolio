from django.db import models

class ProfileInfo(models.Model):

    full_name = models.CharField(max_length=50)
    headline = models.CharField(max_length=100,blank=True, null=True)
    bio_md = models.TextField(blank=True, null=True)
    aspirations_md = models.TextField(blank=True, null=True)
    skills_list = models.TextField(blank=True, null=True)
    experience_md = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.full_name

class Project(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_summary = models.CharField(max_length=300)
    cover_image = models.ImageField(upload_to='projects/covers/', blank=True, null=True)
    tech_stack = models.CharField(max_length=200,blank=True, null=True)
    problem_description = models.TextField()
    thought_process = models.TextField()
    challenges = models.TextField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    live_demo_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=200, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Obrazek do {self.project.title}"