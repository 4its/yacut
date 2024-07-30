from flask import flash, redirect, render_template

from . import app
from .forms import URLMapForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    try:
        return render_template(
            'index.html',
            form=form,
            link=URLMap.create(
                original=form.original_link.data,
                short=form.custom_id.data,
                validate=False
            ).short_link()
        )
    except (ValueError, RuntimeError) as error:
        flash(str(error))
        return render_template('index.html', form=form)


@app.route('/<short>', methods=['GET'])
def redirect_to(short):
    return redirect(URLMap.get(short, or_404=True).original)
