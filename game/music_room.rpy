
init python:

    mroom = MusicRoom(fadeout=1.0)
    game_musics = list()
    game_musics.append(("Track 1 - Abertura",'music/catalendas-abertura.ogg'))
    game_musics.append(("Track 2 - Casa do Catalendas",'music/catalendas-casadocatalendas.ogg'))
    game_musics.append(("Track 3 - Dona Preguiça",'music/catalendas-donapreguica.ogg'))
    game_musics.append(("Track 4 - Preguinho",'music/catalendas-preguinho.ogg'))
    game_musics.append(("Track 5 - Dicionário",'music/catalendas-dicionario.ogg'))
    game_musics.append(("Track 6 - Na Tribo 1",'music/catalendas-natribo1.ogg'))
    game_musics.append(("Track 7 - Na Tribo 2",'music/catalendas-natribo2.ogg'))
    game_musics.append(("Track 8 - Carimbó",'music/catalendas-carimbo.ogg'))
    game_musics.append(("Track 9 - Mapinguari",'music/catalendas-mapinguari.ogg'))
    game_musics.append(("Track 10 - Tupã",'music/catalendas-tupa.ogg'))
    game_musics.append(("Track 11 - Viração da Matinta",'music/catalendas-viracaodamatinta.ogg'))

    for ms in game_musics:
        mroom.add(ms[1])


screen music_room:

    tag menu
    add im.Scale('gui/opened-book.png', 1280, 720)
    use navigation

    text "{size=30}Músicas{/size}":
        xalign 0.3
        yalign 0.12

    frame:
        background Frame('gui/b-box.png')
        style_group "musicroom"
        xalign .525
        yalign .8
        has vbox

        python:
            for ms in game_musics:
                ui.textbutton(ms[0], mroom.Play(ms[1]))

        null height 20

        # Buttons that let us advance tracks.
        textbutton _("Next") action mroom.Next()
        textbutton _("Previous") action mroom.Previous()

init -2:

    style musicroom_button:
        top_margin 7
        xminimum 400
        yminimum 35
