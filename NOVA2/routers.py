class AppRouter:
    # Map apps to their specific database aliases
    APP_MAP = {
        'taskmanagement_app': 'tasks_db',
        'learning_logs': 'logs_db',
    }

    def db_for_read(self, model, **hints):
        return self.APP_MAP.get(model._meta.app_label)

    def db_for_write(self, model, **hints):
        return self.APP_MAP.get(model._meta.app_label)

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        target_db = self.APP_MAP.get(app_label)
        if target_db:
            return db == target_db
        # Ensure other apps (admin, auth) stay in the default DB
        return db == 'default'