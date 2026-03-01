from django.contrib import admin
class AppRouter:
    # Map apps to their specific database aliases

    # In NOVA2/routers.py
    def db_for_read(self, model, **hints):
        if model._meta.app_label in ['auth', 'contenttypes', 'admin', 'sessions']:
            return 'default'
        if model._meta.app_label == 'taskmanagement_app':
            return 'tasks_db'
        if model._meta.app_label == 'learning_logs':
            return 'logs_db'
        return 'default' 

    def db_for_write(self, model, **hints):
        if model._meta.app_label in ['auth', 'contenttypes', 'admin', 'sessions']:
            return 'default'

        if model._meta.app_label == 'learning_logs':
            return 'logs_db'

        if model._meta.app_label == 'taskmanagement_app':
            return 'tasks_db'

        return 'default'

    def allow_relation(self, obj1, obj2, **hints):    
            return True
        
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in ['auth', 'contenttypes', 'admin', 'sessions']:
            return db == 'default'

        if app_label == 'learning_logs':
            return db == 'logs_db'

        if app_label == 'taskmanagement_app':
            return db == 'tasks_db'

        return db == 'default'
    
class MultiDBModelAdmin(admin.ModelAdmin):
    using = 'default'

    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)
    def delete_model(self, request, obj):
        obj.delete(using=self.using)
    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # If the field is a User (from auth app), always look in 'default'
        if db_field.related_model._meta.app_label == 'auth':
            return super().formfield_for_foreignkey(db_field, request, using='default', **kwargs)
        
        # Otherwise, use the app's specific database
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.related_model._meta.app_label == 'auth':
            return super().formfield_for_manytomany(db_field, request, using='default', **kwargs)
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)