# Este archivo se encuentra en el dominio público. Puede ser modificado
# libremente como base para tus propias pantallas.

##############################################################################
# Diálogo
#
# Pantalla utilizada para presentar el diálogo en modo adv.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    # Valores por defecto de 'side_image' y 'two_window'
    default side_image = None
    default two_window = False

    # Opta entre las variantes de una ventana o dos ventanas.
    if not two_window:

        # Una ventana.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # Dos ventanas.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # Si hay una imagen lateral, la presenta sobre el texto.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Usa el menú de acceso rápido.
    # use quick_menu


##############################################################################
# Elecciones
#
# Pantalla utilizada para presentar los menus dentro del juego.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Entrada
#
# Pantalla utilizada para la entrada de texto por parte del usuario.
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Pantalla utilizada para el diálogo y los menús en modo nvl.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Presenta el diálogo.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Presenta un menú, si lo hay.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu - Menú principal
#
# Pantalla utilizada para presentar el menú principal, cuando Ren'Py empieza
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:

    # Esta linea asegura que las otras pantallas de menú son reemplazadas.
    tag menu
    $ menumode = 'main'

    # Fondo del menú principal.
    window:
        style "mm_root"

    add im.Scale('gui/closed-book.png', 1280, 720)
    imagebutton:
        xpos .835
        ypos .1
        idle im.FactorScale('gui/b-comecar.png', 0.5)
        hover im.MatrixColor(im.FactorScale('gui/b-comecar.png', 0.5), im.matrix.saturation(.6)*im.matrix.tint(0.89, 0.84, 1.0)*im.matrix.brightness(0.2))
        focus_mask True
        action Start()

    imagebutton:
        xpos .836
        ypos .3
        idle im.FactorScale('gui/b-opcoes.png', 0.5)
        hover im.MatrixColor(im.FactorScale('gui/b-opcoes.png', 0.5), im.matrix.saturation(.6)*im.matrix.tint(0.89, 0.84, 1.0)*im.matrix.brightness(0.2))
        focus_mask True
        action ShowMenu("preferences")

    imagebutton:
        xpos .835
        ypos .5
        idle im.FactorScale('gui/b-extras.png', 0.5)
        hover im.MatrixColor(im.FactorScale('gui/b-extras.png', 0.5), im.matrix.saturation(.6)*im.matrix.tint(0.89, 0.84, 1.0)*im.matrix.brightness(0.2))
        focus_mask True
        action ShowMenu("extras")

    imagebutton:
        xpos .834
        ypos .8
        idle im.FactorScale('gui/b-sair.png', 0.5)
        hover im.MatrixColor(im.FactorScale('gui/b-sair.png', 0.5), im.matrix.saturation(.6)*im.matrix.tint(0.89, 0.84, 1.0)*im.matrix.brightness(0.2))
        focus_mask True
        action Quit(confirm=True)

    # Botones del menú principal.
    frame:
        style_group "mm"
        xalign .98
        yalign .98


        has vbox


        #textbutton _("Start Game") action Start()
        #textbutton _("Load Game") action ShowMenu("load")
        #textbutton _("Extras") action ShowMenu("extras")
        #textbutton _("Preferences") action ShowMenu("preferences")
        # textbutton _("Help") action Help()
        #textbutton _("Quit") action Quit(confirm=True)

init -2:

    # Ajusta todos los botones del menú principal al mismo tamaño.
    style mm_button:
        size_group "mm"



##############################################################################
# Navegación
#
# Pantalla incluida en otras pantallas para presentar las opciones de
# navegación y el fondo en los menús del juego.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:


    # Fondo de los menús del juego.
    window:
        style "gm_root"
    # if storybook == 'closed':
    #     add "gm_bg1.png"
    # else:
    #     add "gm_bg2.png"

    # Botones de navegación.
    imagebutton:
        xpos .835
        ypos .1
        idle im.FactorScale('gui/b-voltar.png', 0.5)
        hover im.MatrixColor(im.FactorScale('gui/b-voltar.png', 0.5), im.matrix.saturation(.6)*im.matrix.tint(0.89, 0.84, 1.0)*im.matrix.brightness(0.2))
        focus_mask True
        action Return()

    imagebutton:
        xpos .836
        ypos .3
        idle im.FactorScale('gui/b-opcoes.png', 0.5)
        hover im.MatrixColor(im.FactorScale('gui/b-opcoes.png', 0.5), im.matrix.saturation(.6)*im.matrix.tint(0.89, 0.84, 1.0)*im.matrix.brightness(0.2))
        selected_idle im.MatrixColor(im.FactorScale('gui/b-opcoes.png', 0.5), im.matrix.saturation(.6)*im.matrix.tint(0.89, 0.84, 1.0)*im.matrix.brightness(0.0))
        focus_mask True
        action ShowMenu("preferences")

    imagebutton:
        xpos .835
        ypos .5
        idle im.FactorScale('gui/b-extras.png', 0.5)
        hover im.MatrixColor(im.FactorScale('gui/b-extras.png', 0.5), im.matrix.saturation(.6)*im.matrix.tint(0.89, 0.84, 1.0)*im.matrix.brightness(0.2))
        selected_idle im.MatrixColor(im.FactorScale('gui/b-extras.png', 0.5), im.matrix.saturation(.6)*im.matrix.tint(0.89, 0.84, 1.0)*im.matrix.brightness(0.0))
        focus_mask True
        action ShowMenu("extras")

    imagebutton:
        xpos .834
        ypos .8
        idle im.FactorScale('gui/b-sair.png', 0.5)
        hover im.MatrixColor(im.FactorScale('gui/b-sair.png', 0.5), im.matrix.saturation(.6)*im.matrix.tint(0.89, 0.84, 1.0)*im.matrix.brightness(0.2))
        focus_mask True
        if menumode == 'game':
            action MainMenu()
        else:
            action Quit(confirm=True)

    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        #textbutton _("Return") action Return()
        #textbutton _("Preferences") action ShowMenu("preferences")
        #textbutton _("Extras") action ShowMenu("extras")
        #textbutton _("Save Game") action ShowMenu("save")
        #textbutton _("Load Game") action ShowMenu("load")
        #textbutton _("Main Menu") action MainMenu()
        # textbutton _("Help") action Help()
        #textbutton _("Quit") action Quit()

