
label a_cabeca_voadora:

    play music 'music/catalendas-natribo1.ogg'
    scene bg_ocanoite

    narrator "Tianoá era a moça mais bonita da aldeia."
    narrator "Era casada com Guatapapi, filho do Pajé e um dos primeiros seres a existir no mundo."

    show paje normalx at idealleft, idealy with moveinleft
    paje "Hmmm... Pajé casou filho com moça boa! Bonita!"
    paje "Filho de Pajé vai ter descendentes fortes e bonitos!"
    paje "Raça de Pajé ficar para sempre na Terra."

    play music 'music/catalendas-mapinguari.ogg' fadein 1.0

    narrator "Mas tinha algo que o Pajé não sabia. Aliás, ninguém sabia."
    narrator "Todas as noites, a cabeça de Tianoá se desprendia do pescoço e voava pelas roças alheias e comia tudo o que via pela frente."

    scene bg_tribo with fade
    play sound "sfx/cabeca-voadora.ogg"
    call ibelieveicanfly('xl_rl', fly_wave_rl, 4)
    call ibelieveicanfly('xxl_lr', fly_wave_lr, 5)
    call ibelieveicanfly('xxxl_rl', fly_wave_rl, 4)

    $ persistent.tianoa_voando = True

    preguinho "Só a cabeça? E pra onde ia a comida??"
    preguica "Isso... ninguém sabia."

    narrator "Antes do amanhecer, a cabeça voltava e se colava novamente ao corpo de Tianoá."
    scene black with fade
    stop sound

    scene bg_ocadia with fade
    play music 'music/catalendas-natribo1.ogg'

    show guatapapi sanguen at idealright, idealy with moveinright
    guatapapi "Guatapapi vai caçar comida boa hoje, pra Tianoá comer!"

    show tianoa normal at idealleft, tianoay with moveinleft
    tianoa "Tianoá é feliz com Guatapapi, isso já basta pra barriga tá cheia."

    show guatapapi sangue at idealright, idealy with dissolve
    $ renpy.pause(0.5, hard=True)
    show guatapapi desconfiado at idealright, idealy with dissolve
    guatapapi "Estranho, Guatapapi todo dia acorda com esse sangue no peito."

    show guatapapi sangue at idealright, idealy
    show tianoa normal2 at idealleft, tianoay
    with dissolve
    tianoa "Mosquito. De noite Tianoá mata um monte em cima de Guatapapi."

    show guatapapi sanguen at idealright, idealy with dissolve
    guatapapi "Aah, meu amor!"


    scene bg_tribo with fade
    play music 'music/catalendas-natribo2.ogg'

    show indio1 normal at idealleft, tianoay with moveinleft
    indio1 "Hmm... Vamo saí daqui!"
    show indio2 cruzado at idealright, tianoay with moveinright
    indio2 "Quieto! Hoje eu descubro por que Guatapapi acorda com aquele sangue no peito!"

    indio1 "Tu achas que Tianoá teria coragem pá cortá o peito do filho do Pajé?"
    indio2 "Num sei! Mas algum motivo deve ter para ele sangrar de manhã!"

    show indio1 cruzado at idealleft, tianoay with dissolve
    indio1 "Aí é que tu te enganas! Não é sangue dele não!"
    show indio2 normal at idealright, tianoay with dissolve
    indio2 "Como é que sabes?"

    indio1 "Já perguntei pra ele! Não tem nenhum machucado, não!"
    indio2 "Então deve ser o que eu pensei!"

    show indio1 normal at idealleft, tianoay with dissolve
    indio1 "O quê?"
    indio2 "F E I T I Ç O!!" with vpunch

    show indio1 cruzado at idealleft, tianoay with dissolve
    indio1 "Tá doido? Vamo logo é saí daqui!"
    indio1 "Se o Pajé vê a gente espiando o filho dele vai botar a gente de castigo!"

    indio2 "Cala a boca medroso! Tu sabes o que eu descobri?"
    indio1 "Não, e acho que num quero sabê!"

    indio2 "Tianoá põe sangue dela na bebida sagrada!"
    show indio1 normal at idealleft, tianoay with dissolve
    indio1 "O quê? Na bebida sagrada?"

    show indio2 cruzado at idealright, tianoay with dissolve
    indio2 "Por isso que ela não gosta que ninguém a veja, quando ela faz a bebida!"
    indio1 "Sangue dela? Arrghh!"

    indio2 "Ela corta o dedo e deixa o sangue cair na bebida!"
    indio1 "Arrghh!"

    indio1 "Olha lá! Tá acontecendo alguma coisa na rede!"

    show indio2 normalx at idealright, tianoay with dissolve
    indio2 "É agora que a gente vai saber o segredo de Tianoá!"

    indio1 "O que é aquilo??"

    show indio2 eita at idealright, tianoay with dissolve
    indio2 "Não acredito!!"

    stop music fadeout 1.0
    play music 'music/catalendas-mapinguari.ogg' fadein 1.0

    indio1 "Vamos sair correndo daqui!"
    indio2 "Ela tá vindo pra cá!"

    show indio1 normalx at idealleft, tianoay, saindoe
    show indio2 normal at idealright, tianoay, saindoe

    call ibelieveicanfly('xxxl_rl', fly_wave_rl, 4)

    stop music fadeout 1.0

    return
