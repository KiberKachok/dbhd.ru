from flask import Flask, render_template, redirect, url_for
from data import Film, Actor, db_session
from Forms import add_film_form, add_actor_form, search_form
from modhash import is_moderator
from kinopoisk.movie import Movie
# from flask_sitemap import Sitemap

app = Flask(__name__)
# ext = Sitemap(app=app)
app.config['SECRET_KEY'] = 'drunken_key'
db_session.global_init("db/pie.sqlite")
WTF_CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = 'a random string'


def main():
    app.run()

@app.route('/add_film', methods=['GET', 'POST'])
def add_film():
    form = add_film_form.AddFilmForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        movie = Movie(id=form.kp_id.data)
        if_exist = False
        try:
            movie.get_content('main_page')
        except Exception:
            if_exist = False
        else:
            if_exist = True

        if if_exist and len(session.query(Film.Film).filter(Film.Film.kp_id == form.kp_id.data).all()) == 0:
            film = Film.Film(movie.id, movie.title, movie.title_en, movie.plot, movie.year)
            session.add(film)
            session.commit()

            session = db_session.create_session()
            actors_list = movie.actors
            actors_to_add = actors_list.copy()
            actors_list = list(map(str, actors_list))
            for actor in session.query(Actor.Actor).filter(Actor.Actor.name.in_(actors_list)):
                actors_list.remove(str(actor.name))
                if actor.films != None:
                    actor.films = str(actor.films) + str(film.id) + '/'
                else:
                    actor.films = str(film.id) + '/'
            for i in actors_list:
                actor = Actor.Actor(str(i))
                actor.films = str(film.id) + '/'
                session.add(actor)
            session.commit()

            session = db_session.create_session()
            actors_str = ""
            for i in actors_to_add:
                actor_id = str(session.query(Actor.Actor).filter(Actor.Actor.name == str(i)).first().id)
                actors_str += "/" + actor_id

            film = session.query(Film.Film).filter(Film.Film.id == film.id).first()
            if not film.actors:
                film.actors = actors_str
            else:
                film.actors = str(film.actors) + actors_str
            session.commit()
            return redirect('/add_film')
    return render_template("add_film.html", form=form)

@app.route('/lib/<index_name>', methods=['GET', 'POST'])
def watch(index_name):
    session = db_session.create_session()
    film = session.query(Film.Film).filter(Film.Film.id == index_name).first()
    actors = []

    for actor in session.query(Actor.Actor).filter(Actor.Actor.id.in_(str(film.actors).split('/'))):
        actors.append(actor)

    session.commit()
    return render_template("film.html", film=film, actors=actors)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = search_form.SearchForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        films = []
        actors = []

        for film in session.query(Film.Film).filter(Film.Film.title_lower.like('%' + form.search_request.data.lower() + '%')):
            films.append(film)

        for actor in session.query(Actor.Actor).filter(Actor.Actor.name_lower.like('%' + form.search_request.data.lower() + '%')):
            actors.append(actor)

        return render_template("search_results.html", films=films, count=len(films), actors=actors, count_acts=len(actors))
    return render_template("index.html", form=form)

# @ext.register_generator
# def index():
#     # Not needed if you set SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS=True
#     yield 'index', {}

@app.route('/acts/<index_name>', methods=['GET', 'POST'])
def actor_list(index_name):
    session = db_session.create_session()
    actor = session.query(Actor.Actor).filter(Actor.Actor.id == index_name).first()
    films_names = []
    films_ids = str(actor.films).split('/')

    for films_iter in session.query(Film.Film).filter(Film.Film.id.in_(films_ids)):
        films_names.append(films_iter)

    session.commit()
    return render_template("actor.html", actor=actor, films_names=films_names)

@app.route('/faq')
def faq():
    return render_template("faq.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    main()