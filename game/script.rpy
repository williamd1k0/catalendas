
init -15 python:
    storybook = 'closed'
    menumode = 'main'
    menubook = False

    char_sizes = {
        'preguica': (762, 650),
        'preguinho': (529, 550),
        'paje': (442, 700),
        'guatapapi': (421, 700),
        'tianoa': (473, 750),
        'indio1': (457, 700),
        'indio2': (457, 700),
        'bacurau': (300, 255)
    }


define narrator = Character(None, window_style="centered_window", what_style="centered_text", what_prefix='"', what_suffix='"')

# Dona Preguiça
define preguica = Character("Dona Preguiça", color="#802d4b")
image preguica normal = im.Composite(char_sizes['preguica'],
    (0, 0), im.Scale('preguica/normal.png', *char_sizes['preguica'])
)
image preguica normalx = im.Flip(im.Composite(char_sizes['preguica'],
    (0, 0), im.Scale('preguica/normal.png', *char_sizes['preguica'])
), horizontal=True)
image preguica pensando = im.Composite(char_sizes['preguica'],
    (0, 0), im.Scale('preguica/pensando.png', *char_sizes['preguica'])
)
image preguica explicando = im.Composite(char_sizes['preguica'],
    (0, 0), im.Scale('preguica/explicando.png', *char_sizes['preguica'])
)
image preguica livro = im.Composite(char_sizes['preguica'],
    (0, 0), im.Scale('preguica/livro.png', *char_sizes['preguica'])
)
image preguica pensando_livro = im.Composite(char_sizes['preguica'],
    (0, 0), im.Scale('preguica/pensando-livro.png', *char_sizes['preguica'])
)
image preguica tchau = im.Composite(char_sizes['preguica'],
    (0, 0), im.Scale('preguica/tchau.png', *char_sizes['preguica'])
)

# Preguinho
define preguinho = Character("Preguinho", color="#2487c4")
image preguinho normal = im.Composite(char_sizes['preguinho'],
    (0, 0), im.Scale('preguinho/normal.png', *char_sizes['preguinho'])
)
image preguinho apontando = im.Composite(char_sizes['preguinho'],
    (0, 0), im.Scale('preguinho/apontando.png', *char_sizes['preguinho'])
)
image preguinho espantado = im.Composite(char_sizes['preguinho'],
    (0, 0), im.Scale('preguinho/espantado.png', *char_sizes['preguinho'])
)
image preguinho espantadopp = im.Composite(char_sizes['preguinho'],
    (0, 0), im.Scale('preguinho/espantado.png', *char_sizes['preguinho'])
)
image preguinho medo = im.Composite(char_sizes['preguinho'],
    (0, 0), im.Scale('preguinho/espantado.png', *char_sizes['preguinho'])
)
image preguinho medox = im.Composite(char_sizes['preguinho'],
    (0, 0), im.Flip(im.Scale('preguinho/espantado.png', *char_sizes['preguinho']), horizontal=True)
)
image preguinho aponta = im.FactorScale('preguinho/aponta.png', 0.5)

# Pajé
define paje = Character("Pajé", color="#a72727")
image paje normalx = im.Flip(im.Composite(char_sizes['paje'],
    (0, 0), im.Scale('paje/normal.png', *char_sizes['paje'])
), horizontal=True)
image paje bravo = im.Flip(im.Composite(char_sizes['paje'],
    (0, 0), im.Scale('paje/nervouso.png', *char_sizes['paje'])
), horizontal=True)
image paje bravox = im.Composite(char_sizes['paje'],
    (0, 0), im.Scale('paje/nervouso.png', *char_sizes['paje'])
)

