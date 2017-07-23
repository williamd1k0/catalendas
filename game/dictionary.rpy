

screen dictionary:

    tag menu
    add im.Scale('gui/opened-book.png', 1280, 720)
    use navigation

    text _("{size=30}Dicionário{/size}"):
        xalign 0.3
        yalign 0.12

    default tt = Tooltip('')

    frame:
        xalign 0.5
        yalign 0.3
        background Frame('gui/b-box.png')
        style_group "dicio"
        has vbox

        textbutton "Bacurau":
            action tt.Action(_("O bacurau é uma ave caprimulgiforme da família caprimulgidae. Conhecido também como curiango, curiango-comum, ju-jau, amanhã-eu-vou (em Minas Gerais), ibijau, mede-léguas, acurana e a-ku-kú (nomes indígenas - Mato Grosso). O seu nome é onomatopaico e deriva de sua vocalização."))

        textbutton "Matinta Perera":
            action tt.Action(_("É uma personagem do folclore brasileiro, mais precisamente na região norte do país. Trata-se de uma velha que à noite se transforma em um pássaro agourento que pousa sobre os muros e telhados das casas e se põe a assobiar e só para quando o morador, já muito enfurecido pelo estridente assobio, lhe promete algo para que pare."))

        textbutton "Tupari":
            action tt.Action(_("Os Tuparis são um grupo indígena que habita o Sul do estado brasileiro de Rondônia, mais precisamente nas Áreas Indígenas Rio Branco e Rio Guaporé."))

    frame:
        xalign 0.5
        yalign 0.9
        xsize 700
        ysize 170
        background Frame('gui/b-box.png')
        vbox:
            text tt.value

init -2:

    style dicio_button:
        xminimum 200
        ymargin 5
