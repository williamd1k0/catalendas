
init:


    python:
        credits_title = "{b}{size=+10}Catalendas", u"A Lenda da Cabeça Voadora{/size}{/b}"
        staff = {
            'programmer': 'William Tumeo',
            'art': 'Yomiell Z80',
            'sfx': u'Vinícius Kleinsorgen'
        }
        credits_list = [
            ('Elenco', [
                u'Dona Preguiça',
                'Preguinho',
                u'Pajé',
                'Guatapapi',
                u'Tianoá',
                u'Índio fofoqueiro',
                u'Índio fuxiqueiro'
            ]),
            (u'Direção de Arte', [
                staff['art']
            ]),
            ('Design de Personagens', [
                staff['art']
            ]),
            (u'Animações', [
                staff['art'],
                staff['programmer']
            ]),
            (u'Cenários', [
                staff['art']
            ]),
            ('GUI', [
                staff['programmer'],
                staff['art']
            ]),
            ('Programador Principal', [
                staff['programmer']
            ]),
            (u'Adaptação', [
                staff['programmer'],
                staff['art']
            ]),
            (u'Direção de Fotografia', [
                staff['programmer']
            ]),
            ('Efeitos Sonoros', [
                staff['sfx']
            ]),
            ('Revisão', [
                staff['sfx']
            ]),
            ('Agradecimentos Especiais', (
                'Pedro "Cogu" Casanova',
                'Emanuel Victor'
            ))
        ]

        roll_time = 50
        credits_str = credits_title[0]+'\n\n'+credits_title[1]

        for item in credits_list:
            credits_str += '\n\n\n{b}{size=32}'+item[0]+'{/size}{/b}\n\n'
            for i in item[1]:
                credits_str += '{size=30}'+i+'{/size}\n'

    image creditsroll = Text(credits_str, text_align=0.5)


label credits_roll:

    play music "<from 18>music/catalendas-abertura.ogg"
    scene bg_ceu_estrelado
    show creditsroll at Move((0.5, 4.5), (0.5, 0.0), roll_time, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    $ renpy.pause(roll_time+15, hard=True)

    return