init -2:

    # Todos los botones del menú de navegación del mismo tamaño
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Guardar, Cargar
#
# Pantallas que permiten al usuario guardar y cargar las partidas.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Ya que guardar y cargar son muy similares, se combinan en una sola
# pantalla, selector de archivo ('file_picker'). Esa se usa desde
# simples pantallas de guardado y carga.

screen file_picker:

    frame:
        style "file_picker_frame"

        has vbox

        # Los botones superiores permiten al usuario escoger entre
        # páginas de archivos.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Presenta una cuadrícula de espacios para archivos.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Presenta diez espacios para archivos, numerados de 1 a 10.
            for i in range(1, columns * rows + 1):

                # Cada espacio es un botón.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Añade la captura de pantalla.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)

# Vai ser substituido por um pause-game
screen save:

    # Esta linea asegura que las otras pantallas de menú son reemplazadas.
    $ FileTakeScreenshot()
    tag menu
    if storybook == 'closed':
        add im.Scale('gui/closed-book.png', 1280, 720)
    else:
        add im.Scale('gui/opened-book.png', 1280, 720)

    use navigation

    if storybook == 'opened':
        add FileCurrentScreenshot():
            size (620,349)
            xalign .5
            yalign .5

        add 'vfx/overlay.png':
            size (620,349)
            xalign .5
            yalign .5


    #use file_picker

screen extras:

    tag menu
    add im.Scale('gui/opened-book.png', 1280, 720)
    use navigation

    text "{size=30}Extras{/size}":
        xalign 0.3
        yalign 0.12

    frame:
        style_group 'extras'
        background Frame('gui/b-box.png')
        xalign 0.35
        ypos 0.2
        has vbox

        textbutton _("Musics") action ShowMenu("music_room")
        null height 20
        textbutton _("Gallery") action ShowMenu("gallery")
        null height 20
        textbutton _("Dictionary") action ShowMenu("dictionary")
        null height 20
        textbutton _("Credits") action ShowMenu("credits")

init -2:

    style extras_button:
        xminimum 250
        yminimum 35


screen credits:

    tag menu
    add im.Scale('gui/opened-book.png', 1280, 720)
    use navigation

    text "{size=30}Créditos{/size}":
        xalign 0.3
        yalign 0.12

    frame:
        style_group 'credits'
        background Frame('gui/b-box.png')
        xalign 0.54
        ypos 0.25
        has vbox
        text "{size=+10}Programa: William Tumeo\n      {a=https://github.com/williamd1k0}GitHub{/a}\n      {a=https://twitter.com/williamd1k0}@williamd1k0{/a}{/size}"
        text "\n{size=+10}Arte: Ana \"Yomiell\"\n      {a=https://www.facebook.com/ArtistYomiell}Facebook{/a}\n      {a=https://twitter.com/Yomiell}@Yomiell{/a}{/size}"
        text "\n{size=+10}Áudio: Vinícius Kleinsorgen\n      {a=https://soundcloud.com/viniciuskps}SoundCloud{/a}\n      {a=https://twitter.com/viniciuskps}@viniciuskps{/a}{/size}"


# Backup
# screen save:
#
#     # Esta linea asegura que las otras pantallas de menú son reemplazadas.
#     tag menu
#
#     use navigation
#     use file_picker

screen load:

    # Esta linea asegura que las otras pantallas de menú son reemplazadas.
    tag menu

    use navigation
    #use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


