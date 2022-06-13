import logging
from flask import Blueprint

import ckan.plugins.toolkit as tk

render = tk.render
log = logging.getLogger(__name__)

dreddx_dataviz_gallery = Blueprint(u'dreddx_dataviz_gallery', __name__, url_prefix=u'/dataviz')

def index():
    return _index('dataviz/index.html')

def _index(template_file):
    return render(template_file)

dreddx_dataviz_gallery.add_url_rule(u'', view_func=index)