
label as_estrelas:

    #centered "As estrelas"
    scene bg_ceu_estrelado_sc
    play music 'music/catalendas-casadocatalendas.ogg'
    $ persistent.ceu_estrelado = True

    show maria1 at tmaria1, orion1
    show maria2 at tmaria2, orion2
    show maria3 at tmaria3, orion3
    show maria4 at tmaria4
    preguica "É aquele ali!"

    preguica "Aquele ali, Preguinho, é o Cinturão de Orion!"
    preguinho "Aahh... Não consigo ver nada, Dona Preguiça..."

    scene bg_casa_preguica with fade
    with Pause(1)
    $ persistent.casa_preguica = True

    scene bg_casa_preguicapp with dissolve

    show preguica explicando at idealright, preguicay with moveinright
    preguica "Ali Preguinho. Tens que te concentrar um pouco."

    show preguinho espantado at idealleft, idealy with moveinleft
    preguinho "Ah... Eu tô tentando mas eu não consigo, Dona Preguiça..."
    show preguica pensando at idealright, preguicay
    show preguinho normal at idealleft, idealy
    with dissolve
    preguinho "Do céu, eu só consigo ver... hmm... as Três Marias!"

    show preguica normal at idealright, preguicay with dissolve
    preguica "Pronto! É isso! As Três Marias fazem parte do Cinturão de Orion."
    preguica "Elas ficam bem no meio. O Cinturão é um quadrado."

    show preguinho espantado at idealleft, idealy with dissolve
    preguinho "Ah... Mas por que chamam d-de Cinturão de Orion? Não é, Dona Preguiça?"

    show preguica pensando at idealright, preguicay with dissolve
    preguica "Isso é uma antiga lenda, Preguinho. Todos os povos antigos tinham sua maneira de olhar o céu."
    show preguica normal at idealright, preguicay
    show preguinho normal at idealleft, idealy
    with dissolve
    preguica "Orion, por exemplo, é um caçador. Ele está no céu junto com duas outras constelações, a do Cão Maior, e a do Cão Menor."

    show preguinho espantado at idealleft, idealy with dissolve
    preguinho "Puxa, tem até cachorro no céu!?"

    show preguica explicando at idealright, preguicay with dissolve
    preguica "Não, Preguinho! As várias posições das estrelas é que formam figuras, inclusive de animais. Desde o início do mundo, o céu serviu de mapa, calendário e até relógio."

    show preguica normal at idealright, preguicay
    show preguinho espantadopp at idealleft, idealy
    with dissolve
    preguinho "Hã? Relógio?"
    show preguinho apontando at idealleft, idealy with dissolve
    preguinho "Olhando pra quarta Maria, Dona Preguiça, que horas tem?"

    show preguica pensando at idealright, preguicay with dissolve
    preguica "Quarta Maria??"

    preguinho "É! A senhora tá vendo, ó..."

    scene bg_ceu_estrelado_sc
    show maria1 at tmaria1, orion1
    show maria2 at tmaria2, orion2
    show maria3 at tmaria3, orion3
    show maria4 at tmaria4, orion2

    transform aponta_dedo:
        yanchor 1.0
        xanchor 0.5
        xalign 0.5
        yalign 1.2
        pause 1.5
        linear .5 rotate -16 xalign 0.485
        pause 1.0
        linear .5 rotate -39 xalign 0.456
        pause 1.0
        linear .5 rotate -50 xalign 0.445


    show preguinho aponta at aponta_dedo with moveinbottom
    preguinho "Uma...{w=1.0} duas...{w=1.0} três...{w=1.0} e aquela ali do lado é a quarta Maria!"

    scene bg_casa_preguicapp with dissolve
    show preguinho normal at idealleft, idealy
    show preguica pensando at idealright, preguicay
    with dissolve

    preguica "Não, Preguinho! São só três Marias mesmo. Aquela quarta estrela é outra coisa."
    show preguica normal at idealright, preguicay with dissolve
    preguica "Para os índios, por exemplo, ela é Panhaom."

    show preguinho espantado at idealleft, idealy with dissolve
    preguinho "Panhaom?"

    show preguica pensando at idealright, preguicay with dissolve
    preguica "É. Significa bacurau em Tupari."

    show preguinho espantadopp at idealleft, idealy with dissolve
    preguinho "Bacurau??"

    show preguinho normal at idealleft, idealy with dissolve
    preguica "É. Bacurau é um pássaro, Preguinho."

    show preguinho normal at idealleft, idealy with dissolve
    preguinho "Ahh, eu sei! Aquele que só sai à noite, igualzinho a Matinta Perera."

    show preguica explicando at idealright, preguicay with dissolve
    preguica "É. Aquela estrela ganhou esse nome por causa de Tianoá."

    show preguinho espantado at idealleft, idealy with dissolve
    preguinho "Ah, e quem foi Tianoá?"

    show preguica normal at idealright, preguicay with dissolve
    preguica "É uma antiga lenda Tupari. Tianoá ficou conhecida como A Cabeça Voadora."

    show preguinho espantadopp at idealleft, idealy with dissolve
    preguinho "Égua!! Uma cabeça que voa!!"

    show preguica pensando at idealright, preguicay with dissolve
    preguica "É. Deixe-me pegar o meu livro pra te contar essa lenda."
    show preguica normal at idealright, preguicay with dissolve
    show preguica normalx at idealright, preguicay, saindod

    show preguinho medo at idealleft, idealy with dissolve
    preguinho "Uuh... Uma cabeça que voa. Essa eu não tinha ouvido ainda!"

    return