##############################################################################
# Opciones
#
# Pantalla que permite al usuario cambiar las opciones.
# http://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences:

    tag menu

    # Incluye la navegación.
    add im.Scale('gui/opened-book.png', 1280, 720)
    use navigation

    text "{size=30}Configurações{/size}":
        xalign 0.3
        yalign 0.12

    # Coloca las columnas de navegación en una cuadrícula de anchura 3.
    #grid 2 1:
    #    style_group "prefs"
    #    xfill True

        # Columna izquierda.
    vbox:
        xalign 0.5
        yalign 0.6
        xmaximum 0.5
        frame:
            style_group "pref"
            has vbox

            label _("Display")
            textbutton _("Window") action Preference("display", "window")
            textbutton _("Fullscreen") action Preference("display", "fullscreen")

        frame:
            style_group "pref"
            has vbox

            label _("Idioma")
            textbutton _("Português") action Function(renpy.change_language, None)
            textbutton _("Inglês") action Function(renpy.change_language, "english")

            # frame:
            #     style_group "pref"
            #     has vbox
            #
            #     label _("Transitions")
            #     textbutton _("All") action Preference("transitions", "all")
            #     textbutton _("None") action Preference("transitions", "none")

        # frame:
        #     style_group "pref"
        #     has vbox
        #
        #     label _("Text Speed")
        #     bar value Preference("text speed")


        # vbox:
            # frame:
            #     style_group "pref"
            #     has vbox
            #
            #     label _("Skip")
            #     textbutton _("Seen Messages") action Preference("skip", "seen")
            #     textbutton _("All Messages") action Preference("skip", "all")

            # frame:
            #     style_group "pref"
            #     has vbox
            #
            #     textbutton _("Begin Skipping") action Skip()

            # frame:
            #     style_group "pref"
            #     has vbox
            #
            #     label _("After Choices")
            #     textbutton _("Stop Skipping") action Preference("after choices", "stop")
            #     textbutton _("Keep Skipping") action Preference("after choices", "skip")

            # frame:
            #     style_group "pref"
            #     has vbox
            #
            #     label _("Auto-Forward Time")
            #     bar value Preference("auto-forward time")
            #
            #     if config.has_voice:
            #         textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

    # vbox:
    #     xalign 0.5
    #     yalign 0.7
    #     xmaximum 0.5
        frame:
            yalign .8
            style_group "pref"
            has vbox

            label _("Music Volume")
            bar value Preference("music volume")

        frame:
            yalign .7
            style_group "pref"
            has vbox

            label _("Sound Volume")
            bar value Preference("sound volume")

            if config.sample_sound:
                textbutton _("Test"):
                    action Play("sound", config.sample_sound)
                    style "soundtest_button"

        if config.has_voice:
            frame:
                style_group "pref"
                has vbox

                label _("Voice Volume")
                bar value Preference("voice volume")

                textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                if config.sample_voice:
                    textbutton _("Test"):
                        action Play("voice", config.sample_voice)
                        style "soundtest_button"
#
#        frame:
#            yalign 0.8
#            style_group "pref"
#            has vbox
#
#            textbutton _("Joystick...") action Preference("joystick")
#

init -2:
    style pref_frame:
        size 30
        xfill True
        xmargin 5
        top_margin 5
        xpadding 30
        ypadding 30
        background Frame('gui/b-box.png')

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0


##############################################################################
# Pregunta Sí/No
#
# Pantalla que pregunta al usuario una pregunta Sí/No.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:

    modal True

    window:
        style "gm_root"

    add Solid('#000a')

    frame:
        xmaximum 800
        xalign .5
        background Frame('gui/b-bg.png', 15, 15)
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

    # Clic derecho y escape responden "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        size 30
        layout "subtitle"


##############################################################################
# Quick Menu - Menú de acceso rápido
#
# Pantalla incluida por defecto en la pantalla de diálogo, que añade acceso
# rápido a una serie de funciones útiles.
screen quick_menu:
    pass
    # Añade un menú de acceso rápido interno al juego.
    # hbox:
    #     style_group "quick"
    #
    #     xalign 1.0
    #     yalign 1.0
    #
    #     textbutton _("Back") action Rollback()
    #     textbutton _("Save") action ShowMenu('save')
    #     textbutton _("Q.Save") action QuickSave()
    #     textbutton _("Q.Load") action QuickLoad()
    #     textbutton _("Skip") action Skip()
    #     textbutton _("F.Skip") action Skip(fast=True, confirm=True)
    #     textbutton _("Auto") action Preference("auto-forward", "toggle")
    #     textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"


# Skip suppress
screen suppress_ctrl(time=5.0):
    modal True
    key "K_RCTRL" action NullAction()
    key "K_LCTRL" action NullAction()
    add ui.timer(time, Hide('suppress_ctrl'))

screen process_book:
    add ui.timer(1.0, [ShowMenu()])


screen book_overlay:

    python:
        def show_book():
            global menubook
            renpy.checkpoint()
            ui.timer(0.1, Hide('say'))
            ui.timer(0.3, ShowMenu())
            menubook = True

        def hide_book():
            global menubook
            ui.timer(0.2, ShowMenu())
            ui.timer(1.0, Function(renpy.rollback()))
            menubook = False

    key 'game_menu':
        if not menubook:
            action [Function(show_book)]
        else:
            action [Function(hide_book)]