# Guatapapi
define guatapapi = Character("Guatapapi", color="#f96c3c")
image guatapapi normal = im.Composite(char_sizes['guatapapi'],
    (0, 0), im.Scale('guatapapi/normal.png', *char_sizes['guatapapi'])
)
image guatapapi serio = im.Composite(char_sizes['guatapapi'],
    (0, 0), im.Scale('guatapapi/serio.png', *char_sizes['guatapapi'])
)
image guatapapi sanguen = im.Composite(char_sizes['guatapapi'],
    (0, 0), im.Scale('guatapapi/sangue-normal.png', *char_sizes['guatapapi'])
)
image guatapapi sangue = im.Composite(char_sizes['guatapapi'],
    (0, 0), im.Scale('guatapapi/sangue.png', *char_sizes['guatapapi'])
)
image guatapapi desconfiado = im.Composite(char_sizes['guatapapi'],
    (0, 0), im.Scale('guatapapi/desconfiado.png', *char_sizes['guatapapi'])
)
image guatapapi triste = im.Composite(char_sizes['guatapapi'],
    (0, 0), im.Scale('guatapapi/triste.png', *char_sizes['guatapapi'])
)
image guatapapi bravo = im.Composite(char_sizes['guatapapi'],
    (0, 0), im.Scale('guatapapi/bravo.png', *char_sizes['guatapapi'])
)
image guatapapi desesperado = im.Composite(char_sizes['guatapapi'],
    (0, 0), im.Scale('guatapapi/desesperado.png', *char_sizes['guatapapi'])
)

# Tianoá
define tianoa = Character("Tianoá", color="#e63660")
image tianoa normal = im.Composite(char_sizes['tianoa'],
    (0, 0), im.Scale('tianoa/normal.png', *char_sizes['tianoa'])
)
image tianoa normal2 = im.Composite(char_sizes['tianoa'],
    (0, 0), im.Scale('tianoa/normal-alt.png', *char_sizes['tianoa'])
)
image tianoa morrendo = im.Composite(char_sizes['tianoa'],
    (0, 0), im.Scale('tianoa/morrendo.png', *char_sizes['tianoa'])
)
image tianoa ghost1 = im.Composite(char_sizes['tianoa'],
    (0, 0), im.Recolor(
        im.MatrixColor(
            im.Scale('tianoa/normal.png', *char_sizes['tianoa']),
            im.matrix.saturation(.6)*im.matrix.tint(0.89, 0.84, 1.0)*im.matrix.brightness(0.2)
        ), 255, 255, 255, 180
    )
)
image tianoa ghost2 = im.Composite(char_sizes['tianoa'],
    (0, 0), im.Recolor(
        im.MatrixColor(
            im.Scale('tianoa/normal-alt.png', *char_sizes['tianoa']),
            im.matrix.saturation(.6)*im.matrix.tint(0.89, 0.84, 1.0)*im.matrix.brightness(0.2)
        ), 255, 255, 255, 180
    )
)

# Índios
define indio1 = Character("Índio fofoqueiro" , color="#2d357d")
image indio1 normal = im.Composite(char_sizes['indio1'],
    (0, 0), im.Scale('misc/indio.png', *char_sizes['indio1'])
)
image indio1 normalx = im.Flip(im.Composite(char_sizes['indio1'],
    (0, 0), im.Scale('misc/indio.png', *char_sizes['indio1'])
), horizontal=True)
image indio1 cruzado = im.Composite(char_sizes['indio1'],
    (0, 0), im.Scale('misc/indio-x.png', *char_sizes['indio1'])
)

