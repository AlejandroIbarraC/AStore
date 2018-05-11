#App Store v1.0
#I Tarea Programada. Taller de Programacion. Jeff Schmidt Peralta
#Estudiante: Alejandro Ibarra Campos.
#Abril 2018.

from tkinter import * #importar tkinter para GUI
from tkinter import messagebox #importar messagebox para alertas
import os

#ventana principal. idioma ingles, region USA
root = Tk()
root.title('App Store')
root.minsize(1000, 600)
root.resizable(width = NO, height = NO)

#funcion para cargar imagenes
#E: archivo de imagen
#S: imagen en interfaz
#R: imagen en formato .gif
def loadPicture(name):
    route = os.path.join('images', name)
    photo = PhotoImage(file=route)
    return photo

#carga de iconos e imagenes
back_icon = loadPicture('exiticon.gif')
login_icon = loadPicture('loginicon.gif')
register_icon = loadPicture('registericon.gif')
app1_ad = loadPicture('app1ad.gif')
app1_ad_esp = loadPicture('app1adesp.gif')
games_icon = loadPicture('gamesicon.gif')
apps_icon = loadPicture('appsicon.gif')
search_icon = loadPicture('searchicon.gif')
cr_flag = loadPicture('crflag.gif')
us_flag = loadPicture('usflag.gif')
price0 = loadPicture('000.gif')
price099 = loadPicture('099.gif')
price199 = loadPicture('199.gif')
price420 = loadPicture('420.gif')
price299 = loadPicture('299.gif')
price499 = loadPicture('499.gif')
price699 = loadPicture('699.gif')

#carga de iconos y screenshots de apps
app1_icon = loadPicture('app1icon.gif')
app1_largeIcon = loadPicture('app1largeicon.gif')
app1_scr1 = loadPicture('app1scr1.gif')
app1_scr2 = loadPicture('app1scr2.gif')

app2_icon = loadPicture('app2icon.gif')
app2_largeIcon = loadPicture('app2largeicon.gif')
app2_scr1 = loadPicture('app2scr1.gif')
app2_scr2 = loadPicture('app2scr2.gif')

app3_icon = loadPicture('app3icon.gif')
app3_largeIcon = loadPicture('app3largeicon.gif')
app3_scr1 = loadPicture('app3scr1.gif')
app3_scr2 = loadPicture('app3scr2.gif')

app4_icon = loadPicture('app4icon.gif')
app4_largeIcon = loadPicture('app4largeicon.gif')
app4_scr1 = loadPicture('app4scr1.gif')
app4_scr2 = loadPicture('app4scr2.gif')

app5_icon = loadPicture('app5icon.gif')
app5_largeIcon = loadPicture('app5largeicon.gif')
app5_scr1 = loadPicture('app5scr1.gif')
app5_scr2 = loadPicture('app5scr2.gif')

app6_icon = loadPicture('app6icon.gif')
app6_largeIcon = loadPicture('app6largeicon.gif')
app6_scr1 = loadPicture('app6scr1.gif')
app6_scr2 = loadPicture('app6scr2.gif')

app7_icon = loadPicture('app7icon.gif')
app7_largeIcon = loadPicture('app7largeicon.gif')
app7_scr1 = loadPicture('app7scr1.gif')
app7_scr2 = loadPicture('app7scr2.gif')

app8_icon = loadPicture('app8icon.gif')
app8_largeIcon = loadPicture('app8largeicon.gif')
app8_scr1 = loadPicture('app8scr1.gif')
app8_scr2 = loadPicture('app8scr2.gif')

game1_icon = loadPicture('game1icon.gif')
game1_largeIcon = loadPicture('game1largeicon.gif')
game1_scr1 = loadPicture('game1scr1.gif')
game1_scr2 = loadPicture('game1scr2.gif')

game2_icon = loadPicture('game2icon.gif')
game2_largeIcon = loadPicture('game2largeicon.gif')
game2_scr1 = loadPicture('game2scr1.gif')
game2_scr2 = loadPicture('game2scr2.gif')

game3_icon = loadPicture('game3icon.gif')
game3_largeIcon = loadPicture('game3largeicon.gif')
game3_scr1 = loadPicture('game3scr1.gif')
game3_scr2 = loadPicture('game3scr2.gif')

game4_icon = loadPicture('game4icon.gif')
game4_largeIcon = loadPicture('game4largeicon.gif')
game4_scr1 = loadPicture('game4scr1.gif')
game4_scr2 = loadPicture('game4scr2.gif')

game5_icon = loadPicture('game5icon.gif')
game5_largeIcon = loadPicture('game5largeicon.gif')
game5_scr1 = loadPicture('game5scr1.gif')
game5_scr2 = loadPicture('game5scr2.gif')

game6_icon = loadPicture('game6icon.gif')
game6_largeIcon = loadPicture('game6largeicon.gif')
game6_scr1 = loadPicture('game6scr1.gif')
game6_scr2 = loadPicture('game6scr2.gif')

game7_icon = loadPicture('game7icon.gif')
game7_largeIcon = loadPicture('game7largeicon.gif')
game7_scr1 = loadPicture('game7scr1.gif')
game7_scr2 = loadPicture('game7scr2.gif')

game8_icon = loadPicture('game8icon.gif')
game8_largeIcon = loadPicture('game8largeicon.gif')
game8_scr1 = loadPicture('game8scr1.gif')
game8_scr2 = loadPicture('game8scr2.gif')

################################################################################

#ventana de menu principal en español sin acceso de usuario
def root_esp_not_logged():
    root.withdraw()
    root_esp_not_logged = Toplevel()
    root_esp_not_logged.title('App Store')
    root_esp_not_logged.minsize(1000, 600)
    root_esp_not_logged.resizable(width = NO, height = NO)

    #funcion para cambiar de region
    def root_eng():
        root_esp_not_logged.destroy()
        root.deiconify()

    #labels de menu principal
    welcome_label = Label(root_esp_not_logged, text='Bienvenido a la AStore', font = 'Helvetica 28')
    welcome_label.place(x=340, y=0)

    change_lang_label = Label(root_esp_not_logged, text = 'Cambiar región', font = 'Helvetica 16')
    change_lang_label.place(x=780, y=5)

    change_lang_cr = Button(root_esp_not_logged, image = us_flag, command = root_eng)
    change_lang_cr.place(x=890, y=0)

    #abrir txt y accesar lineas de apps y juegos
    apps_esp = open('apps_esp.txt', 'r+')
    read_apps_esp = apps_esp.readlines()

    app1_line = read_apps_esp[1]
    app1_info = app1_line.split(',')
    app2_line = read_apps_esp[2]
    app2_info = app2_line.split(',')
    app3_line = read_apps_esp[3]
    app3_info = app3_line.split(',')
    app4_line = read_apps_esp[4]
    app4_info = app4_line.split(',')
    app5_line = read_apps_esp[5]
    app5_info = app5_line.split(',')
    app6_line = read_apps_esp[6]
    app6_info = app6_line.split(',')
    app7_line = read_apps_esp[7]
    app7_info = app7_line.split(',')
    app8_line = read_apps_esp[8]
    app8_info = app8_line.split(',')

    games_esp = open('games_esp.txt', 'r+')
    read_games_esp = games_esp.readlines()

    game1_line = read_games_esp[1]
    game1_info = game1_line.split(',')
    game2_line = read_games_esp[2]
    game2_info = game2_line.split(',')
    game3_line = read_games_esp[3]
    game3_info = game3_line.split(',')
    game4_line = read_games_esp[4]
    game4_info = game4_line.split(',')
    game5_line = read_games_esp[5]
    game5_info = game5_line.split(',')
    game6_line = read_games_esp[6]
    game6_info = game6_line.split(',')
    game7_line = read_games_esp[7]
    game7_info = game7_line.split(',')
    game8_line = read_games_esp[8]
    game8_info = game8_line.split(',')

    ################################################################################
    
    #sistema de busqueda con nombre de app o palabras alusivas
    #E: palabra a buscar
    #S: redireccion
    #R: nombre de app o palabra alusiva

    def searchWindow():
        apps = open('apps.txt', 'r+')
        read_apps = apps.readlines()
        
        app1_line = read_apps[1]
        app1_info = app1_line.split(',')
        app2_line = read_apps[2]
        app2_info = app2_line.split(',')
        app3_line = read_apps[3]
        app3_info = app3_line.split(',')
        app4_line = read_apps[4]
        app4_info = app4_line.split(',')
        app5_line = read_apps[5]
        app5_info = app5_line.split(',')
        app6_line = read_apps[6]
        app6_info = app6_line.split(',')
        app7_line = read_apps[7]
        app7_info = app7_line.split(',')
        app8_line = read_apps[8]
        app8_info = app8_line.split(',')
        apps.close()

        games = open('games.txt', 'r+')
        read_games = games.readlines()

        game1_line = read_games[1]
        game1_info = game1_line.split(',')
        game2_line = read_games[2]
        game2_info = game2_line.split(',')
        game3_line = read_games[3]
        game3_info = game3_line.split(',')
        game4_line = read_games[4]
        game4_info = game4_line.split(',')
        game5_line = read_games[5]
        game5_info = game5_line.split(',')
        game6_line = read_games[6]
        game6_info = game6_line.split(',')
        game7_line = read_games[7]
        game7_info = game7_line.split(',')
        game8_line = read_games[8]
        game8_info = game8_line.split(',')
        games.close()
        apps = open('apps.txt', 'r+')
        read_apps = apps.readlines()
        searchText=search_entry.get()

        if searchText.strip() == 'juegos':
            games_menu()
        if searchText.strip() == 'juego':
            games_menu()
        elif searchText.strip() == 'aplicaciones':
            apps_menu()
        elif searchText.strip() == 'aplicacion':
            apps_menu()
        elif searchText.strip() == 'apps':
            apps_menu()
        elif searchText.strip() == 'aps':
            apps_menu()
        elif searchText.strip() == 'games':
            games_menu()
        elif searchText.strip() == 'jugar':
            games_menu()
        elif searchText.strip() == 'play':
            games_menu()
        elif searchText.strip() == 'jeff schmidt python':
            app1_window()
        elif searchText.strip() == 'jeff schmidts python':
            app1_window()
        elif searchText.strip() == 'python':
            app1_window()
        elif searchText.strip() == 'Python':
            app1_window()
        elif searchText.strip() == 'Jeff':
            app1_window()
        elif searchText.strip() == 'jeff':
            app1_window()
        elif searchText.strip() == 'jeff schmidt':
            app1_window()
        elif searchText.strip() == 'schmidt':
            app1_window()
        elif searchText.strip() == 'Schmidt':
            app1_window()
        elif searchText.strip() == 'code':
            app1_window()
        elif searchText.strip() == 'programming':
            app1_window()
        elif searchText.strip() == 'programar':
            app1_window()
        elif searchText.strip() == 'weed smoke pro':
            app2_window()
        elif searchText.strip() == 'weed':
            app2_window()
        elif searchText.strip() == 'smoke':
            app2_window()
        elif searchText.strip() == 'weed smoke':
            app2_window()
        elif searchText.strip() == 'marijuana':
            app2_window()
        elif searchText.strip() == '420':
            app2_window()
        elif searchText.strip() == 'bob marley':
            app2_window()
        elif searchText.strip() == 'math with ed sheeran':
            app3_window()
        elif searchText.strip() == 'ed sheeran':
            app3_window()
        elif searchText.strip() == 'ed':
            app3_window()
        elif searchText.strip() == 'sheeran':
            app3_window()
        elif searchText.strip() == 'math':
            app3_window()
        elif searchText.strip() == 'matematica':
            app3_window()
        elif searchText.strip() == 'mate':
            app3_window()
        elif searchText.strip() == 'you look perfect tonight':
            app3_window()
        elif searchText.strip() == 'taylors swift':
            app4_window()
        elif searchText.strip() == 'taylor swift':
            app4_window()
        elif searchText.strip() == 'swift':
            app4_window()
        elif searchText.strip() == 'taylor':
            app4_window()
        elif searchText.strip() == 'swift code':
            app4_window()
        elif searchText.strip() == 'swift language':
            app4_window()
        elif searchText.strip() == 'swift lenguaje':
            app4_window()
        elif searchText.strip() == 'the pirate bay':
            app5_window()
        elif searchText.strip() == 'free movies':
            app5_window()
        elif searchText.strip() == 'peliculas gratis':
            app5_window()
        elif searchText.strip() == 'pirate':
            app5_window()
        elif searchText.strip() == 'pirate bay':
            app5_window()
        elif searchText.strip() == 'piratear':
            app5_window()
        elif searchText.strip() == 'free tv':
            app5_window()
        elif searchText.strip() == 'torrent':
            app5_window()
        elif searchText.strip() == 'apple music':
            app6_window()
        elif searchText.strip() == 'apple':
            app6_window()
        elif searchText.strip() == 'music':
            app6_window()
        elif searchText.strip() == 'free music':
            app6_window()
        elif searchText.strip() == 'musica gratis':
            app6_window()
        elif searchText.strip() == 'netflix':
            app7_window()
        elif searchText.strip() == 'series':
            app7_window()
        elif searchText.strip() == 'tv shows':
            app7_window()
        elif searchText.strip() == 'movies':
            app7_window()
        elif searchText.strip() == 'peliculas':
            app7_window()
        elif searchText.strip() == 'netflix':
            app7_window()
        elif searchText.strip() == 'im feeling lucky':
            app8_window()
        elif searchText.strip() == 'kiss me pls':
            app8_window()
        elif searchText.strip() == 'kiss me':
            app8_window()
        elif searchText.strip() == 'notlim':
            game1_window()
        elif searchText.strip() == 'Notlim':
            game1_window()
        elif searchText.strip() == 'mining':
            game1_window()
        elif searchText.strip() == 'intro & taller':
            game2_window()
        elif searchText.strip() == 'intro y taller':
            game2_window()
        elif searchText.strip() == 'Intro y Taller':
            game2_window()
        elif searchText.strip() == 'Intro & taller':
            game2_window()
        elif searchText.strip() == 'intro':
            game2_window()
        elif searchText.strip() == 'taller':
            game2_window()
        elif searchText.strip() == 'samus aran':
            game2_window()
        elif searchText.strip() == 'conejos':
            game2_window()
        elif searchText.strip() == 'arnold schwarzenegger':
            game2_window()
        elif searchText.strip() == 'jessie':
            game3_window()
        elif searchText.strip() == 'ingeniera':
            game3_window()
        elif searchText.strip() == 'engineer':
            game3_window()
        elif searchText.strip() == 'game of shots':
            game4_window()
        elif searchText.strip() == 'shots':
            game4_window()
        elif searchText.strip() == 'drinking game':
            game4_window()
        elif searchText.strip() == 'alcohol':
            game4_window()
        elif searchText.strip() == 'tragos':
            game4_window()
        elif searchText.strip() == 'monument valley':
            game5_window()
        elif searchText.strip() == 'arquitectura':
            game5_window()
        elif searchText.strip() == 'architecture':
            game5_window()
        elif searchText.strip() == 'monument':
            game5_window()
        elif searchText.strip() == 'valley':
            game5_window()
        elif searchText.strip() == 'life is strange':
            game6_window()
        elif searchText.strip() == 'life':
            game6_window()
        elif searchText.strip() == 'strange':
            game6_window()
        elif searchText.strip() == 'max caulfield':
            game6_window()
        elif searchText.strip() == 'blackwell':
            game6_window()
        elif searchText.strip() == 'unbreakable':
            game7_window()
        elif searchText.strip() == 'jeff schmidt game':
            game7_window()
        elif searchText.strip() == 'jeff schmidt juego':
            game7_window()
        elif searchText.strip() == 'stocks':
            game8_window()
        elif searchText.strip() == 'bolsa':
            game8_window()
        elif searchText.strip() == 'dinero':
            game8_window()
        elif searchText.strip() == 'money':
            game8_window()
        elif searchText.strip() == 'strategy':
            game8_window()
        elif searchText.strip() == 'estrategia':
            game8_window()
        elif searchText.strip() == app1_info[3].strip():
            app1_window()
        elif searchText.strip() == app2_info[3].strip():
            app2_window()   
        elif searchText.strip() == app3_info[3].strip():
            app3_window()
        elif searchText.strip() == app4_info[3].strip():
            app4_window()
        elif searchText.strip() == app5_info[3].strip():
            app5_window()
        elif searchText.strip() == app6_info[3].strip():
            app6_window()
        elif searchText.strip() == app7_info[3].strip():
            app7_window()
        elif searchText.strip() == app8_info[3].strip():
            app8_window()
        elif searchText.strip() == game1_info[3].strip():
            game1_window()
        elif searchText.strip() == game2_info[3].strip():
            game2_window()
        elif searchText.strip() == game3_info[3].strip():
            game3_window()
        elif searchText.strip() == game4_info[3].strip():
            game4_window()
        elif searchText.strip() == game5_info[3].strip():
            game5_window()
        elif searchText.strip() == game6_info[3].strip():
            game6_window()
        elif searchText.strip() == game7_info[3].strip():
            game7_window()
        elif searchText.strip() == game8_info[3].strip():
            game8_window()
        else:
            messagebox.showwarning("Resultado de busqueda:",searchText+' not encontrado')

    ###############################################################################

    #ventana de registro
    def registerWindow():
        registerwindow = Toplevel()
        registerwindow.title('App Store')
        registerwindow.minsize(1000,600)
        registerwindow.resizable(width = NO, height = NO)

        registercanvas = Canvas(registerwindow, width = 1000, height = 600, bg = 'white')
        registercanvas.place(x=0,y=0)

        #labels:
        title_label = Label(registercanvas, text = 'Registro - REGIÓN COSTA RICA', font = 'Helvetica 28')
        title_label.place(x=320, y=20)

        name_label = Label(registercanvas, text = 'Nombre:', font = 'Helvetica 24')
        name_label.place(x=100, y=175)

        lastname_label = Label(registercanvas, text = 'Apellido:', font = 'Helvetica 24')
        lastname_label.place(x=100, y=250)

        email_label = Label(registercanvas, text = 'Usuario:', font = 'Helvetica 24')
        email_label.place(x=100, y=325)

        password_label =  Label(registercanvas, text = 'Contraseña:', font = 'Helvetica 24')
        password_label.place(x=100, y= 400)
        
        #entries:
        nameentry = Entry(registercanvas, width = 20)
        nameentry.place(x=300, y=175)

        lastnameentry = Entry(registercanvas, width = 20)
        lastnameentry.place(x=300, y= 250)

        usernameentry = Entry(registercanvas, width = 20)
        usernameentry.place(x=300, y=325)

        passwordentry = Entry(registercanvas, show = '*', width = 20)
        passwordentry.place(x=300, y=400)

        #funcion para registrar usuarios usando archivos txt
        #E: datos de entries
        #S: escribir nuevo usuario en archivo de texto
        def filewrite():
            a = open ('usercount.txt','r+')
            lastIndex = a.readlines()
            userid = lastIndex[len(lastIndex) - 1]
            name = nameentry.get()
            lastname = lastnameentry.get()
            username = usernameentry.get()
            password = passwordentry.get()
            b = open('users.txt','a')
            info = username + ',' + name + ',' + password + ',' + lastname + ',' + userid + ',' + 'CR' + ',' + '0'
            b.write('\n' + str(info))
            a.write('\n' + str(int(userid) + 1))

        processregisterbutton = Button(registercanvas, text = 'Registrar', command = filewrite)
        processregisterbutton.place(x=250, y=500)
        
        def backtoroot():
            registerwindow.destroy()

        backbutton = Button(registerwindow, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ##############################################################################

    #ventana de login
    def loginWindow():
        loginwindow = Toplevel()
        loginwindow.title('App Store')
        loginwindow.minsize(1000,600)
        loginwindow.resizable(width = NO, height = NO)

        logincanvas = Canvas(loginwindow, width = 1000, height = 600, bg = 'white')
        logincanvas.place(x=0,y=0)

        title_label = Label(logincanvas, text = 'Acceso - REGIÓN COSTA RICA', font = 'Helvetica 28')
        title_label.place(x=320, y=20)

        username_email_label = Label(logincanvas, text = 'Usuario/Email', font = 'Helvetica 24')
        username_email_label.place(x=100,y=175)

        password_label = Label(logincanvas, text = 'Contraseña', font = 'Helvetica 24')
        password_label.place(x=100, y=250)

        emailloginentry = Entry(logincanvas, width = 20)
        emailloginentry.place(x=350, y=175)

        passwordloginentry = Entry(logincanvas, show = '*', width = 20)
        passwordloginentry.place(x=350, y=250)

        #funcion para login con txt
        #E: usuario y password de entry
        #S: redireccion si son validos y mensaje de error si no
        #R: usuario y password validos
        def login():
            user0 = emailloginentry.get()
            pass0 = passwordloginentry.get()
            with open("users.txt", "r") as file:
                reader = file.readlines()
            for line in reader:
               if not line.strip():
                   continue
               else:
                   username=line.split(",")[0]
                   pswd=line.split(",")[2]
                   if username == user0  and pswd == pass0:
                       root_esp()
                       break
            else:
               messagebox.showwarning("Information",'Usuario o contraseña incorrecto')
            
        processloginbutton = Button(logincanvas, text = 'Acceder', command = login)
        processloginbutton.place(x=100, y=400)

        def backtoroot():
            loginwindow.destroy()

        backbutton = Button(loginwindow, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    #ventana de menu de apps
    def apps_menu():
        apps_menu = Toplevel()
        apps_menu.title('App Store')
        apps_menu.minsize(1000, 600)
        apps_menu.resizable(width = NO, height = NO)

        appsmenu_canvas = Canvas(apps_menu, width = 1000, height = 600, bg = 'white')
        appsmenu_canvas.place(x=0, y=0)

        #app 1
        app1_icon = Button(appsmenu_canvas, image = app1_largeIcon, command = app1_window)
        app1_icon.place(x=60, y=70)

        app1_label = Label(appsmenu_canvas, text = app1_info[3], font = 'Helvetica 24')
        app1_label.place(x=30, y=270)

        app1_price = Label(appsmenu_canvas, text = app1_info[9], font = 'Helvetica 24')
        app1_price.place(x=120, y=300)

        #app 2
        app2_icon = Button(appsmenu_canvas, image = app2_largeIcon, command = app2_window)
        app2_icon.place(x=290, y=70)

        app2_label = Label(appsmenu_canvas, text = app2_info[3], font = 'Helvetica 24')
        app2_label.place(x=280, y=270)

        app2_price = Label(appsmenu_canvas, text = app2_info[9], font = 'Helvetica 24')
        app2_price.place(x=360, y=300)

        #app 3
        app3_icon = Button(appsmenu_canvas, image = app3_largeIcon, command = app3_window)
        app3_icon.place(x=520, y=70)

        app3_label = Label(appsmenu_canvas, text = app3_info[3], font = 'Helvetica 24')
        app3_label.place(x=500, y=270)

        app3_price = Label(appsmenu_canvas, text = app3_info[9], font = 'Helvetica 24')
        app3_price.place(x=580, y=300)

        #app 4
        app4_icon = Button(appsmenu_canvas, image = app4_largeIcon, command = app4_window)
        app4_icon.place(x=750, y=70)

        app4_label = Label(appsmenu_canvas, text = app4_info[3], font = 'Helvetica 24')
        app4_label.place(x=765, y=270)

        app4_price = Label(appsmenu_canvas, text = app4_info[9], font = 'Helvetica 24')
        app4_price.place(x=810, y=300)

        #app 5
        app5_icon = Button(appsmenu_canvas, image = app5_largeIcon, command = app5_window)
        app5_icon.place(x=60, y=350)

        app5_label = Label(appsmenu_canvas, text = app5_info[3], font = 'Helvetica 24')
        app5_label.place(x=65, y=540)

        app5_price = Label(appsmenu_canvas, text = app5_info[9], font = 'Helvetica 24')
        app5_price.place(x=115, y=570)

        #app 6
        app6_icon = Button(appsmenu_canvas, image = app6_largeIcon, command = app6_window)
        app6_icon.place(x=290, y=350)

        app6_label = Label(appsmenu_canvas, text = app6_info[3], font = 'Helvetica 24')
        app6_label.place(x=310, y=540)

        app6_price = Label(appsmenu_canvas, text = app6_info[9], font = 'Helvetica 24')
        app6_price.place(x=345, y=570)

        #app 7
        app7_icon = Button(appsmenu_canvas, image = app7_largeIcon, command = app7_window)
        app7_icon.place(x=520, y=350)

        app7_label = Label(appsmenu_canvas, text = app7_info[3], font = 'Helvetica 24')
        app7_label.place(x=570, y=540)

        app7_price = Label(appsmenu_canvas, text = app7_info[9], font = 'Helvetica 24')
        app7_price.place(x=575, y=570)

        #app 8
        app8_icon = Button(appsmenu_canvas, image = app8_largeIcon, command = app8_window)
        app8_icon.place(x=750, y=350)
        
        app8_label = Label(appsmenu_canvas, text = app8_info[3], font = 'Helvetica 24')
        app8_label.place(x=780, y=540)

        app8_price = Label(appsmenu_canvas, text = app8_info[9], font = 'Helvetica 24')
        app8_price.place(x=810, y=570)

        def backtoroot():
            apps_menu.destroy()

        backbutton = Button(apps_menu, image = back_icon, command = backtoroot)
        backbutton.place(x=20, y=20)

    ###############################################################################

    #ventana de menu de juegos
    def games_menu():
        games_menu = Toplevel()
        games_menu.title('App Store')
        games_menu.minsize(1000, 600)
        games_menu.resizable(width = NO, height = NO)

        gamesmenu_canvas = Canvas(games_menu, width = 1000, height = 600, bg = 'white')
        gamesmenu_canvas.place(x=0, y=0)

        #juego1
        game1_icon = Button(gamesmenu_canvas, image = game1_largeIcon, command = game1_window)
        game1_icon.place(x=60, y=70)

        game1_label = Label(gamesmenu_canvas, text = game1_info[3], font = 'Helvetica 24')
        game1_label.place(x=100, y=270)

        game1_price = Label(gamesmenu_canvas, text = game1_info[9], font = 'Helvetica 24')
        game1_price.place(x=120, y=300)

        #juego2
        game2_icon = Button(gamesmenu_canvas, image = game2_largeIcon, command = game2_window)
        game2_icon.place(x=290, y=70)

        game2_label = Label(gamesmenu_canvas, text = game2_info[3], font = 'Helvetica 24')
        game2_label.place(x=315, y=270)

        game2_price = Label(gamesmenu_canvas, text = game2_info[9], font = 'Helvetica 24')
        game2_price.place(x=355, y=300)

        #juego3
        game3_icon = Button(gamesmenu_canvas, image = game3_largeIcon, command = game3_window)
        game3_icon.place(x=520, y=70)

        game3_label = Label(gamesmenu_canvas, text = game3_info[3], font = 'Helvetica 24')
        game3_label.place(x=575, y=270)

        game3_price = Label(gamesmenu_canvas, text = game3_info[9], font = 'Helvetica 24')
        game3_price.place(x=580, y=300)

        #juego4
        game4_icon = Button(gamesmenu_canvas, image = game4_largeIcon, command = game4_window)
        game4_icon.place(x=750, y=70)

        game4_label = Label(gamesmenu_canvas, text = game4_info[3], font = 'Helvetica 24')
        game4_label.place(x=760, y=270)

        game4_price = Label(gamesmenu_canvas, text = game4_info[9], font = 'Helvetica 24')
        game4_price.place(x=805, y=300)

        #juego5
        game5_icon = Button(gamesmenu_canvas, image = game5_largeIcon, command = game5_window)
        game5_icon.place(x=60, y=350)

        game5_label = Label(gamesmenu_canvas, text = game5_info[3], font = 'Helvetica 24')
        game5_label.place(x=55, y=540)

        game5_price = Label(gamesmenu_canvas, text = game5_info[9], font = 'Helvetica 24')
        game5_price.place(x=110, y=570)

        #juego6
        game6_icon = Button(gamesmenu_canvas, image = game6_largeIcon, command = game6_window)
        game6_icon.place(x=290, y=350)

        game6_label = Label(gamesmenu_canvas, text = game6_info[3], font = 'Helvetica 24')
        game6_label.place(x=300, y=540)

        game6_price = Label(gamesmenu_canvas, text = game6_info[9], font = 'Helvetica 24')
        game6_price.place(x=340, y=570)    

        #juego7
        game7_icon = Button(gamesmenu_canvas, image = game7_largeIcon, command = game7_window)
        game7_icon.place(x=520, y=350)

        game7_label = Label(gamesmenu_canvas, text = game7_info[3], font = 'Helvetica 24')
        game7_label.place(x=540, y=540)

        game7_price = Label(gamesmenu_canvas, text = game7_info[9], font = 'Helvetica 24')
        game7_price.place(x=580, y=570)

        #juego8
        game8_icon = Button(gamesmenu_canvas, image = game8_largeIcon, command = game8_window)
        game8_icon.place(x=750, y=350)

        game8_label = Label(gamesmenu_canvas, text = game8_info[3], font = 'Helvetica 24')
        game8_label.place(x=800, y=540)

        game8_price = Label(gamesmenu_canvas, text = game8_info[9], font = 'Helvetica 24')
        game8_price.place(x=805, y=570)

        def backtoroot():
            games_menu.destroy()

        backbutton = Button(games_menu, image = back_icon, command = backtoroot)
        backbutton.place(x=20, y=20)

    ###############################################################################

    #ventana app 1
    def app1_window():
        root.withdraw()
        app1_window = Toplevel()
        app1_window.title('App Store')
        app1_window.minsize(1000, 600)
        app1_window.resizable(width = NO, height = NO)

        #leer lineas app 1
        app1_line = read_apps_esp[1]
        app1_info = app1_line.split(',')

        app1_canvas = Canvas(app1_window, width = 1000, height = 600, bg = 'white')
        app1_canvas.place(x=0, y=0)

        #labels de info
        app1_largeIcon_pic = Label(app1_canvas, image = app1_largeIcon)
        app1_largeIcon_pic.place(x=100, y=70)

        app1_label = Label(app1_canvas, text = app1_info[3], font = 'Helvetica 30')
        app1_label.place(x=70, y=250)

        app1_scr1_pic = Label(app1_canvas, image = app1_scr1)
        app1_scr1_pic.place(x=450, y=30)

        app1_scr2_pic = Label(app1_canvas, image = app1_scr2)
        app1_scr2_pic.place(x=730, y= 30)

        app1_desc = Label(app1_canvas, font = 'Helvetica 24', text = app1_info[4], justify = LEFT)
        app1_desc.place(x=25, y=380)

        app1_desc2 = Label(app1_canvas, font = 'Helvetica 24', text = app1_info[5], justify = LEFT)
        app1_desc2.place(x=25, y=410)

        app1_desc3 = Label(app1_canvas, font = 'Helvetica 24', text = app1_info[6], justify = LEFT)
        app1_desc3.place(x=25, y=440)

        app1_desc4 = Label(app1_canvas, font = 'Helvetica 24', text = app1_info[7], justify = LEFT)
        app1_desc4.place(x=25, y=470)

        app1_desc5 = Label(app1_canvas, font = 'Helvetica 24', text = app1_info[8], justify = LEFT)
        app1_desc5.place(x=25, y=500)

        app1_size = Label(app1_canvas, font = 'Helvetica 24', text = 'Tamaño:'+app1_info[10])
        app1_size.place(x=25, y=540)

        app1_price = Label(app1_canvas, image = price099)
        app1_price.place(x=115, y=300)

        def backtoroot():
            app1_window.destroy()

        backbutton = Button(app1_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    #ventana de app 2
    def app2_window():
        root.withdraw()
        app2_window = Toplevel()
        app2_window.title('App Store')
        app2_window.minsize(1000, 600)
        app2_window.resizable(width = NO, height = NO)

        #leer lineas app 2
        app2_line = read_apps_esp[2]
        app2_info = app2_line.split(',')

        app2_canvas = Canvas(app2_window, width = 1000, height = 600, bg = 'white')
        app2_canvas.place(x=0, y=0)

        #labels app 2
        app2_largeIcon_pic = Label(app2_canvas, image = app2_largeIcon)
        app2_largeIcon_pic.place(x=100, y=60)

        app2_label = Label(app2_canvas, text = app2_info[3], font = 'Helvetica 30')
        app2_label.place(x=70, y=250)

        app2_scr1_pic = Label(app2_canvas, image = app2_scr1)
        app2_scr1_pic.place(x=450, y=30)

        app2_scr2_pic = Label(app2_canvas, image = app2_scr2)
        app2_scr2_pic.place(x=730, y= 30)

        app2_desc = Label(app2_canvas, font = 'Helvetica 24', text = app2_info[4], justify = LEFT)
        app2_desc.place(x=25, y=380)

        app2_desc2 = Label(app2_canvas, font = 'Helvetica 24', text = app2_info[5], justify = LEFT)
        app2_desc2.place(x=25, y=410)

        app2_desc3 = Label(app2_canvas, font = 'Helvetica 24', text = app2_info[6], justify = LEFT)
        app2_desc3.place(x=25, y=440)

        app2_desc4 = Label(app2_canvas, font = 'Helvetica 24', text = app2_info[7], justify = LEFT)
        app2_desc4.place(x=25, y=470)

        app2_desc5 = Label(app2_canvas, font = 'Helvetica 24', text = app2_info[8], justify = LEFT)
        app2_desc5.place(x=25, y=500)

        app2_size = Label(app2_canvas, font = 'Helvetica 24', text = 'Tamaño: '+app2_info[10])
        app2_size.place(x=25, y=540)
            
        app2_price = Label(app2_canvas, image = price420)
        app2_price.place(x=115, y=300)

        def backtoroot():
            app2_window.destroy()

        backbutton = Button(app2_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    #ventana app 3
    def app3_window():
        root.withdraw()
        app3_window = Toplevel()
        app3_window.title('App Store')
        app3_window.minsize(1000, 600)
        app3_window.resizable(width = NO, height = NO)

        #leer lineas app 3
        app3_line = read_apps_esp[3]
        app3_info = app3_line.split(',')

        app3_canvas = Canvas(app3_window, width = 1000, height = 600, bg = 'white')
        app3_canvas.place(x=0, y=0)

        #labels info app 3
        app3_largeIcon_pic = Label(app3_canvas, image = app3_largeIcon)
        app3_largeIcon_pic.place(x=100, y=70)

        app3_label = Label(app3_canvas, text = app3_info[3], font = 'Helvetica 30')
        app3_label.place(x=50, y=250)

        app3_scr1_pic = Label(app3_canvas, image = app3_scr1)
        app3_scr1_pic.place(x=450, y=30)

        app3_scr2_pic = Label(app3_canvas, image = app3_scr2)
        app3_scr2_pic.place(x=700, y= 30)

        app3_desc = Label(app3_canvas, font = 'Helvetica 24', text = app3_info[4], justify = LEFT)
        app3_desc.place(x=25, y=380)

        app3_desc2 = Label(app3_canvas, font = 'Helvetica 24', text = app3_info[5], justify = LEFT)
        app3_desc2.place(x=25, y=410)

        app3_desc3 = Label(app3_canvas, font = 'Helvetica 24', text = app3_info[6], justify = LEFT)
        app3_desc3.place(x=25, y=440)

        app3_desc4 = Label(app3_canvas, font = 'Helvetica 24', text = app3_info[7], justify = LEFT)
        app3_desc4.place(x=25, y=470)

        app3_desc5 = Label(app3_canvas, font = 'Helvetica 24', text = app3_info[8], justify = LEFT)
        app3_desc5.place(x=25, y=500)

        app3_size = Label(app3_canvas, font = 'Helvetica 24', text = 'Tamaño: '+app3_info[10])
        app3_size.place(x=25, y=540)

        app3_price = Label(app3_canvas, image = price199)
        app3_price.place(x=115, y=300)

        def backtoroot():
            app3_window.destroy()

        backbutton = Button(app3_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    #ventana app 4
    def app4_window():
        root.withdraw()
        app4_window = Toplevel()
        app4_window.title('App Store')
        app4_window.minsize(1000, 600)
        app4_window.resizable(width = NO, height = NO)

        app4_line = read_apps_esp[4]
        app4_info = app4_line.split(',')

        app4_canvas = Canvas(app4_window, width = 1000, height = 600, bg = 'white')
        app4_canvas.place(x=0, y=0)

        app4_largeIcon_pic = Label(app4_canvas, image = app4_largeIcon)
        app4_largeIcon_pic.place(x=100, y=70)

        app4_label = Label(app4_canvas, text = app4_info[3], font = 'Helvetica 30')
        app4_label.place(x=95, y=250)

        app4_scr1_pic = Label(app4_canvas, image = app4_scr1)
        app4_scr1_pic.place(x=450, y=30)

        app4_scr2_pic = Label(app4_canvas, image = app4_scr2)
        app4_scr2_pic.place(x=700, y= 30)

        app4_desc = Label(app4_canvas, font = 'Helvetica 24', text = app4_info[4], justify = LEFT)
        app4_desc.place(x=25, y=380)

        app4_desc2 = Label(app4_canvas, font = 'Helvetica 24', text = app4_info[5], justify = LEFT)
        app4_desc2.place(x=25, y=410)
        
        app4_desc3 = Label(app4_canvas, font = 'Helvetica 24', text = app4_info[6], justify = LEFT)
        app4_desc3.place(x=25, y=440)

        app4_desc4 = Label(app4_canvas, font = 'Helvetica 24', text = app4_info[7], justify = LEFT)
        app4_desc4.place(x=25, y=470)

        app4_desc5 = Label(app4_canvas, font = 'Helvetica 24', text = app4_info[8], justify = LEFT)
        app4_desc5.place(x=25, y=500)

        app4_size = Label(app4_canvas, font = 'Helvetica 24', text = 'Tamaño: '+app4_info[10])
        app4_size.place(x=25, y=540)

        app4_price = Label(app4_canvas, image = price199)
        app4_price.place(x=115, y=300)
        
        def backtoroot():
            app4_window.destroy()

        backbutton = Button(app4_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    #ventana app 5
    def app5_window():
        root.withdraw()
        app5_window = Toplevel()
        app5_window.title('App Store')
        app5_window.minsize(1000, 600)
        app5_window.resizable(width = NO, height = NO)

        app5_line = read_apps_esp[5]
        app5_info = app5_line.split(',')

        app5_canvas = Canvas(app5_window, width = 1000, height = 600, bg = 'white')
        app5_canvas.place(x=0, y=0)

        app5_largeIcon_pic = Label(app5_canvas, image = app5_largeIcon)
        app5_largeIcon_pic.place(x=100, y=70)

        app5_label = Label(app5_canvas, text = app5_info[3], font = 'Helvetica 30')
        app5_label.place(x=85, y=250)

        app5_scr1_pic = Label(app5_canvas, image = app5_scr1)
        app5_scr1_pic.place(x=450, y=30)

        app5_scr2_pic = Label(app5_canvas, image = app5_scr2)
        app5_scr2_pic.place(x=700, y= 30)

        app5_desc = Label(app5_canvas, font = 'Helvetica 24', text = app5_info[4], justify = LEFT)
        app5_desc.place(x=25, y=380)

        app5_desc2 = Label(app5_canvas, font = 'Helvetica 24', text = app5_info[5], justify = LEFT)
        app5_desc2.place(x=25, y=410)

        app5_desc3 = Label(app5_canvas, font = 'Helvetica 24', text = app5_info[6], justify = LEFT)
        app5_desc3.place(x=25, y=440)

        app5_desc4 = Label(app5_canvas, font = 'Helvetica 24', text = app5_info[7], justify = LEFT)
        app5_desc4.place(x=25, y=470)

        app5_desc5 = Label(app5_canvas, font = 'Helvetica 24', text = app5_info[8], justify = LEFT)
        app5_desc5.place(x=25, y=500)

        app5_size = Label(app5_canvas, font = 'Helvetica 24', text = 'Tamaño: '+app5_info[10])
        app5_size.place(x=25, y=540)

        app5_price = Label(app5_canvas, image = price0)
        app5_price.place(x=115, y=300)

        def backtoroot():
            app5_window.destroy()

        backbutton = Button(app5_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    #ventana app 6
    def app6_window():
        root.withdraw()
        app6_window = Toplevel()
        app6_window.title('App Store')
        app6_window.minsize(1000, 600)
        app6_window.resizable(width = NO, height = NO)

        app6_line = read_apps_esp[6]
        app6_info = app6_line.split(',')

        app6_canvas = Canvas(app6_window, width = 1000, height = 600, bg = 'white')
        app6_canvas.place(x=0, y=0)

        app6_largeIcon_pic = Label(app6_canvas, image = app6_largeIcon)
        app6_largeIcon_pic.place(x=100, y=70)

        app6_label = Label(app6_canvas, text = app6_info[3], font = 'Helvetica 30')
        app6_label.place(x=100, y=260)

        app6_scr1_pic = Label(app6_canvas, image = app6_scr1)
        app6_scr1_pic.place(x=450, y=30)

        app6_scr2_pic = Label(app6_canvas, image = app6_scr2)
        app6_scr2_pic.place(x=700, y= 30)

        app6_desc = Label(app6_canvas, font = 'Helvetica 24', text = app6_info[4], justify = LEFT)
        app6_desc.place(x=25, y=380)

        app6_desc2 = Label(app6_canvas, font = 'Helvetica 24', text = app6_info[5], justify = LEFT)
        app6_desc2.place(x=25, y=410)

        app6_desc3 = Label(app6_canvas, font = 'Helvetica 24', text = app6_info[6], justify = LEFT)
        app6_desc3.place(x=25, y=440)

        app6_desc4 = Label(app6_canvas, font = 'Helvetica 24', text = app6_info[7], justify = LEFT)
        app6_desc4.place(x=25, y=470)

        app6_desc5 = Label(app6_canvas, font = 'Helvetica 24', text = app6_info[8], justify = LEFT)
        app6_desc5.place(x=25, y=500)

        app6_size = Label(app6_canvas, font = 'Helvetica 24', text = 'Tamaño: '+app6_info[10])
        app6_size.place(x=25, y=540)

        app6_price = Label(app6_canvas, image = price0)
        app6_price.place(x=115, y=300)

        def backtoroot():
            app6_window.destroy()

        backbutton = Button(app6_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    #ventana app 7
    def app7_window():
        root.withdraw()
        app7_window = Toplevel()
        app7_window.title('App Store')
        app7_window.minsize(1000, 600)
        app7_window.resizable(width = NO, height = NO)

        app7_line = read_apps_esp[7]
        app7_info = app7_line.split(',')

        app7_canvas = Canvas(app7_window, width = 1000, height = 600, bg = 'white')
        app7_canvas.place(x=0, y=0)

        app7_largeIcon_pic = Label(app7_canvas, image = app7_largeIcon)
        app7_largeIcon_pic.place(x=100, y=70)

        app7_label = Label(app7_canvas, text = app7_info[3], font = 'Helvetica 30')
        app7_label.place(x=140, y=250)

        app7_scr1_pic = Label(app7_canvas, image = app7_scr1)
        app7_scr1_pic.place(x=450, y=30)

        app7_scr2_pic = Label(app7_canvas, image = app7_scr2)
        app7_scr2_pic.place(x=700, y= 30)

        app7_desc = Label(app7_canvas, font = 'Helvetica 24', text = app7_info[4], justify = LEFT)
        app7_desc.place(x=25, y=380)

        app7_desc2 = Label(app7_canvas, font = 'Helvetica 24', text = app7_info[5], justify = LEFT)
        app7_desc2.place(x=25, y=410)

        app7_desc3 = Label(app7_canvas, font = 'Helvetica 24', text = app7_info[6], justify = LEFT)
        app7_desc3.place(x=25, y=440)

        app7_desc4 = Label(app7_canvas, font = 'Helvetica 24', text = app7_info[7], justify = LEFT)
        app7_desc4.place(x=25, y=470)

        app7_desc5 = Label(app7_canvas, font = 'Helvetica 24', text = app7_info[8], justify = LEFT)
        app7_desc5.place(x=25, y=500)

        app7_size = Label(app7_canvas, font = 'Helvetica 24', text = 'Tamaño: '+app7_info[10])
        app7_size.place(x=25, y=540)

        app7_price = Label(app7_canvas, image = price0)
        app7_price.place(x=115, y=300)

        def backtoroot():
            app7_window.destroy()

        backbutton = Button(app7_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    #ventana app 8
    def app8_window():
        root.withdraw()
        app8_window = Toplevel()
        app8_window.title('App Store')
        app8_window.minsize(1000, 600)
        app8_window.resizable(width = NO, height = NO)

        app8_line = read_apps_esp[8]
        app8_info = app8_line.split(',')

        app8_canvas = Canvas(app8_window, width = 1000, height = 600, bg = 'white')
        app8_canvas.place(x=0, y=0)

        app8_largeIcon_pic = Label(app8_canvas, image = app8_largeIcon)
        app8_largeIcon_pic.place(x=100, y=70)

        app8_label = Label(app8_canvas, text = app8_info[3], font = 'Helvetica 30')
        app8_label.place(x=105, y=250)

        app8_scr1_pic = Label(app8_canvas, image = app8_scr1)
        app8_scr1_pic.place(x=450, y=30)

        app8_scr2_pic = Label(app8_canvas, image = app8_scr2)
        app8_scr2_pic.place(x=700, y= 30)
        
        app8_desc = Label(app8_canvas, font = 'Helvetica 24', text = app8_info[4], justify = LEFT)
        app8_desc.place(x=25, y=380)

        app8_desc2 = Label(app8_canvas, font = 'Helvetica 24', text = app8_info[5], justify = LEFT)
        app8_desc2.place(x=25, y=410)

        app8_desc3 = Label(app8_canvas, font = 'Helvetica 24', text = app8_info[6], justify = LEFT)
        app8_desc3.place(x=25, y=440)

        app8_desc4 = Label(app8_canvas, font = 'Helvetica 24', text = app8_info[7], justify = LEFT)
        app8_desc4.place(x=25, y=470)

        app8_desc5 = Label(app8_canvas, font = 'Helvetica 24', text = app8_info[8], justify = LEFT)
        app8_desc5.place(x=25, y=500)

        app8_size = Label(app8_canvas, font = 'Helvetica 24', text = 'Tamaño: '+app8_info[10])
        app8_size.place(x=25, y=540)

        app8_price = Label(app8_canvas, image = price0)
        app8_price.place(x=115, y=300)

        def backtoroot():
            app8_window.destroy()

        backbutton = Button(app8_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    #ventana juego 1
    def game1_window():
        root.withdraw()
        game1_window = Toplevel()
        game1_window.title('App Store')
        game1_window.minsize(1000, 600)
        game1_window.resizable(width = NO, height = NO)

        game1_line = read_games_esp[1]
        game1_info = game1_line.split(',')

        game1_canvas = Canvas(game1_window, width = 1000, height = 600, bg = 'white')
        game1_canvas.place(x=0, y=0)

        game1_largeIcon_pic = Label(game1_canvas, image = game1_largeIcon)
        game1_largeIcon_pic.place(x=100, y=70)

        game1_label = Label(game1_canvas, text = game1_info[3], font = 'Helvetica 30')
        game1_label.place(x=133, y=250)

        game1_scr1_pic = Label(game1_canvas, image = game1_scr1)
        game1_scr1_pic.place(x=450, y=30)

        game1_scr2_pic = Label(game1_canvas, image = game1_scr2)
        game1_scr2_pic.place(x=730, y= 30)
        
        game1_desc = Label(game1_canvas, font = 'Helvetica 24', text = game1_info[4], justify = LEFT)
        game1_desc.place(x=25, y=380)

        game1_desc2 = Label(game1_canvas, font = 'Helvetica 24', text = game1_info[5], justify = LEFT)
        game1_desc2.place(x=25, y=410)

        game1_desc3 = Label(game1_canvas, font = 'Helvetica 24', text = game1_info[6], justify = LEFT)
        game1_desc3.place(x=25, y=440)

        game1_desc4 = Label(game1_canvas, font = 'Helvetica 24', text = game1_info[7], justify = LEFT)
        game1_desc4.place(x=25, y=470)

        game1_desc5 = Label(game1_canvas, font = 'Helvetica 24', text = game1_info[8], justify = LEFT)
        game1_desc5.place(x=25, y=500)

        game1_size = Label(game1_canvas, font = 'Helvetica 24', text = 'Tamaño: '+game1_info[10])
        game1_size.place(x=25, y=540)

        game1_price = Label(game1_canvas, image = price0)
        game1_price.place(x=115, y=300)

        def backtoroot():
            game1_window.destroy()

        backbutton = Button(game1_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    #ventana juego 2
    def game2_window():
        root.withdraw()
        game2_window = Toplevel()
        game2_window.title('App Store')
        game2_window.minsize(1000, 600)
        game2_window.resizable(width = NO, height = NO)

        game2_line = read_games_esp[2]
        game2_info = game2_line.split(',')

        game2_canvas = Canvas(game2_window, width = 1000, height = 600, bg = 'white')
        game2_canvas.place(x=0, y=0)

        game2_largeIcon_pic = Label(game2_canvas, image = game2_largeIcon)
        game2_largeIcon_pic.place(x=100, y=70)

        game2_label = Label(game2_canvas, text = game2_info[3], font = 'Helvetica 30')
        game2_label.place(x=95, y=250)

        game2_scr1_pic = Label(game2_canvas, image = game2_scr1)
        game2_scr1_pic.place(x=450, y=30)

        game2_scr2_pic = Label(game2_canvas, image = game2_scr2)
        game2_scr2_pic.place(x=730, y= 30)

        game2_desc = Label(game2_canvas, font = 'Helvetica 24', text = game2_info[4], justify = LEFT)
        game2_desc.place(x=25, y=380)

        game2_desc2 = Label(game2_canvas, font = 'Helvetica 24', text = game2_info[5], justify = LEFT)
        game2_desc2.place(x=25, y=410)

        game2_desc3 = Label(game2_canvas, font = 'Helvetica 24', text = game2_info[6], justify = LEFT)
        game2_desc3.place(x=25, y=440)

        game2_desc4 = Label(game2_canvas, font = 'Helvetica 24', text = game2_info[7], justify = LEFT)
        game2_desc4.place(x=25, y=470)

        game2_desc5 = Label(game2_canvas, font = 'Helvetica 24', text = game2_info[8], justify = LEFT)
        game2_desc5.place(x=25, y=500)

        game2_size = Label(game2_canvas, font = 'Helvetica 24', text = 'Tamaño: '+game2_info[10])
        game2_size.place(x=25, y=540)

        game2_price = Label(game2_canvas, image = price099)
        game2_price.place(x=115, y=300)
    
        def backtoroot():
            game2_window.destroy()

        backbutton = Button(game2_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    #ventana juego 3
    def game3_window():
        root.withdraw()
        game3_window = Toplevel()
        game3_window.title('App Store')
        game3_window.minsize(1000, 600)
        game3_window.resizable(width = NO, height = NO)

        game3_line = read_games_esp[3]
        game3_info = game3_line.split(',')

        game3_canvas = Canvas(game3_window, width = 1000, height = 600, bg = 'white')
        game3_canvas.place(x=0, y=0)

        game3_largeIcon_pic = Label(game3_canvas, image = game3_largeIcon)
        game3_largeIcon_pic.place(x=100, y=70)

        game3_label = Label(game3_canvas, text = game3_info[3], font = 'Helvetica 30')
        game3_label.place(x=135, y=260)

        game3_scr1_pic = Label(game3_canvas, image = game3_scr1)
        game3_scr1_pic.place(x=450, y=30)

        game3_scr2_pic = Label(game3_canvas, image = game3_scr2)
        game3_scr2_pic.place(x=730, y= 30)

        game3_desc = Label(game3_canvas, font = 'Helvetica 24', text = game3_info[4], justify = LEFT)
        game3_desc.place(x=25, y=380)

        game3_desc2 = Label(game3_canvas, font = 'Helvetica 24', text = game3_info[5], justify = LEFT)
        game3_desc2.place(x=25, y=410)

        game3_desc3 = Label(game3_canvas, font = 'Helvetica 24', text = game3_info[6], justify = LEFT)
        game3_desc3.place(x=25, y=440)

        game3_desc4 = Label(game3_canvas, font = 'Helvetica 24', text = game3_info[7], justify = LEFT)
        game3_desc4.place(x=25, y=470)

        game3_desc5 = Label(game3_canvas, font = 'Helvetica 24', text = game3_info[8], justify = LEFT)
        game3_desc5.place(x=25, y=500)

        game3_size = Label(game3_canvas, font = 'Helvetica 24', text = 'Tamaño: '+game3_info[10])
        game3_size.place(x=25, y=540)

        game3_price = Label(game3_canvas, image = price699)
        game3_price.place(x=115, y=300)

        def backtoroot():
            game3_window.destroy()

        backbutton = Button(game3_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    #ventana juego 4
    def game4_window():
        root.withdraw()
        game4_window = Toplevel()
        game4_window.title('App Store')
        game4_window.minsize(1000, 600)
        game4_window.resizable(width = NO, height = NO)

        game4_line = read_games_esp[4]
        game4_info = game4_line.split(',')

        game4_canvas = Canvas(game4_window, width = 1000, height = 600, bg = 'white')
        game4_canvas.place(x=0, y=0)

        game4_largeIcon_pic = Label(game4_canvas, image = game4_largeIcon)
        game4_largeIcon_pic.place(x=100, y=70)

        game4_label = Label(game4_canvas, text = game4_info[3], font = 'Helvetica 30')
        game4_label.place(x=85, y=260)

        game4_scr1_pic = Label(game4_canvas, image = game4_scr1)
        game4_scr1_pic.place(x=450, y=30)

        game4_scr2_pic = Label(game4_canvas, image = game4_scr2)
        game4_scr2_pic.place(x=730, y= 30)

        game4_desc = Label(game4_canvas, font = 'Helvetica 24', text = game4_info[4], justify = LEFT)
        game4_desc.place(x=25, y=380)

        game4_desc2 = Label(game4_canvas, font = 'Helvetica 24', text = game4_info[5], justify = LEFT)
        game4_desc2.place(x=25, y=410)

        game4_desc3 = Label(game4_canvas, font = 'Helvetica 24', text = game4_info[6], justify = LEFT)
        game4_desc3.place(x=25, y=440)

        game4_desc4 = Label(game4_canvas, font = 'Helvetica 24', text = game4_info[7], justify = LEFT)
        game4_desc4.place(x=25, y=470)

        game4_desc5 = Label(game4_canvas, font = 'Helvetica 24', text = game4_info[8], justify = LEFT)
        game4_desc5.place(x=25, y=500)

        game4_size = Label(game4_canvas, font = 'Helvetica 24', text = 'Tamaño: '+game4_info[10])
        game4_size.place(x=25, y=540)

        game4_price = Label(game4_canvas, image = price099)
        game4_price.place(x=115, y=300)
    
        def backtoroot():
            game4_window.destroy()

        backbutton = Button(game4_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    #ventana juego 5
    def game5_window():
        root.withdraw()
        game5_window = Toplevel()
        game5_window.title('App Store')
        game5_window.minsize(1000, 600)
        game5_window.resizable(width = NO, height = NO)

        game5_line = read_games_esp[5]
        game5_info = game5_line.split(',')

        game5_canvas = Canvas(game5_window, width = 1000, height = 600, bg = 'white')
        game5_canvas.place(x=0, y=0)

        game5_largeIcon_pic = Label(game5_canvas, image = game5_largeIcon)
        game5_largeIcon_pic.place(x=100, y=70)

        game5_label = Label(game5_canvas, text = game5_info[3], font = 'Helvetica 30')
        game5_label.place(x=70, y=260)

        game5_scr1_pic = Label(game5_canvas, image = game5_scr1)
        game5_scr1_pic.place(x=450, y=30)

        game5_scr2_pic = Label(game5_canvas, image = game5_scr2)
        game5_scr2_pic.place(x=730, y= 30)

        game5_desc = Label(game5_canvas, font = 'Helvetica 24', text = game5_info[4], justify = LEFT)
        game5_desc.place(x=25, y=380)

        game5_desc2 = Label(game5_canvas, font = 'Helvetica 24', text = game5_info[5], justify = LEFT)
        game5_desc2.place(x=25, y=410)

        game5_desc3 = Label(game5_canvas, font = 'Helvetica 24', text = game5_info[6], justify = LEFT)
        game5_desc3.place(x=25, y=440)

        game5_desc4 = Label(game5_canvas, font = 'Helvetica 24', text = game5_info[7], justify = LEFT)
        game5_desc4.place(x=25, y=470)

        game5_desc5 = Label(game5_canvas, font = 'Helvetica 24', text = game5_info[8], justify = LEFT)
        game5_desc5.place(x=25, y=500)

        game5_size = Label(game5_canvas, font = 'Helvetica 24', text = 'Tamaño: '+game5_info[10])
        game5_size.place(x=25, y=540)

        game5_price = Label(game5_canvas, image = price299)
        game5_price.place(x=115, y=300)

        def backtoroot():
            game5_window.destroy()

        backbutton = Button(game5_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    #ventana juego 6
    def game6_window():
        root.withdraw()
        game6_window = Toplevel()
        game6_window.title('App Store')
        game6_window.minsize(1000, 600)
        game6_window.resizable(width = NO, height = NO)

        game6_line = read_games_esp[6]
        game6_info = game6_line.split(',')

        game6_canvas = Canvas(game6_window, width = 1000, height = 600, bg = 'white')
        game6_canvas.place(x=0, y=0)

        game6_largeIcon_pic = Label(game6_canvas, image = game6_largeIcon)
        game6_largeIcon_pic.place(x=100, y=70)

        game6_label = Label(game6_canvas, text = game6_info[3], font = 'Helvetica 30')
        game6_label.place(x=90, y=260)

        game6_scr1_pic = Label(game6_canvas, image = game6_scr1)
        game6_scr1_pic.place(x=450, y=30)

        game6_scr2_pic = Label(game6_canvas, image = game6_scr2)
        game6_scr2_pic.place(x=730, y= 30)

        game6_desc = Label(game6_canvas, font = 'Helvetica 24', text = game6_info[4], justify = LEFT)
        game6_desc.place(x=25, y=380)

        game6_desc2 = Label(game6_canvas, font = 'Helvetica 24', text = game6_info[5], justify = LEFT)
        game6_desc2.place(x=25, y=410)

        game6_desc3 = Label(game6_canvas, font = 'Helvetica 24', text = game6_info[6], justify = LEFT)
        game6_desc3.place(x=25, y=440)

        game6_desc4 = Label(game6_canvas, font = 'Helvetica 24', text = game6_info[7], justify = LEFT)
        game6_desc4.place(x=25, y=470)

        game6_desc5 = Label(game6_canvas, font = 'Helvetica 24', text = game6_info[8], justify = LEFT)
        game6_desc5.place(x=25, y=500)

        game6_size = Label(game6_canvas, font = 'Helvetica 24', text = 'Tamaño: '+game6_info[10])
        game6_size.place(x=25, y=540)

        game6_price = Label(game6_canvas, image = price699)
        game6_price.place(x=115, y=300)

        def backtoroot():
            game6_window.destroy()

        backbutton = Button(game6_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    #ventana juego 7
    def game7_window():
        root.withdraw()
        game7_window = Toplevel()
        game7_window.title('App Store')
        game7_window.minsize(1000, 600)
        game7_window.resizable(width = NO, height = NO)

        game7_line = read_games_esp[7]
        game7_info = game7_line.split(',')

        game7_canvas = Canvas(game7_window, width = 1000, height = 600, bg = 'white')
        game7_canvas.place(x=0, y=0)

        game7_largeIcon_pic = Label(game7_canvas, image = game7_largeIcon)
        game7_largeIcon_pic.place(x=100, y=70)

        game7_label = Label(game7_canvas, text = game7_info[3], font = 'Helvetica 30')
        game7_label.place(x=100, y=260)

        game7_scr1_pic = Label(game7_canvas, image = game7_scr1)
        game7_scr1_pic.place(x=450, y=30)

        game7_scr2_pic = Label(game7_canvas, image = game7_scr2)
        game7_scr2_pic.place(x=730, y= 30)

        game7_desc = Label(game7_canvas, font = 'Helvetica 24', text = game7_info[4], justify = LEFT)
        game7_desc.place(x=25, y=380)

        game7_desc2 = Label(game7_canvas, font = 'Helvetica 24', text = game7_info[5], justify = LEFT)
        game7_desc2.place(x=25, y=410)

        game7_desc3 = Label(game7_canvas, font = 'Helvetica 24', text = game7_info[6], justify = LEFT)
        game7_desc3.place(x=25, y=440)

        game7_desc4 = Label(game7_canvas, font = 'Helvetica 24', text = game7_info[7], justify = LEFT)
        game7_desc4.place(x=25, y=470)

        game7_desc5 = Label(game7_canvas, font = 'Helvetica 24', text = game7_info[8], justify = LEFT)
        game7_desc5.place(x=25, y=500)

        game7_size = Label(game7_canvas, font = 'Helvetica 24', text = 'Tamaño: '+game7_info[10])
        game7_size.place(x=25, y=540)

        game7_price = Label(game7_canvas, image = price0)
        game7_price.place(x=115, y=300)
        
        def backtoroot():
            game7_window.destroy()

        backbutton = Button(game7_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    #ventana juego 8
    def game8_window():
        root.withdraw()
        game8_window = Toplevel()
        game8_window.title('App Store')
        game8_window.minsize(1000, 600)
        game8_window.resizable(width = NO, height = NO)

        game8_line = read_games_esp[8]
        game8_info = game8_line.split(',')

        game8_canvas = Canvas(game8_window, width = 1000, height = 600, bg = 'white')
        game8_canvas.place(x=0, y=0)

        game8_largeIcon_pic = Label(game8_canvas, image = game8_largeIcon)
        game8_largeIcon_pic.place(x=100, y=70)

        game8_label = Label(game8_canvas, text = game8_info[3], font = 'Helvetica 30')
        game8_label.place(x=130, y=260)

        game8_scr1_pic = Label(game8_canvas, image = game8_scr1)
        game8_scr1_pic.place(x=450, y=30)

        game8_scr2_pic = Label(game8_canvas, image = game8_scr2)
        game8_scr2_pic.place(x=730, y= 30)

        game8_desc = Label(game8_canvas, font = 'Helvetica 24', text = game8_info[4], justify = LEFT)
        game8_desc.place(x=25, y=380)

        game8_desc2 = Label(game8_canvas, font = 'Helvetica 24', text = game8_info[5], justify = LEFT)
        game8_desc2.place(x=25, y=410)

        game8_desc3 = Label(game8_canvas, font = 'Helvetica 24', text = game8_info[6], justify = LEFT)
        game8_desc3.place(x=25, y=440)

        game8_desc4 = Label(game8_canvas, font = 'Helvetica 24', text = game8_info[7], justify = LEFT)
        game8_desc4.place(x=25, y=470)

        game8_desc5 = Label(game8_canvas, font = 'Helvetica 24', text = game8_info[8], justify = LEFT)
        game8_desc5.place(x=25, y=500)

        game8_size = Label(game8_canvas, font = 'Helvetica 24', text = 'Tamaño: '+game8_info[10])
        game8_size.place(x=25, y=540)

        game8_price = Label(game8_canvas, image = price0)
        game8_price.place(x=115, y=300)
    
        def backtoroot():
            game8_window.destroy()

        backbutton = Button(game8_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    #funcion para asignar tecla 'Enter' a boton de busqueda
    #E: tecla
    #S: activar boton de busqueda
    def return_key(key):
        searchWindow()

    root_esp_not_logged.bind('<Return>', return_key)
    
    #labels de registro y login
    login_label = Label(root_esp_not_logged, text = 'Acceso', font = 'Helvetica 20')
    login_label.place(x=20, y=75)

    register_label = Label(root_esp_not_logged, text = 'Registro', font = 'Helvetica 20')
    register_label.place(x=90, y=75)

    #otros labels
    aotd_label = Label(root_esp_not_logged, text = 'App Destacada', font = 'Helvetica 26')
    aotd_label.place(x=250, y=105)

    cat_label = Label(root_esp_not_logged, text = 'Categorías', font = 'Helvetica 26')
    cat_label.place(x=760, y=105)

    games_label = Label(root_esp_not_logged, text = 'Juegos', font = 'Helvetica 26')
    games_label.place(x=720, y=205)

    apps_label = Label(root_esp_not_logged, text = 'Apps', font = 'Helvetica 26')
    apps_label.place(x=730, y=320)

    #labels de apps destacadas
    app2_label = Label(root_esp_not_logged, text = app2_info[3], font = 'Helvetica 16')
    app2_label.place(x=30, y=530)

    app2_pricelabel = Label(root_esp_not_logged, text = app2_info[9], font = 'Helvetica 16')
    app2_pricelabel.place(x=70, y=550)

    app3_label = Label(root_esp_not_logged, text = app3_info[3], font = 'Helvetica 16')
    app3_label.place(x=220, y=530)

    app3_pricelabel = Label(root_esp_not_logged, text = app3_info[9], font = 'Helvetica 16')
    app3_pricelabel.place(x=275, y=550)

    game1_label = Label(root_esp_not_logged, text = game1_info[3], font = 'Helvetica 16')
    game1_label.place(x=465, y=530)

    game1_pricelabel = Label(root_esp_not_logged, text = game1_info[9], font = 'Helvetica 16')
    game1_pricelabel.place(x=475, y=550)

    game2_label = Label(root_esp_not_logged, text = game2_info[3], font = 'Helvetica 16')
    game2_label.place(x=650, y=530)

    game2_pricelabel = Label(root_esp_not_logged, text = game2_info[9], font = 'Helvetica 16')
    game2_pricelabel.place(x=675, y=550)

    game3_label = Label(root_esp_not_logged, text = game3_info[3], font = 'Helvetica 16')
    game3_label.place(x=870, y=530)

    game3_pricelabel = Label(root_esp_not_logged, text = game3_info[9], font = 'Helvetica 16')
    game3_pricelabel.place(x=875, y=550)

    #botones de apps
    app1_ad_pic = Button(root_esp_not_logged, image = app1_ad_esp, command = app1_window)
    app1_ad_pic.place(x=0, y=150)

    app2_pic = Button(root_esp_not_logged, image = app2_icon, command = app2_window)
    app2_pic.place(x=40, y=420)

    app3_pic = Button(root_esp_not_logged, image = app3_icon, command = app3_window)
    app3_pic.place(x=240, y=420)

    game1_pic = Button(root_esp_not_logged, image = game1_icon, command = game1_window)
    game1_pic.place(x=440, y=420)

    game2_pic = Button(root_esp_not_logged, image = game2_icon, command = game2_window)
    game2_pic.place(x=640, y=420)

    game3_pic = Button(root_esp_not_logged, image = game3_icon, command = game3_window)
    game3_pic.place(x=840, y=420)

    #iconos de categorias
    games_icon_pic = Button(root_esp_not_logged, image = games_icon, command = games_menu)
    games_icon_pic.place(x=840, y=165)

    apps_icon_pic = Button(root_esp_not_logged, image = apps_icon, command = apps_menu)
    apps_icon_pic.place(x=840, y=285)

    #sistema de busqueda
    search_label = Button(root_esp_not_logged, image = search_icon, command = searchWindow)
    search_label.place(x=900,y=63)

    search_entry = Entry(root_esp_not_logged, width = 20)
    search_entry.place(x=720,y=70)

    #login and register buttons
    login_button = Button(root_esp_not_logged, image = login_icon, command = loginWindow)
    login_button.place(x=20, y=10)

    register_button = Button(root_esp_not_logged, image = register_icon, command = registerWindow)
    register_button.place(x=100, y= 10)
    
#ventana de menu principal en español con acceso de usuario
def root_esp():
    root_esp = Toplevel()
    root_esp.title('App Store')
    root_esp.minsize(1000, 600)
    root_esp.resizable(width = NO, height = NO)

    #funcion para cambiar de region
    def root_eng():
        root_esp.destroy()
        root_eng_logged()

    #labels
    welcome_label = Label(root_esp, text='Bienvenido a la AStore', font = 'Helvetica 28')
    welcome_label.place(x=340, y=0)

    change_lang_label = Label(root_esp, text = 'Cambiar región', font = 'Helvetica 16')
    change_lang_label.place(x=780, y=5)

    change_lang_cr = Button(root_esp, image = us_flag, command = root_eng)
    change_lang_cr.place(x=890, y=0)

    #leer lineas de txt apps y juegos
    apps_esp = open('apps_esp.txt', 'r+')
    read_apps_esp = apps_esp.readlines()

    app1_line = read_apps_esp[1]
    app1_info = app1_line.split(',')
    app2_line = read_apps_esp[2]
    app2_info = app2_line.split(',')
    app3_line = read_apps_esp[3]
    app3_info = app3_line.split(',')
    app4_line = read_apps_esp[4]
    app4_info = app4_line.split(',')
    app5_line = read_apps_esp[5]
    app5_info = app5_line.split(',')
    app6_line = read_apps_esp[6]
    app6_info = app6_line.split(',')
    app7_line = read_apps_esp[7]
    app7_info = app7_line.split(',')
    app8_line = read_apps_esp[8]
    app8_info = app8_line.split(',')

    games_esp = open('games_esp.txt', 'r+')
    read_games_esp = games_esp.readlines()

    game1_line = read_games_esp[1]
    game1_info = game1_line.split(',')
    game2_line = read_games_esp[2]
    game2_info = game2_line.split(',')
    game3_line = read_games_esp[3]
    game3_info = game3_line.split(',')
    game4_line = read_games_esp[4]
    game4_info = game4_line.split(',')
    game5_line = read_games_esp[5]
    game5_info = game5_line.split(',')
    game6_line = read_games_esp[6]
    game6_info = game6_line.split(',')
    game7_line = read_games_esp[7]
    game7_info = game7_line.split(',')
    game8_line = read_games_esp[8]
    game8_info = game8_line.split(',')

    ##############################################################################

    #sistema de busqueda con nombre de app o palabra alusiva
    #E: palabra a buscar
    #S: redireccion
    #R: nombre de app o palabra alusiva

    def searchWindow():
        apps = open('apps.txt', 'r+')
        read_apps = apps.readlines()
        
        app1_line = read_apps[1]
        app1_info = app1_line.split(',')
        app2_line = read_apps[2]
        app2_info = app2_line.split(',')
        app3_line = read_apps[3]
        app3_info = app3_line.split(',')
        app4_line = read_apps[4]
        app4_info = app4_line.split(',')
        app5_line = read_apps[5]
        app5_info = app5_line.split(',')
        app6_line = read_apps[6]
        app6_info = app6_line.split(',')
        app7_line = read_apps[7]
        app7_info = app7_line.split(',')
        app8_line = read_apps[8]
        app8_info = app8_line.split(',')
        apps.close()

        games = open('games.txt', 'r+')
        read_games = games.readlines()

        game1_line = read_games[1]
        game1_info = game1_line.split(',')
        game2_line = read_games[2]
        game2_info = game2_line.split(',')
        game3_line = read_games[3]
        game3_info = game3_line.split(',')
        game4_line = read_games[4]
        game4_info = game4_line.split(',')
        game5_line = read_games[5]
        game5_info = game5_line.split(',')
        game6_line = read_games[6]
        game6_info = game6_line.split(',')
        game7_line = read_games[7]
        game7_info = game7_line.split(',')
        game8_line = read_games[8]
        game8_info = game8_line.split(',')
        games.close()
        apps = open('apps.txt', 'r+')
        read_apps = apps.readlines()
        searchText=search_entry.get()

        if searchText.strip() == 'juegos':
            games_menu()
        if searchText.strip() == 'juego':
            games_menu()
        elif searchText.strip() == 'aplicaciones':
            apps_menu()
        elif searchText.strip() == 'aplicacion':
            apps_menu()
        elif searchText.strip() == 'apps':
            apps_menu()
        elif searchText.strip() == 'aps':
            apps_menu()
        elif searchText.strip() == 'games':
            games_menu()
        elif searchText.strip() == 'jugar':
            games_menu()
        elif searchText.strip() == 'play':
            games_menu()
        elif searchText.strip() == 'jeff schmidt python':
            app1_window()
        elif searchText.strip() == 'jeff schmidts python':
            app1_window()
        elif searchText.strip() == 'python':
            app1_window()
        elif searchText.strip() == 'Python':
            app1_window()
        elif searchText.strip() == 'Jeff':
            app1_window()
        elif searchText.strip() == 'jeff':
            app1_window()
        elif searchText.strip() == 'jeff schmidt':
            app1_window()
        elif searchText.strip() == 'schmidt':
            app1_window()
        elif searchText.strip() == 'Schmidt':
            app1_window()
        elif searchText.strip() == 'code':
            app1_window()
        elif searchText.strip() == 'programming':
            app1_window()
        elif searchText.strip() == 'programar':
            app1_window()
        elif searchText.strip() == 'weed smoke pro':
            app2_window()
        elif searchText.strip() == 'weed':
            app2_window()
        elif searchText.strip() == 'smoke':
            app2_window()
        elif searchText.strip() == 'weed smoke':
            app2_window()
        elif searchText.strip() == 'marijuana':
            app2_window()
        elif searchText.strip() == '420':
            app2_window()
        elif searchText.strip() == 'bob marley':
            app2_window()
        elif searchText.strip() == 'math with ed sheeran':
            app3_window()
        elif searchText.strip() == 'ed sheeran':
            app3_window()
        elif searchText.strip() == 'ed':
            app3_window()
        elif searchText.strip() == 'sheeran':
            app3_window()
        elif searchText.strip() == 'math':
            app3_window()
        elif searchText.strip() == 'matematica':
            app3_window()
        elif searchText.strip() == 'mate':
            app3_window()
        elif searchText.strip() == 'you look perfect tonight':
            app3_window()
        elif searchText.strip() == 'taylors swift':
            app4_window()
        elif searchText.strip() == 'taylor swift':
            app4_window()
        elif searchText.strip() == 'swift':
            app4_window()
        elif searchText.strip() == 'taylor':
            app4_window()
        elif searchText.strip() == 'swift code':
            app4_window()
        elif searchText.strip() == 'swift language':
            app4_window()
        elif searchText.strip() == 'swift lenguaje':
            app4_window()
        elif searchText.strip() == 'the pirate bay':
            app5_window()
        elif searchText.strip() == 'free movies':
            app5_window()
        elif searchText.strip() == 'peliculas gratis':
            app5_window()
        elif searchText.strip() == 'pirate':
            app5_window()
        elif searchText.strip() == 'pirate bay':
            app5_window()
        elif searchText.strip() == 'piratear':
            app5_window()
        elif searchText.strip() == 'free tv':
            app5_window()
        elif searchText.strip() == 'torrent':
            app5_window()
        elif searchText.strip() == 'apple music':
            app6_window()
        elif searchText.strip() == 'apple':
            app6_window()
        elif searchText.strip() == 'music':
            app6_window()
        elif searchText.strip() == 'free music':
            app6_window()
        elif searchText.strip() == 'musica gratis':
            app6_window()
        elif searchText.strip() == 'netflix':
            app7_window()
        elif searchText.strip() == 'series':
            app7_window()
        elif searchText.strip() == 'tv shows':
            app7_window()
        elif searchText.strip() == 'movies':
            app7_window()
        elif searchText.strip() == 'peliculas':
            app7_window()
        elif searchText.strip() == 'netflix':
            app7_window()
        elif searchText.strip() == 'im feeling lucky':
            app8_window()
        elif searchText.strip() == 'kiss me pls':
            app8_window()
        elif searchText.strip() == 'kiss me':
            app8_window()
        elif searchText.strip() == 'notlim':
            game1_window()
        elif searchText.strip() == 'Notlim':
            game1_window()
        elif searchText.strip() == 'mining':
            game1_window()
        elif searchText.strip() == 'intro & taller':
            game2_window()
        elif searchText.strip() == 'intro y taller':
            game2_window()
        elif searchText.strip() == 'Intro y Taller':
            game2_window()
        elif searchText.strip() == 'Intro & taller':
            game2_window()
        elif searchText.strip() == 'intro':
            game2_window()
        elif searchText.strip() == 'taller':
            game2_window()
        elif searchText.strip() == 'samus aran':
            game2_window()
        elif searchText.strip() == 'conejos':
            game2_window()
        elif searchText.strip() == 'arnold schwarzenegger':
            game2_window()
        elif searchText.strip() == 'jessie':
            game3_window()
        elif searchText.strip() == 'ingeniera':
            game3_window()
        elif searchText.strip() == 'engineer':
            game3_window()
        elif searchText.strip() == 'game of shots':
            game4_window()
        elif searchText.strip() == 'shots':
            game4_window()
        elif searchText.strip() == 'drinking game':
            game4_window()
        elif searchText.strip() == 'alcohol':
            game4_window()
        elif searchText.strip() == 'tragos':
            game4_window()
        elif searchText.strip() == 'monument valley':
            game5_window()
        elif searchText.strip() == 'arquitectura':
            game5_window()
        elif searchText.strip() == 'architecture':
            game5_window()
        elif searchText.strip() == 'monument':
            game5_window()
        elif searchText.strip() == 'valley':
            game5_window()
        elif searchText.strip() == 'life is strange':
            game6_window()
        elif searchText.strip() == 'life':
            game6_window()
        elif searchText.strip() == 'strange':
            game6_window()
        elif searchText.strip() == 'max caulfield':
            game6_window()
        elif searchText.strip() == 'blackwell':
            game6_window()
        elif searchText.strip() == 'unbreakable':
            game7_window()
        elif searchText.strip() == 'jeff schmidt game':
            game7_window()
        elif searchText.strip() == 'jeff schmidt juego':
            game7_window()
        elif searchText.strip() == 'stocks':
            game8_window()
        elif searchText.strip() == 'bolsa':
            game8_window()
        elif searchText.strip() == 'dinero':
            game8_window()
        elif searchText.strip() == 'money':
            game8_window()
        elif searchText.strip() == 'strategy':
            game8_window()
        elif searchText.strip() == 'estrategia':
            game8_window()
        elif searchText.strip() == app1_info[3].strip():
            app1_window()
        elif searchText.strip() == app2_info[3].strip():
            app2_window()   
        elif searchText.strip() == app3_info[3].strip():
            app3_window()
        elif searchText.strip() == app4_info[3].strip():
            app4_window()
        elif searchText.strip() == app5_info[3].strip():
            app5_window()
        elif searchText.strip() == app6_info[3].strip():
            app6_window()
        elif searchText.strip() == app7_info[3].strip():
            app7_window()
        elif searchText.strip() == app8_info[3].strip():
            app8_window()
        elif searchText.strip() == game1_info[3].strip():
            game1_window()
        elif searchText.strip() == game2_info[3].strip():
            game2_window()
        elif searchText.strip() == game3_info[3].strip():
            game3_window()
        elif searchText.strip() == game4_info[3].strip():
            game4_window()
        elif searchText.strip() == game5_info[3].strip():
            game5_window()
        elif searchText.strip() == game6_info[3].strip():
            game6_window()
        elif searchText.strip() == game7_info[3].strip():
            game7_window()
        elif searchText.strip() == game8_info[3].strip():
            game8_window()
        else:
            messagebox.showwarning("Search results:",searchText+' not found')

    ###############################################################################

    #menu de apps
    def apps_menu():
        apps_menu = Toplevel()
        apps_menu.title('App Store')
        apps_menu.minsize(1000, 600)
        apps_menu.resizable(width = NO, height = NO)

        appsmenu_canvas = Canvas(apps_menu, width = 1000, height = 600, bg = 'white')
        appsmenu_canvas.place(x=0, y=0)

        #
        app1_icon = Button(appsmenu_canvas, image = app1_largeIcon, command = app1_window)
        app1_icon.place(x=60, y=70)

        app1_label = Label(appsmenu_canvas, text = app1_info[3], font = 'Helvetica 24')
        app1_label.place(x=30, y=270)

        app1_price = Label(appsmenu_canvas, text = app1_info[9], font = 'Helvetica 24')
        app1_price.place(x=120, y=300)

        #
        app2_icon = Button(appsmenu_canvas, image = app2_largeIcon, command = app2_window)
        app2_icon.place(x=290, y=70)

        app2_label = Label(appsmenu_canvas, text = app2_info[3], font = 'Helvetica 24')
        app2_label.place(x=280, y=270)

        app2_price = Label(appsmenu_canvas, text = app2_info[9], font = 'Helvetica 24')
        app2_price.place(x=360, y=300)

        #
        app3_icon = Button(appsmenu_canvas, image = app3_largeIcon, command = app3_window)
        app3_icon.place(x=520, y=70)

        app3_label = Label(appsmenu_canvas, text = app3_info[3], font = 'Helvetica 24')
        app3_label.place(x=500, y=270)

        app3_price = Label(appsmenu_canvas, text = app3_info[9], font = 'Helvetica 24')
        app3_price.place(x=580, y=300)

        #
        app4_icon = Button(appsmenu_canvas, image = app4_largeIcon, command = app4_window)
        app4_icon.place(x=750, y=70)

        app4_label = Label(appsmenu_canvas, text = app4_info[3], font = 'Helvetica 24')
        app4_label.place(x=765, y=270)

        app4_price = Label(appsmenu_canvas, text = app4_info[9], font = 'Helvetica 24')
        app4_price.place(x=810, y=300)

        #
        app5_icon = Button(appsmenu_canvas, image = app5_largeIcon, command = app5_window)
        app5_icon.place(x=60, y=350)

        app5_label = Label(appsmenu_canvas, text = app5_info[3], font = 'Helvetica 24')
        app5_label.place(x=65, y=540)

        app5_price = Label(appsmenu_canvas, text = app5_info[9], font = 'Helvetica 24')
        app5_price.place(x=115, y=570)

        #
        app6_icon = Button(appsmenu_canvas, image = app6_largeIcon, command = app6_window)
        app6_icon.place(x=290, y=350)

        app6_label = Label(appsmenu_canvas, text = app6_info[3], font = 'Helvetica 24')
        app6_label.place(x=310, y=540)

        app6_price = Label(appsmenu_canvas, text = app6_info[9], font = 'Helvetica 24')
        app6_price.place(x=345, y=570)

        #
        app7_icon = Button(appsmenu_canvas, image = app7_largeIcon, command = app7_window)
        app7_icon.place(x=520, y=350)

        app7_label = Label(appsmenu_canvas, text = app7_info[3], font = 'Helvetica 24')
        app7_label.place(x=570, y=540)

        app7_price = Label(appsmenu_canvas, text = app7_info[9], font = 'Helvetica 24')
        app7_price.place(x=575, y=570)

        #
        app8_icon = Button(appsmenu_canvas, image = app8_largeIcon, command = app8_window)
        app8_icon.place(x=750, y=350)
        
        app8_label = Label(appsmenu_canvas, text = app8_info[3], font = 'Helvetica 24')
        app8_label.place(x=780, y=540)

        app8_price = Label(appsmenu_canvas, text = app8_info[9], font = 'Helvetica 24')
        app8_price.place(x=810, y=570)

        def backtoroot():
            apps_menu.destroy()

        backbutton = Button(apps_menu, image = back_icon, command = backtoroot)
        backbutton.place(x=20, y=20)

    ###############################################################################

    #menu de juegos
    def games_menu():
        games_menu = Toplevel()
        games_menu.title('App Store')
        games_menu.minsize(1000, 600)
        games_menu.resizable(width = NO, height = NO)

        gamesmenu_canvas = Canvas(games_menu, width = 1000, height = 600, bg = 'white')
        gamesmenu_canvas.place(x=0, y=0)

        #
        game1_icon = Button(gamesmenu_canvas, image = game1_largeIcon, command = game1_window)
        game1_icon.place(x=60, y=70)

        game1_label = Label(gamesmenu_canvas, text = game1_info[3], font = 'Helvetica 24')
        game1_label.place(x=100, y=270)

        game1_price = Label(gamesmenu_canvas, text = game1_info[9], font = 'Helvetica 24')
        game1_price.place(x=120, y=300)

        #
        game2_icon = Button(gamesmenu_canvas, image = game2_largeIcon, command = game2_window)
        game2_icon.place(x=290, y=70)

        game2_label = Label(gamesmenu_canvas, text = game2_info[3], font = 'Helvetica 24')
        game2_label.place(x=315, y=270)

        game2_price = Label(gamesmenu_canvas, text = game2_info[9], font = 'Helvetica 24')
        game2_price.place(x=355, y=300)

        #
        game3_icon = Button(gamesmenu_canvas, image = game3_largeIcon, command = game3_window)
        game3_icon.place(x=520, y=70)

        game3_label = Label(gamesmenu_canvas, text = game3_info[3], font = 'Helvetica 24')
        game3_label.place(x=575, y=270)

        game3_price = Label(gamesmenu_canvas, text = game3_info[9], font = 'Helvetica 24')
        game3_price.place(x=580, y=300)

        #
        game4_icon = Button(gamesmenu_canvas, image = game4_largeIcon, command = game4_window)
        game4_icon.place(x=750, y=70)

        game4_label = Label(gamesmenu_canvas, text = game4_info[3], font = 'Helvetica 24')
        game4_label.place(x=760, y=270)

        game4_price = Label(gamesmenu_canvas, text = game4_info[9], font = 'Helvetica 24')
        game4_price.place(x=805, y=300)

        #
        game5_icon = Button(gamesmenu_canvas, image = game5_largeIcon, command = game5_window)
        game5_icon.place(x=60, y=350)

        game5_label = Label(gamesmenu_canvas, text = game5_info[3], font = 'Helvetica 24')
        game5_label.place(x=55, y=540)

        game5_price = Label(gamesmenu_canvas, text = game5_info[9], font = 'Helvetica 24')
        game5_price.place(x=110, y=570)

        #
        game6_icon = Button(gamesmenu_canvas, image = game6_largeIcon, command = game6_window)
        game6_icon.place(x=290, y=350)

        game6_label = Label(gamesmenu_canvas, text = game6_info[3], font = 'Helvetica 24')
        game6_label.place(x=300, y=540)

        game6_price = Label(gamesmenu_canvas, text = game6_info[9], font = 'Helvetica 24')
        game6_price.place(x=340, y=570)    

        #
        game7_icon = Button(gamesmenu_canvas, image = game7_largeIcon, command = game7_window)
        game7_icon.place(x=520, y=350)

        game7_label = Label(gamesmenu_canvas, text = game7_info[3], font = 'Helvetica 24')
        game7_label.place(x=540, y=540)

        game7_price = Label(gamesmenu_canvas, text = game7_info[9], font = 'Helvetica 24')
        game7_price.place(x=580, y=570)

        #
        game8_icon = Button(gamesmenu_canvas, image = game8_largeIcon, command = game8_window)
        game8_icon.place(x=750, y=350)

        game8_label = Label(gamesmenu_canvas, text = game8_info[3], font = 'Helvetica 24')
        game8_label.place(x=800, y=540)

        game8_price = Label(gamesmenu_canvas, text = game8_info[9], font = 'Helvetica 24')
        game8_price.place(x=805, y=570)

        def backtoroot():
            games_menu.destroy()

        backbutton = Button(games_menu, image = back_icon, command = backtoroot)
        backbutton.place(x=20, y=20)

    ###############################################################################

    #ventanas de apps
    def app1_window():
        root.withdraw()
        app1_window = Toplevel()
        app1_window.title('App Store')
        app1_window.minsize(1000, 600)
        app1_window.resizable(width = NO, height = NO)

        #leer lineas de app desde txt
        app1_line = read_apps_esp[1]
        app1_info = app1_line.split(',')

        app1_canvas = Canvas(app1_window, width = 1000, height = 600, bg = 'white')
        app1_canvas.place(x=0, y=0)

        #labels de app info
        app1_largeIcon_pic = Label(app1_canvas, image = app1_largeIcon)
        app1_largeIcon_pic.place(x=100, y=70)

        app1_label = Label(app1_canvas, text = app1_info[3], font = 'Helvetica 30')
        app1_label.place(x=70, y=250)

        app1_scr1_pic = Label(app1_canvas, image = app1_scr1)
        app1_scr1_pic.place(x=450, y=30)

        app1_scr2_pic = Label(app1_canvas, image = app1_scr2)
        app1_scr2_pic.place(x=730, y= 30)

        app1_desc = Label(app1_canvas, font = 'Helvetica 24', text = app1_info[4], justify = LEFT)
        app1_desc.place(x=25, y=380)

        app1_desc2 = Label(app1_canvas, font = 'Helvetica 24', text = app1_info[5], justify = LEFT)
        app1_desc2.place(x=25, y=410)

        app1_desc3 = Label(app1_canvas, font = 'Helvetica 24', text = app1_info[6], justify = LEFT)
        app1_desc3.place(x=25, y=440)

        app1_desc4 = Label(app1_canvas, font = 'Helvetica 24', text = app1_info[7], justify = LEFT)
        app1_desc4.place(x=25, y=470)

        app1_desc5 = Label(app1_canvas, font = 'Helvetica 24', text = app1_info[8], justify = LEFT)
        app1_desc5.place(x=25, y=500)

        app1_size = Label(app1_canvas, font = 'Helvetica 24', text = 'Tamaño:'+app1_info[10])
        app1_size.place(x=25, y=540)

        #funcion para agregar descarga a info de app
        def download():
            add_download = int(app1_info[11]) + 1
            app1_info[11] = add_download
            new_1 = app1_info[0] + ',' + app1_info[1] + ',' + app1_info[2] + ',' + app1_info[3] + ',' + app1_info[4] + ',' + app1_info[5] + ',' + app1_info[6] + ',' + app1_info[7] + ',' + app1_info[8] + ',' + app1_info[9] + ',' + app1_info[10] + ',' + str(app1_info[11])
            new_2 = app2_info[0] + ',' + app2_info[1] + ',' + app2_info[2] + ',' + app2_info[3] + ',' + app2_info[4] + ',' + app2_info[5] + ',' + app2_info[6] + ',' + app2_info[7] + ',' + app2_info[8] + ',' + app2_info[9] + ',' + app2_info[10] + ',' + app2_info[11]
            new_3 = app3_info[0] + ',' + app3_info[1] + ',' + app3_info[2] + ',' + app3_info[3] + ',' + app3_info[4] + ',' + app3_info[5] + ',' + app3_info[6] + ',' + app3_info[7] + ',' + app3_info[8] + ',' + app3_info[9] + ',' + app3_info[10] + ',' + app3_info[11]
            new_4 = app4_info[0] + ',' + app4_info[1] + ',' + app4_info[2] + ',' + app4_info[3] + ',' + app4_info[4] + ',' + app4_info[5] + ',' + app4_info[6] + ',' + app4_info[7] + ',' + app4_info[8] + ',' + app4_info[9] + ',' + app4_info[10] + ',' + app4_info[11]
            new_5 = app5_info[0] + ',' + app5_info[1] + ',' + app5_info[2] + ',' + app5_info[3] + ',' + app5_info[4] + ',' + app5_info[5] + ',' + app5_info[6] + ',' + app5_info[7] + ',' + app5_info[8] + ',' + app5_info[9] + ',' + app5_info[10] + ',' + app5_info[11]
            new_6 = app6_info[0] + ',' + app6_info[1] + ',' + app6_info[2] + ',' + app6_info[3] + ',' + app6_info[4] + ',' + app6_info[5] + ',' + app6_info[6] + ',' + app6_info[7] + ',' + app6_info[8] + ',' + app6_info[9] + ',' + app6_info[10] + ',' + app6_info[11]
            new_7 = app7_info[0] + ',' + app7_info[1] + ',' + app7_info[2] + ',' + app7_info[3] + ',' + app7_info[4] + ',' + app7_info[5] + ',' + app7_info[6] + ',' + app7_info[7] + ',' + app7_info[8] + ',' + app7_info[9] + ',' + app7_info[10] + ',' + app7_info[11]
            new_8 = app8_info[0] + ',' + app8_info[1] + ',' + app8_info[2] + ',' + app8_info[3] + ',' + app8_info[4] + ',' + app8_info[5] + ',' + app8_info[6] + ',' + app8_info[7] + ',' + app8_info[8] + ',' + app8_info[9] + ',' + app8_info[10] + ',' + app8_info[11]
            a = open('apps_esp.txt', 'w')
            b = a.close
            c = open('apps_esp.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsCR' + '\n')
            write1 = c.write(new_1 + '\n')
            write2 = c.write(new_2)
            write3 = c.write(new_3)
            write4 = c.write(new_4)
            write5 = c.write(new_5)
            write6 = c.write(new_6)
            write7 = c.write(new_7)
            write8 = c.write(new_8)
            d = c.close

        app1_price = Button(app1_canvas, image = price099, command = download)
        app1_price.place(x=115, y=300)

        def backtoroot():
            app1_window.destroy()

        backbutton = Button(app1_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    def app2_window():
        root.withdraw()
        app2_window = Toplevel()
        app2_window.title('App Store')
        app2_window.minsize(1000, 600)
        app2_window.resizable(width = NO, height = NO)

        app2_line = read_apps_esp[2]
        app2_info = app2_line.split(',')

        app2_canvas = Canvas(app2_window, width = 1000, height = 600, bg = 'white')
        app2_canvas.place(x=0, y=0)

        app2_largeIcon_pic = Label(app2_canvas, image = app2_largeIcon)
        app2_largeIcon_pic.place(x=100, y=60)

        app2_label = Label(app2_canvas, text = app2_info[3], font = 'Helvetica 30')
        app2_label.place(x=70, y=250)

        app2_scr1_pic = Label(app2_canvas, image = app2_scr1)
        app2_scr1_pic.place(x=450, y=30)

        app2_scr2_pic = Label(app2_canvas, image = app2_scr2)
        app2_scr2_pic.place(x=730, y= 30)

        app2_desc = Label(app2_canvas, font = 'Helvetica 24', text = app2_info[4], justify = LEFT)
        app2_desc.place(x=25, y=380)

        app2_desc2 = Label(app2_canvas, font = 'Helvetica 24', text = app2_info[5], justify = LEFT)
        app2_desc2.place(x=25, y=410)

        app2_desc3 = Label(app2_canvas, font = 'Helvetica 24', text = app2_info[6], justify = LEFT)
        app2_desc3.place(x=25, y=440)

        app2_desc4 = Label(app2_canvas, font = 'Helvetica 24', text = app2_info[7], justify = LEFT)
        app2_desc4.place(x=25, y=470)

        app2_desc5 = Label(app2_canvas, font = 'Helvetica 24', text = app2_info[8], justify = LEFT)
        app2_desc5.place(x=25, y=500)

        app2_size = Label(app2_canvas, font = 'Helvetica 24', text = 'Tamaño: '+app2_info[10])
        app2_size.place(x=25, y=540)

        #funcion para agregar descarga a info de app
        def download():
            add_download = int(app2_info[11]) + 1
            app2_info[11] = add_download
            new_1 = app1_info[0] + ',' + app1_info[1] + ',' + app1_info[2] + ',' + app1_info[3] + ',' + app1_info[4] + ',' + app1_info[5] + ',' + app1_info[6] + ',' + app1_info[7] + ',' + app1_info[8] + ',' + app1_info[9] + ',' + app1_info[10] + ',' + app1_info[11]
            new_2 = app2_info[0] + ',' + app2_info[1] + ',' + app2_info[2] + ',' + app2_info[3] + ',' + app2_info[4] + ',' + app2_info[5] + ',' + app2_info[6] + ',' + app2_info[7] + ',' + app2_info[8] + ',' + app2_info[9] + ',' + app2_info[10] + ',' + str(app2_info[11])
            new_3 = app3_info[0] + ',' + app3_info[1] + ',' + app3_info[2] + ',' + app3_info[3] + ',' + app3_info[4] + ',' + app3_info[5] + ',' + app3_info[6] + ',' + app3_info[7] + ',' + app3_info[8] + ',' + app3_info[9] + ',' + app3_info[10] + ',' + app3_info[11]
            new_4 = app4_info[0] + ',' + app4_info[1] + ',' + app4_info[2] + ',' + app4_info[3] + ',' + app4_info[4] + ',' + app4_info[5] + ',' + app4_info[6] + ',' + app4_info[7] + ',' + app4_info[8] + ',' + app4_info[9] + ',' + app4_info[10] + ',' + app4_info[11]
            new_5 = app5_info[0] + ',' + app5_info[1] + ',' + app5_info[2] + ',' + app5_info[3] + ',' + app5_info[4] + ',' + app5_info[5] + ',' + app5_info[6] + ',' + app5_info[7] + ',' + app5_info[8] + ',' + app5_info[9] + ',' + app5_info[10] + ',' + app5_info[11]
            new_6 = app6_info[0] + ',' + app6_info[1] + ',' + app6_info[2] + ',' + app6_info[3] + ',' + app6_info[4] + ',' + app6_info[5] + ',' + app6_info[6] + ',' + app6_info[7] + ',' + app6_info[8] + ',' + app6_info[9] + ',' + app6_info[10] + ',' + app6_info[11]
            new_7 = app7_info[0] + ',' + app7_info[1] + ',' + app7_info[2] + ',' + app7_info[3] + ',' + app7_info[4] + ',' + app7_info[5] + ',' + app7_info[6] + ',' + app7_info[7] + ',' + app7_info[8] + ',' + app7_info[9] + ',' + app7_info[10] + ',' + app7_info[11]
            new_8 = app8_info[0] + ',' + app8_info[1] + ',' + app8_info[2] + ',' + app8_info[3] + ',' + app8_info[4] + ',' + app8_info[5] + ',' + app8_info[6] + ',' + app8_info[7] + ',' + app8_info[8] + ',' + app8_info[9] + ',' + app8_info[10] + ',' + app8_info[11]
            a = open('apps_esp.txt', 'w')
            b = a.close
            c = open('apps_esp.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsCR' + '\n')
            write1 = c.write(new_1)
            write2 = c.write(new_2 + '\n')
            write3 = c.write(new_3)
            write4 = c.write(new_4)
            write5 = c.write(new_5)
            write6 = c.write(new_6)
            write7 = c.write(new_7)
            write8 = c.write(new_8)
            d = c.close
            
        app2_price = Button(app2_canvas, image = price420, command = download)
        app2_price.place(x=115, y=300)

        def backtoroot():
            app2_window.destroy()

        backbutton = Button(app2_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    def app3_window():
        root.withdraw()
        app3_window = Toplevel()
        app3_window.title('App Store')
        app3_window.minsize(1000, 600)
        app3_window.resizable(width = NO, height = NO)

        app3_line = read_apps_esp[3]
        app3_info = app3_line.split(',')

        app3_canvas = Canvas(app3_window, width = 1000, height = 600, bg = 'white')
        app3_canvas.place(x=0, y=0)

        app3_largeIcon_pic = Label(app3_canvas, image = app3_largeIcon)
        app3_largeIcon_pic.place(x=100, y=70)

        app3_label = Label(app3_canvas, text = app3_info[3], font = 'Helvetica 30')
        app3_label.place(x=50, y=250)

        app3_scr1_pic = Label(app3_canvas, image = app3_scr1)
        app3_scr1_pic.place(x=450, y=30)

        app3_scr2_pic = Label(app3_canvas, image = app3_scr2)
        app3_scr2_pic.place(x=700, y= 30)

        app3_desc = Label(app3_canvas, font = 'Helvetica 24', text = app3_info[4], justify = LEFT)
        app3_desc.place(x=25, y=380)

        app3_desc2 = Label(app3_canvas, font = 'Helvetica 24', text = app3_info[5], justify = LEFT)
        app3_desc2.place(x=25, y=410)

        app3_desc3 = Label(app3_canvas, font = 'Helvetica 24', text = app3_info[6], justify = LEFT)
        app3_desc3.place(x=25, y=440)

        app3_desc4 = Label(app3_canvas, font = 'Helvetica 24', text = app3_info[7], justify = LEFT)
        app3_desc4.place(x=25, y=470)

        app3_desc5 = Label(app3_canvas, font = 'Helvetica 24', text = app3_info[8], justify = LEFT)
        app3_desc5.place(x=25, y=500)

        app3_size = Label(app3_canvas, font = 'Helvetica 24', text = 'Tamaño: '+app3_info[10])
        app3_size.place(x=25, y=540)

        #funcion para agregar descarga a info de app
        def download():
            add_download = int(app3_info[11]) + 1
            app3_info[11] = add_download
            new_1 = app1_info[0] + ',' + app1_info[1] + ',' + app1_info[2] + ',' + app1_info[3] + ',' + app1_info[4] + ',' + app1_info[5] + ',' + app1_info[6] + ',' + app1_info[7] + ',' + app1_info[8] + ',' + app1_info[9] + ',' + app1_info[10] + ',' + app1_info[11]
            new_2 = app2_info[0] + ',' + app2_info[1] + ',' + app2_info[2] + ',' + app2_info[3] + ',' + app2_info[4] + ',' + app2_info[5] + ',' + app2_info[6] + ',' + app2_info[7] + ',' + app2_info[8] + ',' + app2_info[9] + ',' + app2_info[10] + ',' + app2_info[11]
            new_3 = app3_info[0] + ',' + app3_info[1] + ',' + app3_info[2] + ',' + app3_info[3] + ',' + app3_info[4] + ',' + app3_info[5] + ',' + app3_info[6] + ',' + app3_info[7] + ',' + app3_info[8] + ',' + app3_info[9] + ',' + app3_info[10] + ',' + str(app3_info[11])
            new_4 = app4_info[0] + ',' + app4_info[1] + ',' + app4_info[2] + ',' + app4_info[3] + ',' + app4_info[4] + ',' + app4_info[5] + ',' + app4_info[6] + ',' + app4_info[7] + ',' + app4_info[8] + ',' + app4_info[9] + ',' + app4_info[10] + ',' + app4_info[11]
            new_5 = app5_info[0] + ',' + app5_info[1] + ',' + app5_info[2] + ',' + app5_info[3] + ',' + app5_info[4] + ',' + app5_info[5] + ',' + app5_info[6] + ',' + app5_info[7] + ',' + app5_info[8] + ',' + app5_info[9] + ',' + app5_info[10] + ',' + app5_info[11]
            new_6 = app6_info[0] + ',' + app6_info[1] + ',' + app6_info[2] + ',' + app6_info[3] + ',' + app6_info[4] + ',' + app6_info[5] + ',' + app6_info[6] + ',' + app6_info[7] + ',' + app6_info[8] + ',' + app6_info[9] + ',' + app6_info[10] + ',' + app6_info[11]
            new_7 = app7_info[0] + ',' + app7_info[1] + ',' + app7_info[2] + ',' + app7_info[3] + ',' + app7_info[4] + ',' + app7_info[5] + ',' + app7_info[6] + ',' + app7_info[7] + ',' + app7_info[8] + ',' + app7_info[9] + ',' + app7_info[10] + ',' + app7_info[11]
            new_8 = app8_info[0] + ',' + app8_info[1] + ',' + app8_info[2] + ',' + app8_info[3] + ',' + app8_info[4] + ',' + app8_info[5] + ',' + app8_info[6] + ',' + app8_info[7] + ',' + app8_info[8] + ',' + app8_info[9] + ',' + app8_info[10] + ',' + app8_info[11]
            a = open('apps_esp.txt', 'w')
            b = a.close
            c = open('apps_esp.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsCR' + '\n')
            write1 = c.write(new_1)
            write2 = c.write(new_2)
            write3 = c.write(new_3 + '\n')
            write4 = c.write(new_4)
            write5 = c.write(new_5)
            write6 = c.write(new_6)
            write7 = c.write(new_7)
            write8 = c.write(new_8)
            d = c.close

        app3_price = Button(app3_canvas, image = price199, command = download)
        app3_price.place(x=115, y=300)

        def backtoroot():
            app3_window.destroy()

        backbutton = Button(app3_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    def app4_window():
        root.withdraw()
        app4_window = Toplevel()
        app4_window.title('App Store')
        app4_window.minsize(1000, 600)
        app4_window.resizable(width = NO, height = NO)

        app4_line = read_apps_esp[4]
        app4_info = app4_line.split(',')

        app4_canvas = Canvas(app4_window, width = 1000, height = 600, bg = 'white')
        app4_canvas.place(x=0, y=0)

        app4_largeIcon_pic = Label(app4_canvas, image = app4_largeIcon)
        app4_largeIcon_pic.place(x=100, y=70)

        app4_label = Label(app4_canvas, text = app4_info[3], font = 'Helvetica 30')
        app4_label.place(x=95, y=250)

        app4_scr1_pic = Label(app4_canvas, image = app4_scr1)
        app4_scr1_pic.place(x=450, y=30)

        app4_scr2_pic = Label(app4_canvas, image = app4_scr2)
        app4_scr2_pic.place(x=700, y= 30)

        app4_desc = Label(app4_canvas, font = 'Helvetica 24', text = app4_info[4], justify = LEFT)
        app4_desc.place(x=25, y=380)

        app4_desc2 = Label(app4_canvas, font = 'Helvetica 24', text = app4_info[5], justify = LEFT)
        app4_desc2.place(x=25, y=410)
        
        app4_desc3 = Label(app4_canvas, font = 'Helvetica 24', text = app4_info[6], justify = LEFT)
        app4_desc3.place(x=25, y=440)

        app4_desc4 = Label(app4_canvas, font = 'Helvetica 24', text = app4_info[7], justify = LEFT)
        app4_desc4.place(x=25, y=470)

        app4_desc5 = Label(app4_canvas, font = 'Helvetica 24', text = app4_info[8], justify = LEFT)
        app4_desc5.place(x=25, y=500)

        app4_size = Label(app4_canvas, font = 'Helvetica 24', text = 'Tamaño: '+app4_info[10])
        app4_size.place(x=25, y=540)

        #funcion para agregar descarga a info de app
        def download():
            add_download = int(app4_info[11]) + 1
            app4_info[11] = add_download
            new_1 = app1_info[0] + ',' + app1_info[1] + ',' + app1_info[2] + ',' + app1_info[3] + ',' + app1_info[4] + ',' + app1_info[5] + ',' + app1_info[6] + ',' + app1_info[7] + ',' + app1_info[8] + ',' + app1_info[9] + ',' + app1_info[10] + ',' + app1_info[11]
            new_2 = app2_info[0] + ',' + app2_info[1] + ',' + app2_info[2] + ',' + app2_info[3] + ',' + app2_info[4] + ',' + app2_info[5] + ',' + app2_info[6] + ',' + app2_info[7] + ',' + app2_info[8] + ',' + app2_info[9] + ',' + app2_info[10] + ',' + app2_info[11]
            new_3 = app3_info[0] + ',' + app3_info[1] + ',' + app3_info[2] + ',' + app3_info[3] + ',' + app3_info[4] + ',' + app3_info[5] + ',' + app3_info[6] + ',' + app3_info[7] + ',' + app3_info[8] + ',' + app3_info[9] + ',' + app3_info[10] + ',' + app3_info[11]
            new_4 = app4_info[0] + ',' + app4_info[1] + ',' + app4_info[2] + ',' + app4_info[3] + ',' + app4_info[4] + ',' + app4_info[5] + ',' + app4_info[6] + ',' + app4_info[7] + ',' + app4_info[8] + ',' + app4_info[9] + ',' + app4_info[10] + ',' + str(app4_info[11])
            new_5 = app5_info[0] + ',' + app5_info[1] + ',' + app5_info[2] + ',' + app5_info[3] + ',' + app5_info[4] + ',' + app5_info[5] + ',' + app5_info[6] + ',' + app5_info[7] + ',' + app5_info[8] + ',' + app5_info[9] + ',' + app5_info[10] + ',' + app5_info[11]
            new_6 = app6_info[0] + ',' + app6_info[1] + ',' + app6_info[2] + ',' + app6_info[3] + ',' + app6_info[4] + ',' + app6_info[5] + ',' + app6_info[6] + ',' + app6_info[7] + ',' + app6_info[8] + ',' + app6_info[9] + ',' + app6_info[10] + ',' + app6_info[11]
            new_7 = app7_info[0] + ',' + app7_info[1] + ',' + app7_info[2] + ',' + app7_info[3] + ',' + app7_info[4] + ',' + app7_info[5] + ',' + app7_info[6] + ',' + app7_info[7] + ',' + app7_info[8] + ',' + app7_info[9] + ',' + app7_info[10] + ',' + app7_info[11]
            new_8 = app8_info[0] + ',' + app8_info[1] + ',' + app8_info[2] + ',' + app8_info[3] + ',' + app8_info[4] + ',' + app8_info[5] + ',' + app8_info[6] + ',' + app8_info[7] + ',' + app8_info[8] + ',' + app8_info[9] + ',' + app8_info[10] + ',' + app8_info[11]
            a = open('apps_esp.txt', 'w')
            b = a.close
            c = open('apps_esp.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsCR' + '\n')
            write1 = c.write(new_1)
            write2 = c.write(new_2)
            write3 = c.write(new_3)
            write4 = c.write(new_4 + '\n')
            write5 = c.write(new_5)
            write6 = c.write(new_6)
            write7 = c.write(new_7)
            write8 = c.write(new_8)
            d = c.close

        app4_price = Button(app4_canvas, image = price199, command = download)
        app4_price.place(x=115, y=300)
        
        def backtoroot():
            app4_window.destroy()

        backbutton = Button(app4_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    def app5_window():
        root.withdraw()
        app5_window = Toplevel()
        app5_window.title('App Store')
        app5_window.minsize(1000, 600)
        app5_window.resizable(width = NO, height = NO)

        app5_line = read_apps_esp[5]
        app5_info = app5_line.split(',')

        app5_canvas = Canvas(app5_window, width = 1000, height = 600, bg = 'white')
        app5_canvas.place(x=0, y=0)

        app5_largeIcon_pic = Label(app5_canvas, image = app5_largeIcon)
        app5_largeIcon_pic.place(x=100, y=70)

        app5_label = Label(app5_canvas, text = app5_info[3], font = 'Helvetica 30')
        app5_label.place(x=85, y=250)

        app5_scr1_pic = Label(app5_canvas, image = app5_scr1)
        app5_scr1_pic.place(x=450, y=30)

        app5_scr2_pic = Label(app5_canvas, image = app5_scr2)
        app5_scr2_pic.place(x=700, y= 30)

        app5_desc = Label(app5_canvas, font = 'Helvetica 24', text = app5_info[4], justify = LEFT)
        app5_desc.place(x=25, y=380)

        app5_desc2 = Label(app5_canvas, font = 'Helvetica 24', text = app5_info[5], justify = LEFT)
        app5_desc2.place(x=25, y=410)

        app5_desc3 = Label(app5_canvas, font = 'Helvetica 24', text = app5_info[6], justify = LEFT)
        app5_desc3.place(x=25, y=440)

        app5_desc4 = Label(app5_canvas, font = 'Helvetica 24', text = app5_info[7], justify = LEFT)
        app5_desc4.place(x=25, y=470)

        app5_desc5 = Label(app5_canvas, font = 'Helvetica 24', text = app5_info[8], justify = LEFT)
        app5_desc5.place(x=25, y=500)

        app5_size = Label(app5_canvas, font = 'Helvetica 24', text = 'Tamaño: '+app5_info[10])
        app5_size.place(x=25, y=540)

        #funcion para agregar descarga a info de app
        def download():
            add_download = int(app5_info[11]) + 1
            app5_info[11] = add_download
            new_1 = app1_info[0] + ',' + app1_info[1] + ',' + app1_info[2] + ',' + app1_info[3] + ',' + app1_info[4] + ',' + app1_info[5] + ',' + app1_info[6] + ',' + app1_info[7] + ',' + app1_info[8] + ',' + app1_info[9] + ',' + app1_info[10] + ',' + app1_info[11]
            new_2 = app2_info[0] + ',' + app2_info[1] + ',' + app2_info[2] + ',' + app2_info[3] + ',' + app2_info[4] + ',' + app2_info[5] + ',' + app2_info[6] + ',' + app2_info[7] + ',' + app2_info[8] + ',' + app2_info[9] + ',' + app2_info[10] + ',' + app2_info[11]
            new_3 = app3_info[0] + ',' + app3_info[1] + ',' + app3_info[2] + ',' + app3_info[3] + ',' + app3_info[4] + ',' + app3_info[5] + ',' + app3_info[6] + ',' + app3_info[7] + ',' + app3_info[8] + ',' + app3_info[9] + ',' + app3_info[10] + ',' + app3_info[11]
            new_4 = app4_info[0] + ',' + app4_info[1] + ',' + app4_info[2] + ',' + app4_info[3] + ',' + app4_info[4] + ',' + app4_info[5] + ',' + app4_info[6] + ',' + app4_info[7] + ',' + app4_info[8] + ',' + app4_info[9] + ',' + app4_info[10] + ',' + app4_info[11]
            new_5 = app5_info[0] + ',' + app5_info[1] + ',' + app5_info[2] + ',' + app5_info[3] + ',' + app5_info[4] + ',' + app5_info[5] + ',' + app5_info[6] + ',' + app5_info[7] + ',' + app5_info[8] + ',' + app5_info[9] + ',' + app5_info[10] + ',' + str(app5_info[11])
            new_6 = app6_info[0] + ',' + app6_info[1] + ',' + app6_info[2] + ',' + app6_info[3] + ',' + app6_info[4] + ',' + app6_info[5] + ',' + app6_info[6] + ',' + app6_info[7] + ',' + app6_info[8] + ',' + app6_info[9] + ',' + app6_info[10] + ',' + app6_info[11]
            new_7 = app7_info[0] + ',' + app7_info[1] + ',' + app7_info[2] + ',' + app7_info[3] + ',' + app7_info[4] + ',' + app7_info[5] + ',' + app7_info[6] + ',' + app7_info[7] + ',' + app7_info[8] + ',' + app7_info[9] + ',' + app7_info[10] + ',' + app7_info[11]
            new_8 = app8_info[0] + ',' + app8_info[1] + ',' + app8_info[2] + ',' + app8_info[3] + ',' + app8_info[4] + ',' + app8_info[5] + ',' + app8_info[6] + ',' + app8_info[7] + ',' + app8_info[8] + ',' + app8_info[9] + ',' + app8_info[10] + ',' + app8_info[11]
            a = open('apps_esp.txt', 'w')
            b = a.close
            c = open('apps_esp.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsCR' + '\n')
            write1 = c.write(new_1)
            write2 = c.write(new_2)
            write3 = c.write(new_3)
            write4 = c.write(new_4)
            write5 = c.write(new_5 + '\n')
            write6 = c.write(new_6)
            write7 = c.write(new_7)
            write8 = c.write(new_8)
            d = c.close

        app5_price = Button(app5_canvas, image = price0, command = download)
        app5_price.place(x=115, y=300)

        def backtoroot():
            app5_window.destroy()

        backbutton = Button(app5_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    def app6_window():
        root.withdraw()
        app6_window = Toplevel()
        app6_window.title('App Store')
        app6_window.minsize(1000, 600)
        app6_window.resizable(width = NO, height = NO)

        app6_line = read_apps_esp[6]
        app6_info = app6_line.split(',')

        app6_canvas = Canvas(app6_window, width = 1000, height = 600, bg = 'white')
        app6_canvas.place(x=0, y=0)

        app6_largeIcon_pic = Label(app6_canvas, image = app6_largeIcon)
        app6_largeIcon_pic.place(x=100, y=70)

        app6_label = Label(app6_canvas, text = app6_info[3], font = 'Helvetica 30')
        app6_label.place(x=100, y=260)

        app6_scr1_pic = Label(app6_canvas, image = app6_scr1)
        app6_scr1_pic.place(x=450, y=30)

        app6_scr2_pic = Label(app6_canvas, image = app6_scr2)
        app6_scr2_pic.place(x=700, y= 30)

        app6_desc = Label(app6_canvas, font = 'Helvetica 24', text = app6_info[4], justify = LEFT)
        app6_desc.place(x=25, y=380)

        app6_desc2 = Label(app6_canvas, font = 'Helvetica 24', text = app6_info[5], justify = LEFT)
        app6_desc2.place(x=25, y=410)

        app6_desc3 = Label(app6_canvas, font = 'Helvetica 24', text = app6_info[6], justify = LEFT)
        app6_desc3.place(x=25, y=440)

        app6_desc4 = Label(app6_canvas, font = 'Helvetica 24', text = app6_info[7], justify = LEFT)
        app6_desc4.place(x=25, y=470)

        app6_desc5 = Label(app6_canvas, font = 'Helvetica 24', text = app6_info[8], justify = LEFT)
        app6_desc5.place(x=25, y=500)

        app6_size = Label(app6_canvas, font = 'Helvetica 24', text = 'Tamaño: '+app6_info[10])
        app6_size.place(x=25, y=540)

        #funcion para agregar descarga a info de app
        def download():
            add_download = int(app6_info[11]) + 1
            app6_info[11] = add_download
            new_1 = app1_info[0] + ',' + app1_info[1] + ',' + app1_info[2] + ',' + app1_info[3] + ',' + app1_info[4] + ',' + app1_info[5] + ',' + app1_info[6] + ',' + app1_info[7] + ',' + app1_info[8] + ',' + app1_info[9] + ',' + app1_info[10] + ',' + app1_info[11]
            new_2 = app2_info[0] + ',' + app2_info[1] + ',' + app2_info[2] + ',' + app2_info[3] + ',' + app2_info[4] + ',' + app2_info[5] + ',' + app2_info[6] + ',' + app2_info[7] + ',' + app2_info[8] + ',' + app2_info[9] + ',' + app2_info[10] + ',' + app2_info[11]
            new_3 = app3_info[0] + ',' + app3_info[1] + ',' + app3_info[2] + ',' + app3_info[3] + ',' + app3_info[4] + ',' + app3_info[5] + ',' + app3_info[6] + ',' + app3_info[7] + ',' + app3_info[8] + ',' + app3_info[9] + ',' + app3_info[10] + ',' + app3_info[11]
            new_4 = app4_info[0] + ',' + app4_info[1] + ',' + app4_info[2] + ',' + app4_info[3] + ',' + app4_info[4] + ',' + app4_info[5] + ',' + app4_info[6] + ',' + app4_info[7] + ',' + app4_info[8] + ',' + app4_info[9] + ',' + app4_info[10] + ',' + app4_info[11]
            new_5 = app5_info[0] + ',' + app5_info[1] + ',' + app5_info[2] + ',' + app5_info[3] + ',' + app5_info[4] + ',' + app5_info[5] + ',' + app5_info[6] + ',' + app5_info[7] + ',' + app5_info[8] + ',' + app5_info[9] + ',' + app5_info[10] + ',' + app5_info[11]
            new_6 = app6_info[0] + ',' + app6_info[1] + ',' + app6_info[2] + ',' + app6_info[3] + ',' + app6_info[4] + ',' + app6_info[5] + ',' + app6_info[6] + ',' + app6_info[7] + ',' + app6_info[8] + ',' + app6_info[9] + ',' + app6_info[10] + ',' + str(app6_info[11])
            new_7 = app7_info[0] + ',' + app7_info[1] + ',' + app7_info[2] + ',' + app7_info[3] + ',' + app7_info[4] + ',' + app7_info[5] + ',' + app7_info[6] + ',' + app7_info[7] + ',' + app7_info[8] + ',' + app7_info[9] + ',' + app7_info[10] + ',' + app7_info[11]
            new_8 = app8_info[0] + ',' + app8_info[1] + ',' + app8_info[2] + ',' + app8_info[3] + ',' + app8_info[4] + ',' + app8_info[5] + ',' + app8_info[6] + ',' + app8_info[7] + ',' + app8_info[8] + ',' + app8_info[9] + ',' + app8_info[10] + ',' + app8_info[11]
            a = open('apps_esp.txt', 'w')
            b = a.close
            c = open('apps_esp.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsCR' + '\n')
            write1 = c.write(new_1)
            write2 = c.write(new_2)
            write3 = c.write(new_3)
            write4 = c.write(new_4)
            write5 = c.write(new_5)
            write6 = c.write(new_6 + '\n')
            write7 = c.write(new_7)
            write8 = c.write(new_8)
            d = c.close

        app6_price = Button(app6_canvas, image = price0, command = download)
        app6_price.place(x=115, y=300)

        def backtoroot():
            app6_window.destroy()

        backbutton = Button(app6_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    def app7_window():
        root.withdraw()
        app7_window = Toplevel()
        app7_window.title('App Store')
        app7_window.minsize(1000, 600)
        app7_window.resizable(width = NO, height = NO)

        app7_line = read_apps_esp[7]
        app7_info = app7_line.split(',')

        app7_canvas = Canvas(app7_window, width = 1000, height = 600, bg = 'white')
        app7_canvas.place(x=0, y=0)

        app7_largeIcon_pic = Label(app7_canvas, image = app7_largeIcon)
        app7_largeIcon_pic.place(x=100, y=70)

        app7_label = Label(app7_canvas, text = app7_info[3], font = 'Helvetica 30')
        app7_label.place(x=140, y=250)

        app7_scr1_pic = Label(app7_canvas, image = app7_scr1)
        app7_scr1_pic.place(x=450, y=30)

        app7_scr2_pic = Label(app7_canvas, image = app7_scr2)
        app7_scr2_pic.place(x=700, y= 30)

        app7_desc = Label(app7_canvas, font = 'Helvetica 24', text = app7_info[4], justify = LEFT)
        app7_desc.place(x=25, y=380)

        app7_desc2 = Label(app7_canvas, font = 'Helvetica 24', text = app7_info[5], justify = LEFT)
        app7_desc2.place(x=25, y=410)

        app7_desc3 = Label(app7_canvas, font = 'Helvetica 24', text = app7_info[6], justify = LEFT)
        app7_desc3.place(x=25, y=440)

        app7_desc4 = Label(app7_canvas, font = 'Helvetica 24', text = app7_info[7], justify = LEFT)
        app7_desc4.place(x=25, y=470)

        app7_desc5 = Label(app7_canvas, font = 'Helvetica 24', text = app7_info[8], justify = LEFT)
        app7_desc5.place(x=25, y=500)

        app7_size = Label(app7_canvas, font = 'Helvetica 24', text = 'Tamaño: '+app7_info[10])
        app7_size.place(x=25, y=540)

        #funcion para agregar descarga a info de app
        def download():
            add_download = int(app7_info[11]) + 1
            app7_info[11] = add_download
            new_1 = app1_info[0] + ',' + app1_info[1] + ',' + app1_info[2] + ',' + app1_info[3] + ',' + app1_info[4] + ',' + app1_info[5] + ',' + app1_info[6] + ',' + app1_info[7] + ',' + app1_info[8] + ',' + app1_info[9] + ',' + app1_info[10] + ',' + app1_info[11]
            new_2 = app2_info[0] + ',' + app2_info[1] + ',' + app2_info[2] + ',' + app2_info[3] + ',' + app2_info[4] + ',' + app2_info[5] + ',' + app2_info[6] + ',' + app2_info[7] + ',' + app2_info[8] + ',' + app2_info[9] + ',' + app2_info[10] + ',' + app2_info[11]
            new_3 = app3_info[0] + ',' + app3_info[1] + ',' + app3_info[2] + ',' + app3_info[3] + ',' + app3_info[4] + ',' + app3_info[5] + ',' + app3_info[6] + ',' + app3_info[7] + ',' + app3_info[8] + ',' + app3_info[9] + ',' + app3_info[10] + ',' + app3_info[11]
            new_4 = app4_info[0] + ',' + app4_info[1] + ',' + app4_info[2] + ',' + app4_info[3] + ',' + app4_info[4] + ',' + app4_info[5] + ',' + app4_info[6] + ',' + app4_info[7] + ',' + app4_info[8] + ',' + app4_info[9] + ',' + app4_info[10] + ',' + app4_info[11]
            new_5 = app5_info[0] + ',' + app5_info[1] + ',' + app5_info[2] + ',' + app5_info[3] + ',' + app5_info[4] + ',' + app5_info[5] + ',' + app5_info[6] + ',' + app5_info[7] + ',' + app5_info[8] + ',' + app5_info[9] + ',' + app5_info[10] + ',' + app5_info[11]
            new_6 = app6_info[0] + ',' + app6_info[1] + ',' + app6_info[2] + ',' + app6_info[3] + ',' + app6_info[4] + ',' + app6_info[5] + ',' + app6_info[6] + ',' + app6_info[7] + ',' + app6_info[8] + ',' + app6_info[9] + ',' + app6_info[10] + ',' + app6_info[11]
            new_7 = app7_info[0] + ',' + app7_info[1] + ',' + app7_info[2] + ',' + app7_info[3] + ',' + app7_info[4] + ',' + app7_info[5] + ',' + app7_info[6] + ',' + app7_info[7] + ',' + app7_info[8] + ',' + app7_info[9] + ',' + app7_info[10] + ',' + str(app7_info[11])
            new_8 = app8_info[0] + ',' + app8_info[1] + ',' + app8_info[2] + ',' + app8_info[3] + ',' + app8_info[4] + ',' + app8_info[5] + ',' + app8_info[6] + ',' + app8_info[7] + ',' + app8_info[8] + ',' + app8_info[9] + ',' + app8_info[10] + ',' + app8_info[11]
            a = open('apps_esp.txt', 'w')
            b = a.close
            c = open('apps_esp.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsCR' + '\n')
            write1 = c.write(new_1)
            write2 = c.write(new_2)
            write3 = c.write(new_3)
            write4 = c.write(new_4)
            write5 = c.write(new_5)
            write6 = c.write(new_6)
            write7 = c.write(new_7 + '\n')
            write8 = c.write(new_8)
            d = c.close

        app7_price = Button(app7_canvas, image = price0, command = download)
        app7_price.place(x=115, y=300)

        def backtoroot():
            app7_window.destroy()

        backbutton = Button(app7_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    def app8_window():
        root.withdraw()
        app8_window = Toplevel()
        app8_window.title('App Store')
        app8_window.minsize(1000, 600)
        app8_window.resizable(width = NO, height = NO)

        app8_line = read_apps_esp[8]
        app8_info = app8_line.split(',')

        app8_canvas = Canvas(app8_window, width = 1000, height = 600, bg = 'white')
        app8_canvas.place(x=0, y=0)

        app8_largeIcon_pic = Label(app8_canvas, image = app8_largeIcon)
        app8_largeIcon_pic.place(x=100, y=70)

        app8_label = Label(app8_canvas, text = app8_info[3], font = 'Helvetica 30')
        app8_label.place(x=105, y=250)

        app8_scr1_pic = Label(app8_canvas, image = app8_scr1)
        app8_scr1_pic.place(x=450, y=30)

        app8_scr2_pic = Label(app8_canvas, image = app8_scr2)
        app8_scr2_pic.place(x=700, y= 30)
        
        app8_desc = Label(app8_canvas, font = 'Helvetica 24', text = app8_info[4], justify = LEFT)
        app8_desc.place(x=25, y=380)

        app8_desc2 = Label(app8_canvas, font = 'Helvetica 24', text = app8_info[5], justify = LEFT)
        app8_desc2.place(x=25, y=410)

        app8_desc3 = Label(app8_canvas, font = 'Helvetica 24', text = app8_info[6], justify = LEFT)
        app8_desc3.place(x=25, y=440)

        app8_desc4 = Label(app8_canvas, font = 'Helvetica 24', text = app8_info[7], justify = LEFT)
        app8_desc4.place(x=25, y=470)

        app8_desc5 = Label(app8_canvas, font = 'Helvetica 24', text = app8_info[8], justify = LEFT)
        app8_desc5.place(x=25, y=500)

        app8_size = Label(app8_canvas, font = 'Helvetica 24', text = 'Tamaño: '+app8_info[10])
        app8_size.place(x=25, y=540)

        #funcion para agregar descarga a info de app
        def download():
            add_download = int(app8_info[11]) + 1
            app8_info[11] = add_download
            new_1 = app1_info[0] + ',' + app1_info[1] + ',' + app1_info[2] + ',' + app1_info[3] + ',' + app1_info[4] + ',' + app1_info[5] + ',' + app1_info[6] + ',' + app1_info[7] + ',' + app1_info[8] + ',' + app1_info[9] + ',' + app1_info[10] + ',' + app1_info[11]
            new_2 = app2_info[0] + ',' + app2_info[1] + ',' + app2_info[2] + ',' + app2_info[3] + ',' + app2_info[4] + ',' + app2_info[5] + ',' + app2_info[6] + ',' + app2_info[7] + ',' + app2_info[8] + ',' + app2_info[9] + ',' + app2_info[10] + ',' + app2_info[11]
            new_3 = app3_info[0] + ',' + app3_info[1] + ',' + app3_info[2] + ',' + app3_info[3] + ',' + app3_info[4] + ',' + app3_info[5] + ',' + app3_info[6] + ',' + app3_info[7] + ',' + app3_info[8] + ',' + app3_info[9] + ',' + app3_info[10] + ',' + app3_info[11]
            new_4 = app4_info[0] + ',' + app4_info[1] + ',' + app4_info[2] + ',' + app4_info[3] + ',' + app4_info[4] + ',' + app4_info[5] + ',' + app4_info[6] + ',' + app4_info[7] + ',' + app4_info[8] + ',' + app4_info[9] + ',' + app4_info[10] + ',' + app4_info[11]
            new_5 = app5_info[0] + ',' + app5_info[1] + ',' + app5_info[2] + ',' + app5_info[3] + ',' + app5_info[4] + ',' + app5_info[5] + ',' + app5_info[6] + ',' + app5_info[7] + ',' + app5_info[8] + ',' + app5_info[9] + ',' + app5_info[10] + ',' + app5_info[11]
            new_6 = app6_info[0] + ',' + app6_info[1] + ',' + app6_info[2] + ',' + app6_info[3] + ',' + app6_info[4] + ',' + app6_info[5] + ',' + app6_info[6] + ',' + app6_info[7] + ',' + app6_info[8] + ',' + app6_info[9] + ',' + app6_info[10] + ',' + app6_info[11]
            new_7 = app7_info[0] + ',' + app7_info[1] + ',' + app7_info[2] + ',' + app7_info[3] + ',' + app7_info[4] + ',' + app7_info[5] + ',' + app7_info[6] + ',' + app7_info[7] + ',' + app7_info[8] + ',' + app7_info[9] + ',' + app7_info[10] + ',' + app7_info[11]
            new_8 = app8_info[0] + ',' + app8_info[1] + ',' + app8_info[2] + ',' + app8_info[3] + ',' + app8_info[4] + ',' + app8_info[5] + ',' + app8_info[6] + ',' + app8_info[7] + ',' + app8_info[8] + ',' + app8_info[9] + ',' + app8_info[10] + ',' +str(app8_info[11])
            a = open('apps_esp.txt', 'w')
            b = a.close
            c = open('apps_esp.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsCR' + '\n')
            write1 = c.write(new_1)
            write2 = c.write(new_2)
            write3 = c.write(new_3)
            write4 = c.write(new_4)
            write5 = c.write(new_5)
            write6 = c.write(new_6)
            write7 = c.write(new_7)
            write8 = c.write(new_8 + '\n')
            d = c.close

        app8_price = Button(app8_canvas, image = price0, command = download)
        app8_price.place(x=115, y=300)

        def backtoroot():
            app8_window.destroy()

        backbutton = Button(app8_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    ###############################################################################

    def game1_window():
        root.withdraw()
        game1_window = Toplevel()
        game1_window.title('App Store')
        game1_window.minsize(1000, 600)
        game1_window.resizable(width = NO, height = NO)

        game1_line = read_games_esp[1]
        game1_info = game1_line.split(',')

        game1_canvas = Canvas(game1_window, width = 1000, height = 600, bg = 'white')
        game1_canvas.place(x=0, y=0)

        game1_largeIcon_pic = Label(game1_canvas, image = game1_largeIcon)
        game1_largeIcon_pic.place(x=100, y=70)

        game1_label = Label(game1_canvas, text = game1_info[3], font = 'Helvetica 30')
        game1_label.place(x=133, y=250)

        game1_scr1_pic = Label(game1_canvas, image = game1_scr1)
        game1_scr1_pic.place(x=450, y=30)

        game1_scr2_pic = Label(game1_canvas, image = game1_scr2)
        game1_scr2_pic.place(x=730, y= 30)
        
        game1_desc = Label(game1_canvas, font = 'Helvetica 24', text = game1_info[4], justify = LEFT)
        game1_desc.place(x=25, y=380)

        game1_desc2 = Label(game1_canvas, font = 'Helvetica 24', text = game1_info[5], justify = LEFT)
        game1_desc2.place(x=25, y=410)

        game1_desc3 = Label(game1_canvas, font = 'Helvetica 24', text = game1_info[6], justify = LEFT)
        game1_desc3.place(x=25, y=440)

        game1_desc4 = Label(game1_canvas, font = 'Helvetica 24', text = game1_info[7], justify = LEFT)
        game1_desc4.place(x=25, y=470)

        game1_desc5 = Label(game1_canvas, font = 'Helvetica 24', text = game1_info[8], justify = LEFT)
        game1_desc5.place(x=25, y=500)

        game1_size = Label(game1_canvas, font = 'Helvetica 24', text = 'Tamaño: '+game1_info[10])
        game1_size.place(x=25, y=540)

        #funcion para agregar descarga a info de app
        def download():
            add_download = int(game1_info[11]) + 1
            game1_info[11] = add_download
            new_1 = game1_info[0] + ',' + game1_info[1] + ',' + game1_info[2] + ',' + game1_info[3] + ',' + game1_info[4] + ',' + game1_info[5] + ',' + game1_info[6] + ',' + game1_info[7] + ',' + game1_info[8] + ',' + game1_info[9] + ',' + game1_info[10] + ',' + str(game1_info[11])
            new_2 = game2_info[0] + ',' + game2_info[1] + ',' + game2_info[2] + ',' + game2_info[3] + ',' + game2_info[4] + ',' + game2_info[5] + ',' + game2_info[6] + ',' + game2_info[7] + ',' + game2_info[8] + ',' + game2_info[9] + ',' + game2_info[10] + ',' + game2_info[11]
            new_3 = game3_info[0] + ',' + game3_info[1] + ',' + game3_info[2] + ',' + game3_info[3] + ',' + game3_info[4] + ',' + game3_info[5] + ',' + game3_info[6] + ',' + game3_info[7] + ',' + game3_info[8] + ',' + game3_info[9] + ',' + game3_info[10] + ',' + game3_info[11]
            new_4 = game4_info[0] + ',' + game4_info[1] + ',' + game4_info[2] + ',' + game4_info[3] + ',' + game4_info[4] + ',' + game4_info[5] + ',' + game4_info[6] + ',' + game4_info[7] + ',' + game4_info[8] + ',' + game4_info[9] + ',' + game4_info[10] + ',' + game4_info[11]
            new_5 = game5_info[0] + ',' + game5_info[1] + ',' + game5_info[2] + ',' + game5_info[3] + ',' + game5_info[4] + ',' + game5_info[5] + ',' + game5_info[6] + ',' + game5_info[7] + ',' + game5_info[8] + ',' + game5_info[9] + ',' + game5_info[10] + ',' + game5_info[11]
            new_6 = game6_info[0] + ',' + game6_info[1] + ',' + game6_info[2] + ',' + game6_info[3] + ',' + game6_info[4] + ',' + game6_info[5] + ',' + game6_info[6] + ',' + game6_info[7] + ',' + game6_info[8] + ',' + game6_info[9] + ',' + game6_info[10] + ',' + game6_info[11]
            new_7 = game7_info[0] + ',' + game7_info[1] + ',' + game7_info[2] + ',' + game7_info[3] + ',' + game7_info[4] + ',' + game7_info[5] + ',' + game7_info[6] + ',' + game7_info[7] + ',' + game7_info[8] + ',' + game7_info[9] + ',' + game7_info[10] + ',' + game7_info[11]
            new_8 = game8_info[0] + ',' + game8_info[1] + ',' + game8_info[2] + ',' + game8_info[3] + ',' + game8_info[4] + ',' + game8_info[5] + ',' + game8_info[6] + ',' + game8_info[7] + ',' + game8_info[8] + ',' + game8_info[9] + ',' + game8_info[10] + ',' + game8_info[11]
            a = open('games_esp.txt', 'w')
            b = a.close
            c = open('games_esp.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsCR' + '\n')
            write1 = c.write(new_1 + '\n')
            write2 = c.write(new_2)
            write3 = c.write(new_3)
            write4 = c.write(new_4)
            write5 = c.write(new_5)
            write6 = c.write(new_6)
            write7 = c.write(new_7)
            write8 = c.write(new_8)
            d = c.close

        game1_price = Button(game1_canvas, image = price0, command = download)
        game1_price.place(x=115, y=300)

        def backtoroot():
            game1_window.destroy()

        backbutton = Button(game1_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    def game2_window():
        root.withdraw()
        game2_window = Toplevel()
        game2_window.title('App Store')
        game2_window.minsize(1000, 600)
        game2_window.resizable(width = NO, height = NO)

        game2_line = read_games_esp[2]
        game2_info = game2_line.split(',')

        game2_canvas = Canvas(game2_window, width = 1000, height = 600, bg = 'white')
        game2_canvas.place(x=0, y=0)

        game2_largeIcon_pic = Label(game2_canvas, image = game2_largeIcon)
        game2_largeIcon_pic.place(x=100, y=70)

        game2_label = Label(game2_canvas, text = game2_info[3], font = 'Helvetica 30')
        game2_label.place(x=95, y=250)

        game2_scr1_pic = Label(game2_canvas, image = game2_scr1)
        game2_scr1_pic.place(x=450, y=30)

        game2_scr2_pic = Label(game2_canvas, image = game2_scr2)
        game2_scr2_pic.place(x=730, y= 30)

        game2_desc = Label(game2_canvas, font = 'Helvetica 24', text = game2_info[4], justify = LEFT)
        game2_desc.place(x=25, y=380)

        game2_desc2 = Label(game2_canvas, font = 'Helvetica 24', text = game2_info[5], justify = LEFT)
        game2_desc2.place(x=25, y=410)

        game2_desc3 = Label(game2_canvas, font = 'Helvetica 24', text = game2_info[6], justify = LEFT)
        game2_desc3.place(x=25, y=440)

        game2_desc4 = Label(game2_canvas, font = 'Helvetica 24', text = game2_info[7], justify = LEFT)
        game2_desc4.place(x=25, y=470)

        game2_desc5 = Label(game2_canvas, font = 'Helvetica 24', text = game2_info[8], justify = LEFT)
        game2_desc5.place(x=25, y=500)

        game2_size = Label(game2_canvas, font = 'Helvetica 24', text = 'Tamaño: '+game2_info[10])
        game2_size.place(x=25, y=540)

        #funcion para agregar descarga a info de app
        def download():
            add_download = int(game2_info[11]) + 1
            game2_info[11] = add_download
            new_1 = game1_info[0] + ',' + game1_info[1] + ',' + game1_info[2] + ',' + game1_info[3] + ',' + game1_info[4] + ',' + game1_info[5] + ',' + game1_info[6] + ',' + game1_info[7] + ',' + game1_info[8] + ',' + game1_info[9] + ',' + game1_info[10] + ',' + game1_info[11]
            new_2 = game2_info[0] + ',' + game2_info[1] + ',' + game2_info[2] + ',' + game2_info[3] + ',' + game2_info[4] + ',' + game2_info[5] + ',' + game2_info[6] + ',' + game2_info[7] + ',' + game2_info[8] + ',' + game2_info[9] + ',' + game2_info[10] + ',' + str(game2_info[11])
            new_3 = game3_info[0] + ',' + game3_info[1] + ',' + game3_info[2] + ',' + game3_info[3] + ',' + game3_info[4] + ',' + game3_info[5] + ',' + game3_info[6] + ',' + game3_info[7] + ',' + game3_info[8] + ',' + game3_info[9] + ',' + game3_info[10] + ',' + game3_info[11]
            new_4 = game4_info[0] + ',' + game4_info[1] + ',' + game4_info[2] + ',' + game4_info[3] + ',' + game4_info[4] + ',' + game4_info[5] + ',' + game4_info[6] + ',' + game4_info[7] + ',' + game4_info[8] + ',' + game4_info[9] + ',' + game4_info[10] + ',' + game4_info[11]
            new_5 = game5_info[0] + ',' + game5_info[1] + ',' + game5_info[2] + ',' + game5_info[3] + ',' + game5_info[4] + ',' + game5_info[5] + ',' + game5_info[6] + ',' + game5_info[7] + ',' + game5_info[8] + ',' + game5_info[9] + ',' + game5_info[10] + ',' + game5_info[11]
            new_6 = game6_info[0] + ',' + game6_info[1] + ',' + game6_info[2] + ',' + game6_info[3] + ',' + game6_info[4] + ',' + game6_info[5] + ',' + game6_info[6] + ',' + game6_info[7] + ',' + game6_info[8] + ',' + game6_info[9] + ',' + game6_info[10] + ',' + game6_info[11]
            new_7 = game7_info[0] + ',' + game7_info[1] + ',' + game7_info[2] + ',' + game7_info[3] + ',' + game7_info[4] + ',' + game7_info[5] + ',' + game7_info[6] + ',' + game7_info[7] + ',' + game7_info[8] + ',' + game7_info[9] + ',' + game7_info[10] + ',' + game7_info[11]
            new_8 = game8_info[0] + ',' + game8_info[1] + ',' + game8_info[2] + ',' + game8_info[3] + ',' + game8_info[4] + ',' + game8_info[5] + ',' + game8_info[6] + ',' + game8_info[7] + ',' + game8_info[8] + ',' + game8_info[9] + ',' + game8_info[10] + ',' + game8_info[11]
            a = open('games_esp.txt', 'w')
            b = a.close
            c = open('games_esp.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsCR' + '\n')
            write1 = c.write(new_1)
            write2 = c.write(new_2 + '\n')
            write3 = c.write(new_3)
            write4 = c.write(new_4)
            write5 = c.write(new_5)
            write6 = c.write(new_6)
            write7 = c.write(new_7)
            write8 = c.write(new_8)
            d = c.close

        game2_price = Button(game2_canvas, image = price099, command = download)
        game2_price.place(x=115, y=300)
    
        def backtoroot():
            game2_window.destroy()

        backbutton = Button(game2_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    def game3_window():
        root.withdraw()
        game3_window = Toplevel()
        game3_window.title('App Store')
        game3_window.minsize(1000, 600)
        game3_window.resizable(width = NO, height = NO)

        game3_line = read_games_esp[3]
        game3_info = game3_line.split(',')

        game3_canvas = Canvas(game3_window, width = 1000, height = 600, bg = 'white')
        game3_canvas.place(x=0, y=0)

        game3_largeIcon_pic = Label(game3_canvas, image = game3_largeIcon)
        game3_largeIcon_pic.place(x=100, y=70)

        game3_label = Label(game3_canvas, text = game3_info[3], font = 'Helvetica 30')
        game3_label.place(x=135, y=260)

        game3_scr1_pic = Label(game3_canvas, image = game3_scr1)
        game3_scr1_pic.place(x=450, y=30)

        game3_scr2_pic = Label(game3_canvas, image = game3_scr2)
        game3_scr2_pic.place(x=730, y= 30)

        game3_desc = Label(game3_canvas, font = 'Helvetica 24', text = game3_info[4], justify = LEFT)
        game3_desc.place(x=25, y=380)

        game3_desc2 = Label(game3_canvas, font = 'Helvetica 24', text = game3_info[5], justify = LEFT)
        game3_desc2.place(x=25, y=410)

        game3_desc3 = Label(game3_canvas, font = 'Helvetica 24', text = game3_info[6], justify = LEFT)
        game3_desc3.place(x=25, y=440)

        game3_desc4 = Label(game3_canvas, font = 'Helvetica 24', text = game3_info[7], justify = LEFT)
        game3_desc4.place(x=25, y=470)

        game3_desc5 = Label(game3_canvas, font = 'Helvetica 24', text = game3_info[8], justify = LEFT)
        game3_desc5.place(x=25, y=500)

        game3_size = Label(game3_canvas, font = 'Helvetica 24', text = 'Tamaño: '+game3_info[10])
        game3_size.place(x=25, y=540)

        #funcion para agregar descarga a info de app
        def download():
            add_download = int(game3_info[11]) + 1
            game3_info[11] = add_download
            new_1 = game1_info[0] + ',' + game1_info[1] + ',' + game1_info[2] + ',' + game1_info[3] + ',' + game1_info[4] + ',' + game1_info[5] + ',' + game1_info[6] + ',' + game1_info[7] + ',' + game1_info[8] + ',' + game1_info[9] + ',' + game1_info[10] + ',' + game1_info[11]
            new_2 = game2_info[0] + ',' + game2_info[1] + ',' + game2_info[2] + ',' + game2_info[3] + ',' + game2_info[4] + ',' + game2_info[5] + ',' + game2_info[6] + ',' + game2_info[7] + ',' + game2_info[8] + ',' + game2_info[9] + ',' + game2_info[10] + ',' + game2_info[11]
            new_3 = game3_info[0] + ',' + game3_info[1] + ',' + game3_info[2] + ',' + game3_info[3] + ',' + game3_info[4] + ',' + game3_info[5] + ',' + game3_info[6] + ',' + game3_info[7] + ',' + game3_info[8] + ',' + game3_info[9] + ',' + game3_info[10] + ',' + str(game3_info[11])
            new_4 = game4_info[0] + ',' + game4_info[1] + ',' + game4_info[2] + ',' + game4_info[3] + ',' + game4_info[4] + ',' + game4_info[5] + ',' + game4_info[6] + ',' + game4_info[7] + ',' + game4_info[8] + ',' + game4_info[9] + ',' + game4_info[10] + ',' + game4_info[11]
            new_5 = game5_info[0] + ',' + game5_info[1] + ',' + game5_info[2] + ',' + game5_info[3] + ',' + game5_info[4] + ',' + game5_info[5] + ',' + game5_info[6] + ',' + game5_info[7] + ',' + game5_info[8] + ',' + game5_info[9] + ',' + game5_info[10] + ',' + game5_info[11]
            new_6 = game6_info[0] + ',' + game6_info[1] + ',' + game6_info[2] + ',' + game6_info[3] + ',' + game6_info[4] + ',' + game6_info[5] + ',' + game6_info[6] + ',' + game6_info[7] + ',' + game6_info[8] + ',' + game6_info[9] + ',' + game6_info[10] + ',' + game6_info[11]
            new_7 = game7_info[0] + ',' + game7_info[1] + ',' + game7_info[2] + ',' + game7_info[3] + ',' + game7_info[4] + ',' + game7_info[5] + ',' + game7_info[6] + ',' + game7_info[7] + ',' + game7_info[8] + ',' + game7_info[9] + ',' + game7_info[10] + ',' + game7_info[11]
            new_8 = game8_info[0] + ',' + game8_info[1] + ',' + game8_info[2] + ',' + game8_info[3] + ',' + game8_info[4] + ',' + game8_info[5] + ',' + game8_info[6] + ',' + game8_info[7] + ',' + game8_info[8] + ',' + game8_info[9] + ',' + game8_info[10] + ',' + game8_info[11]
            a = open('games_esp.txt', 'w')
            b = a.close
            c = open('games_esp.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsCR' + '\n')
            write1 = c.write(new_1)
            write2 = c.write(new_2)
            write3 = c.write(new_3  + '\n')
            write4 = c.write(new_4)
            write5 = c.write(new_5)
            write6 = c.write(new_6)
            write7 = c.write(new_7)
            write8 = c.write(new_8)
            d = c.close

        game3_price = Button(game3_canvas, image = price699, command = download)
        game3_price.place(x=115, y=300)

        def backtoroot():
            game3_window.destroy()

        backbutton = Button(game3_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    def game4_window():
        root.withdraw()
        game4_window = Toplevel()
        game4_window.title('App Store')
        game4_window.minsize(1000, 600)
        game4_window.resizable(width = NO, height = NO)

        game4_line = read_games_esp[4]
        game4_info = game4_line.split(',')

        game4_canvas = Canvas(game4_window, width = 1000, height = 600, bg = 'white')
        game4_canvas.place(x=0, y=0)

        game4_largeIcon_pic = Label(game4_canvas, image = game4_largeIcon)
        game4_largeIcon_pic.place(x=100, y=70)

        game4_label = Label(game4_canvas, text = game4_info[3], font = 'Helvetica 30')
        game4_label.place(x=85, y=260)

        game4_scr1_pic = Label(game4_canvas, image = game4_scr1)
        game4_scr1_pic.place(x=450, y=30)

        game4_scr2_pic = Label(game4_canvas, image = game4_scr2)
        game4_scr2_pic.place(x=730, y= 30)

        game4_desc = Label(game4_canvas, font = 'Helvetica 24', text = game4_info[4], justify = LEFT)
        game4_desc.place(x=25, y=380)

        game4_desc2 = Label(game4_canvas, font = 'Helvetica 24', text = game4_info[5], justify = LEFT)
        game4_desc2.place(x=25, y=410)

        game4_desc3 = Label(game4_canvas, font = 'Helvetica 24', text = game4_info[6], justify = LEFT)
        game4_desc3.place(x=25, y=440)

        game4_desc4 = Label(game4_canvas, font = 'Helvetica 24', text = game4_info[7], justify = LEFT)
        game4_desc4.place(x=25, y=470)

        game4_desc5 = Label(game4_canvas, font = 'Helvetica 24', text = game4_info[8], justify = LEFT)
        game4_desc5.place(x=25, y=500)

        game4_size = Label(game4_canvas, font = 'Helvetica 24', text = 'Tamaño: '+game4_info[10])
        game4_size.place(x=25, y=540)

        #funcion para agregar descarga a info de app
        def download():
            add_download = int(game4_info[11]) + 1
            game4_info[11] = add_download
            new_1 = game1_info[0] + ',' + game1_info[1] + ',' + game1_info[2] + ',' + game1_info[3] + ',' + game1_info[4] + ',' + game1_info[5] + ',' + game1_info[6] + ',' + game1_info[7] + ',' + game1_info[8] + ',' + game1_info[9] + ',' + game1_info[10] + ',' + game1_info[11]
            new_2 = game2_info[0] + ',' + game2_info[1] + ',' + game2_info[2] + ',' + game2_info[3] + ',' + game2_info[4] + ',' + game2_info[5] + ',' + game2_info[6] + ',' + game2_info[7] + ',' + game2_info[8] + ',' + game2_info[9] + ',' + game2_info[10] + ',' + game2_info[11]
            new_3 = game3_info[0] + ',' + game3_info[1] + ',' + game3_info[2] + ',' + game3_info[3] + ',' + game3_info[4] + ',' + game3_info[5] + ',' + game3_info[6] + ',' + game3_info[7] + ',' + game3_info[8] + ',' + game3_info[9] + ',' + game3_info[10] + ',' + game3_info[11]
            new_4 = game4_info[0] + ',' + game4_info[1] + ',' + game4_info[2] + ',' + game4_info[3] + ',' + game4_info[4] + ',' + game4_info[5] + ',' + game4_info[6] + ',' + game4_info[7] + ',' + game4_info[8] + ',' + game4_info[9] + ',' + game4_info[10] + ',' + str(game4_info[11])
            new_5 = game5_info[0] + ',' + game5_info[1] + ',' + game5_info[2] + ',' + game5_info[3] + ',' + game5_info[4] + ',' + game5_info[5] + ',' + game5_info[6] + ',' + game5_info[7] + ',' + game5_info[8] + ',' + game5_info[9] + ',' + game5_info[10] + ',' + game5_info[11]
            new_6 = game6_info[0] + ',' + game6_info[1] + ',' + game6_info[2] + ',' + game6_info[3] + ',' + game6_info[4] + ',' + game6_info[5] + ',' + game6_info[6] + ',' + game6_info[7] + ',' + game6_info[8] + ',' + game6_info[9] + ',' + game6_info[10] + ',' + game6_info[11]
            new_7 = game7_info[0] + ',' + game7_info[1] + ',' + game7_info[2] + ',' + game7_info[3] + ',' + game7_info[4] + ',' + game7_info[5] + ',' + game7_info[6] + ',' + game7_info[7] + ',' + game7_info[8] + ',' + game7_info[9] + ',' + game7_info[10] + ',' + game7_info[11]
            new_8 = game8_info[0] + ',' + game8_info[1] + ',' + game8_info[2] + ',' + game8_info[3] + ',' + game8_info[4] + ',' + game8_info[5] + ',' + game8_info[6] + ',' + game8_info[7] + ',' + game8_info[8] + ',' + game8_info[9] + ',' + game8_info[10] + ',' + game8_info[11]
            a = open('games_esp.txt', 'w')
            b = a.close
            c = open('games_esp.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsCR' + '\n')
            write1 = c.write(new_1)
            write2 = c.write(new_2)
            write3 = c.write(new_3)
            write4 = c.write(new_4 + '\n')
            write5 = c.write(new_5)
            write6 = c.write(new_6)
            write7 = c.write(new_7)
            write8 = c.write(new_8)
            d = c.close

        game4_price = Button(game4_canvas, image = price099, command = download)
        game4_price.place(x=115, y=300)
    
        def backtoroot():
            game4_window.destroy()

        backbutton = Button(game4_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    def game5_window():
        root.withdraw()
        game5_window = Toplevel()
        game5_window.title('App Store')
        game5_window.minsize(1000, 600)
        game5_window.resizable(width = NO, height = NO)

        game5_line = read_games_esp[5]
        game5_info = game5_line.split(',')

        game5_canvas = Canvas(game5_window, width = 1000, height = 600, bg = 'white')
        game5_canvas.place(x=0, y=0)

        game5_largeIcon_pic = Label(game5_canvas, image = game5_largeIcon)
        game5_largeIcon_pic.place(x=100, y=70)

        game5_label = Label(game5_canvas, text = game5_info[3], font = 'Helvetica 30')
        game5_label.place(x=70, y=260)

        game5_scr1_pic = Label(game5_canvas, image = game5_scr1)
        game5_scr1_pic.place(x=450, y=30)

        game5_scr2_pic = Label(game5_canvas, image = game5_scr2)
        game5_scr2_pic.place(x=730, y= 30)

        game5_desc = Label(game5_canvas, font = 'Helvetica 24', text = game5_info[4], justify = LEFT)
        game5_desc.place(x=25, y=380)

        game5_desc2 = Label(game5_canvas, font = 'Helvetica 24', text = game5_info[5], justify = LEFT)
        game5_desc2.place(x=25, y=410)

        game5_desc3 = Label(game5_canvas, font = 'Helvetica 24', text = game5_info[6], justify = LEFT)
        game5_desc3.place(x=25, y=440)

        game5_desc4 = Label(game5_canvas, font = 'Helvetica 24', text = game5_info[7], justify = LEFT)
        game5_desc4.place(x=25, y=470)

        game5_desc5 = Label(game5_canvas, font = 'Helvetica 24', text = game5_info[8], justify = LEFT)
        game5_desc5.place(x=25, y=500)

        game5_size = Label(game5_canvas, font = 'Helvetica 24', text = 'Tamaño: '+game5_info[10])
        game5_size.place(x=25, y=540)

        #funcion para agregar descarga a info de app
        def download():
            add_download = int(game5_info[11]) + 1
            game5_info[11] = add_download
            new_1 = game1_info[0] + ',' + game1_info[1] + ',' + game1_info[2] + ',' + game1_info[3] + ',' + game1_info[4] + ',' + game1_info[5] + ',' + game1_info[6] + ',' + game1_info[7] + ',' + game1_info[8] + ',' + game1_info[9] + ',' + game1_info[10] + ',' + game1_info[11]
            new_2 = game2_info[0] + ',' + game2_info[1] + ',' + game2_info[2] + ',' + game2_info[3] + ',' + game2_info[4] + ',' + game2_info[5] + ',' + game2_info[6] + ',' + game2_info[7] + ',' + game2_info[8] + ',' + game2_info[9] + ',' + game2_info[10] + ',' + game2_info[11]
            new_3 = game3_info[0] + ',' + game3_info[1] + ',' + game3_info[2] + ',' + game3_info[3] + ',' + game3_info[4] + ',' + game3_info[5] + ',' + game3_info[6] + ',' + game3_info[7] + ',' + game3_info[8] + ',' + game3_info[9] + ',' + game3_info[10] + ',' + game3_info[11]
            new_4 = game4_info[0] + ',' + game4_info[1] + ',' + game4_info[2] + ',' + game4_info[3] + ',' + game4_info[4] + ',' + game4_info[5] + ',' + game4_info[6] + ',' + game4_info[7] + ',' + game4_info[8] + ',' + game4_info[9] + ',' + game4_info[10] + ',' + game4_info[11]
            new_5 = game5_info[0] + ',' + game5_info[1] + ',' + game5_info[2] + ',' + game5_info[3] + ',' + game5_info[4] + ',' + game5_info[5] + ',' + game5_info[6] + ',' + game5_info[7] + ',' + game5_info[8] + ',' + game5_info[9] + ',' + game5_info[10] + ',' + str(game5_info[11])
            new_6 = game6_info[0] + ',' + game6_info[1] + ',' + game6_info[2] + ',' + game6_info[3] + ',' + game6_info[4] + ',' + game6_info[5] + ',' + game6_info[6] + ',' + game6_info[7] + ',' + game6_info[8] + ',' + game6_info[9] + ',' + game6_info[10] + ',' + game6_info[11]
            new_7 = game7_info[0] + ',' + game7_info[1] + ',' + game7_info[2] + ',' + game7_info[3] + ',' + game7_info[4] + ',' + game7_info[5] + ',' + game7_info[6] + ',' + game7_info[7] + ',' + game7_info[8] + ',' + game7_info[9] + ',' + game7_info[10] + ',' + game7_info[11]
            new_8 = game8_info[0] + ',' + game8_info[1] + ',' + game8_info[2] + ',' + game8_info[3] + ',' + game8_info[4] + ',' + game8_info[5] + ',' + game8_info[6] + ',' + game8_info[7] + ',' + game8_info[8] + ',' + game8_info[9] + ',' + game8_info[10] + ',' + game8_info[11]
            a = open('games_esp.txt', 'w')
            b = a.close
            c = open('games_esp.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsCR' + '\n')
            write1 = c.write(new_1)
            write2 = c.write(new_2)
            write3 = c.write(new_3)
            write4 = c.write(new_4)
            write5 = c.write(new_5 + '\n')
            write6 = c.write(new_6)
            write7 = c.write(new_7)
            write8 = c.write(new_8)
            d = c.close

        game5_price = Button(game5_canvas, image = price299, command = download)
        game5_price.place(x=115, y=300)

        def backtoroot():
            game5_window.destroy()

        backbutton = Button(game5_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    def game6_window():
        root.withdraw()
        game6_window = Toplevel()
        game6_window.title('App Store')
        game6_window.minsize(1000, 600)
        game6_window.resizable(width = NO, height = NO)

        game6_line = read_games_esp[6]
        game6_info = game6_line.split(',')

        game6_canvas = Canvas(game6_window, width = 1000, height = 600, bg = 'white')
        game6_canvas.place(x=0, y=0)

        game6_largeIcon_pic = Label(game6_canvas, image = game6_largeIcon)
        game6_largeIcon_pic.place(x=100, y=70)

        game6_label = Label(game6_canvas, text = game6_info[3], font = 'Helvetica 30')
        game6_label.place(x=90, y=260)

        game6_scr1_pic = Label(game6_canvas, image = game6_scr1)
        game6_scr1_pic.place(x=450, y=30)

        game6_scr2_pic = Label(game6_canvas, image = game6_scr2)
        game6_scr2_pic.place(x=730, y= 30)

        game6_desc = Label(game6_canvas, font = 'Helvetica 24', text = game6_info[4], justify = LEFT)
        game6_desc.place(x=25, y=380)

        game6_desc2 = Label(game6_canvas, font = 'Helvetica 24', text = game6_info[5], justify = LEFT)
        game6_desc2.place(x=25, y=410)

        game6_desc3 = Label(game6_canvas, font = 'Helvetica 24', text = game6_info[6], justify = LEFT)
        game6_desc3.place(x=25, y=440)

        game6_desc4 = Label(game6_canvas, font = 'Helvetica 24', text = game6_info[7], justify = LEFT)
        game6_desc4.place(x=25, y=470)

        game6_desc5 = Label(game6_canvas, font = 'Helvetica 24', text = game6_info[8], justify = LEFT)
        game6_desc5.place(x=25, y=500)

        game6_size = Label(game6_canvas, font = 'Helvetica 24', text = 'Tamaño: '+game6_info[10])
        game6_size.place(x=25, y=540)

        #funcion para agregar descarga a info de app
        def download():
            add_download = int(game6_info[11]) + 1
            game6_info[11] = add_download
            new_1 = game1_info[0] + ',' + game1_info[1] + ',' + game1_info[2] + ',' + game1_info[3] + ',' + game1_info[4] + ',' + game1_info[5] + ',' + game1_info[6] + ',' + game1_info[7] + ',' + game1_info[8] + ',' + game1_info[9] + ',' + game1_info[10] + ',' + game1_info[11]
            new_2 = game2_info[0] + ',' + game2_info[1] + ',' + game2_info[2] + ',' + game2_info[3] + ',' + game2_info[4] + ',' + game2_info[5] + ',' + game2_info[6] + ',' + game2_info[7] + ',' + game2_info[8] + ',' + game2_info[9] + ',' + game2_info[10] + ',' + game2_info[11]
            new_3 = game3_info[0] + ',' + game3_info[1] + ',' + game3_info[2] + ',' + game3_info[3] + ',' + game3_info[4] + ',' + game3_info[5] + ',' + game3_info[6] + ',' + game3_info[7] + ',' + game3_info[8] + ',' + game3_info[9] + ',' + game3_info[10] + ',' + game3_info[11]
            new_4 = game4_info[0] + ',' + game4_info[1] + ',' + game4_info[2] + ',' + game4_info[3] + ',' + game4_info[4] + ',' + game4_info[5] + ',' + game4_info[6] + ',' + game4_info[7] + ',' + game4_info[8] + ',' + game4_info[9] + ',' + game4_info[10] + ',' + game4_info[11]
            new_5 = game5_info[0] + ',' + game5_info[1] + ',' + game5_info[2] + ',' + game5_info[3] + ',' + game5_info[4] + ',' + game5_info[5] + ',' + game5_info[6] + ',' + game5_info[7] + ',' + game5_info[8] + ',' + game5_info[9] + ',' + game5_info[10] + ',' + game5_info[11]
            new_6 = game6_info[0] + ',' + game6_info[1] + ',' + game6_info[2] + ',' + game6_info[3] + ',' + game6_info[4] + ',' + game6_info[5] + ',' + game6_info[6] + ',' + game6_info[7] + ',' + game6_info[8] + ',' + game6_info[9] + ',' + game6_info[10] + ',' + str(game6_info[11])
            new_7 = game7_info[0] + ',' + game7_info[1] + ',' + game7_info[2] + ',' + game7_info[3] + ',' + game7_info[4] + ',' + game7_info[5] + ',' + game7_info[6] + ',' + game7_info[7] + ',' + game7_info[8] + ',' + game7_info[9] + ',' + game7_info[10] + ',' + game7_info[11]
            new_8 = game8_info[0] + ',' + game8_info[1] + ',' + game8_info[2] + ',' + game8_info[3] + ',' + game8_info[4] + ',' + game8_info[5] + ',' + game8_info[6] + ',' + game8_info[7] + ',' + game8_info[8] + ',' + game8_info[9] + ',' + game8_info[10] + ',' + game8_info[11]
            a = open('games_esp.txt', 'w')
            b = a.close
            c = open('games_esp.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsCR' + '\n')
            write1 = c.write(new_1)
            write2 = c.write(new_2)
            write3 = c.write(new_3)
            write4 = c.write(new_4)
            write5 = c.write(new_5)
            write6 = c.write(new_6 + '\n')
            write7 = c.write(new_7)
            write8 = c.write(new_8)
            d = c.close

        game6_price = Button(game6_canvas, image = price699, command = download)
        game6_price.place(x=115, y=300)

        def backtoroot():
            game6_window.destroy()

        backbutton = Button(game6_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    def game7_window():
        root.withdraw()
        game7_window = Toplevel()
        game7_window.title('App Store')
        game7_window.minsize(1000, 600)
        game7_window.resizable(width = NO, height = NO)

        game7_line = read_games_esp[7]
        game7_info = game7_line.split(',')

        game7_canvas = Canvas(game7_window, width = 1000, height = 600, bg = 'white')
        game7_canvas.place(x=0, y=0)

        game7_largeIcon_pic = Label(game7_canvas, image = game7_largeIcon)
        game7_largeIcon_pic.place(x=100, y=70)

        game7_label = Label(game7_canvas, text = game7_info[3], font = 'Helvetica 30')
        game7_label.place(x=100, y=260)

        game7_scr1_pic = Label(game7_canvas, image = game7_scr1)
        game7_scr1_pic.place(x=450, y=30)

        game7_scr2_pic = Label(game7_canvas, image = game7_scr2)
        game7_scr2_pic.place(x=730, y= 30)

        game7_desc = Label(game7_canvas, font = 'Helvetica 24', text = game7_info[4], justify = LEFT)
        game7_desc.place(x=25, y=380)

        game7_desc2 = Label(game7_canvas, font = 'Helvetica 24', text = game7_info[5], justify = LEFT)
        game7_desc2.place(x=25, y=410)

        game7_desc3 = Label(game7_canvas, font = 'Helvetica 24', text = game7_info[6], justify = LEFT)
        game7_desc3.place(x=25, y=440)

        game7_desc4 = Label(game7_canvas, font = 'Helvetica 24', text = game7_info[7], justify = LEFT)
        game7_desc4.place(x=25, y=470)

        game7_desc5 = Label(game7_canvas, font = 'Helvetica 24', text = game7_info[8], justify = LEFT)
        game7_desc5.place(x=25, y=500)

        game7_size = Label(game7_canvas, font = 'Helvetica 24', text = 'Tamaño: '+game7_info[10])
        game7_size.place(x=25, y=540)

        #funcion para agregar descarga a info de app
        def download():
            add_download = int(game7_info[11]) + 1
            game7_info[11] = add_download
            new_1 = game1_info[0] + ',' + game1_info[1] + ',' + game1_info[2] + ',' + game1_info[3] + ',' + game1_info[4] + ',' + game1_info[5] + ',' + game1_info[6] + ',' + game1_info[7] + ',' + game1_info[8] + ',' + game1_info[9] + ',' + game1_info[10] + ',' + game1_info[11]
            new_2 = game2_info[0] + ',' + game2_info[1] + ',' + game2_info[2] + ',' + game2_info[3] + ',' + game2_info[4] + ',' + game2_info[5] + ',' + game2_info[6] + ',' + game2_info[7] + ',' + game2_info[8] + ',' + game2_info[9] + ',' + game2_info[10] + ',' + game2_info[11]
            new_3 = game3_info[0] + ',' + game3_info[1] + ',' + game3_info[2] + ',' + game3_info[3] + ',' + game3_info[4] + ',' + game3_info[5] + ',' + game3_info[6] + ',' + game3_info[7] + ',' + game3_info[8] + ',' + game3_info[9] + ',' + game3_info[10] + ',' + game3_info[11]
            new_4 = game4_info[0] + ',' + game4_info[1] + ',' + game4_info[2] + ',' + game4_info[3] + ',' + game4_info[4] + ',' + game4_info[5] + ',' + game4_info[6] + ',' + game4_info[7] + ',' + game4_info[8] + ',' + game4_info[9] + ',' + game4_info[10] + ',' + game4_info[11]
            new_5 = game5_info[0] + ',' + game5_info[1] + ',' + game5_info[2] + ',' + game5_info[3] + ',' + game5_info[4] + ',' + game5_info[5] + ',' + game5_info[6] + ',' + game5_info[7] + ',' + game5_info[8] + ',' + game5_info[9] + ',' + game5_info[10] + ',' + game5_info[11]
            new_6 = game6_info[0] + ',' + game6_info[1] + ',' + game6_info[2] + ',' + game6_info[3] + ',' + game6_info[4] + ',' + game6_info[5] + ',' + game6_info[6] + ',' + game6_info[7] + ',' + game6_info[8] + ',' + game6_info[9] + ',' + game6_info[10] + ',' + game6_info[11]
            new_7 = game7_info[0] + ',' + game7_info[1] + ',' + game7_info[2] + ',' + game7_info[3] + ',' + game7_info[4] + ',' + game7_info[5] + ',' + game7_info[6] + ',' + game7_info[7] + ',' + game7_info[8] + ',' + game7_info[9] + ',' + game7_info[10] + ',' + str(game7_info[11])
            new_8 = game8_info[0] + ',' + game8_info[1] + ',' + game8_info[2] + ',' + game8_info[3] + ',' + game8_info[4] + ',' + game8_info[5] + ',' + game8_info[6] + ',' + game8_info[7] + ',' + game8_info[8] + ',' + game8_info[9] + ',' + game8_info[10] + ',' + game8_info[11]
            a = open('games_esp.txt', 'w')
            b = a.close
            c = open('games_esp.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsCR' + '\n')
            write1 = c.write(new_1)
            write2 = c.write(new_2)
            write3 = c.write(new_3)
            write4 = c.write(new_4)
            write5 = c.write(new_5)
            write6 = c.write(new_6)
            write7 = c.write(new_7 + '\n')
            write8 = c.write(new_8)
            d = c.close

        game7_price = Button(game7_canvas, image = price0, command = download)
        game7_price.place(x=115, y=300)
        
        def backtoroot():
            game7_window.destroy()

        backbutton = Button(game7_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    def game8_window():
        root.withdraw()
        game8_window = Toplevel()
        game8_window.title('App Store')
        game8_window.minsize(1000, 600)
        game8_window.resizable(width = NO, height = NO)

        game8_line = read_games_esp[8]
        game8_info = game8_line.split(',')

        game8_canvas = Canvas(game8_window, width = 1000, height = 600, bg = 'white')
        game8_canvas.place(x=0, y=0)

        game8_largeIcon_pic = Label(game8_canvas, image = game8_largeIcon)
        game8_largeIcon_pic.place(x=100, y=70)

        game8_label = Label(game8_canvas, text = game8_info[3], font = 'Helvetica 30')
        game8_label.place(x=130, y=260)

        game8_scr1_pic = Label(game8_canvas, image = game8_scr1)
        game8_scr1_pic.place(x=450, y=30)

        game8_scr2_pic = Label(game8_canvas, image = game8_scr2)
        game8_scr2_pic.place(x=730, y= 30)

        game8_desc = Label(game8_canvas, font = 'Helvetica 24', text = game8_info[4], justify = LEFT)
        game8_desc.place(x=25, y=380)

        game8_desc2 = Label(game8_canvas, font = 'Helvetica 24', text = game8_info[5], justify = LEFT)
        game8_desc2.place(x=25, y=410)

        game8_desc3 = Label(game8_canvas, font = 'Helvetica 24', text = game8_info[6], justify = LEFT)
        game8_desc3.place(x=25, y=440)

        game8_desc4 = Label(game8_canvas, font = 'Helvetica 24', text = game8_info[7], justify = LEFT)
        game8_desc4.place(x=25, y=470)

        game8_desc5 = Label(game8_canvas, font = 'Helvetica 24', text = game8_info[8], justify = LEFT)
        game8_desc5.place(x=25, y=500)

        game8_size = Label(game8_canvas, font = 'Helvetica 24', text = 'Tamaño: '+game8_info[10])
        game8_size.place(x=25, y=540)

        #funcion para agregar descarga a info de app
        def download():
            add_download = int(game8_info[11]) + 1
            game8_info[11] = add_download
            new_1 = game1_info[0] + ',' + game1_info[1] + ',' + game1_info[2] + ',' + game1_info[3] + ',' + game1_info[4] + ',' + game1_info[5] + ',' + game1_info[6] + ',' + game1_info[7] + ',' + game1_info[8] + ',' + game1_info[9] + ',' + game1_info[10] + ',' + game1_info[11]
            new_2 = game2_info[0] + ',' + game2_info[1] + ',' + game2_info[2] + ',' + game2_info[3] + ',' + game2_info[4] + ',' + game2_info[5] + ',' + game2_info[6] + ',' + game2_info[7] + ',' + game2_info[8] + ',' + game2_info[9] + ',' + game2_info[10] + ',' + game2_info[11]
            new_3 = game3_info[0] + ',' + game3_info[1] + ',' + game3_info[2] + ',' + game3_info[3] + ',' + game3_info[4] + ',' + game3_info[5] + ',' + game3_info[6] + ',' + game3_info[7] + ',' + game3_info[8] + ',' + game3_info[9] + ',' + game3_info[10] + ',' + game3_info[11]
            new_4 = game4_info[0] + ',' + game4_info[1] + ',' + game4_info[2] + ',' + game4_info[3] + ',' + game4_info[4] + ',' + game4_info[5] + ',' + game4_info[6] + ',' + game4_info[7] + ',' + game4_info[8] + ',' + game4_info[9] + ',' + game4_info[10] + ',' + game4_info[11]
            new_5 = game5_info[0] + ',' + game5_info[1] + ',' + game5_info[2] + ',' + game5_info[3] + ',' + game5_info[4] + ',' + game5_info[5] + ',' + game5_info[6] + ',' + game5_info[7] + ',' + game5_info[8] + ',' + game5_info[9] + ',' + game5_info[10] + ',' + game5_info[11]
            new_6 = game6_info[0] + ',' + game6_info[1] + ',' + game6_info[2] + ',' + game6_info[3] + ',' + game6_info[4] + ',' + game6_info[5] + ',' + game6_info[6] + ',' + game6_info[7] + ',' + game6_info[8] + ',' + game6_info[9] + ',' + game6_info[10] + ',' + game6_info[11]
            new_7 = game7_info[0] + ',' + game7_info[1] + ',' + game7_info[2] + ',' + game7_info[3] + ',' + game7_info[4] + ',' + game7_info[5] + ',' + game7_info[6] + ',' + game7_info[7] + ',' + game7_info[8] + ',' + game7_info[9] + ',' + game7_info[10] + ',' + game7_info[11]
            new_8 = game8_info[0] + ',' + game8_info[1] + ',' + game8_info[2] + ',' + game8_info[3] + ',' + game8_info[4] + ',' + game8_info[5] + ',' + game8_info[6] + ',' + game8_info[7] + ',' + game8_info[8] + ',' + game8_info[9] + ',' + game8_info[10] + ',' + str(game8_info[11])
            a = open('games_esp.txt', 'w')
            b = a.close
            c = open('games_esp.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsCR' + '\n')
            write1 = c.write(new_1)
            write2 = c.write(new_2)
            write3 = c.write(new_3)
            write4 = c.write(new_4)
            write5 = c.write(new_5)
            write6 = c.write(new_6)
            write7 = c.write(new_7)
            write8 = c.write(new_8 + '\n')
            d = c.close

        game8_price = Button(game8_canvas, image = price0, command = download)
        game8_price.place(x=115, y=300)
    
        def backtoroot():
            game8_window.destroy()

        backbutton = Button(game8_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    #funcion para asignar tecla 'Enter' a boton de busqueda
    #E: tecla
    #S: activar boton de busqueda
    def return_key(key):
        searchWindow()

    root_esp.bind('<Return>', return_key)

    #labels
    aotd_label = Label(root_esp, text = 'App Destacada', font = 'Helvetica 26')
    aotd_label.place(x=250, y=105)

    cat_label = Label(root_esp, text = 'Categorías', font = 'Helvetica 26')
    cat_label.place(x=760, y=105)

    games_label = Label(root_esp, text = 'Juegos', font = 'Helvetica 26')
    games_label.place(x=720, y=205)

    apps_label = Label(root_esp, text = 'Apps', font = 'Helvetica 26')
    apps_label.place(x=730, y=320)

    #labels de apps
    app2_label = Label(root_esp, text = app2_info[3], font = 'Helvetica 16')
    app2_label.place(x=30, y=530)

    app2_pricelabel = Label(root_esp, text = app2_info[9], font = 'Helvetica 16')
    app2_pricelabel.place(x=70, y=550)

    app3_label = Label(root_esp, text = app3_info[3], font = 'Helvetica 16')
    app3_label.place(x=220, y=530)

    app3_pricelabel = Label(root_esp, text = app3_info[9], font = 'Helvetica 16')
    app3_pricelabel.place(x=275, y=550)

    game1_label = Label(root_esp, text = game1_info[3], font = 'Helvetica 16')
    game1_label.place(x=465, y=530)

    game1_pricelabel = Label(root_esp, text = game1_info[9], font = 'Helvetica 16')
    game1_pricelabel.place(x=475, y=550)

    game2_label = Label(root_esp, text = game2_info[3], font = 'Helvetica 16')
    game2_label.place(x=650, y=530)

    game2_pricelabel = Label(root_esp, text = game2_info[9], font = 'Helvetica 16')
    game2_pricelabel.place(x=675, y=550)

    game3_label = Label(root_esp, text = game3_info[3], font = 'Helvetica 16')
    game3_label.place(x=870, y=530)

    game3_pricelabel = Label(root_esp, text = game3_info[9], font = 'Helvetica 16')
    game3_pricelabel.place(x=875, y=550)

    #botones de apps
    app1_ad_pic = Button(root_esp, image = app1_ad_esp, command = app1_window)
    app1_ad_pic.place(x=0, y=150)

    app2_pic = Button(root_esp, image = app2_icon, command = app2_window)
    app2_pic.place(x=40, y=420)

    app3_pic = Button(root_esp, image = app3_icon, command = app3_window)
    app3_pic.place(x=240, y=420)

    game1_pic = Button(root_esp, image = game1_icon, command = game1_window)
    game1_pic.place(x=440, y=420)

    game2_pic = Button(root_esp, image = game2_icon, command = game2_window)
    game2_pic.place(x=640, y=420)

    game3_pic = Button(root_esp, image = game3_icon, command = game3_window)
    game3_pic.place(x=840, y=420)

    #sistema de busqueda
    search_label = Button(root_esp, image = search_icon, command = searchWindow)
    search_label.place(x=900,y=63)

    search_entry = Entry(root_esp, width = 20)
    search_entry.place(x=720,y=70)

    #categorias
    games_icon_pic = Button(root_esp, image = games_icon, command = games_menu)
    games_icon_pic.place(x=840, y=165)

    apps_icon_pic = Button(root_esp, image = apps_icon, command = apps_menu)
    apps_icon_pic.place(x=840, y=285)

#ventana principal en ingles con acceso de usuario. ventana identica a root_esp() pero en ingles
def root_eng_logged():
    root_eng_logged = Toplevel()
    root_eng_logged.title('App Store')
    root_eng_logged.minsize(1000, 600)
    root_eng_logged.resizable(width = NO, height = NO)

    welcome_label = Label(root_eng_logged, text='Welcome to the AStore', font = 'Helvetica 28')
    welcome_label.place(x=340, y=0)

    change_lang_label = Label(root_eng_logged, text = 'Change region', font = 'Helvetica 16')
    change_lang_label.place(x=780, y=5)

    change_lang_cr = Button(root_eng_logged, image = cr_flag, command = root_esp)
    change_lang_cr.place(x=890, y=0)

    apps = open('apps.txt', 'r+')
    read_apps = apps.readlines()

    app1_line = read_apps[1]
    app1_info = app1_line.split(',')
    app2_line = read_apps[2]
    app2_info = app2_line.split(',')
    app3_line = read_apps[3]
    app3_info = app3_line.split(',')
    app4_line = read_apps[4]
    app4_info = app4_line.split(',')
    app5_line = read_apps[5]
    app5_info = app5_line.split(',')
    app6_line = read_apps[6]
    app6_info = app6_line.split(',')
    app7_line = read_apps[7]
    app7_info = app7_line.split(',')
    app8_line = read_apps[8]
    app8_info = app8_line.split(',')

    games = open('games.txt', 'r+')
    read_games = games.readlines()

    game1_line = read_games[1]
    game1_info = game1_line.split(',')
    game2_line = read_games[2]
    game2_info = game2_line.split(',')
    game3_line = read_games[3]
    game3_info = game3_line.split(',')
    game4_line = read_games[4]
    game4_info = game4_line.split(',')
    game5_line = read_games[5]
    game5_info = game5_line.split(',')
    game6_line = read_games[6]
    game6_info = game6_line.split(',')
    game7_line = read_games[7]
    game7_info = game7_line.split(',')
    game8_line = read_games[8]
    game8_info = game8_line.split(',')

    #############################################################################
    
    #sistema de busqueda con nombre de app o palabra alusiva
    #E: palabra a buscar
    #S: redireccion
    #R: nombre de app o palabra alusiva

    def searchWindow():
        apps = open('apps.txt', 'r+')
        read_apps = apps.readlines()
        
        app1_line = read_apps[1]
        app1_info = app1_line.split(',')
        app2_line = read_apps[2]
        app2_info = app2_line.split(',')
        app3_line = read_apps[3]
        app3_info = app3_line.split(',')
        app4_line = read_apps[4]
        app4_info = app4_line.split(',')
        app5_line = read_apps[5]
        app5_info = app5_line.split(',')
        app6_line = read_apps[6]
        app6_info = app6_line.split(',')
        app7_line = read_apps[7]
        app7_info = app7_line.split(',')
        app8_line = read_apps[8]
        app8_info = app8_line.split(',')
        apps.close()

        games = open('games.txt', 'r+')
        read_games = games.readlines()

        game1_line = read_games[1]
        game1_info = game1_line.split(',')
        game2_line = read_games[2]
        game2_info = game2_line.split(',')
        game3_line = read_games[3]
        game3_info = game3_line.split(',')
        game4_line = read_games[4]
        game4_info = game4_line.split(',')
        game5_line = read_games[5]
        game5_info = game5_line.split(',')
        game6_line = read_games[6]
        game6_info = game6_line.split(',')
        game7_line = read_games[7]
        game7_info = game7_line.split(',')
        game8_line = read_games[8]
        game8_info = game8_line.split(',')
        games.close()
        apps = open('apps.txt', 'r+')
        read_apps = apps.readlines()
        searchText=search_entry.get()

        if searchText.strip() == 'juegos':
            games_menu()
        if searchText.strip() == 'juego':
            games_menu()
        elif searchText.strip() == 'aplicaciones':
            apps_menu()
        elif searchText.strip() == 'aplicacion':
            apps_menu()
        elif searchText.strip() == 'apps':
            apps_menu()
        elif searchText.strip() == 'aps':
            apps_menu()
        elif searchText.strip() == 'games':
            games_menu()
        elif searchText.strip() == 'jugar':
            games_menu()
        elif searchText.strip() == 'play':
            games_menu()
        elif searchText.strip() == 'jeff schmidt python':
            app1_window()
        elif searchText.strip() == 'jeff schmidts python':
            app1_window()
        elif searchText.strip() == 'python':
            app1_window()
        elif searchText.strip() == 'Python':
            app1_window()
        elif searchText.strip() == 'Jeff':
            app1_window()
        elif searchText.strip() == 'jeff':
            app1_window()
        elif searchText.strip() == 'jeff schmidt':
            app1_window()
        elif searchText.strip() == 'schmidt':
            app1_window()
        elif searchText.strip() == 'Schmidt':
            app1_window()
        elif searchText.strip() == 'code':
            app1_window()
        elif searchText.strip() == 'programming':
            app1_window()
        elif searchText.strip() == 'programar':
            app1_window()
        elif searchText.strip() == 'weed smoke pro':
            app2_window()
        elif searchText.strip() == 'weed':
            app2_window()
        elif searchText.strip() == 'smoke':
            app2_window()
        elif searchText.strip() == 'weed smoke':
            app2_window()
        elif searchText.strip() == 'marijuana':
            app2_window()
        elif searchText.strip() == '420':
            app2_window()
        elif searchText.strip() == 'bob marley':
            app2_window()
        elif searchText.strip() == 'math with ed sheeran':
            app3_window()
        elif searchText.strip() == 'ed sheeran':
            app3_window()
        elif searchText.strip() == 'ed':
            app3_window()
        elif searchText.strip() == 'sheeran':
            app3_window()
        elif searchText.strip() == 'math':
            app3_window()
        elif searchText.strip() == 'matematica':
            app3_window()
        elif searchText.strip() == 'mate':
            app3_window()
        elif searchText.strip() == 'you look perfect tonight':
            app3_window()
        elif searchText.strip() == 'taylors swift':
            app4_window()
        elif searchText.strip() == 'taylor swift':
            app4_window()
        elif searchText.strip() == 'swift':
            app4_window()
        elif searchText.strip() == 'taylor':
            app4_window()
        elif searchText.strip() == 'swift code':
            app4_window()
        elif searchText.strip() == 'swift language':
            app4_window()
        elif searchText.strip() == 'swift lenguaje':
            app4_window()
        elif searchText.strip() == 'the pirate bay':
            app5_window()
        elif searchText.strip() == 'free movies':
            app5_window()
        elif searchText.strip() == 'peliculas gratis':
            app5_window()
        elif searchText.strip() == 'pirate':
            app5_window()
        elif searchText.strip() == 'pirate bay':
            app5_window()
        elif searchText.strip() == 'piratear':
            app5_window()
        elif searchText.strip() == 'free tv':
            app5_window()
        elif searchText.strip() == 'torrent':
            app5_window()
        elif searchText.strip() == 'apple music':
            app6_window()
        elif searchText.strip() == 'apple':
            app6_window()
        elif searchText.strip() == 'music':
            app6_window()
        elif searchText.strip() == 'free music':
            app6_window()
        elif searchText.strip() == 'musica gratis':
            app6_window()
        elif searchText.strip() == 'netflix':
            app7_window()
        elif searchText.strip() == 'series':
            app7_window()
        elif searchText.strip() == 'tv shows':
            app7_window()
        elif searchText.strip() == 'movies':
            app7_window()
        elif searchText.strip() == 'peliculas':
            app7_window()
        elif searchText.strip() == 'netflix':
            app7_window()
        elif searchText.strip() == 'im feeling lucky':
            app8_window()
        elif searchText.strip() == 'kiss me pls':
            app8_window()
        elif searchText.strip() == 'kiss me':
            app8_window()
        elif searchText.strip() == 'notlim':
            game1_window()
        elif searchText.strip() == 'Notlim':
            game1_window()
        elif searchText.strip() == 'mining':
            game1_window()
        elif searchText.strip() == 'intro & taller':
            game2_window()
        elif searchText.strip() == 'intro y taller':
            game2_window()
        elif searchText.strip() == 'Intro y Taller':
            game2_window()
        elif searchText.strip() == 'Intro & taller':
            game2_window()
        elif searchText.strip() == 'intro':
            game2_window()
        elif searchText.strip() == 'taller':
            game2_window()
        elif searchText.strip() == 'samus aran':
            game2_window()
        elif searchText.strip() == 'conejos':
            game2_window()
        elif searchText.strip() == 'arnold schwarzenegger':
            game2_window()
        elif searchText.strip() == 'jessie':
            game3_window()
        elif searchText.strip() == 'ingeniera':
            game3_window()
        elif searchText.strip() == 'engineer':
            game3_window()
        elif searchText.strip() == 'game of shots':
            game4_window()
        elif searchText.strip() == 'shots':
            game4_window()
        elif searchText.strip() == 'drinking game':
            game4_window()
        elif searchText.strip() == 'alcohol':
            game4_window()
        elif searchText.strip() == 'tragos':
            game4_window()
        elif searchText.strip() == 'monument valley':
            game5_window()
        elif searchText.strip() == 'arquitectura':
            game5_window()
        elif searchText.strip() == 'architecture':
            game5_window()
        elif searchText.strip() == 'monument':
            game5_window()
        elif searchText.strip() == 'valley':
            game5_window()
        elif searchText.strip() == 'life is strange':
            game6_window()
        elif searchText.strip() == 'life':
            game6_window()
        elif searchText.strip() == 'strange':
            game6_window()
        elif searchText.strip() == 'max caulfield':
            game6_window()
        elif searchText.strip() == 'blackwell':
            game6_window()
        elif searchText.strip() == 'unbreakable':
            game7_window()
        elif searchText.strip() == 'jeff schmidt game':
            game7_window()
        elif searchText.strip() == 'jeff schmidt juego':
            game7_window()
        elif searchText.strip() == 'stocks':
            game8_window()
        elif searchText.strip() == 'bolsa':
            game8_window()
        elif searchText.strip() == 'dinero':
            game8_window()
        elif searchText.strip() == 'money':
            game8_window()
        elif searchText.strip() == 'strategy':
            game8_window()
        elif searchText.strip() == 'estrategia':
            game8_window()
        elif searchText.strip() == app1_info[3].strip():
            app1_window()
        elif searchText.strip() == app2_info[3].strip():
            app2_window()   
        elif searchText.strip() == app3_info[3].strip():
            app3_window()
        elif searchText.strip() == app4_info[3].strip():
            app4_window()
        elif searchText.strip() == app5_info[3].strip():
            app5_window()
        elif searchText.strip() == app6_info[3].strip():
            app6_window()
        elif searchText.strip() == app7_info[3].strip():
            app7_window()
        elif searchText.strip() == app8_info[3].strip():
            app8_window()
        elif searchText.strip() == game1_info[3].strip():
            game1_window()
        elif searchText.strip() == game2_info[3].strip():
            game2_window()
        elif searchText.strip() == game3_info[3].strip():
            game3_window()
        elif searchText.strip() == game4_info[3].strip():
            game4_window()
        elif searchText.strip() == game5_info[3].strip():
            game5_window()
        elif searchText.strip() == game6_info[3].strip():
            game6_window()
        elif searchText.strip() == game7_info[3].strip():
            game7_window()
        elif searchText.strip() == game8_info[3].strip():
            game8_window()
        else:
            messagebox.showwarning("Search results:",searchText+' not found')

    ###############################################################################

    def apps_menu():
        apps_menu = Toplevel()
        apps_menu.title('App Store')
        apps_menu.minsize(1000, 600)
        apps_menu.resizable(width = NO, height = NO)

        appsmenu_canvas = Canvas(apps_menu, width = 1000, height = 600, bg = 'white')
        appsmenu_canvas.place(x=0, y=0)

        app1_line = read_apps[1]
        app1_info = app1_line.split(',')
        app2_line = read_apps[2]
        app2_info = app2_line.split(',')
        app3_line = read_apps[3]
        app3_info = app3_line.split(',')
        app4_line = read_apps[4]
        app4_info = app4_line.split(',')
        app5_line = read_apps[5]
        app5_info = app5_line.split(',')
        app6_line = read_apps[6]
        app6_info = app6_line.split(',')
        app7_line = read_apps[7]
        app7_info = app7_line.split(',')
        app8_line = read_apps[8]
        app8_info = app8_line.split(',')
        
        #
        app1_icon = Button(appsmenu_canvas, image = app1_largeIcon, command = app1_window)
        app1_icon.place(x=60, y=70)

        app1_label = Label(appsmenu_canvas, text = app1_info[3], font = 'Helvetica 24')
        app1_label.place(x=30, y=270)

        app1_price = Label(appsmenu_canvas, text = app1_info[9], font = 'Helvetica 24')
        app1_price.place(x=120, y=300)

        #
        app2_icon = Button(appsmenu_canvas, image = app2_largeIcon, command = app2_window)
        app2_icon.place(x=290, y=70)

        app2_label = Label(appsmenu_canvas, text = app2_info[3], font = 'Helvetica 24')
        app2_label.place(x=280, y=270)

        app2_price = Label(appsmenu_canvas, text = app2_info[9], font = 'Helvetica 24')
        app2_price.place(x=360, y=300)

        #
        app3_icon = Button(appsmenu_canvas, image = app3_largeIcon, command = app3_window)
        app3_icon.place(x=520, y=70)

        app3_label = Label(appsmenu_canvas, text = app3_info[3], font = 'Helvetica 24')
        app3_label.place(x=500, y=270)

        app3_price = Label(appsmenu_canvas, text = app3_info[9], font = 'Helvetica 24')
        app3_price.place(x=580, y=300)

        #
        app4_icon = Button(appsmenu_canvas, image = app4_largeIcon, command = app4_window)
        app4_icon.place(x=750, y=70)

        app4_label = Label(appsmenu_canvas, text = app4_info[3], font = 'Helvetica 24')
        app4_label.place(x=765, y=270)

        app4_price = Label(appsmenu_canvas, text = app4_info[9], font = 'Helvetica 24')
        app4_price.place(x=810, y=300)

        #
        app5_icon = Button(appsmenu_canvas, image = app5_largeIcon, command = app5_window)
        app5_icon.place(x=60, y=350)

        app5_label = Label(appsmenu_canvas, text = app5_info[3], font = 'Helvetica 24')
        app5_label.place(x=65, y=540)

        app5_price = Label(appsmenu_canvas, text = app5_info[9], font = 'Helvetica 24')
        app5_price.place(x=115, y=570)

        #
        app6_icon = Button(appsmenu_canvas, image = app6_largeIcon, command = app6_window)
        app6_icon.place(x=290, y=350)

        app6_label = Label(appsmenu_canvas, text = app6_info[3], font = 'Helvetica 24')
        app6_label.place(x=310, y=540)

        app6_price = Label(appsmenu_canvas, text = app6_info[9], font = 'Helvetica 24')
        app6_price.place(x=345, y=570)

        #
        app7_icon = Button(appsmenu_canvas, image = app7_largeIcon, command = app7_window)
        app7_icon.place(x=520, y=350)

        app7_label = Label(appsmenu_canvas, text = app7_info[3], font = 'Helvetica 24')
        app7_label.place(x=570, y=540)

        app7_price = Label(appsmenu_canvas, text = app7_info[9], font = 'Helvetica 24')
        app7_price.place(x=575, y=570)

        #
        app8_icon = Button(appsmenu_canvas, image = app8_largeIcon, command = app8_window)
        app8_icon.place(x=750, y=350)
        
        app8_label = Label(appsmenu_canvas, text = app8_info[3], font = 'Helvetica 24')
        app8_label.place(x=780, y=540)

        app8_price = Label(appsmenu_canvas, text = app8_info[9], font = 'Helvetica 24')
        app8_price.place(x=810, y=570)

        def backtoroot():
            apps_menu.destroy()

        backbutton = Button(apps_menu, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    def games_menu():
        games_menu = Toplevel()
        games_menu.title('App Store')
        games_menu.minsize(1000, 600)
        games_menu.resizable(width = NO, height = NO)

        gamesmenu_canvas = Canvas(games_menu, width = 1000, height = 600, bg = 'white')
        gamesmenu_canvas.place(x=0, y=0)

        game1_line = read_games[1]
        game1_info = game1_line.split(',')
        game2_line = read_games[2]
        game2_info = game2_line.split(',')
        game3_line = read_games[3]
        game3_info = game3_line.split(',')
        
        #
        game1_icon = Button(gamesmenu_canvas, image = game1_largeIcon, command = game1_window)
        game1_icon.place(x=60, y=70)

        game1_label = Label(gamesmenu_canvas, text = game1_info[3], font = 'Helvetica 24')
        game1_label.place(x=100, y=270)

        game1_price = Label(gamesmenu_canvas, text = game1_info[9], font = 'Helvetica 24')
        game1_price.place(x=120, y=300)

        #
        game2_icon = Button(gamesmenu_canvas, image = game2_largeIcon, command = game2_window)
        game2_icon.place(x=290, y=70)

        game2_label = Label(gamesmenu_canvas, text = game2_info[3], font = 'Helvetica 24')
        game2_label.place(x=315, y=270)

        game2_price = Label(gamesmenu_canvas, text = game2_info[9], font = 'Helvetica 24')
        game2_price.place(x=355, y=300)

        #
        game3_icon = Button(gamesmenu_canvas, image = game3_largeIcon, command = game3_window)
        game3_icon.place(x=520, y=70)

        game3_label = Label(gamesmenu_canvas, text = game3_info[3], font = 'Helvetica 24')
        game3_label.place(x=575, y=270)

        game3_price = Label(gamesmenu_canvas, text = game3_info[9], font = 'Helvetica 24')
        game3_price.place(x=580, y=300)

        #
        game4_icon = Button(gamesmenu_canvas, image = game4_largeIcon, command = game4_window)
        game4_icon.place(x=750, y=70)

        game4_label = Label(gamesmenu_canvas, text = game4_info[3], font = 'Helvetica 24')
        game4_label.place(x=760, y=270)

        game4_price = Label(gamesmenu_canvas, text = game4_info[9], font = 'Helvetica 24')
        game4_price.place(x=805, y=300)

        #
        game5_icon = Button(gamesmenu_canvas, image = game5_largeIcon, command = game5_window)
        game5_icon.place(x=60, y=350)

        game5_label = Label(gamesmenu_canvas, text = game5_info[3], font = 'Helvetica 24')
        game5_label.place(x=55, y=540)

        game5_price = Label(gamesmenu_canvas, text = game5_info[9], font = 'Helvetica 24')
        game5_price.place(x=110, y=570)

        #
        game6_icon = Button(gamesmenu_canvas, image = game6_largeIcon, command = game6_window)
        game6_icon.place(x=290, y=350)

        game6_label = Label(gamesmenu_canvas, text = game6_info[3], font = 'Helvetica 24')
        game6_label.place(x=300, y=540)

        game6_price = Label(gamesmenu_canvas, text = game6_info[9], font = 'Helvetica 24')
        game6_price.place(x=340, y=570)    

        #
        game7_icon = Button(gamesmenu_canvas, image = game7_largeIcon, command = game7_window)
        game7_icon.place(x=520, y=350)

        game7_label = Label(gamesmenu_canvas, text = game7_info[3], font = 'Helvetica 24')
        game7_label.place(x=540, y=540)

        game7_price = Label(gamesmenu_canvas, text = game7_info[9], font = 'Helvetica 24')
        game7_price.place(x=580, y=570)

        #
        game8_icon = Button(gamesmenu_canvas, image = game8_largeIcon, command = game8_window)
        game8_icon.place(x=750, y=350)

        game8_label = Label(gamesmenu_canvas, text = game8_info[3], font = 'Helvetica 24')
        game8_label.place(x=800, y=540)

        game8_price = Label(gamesmenu_canvas, text = game8_info[9], font = 'Helvetica 24')
        game8_price.place(x=820, y=570)

        def backtoroot():
            games_menu.destroy()

        backbutton = Button(games_menu, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    def app1_window():
        app1_window = Toplevel()
        app1_window.title('App Store')
        app1_window.minsize(1000, 600)
        app1_window.resizable(width = NO, height = NO)

        app1_line = read_apps[1]
        app1_info = app1_line.split(',')

        app1_canvas = Canvas(app1_window, width = 1000, height = 600, bg = 'white')
        app1_canvas.place(x=0, y=0)

        app1_largeIcon_pic = Label(app1_canvas, image = app1_largeIcon)
        app1_largeIcon_pic.place(x=100, y=70)

        app1_label = Label(app1_canvas, text = app1_info[3], font = 'Helvetica 30')
        app1_label.place(x=70, y=250)

        app1_scr1_pic = Label(app1_canvas, image = app1_scr1)
        app1_scr1_pic.place(x=450, y=30)

        app1_scr2_pic = Label(app1_canvas, image = app1_scr2)
        app1_scr2_pic.place(x=730, y= 30)

        app1_desc = Label(app1_canvas, font = 'Helvetica 24', text = app1_info[4], justify = LEFT)
        app1_desc.place(x=25, y=380)

        app1_desc2 = Label(app1_canvas, font = 'Helvetica 24', text = app1_info[5], justify = LEFT)
        app1_desc2.place(x=25, y=410)

        app1_desc3 = Label(app1_canvas, font = 'Helvetica 24', text = app1_info[6], justify = LEFT)
        app1_desc3.place(x=25, y=440)

        app1_desc4 = Label(app1_canvas, font = 'Helvetica 24', text = app1_info[7], justify = LEFT)
        app1_desc4.place(x=25, y=470)

        app1_desc5 = Label(app1_canvas, font = 'Helvetica 24', text = app1_info[8], justify = LEFT)
        app1_desc5.place(x=25, y=500)

        app1_size = Label(app1_canvas, font = 'Helvetica 24', text = 'App Size:'+app1_info[10])
        app1_size.place(x=25, y=540)

        def download():
            add_download = int(app1_info[11]) + 1
            app1_info[11] = add_download
            new_1 = app1_info[0] + ',' + app1_info[1] + ',' + app1_info[2] + ',' + app1_info[3] + ',' + app1_info[4] + ',' + app1_info[5] + ',' + app1_info[6] + ',' + app1_info[7] + ',' + app1_info[8] + ',' + app1_info[9] + ',' + app1_info[10] + ',' + str(app1_info[11])
            new_2 = app2_info[0] + ',' + app2_info[1] + ',' + app2_info[2] + ',' + app2_info[3] + ',' + app2_info[4] + ',' + app2_info[5] + ',' + app2_info[6] + ',' + app2_info[7] + ',' + app2_info[8] + ',' + app2_info[9] + ',' + app2_info[10] + ',' + app2_info[11]
            new_3 = app3_info[0] + ',' + app3_info[1] + ',' + app3_info[2] + ',' + app3_info[3] + ',' + app3_info[4] + ',' + app3_info[5] + ',' + app3_info[6] + ',' + app3_info[7] + ',' + app3_info[8] + ',' + app3_info[9] + ',' + app3_info[10] + ',' + app3_info[11]
            new_4 = app4_info[0] + ',' + app4_info[1] + ',' + app4_info[2] + ',' + app4_info[3] + ',' + app4_info[4] + ',' + app4_info[5] + ',' + app4_info[6] + ',' + app4_info[7] + ',' + app4_info[8] + ',' + app4_info[9] + ',' + app4_info[10] + ',' + app4_info[11]
            new_5 = app5_info[0] + ',' + app5_info[1] + ',' + app5_info[2] + ',' + app5_info[3] + ',' + app5_info[4] + ',' + app5_info[5] + ',' + app5_info[6] + ',' + app5_info[7] + ',' + app5_info[8] + ',' + app5_info[9] + ',' + app5_info[10] + ',' + app5_info[11]
            new_6 = app6_info[0] + ',' + app6_info[1] + ',' + app6_info[2] + ',' + app6_info[3] + ',' + app6_info[4] + ',' + app6_info[5] + ',' + app6_info[6] + ',' + app6_info[7] + ',' + app6_info[8] + ',' + app6_info[9] + ',' + app6_info[10] + ',' + app6_info[11]
            new_7 = app7_info[0] + ',' + app7_info[1] + ',' + app7_info[2] + ',' + app7_info[3] + ',' + app7_info[4] + ',' + app7_info[5] + ',' + app7_info[6] + ',' + app7_info[7] + ',' + app7_info[8] + ',' + app7_info[9] + ',' + app7_info[10] + ',' + app7_info[11]
            new_8 = app8_info[0] + ',' + app8_info[1] + ',' + app8_info[2] + ',' + app8_info[3] + ',' + app8_info[4] + ',' + app8_info[5] + ',' + app8_info[6] + ',' + app8_info[7] + ',' + app8_info[8] + ',' + app8_info[9] + ',' + app8_info[10] + ',' + app8_info[11]
            a = open('apps.txt', 'w')
            b = a.close
            c = open('apps.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsUS' + '\n')
            write1 = c.write(new_1 + '\n')
            write2 = c.write(new_2)
            write3 = c.write(new_3)
            write4 = c.write(new_4)
            write5 = c.write(new_5)
            write6 = c.write(new_6)
            write7 = c.write(new_7)
            write8 = c.write(new_8)
            d = c.close

        app1_price = Button(app1_canvas, image = price099, command = download)
        app1_price.place(x=115, y=300)

        def backtoroot():
            app1_window.destroy()

        backbutton = Button(app1_window, image = back_icon, command = backtoroot)
        backbutton.place(x=20, y=20)

    ###############################################################################

    def app2_window():
        app2_window = Toplevel()
        app2_window.title('App Store')
        app2_window.minsize(1000, 600)
        app2_window.resizable(width = NO, height = NO)

        app2_line = read_apps[2]
        app2_info = app2_line.split(',')

        app2_canvas = Canvas(app2_window, width = 1000, height = 600, bg = 'white')
        app2_canvas.place(x=0, y=0)

        app2_largeIcon_pic = Label(app2_canvas, image = app2_largeIcon)
        app2_largeIcon_pic.place(x=100, y=60)

        app2_label = Label(app2_canvas, text = app2_info[3], font = 'Helvetica 30')
        app2_label.place(x=70, y=250)

        app2_scr1_pic = Label(app2_canvas, image = app2_scr1)
        app2_scr1_pic.place(x=450, y=30)

        app2_scr2_pic = Label(app2_canvas, image = app2_scr2)
        app2_scr2_pic.place(x=730, y= 30)

        app2_desc = Label(app2_canvas, font = 'Helvetica 24', text = app2_info[4], justify = LEFT)
        app2_desc.place(x=25, y=380)

        app2_desc2 = Label(app2_canvas, font = 'Helvetica 24', text = app2_info[5], justify = LEFT)
        app2_desc2.place(x=25, y=410)

        app2_desc3 = Label(app2_canvas, font = 'Helvetica 24', text = app2_info[6], justify = LEFT)
        app2_desc3.place(x=25, y=440)

        app2_desc4 = Label(app2_canvas, font = 'Helvetica 24', text = app2_info[7], justify = LEFT)
        app2_desc4.place(x=25, y=470)

        app2_desc5 = Label(app2_canvas, font = 'Helvetica 24', text = app2_info[8], justify = LEFT)
        app2_desc5.place(x=25, y=500)

        app2_size = Label(app2_canvas, font = 'Helvetica 24', text = 'App Size: '+app2_info[10])
        app2_size.place(x=25, y=540)

        def download():
            add_download = int(app2_info[11]) + 1
            app2_info[11] = add_download
            new_1 = app1_info[0] + ',' + app1_info[1] + ',' + app1_info[2] + ',' + app1_info[3] + ',' + app1_info[4] + ',' + app1_info[5] + ',' + app1_info[6] + ',' + app1_info[7] + ',' + app1_info[8] + ',' + app1_info[9] + ',' + app1_info[10] + ',' + app1_info[11]
            new_2 = app2_info[0] + ',' + app2_info[1] + ',' + app2_info[2] + ',' + app2_info[3] + ',' + app2_info[4] + ',' + app2_info[5] + ',' + app2_info[6] + ',' + app2_info[7] + ',' + app2_info[8] + ',' + app2_info[9] + ',' + app2_info[10] + ',' + str(app2_info[11])
            new_3 = app3_info[0] + ',' + app3_info[1] + ',' + app3_info[2] + ',' + app3_info[3] + ',' + app3_info[4] + ',' + app3_info[5] + ',' + app3_info[6] + ',' + app3_info[7] + ',' + app3_info[8] + ',' + app3_info[9] + ',' + app3_info[10] + ',' + app3_info[11]
            new_4 = app4_info[0] + ',' + app4_info[1] + ',' + app4_info[2] + ',' + app4_info[3] + ',' + app4_info[4] + ',' + app4_info[5] + ',' + app4_info[6] + ',' + app4_info[7] + ',' + app4_info[8] + ',' + app4_info[9] + ',' + app4_info[10] + ',' + app4_info[11]
            new_5 = app5_info[0] + ',' + app5_info[1] + ',' + app5_info[2] + ',' + app5_info[3] + ',' + app5_info[4] + ',' + app5_info[5] + ',' + app5_info[6] + ',' + app5_info[7] + ',' + app5_info[8] + ',' + app5_info[9] + ',' + app5_info[10] + ',' + app5_info[11]
            new_6 = app6_info[0] + ',' + app6_info[1] + ',' + app6_info[2] + ',' + app6_info[3] + ',' + app6_info[4] + ',' + app6_info[5] + ',' + app6_info[6] + ',' + app6_info[7] + ',' + app6_info[8] + ',' + app6_info[9] + ',' + app6_info[10] + ',' + app6_info[11]
            new_7 = app7_info[0] + ',' + app7_info[1] + ',' + app7_info[2] + ',' + app7_info[3] + ',' + app7_info[4] + ',' + app7_info[5] + ',' + app7_info[6] + ',' + app7_info[7] + ',' + app7_info[8] + ',' + app7_info[9] + ',' + app7_info[10] + ',' + app7_info[11]
            new_8 = app8_info[0] + ',' + app8_info[1] + ',' + app8_info[2] + ',' + app8_info[3] + ',' + app8_info[4] + ',' + app8_info[5] + ',' + app8_info[6] + ',' + app8_info[7] + ',' + app8_info[8] + ',' + app8_info[9] + ',' + app8_info[10] + ',' + app8_info[11]
            a = open('apps.txt', 'w')
            b = a.close
            c = open('apps.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsUS' + '\n')
            write1 = c.write(new_1)
            write2 = c.write(new_2 + '\n')
            write3 = c.write(new_3)
            write4 = c.write(new_4)
            write5 = c.write(new_5)
            write6 = c.write(new_6)
            write7 = c.write(new_7)
            write8 = c.write(new_8)
            d = c.close
            
        app2_price = Button(app2_canvas, image = price420, command = download)
        app2_price.place(x=115, y=300)
        
        def backtoroot():
            app2_window.destroy()

        backbutton = Button(app2_window, image = back_icon, command = backtoroot)
        backbutton.place(x=20, y=20)


    ###############################################################################

    def app3_window():
        app3_window = Toplevel()
        app3_window.title('App Store')
        app3_window.minsize(1000, 600)
        app3_window.resizable(width = NO, height = NO)

        app3_line = read_apps[3]
        app3_info = app3_line.split(',')

        app3_canvas = Canvas(app3_window, width = 1000, height = 600, bg = 'white')
        app3_canvas.place(x=0, y=0)

        app3_largeIcon_pic = Label(app3_canvas, image = app3_largeIcon)
        app3_largeIcon_pic.place(x=100, y=70)

        app3_label = Label(app3_canvas, text = app3_info[3], font = 'Helvetica 30')
        app3_label.place(x=50, y=250)

        app3_scr1_pic = Label(app3_canvas, image = app3_scr1)
        app3_scr1_pic.place(x=450, y=30)

        app3_scr2_pic = Label(app3_canvas, image = app3_scr2)
        app3_scr2_pic.place(x=700, y= 30)

        app3_desc = Label(app3_canvas, font = 'Helvetica 24', text = app3_info[4], justify = LEFT)
        app3_desc.place(x=25, y=380)

        app3_desc2 = Label(app3_canvas, font = 'Helvetica 24', text = app3_info[5], justify = LEFT)
        app3_desc2.place(x=25, y=410)

        app3_desc3 = Label(app3_canvas, font = 'Helvetica 24', text = app3_info[6], justify = LEFT)
        app3_desc3.place(x=25, y=440)

        app3_desc4 = Label(app3_canvas, font = 'Helvetica 24', text = app3_info[7], justify = LEFT)
        app3_desc4.place(x=25, y=470)

        app3_desc5 = Label(app3_canvas, font = 'Helvetica 24', text = app3_info[8], justify = LEFT)
        app3_desc5.place(x=25, y=500)

        app3_size = Label(app3_canvas, font = 'Helvetica 24', text = 'App Size: '+app3_info[10])
        app3_size.place(x=25, y=540)

        def download():
            add_download = int(app3_info[11]) + 1
            app3_info[11] = add_download
            new_1 = app1_info[0] + ',' + app1_info[1] + ',' + app1_info[2] + ',' + app1_info[3] + ',' + app1_info[4] + ',' + app1_info[5] + ',' + app1_info[6] + ',' + app1_info[7] + ',' + app1_info[8] + ',' + app1_info[9] + ',' + app1_info[10] + ',' + app1_info[11]
            new_2 = app2_info[0] + ',' + app2_info[1] + ',' + app2_info[2] + ',' + app2_info[3] + ',' + app2_info[4] + ',' + app2_info[5] + ',' + app2_info[6] + ',' + app2_info[7] + ',' + app2_info[8] + ',' + app2_info[9] + ',' + app2_info[10] + ',' + app2_info[11]
            new_3 = app3_info[0] + ',' + app3_info[1] + ',' + app3_info[2] + ',' + app3_info[3] + ',' + app3_info[4] + ',' + app3_info[5] + ',' + app3_info[6] + ',' + app3_info[7] + ',' + app3_info[8] + ',' + app3_info[9] + ',' + app3_info[10] + ',' + str(app3_info[11])
            new_4 = app4_info[0] + ',' + app4_info[1] + ',' + app4_info[2] + ',' + app4_info[3] + ',' + app4_info[4] + ',' + app4_info[5] + ',' + app4_info[6] + ',' + app4_info[7] + ',' + app4_info[8] + ',' + app4_info[9] + ',' + app4_info[10] + ',' + app4_info[11]
            new_5 = app5_info[0] + ',' + app5_info[1] + ',' + app5_info[2] + ',' + app5_info[3] + ',' + app5_info[4] + ',' + app5_info[5] + ',' + app5_info[6] + ',' + app5_info[7] + ',' + app5_info[8] + ',' + app5_info[9] + ',' + app5_info[10] + ',' + app5_info[11]
            new_6 = app6_info[0] + ',' + app6_info[1] + ',' + app6_info[2] + ',' + app6_info[3] + ',' + app6_info[4] + ',' + app6_info[5] + ',' + app6_info[6] + ',' + app6_info[7] + ',' + app6_info[8] + ',' + app6_info[9] + ',' + app6_info[10] + ',' + app6_info[11]
            new_7 = app7_info[0] + ',' + app7_info[1] + ',' + app7_info[2] + ',' + app7_info[3] + ',' + app7_info[4] + ',' + app7_info[5] + ',' + app7_info[6] + ',' + app7_info[7] + ',' + app7_info[8] + ',' + app7_info[9] + ',' + app7_info[10] + ',' + app7_info[11]
            new_8 = app8_info[0] + ',' + app8_info[1] + ',' + app8_info[2] + ',' + app8_info[3] + ',' + app8_info[4] + ',' + app8_info[5] + ',' + app8_info[6] + ',' + app8_info[7] + ',' + app8_info[8] + ',' + app8_info[9] + ',' + app8_info[10] + ',' + app8_info[11]
            a = open('apps.txt', 'w')
            b = a.close
            c = open('apps.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsUS' + '\n')
            write1 = c.write(new_1)
            write2 = c.write(new_2)
            write3 = c.write(new_3 + '\n')
            write4 = c.write(new_4)
            write5 = c.write(new_5)
            write6 = c.write(new_6)
            write7 = c.write(new_7)
            write8 = c.write(new_8)
            d = c.close

        app3_price = Button(app3_canvas, image = price199, command = download)
        app3_price.place(x=115, y=300)

        def backtoroot():
            app3_window.destroy()

        backbutton = Button(app3_window, image = back_icon, command = backtoroot)
        backbutton.place(x=20, y=20)

    ###############################################################################

    def app4_window():
        root.withdraw()
        app4_window = Toplevel()
        app4_window.title('App Store')
        app4_window.minsize(1000, 600)
        app4_window.resizable(width = NO, height = NO)

        app4_line = read_apps[4]
        app4_info = app4_line.split(',')

        app4_canvas = Canvas(app4_window, width = 1000, height = 600, bg = 'white')
        app4_canvas.place(x=0, y=0)

        app4_largeIcon_pic = Label(app4_canvas, image = app4_largeIcon)
        app4_largeIcon_pic.place(x=100, y=70)

        app4_label = Label(app4_canvas, text = app4_info[3], font = 'Helvetica 30')
        app4_label.place(x=95, y=250)

        app4_scr1_pic = Label(app4_canvas, image = app4_scr1)
        app4_scr1_pic.place(x=450, y=30)

        app4_scr2_pic = Label(app4_canvas, image = app4_scr2)
        app4_scr2_pic.place(x=700, y= 30)

        app4_desc = Label(app4_canvas, font = 'Helvetica 24', text = app4_info[4], justify = LEFT)
        app4_desc.place(x=25, y=380)

        app4_desc2 = Label(app4_canvas, font = 'Helvetica 24', text = app4_info[5], justify = LEFT)
        app4_desc2.place(x=25, y=410)
        
        app4_desc3 = Label(app4_canvas, font = 'Helvetica 24', text = app4_info[6], justify = LEFT)
        app4_desc3.place(x=25, y=440)

        app4_desc4 = Label(app4_canvas, font = 'Helvetica 24', text = app4_info[7], justify = LEFT)
        app4_desc4.place(x=25, y=470)

        app4_desc5 = Label(app4_canvas, font = 'Helvetica 24', text = app4_info[8], justify = LEFT)
        app4_desc5.place(x=25, y=500)

        app4_size = Label(app4_canvas, font = 'Helvetica 24', text = 'App Size: '+app4_info[10])
        app4_size.place(x=25, y=540)

        def download():
            add_download = int(app4_info[11]) + 1
            app4_info[11] = add_download
            new_1 = app1_info[0] + ',' + app1_info[1] + ',' + app1_info[2] + ',' + app1_info[3] + ',' + app1_info[4] + ',' + app1_info[5] + ',' + app1_info[6] + ',' + app1_info[7] + ',' + app1_info[8] + ',' + app1_info[9] + ',' + app1_info[10] + ',' + app1_info[11]
            new_2 = app2_info[0] + ',' + app2_info[1] + ',' + app2_info[2] + ',' + app2_info[3] + ',' + app2_info[4] + ',' + app2_info[5] + ',' + app2_info[6] + ',' + app2_info[7] + ',' + app2_info[8] + ',' + app2_info[9] + ',' + app2_info[10] + ',' + app2_info[11]
            new_3 = app3_info[0] + ',' + app3_info[1] + ',' + app3_info[2] + ',' + app3_info[3] + ',' + app3_info[4] + ',' + app3_info[5] + ',' + app3_info[6] + ',' + app3_info[7] + ',' + app3_info[8] + ',' + app3_info[9] + ',' + app3_info[10] + ',' + app3_info[11]
            new_4 = app4_info[0] + ',' + app4_info[1] + ',' + app4_info[2] + ',' + app4_info[3] + ',' + app4_info[4] + ',' + app4_info[5] + ',' + app4_info[6] + ',' + app4_info[7] + ',' + app4_info[8] + ',' + app4_info[9] + ',' + app4_info[10] + ',' + str(app4_info[11])
            new_5 = app5_info[0] + ',' + app5_info[1] + ',' + app5_info[2] + ',' + app5_info[3] + ',' + app5_info[4] + ',' + app5_info[5] + ',' + app5_info[6] + ',' + app5_info[7] + ',' + app5_info[8] + ',' + app5_info[9] + ',' + app5_info[10] + ',' + app5_info[11]
            new_6 = app6_info[0] + ',' + app6_info[1] + ',' + app6_info[2] + ',' + app6_info[3] + ',' + app6_info[4] + ',' + app6_info[5] + ',' + app6_info[6] + ',' + app6_info[7] + ',' + app6_info[8] + ',' + app6_info[9] + ',' + app6_info[10] + ',' + app6_info[11]
            new_7 = app7_info[0] + ',' + app7_info[1] + ',' + app7_info[2] + ',' + app7_info[3] + ',' + app7_info[4] + ',' + app7_info[5] + ',' + app7_info[6] + ',' + app7_info[7] + ',' + app7_info[8] + ',' + app7_info[9] + ',' + app7_info[10] + ',' + app7_info[11]
            new_8 = app8_info[0] + ',' + app8_info[1] + ',' + app8_info[2] + ',' + app8_info[3] + ',' + app8_info[4] + ',' + app8_info[5] + ',' + app8_info[6] + ',' + app8_info[7] + ',' + app8_info[8] + ',' + app8_info[9] + ',' + app8_info[10] + ',' + app8_info[11]
            a = open('apps.txt', 'w')
            b = a.close
            c = open('apps.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsUS' + '\n')
            write1 = c.write(new_1)
            write2 = c.write(new_2)
            write3 = c.write(new_3)
            write4 = c.write(new_4 + '\n')
            write5 = c.write(new_5)
            write6 = c.write(new_6)
            write7 = c.write(new_7)
            write8 = c.write(new_8)
            d = c.close

        app4_price = Button(app4_canvas, image = price199, command = download)
        app4_price.place(x=115, y=300)

        def backtoroot():
            app4_window.destroy()

        backbutton = Button(app4_window, image = back_icon, command = backtoroot)
        backbutton.place(x=20, y=20)

    ###############################################################################

    def app5_window():
        root.withdraw()
        app5_window = Toplevel()
        app5_window.title('App Store')
        app5_window.minsize(1000, 600)
        app5_window.resizable(width = NO, height = NO)

        app5_line = read_apps[5]
        app5_info = app5_line.split(',')

        app5_canvas = Canvas(app5_window, width = 1000, height = 600, bg = 'white')
        app5_canvas.place(x=0, y=0)

        app5_largeIcon_pic = Label(app5_canvas, image = app5_largeIcon)
        app5_largeIcon_pic.place(x=100, y=70)

        app5_label = Label(app5_canvas, text = app5_info[3], font = 'Helvetica 30')
        app5_label.place(x=85, y=250)

        app5_scr1_pic = Label(app5_canvas, image = app5_scr1)
        app5_scr1_pic.place(x=450, y=30)

        app5_scr2_pic = Label(app5_canvas, image = app5_scr2)
        app5_scr2_pic.place(x=700, y= 30)

        app5_desc = Label(app5_canvas, font = 'Helvetica 24', text = app5_info[4], justify = LEFT)
        app5_desc.place(x=25, y=380)

        app5_desc2 = Label(app5_canvas, font = 'Helvetica 24', text = app5_info[5], justify = LEFT)
        app5_desc2.place(x=25, y=410)

        app5_desc3 = Label(app5_canvas, font = 'Helvetica 24', text = app5_info[6], justify = LEFT)
        app5_desc3.place(x=25, y=440)

        app5_desc4 = Label(app5_canvas, font = 'Helvetica 24', text = app5_info[7], justify = LEFT)
        app5_desc4.place(x=25, y=470)

        app5_desc5 = Label(app5_canvas, font = 'Helvetica 24', text = app5_info[8], justify = LEFT)
        app5_desc5.place(x=25, y=500)

        app5_size = Label(app5_canvas, font = 'Helvetica 24', text = 'App Size: '+app5_info[10])
        app5_size.place(x=25, y=540)

        def download():
            add_download = int(app5_info[11]) + 1
            app5_info[11] = add_download
            new_1 = app1_info[0] + ',' + app1_info[1] + ',' + app1_info[2] + ',' + app1_info[3] + ',' + app1_info[4] + ',' + app1_info[5] + ',' + app1_info[6] + ',' + app1_info[7] + ',' + app1_info[8] + ',' + app1_info[9] + ',' + app1_info[10] + ',' + app1_info[11]
            new_2 = app2_info[0] + ',' + app2_info[1] + ',' + app2_info[2] + ',' + app2_info[3] + ',' + app2_info[4] + ',' + app2_info[5] + ',' + app2_info[6] + ',' + app2_info[7] + ',' + app2_info[8] + ',' + app2_info[9] + ',' + app2_info[10] + ',' + app2_info[11]
            new_3 = app3_info[0] + ',' + app3_info[1] + ',' + app3_info[2] + ',' + app3_info[3] + ',' + app3_info[4] + ',' + app3_info[5] + ',' + app3_info[6] + ',' + app3_info[7] + ',' + app3_info[8] + ',' + app3_info[9] + ',' + app3_info[10] + ',' + app3_info[11]
            new_4 = app4_info[0] + ',' + app4_info[1] + ',' + app4_info[2] + ',' + app4_info[3] + ',' + app4_info[4] + ',' + app4_info[5] + ',' + app4_info[6] + ',' + app4_info[7] + ',' + app4_info[8] + ',' + app4_info[9] + ',' + app4_info[10] + ',' + app4_info[11]
            new_5 = app5_info[0] + ',' + app5_info[1] + ',' + app5_info[2] + ',' + app5_info[3] + ',' + app5_info[4] + ',' + app5_info[5] + ',' + app5_info[6] + ',' + app5_info[7] + ',' + app5_info[8] + ',' + app5_info[9] + ',' + app5_info[10] + ',' + str(app5_info[11])
            new_6 = app6_info[0] + ',' + app6_info[1] + ',' + app6_info[2] + ',' + app6_info[3] + ',' + app6_info[4] + ',' + app6_info[5] + ',' + app6_info[6] + ',' + app6_info[7] + ',' + app6_info[8] + ',' + app6_info[9] + ',' + app6_info[10] + ',' + app6_info[11]
            new_7 = app7_info[0] + ',' + app7_info[1] + ',' + app7_info[2] + ',' + app7_info[3] + ',' + app7_info[4] + ',' + app7_info[5] + ',' + app7_info[6] + ',' + app7_info[7] + ',' + app7_info[8] + ',' + app7_info[9] + ',' + app7_info[10] + ',' + app7_info[11]
            new_8 = app8_info[0] + ',' + app8_info[1] + ',' + app8_info[2] + ',' + app8_info[3] + ',' + app8_info[4] + ',' + app8_info[5] + ',' + app8_info[6] + ',' + app8_info[7] + ',' + app8_info[8] + ',' + app8_info[9] + ',' + app8_info[10] + ',' + app8_info[11]
            a = open('apps.txt', 'w')
            b = a.close
            c = open('apps.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsUS' + '\n')
            write1 = c.write(new_1)
            write2 = c.write(new_2)
            write3 = c.write(new_3)
            write4 = c.write(new_4)
            write5 = c.write(new_5 + '\n')
            write6 = c.write(new_6)
            write7 = c.write(new_7)
            write8 = c.write(new_8)
            d = c.close

        app5_price = Button(app5_canvas, image = price0, command = download)
        app5_price.place(x=115, y=300)

        def backtoroot():
            app5_window.destroy()

        backbutton = Button(app5_window, image = back_icon, command = backtoroot)
        backbutton.place(x=20, y=20)

    ###############################################################################

    def app6_window():
        root.withdraw()
        app6_window = Toplevel()
        app6_window.title('App Store')
        app6_window.minsize(1000, 600)
        app6_window.resizable(width = NO, height = NO)

        app6_line = read_apps[6]
        app6_info = app6_line.split(',')

        app6_canvas = Canvas(app6_window, width = 1000, height = 600, bg = 'white')
        app6_canvas.place(x=0, y=0)

        app6_largeIcon_pic = Label(app6_canvas, image = app6_largeIcon)
        app6_largeIcon_pic.place(x=100, y=70)

        app6_label = Label(app6_canvas, text = app6_info[3], font = 'Helvetica 30')
        app6_label.place(x=100, y=260)

        app6_scr1_pic = Label(app6_canvas, image = app6_scr1)
        app6_scr1_pic.place(x=450, y=30)

        app6_scr2_pic = Label(app6_canvas, image = app6_scr2)
        app6_scr2_pic.place(x=700, y= 30)

        app6_desc = Label(app6_canvas, font = 'Helvetica 24', text = app6_info[4], justify = LEFT)
        app6_desc.place(x=25, y=380)

        app6_desc2 = Label(app6_canvas, font = 'Helvetica 24', text = app6_info[5], justify = LEFT)
        app6_desc2.place(x=25, y=410)

        app6_desc3 = Label(app6_canvas, font = 'Helvetica 24', text = app6_info[6], justify = LEFT)
        app6_desc3.place(x=25, y=440)

        app6_desc4 = Label(app6_canvas, font = 'Helvetica 24', text = app6_info[7], justify = LEFT)
        app6_desc4.place(x=25, y=470)

        app6_desc5 = Label(app6_canvas, font = 'Helvetica 24', text = app6_info[8], justify = LEFT)
        app6_desc5.place(x=25, y=500)

        app6_size = Label(app6_canvas, font = 'Helvetica 24', text = 'App Size: '+app6_info[10])
        app6_size.place(x=25, y=540)

        def download():
            add_download = int(app6_info[11]) + 1
            app6_info[11] = add_download
            new_1 = app1_info[0] + ',' + app1_info[1] + ',' + app1_info[2] + ',' + app1_info[3] + ',' + app1_info[4] + ',' + app1_info[5] + ',' + app1_info[6] + ',' + app1_info[7] + ',' + app1_info[8] + ',' + app1_info[9] + ',' + app1_info[10] + ',' + app1_info[11]
            new_2 = app2_info[0] + ',' + app2_info[1] + ',' + app2_info[2] + ',' + app2_info[3] + ',' + app2_info[4] + ',' + app2_info[5] + ',' + app2_info[6] + ',' + app2_info[7] + ',' + app2_info[8] + ',' + app2_info[9] + ',' + app2_info[10] + ',' + app2_info[11]
            new_3 = app3_info[0] + ',' + app3_info[1] + ',' + app3_info[2] + ',' + app3_info[3] + ',' + app3_info[4] + ',' + app3_info[5] + ',' + app3_info[6] + ',' + app3_info[7] + ',' + app3_info[8] + ',' + app3_info[9] + ',' + app3_info[10] + ',' + app3_info[11]
            new_4 = app4_info[0] + ',' + app4_info[1] + ',' + app4_info[2] + ',' + app4_info[3] + ',' + app4_info[4] + ',' + app4_info[5] + ',' + app4_info[6] + ',' + app4_info[7] + ',' + app4_info[8] + ',' + app4_info[9] + ',' + app4_info[10] + ',' + app4_info[11]
            new_5 = app5_info[0] + ',' + app5_info[1] + ',' + app5_info[2] + ',' + app5_info[3] + ',' + app5_info[4] + ',' + app5_info[5] + ',' + app5_info[6] + ',' + app5_info[7] + ',' + app5_info[8] + ',' + app5_info[9] + ',' + app5_info[10] + ',' + app5_info[11]
            new_6 = app6_info[0] + ',' + app6_info[1] + ',' + app6_info[2] + ',' + app6_info[3] + ',' + app6_info[4] + ',' + app6_info[5] + ',' + app6_info[6] + ',' + app6_info[7] + ',' + app6_info[8] + ',' + app6_info[9] + ',' + app6_info[10] + ',' + str(app6_info[11])
            new_7 = app7_info[0] + ',' + app7_info[1] + ',' + app7_info[2] + ',' + app7_info[3] + ',' + app7_info[4] + ',' + app7_info[5] + ',' + app7_info[6] + ',' + app7_info[7] + ',' + app7_info[8] + ',' + app7_info[9] + ',' + app7_info[10] + ',' + app7_info[11]
            new_8 = app8_info[0] + ',' + app8_info[1] + ',' + app8_info[2] + ',' + app8_info[3] + ',' + app8_info[4] + ',' + app8_info[5] + ',' + app8_info[6] + ',' + app8_info[7] + ',' + app8_info[8] + ',' + app8_info[9] + ',' + app8_info[10] + ',' + app8_info[11]
            a = open('apps.txt', 'w')
            b = a.close
            c = open('apps.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsUS' + '\n')
            write1 = c.write(new_1)
            write2 = c.write(new_2)
            write3 = c.write(new_3)
            write4 = c.write(new_4)
            write5 = c.write(new_5)
            write6 = c.write(new_6 + '\n')
            write7 = c.write(new_7)
            write8 = c.write(new_8)
            d = c.close

        app6_price = Button(app6_canvas, image = price0, command = download)
        app6_price.place(x=115, y=300)

        def backtoroot():
            app6_window.destroy()

        backbutton = Button(app6_window, image = back_icon, command = backtoroot)
        backbutton.place(x=20, y=20)

    ###############################################################################

    def app7_window():
        root.withdraw()
        app7_window = Toplevel()
        app7_window.title('App Store')
        app7_window.minsize(1000, 600)
        app7_window.resizable(width = NO, height = NO)

        app7_line = read_apps[7]
        app7_info = app7_line.split(',')

        app7_canvas = Canvas(app7_window, width = 1000, height = 600, bg = 'white')
        app7_canvas.place(x=0, y=0)

        app7_largeIcon_pic = Label(app7_canvas, image = app7_largeIcon)
        app7_largeIcon_pic.place(x=100, y=70)

        app7_label = Label(app7_canvas, text = app7_info[3], font = 'Helvetica 30')
        app7_label.place(x=140, y=250)

        app7_scr1_pic = Label(app7_canvas, image = app7_scr1)
        app7_scr1_pic.place(x=450, y=30)

        app7_scr2_pic = Label(app7_canvas, image = app7_scr2)
        app7_scr2_pic.place(x=700, y= 30)

        app7_desc = Label(app7_canvas, font = 'Helvetica 24', text = app7_info[4], justify = LEFT)
        app7_desc.place(x=25, y=380)

        app7_desc2 = Label(app7_canvas, font = 'Helvetica 24', text = app7_info[5], justify = LEFT)
        app7_desc2.place(x=25, y=410)

        app7_desc3 = Label(app7_canvas, font = 'Helvetica 24', text = app7_info[6], justify = LEFT)
        app7_desc3.place(x=25, y=440)

        app7_desc4 = Label(app7_canvas, font = 'Helvetica 24', text = app7_info[7], justify = LEFT)
        app7_desc4.place(x=25, y=470)

        app7_desc5 = Label(app7_canvas, font = 'Helvetica 24', text = app7_info[8], justify = LEFT)
        app7_desc5.place(x=25, y=500)

        app7_size = Label(app7_canvas, font = 'Helvetica 24', text = 'App Size: '+app7_info[10])
        app7_size.place(x=25, y=540)

        def download():
            add_download = int(app7_info[11]) + 1
            app7_info[11] = add_download
            new_1 = app1_info[0] + ',' + app1_info[1] + ',' + app1_info[2] + ',' + app1_info[3] + ',' + app1_info[4] + ',' + app1_info[5] + ',' + app1_info[6] + ',' + app1_info[7] + ',' + app1_info[8] + ',' + app1_info[9] + ',' + app1_info[10] + ',' + app1_info[11]
            new_2 = app2_info[0] + ',' + app2_info[1] + ',' + app2_info[2] + ',' + app2_info[3] + ',' + app2_info[4] + ',' + app2_info[5] + ',' + app2_info[6] + ',' + app2_info[7] + ',' + app2_info[8] + ',' + app2_info[9] + ',' + app2_info[10] + ',' + app2_info[11]
            new_3 = app3_info[0] + ',' + app3_info[1] + ',' + app3_info[2] + ',' + app3_info[3] + ',' + app3_info[4] + ',' + app3_info[5] + ',' + app3_info[6] + ',' + app3_info[7] + ',' + app3_info[8] + ',' + app3_info[9] + ',' + app3_info[10] + ',' + app3_info[11]
            new_4 = app4_info[0] + ',' + app4_info[1] + ',' + app4_info[2] + ',' + app4_info[3] + ',' + app4_info[4] + ',' + app4_info[5] + ',' + app4_info[6] + ',' + app4_info[7] + ',' + app4_info[8] + ',' + app4_info[9] + ',' + app4_info[10] + ',' + app4_info[11]
            new_5 = app5_info[0] + ',' + app5_info[1] + ',' + app5_info[2] + ',' + app5_info[3] + ',' + app5_info[4] + ',' + app5_info[5] + ',' + app5_info[6] + ',' + app5_info[7] + ',' + app5_info[8] + ',' + app5_info[9] + ',' + app5_info[10] + ',' + app5_info[11]
            new_6 = app6_info[0] + ',' + app6_info[1] + ',' + app6_info[2] + ',' + app6_info[3] + ',' + app6_info[4] + ',' + app6_info[5] + ',' + app6_info[6] + ',' + app6_info[7] + ',' + app6_info[8] + ',' + app6_info[9] + ',' + app6_info[10] + ',' + app6_info[11]
            new_7 = app7_info[0] + ',' + app7_info[1] + ',' + app7_info[2] + ',' + app7_info[3] + ',' + app7_info[4] + ',' + app7_info[5] + ',' + app7_info[6] + ',' + app7_info[7] + ',' + app7_info[8] + ',' + app7_info[9] + ',' + app7_info[10] + ',' + str(app7_info[11])
            new_8 = app8_info[0] + ',' + app8_info[1] + ',' + app8_info[2] + ',' + app8_info[3] + ',' + app8_info[4] + ',' + app8_info[5] + ',' + app8_info[6] + ',' + app8_info[7] + ',' + app8_info[8] + ',' + app8_info[9] + ',' + app8_info[10] + ',' + app8_info[11]
            a = open('apps.txt', 'w')
            b = a.close
            c = open('apps.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsUS' + '\n')
            write1 = c.write(new_1)
            write2 = c.write(new_2)
            write3 = c.write(new_3)
            write4 = c.write(new_4)
            write5 = c.write(new_5)
            write6 = c.write(new_6)
            write7 = c.write(new_7 + '\n')
            write8 = c.write(new_8)
            d = c.close

        app7_price = Button(app7_canvas, image = price0, command = download)
        app7_price.place(x=115, y=300)

        def backtoroot():
            app7_window.destroy()

        backbutton = Button(app7_window, image = back_icon, command = backtoroot)
        backbutton.place(x=20, y=20)

    ###############################################################################

    def app8_window():
        root.withdraw()
        app8_window = Toplevel()
        app8_window.title('App Store')
        app8_window.minsize(1000, 600)
        app8_window.resizable(width = NO, height = NO)

        app8_line = read_apps[8]
        app8_info = app8_line.split(',')

        app8_canvas = Canvas(app8_window, width = 1000, height = 600, bg = 'white')
        app8_canvas.place(x=0, y=0)

        app8_largeIcon_pic = Label(app8_canvas, image = app8_largeIcon)
        app8_largeIcon_pic.place(x=100, y=70)

        app8_label = Label(app8_canvas, text = app8_info[3], font = 'Helvetica 30')
        app8_label.place(x=105, y=250)

        app8_scr1_pic = Label(app8_canvas, image = app8_scr1)
        app8_scr1_pic.place(x=450, y=30)

        app8_scr2_pic = Label(app8_canvas, image = app8_scr2)
        app8_scr2_pic.place(x=700, y= 30)
        
        app8_desc = Label(app8_canvas, font = 'Helvetica 24', text = app8_info[4], justify = LEFT)
        app8_desc.place(x=25, y=380)

        app8_desc2 = Label(app8_canvas, font = 'Helvetica 24', text = app8_info[5], justify = LEFT)
        app8_desc2.place(x=25, y=410)

        app8_desc3 = Label(app8_canvas, font = 'Helvetica 24', text = app8_info[6], justify = LEFT)
        app8_desc3.place(x=25, y=440)

        app8_desc4 = Label(app8_canvas, font = 'Helvetica 24', text = app8_info[7], justify = LEFT)
        app8_desc4.place(x=25, y=470)

        app8_desc5 = Label(app8_canvas, font = 'Helvetica 24', text = app8_info[8], justify = LEFT)
        app8_desc5.place(x=25, y=500)

        app8_size = Label(app8_canvas, font = 'Helvetica 24', text = 'App Size: '+app8_info[10])
        app8_size.place(x=25, y=540)

        def download():
            add_download = int(app8_info[11]) + 1
            app8_info[11] = add_download
            new_1 = app1_info[0] + ',' + app1_info[1] + ',' + app1_info[2] + ',' + app1_info[3] + ',' + app1_info[4] + ',' + app1_info[5] + ',' + app1_info[6] + ',' + app1_info[7] + ',' + app1_info[8] + ',' + app1_info[9] + ',' + app1_info[10] + ',' + app1_info[11]
            new_2 = app2_info[0] + ',' + app2_info[1] + ',' + app2_info[2] + ',' + app2_info[3] + ',' + app2_info[4] + ',' + app2_info[5] + ',' + app2_info[6] + ',' + app2_info[7] + ',' + app2_info[8] + ',' + app2_info[9] + ',' + app2_info[10] + ',' + app2_info[11]
            new_3 = app3_info[0] + ',' + app3_info[1] + ',' + app3_info[2] + ',' + app3_info[3] + ',' + app3_info[4] + ',' + app3_info[5] + ',' + app3_info[6] + ',' + app3_info[7] + ',' + app3_info[8] + ',' + app3_info[9] + ',' + app3_info[10] + ',' + app3_info[11]
            new_4 = app4_info[0] + ',' + app4_info[1] + ',' + app4_info[2] + ',' + app4_info[3] + ',' + app4_info[4] + ',' + app4_info[5] + ',' + app4_info[6] + ',' + app4_info[7] + ',' + app4_info[8] + ',' + app4_info[9] + ',' + app4_info[10] + ',' + app4_info[11]
            new_5 = app5_info[0] + ',' + app5_info[1] + ',' + app5_info[2] + ',' + app5_info[3] + ',' + app5_info[4] + ',' + app5_info[5] + ',' + app5_info[6] + ',' + app5_info[7] + ',' + app5_info[8] + ',' + app5_info[9] + ',' + app5_info[10] + ',' + app5_info[11]
            new_6 = app6_info[0] + ',' + app6_info[1] + ',' + app6_info[2] + ',' + app6_info[3] + ',' + app6_info[4] + ',' + app6_info[5] + ',' + app6_info[6] + ',' + app6_info[7] + ',' + app6_info[8] + ',' + app6_info[9] + ',' + app6_info[10] + ',' + app6_info[11]
            new_7 = app7_info[0] + ',' + app7_info[1] + ',' + app7_info[2] + ',' + app7_info[3] + ',' + app7_info[4] + ',' + app7_info[5] + ',' + app7_info[6] + ',' + app7_info[7] + ',' + app7_info[8] + ',' + app7_info[9] + ',' + app7_info[10] + ',' + app7_info[11]
            new_8 = app8_info[0] + ',' + app8_info[1] + ',' + app8_info[2] + ',' + app8_info[3] + ',' + app8_info[4] + ',' + app8_info[5] + ',' + app8_info[6] + ',' + app8_info[7] + ',' + app8_info[8] + ',' + app8_info[9] + ',' + app8_info[10] + ',' +str(app8_info[11])
            a = open('apps.txt', 'w')
            b = a.close
            c = open('apps.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsUS' + '\n')
            write1 = c.write(new_1)
            write2 = c.write(new_2)
            write3 = c.write(new_3)
            write4 = c.write(new_4)
            write5 = c.write(new_5)
            write6 = c.write(new_6)
            write7 = c.write(new_7)
            write8 = c.write(new_8 + '\n')
            d = c.close

        app8_price = Button(app8_canvas, image = price0, command = download)
        app8_price.place(x=115, y=300)

        def backtoroot():
            app8_window.destroy()

        backbutton = Button(app8_window, image = back_icon, command = backtoroot)
        backbutton.place(x=20, y=20)

    ###############################################################################

    ###############################################################################

    def game1_window():
        game1_window = Toplevel()
        game1_window.title('App Store')
        game1_window.minsize(1000, 600)
        game1_window.resizable(width = NO, height = NO)

        game1_line = read_games[1]
        game1_info = game1_line.split(',')

        game1_canvas = Canvas(game1_window, width = 1000, height = 600, bg = 'white')
        game1_canvas.place(x=0, y=0)

        game1_largeIcon_pic = Label(game1_canvas, image = game1_largeIcon)
        game1_largeIcon_pic.place(x=100, y=70)

        game1_label = Label(game1_canvas, text = game1_info[3], font = 'Helvetica 30')
        game1_label.place(x=133, y=250)

        game1_scr1_pic = Label(game1_canvas, image = game1_scr1)
        game1_scr1_pic.place(x=450, y=30)

        game1_scr2_pic = Label(game1_canvas, image = game1_scr2)
        game1_scr2_pic.place(x=730, y= 30)
        
        game1_desc = Label(game1_canvas, font = 'Helvetica 24', text = game1_info[4], justify = LEFT)
        game1_desc.place(x=25, y=380)

        game1_desc2 = Label(game1_canvas, font = 'Helvetica 24', text = game1_info[5], justify = LEFT)
        game1_desc2.place(x=25, y=410)

        game1_desc3 = Label(game1_canvas, font = 'Helvetica 24', text = game1_info[6], justify = LEFT)
        game1_desc3.place(x=25, y=440)

        game1_desc4 = Label(game1_canvas, font = 'Helvetica 24', text = game1_info[7], justify = LEFT)
        game1_desc4.place(x=25, y=470)

        game1_desc5 = Label(game1_canvas, font = 'Helvetica 24', text = game1_info[8], justify = LEFT)
        game1_desc5.place(x=25, y=500)

        game1_size = Label(game1_canvas, font = 'Helvetica 24', text = 'App Size: '+game1_info[10])
        game1_size.place(x=25, y=540)

        def download():
            add_download = int(game1_info[11]) + 1
            game1_info[11] = add_download
            new_1 = game1_info[0] + ',' + game1_info[1] + ',' + game1_info[2] + ',' + game1_info[3] + ',' + game1_info[4] + ',' + game1_info[5] + ',' + game1_info[6] + ',' + game1_info[7] + ',' + game1_info[8] + ',' + game1_info[9] + ',' + game1_info[10] + ',' + str(game1_info[11])
            new_2 = game2_info[0] + ',' + game2_info[1] + ',' + game2_info[2] + ',' + game2_info[3] + ',' + game2_info[4] + ',' + game2_info[5] + ',' + game2_info[6] + ',' + game2_info[7] + ',' + game2_info[8] + ',' + game2_info[9] + ',' + game2_info[10] + ',' + game2_info[11]
            new_3 = game3_info[0] + ',' + game3_info[1] + ',' + game3_info[2] + ',' + game3_info[3] + ',' + game3_info[4] + ',' + game3_info[5] + ',' + game3_info[6] + ',' + game3_info[7] + ',' + game3_info[8] + ',' + game3_info[9] + ',' + game3_info[10] + ',' + game3_info[11]
            new_4 = game4_info[0] + ',' + game4_info[1] + ',' + game4_info[2] + ',' + game4_info[3] + ',' + game4_info[4] + ',' + game4_info[5] + ',' + game4_info[6] + ',' + game4_info[7] + ',' + game4_info[8] + ',' + game4_info[9] + ',' + game4_info[10] + ',' + game4_info[11]
            new_5 = game5_info[0] + ',' + game5_info[1] + ',' + game5_info[2] + ',' + game5_info[3] + ',' + game5_info[4] + ',' + game5_info[5] + ',' + game5_info[6] + ',' + game5_info[7] + ',' + game5_info[8] + ',' + game5_info[9] + ',' + game5_info[10] + ',' + game5_info[11]
            new_6 = game6_info[0] + ',' + game6_info[1] + ',' + game6_info[2] + ',' + game6_info[3] + ',' + game6_info[4] + ',' + game6_info[5] + ',' + game6_info[6] + ',' + game6_info[7] + ',' + game6_info[8] + ',' + game6_info[9] + ',' + game6_info[10] + ',' + game6_info[11]
            new_7 = game7_info[0] + ',' + game7_info[1] + ',' + game7_info[2] + ',' + game7_info[3] + ',' + game7_info[4] + ',' + game7_info[5] + ',' + game7_info[6] + ',' + game7_info[7] + ',' + game7_info[8] + ',' + game7_info[9] + ',' + game7_info[10] + ',' + game7_info[11]
            new_8 = game8_info[0] + ',' + game8_info[1] + ',' + game8_info[2] + ',' + game8_info[3] + ',' + game8_info[4] + ',' + game8_info[5] + ',' + game8_info[6] + ',' + game8_info[7] + ',' + game8_info[8] + ',' + game8_info[9] + ',' + game8_info[10] + ',' + game8_info[11]
            a = open('games.txt', 'w')
            b = a.close
            c = open('games.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsUS' + '\n')
            write1 = c.write(new_1 + '\n')
            write2 = c.write(new_2)
            write3 = c.write(new_3)
            write4 = c.write(new_4)
            write5 = c.write(new_5)
            write6 = c.write(new_6)
            write7 = c.write(new_7)
            write8 = c.write(new_8)
            d = c.close

        game1_price = Button(game1_canvas, image = price0, command = download)
        game1_price.place(x=115, y=300)

        def backtoroot():
            game1_window.destroy()

        backbutton = Button(game1_window, image = back_icon, command = backtoroot)
        backbutton.place(x=20, y=20)

    ###############################################################################

    def game2_window():
        game2_window = Toplevel()
        game2_window.title('App Store')
        game2_window.minsize(1000, 600)
        game2_window.resizable(width = NO, height = NO)

        game2_line = read_games[2]
        game2_info = game2_line.split(',')

        game2_canvas = Canvas(game2_window, width = 1000, height = 600, bg = 'white')
        game2_canvas.place(x=0, y=0)

        game2_largeIcon_pic = Label(game2_canvas, image = game2_largeIcon)
        game2_largeIcon_pic.place(x=100, y=70)

        game2_label = Label(game2_canvas, text = game2_info[3], font = 'Helvetica 30')
        game2_label.place(x=95, y=250)

        game2_scr1_pic = Label(game2_canvas, image = game2_scr1)
        game2_scr1_pic.place(x=450, y=30)

        game2_scr2_pic = Label(game2_canvas, image = game2_scr2)
        game2_scr2_pic.place(x=730, y= 30)

        game2_desc = Label(game2_canvas, font = 'Helvetica 24', text = game2_info[4], justify = LEFT)
        game2_desc.place(x=25, y=380)

        game2_desc2 = Label(game2_canvas, font = 'Helvetica 24', text = game2_info[5], justify = LEFT)
        game2_desc2.place(x=25, y=410)

        game2_desc3 = Label(game2_canvas, font = 'Helvetica 24', text = game2_info[6], justify = LEFT)
        game2_desc3.place(x=25, y=440)

        game2_desc4 = Label(game2_canvas, font = 'Helvetica 24', text = game2_info[7], justify = LEFT)
        game2_desc4.place(x=25, y=470)

        game2_desc5 = Label(game2_canvas, font = 'Helvetica 24', text = game2_info[8], justify = LEFT)
        game2_desc5.place(x=25, y=500)

        game2_size = Label(game2_canvas, font = 'Helvetica 24', text = 'App Size: '+game2_info[10])
        game2_size.place(x=25, y=540)

        def download():
            add_download = int(game2_info[11]) + 1
            game2_info[11] = add_download
            new_1 = game1_info[0] + ',' + game1_info[1] + ',' + game1_info[2] + ',' + game1_info[3] + ',' + game1_info[4] + ',' + game1_info[5] + ',' + game1_info[6] + ',' + game1_info[7] + ',' + game1_info[8] + ',' + game1_info[9] + ',' + game1_info[10] + ',' + game1_info[11]
            new_2 = game2_info[0] + ',' + game2_info[1] + ',' + game2_info[2] + ',' + game2_info[3] + ',' + game2_info[4] + ',' + game2_info[5] + ',' + game2_info[6] + ',' + game2_info[7] + ',' + game2_info[8] + ',' + game2_info[9] + ',' + game2_info[10] + ',' + str(game2_info[11])
            new_3 = game3_info[0] + ',' + game3_info[1] + ',' + game3_info[2] + ',' + game3_info[3] + ',' + game3_info[4] + ',' + game3_info[5] + ',' + game3_info[6] + ',' + game3_info[7] + ',' + game3_info[8] + ',' + game3_info[9] + ',' + game3_info[10] + ',' + game3_info[11]
            new_4 = game4_info[0] + ',' + game4_info[1] + ',' + game4_info[2] + ',' + game4_info[3] + ',' + game4_info[4] + ',' + game4_info[5] + ',' + game4_info[6] + ',' + game4_info[7] + ',' + game4_info[8] + ',' + game4_info[9] + ',' + game4_info[10] + ',' + game4_info[11]
            new_5 = game5_info[0] + ',' + game5_info[1] + ',' + game5_info[2] + ',' + game5_info[3] + ',' + game5_info[4] + ',' + game5_info[5] + ',' + game5_info[6] + ',' + game5_info[7] + ',' + game5_info[8] + ',' + game5_info[9] + ',' + game5_info[10] + ',' + game5_info[11]
            new_6 = game6_info[0] + ',' + game6_info[1] + ',' + game6_info[2] + ',' + game6_info[3] + ',' + game6_info[4] + ',' + game6_info[5] + ',' + game6_info[6] + ',' + game6_info[7] + ',' + game6_info[8] + ',' + game6_info[9] + ',' + game6_info[10] + ',' + game6_info[11]
            new_7 = game7_info[0] + ',' + game7_info[1] + ',' + game7_info[2] + ',' + game7_info[3] + ',' + game7_info[4] + ',' + game7_info[5] + ',' + game7_info[6] + ',' + game7_info[7] + ',' + game7_info[8] + ',' + game7_info[9] + ',' + game7_info[10] + ',' + game7_info[11]
            new_8 = game8_info[0] + ',' + game8_info[1] + ',' + game8_info[2] + ',' + game8_info[3] + ',' + game8_info[4] + ',' + game8_info[5] + ',' + game8_info[6] + ',' + game8_info[7] + ',' + game8_info[8] + ',' + game8_info[9] + ',' + game8_info[10] + ',' + game8_info[11]
            a = open('games.txt', 'w')
            b = a.close
            c = open('games.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsUS' + '\n')
            write1 = c.write(new_1)
            write2 = c.write(new_2 + '\n')
            write3 = c.write(new_3)
            write4 = c.write(new_4)
            write5 = c.write(new_5)
            write6 = c.write(new_6)
            write7 = c.write(new_7)
            write8 = c.write(new_8)
            d = c.close

        game2_price = Button(game2_canvas, image = price099, command = download)
        game2_price.place(x=115, y=300)

        def backtoroot():
            game2_window.destroy()

        backbutton = Button(game2_window, image = back_icon, command = backtoroot)
        backbutton.place(x=20, y=20)

    ###############################################################################

    def game3_window():
        game3_window = Toplevel()
        game3_window.title('App Store')
        game3_window.minsize(1000, 600)
        game3_window.resizable(width = NO, height = NO)

        game3_line = read_games[3]
        game3_info = game3_line.split(',')

        game3_canvas = Canvas(game3_window, width = 1000, height = 600, bg = 'white')
        game3_canvas.place(x=0, y=0)

        game3_largeIcon_pic = Label(game3_canvas, image = game3_largeIcon)
        game3_largeIcon_pic.place(x=100, y=70)

        game3_label = Label(game3_canvas, text = game3_info[3], font = 'Helvetica 30')
        game3_label.place(x=135, y=260)

        game3_scr1_pic = Label(game3_canvas, image = game3_scr1)
        game3_scr1_pic.place(x=450, y=30)

        game3_scr2_pic = Label(game3_canvas, image = game3_scr2)
        game3_scr2_pic.place(x=730, y= 30)

        game3_desc = Label(game3_canvas, font = 'Helvetica 24', text = game3_info[4], justify = LEFT)
        game3_desc.place(x=25, y=380)

        game3_desc2 = Label(game3_canvas, font = 'Helvetica 24', text = game3_info[5], justify = LEFT)
        game3_desc2.place(x=25, y=410)

        game3_desc3 = Label(game3_canvas, font = 'Helvetica 24', text = game3_info[6], justify = LEFT)
        game3_desc3.place(x=25, y=440)

        game3_desc4 = Label(game3_canvas, font = 'Helvetica 24', text = game3_info[7], justify = LEFT)
        game3_desc4.place(x=25, y=470)

        game3_desc5 = Label(game3_canvas, font = 'Helvetica 24', text = game3_info[8], justify = LEFT)
        game3_desc5.place(x=25, y=500)

        game3_size = Label(game3_canvas, font = 'Helvetica 24', text = 'App Size: '+game3_info[10])
        game3_size.place(x=25, y=540)

        def download():
            add_download = int(game3_info[11]) + 1
            game3_info[11] = add_download
            new_1 = game1_info[0] + ',' + game1_info[1] + ',' + game1_info[2] + ',' + game1_info[3] + ',' + game1_info[4] + ',' + game1_info[5] + ',' + game1_info[6] + ',' + game1_info[7] + ',' + game1_info[8] + ',' + game1_info[9] + ',' + game1_info[10] + ',' + game1_info[11]
            new_2 = game2_info[0] + ',' + game2_info[1] + ',' + game2_info[2] + ',' + game2_info[3] + ',' + game2_info[4] + ',' + game2_info[5] + ',' + game2_info[6] + ',' + game2_info[7] + ',' + game2_info[8] + ',' + game2_info[9] + ',' + game2_info[10] + ',' + game2_info[11]
            new_3 = game3_info[0] + ',' + game3_info[1] + ',' + game3_info[2] + ',' + game3_info[3] + ',' + game3_info[4] + ',' + game3_info[5] + ',' + game3_info[6] + ',' + game3_info[7] + ',' + game3_info[8] + ',' + game3_info[9] + ',' + game3_info[10] + ',' + str(game3_info[11])
            new_4 = game4_info[0] + ',' + game4_info[1] + ',' + game4_info[2] + ',' + game4_info[3] + ',' + game4_info[4] + ',' + game4_info[5] + ',' + game4_info[6] + ',' + game4_info[7] + ',' + game4_info[8] + ',' + game4_info[9] + ',' + game4_info[10] + ',' + game4_info[11]
            new_5 = game5_info[0] + ',' + game5_info[1] + ',' + game5_info[2] + ',' + game5_info[3] + ',' + game5_info[4] + ',' + game5_info[5] + ',' + game5_info[6] + ',' + game5_info[7] + ',' + game5_info[8] + ',' + game5_info[9] + ',' + game5_info[10] + ',' + game5_info[11]
            new_6 = game6_info[0] + ',' + game6_info[1] + ',' + game6_info[2] + ',' + game6_info[3] + ',' + game6_info[4] + ',' + game6_info[5] + ',' + game6_info[6] + ',' + game6_info[7] + ',' + game6_info[8] + ',' + game6_info[9] + ',' + game6_info[10] + ',' + game6_info[11]
            new_7 = game7_info[0] + ',' + game7_info[1] + ',' + game7_info[2] + ',' + game7_info[3] + ',' + game7_info[4] + ',' + game7_info[5] + ',' + game7_info[6] + ',' + game7_info[7] + ',' + game7_info[8] + ',' + game7_info[9] + ',' + game7_info[10] + ',' + game7_info[11]
            new_8 = game8_info[0] + ',' + game8_info[1] + ',' + game8_info[2] + ',' + game8_info[3] + ',' + game8_info[4] + ',' + game8_info[5] + ',' + game8_info[6] + ',' + game8_info[7] + ',' + game8_info[8] + ',' + game8_info[9] + ',' + game8_info[10] + ',' + game8_info[11]
            a = open('games.txt', 'w')
            b = a.close
            c = open('games.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsUS' + '\n')
            write1 = c.write(new_1)
            write2 = c.write(new_2)
            write3 = c.write(new_3  + '\n')
            write4 = c.write(new_4)
            write5 = c.write(new_5)
            write6 = c.write(new_6)
            write7 = c.write(new_7)
            write8 = c.write(new_8)
            d = c.close

        game3_price = Button(game3_canvas, image = price699, command = download)
        game3_price.place(x=115, y=300)

        def backtoroot():
            game3_window.destroy()
            
        backbutton = Button(game3_window, image = back_icon, command = backtoroot)
        backbutton.place(x=20, y=20)

    ###############################################################################

    def game4_window():
        root.withdraw()
        game4_window = Toplevel()
        game4_window.title('App Store')
        game4_window.minsize(1000, 600)
        game4_window.resizable(width = NO, height = NO)

        game4_line = read_games[4]
        game4_info = game4_line.split(',')

        game4_canvas = Canvas(game4_window, width = 1000, height = 600, bg = 'white')
        game4_canvas.place(x=0, y=0)

        game4_largeIcon_pic = Label(game4_canvas, image = game4_largeIcon)
        game4_largeIcon_pic.place(x=100, y=70)

        game4_label = Label(game4_canvas, text = game4_info[3], font = 'Helvetica 30')
        game4_label.place(x=85, y=260)

        game4_scr1_pic = Label(game4_canvas, image = game4_scr1)
        game4_scr1_pic.place(x=450, y=30)

        game4_scr2_pic = Label(game4_canvas, image = game4_scr2)
        game4_scr2_pic.place(x=730, y= 30)

        game4_desc = Label(game4_canvas, font = 'Helvetica 24', text = game4_info[4], justify = LEFT)
        game4_desc.place(x=25, y=380)

        game4_desc2 = Label(game4_canvas, font = 'Helvetica 24', text = game4_info[5], justify = LEFT)
        game4_desc2.place(x=25, y=410)

        game4_desc3 = Label(game4_canvas, font = 'Helvetica 24', text = game4_info[6], justify = LEFT)
        game4_desc3.place(x=25, y=440)

        game4_desc4 = Label(game4_canvas, font = 'Helvetica 24', text = game4_info[7], justify = LEFT)
        game4_desc4.place(x=25, y=470)

        game4_desc5 = Label(game4_canvas, font = 'Helvetica 24', text = game4_info[8], justify = LEFT)
        game4_desc5.place(x=25, y=500)

        game4_size = Label(game4_canvas, font = 'Helvetica 24', text = 'App Size: '+game4_info[10])
        game4_size.place(x=25, y=540)

        def download():
            add_download = int(game4_info[11]) + 1
            game4_info[11] = add_download
            new_1 = game1_info[0] + ',' + game1_info[1] + ',' + game1_info[2] + ',' + game1_info[3] + ',' + game1_info[4] + ',' + game1_info[5] + ',' + game1_info[6] + ',' + game1_info[7] + ',' + game1_info[8] + ',' + game1_info[9] + ',' + game1_info[10] + ',' + game1_info[11]
            new_2 = game2_info[0] + ',' + game2_info[1] + ',' + game2_info[2] + ',' + game2_info[3] + ',' + game2_info[4] + ',' + game2_info[5] + ',' + game2_info[6] + ',' + game2_info[7] + ',' + game2_info[8] + ',' + game2_info[9] + ',' + game2_info[10] + ',' + game2_info[11]
            new_3 = game3_info[0] + ',' + game3_info[1] + ',' + game3_info[2] + ',' + game3_info[3] + ',' + game3_info[4] + ',' + game3_info[5] + ',' + game3_info[6] + ',' + game3_info[7] + ',' + game3_info[8] + ',' + game3_info[9] + ',' + game3_info[10] + ',' + game3_info[11]
            new_4 = game4_info[0] + ',' + game4_info[1] + ',' + game4_info[2] + ',' + game4_info[3] + ',' + game4_info[4] + ',' + game4_info[5] + ',' + game4_info[6] + ',' + game4_info[7] + ',' + game4_info[8] + ',' + game4_info[9] + ',' + game4_info[10] + ',' + str(game4_info[11])
            new_5 = game5_info[0] + ',' + game5_info[1] + ',' + game5_info[2] + ',' + game5_info[3] + ',' + game5_info[4] + ',' + game5_info[5] + ',' + game5_info[6] + ',' + game5_info[7] + ',' + game5_info[8] + ',' + game5_info[9] + ',' + game5_info[10] + ',' + game5_info[11]
            new_6 = game6_info[0] + ',' + game6_info[1] + ',' + game6_info[2] + ',' + game6_info[3] + ',' + game6_info[4] + ',' + game6_info[5] + ',' + game6_info[6] + ',' + game6_info[7] + ',' + game6_info[8] + ',' + game6_info[9] + ',' + game6_info[10] + ',' + game6_info[11]
            new_7 = game7_info[0] + ',' + game7_info[1] + ',' + game7_info[2] + ',' + game7_info[3] + ',' + game7_info[4] + ',' + game7_info[5] + ',' + game7_info[6] + ',' + game7_info[7] + ',' + game7_info[8] + ',' + game7_info[9] + ',' + game7_info[10] + ',' + game7_info[11]
            new_8 = game8_info[0] + ',' + game8_info[1] + ',' + game8_info[2] + ',' + game8_info[3] + ',' + game8_info[4] + ',' + game8_info[5] + ',' + game8_info[6] + ',' + game8_info[7] + ',' + game8_info[8] + ',' + game8_info[9] + ',' + game8_info[10] + ',' + game8_info[11]
            a = open('games.txt', 'w')
            b = a.close
            c = open('games.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsUS' + '\n')
            write1 = c.write(new_1)
            write2 = c.write(new_2)
            write3 = c.write(new_3)
            write4 = c.write(new_4 + '\n')
            write5 = c.write(new_5)
            write6 = c.write(new_6)
            write7 = c.write(new_7)
            write8 = c.write(new_8)
            d = c.close

        game4_price = Button(game4_canvas, image = price099, command = download)
        game4_price.place(x=115, y=300)
        
        def backtoroot():
                game4_window.destroy()

        backbutton = Button(game4_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    def game5_window():
        root.withdraw()
        game5_window = Toplevel()
        game5_window.title('App Store')
        game5_window.minsize(1000, 600)
        game5_window.resizable(width = NO, height = NO)

        game5_line = read_games[5]
        game5_info = game5_line.split(',')

        game5_canvas = Canvas(game5_window, width = 1000, height = 600, bg = 'white')
        game5_canvas.place(x=0, y=0)

        game5_largeIcon_pic = Label(game5_canvas, image = game5_largeIcon)
        game5_largeIcon_pic.place(x=100, y=70)

        game5_label = Label(game5_canvas, text = game5_info[3], font = 'Helvetica 30')
        game5_label.place(x=70, y=260)

        game5_scr1_pic = Label(game5_canvas, image = game5_scr1)
        game5_scr1_pic.place(x=450, y=30)

        game5_scr2_pic = Label(game5_canvas, image = game5_scr2)
        game5_scr2_pic.place(x=730, y= 30)

        game5_desc = Label(game5_canvas, font = 'Helvetica 24', text = game5_info[4], justify = LEFT)
        game5_desc.place(x=25, y=380)

        game5_desc2 = Label(game5_canvas, font = 'Helvetica 24', text = game5_info[5], justify = LEFT)
        game5_desc2.place(x=25, y=410)

        game5_desc3 = Label(game5_canvas, font = 'Helvetica 24', text = game5_info[6], justify = LEFT)
        game5_desc3.place(x=25, y=440)

        game5_desc4 = Label(game5_canvas, font = 'Helvetica 24', text = game5_info[7], justify = LEFT)
        game5_desc4.place(x=25, y=470)

        game5_desc5 = Label(game5_canvas, font = 'Helvetica 24', text = game5_info[8], justify = LEFT)
        game5_desc5.place(x=25, y=500)

        game5_size = Label(game5_canvas, font = 'Helvetica 24', text = 'App Size: '+game5_info[10])
        game5_size.place(x=25, y=540)

        def download():
            add_download = int(game5_info[11]) + 1
            game5_info[11] = add_download
            new_1 = game1_info[0] + ',' + game1_info[1] + ',' + game1_info[2] + ',' + game1_info[3] + ',' + game1_info[4] + ',' + game1_info[5] + ',' + game1_info[6] + ',' + game1_info[7] + ',' + game1_info[8] + ',' + game1_info[9] + ',' + game1_info[10] + ',' + game1_info[11]
            new_2 = game2_info[0] + ',' + game2_info[1] + ',' + game2_info[2] + ',' + game2_info[3] + ',' + game2_info[4] + ',' + game2_info[5] + ',' + game2_info[6] + ',' + game2_info[7] + ',' + game2_info[8] + ',' + game2_info[9] + ',' + game2_info[10] + ',' + game2_info[11]
            new_3 = game3_info[0] + ',' + game3_info[1] + ',' + game3_info[2] + ',' + game3_info[3] + ',' + game3_info[4] + ',' + game3_info[5] + ',' + game3_info[6] + ',' + game3_info[7] + ',' + game3_info[8] + ',' + game3_info[9] + ',' + game3_info[10] + ',' + game3_info[11]
            new_4 = game4_info[0] + ',' + game4_info[1] + ',' + game4_info[2] + ',' + game4_info[3] + ',' + game4_info[4] + ',' + game4_info[5] + ',' + game4_info[6] + ',' + game4_info[7] + ',' + game4_info[8] + ',' + game4_info[9] + ',' + game4_info[10] + ',' + game4_info[11]
            new_5 = game5_info[0] + ',' + game5_info[1] + ',' + game5_info[2] + ',' + game5_info[3] + ',' + game5_info[4] + ',' + game5_info[5] + ',' + game5_info[6] + ',' + game5_info[7] + ',' + game5_info[8] + ',' + game5_info[9] + ',' + game5_info[10] + ',' + str(game5_info[11])
            new_6 = game6_info[0] + ',' + game6_info[1] + ',' + game6_info[2] + ',' + game6_info[3] + ',' + game6_info[4] + ',' + game6_info[5] + ',' + game6_info[6] + ',' + game6_info[7] + ',' + game6_info[8] + ',' + game6_info[9] + ',' + game6_info[10] + ',' + game6_info[11]
            new_7 = game7_info[0] + ',' + game7_info[1] + ',' + game7_info[2] + ',' + game7_info[3] + ',' + game7_info[4] + ',' + game7_info[5] + ',' + game7_info[6] + ',' + game7_info[7] + ',' + game7_info[8] + ',' + game7_info[9] + ',' + game7_info[10] + ',' + game7_info[11]
            new_8 = game8_info[0] + ',' + game8_info[1] + ',' + game8_info[2] + ',' + game8_info[3] + ',' + game8_info[4] + ',' + game8_info[5] + ',' + game8_info[6] + ',' + game8_info[7] + ',' + game8_info[8] + ',' + game8_info[9] + ',' + game8_info[10] + ',' + game8_info[11]
            a = open('games.txt', 'w')
            b = a.close
            c = open('games.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsUS' + '\n')
            write1 = c.write(new_1)
            write2 = c.write(new_2)
            write3 = c.write(new_3)
            write4 = c.write(new_4)
            write5 = c.write(new_5 + '\n')
            write6 = c.write(new_6)
            write7 = c.write(new_7)
            write8 = c.write(new_8)
            d = c.close

        game5_price = Button(game5_canvas, image = price299, command = download)
        game5_price.place(x=115, y=300)

        def backtoroot():
                game5_window.destroy()

        backbutton = Button(game5_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)

    ###############################################################################

    def game6_window():
        root.withdraw()
        game6_window = Toplevel()
        game6_window.title('App Store')
        game6_window.minsize(1000, 600)
        game6_window.resizable(width = NO, height = NO)

        game6_line = read_games[6]
        game6_info = game6_line.split(',')

        game6_canvas = Canvas(game6_window, width = 1000, height = 600, bg = 'white')
        game6_canvas.place(x=0, y=0)

        game6_largeIcon_pic = Label(game6_canvas, image = game6_largeIcon)
        game6_largeIcon_pic.place(x=100, y=70)

        game6_label = Label(game6_canvas, text = game6_info[3], font = 'Helvetica 30')
        game6_label.place(x=90, y=260)

        game6_scr1_pic = Label(game6_canvas, image = game6_scr1)
        game6_scr1_pic.place(x=450, y=30)

        game6_scr2_pic = Label(game6_canvas, image = game6_scr2)
        game6_scr2_pic.place(x=730, y= 30)

        game6_desc = Label(game6_canvas, font = 'Helvetica 24', text = game6_info[4], justify = LEFT)
        game6_desc.place(x=25, y=380)

        game6_desc2 = Label(game6_canvas, font = 'Helvetica 24', text = game6_info[5], justify = LEFT)
        game6_desc2.place(x=25, y=410)

        game6_desc3 = Label(game6_canvas, font = 'Helvetica 24', text = game6_info[6], justify = LEFT)
        game6_desc3.place(x=25, y=440)

        game6_desc4 = Label(game6_canvas, font = 'Helvetica 24', text = game6_info[7], justify = LEFT)
        game6_desc4.place(x=25, y=470)

        game6_desc5 = Label(game6_canvas, font = 'Helvetica 24', text = game6_info[8], justify = LEFT)
        game6_desc5.place(x=25, y=500)

        game6_size = Label(game6_canvas, font = 'Helvetica 24', text = 'App Size: '+game6_info[10])
        game6_size.place(x=25, y=540)

        def download():
            add_download = int(game6_info[11]) + 1
            game6_info[11] = add_download
            new_1 = game1_info[0] + ',' + game1_info[1] + ',' + game1_info[2] + ',' + game1_info[3] + ',' + game1_info[4] + ',' + game1_info[5] + ',' + game1_info[6] + ',' + game1_info[7] + ',' + game1_info[8] + ',' + game1_info[9] + ',' + game1_info[10] + ',' + game1_info[11]
            new_2 = game2_info[0] + ',' + game2_info[1] + ',' + game2_info[2] + ',' + game2_info[3] + ',' + game2_info[4] + ',' + game2_info[5] + ',' + game2_info[6] + ',' + game2_info[7] + ',' + game2_info[8] + ',' + game2_info[9] + ',' + game2_info[10] + ',' + game2_info[11]
            new_3 = game3_info[0] + ',' + game3_info[1] + ',' + game3_info[2] + ',' + game3_info[3] + ',' + game3_info[4] + ',' + game3_info[5] + ',' + game3_info[6] + ',' + game3_info[7] + ',' + game3_info[8] + ',' + game3_info[9] + ',' + game3_info[10] + ',' + game3_info[11]
            new_4 = game4_info[0] + ',' + game4_info[1] + ',' + game4_info[2] + ',' + game4_info[3] + ',' + game4_info[4] + ',' + game4_info[5] + ',' + game4_info[6] + ',' + game4_info[7] + ',' + game4_info[8] + ',' + game4_info[9] + ',' + game4_info[10] + ',' + game4_info[11]
            new_5 = game5_info[0] + ',' + game5_info[1] + ',' + game5_info[2] + ',' + game5_info[3] + ',' + game5_info[4] + ',' + game5_info[5] + ',' + game5_info[6] + ',' + game5_info[7] + ',' + game5_info[8] + ',' + game5_info[9] + ',' + game5_info[10] + ',' + game5_info[11]
            new_6 = game6_info[0] + ',' + game6_info[1] + ',' + game6_info[2] + ',' + game6_info[3] + ',' + game6_info[4] + ',' + game6_info[5] + ',' + game6_info[6] + ',' + game6_info[7] + ',' + game6_info[8] + ',' + game6_info[9] + ',' + game6_info[10] + ',' + str(game6_info[11])
            new_7 = game7_info[0] + ',' + game7_info[1] + ',' + game7_info[2] + ',' + game7_info[3] + ',' + game7_info[4] + ',' + game7_info[5] + ',' + game7_info[6] + ',' + game7_info[7] + ',' + game7_info[8] + ',' + game7_info[9] + ',' + game7_info[10] + ',' + game7_info[11]
            new_8 = game8_info[0] + ',' + game8_info[1] + ',' + game8_info[2] + ',' + game8_info[3] + ',' + game8_info[4] + ',' + game8_info[5] + ',' + game8_info[6] + ',' + game8_info[7] + ',' + game8_info[8] + ',' + game8_info[9] + ',' + game8_info[10] + ',' + game8_info[11]
            a = open('games.txt', 'w')
            b = a.close
            c = open('games.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsUS' + '\n')
            write1 = c.write(new_1)
            write2 = c.write(new_2)
            write3 = c.write(new_3)
            write4 = c.write(new_4)
            write5 = c.write(new_5)
            write6 = c.write(new_6 + '\n')
            write7 = c.write(new_7)
            write8 = c.write(new_8)
            d = c.close

        game6_price = Button(game6_canvas, image = price699, command = download)
        game6_price.place(x=115, y=300)

        def backtoroot():
                game6_window.destroy()

        backbutton = Button(game6_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)


    ###############################################################################

    def game7_window():
        root.withdraw()
        game7_window = Toplevel()
        game7_window.title('App Store')
        game7_window.minsize(1000, 600)
        game7_window.resizable(width = NO, height = NO)

        game7_line = read_games[7]
        game7_info = game7_line.split(',')

        game7_canvas = Canvas(game7_window, width = 1000, height = 600, bg = 'white')
        game7_canvas.place(x=0, y=0)

        game7_largeIcon_pic = Label(game7_canvas, image = game7_largeIcon)
        game7_largeIcon_pic.place(x=100, y=70)

        game7_label = Label(game7_canvas, text = game7_info[3], font = 'Helvetica 30')
        game7_label.place(x=100, y=260)

        game7_scr1_pic = Label(game7_canvas, image = game7_scr1)
        game7_scr1_pic.place(x=450, y=30)

        game7_scr2_pic = Label(game7_canvas, image = game7_scr2)
        game7_scr2_pic.place(x=730, y= 30)

        game7_desc = Label(game7_canvas, font = 'Helvetica 24', text = game7_info[4], justify = LEFT)
        game7_desc.place(x=25, y=380)

        game7_desc2 = Label(game7_canvas, font = 'Helvetica 24', text = game7_info[5], justify = LEFT)
        game7_desc2.place(x=25, y=410)

        game7_desc3 = Label(game7_canvas, font = 'Helvetica 24', text = game7_info[6], justify = LEFT)
        game7_desc3.place(x=25, y=440)

        game7_desc4 = Label(game7_canvas, font = 'Helvetica 24', text = game7_info[7], justify = LEFT)
        game7_desc4.place(x=25, y=470)

        game7_desc5 = Label(game7_canvas, font = 'Helvetica 24', text = game7_info[8], justify = LEFT)
        game7_desc5.place(x=25, y=500)

        game7_size = Label(game7_canvas, font = 'Helvetica 24', text = 'App Size: '+game7_info[10])
        game7_size.place(x=25, y=540)

        def download():
            add_download = int(game7_info[11]) + 1
            game7_info[11] = add_download
            new_1 = game1_info[0] + ',' + game1_info[1] + ',' + game1_info[2] + ',' + game1_info[3] + ',' + game1_info[4] + ',' + game1_info[5] + ',' + game1_info[6] + ',' + game1_info[7] + ',' + game1_info[8] + ',' + game1_info[9] + ',' + game1_info[10] + ',' + game1_info[11]
            new_2 = game2_info[0] + ',' + game2_info[1] + ',' + game2_info[2] + ',' + game2_info[3] + ',' + game2_info[4] + ',' + game2_info[5] + ',' + game2_info[6] + ',' + game2_info[7] + ',' + game2_info[8] + ',' + game2_info[9] + ',' + game2_info[10] + ',' + game2_info[11]
            new_3 = game3_info[0] + ',' + game3_info[1] + ',' + game3_info[2] + ',' + game3_info[3] + ',' + game3_info[4] + ',' + game3_info[5] + ',' + game3_info[6] + ',' + game3_info[7] + ',' + game3_info[8] + ',' + game3_info[9] + ',' + game3_info[10] + ',' + game3_info[11]
            new_4 = game4_info[0] + ',' + game4_info[1] + ',' + game4_info[2] + ',' + game4_info[3] + ',' + game4_info[4] + ',' + game4_info[5] + ',' + game4_info[6] + ',' + game4_info[7] + ',' + game4_info[8] + ',' + game4_info[9] + ',' + game4_info[10] + ',' + game4_info[11]
            new_5 = game5_info[0] + ',' + game5_info[1] + ',' + game5_info[2] + ',' + game5_info[3] + ',' + game5_info[4] + ',' + game5_info[5] + ',' + game5_info[6] + ',' + game5_info[7] + ',' + game5_info[8] + ',' + game5_info[9] + ',' + game5_info[10] + ',' + game5_info[11]
            new_6 = game6_info[0] + ',' + game6_info[1] + ',' + game6_info[2] + ',' + game6_info[3] + ',' + game6_info[4] + ',' + game6_info[5] + ',' + game6_info[6] + ',' + game6_info[7] + ',' + game6_info[8] + ',' + game6_info[9] + ',' + game6_info[10] + ',' + game6_info[11]
            new_7 = game7_info[0] + ',' + game7_info[1] + ',' + game7_info[2] + ',' + game7_info[3] + ',' + game7_info[4] + ',' + game7_info[5] + ',' + game7_info[6] + ',' + game7_info[7] + ',' + game7_info[8] + ',' + game7_info[9] + ',' + game7_info[10] + ',' + str(game7_info[11])
            new_8 = game8_info[0] + ',' + game8_info[1] + ',' + game8_info[2] + ',' + game8_info[3] + ',' + game8_info[4] + ',' + game8_info[5] + ',' + game8_info[6] + ',' + game8_info[7] + ',' + game8_info[8] + ',' + game8_info[9] + ',' + game8_info[10] + ',' + game8_info[11]
            a = open('games.txt', 'w')
            b = a.close
            c = open('games.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsUS' + '\n')
            write1 = c.write(new_1)
            write2 = c.write(new_2)
            write3 = c.write(new_3)
            write4 = c.write(new_4)
            write5 = c.write(new_5)
            write6 = c.write(new_6)
            write7 = c.write(new_7 + '\n')
            write8 = c.write(new_8)
            d = c.close

        game7_price = Button(game7_canvas, image = price0, command = download)
        game7_price.place(x=115, y=300)

        def backtoroot():
                game7_window.destroy()

        backbutton = Button(game7_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)


    ###############################################################################

    def game8_window():
        root.withdraw()
        game8_window = Toplevel()
        game8_window.title('App Store')
        game8_window.minsize(1000, 600)
        game8_window.resizable(width = NO, height = NO)

        game8_line = read_games[8]
        game8_info = game8_line.split(',')

        game8_canvas = Canvas(game8_window, width = 1000, height = 600, bg = 'white')
        game8_canvas.place(x=0, y=0)

        game8_largeIcon_pic = Label(game8_canvas, image = game8_largeIcon)
        game8_largeIcon_pic.place(x=100, y=70)

        game8_label = Label(game8_canvas, text = game8_info[3], font = 'Helvetica 30')
        game8_label.place(x=130, y=260)

        game8_scr1_pic = Label(game8_canvas, image = game8_scr1)
        game8_scr1_pic.place(x=450, y=30)

        game8_scr2_pic = Label(game8_canvas, image = game8_scr2)
        game8_scr2_pic.place(x=730, y= 30)

        game8_desc = Label(game8_canvas, font = 'Helvetica 24', text = game8_info[4], justify = LEFT)
        game8_desc.place(x=25, y=380)

        game8_desc2 = Label(game8_canvas, font = 'Helvetica 24', text = game8_info[5], justify = LEFT)
        game8_desc2.place(x=25, y=410)

        game8_desc3 = Label(game8_canvas, font = 'Helvetica 24', text = game8_info[6], justify = LEFT)
        game8_desc3.place(x=25, y=440)

        game8_desc4 = Label(game8_canvas, font = 'Helvetica 24', text = game8_info[7], justify = LEFT)
        game8_desc4.place(x=25, y=470)

        game8_desc5 = Label(game8_canvas, font = 'Helvetica 24', text = game8_info[8], justify = LEFT)
        game8_desc5.place(x=25, y=500)

        game8_size = Label(game8_canvas, font = 'Helvetica 24', text = 'App Size: '+game8_info[10])
        game8_size.place(x=25, y=540)

        def download():
            add_download = int(game8_info[11]) + 1
            game8_info[11] = add_download
            new_1 = game1_info[0] + ',' + game1_info[1] + ',' + game1_info[2] + ',' + game1_info[3] + ',' + game1_info[4] + ',' + game1_info[5] + ',' + game1_info[6] + ',' + game1_info[7] + ',' + game1_info[8] + ',' + game1_info[9] + ',' + game1_info[10] + ',' + game1_info[11]
            new_2 = game2_info[0] + ',' + game2_info[1] + ',' + game2_info[2] + ',' + game2_info[3] + ',' + game2_info[4] + ',' + game2_info[5] + ',' + game2_info[6] + ',' + game2_info[7] + ',' + game2_info[8] + ',' + game2_info[9] + ',' + game2_info[10] + ',' + game2_info[11]
            new_3 = game3_info[0] + ',' + game3_info[1] + ',' + game3_info[2] + ',' + game3_info[3] + ',' + game3_info[4] + ',' + game3_info[5] + ',' + game3_info[6] + ',' + game3_info[7] + ',' + game3_info[8] + ',' + game3_info[9] + ',' + game3_info[10] + ',' + game3_info[11]
            new_4 = game4_info[0] + ',' + game4_info[1] + ',' + game4_info[2] + ',' + game4_info[3] + ',' + game4_info[4] + ',' + game4_info[5] + ',' + game4_info[6] + ',' + game4_info[7] + ',' + game4_info[8] + ',' + game4_info[9] + ',' + game4_info[10] + ',' + game4_info[11]
            new_5 = game5_info[0] + ',' + game5_info[1] + ',' + game5_info[2] + ',' + game5_info[3] + ',' + game5_info[4] + ',' + game5_info[5] + ',' + game5_info[6] + ',' + game5_info[7] + ',' + game5_info[8] + ',' + game5_info[9] + ',' + game5_info[10] + ',' + game5_info[11]
            new_6 = game6_info[0] + ',' + game6_info[1] + ',' + game6_info[2] + ',' + game6_info[3] + ',' + game6_info[4] + ',' + game6_info[5] + ',' + game6_info[6] + ',' + game6_info[7] + ',' + game6_info[8] + ',' + game6_info[9] + ',' + game6_info[10] + ',' + game6_info[11]
            new_7 = game7_info[0] + ',' + game7_info[1] + ',' + game7_info[2] + ',' + game7_info[3] + ',' + game7_info[4] + ',' + game7_info[5] + ',' + game7_info[6] + ',' + game7_info[7] + ',' + game7_info[8] + ',' + game7_info[9] + ',' + game7_info[10] + ',' + game7_info[11]
            new_8 = game8_info[0] + ',' + game8_info[1] + ',' + game8_info[2] + ',' + game8_info[3] + ',' + game8_info[4] + ',' + game8_info[5] + ',' + game8_info[6] + ',' + game8_info[7] + ',' + game8_info[8] + ',' + game8_info[9] + ',' + game8_info[10] + ',' + str(game8_info[11])
            a = open('games.txt', 'w')
            b = a.close
            c = open('games.txt', 'a')
            write0 = c.write('#[0-sellerid, 1-productid, 2-category, 3-appname, 4-appdescription1, 5-appdescription2, 6-appdescription3, 7-appdescription4, 8-appdescription5, 9-price, 10-appsize, 11-downloadsUS' + '\n')
            write1 = c.write(new_1)
            write2 = c.write(new_2)
            write3 = c.write(new_3)
            write4 = c.write(new_4)
            write5 = c.write(new_5)
            write6 = c.write(new_6)
            write7 = c.write(new_7)
            write8 = c.write(new_8 + '\n')
            d = c.close

        game8_price = Button(game8_canvas, image = price0, command = download)
        game8_price.place(x=115, y=300)

        def backtoroot():
                game8_window.destroy()

        backbutton = Button(game8_canvas, image = back_icon, command = backtoroot)
        backbutton.place(x=20,y=20)


    ###############################################################################

    #funcion para asignar tecla 'Enter' a boton de busqueda
    #E: tecla
    #S: activar boton de busqueda
    def return_key(key):
        searchWindow()

    root_eng_logged.bind('<Return>', return_key)

    #other labels from homescreen
    aotd_label = Label(root_eng_logged, text = 'Featured App', font = 'Helvetica 26')
    aotd_label.place(x=250, y=105)

    cat_label = Label(root_eng_logged, text = 'Categories', font = 'Helvetica 26')
    cat_label.place(x=760, y=105)

    games_label = Label(root_eng_logged, text = 'Games', font = 'Helvetica 26')
    games_label.place(x=720, y=205)

    apps_label = Label(root_eng_logged, text = 'Apps', font = 'Helvetica 26')
    apps_label.place(x=730, y=320)

    #labels from apps under the featured one
    app2_label = Label(root_eng_logged, text = app2_info[3], font = 'Helvetica 16')
    app2_label.place(x=30, y=530)

    app2_pricelabel = Label(root_eng_logged, text = app2_info[9], font = 'Helvetica 16')
    app2_pricelabel.place(x=70, y=550)

    app3_label = Label(root_eng_logged, text = app3_info[3], font = 'Helvetica 16')
    app3_label.place(x=220, y=530)

    app3_pricelabel = Label(root_eng_logged, text = app3_info[9], font = 'Helvetica 16')
    app3_pricelabel.place(x=275, y=550)

    game1_label = Label(root_eng_logged, text = game1_info[3], font = 'Helvetica 16')
    game1_label.place(x=465, y=530)

    game1_pricelabel = Label(root_eng_logged, text = game1_info[9], font = 'Helvetica 16')
    game1_pricelabel.place(x=475, y=550)

    game2_label = Label(root_eng_logged, text = game2_info[3], font = 'Helvetica 16')
    game2_label.place(x=650, y=530)

    game2_pricelabel = Label(root_eng_logged, text = game2_info[9], font = 'Helvetica 16')
    game2_pricelabel.place(x=675, y=550)

    game3_label = Label(root_eng_logged, text = game3_info[3], font = 'Helvetica 16')
    game3_label.place(x=870, y=530)

    game3_pricelabel = Label(root_eng_logged, text = game3_info[9], font = 'Helvetica 16')
    game3_pricelabel.place(x=875, y=550)

    #App Buttons on homescreen
    app1_ad_pic = Button(root_eng_logged, image = app1_ad, command = app1_window)
    app1_ad_pic.place(x=0, y=150)

    app2_pic = Button(root_eng_logged, image = app2_icon, command = app2_window)
    app2_pic.place(x=40, y=420)

    app3_pic = Button(root_eng_logged, image = app3_icon, command = app3_window)
    app3_pic.place(x=240, y=420)

    game1_pic = Button(root_eng_logged, image = game1_icon, command = game1_window)
    game1_pic.place(x=440, y=420)

    game2_pic = Button(root_eng_logged, image = game2_icon, command = game2_window)
    game2_pic.place(x=640, y=420)

    game3_pic = Button(root_eng_logged, image = game3_icon, command = game3_window)
    game3_pic.place(x=840, y=420)

    #search system
    search_label = Button(root_eng_logged, image = search_icon, command = searchWindow)
    search_label.place(x=900,y=63)

    search_entry = Entry(root_eng_logged, width = 20)
    search_entry.place(x=720,y=70)

    #category icons
    games_icon_pic = Button(root_eng_logged, image = games_icon, command = games_menu)
    games_icon_pic.place(x=840, y=165)

    apps_icon_pic = Button(root_eng_logged, image = apps_icon, command = apps_menu)
    apps_icon_pic.place(x=840, y=285)
    
#labels from homescreen
welcome_label = Label(root, text='Welcome to the AStore', font = 'Helvetica 28')
welcome_label.place(x=340, y=0)

change_lang_label = Label(root, text = 'Change region', font = 'Helvetica 16')
change_lang_label.place(x=780, y=5)

change_lang_cr = Button(root, image = cr_flag, command = root_esp_not_logged)
change_lang_cr.place(x=890, y=0)

#open apps and games lines from txt
apps = open('apps.txt', 'r+')
read_apps = apps.readlines()

app1_line = read_apps[1]
app1_info = app1_line.split(',')
app2_line = read_apps[2]
app2_info = app2_line.split(',')
app3_line = read_apps[3]
app3_info = app3_line.split(',')
app4_line = read_apps[4]
app4_info = app4_line.split(',')
app5_line = read_apps[5]
app5_info = app5_line.split(',')
app6_line = read_apps[6]
app6_info = app6_line.split(',')
app7_line = read_apps[7]
app7_info = app7_line.split(',')
app8_line = read_apps[8]
app8_info = app8_line.split(',')

games = open('games.txt', 'r+')
read_games = games.readlines()

game1_line = read_games[1]
game1_info = game1_line.split(',')
game2_line = read_games[2]
game2_info = game2_line.split(',')
game3_line = read_games[3]
game3_info = game3_line.split(',')
game4_line = read_games[4]
game4_info = game4_line.split(',')
game5_line = read_games[5]
game5_info = game5_line.split(',')
game6_line = read_games[6]
game6_info = game6_line.split(',')
game7_line = read_games[7]
game7_info = game7_line.split(',')
game8_line = read_games[8]
game8_info = game8_line.split(',')

###############################################################################

#sistema de busqueda con nombre de app o palabras alusivas
#E: palabra a buscar
#S: redireccion
#R: nombre de app o palabra alusiva

def searchWindow():
    apps = open('apps.txt', 'r+')
    read_apps = apps.readlines()
    
    app1_line = read_apps[1]
    app1_info = app1_line.split(',')
    app2_line = read_apps[2]
    app2_info = app2_line.split(',')
    app3_line = read_apps[3]
    app3_info = app3_line.split(',')
    app4_line = read_apps[4]
    app4_info = app4_line.split(',')
    app5_line = read_apps[5]
    app5_info = app5_line.split(',')
    app6_line = read_apps[6]
    app6_info = app6_line.split(',')
    app7_line = read_apps[7]
    app7_info = app7_line.split(',')
    app8_line = read_apps[8]
    app8_info = app8_line.split(',')
    apps.close()

    games = open('games.txt', 'r+')
    read_games = games.readlines()

    game1_line = read_games[1]
    game1_info = game1_line.split(',')
    game2_line = read_games[2]
    game2_info = game2_line.split(',')
    game3_line = read_games[3]
    game3_info = game3_line.split(',')
    game4_line = read_games[4]
    game4_info = game4_line.split(',')
    game5_line = read_games[5]
    game5_info = game5_line.split(',')
    game6_line = read_games[6]
    game6_info = game6_line.split(',')
    game7_line = read_games[7]
    game7_info = game7_line.split(',')
    game8_line = read_games[8]
    game8_info = game8_line.split(',')
    games.close()
    apps = open('apps.txt', 'r+')
    read_apps = apps.readlines()
    searchText=search_entry.get()

    if searchText.strip() == 'juegos':
        games_menu()
    if searchText.strip() == 'juego':
        games_menu()
    elif searchText.strip() == 'aplicaciones':
        apps_menu()
    elif searchText.strip() == 'aplicacion':
        apps_menu()
    elif searchText.strip() == 'apps':
        apps_menu()
    elif searchText.strip() == 'aps':
        apps_menu()
    elif searchText.strip() == 'games':
        games_menu()
    elif searchText.strip() == 'jugar':
        games_menu()
    elif searchText.strip() == 'play':
        games_menu()
    elif searchText.strip() == 'jeff schmidt python':
        app1_window()
    elif searchText.strip() == 'jeff schmidts python':
        app1_window()
    elif searchText.strip() == 'python':
        app1_window()
    elif searchText.strip() == 'Python':
        app1_window()
    elif searchText.strip() == 'Jeff':
        app1_window()
    elif searchText.strip() == 'jeff':
        app1_window()
    elif searchText.strip() == 'jeff schmidt':
        app1_window()
    elif searchText.strip() == 'schmidt':
        app1_window()
    elif searchText.strip() == 'Schmidt':
        app1_window()
    elif searchText.strip() == 'code':
        app1_window()
    elif searchText.strip() == 'programming':
        app1_window()
    elif searchText.strip() == 'programar':
        app1_window()
    elif searchText.strip() == 'weed smoke pro':
        app2_window()
    elif searchText.strip() == 'weed':
        app2_window()
    elif searchText.strip() == 'smoke':
        app2_window()
    elif searchText.strip() == 'weed smoke':
        app2_window()
    elif searchText.strip() == 'marijuana':
        app2_window()
    elif searchText.strip() == '420':
        app2_window()
    elif searchText.strip() == 'bob marley':
        app2_window()
    elif searchText.strip() == 'math with ed sheeran':
        app3_window()
    elif searchText.strip() == 'ed sheeran':
        app3_window()
    elif searchText.strip() == 'ed':
        app3_window()
    elif searchText.strip() == 'sheeran':
        app3_window()
    elif searchText.strip() == 'math':
        app3_window()
    elif searchText.strip() == 'matematica':
        app3_window()
    elif searchText.strip() == 'mate':
        app3_window()
    elif searchText.strip() == 'you look perfect tonight':
        app3_window()
    elif searchText.strip() == 'taylors swift':
        app4_window()
    elif searchText.strip() == 'taylor swift':
        app4_window()
    elif searchText.strip() == 'swift':
        app4_window()
    elif searchText.strip() == 'taylor':
        app4_window()
    elif searchText.strip() == 'swift code':
        app4_window()
    elif searchText.strip() == 'swift language':
        app4_window()
    elif searchText.strip() == 'swift lenguaje':
        app4_window()
    elif searchText.strip() == 'the pirate bay':
        app5_window()
    elif searchText.strip() == 'free movies':
        app5_window()
    elif searchText.strip() == 'peliculas gratis':
        app5_window()
    elif searchText.strip() == 'pirate':
        app5_window()
    elif searchText.strip() == 'pirate bay':
        app5_window()
    elif searchText.strip() == 'piratear':
        app5_window()
    elif searchText.strip() == 'free tv':
        app5_window()
    elif searchText.strip() == 'torrent':
        app5_window()
    elif searchText.strip() == 'apple music':
        app6_window()
    elif searchText.strip() == 'apple':
        app6_window()
    elif searchText.strip() == 'music':
        app6_window()
    elif searchText.strip() == 'free music':
        app6_window()
    elif searchText.strip() == 'musica gratis':
        app6_window()
    elif searchText.strip() == 'netflix':
        app7_window()
    elif searchText.strip() == 'series':
        app7_window()
    elif searchText.strip() == 'tv shows':
        app7_window()
    elif searchText.strip() == 'movies':
        app7_window()
    elif searchText.strip() == 'peliculas':
        app7_window()
    elif searchText.strip() == 'netflix':
        app7_window()
    elif searchText.strip() == 'im feeling lucky':
        app8_window()
    elif searchText.strip() == 'kiss me pls':
        app8_window()
    elif searchText.strip() == 'kiss me':
        app8_window()
    elif searchText.strip() == 'notlim':
        game1_window()
    elif searchText.strip() == 'Notlim':
        game1_window()
    elif searchText.strip() == 'mining':
        game1_window()
    elif searchText.strip() == 'intro & taller':
        game2_window()
    elif searchText.strip() == 'intro y taller':
        game2_window()
    elif searchText.strip() == 'Intro y Taller':
        game2_window()
    elif searchText.strip() == 'Intro & taller':
        game2_window()
    elif searchText.strip() == 'intro':
        game2_window()
    elif searchText.strip() == 'taller':
        game2_window()
    elif searchText.strip() == 'samus aran':
        game2_window()
    elif searchText.strip() == 'conejos':
        game2_window()
    elif searchText.strip() == 'arnold schwarzenegger':
        game2_window()
    elif searchText.strip() == 'jessie':
        game3_window()
    elif searchText.strip() == 'ingeniera':
        game3_window()
    elif searchText.strip() == 'engineer':
        game3_window()
    elif searchText.strip() == 'game of shots':
        game4_window()
    elif searchText.strip() == 'shots':
        game4_window()
    elif searchText.strip() == 'drinking game':
        game4_window()
    elif searchText.strip() == 'alcohol':
        game4_window()
    elif searchText.strip() == 'tragos':
        game4_window()
    elif searchText.strip() == 'monument valley':
        game5_window()
    elif searchText.strip() == 'arquitectura':
        game5_window()
    elif searchText.strip() == 'architecture':
        game5_window()
    elif searchText.strip() == 'monument':
        game5_window()
    elif searchText.strip() == 'valley':
        game5_window()
    elif searchText.strip() == 'life is strange':
        game6_window()
    elif searchText.strip() == 'life':
        game6_window()
    elif searchText.strip() == 'strange':
        game6_window()
    elif searchText.strip() == 'max caulfield':
        game6_window()
    elif searchText.strip() == 'blackwell':
        game6_window()
    elif searchText.strip() == 'unbreakable':
        game7_window()
    elif searchText.strip() == 'jeff schmidt game':
        game7_window()
    elif searchText.strip() == 'jeff schmidt juego':
        game7_window()
    elif searchText.strip() == 'stocks':
        game8_window()
    elif searchText.strip() == 'bolsa':
        game8_window()
    elif searchText.strip() == 'dinero':
        game8_window()
    elif searchText.strip() == 'money':
        game8_window()
    elif searchText.strip() == 'strategy':
        game8_window()
    elif searchText.strip() == 'estrategia':
        game8_window()
    elif searchText.strip() == app1_info[3].strip():
        app1_window()
    elif searchText.strip() == app2_info[3].strip():
        app2_window()   
    elif searchText.strip() == app3_info[3].strip():
        app3_window()
    elif searchText.strip() == app4_info[3].strip():
        app4_window()
    elif searchText.strip() == app5_info[3].strip():
        app5_window()
    elif searchText.strip() == app6_info[3].strip():
        app6_window()
    elif searchText.strip() == app7_info[3].strip():
        app7_window()
    elif searchText.strip() == app8_info[3].strip():
        app8_window()
    elif searchText.strip() == game1_info[3].strip():
        game1_window()
    elif searchText.strip() == game2_info[3].strip():
        game2_window()
    elif searchText.strip() == game3_info[3].strip():
        game3_window()
    elif searchText.strip() == game4_info[3].strip():
        game4_window()
    elif searchText.strip() == game5_info[3].strip():
        game5_window()
    elif searchText.strip() == game6_info[3].strip():
        game6_window()
    elif searchText.strip() == game7_info[3].strip():
        game7_window()
    elif searchText.strip() == game8_info[3].strip():
        game8_window()
    else:
        messagebox.showwarning("Search results:",searchText+' not found')

###############################################################################

#register window
def registerWindow():
    root.withdraw()
    registerwindow = Toplevel()
    registerwindow.title('App Store')
    registerwindow.minsize(1000,600)
    registerwindow.resizable(width = NO, height = NO)

    registercanvas = Canvas(registerwindow, width = 1000, height = 600, bg = 'white')
    registercanvas.place(x=0,y=0)

    #labels:
    title_label = Label(registercanvas, text = 'Register - USA REGION', font = 'Helvetica 28')
    title_label.place(x=320, y=20)
    
    name_label = Label(registercanvas, text = 'First Name:', font = 'Helvetica 24')
    name_label.place(x=100, y=175)

    lastname_label = Label(registercanvas, text = 'Last name:', font = 'Helvetica 24')
    lastname_label.place(x=100, y=250)

    email_label = Label(registercanvas, text = 'Email:', font = 'Helvetica 24')
    email_label.place(x=100, y=325)

    country_label = Label(registercanvas, text = 'Password', font = 'Helvetica 24')
    country_label.place(x=100, y=400)
    
    #entries:
    nameentry = Entry(registercanvas, width = 20)
    nameentry.place(x=300, y=175)

    lastnameentry = Entry(registercanvas, width = 20)
    lastnameentry.place(x=300, y= 250)

    usernameentry = Entry(registercanvas, width = 20)
    usernameentry.place(x=300, y=325)

    passwordentry = Entry(registercanvas, show = '*', width = 20)
    passwordentry.place(x=300, y=400)

    #write users in txt files
    def filewrite():
        a = open ('usercount.txt','r+')
        lastIndex = a.readlines()
        userid = lastIndex[len(lastIndex) - 1]
        name = nameentry.get()
        lastname = lastnameentry.get()
        username = usernameentry.get()
        password = passwordentry.get()
        b = open('users.txt','a')
        info = username + ',' + name + ',' + password + ',' + lastname + ',' + userid + ',' + 'US' + ',' + '0'
        b.write('\n' + str(info))
        a.write('\n' + str(int(userid) + 1))

    processregisterbutton = Button(registercanvas, text = 'Sign Up', command = filewrite)
    processregisterbutton.place(x=250, y=500)
    
    def backtoroot():
        registerwindow.destroy()
        root.deiconify()

    backbutton = Button(registerwindow, image = back_icon, command = backtoroot)
    backbutton.place(x=20,y=20)

##############################################################################

#login window
def loginWindow():
    root.withdraw()
    loginwindow = Toplevel()
    loginwindow.title('App Store')
    loginwindow.minsize(1000,600)
    loginwindow.resizable(width = NO, height = NO)

    logincanvas = Canvas(loginwindow, width = 1000, height = 600, bg = 'white')
    logincanvas.place(x=0,y=0)

    title_label = Label(logincanvas, text = 'Access - USA REGION', font = 'Helvetica 28')
    title_label.place(x=320, y=20)

    username_email_label = Label(logincanvas, text = 'Username/Email', font = 'Helvetica 24')
    username_email_label.place(x=100,y=175)

    password_label = Label(logincanvas, text = 'Password', font = 'Helvetica 24')
    password_label.place(x=100, y=250)

    emailloginentry = Entry(logincanvas, width = 20)
    emailloginentry.place(x=350, y=175)

    passwordloginentry = Entry(logincanvas, show = '*', width = 20)
    passwordloginentry.place(x=350, y=250)

    #login function
    #E: user y password de entry
    #S: redireccion si user y password son validos y error si no
    #R: user y password validos
    def login():
            user0 = emailloginentry.get()
            pass0 = passwordloginentry.get()
            with open("users.txt", "r") as file:
                reader = file.readlines()
            
            for line in reader:
               if not line.strip():
                   continue
               else:
                   username=line.split(",")[0]
                   pswd=line.split(",")[2]
                   if username == user0  and pswd == pass0:
                       root_eng_logged()
                       break
            else:
               messagebox.showwarning("Information",'Incorrect username or password')
        
    processloginbutton = Button(logincanvas, text = 'Log in', font = 'Helvetica 24',  command = login)
    processloginbutton.place(x=100, y=400)

    def backtoroot():
        loginwindow.destroy()
        root.deiconify()

    backbutton = Button(loginwindow, image = back_icon, command = backtoroot)
    backbutton.place(x=20,y=20)

###############################################################################

#apps menu
def apps_menu():
    root.withdraw()
    apps_menu = Toplevel()
    apps_menu.title('App Store')
    apps_menu.minsize(1000, 600)
    apps_menu.resizable(width = NO, height = NO)

    appsmenu_canvas = Canvas(apps_menu, width = 1000, height = 600, bg = 'white')
    appsmenu_canvas.place(x=0, y=0)

    app1_line = read_apps[1]
    app1_info = app1_line.split(',')
    app2_line = read_apps[2]
    app2_info = app2_line.split(',')
    app3_line = read_apps[3]
    app3_info = app3_line.split(',')
    app4_line = read_apps[4]
    app4_info = app4_line.split(',')
    app5_line = read_apps[5]
    app5_info = app5_line.split(',')
    app6_line = read_apps[6]
    app6_info = app6_line.split(',')
    app7_line = read_apps[7]
    app7_info = app7_line.split(',')
    app8_line = read_apps[8]
    app8_info = app8_line.split(',')
    
    #
    app1_icon = Button(appsmenu_canvas, image = app1_largeIcon, command = app1_window)
    app1_icon.place(x=60, y=70)

    app1_label = Label(appsmenu_canvas, text = app1_info[3], font = 'Helvetica 24')
    app1_label.place(x=30, y=270)

    app1_price = Label(appsmenu_canvas, text = app1_info[9], font = 'Helvetica 24')
    app1_price.place(x=120, y=300)

    #
    app2_icon = Button(appsmenu_canvas, image = app2_largeIcon, command = app2_window)
    app2_icon.place(x=290, y=70)

    app2_label = Label(appsmenu_canvas, text = app2_info[3], font = 'Helvetica 24')
    app2_label.place(x=280, y=270)

    app2_price = Label(appsmenu_canvas, text = app2_info[9], font = 'Helvetica 24')
    app2_price.place(x=360, y=300)

    #
    app3_icon = Button(appsmenu_canvas, image = app3_largeIcon, command = app3_window)
    app3_icon.place(x=520, y=70)

    app3_label = Label(appsmenu_canvas, text = app3_info[3], font = 'Helvetica 24')
    app3_label.place(x=500, y=270)

    app3_price = Label(appsmenu_canvas, text = app3_info[9], font = 'Helvetica 24')
    app3_price.place(x=580, y=300)

    #
    app4_icon = Button(appsmenu_canvas, image = app4_largeIcon, command = app4_window)
    app4_icon.place(x=750, y=70)

    app4_label = Label(appsmenu_canvas, text = app4_info[3], font = 'Helvetica 24')
    app4_label.place(x=765, y=270)

    app4_price = Label(appsmenu_canvas, text = app4_info[9], font = 'Helvetica 24')
    app4_price.place(x=810, y=300)

    #
    app5_icon = Button(appsmenu_canvas, image = app5_largeIcon, command = app5_window)
    app5_icon.place(x=60, y=350)

    app5_label = Label(appsmenu_canvas, text = app5_info[3], font = 'Helvetica 24')
    app5_label.place(x=65, y=540)

    app5_price = Label(appsmenu_canvas, text = app5_info[9], font = 'Helvetica 24')
    app5_price.place(x=115, y=570)

    #
    app6_icon = Button(appsmenu_canvas, image = app6_largeIcon, command = app6_window)
    app6_icon.place(x=290, y=350)

    app6_label = Label(appsmenu_canvas, text = app6_info[3], font = 'Helvetica 24')
    app6_label.place(x=310, y=540)

    app6_price = Label(appsmenu_canvas, text = app6_info[9], font = 'Helvetica 24')
    app6_price.place(x=345, y=570)

    #
    app7_icon = Button(appsmenu_canvas, image = app7_largeIcon, command = app7_window)
    app7_icon.place(x=520, y=350)

    app7_label = Label(appsmenu_canvas, text = app7_info[3], font = 'Helvetica 24')
    app7_label.place(x=570, y=540)

    app7_price = Label(appsmenu_canvas, text = app7_info[9], font = 'Helvetica 24')
    app7_price.place(x=575, y=570)

    #
    app8_icon = Button(appsmenu_canvas, image = app8_largeIcon, command = app8_window)
    app8_icon.place(x=750, y=350)
    
    app8_label = Label(appsmenu_canvas, text = app8_info[3], font = 'Helvetica 24')
    app8_label.place(x=780, y=540)

    app8_price = Label(appsmenu_canvas, text = app8_info[9], font = 'Helvetica 24')
    app8_price.place(x=810, y=570)

    def backtoroot():
        apps_menu.destroy()
        root.deiconify()

    backbutton = Button(apps_menu, image = back_icon, command = backtoroot)
    backbutton.place(x=20,y=20)

###############################################################################

#games menu
def games_menu():
    root.withdraw()
    games_menu = Toplevel()
    games_menu.title('App Store')
    games_menu.minsize(1000, 600)
    games_menu.resizable(width = NO, height = NO)

    gamesmenu_canvas = Canvas(games_menu, width = 1000, height = 600, bg = 'white')
    gamesmenu_canvas.place(x=0, y=0)

    game1_line = read_games[1]
    game1_info = game1_line.split(',')
    game2_line = read_games[2]
    game2_info = game2_line.split(',')
    game3_line = read_games[3]
    game3_info = game3_line.split(',')
    
    #
    game1_icon = Button(gamesmenu_canvas, image = game1_largeIcon, command = game1_window)
    game1_icon.place(x=60, y=70)

    game1_label = Label(gamesmenu_canvas, text = game1_info[3], font = 'Helvetica 24')
    game1_label.place(x=100, y=270)

    game1_price = Label(gamesmenu_canvas, text = game1_info[9], font = 'Helvetica 24')
    game1_price.place(x=120, y=300)

    #
    game2_icon = Button(gamesmenu_canvas, image = game2_largeIcon, command = game2_window)
    game2_icon.place(x=290, y=70)

    game2_label = Label(gamesmenu_canvas, text = game2_info[3], font = 'Helvetica 24')
    game2_label.place(x=315, y=270)

    game2_price = Label(gamesmenu_canvas, text = game2_info[9], font = 'Helvetica 24')
    game2_price.place(x=355, y=300)

    #
    game3_icon = Button(gamesmenu_canvas, image = game3_largeIcon, command = game3_window)
    game3_icon.place(x=520, y=70)

    game3_label = Label(gamesmenu_canvas, text = game3_info[3], font = 'Helvetica 24')
    game3_label.place(x=575, y=270)

    game3_price = Label(gamesmenu_canvas, text = game3_info[9], font = 'Helvetica 24')
    game3_price.place(x=580, y=300)

    #
    game4_icon = Button(gamesmenu_canvas, image = game4_largeIcon, command = game4_window)
    game4_icon.place(x=750, y=70)

    game4_label = Label(gamesmenu_canvas, text = game4_info[3], font = 'Helvetica 24')
    game4_label.place(x=760, y=270)

    game4_price = Label(gamesmenu_canvas, text = game4_info[9], font = 'Helvetica 24')
    game4_price.place(x=805, y=300)

    #
    game5_icon = Button(gamesmenu_canvas, image = game5_largeIcon, command = game5_window)
    game5_icon.place(x=60, y=350)

    game5_label = Label(gamesmenu_canvas, text = game5_info[3], font = 'Helvetica 24')
    game5_label.place(x=55, y=540)

    game5_price = Label(gamesmenu_canvas, text = game5_info[9], font = 'Helvetica 24')
    game5_price.place(x=110, y=570)

    #
    game6_icon = Button(gamesmenu_canvas, image = game6_largeIcon, command = game6_window)
    game6_icon.place(x=290, y=350)

    game6_label = Label(gamesmenu_canvas, text = game6_info[3], font = 'Helvetica 24')
    game6_label.place(x=300, y=540)

    game6_price = Label(gamesmenu_canvas, text = game6_info[9], font = 'Helvetica 24')
    game6_price.place(x=340, y=570)    

    #
    game7_icon = Button(gamesmenu_canvas, image = game7_largeIcon, command = game7_window)
    game7_icon.place(x=520, y=350)

    game7_label = Label(gamesmenu_canvas, text = game7_info[3], font = 'Helvetica 24')
    game7_label.place(x=540, y=540)

    game7_price = Label(gamesmenu_canvas, text = game7_info[9], font = 'Helvetica 24')
    game7_price.place(x=580, y=570)

    #
    game8_icon = Button(gamesmenu_canvas, image = game8_largeIcon, command = game8_window)
    game8_icon.place(x=750, y=350)

    game8_label = Label(gamesmenu_canvas, text = game8_info[3], font = 'Helvetica 24')
    game8_label.place(x=800, y=540)

    game8_price = Label(gamesmenu_canvas, text = game8_info[9], font = 'Helvetica 24')
    game8_price.place(x=820, y=570)

    def backtoroot():
        games_menu.destroy()
        root.deiconify()

    backbutton = Button(games_menu, image = back_icon, command = backtoroot)
    backbutton.place(x=20,y=20)

###############################################################################

#app windows
def app1_window():
    app1_window = Toplevel()
    app1_window.title('App Store')
    app1_window.minsize(1000, 600)
    app1_window.resizable(width = NO, height = NO)

    #access app info from lines in txt
    app1_line = read_apps[1]
    app1_info = app1_line.split(',')

    app1_canvas = Canvas(app1_window, width = 1000, height = 600, bg = 'white')
    app1_canvas.place(x=0, y=0)

    #labels for info
    app1_largeIcon_pic = Label(app1_canvas, image = app1_largeIcon)
    app1_largeIcon_pic.place(x=100, y=70)

    app1_label = Label(app1_canvas, text = app1_info[3], font = 'Helvetica 30')
    app1_label.place(x=70, y=250)

    app1_scr1_pic = Label(app1_canvas, image = app1_scr1)
    app1_scr1_pic.place(x=450, y=30)

    app1_scr2_pic = Label(app1_canvas, image = app1_scr2)
    app1_scr2_pic.place(x=730, y= 30)

    app1_desc = Label(app1_canvas, font = 'Helvetica 24', text = app1_info[4], justify = LEFT)
    app1_desc.place(x=25, y=380)

    app1_desc2 = Label(app1_canvas, font = 'Helvetica 24', text = app1_info[5], justify = LEFT)
    app1_desc2.place(x=25, y=410)

    app1_desc3 = Label(app1_canvas, font = 'Helvetica 24', text = app1_info[6], justify = LEFT)
    app1_desc3.place(x=25, y=440)

    app1_desc4 = Label(app1_canvas, font = 'Helvetica 24', text = app1_info[7], justify = LEFT)
    app1_desc4.place(x=25, y=470)

    app1_desc5 = Label(app1_canvas, font = 'Helvetica 24', text = app1_info[8], justify = LEFT)
    app1_desc5.place(x=25, y=500)

    app1_size = Label(app1_canvas, font = 'Helvetica 24', text = 'App Size:'+app1_info[10])
    app1_size.place(x=25, y=540)

    app1_price = Label(app1_canvas, image = price099)
    app1_price.place(x=115, y=300)

    def backtoroot():
        app1_window.destroy()

    backbutton = Button(app1_window, image = back_icon, command = backtoroot)
    backbutton.place(x=20, y=20)

###############################################################################

def app2_window():
    app2_window = Toplevel()
    app2_window.title('App Store')
    app2_window.minsize(1000, 600)
    app2_window.resizable(width = NO, height = NO)

    app2_line = read_apps[2]
    app2_info = app2_line.split(',')

    app2_canvas = Canvas(app2_window, width = 1000, height = 600, bg = 'white')
    app2_canvas.place(x=0, y=0)

    app2_largeIcon_pic = Label(app2_canvas, image = app2_largeIcon)
    app2_largeIcon_pic.place(x=100, y=60)

    app2_label = Label(app2_canvas, text = app2_info[3], font = 'Helvetica 30')
    app2_label.place(x=70, y=250)

    app2_scr1_pic = Label(app2_canvas, image = app2_scr1)
    app2_scr1_pic.place(x=450, y=30)

    app2_scr2_pic = Label(app2_canvas, image = app2_scr2)
    app2_scr2_pic.place(x=730, y= 30)

    app2_desc = Label(app2_canvas, font = 'Helvetica 24', text = app2_info[4], justify = LEFT)
    app2_desc.place(x=25, y=380)

    app2_desc2 = Label(app2_canvas, font = 'Helvetica 24', text = app2_info[5], justify = LEFT)
    app2_desc2.place(x=25, y=410)

    app2_desc3 = Label(app2_canvas, font = 'Helvetica 24', text = app2_info[6], justify = LEFT)
    app2_desc3.place(x=25, y=440)

    app2_desc4 = Label(app2_canvas, font = 'Helvetica 24', text = app2_info[7], justify = LEFT)
    app2_desc4.place(x=25, y=470)

    app2_desc5 = Label(app2_canvas, font = 'Helvetica 24', text = app2_info[8], justify = LEFT)
    app2_desc5.place(x=25, y=500)

    app2_size = Label(app2_canvas, font = 'Helvetica 24', text = 'App Size: '+app2_info[10])
    app2_size.place(x=25, y=540)
        
    app2_price = Label(app2_canvas, image = price420)
    app2_price.place(x=115, y=300)
    
    def backtoroot():
        app2_window.destroy()

    backbutton = Button(app2_window, image = back_icon, command = backtoroot)
    backbutton.place(x=20, y=20)


###############################################################################

def app3_window():
    app3_window = Toplevel()
    app3_window.title('App Store')
    app3_window.minsize(1000, 600)
    app3_window.resizable(width = NO, height = NO)

    app3_line = read_apps[3]
    app3_info = app3_line.split(',')

    app3_canvas = Canvas(app3_window, width = 1000, height = 600, bg = 'white')
    app3_canvas.place(x=0, y=0)

    app3_largeIcon_pic = Label(app3_canvas, image = app3_largeIcon)
    app3_largeIcon_pic.place(x=100, y=70)

    app3_label = Label(app3_canvas, text = app3_info[3], font = 'Helvetica 30')
    app3_label.place(x=50, y=250)

    app3_scr1_pic = Label(app3_canvas, image = app3_scr1)
    app3_scr1_pic.place(x=450, y=30)

    app3_scr2_pic = Label(app3_canvas, image = app3_scr2)
    app3_scr2_pic.place(x=700, y= 30)

    app3_desc = Label(app3_canvas, font = 'Helvetica 24', text = app3_info[4], justify = LEFT)
    app3_desc.place(x=25, y=380)

    app3_desc2 = Label(app3_canvas, font = 'Helvetica 24', text = app3_info[5], justify = LEFT)
    app3_desc2.place(x=25, y=410)

    app3_desc3 = Label(app3_canvas, font = 'Helvetica 24', text = app3_info[6], justify = LEFT)
    app3_desc3.place(x=25, y=440)

    app3_desc4 = Label(app3_canvas, font = 'Helvetica 24', text = app3_info[7], justify = LEFT)
    app3_desc4.place(x=25, y=470)

    app3_desc5 = Label(app3_canvas, font = 'Helvetica 24', text = app3_info[8], justify = LEFT)
    app3_desc5.place(x=25, y=500)

    app3_size = Label(app3_canvas, font = 'Helvetica 24', text = 'App Size: '+app3_info[10])
    app3_size.place(x=25, y=540)

    app3_price = Label(app3_canvas, image = price199)
    app3_price.place(x=115, y=300)

    def backtoroot():
        app3_window.destroy()

    backbutton = Button(app3_window, image = back_icon, command = backtoroot)
    backbutton.place(x=20, y=20)

###############################################################################

def app4_window():
    app4_window = Toplevel()
    app4_window.title('App Store')
    app4_window.minsize(1000, 600)
    app4_window.resizable(width = NO, height = NO)

    app4_line = read_apps[4]
    app4_info = app4_line.split(',')

    app4_canvas = Canvas(app4_window, width = 1000, height = 600, bg = 'white')
    app4_canvas.place(x=0, y=0)

    app4_largeIcon_pic = Label(app4_canvas, image = app4_largeIcon)
    app4_largeIcon_pic.place(x=100, y=70)

    app4_label = Label(app4_canvas, text = app4_info[3], font = 'Helvetica 30')
    app4_label.place(x=95, y=250)

    app4_scr1_pic = Label(app4_canvas, image = app4_scr1)
    app4_scr1_pic.place(x=450, y=30)

    app4_scr2_pic = Label(app4_canvas, image = app4_scr2)
    app4_scr2_pic.place(x=700, y= 30)

    app4_desc = Label(app4_canvas, font = 'Helvetica 24', text = app4_info[4], justify = LEFT)
    app4_desc.place(x=25, y=380)

    app4_desc2 = Label(app4_canvas, font = 'Helvetica 24', text = app4_info[5], justify = LEFT)
    app4_desc2.place(x=25, y=410)
    
    app4_desc3 = Label(app4_canvas, font = 'Helvetica 24', text = app4_info[6], justify = LEFT)
    app4_desc3.place(x=25, y=440)

    app4_desc4 = Label(app4_canvas, font = 'Helvetica 24', text = app4_info[7], justify = LEFT)
    app4_desc4.place(x=25, y=470)

    app4_desc5 = Label(app4_canvas, font = 'Helvetica 24', text = app4_info[8], justify = LEFT)
    app4_desc5.place(x=25, y=500)

    app4_size = Label(app4_canvas, font = 'Helvetica 24', text = 'App Size: '+app4_info[10])
    app4_size.place(x=25, y=540)

    app4_price = Label(app4_canvas, image = price199)
    app4_price.place(x=115, y=300)

    def backtoroot():
        app4_window.destroy()

    backbutton = Button(app4_window, image = back_icon, command = backtoroot)
    backbutton.place(x=20, y=20)

###############################################################################

def app5_window():
    app5_window = Toplevel()
    app5_window.title('App Store')
    app5_window.minsize(1000, 600)
    app5_window.resizable(width = NO, height = NO)

    app5_line = read_apps[5]
    app5_info = app5_line.split(',')

    app5_canvas = Canvas(app5_window, width = 1000, height = 600, bg = 'white')
    app5_canvas.place(x=0, y=0)

    app5_largeIcon_pic = Label(app5_canvas, image = app5_largeIcon)
    app5_largeIcon_pic.place(x=100, y=70)

    app5_label = Label(app5_canvas, text = app5_info[3], font = 'Helvetica 30')
    app5_label.place(x=85, y=250)

    app5_scr1_pic = Label(app5_canvas, image = app5_scr1)
    app5_scr1_pic.place(x=450, y=30)

    app5_scr2_pic = Label(app5_canvas, image = app5_scr2)
    app5_scr2_pic.place(x=700, y= 30)

    app5_desc = Label(app5_canvas, font = 'Helvetica 24', text = app5_info[4], justify = LEFT)
    app5_desc.place(x=25, y=380)

    app5_desc2 = Label(app5_canvas, font = 'Helvetica 24', text = app5_info[5], justify = LEFT)
    app5_desc2.place(x=25, y=410)

    app5_desc3 = Label(app5_canvas, font = 'Helvetica 24', text = app5_info[6], justify = LEFT)
    app5_desc3.place(x=25, y=440)

    app5_desc4 = Label(app5_canvas, font = 'Helvetica 24', text = app5_info[7], justify = LEFT)
    app5_desc4.place(x=25, y=470)

    app5_desc5 = Label(app5_canvas, font = 'Helvetica 24', text = app5_info[8], justify = LEFT)
    app5_desc5.place(x=25, y=500)

    app5_size = Label(app5_canvas, font = 'Helvetica 24', text = 'App Size: '+app5_info[10])
    app5_size.place(x=25, y=540)
    
    app5_price = Label(app5_canvas, image = price0)
    app5_price.place(x=115, y=300)

    def backtoroot():
        app5_window.destroy()

    backbutton = Button(app5_window, image = back_icon, command = backtoroot)
    backbutton.place(x=20, y=20)

###############################################################################

def app6_window():
    app6_window = Toplevel()
    app6_window.title('App Store')
    app6_window.minsize(1000, 600)
    app6_window.resizable(width = NO, height = NO)

    app6_line = read_apps[6]
    app6_info = app6_line.split(',')

    app6_canvas = Canvas(app6_window, width = 1000, height = 600, bg = 'white')
    app6_canvas.place(x=0, y=0)

    app6_largeIcon_pic = Label(app6_canvas, image = app6_largeIcon)
    app6_largeIcon_pic.place(x=100, y=70)

    app6_label = Label(app6_canvas, text = app6_info[3], font = 'Helvetica 30')
    app6_label.place(x=100, y=260)

    app6_scr1_pic = Label(app6_canvas, image = app6_scr1)
    app6_scr1_pic.place(x=450, y=30)

    app6_scr2_pic = Label(app6_canvas, image = app6_scr2)
    app6_scr2_pic.place(x=700, y= 30)

    app6_desc = Label(app6_canvas, font = 'Helvetica 24', text = app6_info[4], justify = LEFT)
    app6_desc.place(x=25, y=380)

    app6_desc2 = Label(app6_canvas, font = 'Helvetica 24', text = app6_info[5], justify = LEFT)
    app6_desc2.place(x=25, y=410)

    app6_desc3 = Label(app6_canvas, font = 'Helvetica 24', text = app6_info[6], justify = LEFT)
    app6_desc3.place(x=25, y=440)

    app6_desc4 = Label(app6_canvas, font = 'Helvetica 24', text = app6_info[7], justify = LEFT)
    app6_desc4.place(x=25, y=470)

    app6_desc5 = Label(app6_canvas, font = 'Helvetica 24', text = app6_info[8], justify = LEFT)
    app6_desc5.place(x=25, y=500)

    app6_size = Label(app6_canvas, font = 'Helvetica 24', text = 'App Size: '+app6_info[10])
    app6_size.place(x=25, y=540)

    app6_price = Label(app6_canvas, image = price0)
    app6_price.place(x=115, y=300)

    def backtoroot():
        app6_window.destroy()

    backbutton = Button(app6_window, image = back_icon, command = backtoroot)
    backbutton.place(x=20, y=20)

###############################################################################

def app7_window():
    app7_window = Toplevel()
    app7_window.title('App Store')
    app7_window.minsize(1000, 600)
    app7_window.resizable(width = NO, height = NO)

    app7_line = read_apps[7]
    app7_info = app7_line.split(',')

    app7_canvas = Canvas(app7_window, width = 1000, height = 600, bg = 'white')
    app7_canvas.place(x=0, y=0)

    app7_largeIcon_pic = Label(app7_canvas, image = app7_largeIcon)
    app7_largeIcon_pic.place(x=100, y=70)

    app7_label = Label(app7_canvas, text = app7_info[3], font = 'Helvetica 30')
    app7_label.place(x=140, y=250)

    app7_scr1_pic = Label(app7_canvas, image = app7_scr1)
    app7_scr1_pic.place(x=450, y=30)

    app7_scr2_pic = Label(app7_canvas, image = app7_scr2)
    app7_scr2_pic.place(x=700, y= 30)

    app7_desc = Label(app7_canvas, font = 'Helvetica 24', text = app7_info[4], justify = LEFT)
    app7_desc.place(x=25, y=380)

    app7_desc2 = Label(app7_canvas, font = 'Helvetica 24', text = app7_info[5], justify = LEFT)
    app7_desc2.place(x=25, y=410)

    app7_desc3 = Label(app7_canvas, font = 'Helvetica 24', text = app7_info[6], justify = LEFT)
    app7_desc3.place(x=25, y=440)

    app7_desc4 = Label(app7_canvas, font = 'Helvetica 24', text = app7_info[7], justify = LEFT)
    app7_desc4.place(x=25, y=470)

    app7_desc5 = Label(app7_canvas, font = 'Helvetica 24', text = app7_info[8], justify = LEFT)
    app7_desc5.place(x=25, y=500)

    app7_size = Label(app7_canvas, font = 'Helvetica 24', text = 'App Size: '+app7_info[10])
    app7_size.place(x=25, y=540)

    app7_price = Label(app7_canvas, image = price0)
    app7_price.place(x=115, y=300)

    def backtoroot():
        app7_window.destroy()

    backbutton = Button(app7_window, image = back_icon, command = backtoroot)
    backbutton.place(x=20, y=20)

###############################################################################

def app8_window():
    app8_window = Toplevel()
    app8_window.title('App Store')
    app8_window.minsize(1000, 600)
    app8_window.resizable(width = NO, height = NO)

    app8_line = read_apps[8]
    app8_info = app8_line.split(',')

    app8_canvas = Canvas(app8_window, width = 1000, height = 600, bg = 'white')
    app8_canvas.place(x=0, y=0)

    app8_largeIcon_pic = Label(app8_canvas, image = app8_largeIcon)
    app8_largeIcon_pic.place(x=100, y=70)

    app8_label = Label(app8_canvas, text = app8_info[3], font = 'Helvetica 30')
    app8_label.place(x=105, y=250)

    app8_scr1_pic = Label(app8_canvas, image = app8_scr1)
    app8_scr1_pic.place(x=450, y=30)

    app8_scr2_pic = Label(app8_canvas, image = app8_scr2)
    app8_scr2_pic.place(x=700, y= 30)
    
    app8_desc = Label(app8_canvas, font = 'Helvetica 24', text = app8_info[4], justify = LEFT)
    app8_desc.place(x=25, y=380)

    app8_desc2 = Label(app8_canvas, font = 'Helvetica 24', text = app8_info[5], justify = LEFT)
    app8_desc2.place(x=25, y=410)

    app8_desc3 = Label(app8_canvas, font = 'Helvetica 24', text = app8_info[6], justify = LEFT)
    app8_desc3.place(x=25, y=440)

    app8_desc4 = Label(app8_canvas, font = 'Helvetica 24', text = app8_info[7], justify = LEFT)
    app8_desc4.place(x=25, y=470)

    app8_desc5 = Label(app8_canvas, font = 'Helvetica 24', text = app8_info[8], justify = LEFT)
    app8_desc5.place(x=25, y=500)

    app8_size = Label(app8_canvas, font = 'Helvetica 24', text = 'App Size: '+app8_info[10])
    app8_size.place(x=25, y=540)

    app8_price = Label(app8_canvas, image = price0)
    app8_price.place(x=115, y=300)

    def backtoroot():
        app8_window.destroy()

    backbutton = Button(app8_window, image = back_icon, command = backtoroot)
    backbutton.place(x=20, y=20)

###############################################################################

###############################################################################

def game1_window():
    game1_window = Toplevel()
    game1_window.title('App Store')
    game1_window.minsize(1000, 600)
    game1_window.resizable(width = NO, height = NO)

    game1_line = read_games[1]
    game1_info = game1_line.split(',')

    game1_canvas = Canvas(game1_window, width = 1000, height = 600, bg = 'white')
    game1_canvas.place(x=0, y=0)

    game1_largeIcon_pic = Label(game1_canvas, image = game1_largeIcon)
    game1_largeIcon_pic.place(x=100, y=70)

    game1_label = Label(game1_canvas, text = game1_info[3], font = 'Helvetica 30')
    game1_label.place(x=133, y=250)

    game1_scr1_pic = Label(game1_canvas, image = game1_scr1)
    game1_scr1_pic.place(x=450, y=30)

    game1_scr2_pic = Label(game1_canvas, image = game1_scr2)
    game1_scr2_pic.place(x=730, y= 30)
    
    game1_desc = Label(game1_canvas, font = 'Helvetica 24', text = game1_info[4], justify = LEFT)
    game1_desc.place(x=25, y=380)

    game1_desc2 = Label(game1_canvas, font = 'Helvetica 24', text = game1_info[5], justify = LEFT)
    game1_desc2.place(x=25, y=410)

    game1_desc3 = Label(game1_canvas, font = 'Helvetica 24', text = game1_info[6], justify = LEFT)
    game1_desc3.place(x=25, y=440)

    game1_desc4 = Label(game1_canvas, font = 'Helvetica 24', text = game1_info[7], justify = LEFT)
    game1_desc4.place(x=25, y=470)

    game1_desc5 = Label(game1_canvas, font = 'Helvetica 24', text = game1_info[8], justify = LEFT)
    game1_desc5.place(x=25, y=500)

    game1_size = Label(game1_canvas, font = 'Helvetica 24', text = 'App Size: '+game1_info[10])
    game1_size.place(x=25, y=540)

    game1_price = Label(game1_canvas, image = price0)
    game1_price.place(x=115, y=300)

    def backtoroot():
        game1_window.destroy()

    backbutton = Button(game1_window, image = back_icon, command = backtoroot)
    backbutton.place(x=20, y=20)

###############################################################################

def game2_window():
    game2_window = Toplevel()
    game2_window.title('App Store')
    game2_window.minsize(1000, 600)
    game2_window.resizable(width = NO, height = NO)

    game2_line = read_games[2]
    game2_info = game2_line.split(',')

    game2_canvas = Canvas(game2_window, width = 1000, height = 600, bg = 'white')
    game2_canvas.place(x=0, y=0)

    game2_largeIcon_pic = Label(game2_canvas, image = game2_largeIcon)
    game2_largeIcon_pic.place(x=100, y=70)

    game2_label = Label(game2_canvas, text = game2_info[3], font = 'Helvetica 30')
    game2_label.place(x=95, y=250)

    game2_scr1_pic = Label(game2_canvas, image = game2_scr1)
    game2_scr1_pic.place(x=450, y=30)

    game2_scr2_pic = Label(game2_canvas, image = game2_scr2)
    game2_scr2_pic.place(x=730, y= 30)

    game2_desc = Label(game2_canvas, font = 'Helvetica 24', text = game2_info[4], justify = LEFT)
    game2_desc.place(x=25, y=380)

    game2_desc2 = Label(game2_canvas, font = 'Helvetica 24', text = game2_info[5], justify = LEFT)
    game2_desc2.place(x=25, y=410)

    game2_desc3 = Label(game2_canvas, font = 'Helvetica 24', text = game2_info[6], justify = LEFT)
    game2_desc3.place(x=25, y=440)

    game2_desc4 = Label(game2_canvas, font = 'Helvetica 24', text = game2_info[7], justify = LEFT)
    game2_desc4.place(x=25, y=470)

    game2_desc5 = Label(game2_canvas, font = 'Helvetica 24', text = game2_info[8], justify = LEFT)
    game2_desc5.place(x=25, y=500)

    game2_size = Label(game2_canvas, font = 'Helvetica 24', text = 'App Size: '+game2_info[10])
    game2_size.place(x=25, y=540)

    game2_price = Label(game2_canvas, image = price099)
    game2_price.place(x=115, y=300)

    def backtoroot():
        game2_window.destroy()

    backbutton = Button(game2_window, image = back_icon, command = backtoroot)
    backbutton.place(x=20, y=20)

###############################################################################

def game3_window():
    game3_window = Toplevel()
    game3_window.title('App Store')
    game3_window.minsize(1000, 600)
    game3_window.resizable(width = NO, height = NO)

    game3_line = read_games[3]
    game3_info = game3_line.split(',')

    game3_canvas = Canvas(game3_window, width = 1000, height = 600, bg = 'white')
    game3_canvas.place(x=0, y=0)

    game3_largeIcon_pic = Label(game3_canvas, image = game3_largeIcon)
    game3_largeIcon_pic.place(x=100, y=70)

    game3_label = Label(game3_canvas, text = game3_info[3], font = 'Helvetica 30')
    game3_label.place(x=135, y=260)

    game3_scr1_pic = Label(game3_canvas, image = game3_scr1)
    game3_scr1_pic.place(x=450, y=30)

    game3_scr2_pic = Label(game3_canvas, image = game3_scr2)
    game3_scr2_pic.place(x=730, y= 30)

    game3_desc = Label(game3_canvas, font = 'Helvetica 24', text = game3_info[4], justify = LEFT)
    game3_desc.place(x=25, y=380)

    game3_desc2 = Label(game3_canvas, font = 'Helvetica 24', text = game3_info[5], justify = LEFT)
    game3_desc2.place(x=25, y=410)

    game3_desc3 = Label(game3_canvas, font = 'Helvetica 24', text = game3_info[6], justify = LEFT)
    game3_desc3.place(x=25, y=440)

    game3_desc4 = Label(game3_canvas, font = 'Helvetica 24', text = game3_info[7], justify = LEFT)
    game3_desc4.place(x=25, y=470)

    game3_desc5 = Label(game3_canvas, font = 'Helvetica 24', text = game3_info[8], justify = LEFT)
    game3_desc5.place(x=25, y=500)

    game3_size = Label(game3_canvas, font = 'Helvetica 24', text = 'App Size: '+game3_info[10])
    game3_size.place(x=25, y=540)

    game3_price = Label(game3_canvas, image = price699)
    game3_price.place(x=115, y=300)

    def backtoroot():
        game3_window.destroy()
        
    backbutton = Button(game3_window, image = back_icon, command = backtoroot)
    backbutton.place(x=20, y=20)

###############################################################################

def game4_window():
    game4_window = Toplevel()
    game4_window.title('App Store')
    game4_window.minsize(1000, 600)
    game4_window.resizable(width = NO, height = NO)

    game4_line = read_games[4]
    game4_info = game4_line.split(',')

    game4_canvas = Canvas(game4_window, width = 1000, height = 600, bg = 'white')
    game4_canvas.place(x=0, y=0)

    game4_largeIcon_pic = Label(game4_canvas, image = game4_largeIcon)
    game4_largeIcon_pic.place(x=100, y=70)

    game4_label = Label(game4_canvas, text = game4_info[3], font = 'Helvetica 30')
    game4_label.place(x=85, y=260)

    game4_scr1_pic = Label(game4_canvas, image = game4_scr1)
    game4_scr1_pic.place(x=450, y=30)

    game4_scr2_pic = Label(game4_canvas, image = game4_scr2)
    game4_scr2_pic.place(x=730, y= 30)

    game4_desc = Label(game4_canvas, font = 'Helvetica 24', text = game4_info[4], justify = LEFT)
    game4_desc.place(x=25, y=380)

    game4_desc2 = Label(game4_canvas, font = 'Helvetica 24', text = game4_info[5], justify = LEFT)
    game4_desc2.place(x=25, y=410)

    game4_desc3 = Label(game4_canvas, font = 'Helvetica 24', text = game4_info[6], justify = LEFT)
    game4_desc3.place(x=25, y=440)

    game4_desc4 = Label(game4_canvas, font = 'Helvetica 24', text = game4_info[7], justify = LEFT)
    game4_desc4.place(x=25, y=470)

    game4_desc5 = Label(game4_canvas, font = 'Helvetica 24', text = game4_info[8], justify = LEFT)
    game4_desc5.place(x=25, y=500)

    game4_size = Label(game4_canvas, font = 'Helvetica 24', text = 'App Size: '+game4_info[10])
    game4_size.place(x=25, y=540)

    game4_price = Label(game4_canvas, image = price099)
    game4_price.place(x=115, y=300)
    
    def backtoroot():
            game4_window.destroy()

    backbutton = Button(game4_canvas, image = back_icon, command = backtoroot)
    backbutton.place(x=20,y=20)

###############################################################################

def game5_window():
    game5_window = Toplevel()
    game5_window.title('App Store')
    game5_window.minsize(1000, 600)
    game5_window.resizable(width = NO, height = NO)

    game5_line = read_games[5]
    game5_info = game5_line.split(',')

    game5_canvas = Canvas(game5_window, width = 1000, height = 600, bg = 'white')
    game5_canvas.place(x=0, y=0)

    game5_largeIcon_pic = Label(game5_canvas, image = game5_largeIcon)
    game5_largeIcon_pic.place(x=100, y=70)

    game5_label = Label(game5_canvas, text = game5_info[3], font = 'Helvetica 30')
    game5_label.place(x=70, y=260)

    game5_scr1_pic = Label(game5_canvas, image = game5_scr1)
    game5_scr1_pic.place(x=450, y=30)

    game5_scr2_pic = Label(game5_canvas, image = game5_scr2)
    game5_scr2_pic.place(x=730, y= 30)

    game5_desc = Label(game5_canvas, font = 'Helvetica 24', text = game5_info[4], justify = LEFT)
    game5_desc.place(x=25, y=380)

    game5_desc2 = Label(game5_canvas, font = 'Helvetica 24', text = game5_info[5], justify = LEFT)
    game5_desc2.place(x=25, y=410)

    game5_desc3 = Label(game5_canvas, font = 'Helvetica 24', text = game5_info[6], justify = LEFT)
    game5_desc3.place(x=25, y=440)

    game5_desc4 = Label(game5_canvas, font = 'Helvetica 24', text = game5_info[7], justify = LEFT)
    game5_desc4.place(x=25, y=470)

    game5_desc5 = Label(game5_canvas, font = 'Helvetica 24', text = game5_info[8], justify = LEFT)
    game5_desc5.place(x=25, y=500)

    game5_size = Label(game5_canvas, font = 'Helvetica 24', text = 'App Size: '+game5_info[10])
    game5_size.place(x=25, y=540)

    game5_price = Label(game5_canvas, image = price299)
    game5_price.place(x=115, y=300)

    def backtoroot():
            game5_window.destroy()

    backbutton = Button(game5_canvas, image = back_icon, command = backtoroot)
    backbutton.place(x=20,y=20)

###############################################################################

def game6_window():
    game6_window = Toplevel()
    game6_window.title('App Store')
    game6_window.minsize(1000, 600)
    game6_window.resizable(width = NO, height = NO)

    game6_line = read_games[6]
    game6_info = game6_line.split(',')

    game6_canvas = Canvas(game6_window, width = 1000, height = 600, bg = 'white')
    game6_canvas.place(x=0, y=0)

    game6_largeIcon_pic = Label(game6_canvas, image = game6_largeIcon)
    game6_largeIcon_pic.place(x=100, y=70)

    game6_label = Label(game6_canvas, text = game6_info[3], font = 'Helvetica 30')
    game6_label.place(x=90, y=260)

    game6_scr1_pic = Label(game6_canvas, image = game6_scr1)
    game6_scr1_pic.place(x=450, y=30)

    game6_scr2_pic = Label(game6_canvas, image = game6_scr2)
    game6_scr2_pic.place(x=730, y= 30)

    game6_desc = Label(game6_canvas, font = 'Helvetica 24', text = game6_info[4], justify = LEFT)
    game6_desc.place(x=25, y=380)

    game6_desc2 = Label(game6_canvas, font = 'Helvetica 24', text = game6_info[5], justify = LEFT)
    game6_desc2.place(x=25, y=410)

    game6_desc3 = Label(game6_canvas, font = 'Helvetica 24', text = game6_info[6], justify = LEFT)
    game6_desc3.place(x=25, y=440)

    game6_desc4 = Label(game6_canvas, font = 'Helvetica 24', text = game6_info[7], justify = LEFT)
    game6_desc4.place(x=25, y=470)

    game6_desc5 = Label(game6_canvas, font = 'Helvetica 24', text = game6_info[8], justify = LEFT)
    game6_desc5.place(x=25, y=500)

    game6_size = Label(game6_canvas, font = 'Helvetica 24', text = 'App Size: '+game6_info[10])
    game6_size.place(x=25, y=540)

    game6_price = Label(game6_canvas, image = price699)
    game6_price.place(x=115, y=300)

    def backtoroot():
            game6_window.destroy()

    backbutton = Button(game6_canvas, image = back_icon, command = backtoroot)
    backbutton.place(x=20,y=20)


###############################################################################

def game7_window():
    game7_window = Toplevel()
    game7_window.title('App Store')
    game7_window.minsize(1000, 600)
    game7_window.resizable(width = NO, height = NO)

    game7_line = read_games[7]
    game7_info = game7_line.split(',')

    game7_canvas = Canvas(game7_window, width = 1000, height = 600, bg = 'white')
    game7_canvas.place(x=0, y=0)

    game7_largeIcon_pic = Label(game7_canvas, image = game7_largeIcon)
    game7_largeIcon_pic.place(x=100, y=70)

    game7_label = Label(game7_canvas, text = game7_info[3], font = 'Helvetica 30')
    game7_label.place(x=100, y=260)

    game7_scr1_pic = Label(game7_canvas, image = game7_scr1)
    game7_scr1_pic.place(x=450, y=30)

    game7_scr2_pic = Label(game7_canvas, image = game7_scr2)
    game7_scr2_pic.place(x=730, y= 30)

    game7_desc = Label(game7_canvas, font = 'Helvetica 24', text = game7_info[4], justify = LEFT)
    game7_desc.place(x=25, y=380)

    game7_desc2 = Label(game7_canvas, font = 'Helvetica 24', text = game7_info[5], justify = LEFT)
    game7_desc2.place(x=25, y=410)

    game7_desc3 = Label(game7_canvas, font = 'Helvetica 24', text = game7_info[6], justify = LEFT)
    game7_desc3.place(x=25, y=440)

    game7_desc4 = Label(game7_canvas, font = 'Helvetica 24', text = game7_info[7], justify = LEFT)
    game7_desc4.place(x=25, y=470)

    game7_desc5 = Label(game7_canvas, font = 'Helvetica 24', text = game7_info[8], justify = LEFT)
    game7_desc5.place(x=25, y=500)

    game7_size = Label(game7_canvas, font = 'Helvetica 24', text = 'App Size: '+game7_info[10])
    game7_size.place(x=25, y=540)

    game7_price = Label(game7_canvas, image = price0)
    game7_price.place(x=115, y=300)

    def backtoroot():
            game7_window.destroy()

    backbutton = Button(game7_canvas, image = back_icon, command = backtoroot)
    backbutton.place(x=20,y=20)


###############################################################################

def game8_window():
    game8_window = Toplevel()
    game8_window.title('App Store')
    game8_window.minsize(1000, 600)
    game8_window.resizable(width = NO, height = NO)

    game8_line = read_games[8]
    game8_info = game8_line.split(',')

    game8_canvas = Canvas(game8_window, width = 1000, height = 600, bg = 'white')
    game8_canvas.place(x=0, y=0)

    game8_largeIcon_pic = Label(game8_canvas, image = game8_largeIcon)
    game8_largeIcon_pic.place(x=100, y=70)

    game8_label = Label(game8_canvas, text = game8_info[3], font = 'Helvetica 30')
    game8_label.place(x=130, y=260)

    game8_scr1_pic = Label(game8_canvas, image = game8_scr1)
    game8_scr1_pic.place(x=450, y=30)

    game8_scr2_pic = Label(game8_canvas, image = game8_scr2)
    game8_scr2_pic.place(x=730, y= 30)

    game8_desc = Label(game8_canvas, font = 'Helvetica 24', text = game8_info[4], justify = LEFT)
    game8_desc.place(x=25, y=380)

    game8_desc2 = Label(game8_canvas, font = 'Helvetica 24', text = game8_info[5], justify = LEFT)
    game8_desc2.place(x=25, y=410)

    game8_desc3 = Label(game8_canvas, font = 'Helvetica 24', text = game8_info[6], justify = LEFT)
    game8_desc3.place(x=25, y=440)

    game8_desc4 = Label(game8_canvas, font = 'Helvetica 24', text = game8_info[7], justify = LEFT)
    game8_desc4.place(x=25, y=470)

    game8_desc5 = Label(game8_canvas, font = 'Helvetica 24', text = game8_info[8], justify = LEFT)
    game8_desc5.place(x=25, y=500)

    game8_size = Label(game8_canvas, font = 'Helvetica 24', text = 'App Size: '+game8_info[10])
    game8_size.place(x=25, y=540)

    game8_price = Label(game8_canvas, image = price0)
    game8_price.place(x=115, y=300)

    def backtoroot():
            game8_window.destroy()

    backbutton = Button(game8_canvas, image = back_icon, command = backtoroot)
    backbutton.place(x=20,y=20)


###############################################################################

#funcion para asignar tecla 'Enter' a boton de busqueda
#E: tecla
#S: activar boton de busqueda
def return_key(key):
    searchWindow()

root.bind('<Return>', return_key)

#login and register labels
login_label = Label(root, text = 'Log In', font = 'Helvetica 20')
login_label.place(x=20, y=75)

register_label = Label(root, text = 'Sign Up', font = 'Helvetica 20')
register_label.place(x=90, y=75)

#other labels from homescreen
aotd_label = Label(root, text = 'Featured App', font = 'Helvetica 26')
aotd_label.place(x=250, y=105)

cat_label = Label(root, text = 'Categories', font = 'Helvetica 26')
cat_label.place(x=760, y=105)

games_label = Label(root, text = 'Games', font = 'Helvetica 26')
games_label.place(x=720, y=205)

apps_label = Label(root, text = 'Apps', font = 'Helvetica 26')
apps_label.place(x=730, y=320)

#labels from apps under the featured one
app2_label = Label(root, text = app2_info[3], font = 'Helvetica 16')
app2_label.place(x=30, y=530)

app2_pricelabel = Label(root, text = app2_info[9], font = 'Helvetica 16')
app2_pricelabel.place(x=70, y=550)

app3_label = Label(root, text = app3_info[3], font = 'Helvetica 16')
app3_label.place(x=220, y=530)

app3_pricelabel = Label(root, text = app3_info[9], font = 'Helvetica 16')
app3_pricelabel.place(x=275, y=550)

game1_label = Label(root, text = game1_info[3], font = 'Helvetica 16')
game1_label.place(x=465, y=530)

game1_pricelabel = Label(root, text = game1_info[9], font = 'Helvetica 16')
game1_pricelabel.place(x=475, y=550)

game2_label = Label(root, text = game2_info[3], font = 'Helvetica 16')
game2_label.place(x=650, y=530)

game2_pricelabel = Label(root, text = game2_info[9], font = 'Helvetica 16')
game2_pricelabel.place(x=675, y=550)

game3_label = Label(root, text = game3_info[3], font = 'Helvetica 16')
game3_label.place(x=870, y=530)

game3_pricelabel = Label(root, text = game3_info[9], font = 'Helvetica 16')
game3_pricelabel.place(x=875, y=550)

#App Buttons on homescreen
app1_ad_pic = Button(root, image = app1_ad, command = app1_window)
app1_ad_pic.place(x=0, y=150)

app2_pic = Button(root, image = app2_icon, command = app2_window)
app2_pic.place(x=40, y=420)

app3_pic = Button(root, image = app3_icon, command = app3_window)
app3_pic.place(x=240, y=420)

game1_pic = Button(root, image = game1_icon, command = game1_window)
game1_pic.place(x=440, y=420)

game2_pic = Button(root, image = game2_icon, command = game2_window)
game2_pic.place(x=640, y=420)

game3_pic = Button(root, image = game3_icon, command = game3_window)
game3_pic.place(x=840, y=420)

#category icons
games_icon_pic = Button(root, image = games_icon, command = games_menu)
games_icon_pic.place(x=840, y=165)

apps_icon_pic = Button(root, image = apps_icon, command = apps_menu)
apps_icon_pic.place(x=840, y=285)

#search system
search_label = Button(root, image = search_icon, command = searchWindow)
search_label.place(x=900,y=63)

search_entry = Entry(root, width = 20)
search_entry.place(x=720,y=70)

#login and register buttons
login_button = Button(root, image = login_icon, command = loginWindow)
login_button.place(x=20, y=10)

register_button = Button(root, image = register_icon, command = registerWindow)
register_button.place(x=100, y= 10)

root.mainloop()
