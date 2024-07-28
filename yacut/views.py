from flask import redirect, render_template, url_for

from . import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import get_unique_short_id
from settings import TextErrors


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form, )
    short = form.custom_id.data
    if not short:
        short = get_unique_short_id()
    elif URLMap.query.filter_by(short=short).first():
        form.custom_id.errors = (TextErrors.LABEL_EXIST,)
        return render_template('index.html', form=form)
    db.session.add(
        URLMap(
            original=form.original_link.data,
            short=short,
        )
    )
    db.session.commit()
    return render_template(
        'index.html', form=form,
        link=url_for('redirect_to', short=short, _external=True)
    )


@app.route('/<short>', methods=['GET'])
def redirect_to(short):
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original
    )