define indio2 = Character("Índio fuxiqueiro", color="#5b7e2a")
image indio2 normal = im.Flip(im.Composite(char_sizes['indio2'],
    (0, 0), im.MatrixColor(
        im.Scale('misc/indio.png', *char_sizes['indio2']),
        im.matrix.saturation(1.0)*im.matrix.tint(0.8, 0.7, 0.7)*im.matrix.brightness(0.0)
    )
), horizontal=True)
image indio2 normalx = im.Composite(char_sizes['indio2'],
    (0, 0), im.MatrixColor(
        im.Scale('misc/indio.png', *char_sizes['indio2']),
        im.matrix.saturation(1.0)*im.matrix.tint(0.8, 0.7, 0.7)*im.matrix.brightness(0.0)
    )
)
image indio2 cruzado = im.Flip(im.Composite(char_sizes['indio2'],
    (0, 0), im.MatrixColor(
        im.Scale('misc/indio-x.png', *char_sizes['indio2']),
        im.matrix.saturation(1.0)*im.matrix.tint(0.8, 0.7, 0.7)*im.matrix.brightness(0.0)
    )
), horizontal=True)
image indio2 eita = im.Composite(char_sizes['indio2'],
    (0, 0), im.MatrixColor(
        im.Scale('misc/indio-eita.png', *char_sizes['indio2']),
        im.matrix.saturation(1.0)*im.matrix.tint(0.8, 0.7, 0.7)*im.matrix.brightness(0.0)
    )
)

# Bacurau
define bacurau = Character("Bacurau", color="#ffffff")
image bacurau normal = im.Composite(char_sizes['bacurau'],
    (0, 0), im.Scale('misc/bacurau.png', *char_sizes['bacurau'])
)
image bacurau fala = im.FactorScale('misc/bacurau.png', 0.5)
image bacurau flash1 = im.MatrixColor(
    im.FactorScale('misc/bacurau.png', 0.5),
    im.matrix.brightness(0.0)
)
image bacurau flash2 = im.MatrixColor(
    im.FactorScale('misc/bacurau.png', 0.5),
    im.matrix.brightness(0.5)
)
image bacurau flash3 = im.MatrixColor(
    im.FactorScale('misc/bacurau.png', 0.5),
    im.matrix.brightness(1.0)
)

# Musics
define music_intro = 'music/catalendas-abertura.ogg'
define music_casa = 'music/catalendas-casadocatalendas.ogg'

# SFX
define sfx_catavento = 'sfx/catalendas-catavento.ogg'

# Images
image disclaimer_txt = Text("{size=+12}{b}Aviso legal{/b}{/size}{vspace=20}{size=+10}Os personagens deste projeto não nos pertencem e nem suas imagens. {vspace=20}Este projeto não possui nenhuma relação com a {a=http://www.portalcultura.com.br/node/26}{b}TV Cultura{/b}{/a} e a {a=https://inbust.wordpress.com/}{b}Companhia In Bust{/b}{/a}, criadoras do programa de TV {i}Catalendas{/i}.{vspace=20}Projeto feito de fã para fã sem o objetivo de violar os direitos dos personagens e não possui fins lucrativos.{/size}", xmaximum=1000, align=(0.5,0.4))
image tupa_lua = im.Scale("tupa-lua.png", 250, 250)
image catavento_img = im.Scale("catavento.png", 1000, 1000)
image catavento_title = im.Scale("catavento.png", 500, 500)
image catavento_icon = im.Scale("catavento.png", 64, 64)
image titulo = im.Scale("titulo.png", 800, 300)
image classificacao = im.Scale("classificacao.png", 64, 64)
image star = im.Scale('vfx/star.png', 20, 20)
image cinturao = im.FactorScale('bg/estrelas.png', 0.6)
image maria1 = im.FactorScale(im.Crop('bg/estrelas.png', 44, 162, 77, 83), 0.6)
image maria2 = im.FactorScale(im.Crop('bg/estrelas.png', 154, 80, 102, 110), 0.6)
image maria3 = im.FactorScale(im.Crop('bg/estrelas.png', 264, 30, 82, 90), 0.6)
image maria4 = im.FactorScale(im.Crop('bg/estrelas.png', 20, 252, 37, 47), 0.6)
image white = Solid('#fff')
image black = Solid('#000')
image gray = Solid('#5d5d5d')
image green = Solid('#5d5')

