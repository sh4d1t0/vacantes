class PPO(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'vacantes_app':
            return 'itpeopleone'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'vacantes_app':
            return 'itpeopleone'
        return None


    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'vacantes_app':
            return False
        return None