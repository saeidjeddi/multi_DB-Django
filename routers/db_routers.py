class AuthRouter:
    route_app_label = {'auth', 'contenttypes', 'admin', 'sessions', }

    def db_for_read(self, model, **hints):

        if model._meta.app_label in self.route_app_label:
            return 'user_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_label:
            return 'user_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if(
            obj1._meta.app_label in self.route_app_label or
            obj2._meta.app_label in self.route_app_label
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_label:
            return db == 'user_db'
        return None


class HomeRouter:
    route_app_label = {'home', }

    def db_for_read(self, model, **hints):

        if model._meta.app_label in self.route_app_label:
            return 'home_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_label:
            return 'home_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if(
            obj1._meta.app_label in self.route_app_label or
            obj2._meta.app_label in self.route_app_label
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_label:
            return db == 'home_db'
        return None


class StdRouter:
    route_app_label = {'std', }

    def db_for_read(self, model, **hints):

        if model._meta.app_label in self.route_app_label:
            return 'std_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_label:
            return 'std_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if(
            obj1._meta.app_label in self.route_app_label or
            obj2._meta.app_label in self.route_app_label
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_label:
            return db == 'std_db'
        return None
