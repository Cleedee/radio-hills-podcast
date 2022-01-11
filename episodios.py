from datetime import datetime, timedelta, timezone

fuso_horario = timezone( timedelta(hours=-3))

class Episodio:
    def __init__(self, titulo, descricao, arquivo, data_pub, tamanho, duracao,
        guid=None):
        self.titulo = titulo
        self.descricao = descricao
        self.arquivo = arquivo
        self.data_pub = data_pub
        self.tamanho = tamanho
        self.duracao = duracao
        self.guid = guid

lista = [
    Episodio(
        'RH #3 - Aprenda FATE Básico - As perícias e os dados FATE',
        """
Chegamos ao terceiro episódio do Radio Hills, o podcast do To The Hills!, servidor Discord dedicado ao Tabletop RPG. Nesse episódio iniciamos uma série de episódios apresentando o sistema FATE.

Ainda estamos na etapa de aprendizado na edição de áudio, então releve a inabilidade do editor!

Música de Abertura: Mission Ready - Ketsa

Música de Encerramento: Life Ilussion - Ketsa
        """,
        'https://mcdn.podbean.com/mf/download/xwglsn/radio_hills_ep03.mp3',
        datetime(2020, 6, 14, 23, tzinfo=fuso_horario),
        15681408,
        '16:42'
    ),
    Episodio(
        'RH #4 - Aprenda FATE Básico - As Quatro Resoluções e As Quatro Ações',
        """
Segunda parte da série Aprenda FATE Básico. Desta vez tratamos das quatro ações possíveis no FATE: Superar, Criar Vantagem, Atacar e Defender.

Falamos também dos resultados possíveis em um teste de Perícia: falha, empate, sucesso e sucesso com estilo.

Música de Abertura: Mission Ready - Ketsa

Música de Encerramento: Life Ilussion - Ketsa
        """,
        'https://mcdn.podbean.com/mf/download/6t2tay/radio_hills_ep04.mp3',
        datetime(2020, 6, 15, 23, tzinfo=fuso_horario),
        17191470,
        '21:07'
    ),
    Episodio(
        'RH #5 - Aprenda FATE Básico - Um Pouco de Aspectos',
        """
É o terceiro episódio da série Aprenda FATE Básico.

Nesse episódio damos alguns exemplos de ações que interagem com aspectos e de como os invocamos em nosso benefício.
        """,
        'https://mcdn.podbean.com/mf/download/lor456/radio_hills_ep05.mp3',
        datetime(2020, 6, 23, 23, tzinfo=fuso_horario),
        22612986,
        '23:34'
    ),
    Episodio(
        'RH #6 - Pré-vendas, Financiamentos e Jogos Baratos',
        """
A Herança de Cthulhu

NoteQuest

Cultos Inomináveis

Amigo Dragão
        """,
        'https://mcdn.podbean.com/mf/download/hulcng/radio_hills_ep06.mp3',
        datetime(2020, 6, 28, 23, tzinfo=fuso_horario),
        23207322,
        '23:09'
    ),
    Episodio(
        'RH #7 - Aprenda FATE Básico - Exemplos de Ações Envolvendo Aspectos',
        """
Saudações!

No episódio de hoje, Sir Bargle encontra bandidos na estrada. O que aprenderemos com esse conflito? Ouça o episódio e comente.

Música de Abertura: Mission Ready - Ketsa

Música de Encerramento: Life Ilussion - Ketsa
        """,
        'https://mcdn.podbean.com/mf/download/6r9vhu/radio_hills_ep07.mp3',
        datetime(2020, 7, 7, 23, tzinfo=fuso_horario),
        18236236,
        '19:49'
    ),
    Episodio(
        'RH #8 - ENNIE Awards 2020 e Palpites - Parte 1',
        """
<a href="http://www.ennie-awards.com/blog/2020-nominees-and-judges-spotlight-winners/">ENNIE Awards 2020</a>

Nesse episódio comentamos algumas indicações em 7 categorias do prêmio máximo do RPG que é votado pelo público. Teremos uma parte 2 para fechar. Em todas as categorias demos nosso palpite sobre quem ganhará.

Música de Abertura: Mission Ready - Ketsa

Música de Encerramento: Life Ilussion - Ketsa
        """,
        'https://mcdn.podbean.com/mf/download/wbjqea/radio_hills_ep08.mp3',
        datetime(2020, 7, 13, 23, tzinfo=fuso_horario),
        20528866,
        '25:57'
    ),
    Episodio(
        'RH #9 - ENNIE Awards 2020 e Palpites - Parte 2',
        """
<p>Chegamos &agrave; &uacute;ltima parte dos nossos coment&aacute;rios e palpites para a premia&ccedil;&atilde;o deste ano.</p>
<p>&nbsp;</p>
<p>Entrem no nosso <a href="https://discord.gg/ysVYfxw">servidor Discord</a>.</p>
<p>&nbsp;</p>
<p><a href="http://www.ennie-awards.com/blog/2020-nominees-and-judges-spotlight-winners/">ENNIE Awards 2020</a></p>
<p>&nbsp;</p>
<p>M&uacute;sica de Abertura: Mission Ready - Ketsa</p>
<p>M&uacute;sica de Encerramento: Life Ilussion - Ketsa</p>
        """,
        'https://drive.google.com/file/d/1_jnYt_iR_QxcvX9OS5Hg12wbANFNaQ5H/view?usp=sharing',
        datetime(2020, 7, 20, 23, tzinfo=fuso_horario),
        32376778,
        '36:12'
    ),
    Episodio(
        "RH #10 - As Lâminas Estelares de Su'ul - Sessão 1",
        """
Primeira aventura gravada do servidor!
        """,
        'https://archive.org/download/radio_hills_ep10/radio_hills_ep10.mp3',
        datetime(2020, 7, 26, 23, tzinfo=fuso_horario),
        121839201,
        '98:59',
        10
    ),
    Episodio(
        "RH #11 - FATE e Suas Soluções Inovadoras",
        """
<div style="background-color:rgb(245,245,245);font-family:'Droid Sans Mono', monospace, monospace, 'Droid Sans Fallback';font-size:14px;line-height:19px;white-space:pre;"><font color="#448c27">Esse episódio teve a participação do Velho Lich do podcast FATE Masters<span style="white-space:pre;">	</span>que nos ajudou a elaborar algumas reflexões sobre alguns conceitos e mecânicas do FATE que consideramos inovadoras ou, no mínimo, influenciadoras.</font></div><div style="background-color:rgb(245,245,245);font-family:'Droid Sans Mono', monospace, monospace, 'Droid Sans Fallback';font-size:14px;line-height:19px;white-space:pre;"><font color="#448c27"><br></font></div><div style="background-color:rgb(245,245,245);font-family:'Droid Sans Mono', monospace, monospace, 'Droid Sans Fallback';font-size:14px;line-height:19px;white-space:pre;"><ul><li><font color="#448c27"><a href="https://discord.gg/FnqYJv6" rel="nofollow">Movimento FATE Brasil no Discord</a></font></li><li><font color="#448c27"><a href="https://fatemasters.gitlab.io/" rel="nofollow">Podcast FATE Masters</a></font></li><li><a href="https://discord.gg/ysVYfxw" rel="nofollow">To The Hills!</a></li><li><a href="http://station53.blogspot.com/2014/07/avengers-accelerated-invasion-begins.html" rel="nofollow">Avengers Accelerated!</a></li><li><a href="https://machineage.itch.io/ihunt-the-rpg" rel="nofollow">#iHunt</a></li><li><a href="http://solarentretenimento.com.br/loja/bukatsu/52-bukatsu.html" rel="nofollow">Bukatsu!</a></li></ul></div>
        """,
        'https://archive.org/download/radio_hills_ep11/radio_hills_ep11.mp3',
        datetime(2020, 8, 3, 23, tzinfo=fuso_horario),
        66457425,
        '58:08',
        11
    ),
    Episodio(
        "RH #12 - As Lâminas Estelares de Su'ul - Sessão 2",
        """
<p>Segunda parte da aventura para FATE Acelerado no cenário Mestres de Umdaar</p>

<p>Música de Abertura: Mission Ready - Ketsa</p>

<p>Música Introdutória: Broken Hearted - Ketsa</p>

<p>Música de Encerramento: Life Illusion - Ketsa</p>
        """,
        'https://archive.org/download/radio_hills_ep12/radio_hills_ep12.mp3',
        datetime(2020, 8, 9, 23, tzinfo=fuso_horario),
        115428909,
        '86:20',
        '12'
    )    
]