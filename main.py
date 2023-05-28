import play

play.set_backdrop("light blue")

eat = True


@play.when_program_starts# функція для початку програми
def start():
    global player, speech
    text1 = play.new_text(words="р - робити зарядку, с - спати, г - гладити", x = 0, y = 270, font_size=40)
    text2 = play.new_text(words="к - кормити, п  - прибрати, пробіл - піти", x = 0, y = 240, font_size=40) 


    player = play.new_image(image="surikato4.jpg", x=0, y=0, size=100)
    speech = play.new_text(words = "Привіт", x=0, y=-250)



@play.repeat_forever# повторювати завжди(ігровий цикл)
async def do():
    global eat
    if play.key_is_pressed("р") or play.key_is_pressed("Р"):
        player.size = 100
        player.image = "surikato6.jpg"
        speech.words = "я майстер йоги"
        await play.timer(2.0)

        player.image = ("surikat 3.jpg")
        speech.words = ("після зарядки я хочу поспати")
        await play.timer(2.0)

    if play.key_is_pressed("г") or play.key_is_pressed("Г"):
        player.size = 200
        player.image = "surikato1.jpg"
        speech.words = "кайф"
        await play.timer(2.0)

        player.image = ("200px-Suricata")
        speech.words = ("покорми мене")
        await play.timer(2.0)

    if play.key_is_pressed('с') or play.key_is_pressed('С'):
        player.size = 20
        player.image = "1575814835195130290.jpg"
        speech.words = "спить"
        await play.timer(2.0)
        player.size = 300
        player.image = ("images.jpg")
        speech.words = ("я вже поспав погладь мене")


    if play.key_is_pressed("к") and eat == True:
        player.size = 100
        player.image = "220px-Meerkat_(Suricata_suricatta).jpg"
        speech.words = "я наївся"
        await play.timer(3.0)

        player.size = 100
        player.image = "surikato5.jpg"
        speech.words = "прибери за мною"
        await play.timer(2.0)
        eat = False

    if play.key_is_pressed("к") and eat == False:
        player.size = 100
        player.image = "surikato5.jpg"
        speech.words = "я вже не можу їсти"
        await play.timer(3.0)


    if play.key_is_pressed("п") or play.key_is_pressed("П"):
        player.size = 100
        player.image = "surikat 2.jpg"
        speech.words = "так набагато краще"
        await play.timer(2.0)
        eat = True

    if play.key_is_pressed('space'):
        player.size = 100
        player.image = "kryket.jpg"
        speech.words = "ти вже йдеш? тоді бувай"
        await play.timer(2.0)



play.start_program()# запуск програми 