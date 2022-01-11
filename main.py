from feedgen.feed import FeedGenerator
from flask import Flask, Response, send_from_directory, redirect
from flask import url_for, render_template
from google.cloud import datastore
from google.auth.transport import requests
import google.oauth2.id_token

import datetime

SITE = 'https://radio-hills-rpg.rj.r.appspot.com/'

datastore_client = datastore.Client()

def store_time(dt):
    entity = datastore.Entity(key = datastore_client.key('visit'))
    entity.update({
        'timestamp': dt
    })

    datastore_client.put(entity)

def fetch_times(limit):
    query = datastore_client.query(kind='visit')
    query.order = ['-timestamp']
    times = query.fetch(limit=limit)
    return times

def fetch_episodios():
    query = datastore_client.query(kind='Episodio')
    query.order = ['-data_pub']
    episodios = list(query.fetch())
    return episodios

def get_episodio(id):
    query = datastore_client.query(kind='Episodio')
    query.add_filter('guid','=',id)
    episodio = list(query.fetch())
    print(episodio)
    if len(episodio) > 0:
        return episodio[0]
    return None

#from episodios import lista

app = Flask(__name__)

@app.template_filter('data_formatada')
def data_formatada(valor):
    return valor.strftime("%d/%m/%Y")

@app.route('/feed.xml')
def feeds():
    fg = FeedGenerator()
    fg.load_extension('podcast')
    fg.title('Radio Hills RPG')
    fg.description('Podcast sobre RPG do servidor Discord To the Hills!')
    fg.author({'name': 'Cleedee', 'email': 'claudiotorcato@gmail.com'})
    fg.link(href='https://radio-hills-rpg.rj.r.appspot.com/', rel='alternate')
    #fg.link(href='https://radio-hills-rpg.rj.r.appspot.com/feed.xml', rel='self', type='application/rss+xml')
    fg.subtitle('Podcast sobre RPG do servidor Discord To the Hills!')
    fg.logo('http://radio-hills-rpg.rj.r.appspot.com/static/img/logomarca_podcast.png')
    fg.language('pt-br')

    fg.podcast.itunes_category('Leisure','Games')
    fg.podcast.itunes_owner(name='Cleedee',email='claudiotorcato@gmail.com')
    fg.podcast.itunes_author('To The Hills!')
    fg.podcast.itunes_image('http://radio-hills-rpg.rj.r.appspot.com/static/img/logomarca_podcast.png')
    fg.podcast.itunes_subtitle('Podcast sobre RPG do servidor Discord To the Hills!')
    fg.podcast.itunes_explicit(itunes_explicit='no')

    lista = fetch_episodios()

    for episodio in lista:
        fe = fg.add_entry()
        fe.guid(episodio['guid'] if episodio['guid'] else episodio['arquivo'])
        fe.title(episodio['titulo'])
        fe.published(published=episodio['data_pub'])
        fe.link(href=SITE + 'post/' + episodio['guid'])
        #fe.enclosure(episodio['arquivo'], str(episodio['tamanho']), 'audio/mpeg')
        fe.enclosure(SITE + 'download/' + episodio['guid'] , str(episodio['tamanho']), 'audio/mpeg')
        fe.description(description=episodio['descricao'], isSummary=True)
        #fe.podcast.itunes_summary(episodio['descricao'])
        fe.podcast.itunes_explicit(itunes_explicit='no')
        fe.podcast.itunes_duration(episodio['duracao'])
    return Response(fg.rss_str(pretty=True), mimetype='application/rss+xml')

firebase_request_adapter = requests.Request()
@app.route('/')
def index():
    lista = fetch_episodios()
    return render_template('index.html', lista = lista)

@app.route('/post/<id>')
def post(id):
    episodio = get_episodio(id)
    return render_template('post.html', episodio = episodio)

@app.route('/download/<id>')
def download(id):
    with datastore_client.transaction():
        episodio = get_episodio(id)
        total = 0
        try:
            total = episodio['downloads']
            total += 1
            episodio.update({'downloads': total})
        except KeyError as e:
            episodio.update({'downloads': 1})
        finally:
            datastore_client.put(episodio)
        return redirect(episodio['arquivo'])

@app.route('/googleb0a3e3797d19d931.html')
def propriedade():
    return render_template('googleb0a3e3797d19d931.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
    