# Bg
image bg_ceu_estrelado = im.Scale('bg/ceu-estrelado.png', 1280, 720)
image bg_ceu_estrelado_sc = im.Scale('bg/ceu-estrelado-sc.png', 1280, 720)
image bg_casa_preguica_disclaimer = im.Composite((1280, 720),
    (670, 190), im.Scale('bg/casa-preguica-bg.png', 470, 394),
    (0, 0), im.Scale('bg/casa-preguica-fore.png', 1280, 720)
)
image bg_casa_preguica = im.Composite((1280, 720),
    (670, 190), im.Scale('bg/casa-preguica-bg.png', 470, 394),
    (0, 0), im.Scale('bg/casa-preguica-fore.png', 1280, 720),
    (730, 232), im.Scale('preguica/normal.png', 430, 366),
    (640, 320), im.Scale('preguinho/normal.png', 270, 280)
)
image bg_casa_preguical = im.Composite((1280, 720),
    (670, 190), im.Scale('bg/casa-preguica-bg.png', 470, 394),
    (0, 0), im.Scale('bg/casa-preguica-fore.png', 1280, 720),
    (730, 230), im.Scale('preguica/livro.png', 430, 366),
    (640, 320), im.Scale('preguinho/normal.png', 270, 280)
)

image bg_casa_preguicapp = im.Composite((1280, 720),
    (670-292, 190-105), im.FactorScale(im.Scale('bg/casa-preguica-bg.png', 470, 394), 1.5),
    (0-630, 0-200), im.FactorScale(im.Scale('bg/casa-preguica-fore.png', 1280, 720), 1.5)
)

image bg_ocadia = im.Scale('bg/oca-dia.png', 1280, 720)
image bg_ocanoite = im.Scale('bg/oca-noite.png', 1280, 720)
image bg_tribo = im.Scale('bg/tribo.png', 1280, 720)
image bg_tribofogo = im.Scale('bg/tribo-fogo.png', 1280, 720)
image bg_cipo = im.Scale('bg/cg-cipo.png', 1280, 720)
image cg_tianoa_voando = im.Composite((1280, 720),
    (0, 0), im.Scale('bg/tribo.png', 1280, 720),
    (500, 300), im.FactorScale('misc/cabeca1.png', 0.5)
)

# Transforms
define flash = Fade(.25, 0.7, .75, color="#fff")
define fadehold = Fade(.25, 1.5, .75)

transform clock:
    subpixel True
    rotate 0
    linear 3.0 rotate 360
    repeat

transform cataventotitle:
    pause 5
    linear 1.0 zoom 0.5 ypos .7

transform titlepos:
    alpha 0.0
    ypos 0.3
    zoom 4
    pause 5
    alpha 1.0
    easein 1.0 zoom 1.0


transform left2right:
    xalign 8.0
    yalign .5
    linear 1.3 xalign -11.0

transform saindod:
    linear 2.0 xalign 5.0

transform saindoe:
    linear 2.0 xalign -5.0

transform press_start:
    ypos 0.95
    xpos 0.95
    linear 1.0 alpha .5
    linear 1.0 alpha 1.0
    repeat

transform bacuraupos:
    xalign 0.07
    yanchor 1.0
    yalign 0.5

transform bacurausay:
    yanchor 1.0
    yalign 1.5
    xalign -0.2

transform idealright:
    xalign 0.9

transform idealleft:
    xalign 0.1

transform pajeleft:
    xalign 0.0

transform pajeright:
    xalign 0.4

transform pajeleftx:
    xalign 1.0

transform pajerightx:
    xalign 0.6

transform pajerightxpp:
    xalign 0.55

transform idealy:
    yanchor 1.0
    yalign 1.4

transform tianoay:
    yanchor 1.0
    yalign 1.0

transform preguicay:
    yanchor 1.0
    yalign 1.9

transform tmaria1:
    xanchor 0.5
    yanchor 0.5
    xalign 0.382
    yalign 0.61

transform tmaria2:
    xanchor 0.5
    yanchor 0.5
    xalign 0.446
    yalign 0.545

transform tmaria3:
    xanchor 0.5
    yanchor 0.5
    xalign 0.503
    yalign 0.485

