
label a_fogueira:

    play music 'music/catalendas-casadocatalendas.ogg'
    scene bg_casa_preguicapp with dissolve

    show preguica livro at idealright, preguicay
    show preguinho espantado at idealleft, idealy
    with dissolve

    preguinho "E a cabeça pegou os dois índios?"
    preguica "Não, Preguinho. Eles eram espertos e velozes!!"

    preguinho "Ah, e o que aconteceu depois?"
    preguica "Eles foram correndo contar para o Pajé."

    preguinho "Ihh... O Pajé não acreditou neles e eles ficaram de castigo, não é?"
    show preguica pensando_livro at idealright, preguicay with dissolve
    preguica "Não senhor! Acreditou sim. E ficou furioso!"
    preguica "Todos ficaram furiosos."

    show preguinho normal at idealleft, idealy with dissolve
    preguinho "Ahh, pegaram a cabeça dela e jogaram tão alto que ela virou uma estrela, não foi?"
    show preguica livro at idealright, preguicay with dissolve
    preguica "Calma Preguinho, a história só está começando."

    show preguinho espantado at idealleft, idealy with dissolve
    preguinho "Ah... É que tá me dando um pouquinho de medo, Dona Preguiça..."
    show preguica pensando_livro at idealright, preguicay with dissolve
    preguica "Não precisa ter medo, Preguinho. Escuta o resto da história."

    show preguica livro at idealright, preguicay with dissolve
    preguica "Então, o Pajé teve uma ideia. Chamou todos da tribo e combinaram que naquela noite iam fazer uma festa."
    preguica "Todos foram pegar lenha e fizeram uma fogueira bem grande."

    call catavento('bg_tribo')
    $ storybook = 'opened'

    scene bg_tribo
    play music 'music/catalendas-mapinguari.ogg'

    narrator "O Pajé combinou que a festa só iria acontecer de manhã. Por isso, a fogueira ficou lá, prontinha pra ser queimada."
    narrator "Todos ficaram esperando."

    call ibelieveicanfly('xxl_rl', fly_wave_rl, 5)
label db:
    scene bg_tribofogo with fade
    show fagulha at fogo

    narrator "Então pegaram o corpo de Tianoá e colocaram na fogueira."

    show guatapapi desesperado at idealright, idealy with moveinright
    guatapapi "Tianoá! Tianoá! O que vocês estão fazendo com a minha amada?"

    show paje bravo at idealleft, idealy with moveinleft
    paje "Ela traiu nossa tribo, filho!"
    paje "Está roubando a comida dos outros índios!"

    show guatapapi serio at idealright, idealy with dissolve
    guatapapi "Mas Tianoá e eu nos amamos!"

    show indio1 normal at pajeleft, tianoay with moveinleft
    indio1 "A gente tá sabendo que ela perde a cabeça é por ti."
    show indio2 normalx behind paje at pajeright, tianoay with moveinleft
    indio2 "Vamos queimar esse corpo que já não te pertence."

    scene bg_tribofogo with fade
    show fagulha at fogo

    call ibelieveicanfly('xxl_lr', fly_wave_lr, 5)

    scene bg_tribofogo
    show fagulha at fogo

    show tianoa morrendo at idealleft, tianoay
    show paje bravox at idealright, idealy
    show indio1 normalx at pajeleftx, tianoay
    show indio2 normal behind paje at pajerightx, tianoay
    with fade

    call queima(0.1, 0.5)
    call queima(0.5, 0.1)
    call queima(0.7, 0.2)
    call queima(0.2, 0.3)
    call queima(0.6, 0.6)
    hide queima_txt

    play sound 'sfx/you-died.ogg'
    tianoa "Aaaaahhhh!!!"

    show guatapapi desesperado at pajerightxpp, idealy with moveinright
    guatapapi "Meu amor!! Meu amor!! Meu amooor!!"

    play sound 'sfx/fogueira.ogg' fadein 2.0
    scene black with fade
    call queima(0.5, 0.1)
    call queima(0.6, 0.6)
    call queima(0.7, 0.2)
    call queima(0.1, 0.5)
    call queima(0.2, 0.3)
    hide queima_txt
    stop sound fadeout 2.0
    stop music fadeout 2.0
    $ renpy.pause(2, hard=True)

    scene bg_ocanoite with fadehold
    play music 'music/catalendas-natribo2.ogg'

    show guatapapi triste at idealright, idealy with moveinright
    guatapapi "Já faz dois dias que Tianoá se foi..."
    guatapapi "Guatapapi não consegue dormir direito..."

    play sound 'sfx/bacurau1.ogg'
    show bacurau normal at bacuraupos with fadehold
    show guatapapi bravo at idealright, idealy with dissolve
    play sound 'sfx/bacurau2.ogg'
    $ renpy.pause(0.5, hard=True)


    guatapapi "Pássaro agourento! Guatapapi vai te matar!"

    show bacurau fala at bacurausay with dissolve
    bacurau "Não! Sou sua mulher, ainda apaixonada por ti, meu amor!"

    show guatapapi serio at idealright, idealy with dissolve
    guatapapi "Minha mulher não era assim!"
    bacurau "Fiquei assim depois que me queimaram, meu amor."
    bacurau "Vim te buscar!"

    show guatapapi bravo at idealright, idealy with dissolve
    guatapapi "Eu hein!"
    bacurau "Meu pai e meu irmão estão lá fora, vieram te convidar pra morar na aldeia lá no céu, lá é lindo."

    show guatapapi serio at idealright, idealy with dissolve
    guatapapi "Não sou de confiar em pássaro agourento, não."
    guatapapi "Como é que Guatapapi vai saber que tu não é um bacurau querendo me matar?"

    play sound 'sfx/cabeca-voadora.ogg'
    show bacurau flash1 at bacurausay
    $ renpy.pause(.2, hard=True)
    show bacurau flash2 at bacurausay
    $ renpy.pause(.2, hard=True)
    show bacurau flash3 at bacurausay
    $ renpy.pause(.2, hard=True)

    show tianoa ghost2 at idealleft, tianoay
    hide bacurau
    with flash
    stop sound fadeout 1.0

    tianoa "Está satisfeito agora?"

    show guatapapi normal at idealright, idealy with dissolve
    guatapapi "Tianoá? Meu amor!"

    show tianoa ghost1 at idealleft, tianoay with dissolve
    tianoa "Meu pai fez um cipó pra gente subir lá pro céu."

    play music "music/catalendas-natribo1.ogg"
    scene bg_cipo with fade

    tianoa "Vamos, meu amor! Vamos!"
    $ persistent.cipodoceu = True

    narrator "Os parentes de Tianoá a transformaram em uma estrela."
    narrator "Quando alguém mata uma pessoa na Terra, acende uma luz no céu."
    narrator "E Tianoá, em forma de bacurau, desce pra comer a carne de quem foi assassinado."

    stop music fadeout 1.0

    return


image queima_txt = Text(_("QUEIMA!"))
label queima(x, y):
    show queima_txt:
        xalign x
        yalign y
    with dissolve
    with Pause(0.7)
    return
