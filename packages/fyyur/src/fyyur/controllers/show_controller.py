from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for, flash

from fyyur.extensions import db
from fyyur.models import Show, Artist, Venue
from fyyur.forms import ShowForm

show_bp = Blueprint('shows', __name__)


@show_bp.route('/shows')
def list_shows():
    shows = (
        db.session.query(Show, Artist, Venue)
        .join(Artist)
        .join(Venue)
        .order_by(Show.date.desc())
        .all()
    )

    data = [{
        'venue_id': venue.id,
        'venue_name': venue.name,
        'artist_id': artist.id,
        'artist_name': artist.name,
        'artist_image_link': artist.image_link,
        'start_time': show.date.strftime('%Y-%m-%dT%H:%M:%S.000Z'),
    } for show, artist, venue in shows]

    return render_template('pages/shows.html', shows=data)


@show_bp.route('/shows/create', methods=['GET'])
def create_show_form():
    form = ShowForm()
    return render_template('forms/new_show.html', form=form)


@show_bp.route('/shows/create', methods=['POST'])
def create_show_submission():
    form = ShowForm(request.form)

    if not form.validate():
        flash('An error occurred. Show could not be listed.')
        return render_template('forms/new_show.html', form=form)

    try:
        show = Show(
            artist_id=form.artist_id.data,
            venue_id=form.venue_id.data,
            date=form.start_time.data,
        )
        db.session.add(show)
        db.session.commit()
        flash('Show was successfully listed!')
    except Exception:
        db.session.rollback()
        flash('An error occurred. Show could not be listed.')

    return redirect(url_for('index'))
