from flask import Flask, render_template

app = Flask (__name__)

from models import livro, Genero, Autor

#CLASSES FEITAS NA POO
#OS OBJETOS PASSADOS SÃO DE ACORDO COM O QUE FOI CRIADO NO MODELS.PY
#POR EXEMPLO
#O PRIMEIRO TERMO (FRANZ KAFKA) REPRESENTA O SELF.NOME DA CLASSE AUTOR
#O SEGUNDO TERMO REPRESENTA A BIOGRAFIA, DE ACORDO COM OS PARAMETROS PASSADOS NO CONSTRUTOR DA CLASSE AUTOR
autor1 = Autor('Franz Kafka', 'Franz Kafka (1883–1924) foi um escritor judeu de língua alemã nascido em Praga, cuja obra influenciou profundamente a literatura modernista. Formado em Direito pela Universidade Carolina, trabalhou em uma seguradora até 1922, enquanto escrevia textos que combinavam realismo e fantasia, retratando personagens isolados em cenários burocráticos e opressivos. Entre suas obras mais conhecidas estão A Metamorfose (1915), O Processo (1925) e O Castelo (1926). Diagnosticado com tuberculose em 1917, morreu em 1924. Embora pouco reconhecido em vida, tornou-se célebre após sua morte graças à publicação póstuma de seus manuscritos por seu amigo Max Brod.', 1)
autor2 = Autor('Charles Bukowski', 'Charles Bukowski (1920–1994) foi um escritor e poeta americano de origem alemã, conhecido por seu estilo direto e autobiográfico. Sua obra retrata a vida marginal, o alcoolismo, o sexo e a solidão, com humor ácido e realismo cru. Criou o alter ego Henry Chinaski, presente em vários livros como Cartas na Rua e Misto-Quente. Tornou-se um ícone da literatura underground e morreu de leucemia aos 73 anos.', 2)
autor3 = Autor('Friedrich Nietzsche', 'Friedrich Nietzsche (1844–1900) foi um filósofo alemão cujas ideias influenciaram profundamente a filosofia moderna. Criticou a religião, a moral tradicional e o pensamento ocidental, propondo conceitos como “vontade de potência”, “eterno retorno” e o “além-do-homem” (Übermensch). Sua obra mais conhecida é Assim Falou Zaratustra (1883–85). Enfrentou problemas de saúde mental e física, sendo internado em 1889 e permanecendo incapacitado até sua morte em 1900. Após sua morte, sua filosofia ganhou ampla repercussão, influenciando diversas áreas do pensamento contemporâneo.', 3)

genero1 = Genero('ficção', 1)
genero2 = Genero('poesia contemporânea', 2)
genero3 = Genero('filosofia crítica', 3)

livro1 = livro('A metamorfose', 1915, 'A Metamorfose (1915), de Franz Kafka, é um conto que narra a história de Gregor Samsa, um caixeiro-viajante que acorda certa manhã transformado em um inseto gigante. Incapaz de se comunicar ou trabalhar, Gregor passa a viver isolado em seu quarto, sendo rejeitado pela própria família. A obra explora temas como a alienação, a desumanização e o peso das expectativas sociais, em uma narrativa marcada pelo absurdo e pela crítica à burocracia e aos laços familiares frágeis.', autor1, genero1, 1)
livro2 = livro('VOCÊ FICA TÃO SOZINHO ÀS VEZES QUE ATÉ FAZ SENTIDO', 2018, 'Você Fica Tão Sozinho às Vezes que Até Faz Sentido (1996) é uma coletânea de poemas de Charles Bukowski que explora temas como solidão, rotina, amor, sexo, alcoolismo e o absurdo da vida. Com linguagem direta e crua, Bukowski reflete sobre sua própria existência e a condição humana, sempre com um olhar cínico, melancólico e, por vezes, irônico. É uma obra intimista e brutalmente honesta, típica do estilo do autor.', autor2, genero2, 2)
livro3 = livro('Além do bem e do mal', 2018, 'Além do Bem e do Mal (1886), de Friedrich Nietzsche, é uma obra filosófica que critica a moral tradicional ocidental, especialmente a moral cristã, e propõe uma reavaliação dos valores. Nietzsche questiona noções absolutas de verdade, bem e mal, defendendo uma filosofia baseada na vontade de potência e na superação dos limites impostos pela moralidade herdada. O livro apresenta aforismos e reflexões que antecipam temas centrais do pensamento nietzschiano, como o além-do-homem (Übermensch) e a crítica à razão como instrumento de dominação.', autor3, genero3, 3)

autoreslist = [autor1, autor2, autor3]
livroslist = [livro1, livro2, livro3]
generoslist = [genero1, genero2, genero3]



#ROTAS
@app.route('/')
def home():
    return render_template('home.html', livros = livroslist)

@app.route('/livros')
def livros():
    return render_template('livros.html', livros = livroslist)

@app.route('/autores')
def autores():
    return render_template('autores.html', autores = autoreslist)

@app.route('/generos')
def generos():
    return render_template('generos.html', generos = generoslist)


#ID DAS ROTAS
#ALGUMAS ESTÃO COM ERROS, NÃO CONSEGUI RESOLVER TODAS, USA O CEREBRO AI DOG (SE EU RESOLVER NA PROVA ATUALIZO O CÓDIGO)
@app.route("/livros/<int:id>")
def livro(id):
    for livro in livroslist:
        if livro.id == id:
            return render_template("livros.html", livro=livro)
    return "<h1> Ops! Livro não encontrado para esse identificador</h1>"


@app.route("/autores/<int:id>")
def autor(id):
    for autor in autoreslist:
        if autor.id == id:
            return render_template("autores.html", autor=autor)
    return "<h1> Ops! Autor não encontrado para esse identificador</h1>"



@app.route("/generos/<int:id>")
def genero(id):
    for genero in generoslist:
        if genero.id == id:
            return render_template("generos.html", genero=genero)
    return "<h1> Ops! Genero não encontrado para esse identificador</h1>"

#ESSE NÃO PRECISA ENTENDER KKKKKKKK
#TLGD QUE TODAS AS ROTAS TAO IGUAIS, ENTÃO...
#SÓ TROCAR OS NOMES PELO OQUE VOCE QUER
