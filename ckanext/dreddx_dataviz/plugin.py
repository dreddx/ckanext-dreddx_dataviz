import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

import ckanext.dreddx_dataviz.views.dataviz as dataviz

class DreddxDatavizPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)

    # IBlueprint
    def get_blueprint(self):
        return [
            dataviz.dreddx_dataviz_gallery
        ]

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'dreddx_dataviz')
