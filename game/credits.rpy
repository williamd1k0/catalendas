

# Defining credits manually because of a bug(?) with the tl method
define credits_str = _("""{b}{size=+10}Catalendas
\n
A Lenda da Cabeça Voadora{/size}{/b}
\n\n
{b}{size=32}Elenco{/size}{/b}
\n
{size=30}Dona Preguiça{/size}
{size=30}Preguinho{/size}
{size=30}Pajé{/size}
{size=30}Guatapapi{/size}
{size=30}Tianoá{/size}
{size=30}Índio fofoqueiro{/size}
{size=30}Índio fuxiqueiro{/size}
\n\n
{b}{size=32}Direção de Arte{/size}{/b}
\n
{size=30}Yomiell Z80{/size}
\n\n
{b}{size=32}Design de Personagens{/size}{/b}
\n
{size=30}Yomiell Z80{/size}
\n\n
{b}{size=32}Animações{/size}{/b}
\n
{size=30}Yomiell Z80{/size}
{size=30}William Tumeo{/size}
\n\n
{b}{size=32}Cenários{/size}{/b}
\n
{size=30}Yomiell Z80{/size}
\n\n
{b}{size=32}GUI{/size}{/b}
\n
{size=30}William Tumeo{/size}
{size=30}Yomiell Z80{/size}
\n\n
{b}{size=32}Programador Principal{/size}{/b}
\n
{size=30}William Tumeo{/size}
\n\n
{b}{size=32}Adaptação{/size}{/b}
\n
{size=30}William Tumeo{/size}
{size=30}Yomiell Z80{/size}
\n\n
{b}{size=32}Direção de Fotografia{/size}{/b}
\n
{size=30}William Tumeo{/size}
\n\n
{b}{size=32}Efeitos Sonoros{/size}{/b}
\n
{size=30}Vinícius Kleinsorgen{/size}
\n\n
{b}{size=32}Revisão{/size}{/b}
\n
{size=30}Vinícius Kleinsorgen{/size}
\n\n
{b}{size=32}Agradecimentos Especiais{/size}{/b}
\n
{size=30}Pedro "Cogu" Casanova{/size}
{size=30}Emanuel Victor{/size}""")

image creditsroll = Text(credits_str, text_align=0.5)


label credits_roll:

    play music "<from 18>music/catalendas-abertura.ogg"
    scene bg_ceu_estrelado

    show creditsroll at Move((0.5, 4.5), (0.5, 0.0), 50, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    $ renpy.pause(50+15, hard=True)

    return
