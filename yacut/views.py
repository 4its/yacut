from flask import flash, redirect, render_template, url_for

from . import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import get_unique_short_id

LABEL_EXIST = 'Предложенный вариант короткой ссылки уже существует.'


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if not custom_id:
            custom_id = get_unique_short_id()
        elif URLMap.query.filter_by(short=custom_id).first():
            form.custom_id.errors = (LABEL_EXIST,)
            return render_template('cut_form.html', form=form)
        db.session.add(
            URLMap(
                original=form.original_link.data,
                short=custom_id,
            )
        )
        db.session.commit()
        link = url_for('redirect_to', short=custom_id, _external=True)
        flash(
            f'<a href="{link}" class="text-center">{link}</a>'
        )
    return render_template('cut_form.html', form=form)


@app.route('/<short>', methods=['GET'])
def redirect_to(short):
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original
    )
