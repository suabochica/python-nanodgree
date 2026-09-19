from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for, flash

from fyyur.extensions import db
from fyyur.models import Venue
from fyyur.forms import VenueForm

venue_bp = Blueprint('venues', __name__)


def format_venue_shows(venue):
    upcoming_shows = []
    past_shows = []
    now = datetime.now()

    for show in venue.shows:
        show_data = {
            'artist_id': show.artist_id,
            'artist_name': show.artist.name,
            'artist_image_link': show.artist.image_link,
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


@venue_bp.route('/venues')
def list_venues():
    venues = Venue.query.order_by(Venue.city, Venue.state, Venue.name).all()

    areas = []
    area_map = {}

    for venue in venues:
        key = (venue.city, venue.state)
        if key not in area_map:
            area_item = {
                'city': venue.city,
                'state': venue.state,
                'venues': [],
            }
            area_map[key] = area_item
            areas.append(area_item)
        area_map[key]['venues'].append({
            'id': venue.id,
            'name': venue.name,
            'num_upcoming_shows': 0,
        })

    return render_template('pages/venues.html', areas=areas)


@venue_bp.route('/venues/search', methods=['POST'])
def search_venues():
    search_term = request.form.get('search_term', '')
    venues = Venue.query.filter(
        Venue.name.ilike(f'%{search_term}%')
    ).order_by(Venue.name).all()

    data = [{
        'id': v.id,
        'name': v.name,
        'num_upcoming_shows': len(v.shows),
    } for v in venues]

    return render_template(
        'pages/search_venues.html',
        results={'count': len(data), 'data': data},
        search_term=search_term,
    )


@venue_bp.route('/venues/<int:venue_id>')
def show_venue(venue_id):
    venue = Venue.query.get_or_404(venue_id)
    shows_data = format_venue_shows(venue)

    return render_template('pages/show_venue.html', venue={
        'id': venue.id,
        'name': venue.name,
        'genres': venue.genres.split(',') if venue.genres else [],
        'address': venue.address,
        'city': venue.city,
        'state': venue.state,
        'phone': venue.phone,
        'website': venue.website,
        'facebook_link': venue.facebook_link,
        'image_link': venue.image_link,
        'seeking_talent': getattr(venue, 'seeking_talent', False),
        'seeking_description': getattr(venue, 'seeking_description', ''),
        **shows_data,
    })


@venue_bp.route('/venues/create', methods=['GET'])
def create_venue_form():
    form = VenueForm()
    return render_template('forms/new_venue.html', form=form)


@venue_bp.route('/venues/create', methods=['POST'])
def create_venue_submission():
    form = VenueForm(request.form)

    if not form.validate():
        flash('An error occurred. Venue could not be listed.')
        return render_template('forms/new_venue.html', form=form)

    try:
        venue = Venue(
            name=form.name.data,
            city=form.city.data,
            state=form.state.data,
            address=form.address.data,
            phone=form.phone.data,
            image_link=form.image_link.data,
            facebook_link=form.facebook_link.data,
            website=form.website_link.data,
            genres=','.join(form.genres.data),
        )
        db.session.add(venue)
        db.session.commit()
        flash(f'Venue {venue.name} was successfully listed!')
    except Exception:
        db.session.rollback()
        flash('An error occurred. Venue could not be listed.')

    return redirect(url_for('index'))


@venue_bp.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
    venue = Venue.query.get_or_404(venue_id)
    form = VenueForm(obj=venue)
    return render_template('forms/edit_venue.html', form=form, venue=venue)


@venue_bp.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
    venue = Venue.query.get_or_404(venue_id)
    form = VenueForm(request.form)

    if not form.validate():
        flash('An error occurred. Venue could not be updated.')
        return render_template('forms/edit_venue.html', form=form, venue=venue)

    try:
        venue.name = form.name.data
        venue.city = form.city.data
        venue.state = form.state.data
        venue.address = form.address.data
        venue.phone = form.phone.data
        venue.image_link = form.image_link.data
        venue.facebook_link = form.facebook_link.data
        venue.website = form.website_link.data
        venue.genres = ','.join(form.genres.data)
        db.session.commit()
        flash(f'Venue {venue.name} was successfully updated!')
    except Exception:
        db.session.rollback()
        flash('An error occurred. Venue could not be updated.')

    return redirect(url_for('venues.show_venue', venue_id=venue.id))


@venue_bp.route('/venues/<int:venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
    venue = Venue.query.get_or_404(venue_id)
    try:
        db.session.delete(venue)
        db.session.commit()
    except Exception:
        db.session.rollback()

    return redirect(url_for('index'))
