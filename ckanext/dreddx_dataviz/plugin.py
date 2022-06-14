from flask import Blueprint

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

dreddx_dataviz_gallery = Blueprint(u'dreddx_dataviz_gallery', __name__)

@dreddx_dataviz_gallery.route("/dataviz-gallery")
def dataviz_gallery():
    return toolkit.render("dataviz/index.html")

class DreddxDatavizPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)

    # IBlueprint
    def get_blueprint(self):
        return dreddx_dataviz_gallery

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'dreddx_dataviz')
