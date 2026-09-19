from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for, flash

from fyyur.extensions import db
from fyyur.models import Artist
from fyyur.forms import ArtistForm

artist_bp = Blueprint('artists', __name__)


def format_artist_shows(artist):
    upcoming_shows = []
    past_shows = []
    now = datetime.now()

    for show in artist.shows:
        show_data = {
            'venue_id': show.venue_id,
            'venue_name': show.venue.name,
            'venue_image_link': show.venue.image_link,
            'start_time': show.date.strftime('%Y-%m-%dT%H:%M:%S.000Z'),
        }
        if show.date > now:
            upcoming_shows.append(show_data)
        else:
            past_shows.append(show_data)

    return {
        'upcoming_shows': upcoming_shows,
        'past_shows': past_shows,
        'upcoming_shows_count': len(upcoming_shows),
        'past_shows_count': len(past_shows),
    }


@artist_bp.route('/artists')
def list_artists():
    artists = Artist.query.order_by(Artist.name).all()
    return render_template('pages/artists.html', artists=artists)


@artist_bp.route('/artists/search', methods=['POST'])
def search_artists():
    search_term = request.form.get('search_term', '')
    artists = Artist.query.filter(
        Artist.name.ilike(f'%{search_term}%')
    ).order_by(Artist.name).all()

    data = [{
        'id': a.id,
        'name': a.name,
        'num_upcoming_shows': len(a.shows),
    } for a in artists]

    return render_template(
        'pages/search_artists.html',
        results={'count': len(data), 'data': data},
        search_term=search_term,
    )


@artist_bp.route('/artists/<int:artist_id>')
def show_artist(artist_id):
    artist = Artist.query.get_or_404(artist_id)
    shows_data = format_artist_shows(artist)

    return render_template('pages/show_artist.html', artist={
        'id': artist.id,
        'name': artist.name,
        'genres': artist.genres.split(',') if artist.genres else [],
        'city': artist.city,
        'state': artist.state,
        'phone': artist.phone,
        'website': artist.website,
        'facebook_link': artist.facebook_link,
        'image_link': artist.image_link,
        'seeking_venue': getattr(artist, 'seeking_venue', False),
        'seeking_description': getattr(artist, 'seeking_description', ''),
        **shows_data,
    })


@artist_bp.route('/artists/create', methods=['GET'])
def create_artist_form():
    form = ArtistForm()
    return render_template('forms/new_artist.html', form=form)


@artist_bp.route('/artists/create', methods=['POST'])
def create_artist_submission():
    form = ArtistForm(request.form)

    if not form.validate():
        flash('An error occurred. Artist could not be listed.')
        return render_template('forms/new_artist.html', form=form)

    try:
        artist = Artist(
            name=form.name.data,
            city=form.city.data,
            state=form.state.data,
            phone=form.phone.data,
            image_link=form.image_link.data,
            facebook_link=form.facebook_link.data,
            website=form.website_link.data,
            genres=','.join(form.genres.data),
        )
        db.session.add(artist)
        db.session.commit()
        flash(f'Artist {artist.name} was successfully listed!')
    except Exception:
        db.session.rollback()
        flash('An error occurred. Artist could not be listed.')

    return redirect(url_for('index'))


@artist_bp.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
    artist = Artist.query.get_or_404(artist_id)
    form = ArtistForm(obj=artist)
    return render_template('forms/edit_artist.html', form=form, artist=artist)


@artist_bp.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
    artist = Artist.query.get_or_404(artist_id)
    form = ArtistForm(request.form)

    if not form.validate():
        flash('An error occurred. Artist could not be updated.')
        return render_template('forms/edit_artist.html', form=form, artist=artist)

    try:
        artist.name = form.name.data
        artist.city = form.city.data
        artist.state = form.state.data
        artist.phone = form.phone.data
        artist.image_link = form.image_link.data
        artist.facebook_link = form.facebook_link.data
        artist.website = form.website_link.data
        artist.genres = ','.join(form.genres.data)
        db.session.commit()
        flash(f'Artist {artist.name} was successfully updated!')
    except Exception:
        db.session.rollback()
        flash('An error occurred. Artist could not be updated.')

    return redirect(url_for('artists.show_artist', artist_id=artist.id))