transform tmaria4:
    xanchor 0.5
    yanchor 0.5
    xalign 0.361
    yalign 0.675

transform orion1:
    linear 3.0 alpha 0.2
    linear 2.0 alpha 1.0
    repeat

transform orion2:
    linear 2.0 alpha 0.2
    linear 3.0 alpha 1.0
    repeat

transform orion3:
    linear 2.0 alpha 0.2
    linear 2.0 alpha 1.0
    repeat

transform orion(child):
    contains:
        child
        yalign 0.52
        xalign 0.4
        linear 3.0 alpha 0.2
        linear 2.0 alpha 1.0
        repeat
    contains:
        child
        yalign 0.5
        xalign 0.5
        linear 2.0 alpha 0.2
        linear 3.0 alpha 1.0
        repeat
    contains:
        child
        yalign 0.48
        xalign 0.6
        linear 2.0 alpha 0.2
        linear 2.0 alpha 1.0
        repeat


transform blur(child):
    contains:
        child
        alpha 1.0
    contains:
        child
        alpha 0.2 xoffset -3
    contains:
        child
        alpha 0.2 xoffset 3
    contains:
        child
        alpha 0.2 yoffset -3
    contains:
        child
        alpha 0.2 yoffset 3

transform zoom_blur(child):
    contains:
        child
        alpha 1.0
    contains:
        child
        alpha 0.2 zoom 1.015
    contains:
        child
        alpha 0.2 zoom 1.010
    contains:
        child
        alpha 0.2 zoom 0.995
    contains:
        child
        alpha 0.2 zoom 0.990

transform disclaimer:
    xalign 0.3

transform fly_wave_rl:
    yanchor 0.5
    xpos 1.0
    ypos 0.43
    linear 0.5 xpos 0.86 ypos 0.47
    linear 0.5 xpos 0.69 ypos 0.51
    linear 0.5 xpos 0.51 ypos 0.56
    linear 0.5 xpos 0.33 ypos 0.52
    linear 0.5 xpos 0.15 ypos 0.46
    linear 0.5 xpos 0.0 ypos 0.48
    linear 1.5 xpos -0.5 ypos 0.58

transform fly_wave_lr:
    yanchor 0.5
    xpos -0.5
    ypos 0.58
    linear 1.5 xpos 0.0 ypos 0.48
    linear 0.5 xpos 0.15 ypos 0.46
    linear 0.5 xpos 0.33 ypos 0.52
    linear 0.5 xpos 0.51 ypos 0.56
    linear 0.5 xpos 0.69 ypos 0.51
    linear 0.5 xpos 0.86 ypos 0.47
    linear 0.5 xpos 1.0 ypos 0.43


# Flying Tianoá
label ibelieveicanfly(name, transform_, time_):
    show expression 'flying_tianoa_'+name at transform_
    $ renpy.pause(time_, hard=True)
    return


init:
    python:
        def create_flying_tianoa(name, scale, flip_=True, animespeed=0.2):
            name = 'flying_tianoa_'+name
            if flip_ == True:
                renpy.image(name, Animation(
                    im.Flip(im.FactorScale('misc/cabeca1.png', scale), horizontal=True), animespeed,
                    im.Flip(im.FactorScale('misc/cabeca2.png', scale), horizontal=True), animespeed,
                    im.Flip(im.FactorScale('misc/cabeca3.png',scale), horizontal=True), animespeed
                ))
            else:
                renpy.image(name, Animation(
                    im.FactorScale('misc/cabeca1.png', scale), animespeed,
                    im.FactorScale('misc/cabeca2.png', scale), animespeed,
                    im.FactorScale('misc/cabeca3.png', scale), animespeed
                ))

    $ create_flying_tianoa('xl_rl', 0.3)
    $ create_flying_tianoa('xxl_rl', 0.4)
    $ create_flying_tianoa('xxxl_rl', 0.5)
    $ create_flying_tianoa('xl_lr', 0.3, False)
    $ create_flying_tianoa('xxl_lr', 0.4, False)
    $ create_flying_tianoa('xxxl_lr', 0.5, False)

