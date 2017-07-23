
init python:

    gal = Gallery()

    gal.button("ceu-estrelado")
    gal.condition("persistent.ceu_estrelado")
    gal.image("bg_ceu_estrelado")

    gal.button("casa-catalendas")
    gal.condition("persistent.casa_preguica")
    gal.image("bg_casa_preguica")

    gal.button("tianoa-voando")
    gal.condition("persistent.tianoa_voando")
    gal.image("cg_tianoa_voando")

    gal.button("cipo-do-ceu")
    gal.condition("persistent.cipodoceu")
    gal.image("bg_cipo")

    gal.transition = dissolve


screen gallery:

    tag menu
    add im.Scale('gui/opened-book.png', 1280, 720)
    use navigation

    text _("{size=30}Galeria{/size}"):
        xalign 0.3
        yalign 0.12

    frame:
        xalign 0.5
        yalign 0.5
        style_group "gallery"

        has vbox

        grid 2 2:
            style_group "gallery"
            spacing 10
            add gal.make_button(
                "ceu-estrelado", im.Scale("bg/ceu-estrelado.png", 200, 112.5),
                im.Sepia(im.Scale("bg/ceu-estrelado.png", 200, 112.5)),
                xalign=0.5, yalign=0.5, ysize=150, ypadding=15
            )

            add gal.make_button(
            "casa-catalendas",
                im.Scale(im.Composite((1280, 720),
                    (675, 190), im.Scale('bg/casa-preguica-bg.png', 460, 392),
                    (0, 0), im.Scale('bg/casa-preguica-fore.png', 1280, 720),
                    (730, 232), im.Scale('preguica/normal.png', 430, 366),
                    (640, 320), im.Scale('preguinho/normal.png', 270, 280)
                ), 200, 112.5),
                im.Sepia(im.Scale(im.Composite((1280, 720),
                    (675, 190), im.Scale('bg/casa-preguica-bg.png', 460, 392),
                    (0, 0), im.Scale('bg/casa-preguica-fore.png', 1280, 720),
                    (730, 232), im.Scale('preguica/normal.png', 430, 366),
                    (640, 320), im.Scale('preguinho/normal.png', 270, 280)
                ), 200, 112.5)),
                xalign=0.5, yalign=0.5, ysize=150, ypadding=15
            )

            add gal.make_button(
            "tianoa-voando",
                im.Scale(im.Composite((1280, 720),
                    (0, 0), im.Scale('bg/tribo.png', 1280, 720),
                    (500, 300), im.FactorScale('misc/cabeca1.png', 0.5)
                ), 200, 112.5),
                im.Scale(im.Sepia(im.Composite((1280, 720),
                    (0, 0), im.Scale('bg/tribo.png', 1280, 720),
                    (500, 300), im.FactorScale('misc/cabeca1.png', 0.5)
                )), 200, 112.5),
                xalign=0.5, yalign=0.5, ysize=150, ypadding=15
            )

            add gal.make_button(
            "cipo-do-ceu",
                im.Scale('bg/cg-cipo.png', 200, 112.5),
                im.Sepia(im.Scale('bg/cg-cipo.png', 200, 112.5)),
                xalign=0.5, yalign=0.5, ysize=150, ypadding=15
            )


init -2:
    style gallery_frame:
        xpos 0.25
        ypos 0.2
        background Frame('gui/b-box.png')

    style gallery_button:
        top_margin 10
