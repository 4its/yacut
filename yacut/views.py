from flask import redirect, render_template

from . import app
from .forms import URLMapForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form, )
    url_map = URLMap.create_urlmap(
        form.original_link.data, form.custom_id.data, True
    )
    return render_template(
        'index.html', form=form, link=url_map.short_link()
    )


@app.route('/<short>', methods=['GET'])
def redirect_to(short):
    return redirect(URLMap.get_object(short, True).original)