image fagulha = im.Scale(im.Recolor(im.Crop('bg/estrelas.png', 20, 252, 37, 47), 255, 100, 100), 20, 20)
transform fogo(child):
    contains:
        child
        ypos 1.0
        xpos .5
        linear 1.0 ypos 0.5 xpos .6
        linear .8 ypos -0.1 xpos .5
        pause 2
        repeat

    contains:
        child
        ypos 1.0
        xpos .3
        linear 1.0 ypos 0.5 xpos .6
        linear .8 ypos -0.1 xpos .8
        pause 3
        repeat

    contains:
        child
        ypos 1.0
        xpos .4
        pause 1.5
        linear 1.0 ypos 0.6 xpos .2
        linear .8 ypos -0.1 xpos .3
        repeat

    contains:
        child
        ypos 1.0
        xpos .8
        pause 1
        linear 1.0 ypos 0.4 xpos .9
        linear .8 ypos -0.1 xpos .7
        repeat

    contains:
        child
        ypos 1.0
        xpos .1
        pause 1.6
        linear 1.0 ypos 0.4 xpos .3
        linear .8 ypos -0.1 xpos .2
        repeat

# Intro
label splashscreen:

    $ config.quit_action = Quit(confirm=False)

    transform iconpos:
        ypos 0.84
        xpos 0.9

    scene bg_casa_preguica_disclaimer

    show catavento_icon at iconpos, clock
    $ renpy.pause(3, hard=True)
    hide catavento_icon with dissolve

    show disclaimer_txt
    show classificacao at iconpos
    with dissolve
    $ renpy.pause(10, hard=True)

    scene white
    with dissolve
    play music music_intro
    show tupa_lua at truecenter
    with Pixellate(1, 7)
    if persistent.not_firstrun:
        $ renpy.pause(4)
    else:
        $ renpy.pause(4, hard=True)

    hide tupa_lua with dissolve

    scene bg_ceu_estrelado

    show catavento_title at truecenter, clock, cataventotitle
    with dissolve
    if persistent.not_firstrun:
        $ renpy.pause(4)
    else:
        $ renpy.pause(4, hard=True)

    show titulo at truecenter, titlepos

    if persistent.not_firstrun:
        $ renpy.pause(10)
    else:
        $ renpy.pause(10, hard=True)
        $ persistent.not_firstrun = True

    show text "{color=#fff}PRESSIONE START{/color}" at right, press_start

    # Aguarda interação
    centered ""
    hide titulo
    hide catavento_title
    hide text
    with dissolve

    $ config.quit_action = Quit(confirm=True)

    return


# Catavento
label catavento(bg):

    transform q:
        xpos -1.0
        linear 0.5 xpos -0.5
        linear 0.4 xpos 0.0

    play sound sfx_catavento
    $ renpy.pause(3, hard=True)
    show catavento_img at left2right, clock
    show expression bg behind catavento_img at q

    $ renpy.pause(3, hard=True)
    stop sound fadeout 1.0
    return


# Main
label start:

    $ menumode = 'game'
    #show screen book_overlay
    stop music fadeout 1.0
    scene white with dissolve
    $ renpy.pause(2.0, hard=True)

    show titulo:
        xalign 0.5
        yalign 0.3
    show text "A LENDA DA CABEÇA VOADORA":
        xalign 0.5
        yalign 0.7
    with dissolve
    $ renpy.pause(2.0, hard=True)


    call catavento('bg_ceu_estrelado')
    call as_estrelas
    $ storybook = 'opened'
    stop music fadeout 1.0
    call catavento('bg_ocanoite')
    call a_cabeca_voadora
    $ storybook = 'closed'
    call catavento('bg_casa_preguical')
    call a_fogueira
    $ storybook = 'closed'
    call catavento('bg_casa_preguica')
    call final
    call catavento('bg_ceu_estrelado')
    call credits_roll

    return
