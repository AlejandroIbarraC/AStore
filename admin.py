from tkinter import *
import time
import os

#ventana principal
root = Tk()
root.title('Admin App')
root.minsize(1000, 600)
root.resizable(width = NO, height = NO)

#funcion para cargar imagenes
def loadPicture(name):
    route = os.path.join('images', name)
    photo = PhotoImage(file=route)
    return photo

#carga de imagenes
riddle = loadPicture('accessriddle.gif')
exiticon = loadPicture('exiticon.gif')
monitorsellericon = loadPicture('monitorsellericon.gif')
addsellericon = loadPicture('addsellericon.gif')
resetsellericon = loadPicture('resetsellericon.gif')

#funcion para verificar clave de login
def check_login():
    if key_entry.get() == '()':
        logged_window()
    else:
        fail_label = Label(root, text = 'WRONG', font = 'Helvetica 40', fg = 'red')
        fail_label.place(x=400, y=500)
        key_entry.delete(0, END)

#ventana principal de carga
def logged_window():
    root.withdraw()
    logged_window = Toplevel()
    logged_window.title('Admin App')
    logged_window.minsize(1000,600)
    logged_window.resizable(width=NO, height=NO)

    logged_canvas = Canvas(logged_window, width = 1000, height = 600)
    logged_canvas.place(x=0, y=0)

    welcome_label = Label(logged_canvas, text = 'Welcome, Admin', font = 'Helvetica 30')
    welcome_label.place(x=375,y=50)

    def register_window():
        register_window = Toplevel()
        register_window.title('Admin App')
        register_window.minsize(1000,600)
        register_window.resizable(width=NO, height=NO)

        register_canvas = Canvas(register_window, width = 1000, height = 600)
        register_canvas.place(x=0, y=0)

        #labels:
        title_label = Label(register_canvas, text = 'Add seller', font = 'Helvetica 28')
        title_label.place(x=400, y=50)

        name_label = Label(register_canvas, text = 'Name:', font = 'Helvetica 24')
        name_label.place(x=100, y=150)

        lastname_label = Label(register_canvas, text = 'Last Name:', font = 'Helvetica 24')
        lastname_label.place(x=100, y=225)

        email_label = Label(register_canvas, text = 'Email:', font = 'Helvetica 24')
        email_label.place(x=100, y=300)

        website_label =  Label(register_canvas, text = 'Website:', font = 'Helvetica 24')
        website_label.place(x=100, y= 375)
        
        #entries:
        name_entry = Entry(register_canvas, width = 20)
        name_entry.place(x=300, y=150)

        lastname_entry = Entry(register_canvas, width = 20)
        lastname_entry.place(x=300, y= 225)

        email_entry = Entry(register_canvas, width = 20)
        email_entry.place(x=300, y=300)

        website_entry = Entry(register_canvas, width = 20)
        website_entry.place(x=300, y=375)

        #funcion para agregar vendedor
        def add_seller():
                a = open ('sellercount.txt','r+')
                lastIndex = a.readlines()
                userid = lastIndex[len(lastIndex) - 1]
                name = name_entry.get()
                lastname = lastname_entry.get()
                email = email_entry.get()
                website = website_entry.get()
                b = open('sellers.txt','a')
                info = userid + ',' + name + ',' + lastname + ',' + email + ',' + website + ','  + '0' + ',' + ',' +  ',' +  ','  + ',' + ',' + '0' + ',' +  '0'
                b.write('\n' + str(info))
                a.write('\n' + str(int(userid) + 1))

        def back():
            register_window.destroy()

        back_button = Button(register_canvas, image = exiticon, command = back)
        back_button.place(x=25,y=25)
        
        register_button = Button(register_canvas, text = 'Add Seller', command = add_seller)
        register_button.place(x=330, y=475)

    #ventana para monitorear vendedores
    def monitor_window():
        monitor_window = Toplevel()
        monitor_window.title('Admin App')
        monitor_window.minsize(1000,600)
        monitor_window.resizable(width=NO, height=NO)

        info_label = Label(monitor_window, text = 'App Status: A = Active. I = Inactive', font = 'Helvetica 24', fg = 'firebrick3')
        info_label.place(x=320, y=30)

        def back():
            monitor_window.destroy()

        back_button = Button(monitor_window, image = exiticon, command = back)
        back_button.place(x=25,y=25)

        def seller1():
            seller1 = Toplevel()
            seller1.title('Admin App')
            seller1.minsize(1000,600)
            seller1.resizable(width=NO, height=NO)

            #leer apps y juegos de vendedor
            all_sellers = open('sellers.txt', 'r')
            read_sellers = all_sellers.readlines()
            seller1_line = read_sellers[1]
            seller1_info = seller1_line.split(',')
            
            apps = open('apps.txt', 'r')
            read_apps = apps.readlines()
            app1 = read_apps[1]
            app1_info = app1.split(',')

            apps_esp = open('apps_esp.txt', 'r')
            read_apps_esp = apps_esp.readlines()
            app1_esp = read_apps_esp[1]
            app1_esp_info = app1_esp.split(',')

            games = open('games.txt', 'r')
            read_games = games.readlines()
            game1 = read_games[1]
            game2 = read_games[7]
            game1_info = game1.split(',')
            game2_info = game2.split(',')

            games_esp = open('games_esp.txt', 'r')
            read_games_esp = games_esp.readlines()
            game1_esp = read_games_esp[1]
            game2_esp = read_games_esp[7]
            game1_esp_info = game1_esp.split(',')
            game2_esp_info = game2_esp.split(',')

            def back():
                seller1.destroy()

            back_button = Button(seller1, image = exiticon, command = back)
            back_button.place(x=25,y=25)

            #ventana de agregar app
            def add_app_window():
                add_app_window = Toplevel()
                add_app_window.title('Admin App')
                add_app_window.minsize(1000,600)
                add_app_window.resizable(width=NO, height=NO)

                def add_app():
                    #escribir nueva app en txt de juego en ingles y español
                    a = open ('appcount.txt','r+')
                    lastIndex = a.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    appname = name_entry.get()
                    desc1 = desc1_entry.get()
                    desc2 = desc2_entry.get()
                    desc3 = desc3_entry.get()
                    desc4 = desc4_entry.get()
                    desc5 = desc5_entry.get()
                    price = price_entry.get()
                    appsize = appsize_entry.get()
                    b = open('apps.txt','a')
                    info = '1' + ',' + productid + ',' + '0' + ',' + appname + ',' + desc1 + ',' + desc2 + ',' + desc3 + ',' + desc4 + ',' + desc5 + ',' + price + ',' + appsize + ',' + '0'
                    b.write('\n' + str(info))
                    a.close
                    b.close

                    c = open('appcount.txt','r+')
                    lastIndex = c.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    desc1_esp = desc1_esp_entry.get()
                    desc2_esp = desc2_esp_entry.get()
                    desc3_esp = desc3_esp_entry.get()
                    desc4_esp = desc4_esp_entry.get()
                    desc5_esp = desc5_esp_entry.get()
                    d = open('apps_esp.txt','a')
                    info = '1' + ',' + productid + ',' + '0' + ',' + appname + ',' + desc1_esp + ',' + desc2_esp + ',' + desc3_esp + ',' + desc4_esp + ',' + desc5_esp + ',' + price + ',' + appsize + ',' + '0'
                    d.write('\n' + str(info))
                    c.write('\n' + str(int(productid) + 1))
                    c.close
                    d.close

                    #leer informacion de cada vendedor
                    e = open('sellers.txt', 'r+')
                    read_seller_info = e.readlines()
                    seller1_line = read_seller_info[1]
                    seller1_info = seller1_line.split(',')
                    seller2_line = read_seller_info[2]
                    seller2_info = seller2_line.split(',')
                    seller3_line = read_seller_info[3]
                    seller3_info = seller3_line.split(',')
                    seller4_line = read_seller_info[4]
                    seller4_info = seller4_line.split(',')
                    seller5_line = read_seller_info[5]
                    seller5_info = seller5_line.split(',')
                    seller6_line = read_seller_info[6]
                    seller6_info = seller6_line.split(',')
                    seller7_line = read_seller_info[7]
                    seller7_info = seller7_line.split(',')
                    seller8_line = read_seller_info[8]
                    seller8_info = seller8_line.split(',')
                    seller9_line = read_seller_info[9]
                    seller9_info = seller9_line.split(',')
                    seller10_line = read_seller_info[10]
                    seller10_info = seller10_line.split(',')

                    #agregar nombre de app a info de vendedor en el espacio disponible (5 es el maximo) y sumar 1 al total de apps del vendedor
                    if seller1_info[6] == '':
                        seller1_info[6] = name_entry.get() + ' (I)'
                        seller1_info[5] = str(int(seller1_info[5]) + 1)
                    elif seller1_info[7] == '':
                        seller1_info[7] = name_entry.get() + ' (I)'
                        seller1_info[5] = str(int(seller1_info[5]) + 1)
                    elif seller1_info[8] == '':
                        seller1_info[8] = name_entry.get() + ' (I)'
                        seller1_info[5] = str(int(seller1_info[5]) + 1)
                    elif seller1_info[9] == '':
                        seller1_info[9] = name_entry.get() + ' (I)'
                        seller1_info[5] = str(int(seller1_info[5]) + 1)
                    elif seller1_info[10] == '':
                        seller1_info[10] = name_entry.get() + ' (I)'
                        seller1_info[5] = str(int(seller1_info[5]) + 1)
                    else:
                        print('You have challenged the Matrix')

                    #actualizar txt con nueva informacion de app
                    new_1 = seller1_info[0] + ',' + seller1_info[1] + ',' + seller1_info[2] + ',' + seller1_info[3] + ',' + seller1_info[4] + ',' + seller1_info[5] + ',' + seller1_info[6] + ',' + seller1_info[7] + ',' + seller1_info[8] + ',' + seller1_info[9] + ',' + seller1_info[10] + ',' + seller1_info[11] + ',' + seller1_info[12] 
                    new_2 = seller2_info[0] + ',' + seller2_info[1] + ',' + seller2_info[2] + ',' + seller2_info[3] + ',' + seller2_info[4] + ',' + seller2_info[5] + ',' + seller2_info[6] + ',' + seller2_info[7] + ',' + seller2_info[8] + ',' + seller2_info[9] + ',' + seller2_info[10] + ',' + seller2_info[11] + ',' + seller2_info[12] 
                    new_3 = seller3_info[0] + ',' + seller3_info[1] + ',' + seller3_info[2] + ',' + seller3_info[3] + ',' + seller3_info[4] + ',' + seller3_info[5] + ',' + seller3_info[6] + ',' + seller3_info[7] + ',' + seller3_info[8] + ',' + seller3_info[9] + ',' + seller3_info[10] + ',' + seller3_info[11] + ',' + seller3_info[12] 
                    new_4 = seller4_info[0] + ',' + seller4_info[1] + ',' + seller4_info[2] + ',' + seller4_info[3] + ',' + seller4_info[4] + ',' + seller4_info[5] + ',' + seller4_info[6] + ',' + seller4_info[7] + ',' + seller4_info[8] + ',' + seller4_info[9] + ',' + seller4_info[10] + ',' + seller4_info[11] + ',' + seller4_info[12] 
                    new_5 = seller5_info[0] + ',' + seller5_info[1] + ',' + seller5_info[2] + ',' + seller5_info[3] + ',' + seller5_info[4] + ',' + seller5_info[5] + ',' + seller5_info[6] + ',' + seller5_info[7] + ',' + seller5_info[8] + ',' + seller5_info[9] + ',' + seller5_info[10] + ',' + seller5_info[11] + ',' + seller5_info[12] 
                    new_6 = seller6_info[0] + ',' + seller6_info[1] + ',' + seller6_info[2] + ',' + seller6_info[3] + ',' + seller6_info[4] + ',' + seller6_info[5] + ',' + seller6_info[6] + ',' + seller6_info[7] + ',' + seller6_info[8] + ',' + seller6_info[9] + ',' + seller6_info[10] + ',' + seller6_info[11] + ',' + seller6_info[12] 
                    new_7 = seller7_info[0] + ',' + seller7_info[1] + ',' + seller7_info[2] + ',' + seller7_info[3] + ',' + seller7_info[4] + ',' + seller7_info[5] + ',' + seller7_info[6] + ',' + seller7_info[7] + ',' + seller7_info[8] + ',' + seller7_info[9] + ',' + seller7_info[10] + ',' + seller7_info[11] + ',' + seller7_info[12] 
                    new_8 = seller8_info[0] + ',' + seller8_info[1] + ',' + seller8_info[2] + ',' + seller8_info[3] + ',' + seller8_info[4] + ',' + seller8_info[5] + ',' + seller8_info[6] + ',' + seller8_info[7] + ',' + seller8_info[8] + ',' + seller8_info[9] + ',' + seller8_info[10] + ',' + seller8_info[11] + ',' + seller8_info[12]
                    new_9 = seller9_info[0] + ',' + seller9_info[1] + ',' + seller9_info[2] + ',' + seller9_info[3] + ',' + seller9_info[4] + ',' + seller9_info[5] + ',' + seller9_info[6] + ',' + seller9_info[7] + ',' + seller9_info[8] + ',' + seller9_info[9] + ',' + seller9_info[10] + ',' + seller9_info[11] + ',' + seller9_info[12] 
                    new_10 = seller10_info[0] + ',' + seller10_info[1] + ',' + seller10_info[2] + ',' + seller10_info[3] + ',' + seller10_info[4] + ',' + seller10_info[5] + ',' + seller10_info[6] + ',' + seller10_info[7] + ',' + seller10_info[8] + ',' + seller10_info[9] + ',' + seller10_info[10] + ',' + seller10_info[11] + ',' + seller10_info[12] 
                    f = open('sellers.txt', 'w')
                    g = f.close
                    h = open('sellers.txt', 'a')
                    write0 = h.write('#0-sellerid, 1-name, 2-lastname, 3-email, 4-website, 5-amountappsonsale, 6-app1, 7-app2, 8-app3, 9-app4, 10-app5, 11-downloadsUS, 12-downloadsCR' + '\n')
                    write1 = h.write(new_1)
                    write2 = h.write(new_2)
                    write3 = h.write(new_3)
                    write4 = h.write(new_4)
                    write5 = h.write(new_5)
                    write6 = h.write(new_6)
                    write7 = h.write(new_7)
                    write8 = h.write(new_8)
                    write9 = h.write(new_9)
                    write10 = h.write(new_10)
                    i = h.close

                    success_label = Label(add_app_window, text = 'Success', font = 'Helvetica 38', fg = 'firebrick3')
                    success_label.place(x=680, y=400)

                #labels para info de app que se quiera agregar
                appname_label = Label(add_app_window, text = 'App Name', font = 'Helvetica 24')
                appname_label.place(x=100, y=50)

                desc1_label = Label(add_app_window, text = 'Description 1', font = 'Helvetica 24')
                desc1_label.place(x=100, y=100)

                desc2_label = Label(add_app_window, text = 'Description 2', font = 'Helvetica 24')
                desc2_label.place(x=100, y=150)

                desc3_label = Label(add_app_window, text = 'Description 3', font = 'Helvetica 24')
                desc3_label.place(x=100, y=200)

                desc4_label = Label(add_app_window, text = 'Description 4', font = 'Helvetica 24')
                desc4_label.place(x=100, y=250)

                desc5_label = Label(add_app_window, text = 'Description 5', font = 'Helvetica 24')
                desc5_label.place(x=100, y=300)

                desc1_esp_label = Label(add_app_window, text = 'Description 1 in Spanish', font = 'Helvetica 24')
                desc1_esp_label.place(x=100, y=350)

                desc2_esp_label = Label(add_app_window, text = 'Description 2 in Spanish', font = 'Helvetica 24')
                desc2_esp_label.place(x=100, y=400)

                desc3_esp_label = Label(add_app_window, text = 'Description 3 in Spanish', font = 'Helvetica 24')
                desc3_esp_label.place(x=100, y=450)

                desc4_esp_label = Label(add_app_window, text = 'Description 4 in Spanish', font = 'Helvetica 24')
                desc4_esp_label.place(x=100, y=500)

                desc5_esp_label = Label(add_app_window, text = 'Description 5 in Spanish', font = 'Helvetica 24')
                desc5_esp_label.place(x=100, y=550)

                price_label = Label(add_app_window, text = 'Price ($) or "Free"', font = 'Helvetica 24')
                price_label.place(x=600, y=50)

                appsize_label  = Label(add_app_window, text = 'App Size', font = 'Helvetica 24')
                appsize_label.place(x=600, y=100)

                #entries
                name_entry = Entry(add_app_window, width = 20)
                name_entry.place(x=400, y=50)

                desc1_entry = Entry(add_app_window, width = 20)
                desc1_entry.place(x=400, y=100)

                desc2_entry = Entry(add_app_window, width = 20)
                desc2_entry.place(x=400, y=150)

                desc3_entry = Entry(add_app_window, width = 20)
                desc3_entry.place(x=400, y=200)

                desc4_entry = Entry(add_app_window, width = 20)
                desc4_entry.place(x=400, y=250)

                desc5_entry = Entry(add_app_window, width = 20)
                desc5_entry.place(x=400, y=300)

                desc1_esp_entry = Entry(add_app_window, width = 20)
                desc1_esp_entry.place(x=400, y=350)

                desc2_esp_entry = Entry(add_app_window, width = 20)
                desc2_esp_entry.place(x=400, y=400)

                desc3_esp_entry = Entry(add_app_window, width = 20)
                desc3_esp_entry.place(x=400, y=450)

                desc4_esp_entry = Entry(add_app_window, width = 20)
                desc4_esp_entry.place(x=400, y=500)

                desc5_esp_entry = Entry(add_app_window, width = 20)
                desc5_esp_entry.place(x=400, y=550)

                price_entry = Entry(add_app_window, width = 20)
                price_entry.place(x=800, y=50)

                appsize_entry  = Entry(add_app_window, width = 20)
                appsize_entry.place(x=800, y=100)

                add_app_button = Button(add_app_window, text = 'Add App', command = add_app)
                add_app_button.place(x=700, y=475)

                def back():
                    add_app_window.destroy()

                back_button = Button(add_app_window, image = exiticon, command = back)
                back_button.place(x=25,y=25)

            #ventana de agregar juego
            def add_game_window():
                add_game_window = Toplevel()
                add_game_window.title('Admin App')
                add_game_window.minsize(1000,600)
                add_game_window.resizable(width=NO, height=NO)

                #misma funcion que add_app de la ventana anterior pero para juego
                def add_app():
                    a = open ('appcount.txt','r+')
                    lastIndex = a.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    appname = name_entry.get()
                    desc1 = desc1_entry.get()
                    desc2 = desc2_entry.get()
                    desc3 = desc3_entry.get()
                    desc4 = desc4_entry.get()
                    desc5 = desc5_entry.get()
                    price = price_entry.get()
                    appsize = appsize_entry.get()
                    b = open('games.txt','a')
                    info = '1' + ',' + productid + ',' + '1' + ',' + appname + ',' + desc1 + ',' + desc2 + ',' + desc3 + ',' + desc4 + ',' + desc5 + ',' + price + ',' + appsize + ',' + '0'
                    b.write('\n' + str(info))
                    a.close
                    b.close

                    c = open('appcount.txt','r+')
                    lastIndex = c.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    desc1_esp = desc1_esp_entry.get()
                    desc2_esp = desc2_esp_entry.get()
                    desc3_esp = desc3_esp_entry.get()
                    desc4_esp = desc4_esp_entry.get()
                    desc5_esp = desc5_esp_entry.get()
                    d = open('games_esp.txt','a')
                    info = '1' + ',' + productid + ',' + '1' + ',' + appname + ',' + desc1_esp + ',' + desc2_esp + ',' + desc3_esp + ',' + desc4_esp + ',' + desc5_esp + ',' + price + ',' + appsize + ',' + '0'
                    d.write('\n' + str(info))
                    c.write('\n' + str(int(productid) + 1))
                    c.close
                    d.close

                    e = open('sellers.txt', 'r+')
                    read_seller_info = e.readlines()
                    seller1_line = read_seller_info[1]
                    seller1_info = seller1_line.split(',')
                    seller2_line = read_seller_info[2]
                    seller2_info = seller2_line.split(',')
                    seller3_line = read_seller_info[3]
                    seller3_info = seller3_line.split(',')
                    seller4_line = read_seller_info[4]
                    seller4_info = seller4_line.split(',')
                    seller5_line = read_seller_info[5]
                    seller5_info = seller5_line.split(',')
                    seller6_line = read_seller_info[6]
                    seller6_info = seller6_line.split(',')
                    seller7_line = read_seller_info[7]
                    seller7_info = seller7_line.split(',')
                    seller8_line = read_seller_info[8]
                    seller8_info = seller8_line.split(',')
                    seller9_line = read_seller_info[9]
                    seller9_info = seller9_line.split(',')
                    seller10_line = read_seller_info[10]
                    seller10_info = seller10_line.split(',')

                    if seller1_info[6] == '':
                        seller1_info[6] = name_entry.get() + ' (I)'
                        seller1_info[5] = str(int(seller1_info[5]) + 1)
                    elif seller1_info[7] == '':
                        seller1_info[7] = name_entry.get() + ' (I)'
                        seller1_info[5] = str(int(seller1_info[5]) + 1)
                    elif seller1_info[8] == '':
                        seller1_info[8] = name_entry.get() + ' (I)'
                        seller1_info[5] = str(int(seller1_info[5]) + 1)
                    elif seller1_info[9] == '':
                        seller1_info[9] = name_entry.get() + ' (I)'
                        seller1_info[5] = str(int(seller1_info[5]) + 1)
                    elif seller1_info[10] == '':
                        seller1_info[10] = name_entry.get() + ' (I)'
                        seller1_info[5] = str(int(seller1_info[5]) + 1)
                    else:
                        print('You have challenged the Matrix')
                    
                    new_1 = seller1_info[0] + ',' + seller1_info[1] + ',' + seller1_info[2] + ',' + seller1_info[3] + ',' + seller1_info[4] + ',' + seller1_info[5] + ',' + seller1_info[6] + ',' + seller1_info[7] + ',' + seller1_info[8] + ',' + seller1_info[9] + ',' + seller1_info[10] + ',' + seller1_info[11] + ',' + seller1_info[12] 
                    new_2 = seller2_info[0] + ',' + seller2_info[1] + ',' + seller2_info[2] + ',' + seller2_info[3] + ',' + seller2_info[4] + ',' + seller2_info[5] + ',' + seller2_info[6] + ',' + seller2_info[7] + ',' + seller2_info[8] + ',' + seller2_info[9] + ',' + seller2_info[10] + ',' + seller2_info[11] + ',' + seller2_info[12] 
                    new_3 = seller3_info[0] + ',' + seller3_info[1] + ',' + seller3_info[2] + ',' + seller3_info[3] + ',' + seller3_info[4] + ',' + seller3_info[5] + ',' + seller3_info[6] + ',' + seller3_info[7] + ',' + seller3_info[8] + ',' + seller3_info[9] + ',' + seller3_info[10] + ',' + seller3_info[11] + ',' + seller3_info[12] 
                    new_4 = seller4_info[0] + ',' + seller4_info[1] + ',' + seller4_info[2] + ',' + seller4_info[3] + ',' + seller4_info[4] + ',' + seller4_info[5] + ',' + seller4_info[6] + ',' + seller4_info[7] + ',' + seller4_info[8] + ',' + seller4_info[9] + ',' + seller4_info[10] + ',' + seller4_info[11] + ',' + seller4_info[12] 
                    new_5 = seller5_info[0] + ',' + seller5_info[1] + ',' + seller5_info[2] + ',' + seller5_info[3] + ',' + seller5_info[4] + ',' + seller5_info[5] + ',' + seller5_info[6] + ',' + seller5_info[7] + ',' + seller5_info[8] + ',' + seller5_info[9] + ',' + seller5_info[10] + ',' + seller5_info[11] + ',' + seller5_info[12] 
                    new_6 = seller6_info[0] + ',' + seller6_info[1] + ',' + seller6_info[2] + ',' + seller6_info[3] + ',' + seller6_info[4] + ',' + seller6_info[5] + ',' + seller6_info[6] + ',' + seller6_info[7] + ',' + seller6_info[8] + ',' + seller6_info[9] + ',' + seller6_info[10] + ',' + seller6_info[11] + ',' + seller6_info[12] 
                    new_7 = seller7_info[0] + ',' + seller7_info[1] + ',' + seller7_info[2] + ',' + seller7_info[3] + ',' + seller7_info[4] + ',' + seller7_info[5] + ',' + seller7_info[6] + ',' + seller7_info[7] + ',' + seller7_info[8] + ',' + seller7_info[9] + ',' + seller7_info[10] + ',' + seller7_info[11] + ',' + seller7_info[12] 
                    new_8 = seller8_info[0] + ',' + seller8_info[1] + ',' + seller8_info[2] + ',' + seller8_info[3] + ',' + seller8_info[4] + ',' + seller8_info[5] + ',' + seller8_info[6] + ',' + seller8_info[7] + ',' + seller8_info[8] + ',' + seller8_info[9] + ',' + seller8_info[10] + ',' + seller8_info[11] + ',' + seller8_info[12]
                    new_9 = seller9_info[0] + ',' + seller9_info[1] + ',' + seller9_info[2] + ',' + seller9_info[3] + ',' + seller9_info[4] + ',' + seller9_info[5] + ',' + seller9_info[6] + ',' + seller9_info[7] + ',' + seller9_info[8] + ',' + seller9_info[9] + ',' + seller9_info[10] + ',' + seller9_info[11] + ',' + seller9_info[12] 
                    new_10 = seller10_info[0] + ',' + seller10_info[1] + ',' + seller10_info[2] + ',' + seller10_info[3] + ',' + seller10_info[4] + ',' + seller10_info[5] + ',' + seller10_info[6] + ',' + seller10_info[7] + ',' + seller10_info[8] + ',' + seller10_info[9] + ',' + seller10_info[10] + ',' + seller10_info[11] + ',' + seller10_info[12] 
                    f = open('sellers.txt', 'w')
                    g = f.close
                    h = open('sellers.txt', 'a')
                    write0 = h.write('#0-sellerid, 1-name, 2-lastname, 3-email, 4-website, 5-amountappsonsale, 6-app1, 7-app2, 8-app3, 9-app4, 10-app5, 11-downloadsUS, 12-downloadsCR' + '\n')
                    write1 = h.write(new_1)
                    write2 = h.write(new_2)
                    write3 = h.write(new_3)
                    write4 = h.write(new_4)
                    write5 = h.write(new_5)
                    write6 = h.write(new_6)
                    write7 = h.write(new_7)
                    write8 = h.write(new_8)
                    write9 = h.write(new_9)
                    write10 = h.write(new_10)
                    i = h.close

                    success_label = Label(add_game_window, text = 'Success', font = 'Helvetica 38', fg = 'firebrick3')
                    success_label.place(x=680, y=400)

                #labels para info de app que se quiera agregar
                appname_label = Label(add_game_window, text = 'Game Name', font = 'Helvetica 24')
                appname_label.place(x=100, y=50)

                desc1_label = Label(add_game_window, text = 'Description 1', font = 'Helvetica 24')
                desc1_label.place(x=100, y=100)

                desc2_label = Label(add_game_window, text = 'Description 2', font = 'Helvetica 24')
                desc2_label.place(x=100, y=150)

                desc3_label = Label(add_game_window, text = 'Description 3', font = 'Helvetica 24')
                desc3_label.place(x=100, y=200)

                desc4_label = Label(add_game_window, text = 'Description 4', font = 'Helvetica 24')
                desc4_label.place(x=100, y=250)

                desc5_label = Label(add_game_window, text = 'Description 5', font = 'Helvetica 24')
                desc5_label.place(x=100, y=300)

                desc1_esp_label = Label(add_game_window, text = 'Description 1 in Spanish', font = 'Helvetica 24')
                desc1_esp_label.place(x=100, y=350)

                desc2_esp_label = Label(add_game_window, text = 'Description 2 in Spanish', font = 'Helvetica 24')
                desc2_esp_label.place(x=100, y=400)

                desc3_esp_label = Label(add_game_window, text = 'Description 3 in Spanish', font = 'Helvetica 24')
                desc3_esp_label.place(x=100, y=450)

                desc4_esp_label = Label(add_game_window, text = 'Description 4 in Spanish', font = 'Helvetica 24')
                desc4_esp_label.place(x=100, y=500)

                desc5_esp_label = Label(add_game_window, text = 'Description 5 in Spanish', font = 'Helvetica 24')
                desc5_esp_label.place(x=100, y=550)

                price_label = Label(add_game_window, text = 'Price ($) or "Free"', font = 'Helvetica 24')
                price_label.place(x=600, y=50)

                appsize_label  = Label(add_game_window, text = 'App Size', font = 'Helvetica 24')
                appsize_label.place(x=600, y=100)

                #entries
                name_entry = Entry(add_game_window, width = 20)
                name_entry.place(x=400, y=50)

                desc1_entry = Entry(add_game_window, width = 20)
                desc1_entry.place(x=400, y=100)

                desc2_entry = Entry(add_game_window, width = 20)
                desc2_entry.place(x=400, y=150)

                desc3_entry = Entry(add_game_window, width = 20)
                desc3_entry.place(x=400, y=200)

                desc4_entry = Entry(add_game_window, width = 20)
                desc4_entry.place(x=400, y=250)

                desc5_entry = Entry(add_game_window, width = 20)
                desc5_entry.place(x=400, y=300)

                desc1_esp_entry = Entry(add_game_window, width = 20)
                desc1_esp_entry.place(x=400, y=350)

                desc2_esp_entry = Entry(add_game_window, width = 20)
                desc2_esp_entry.place(x=400, y=400)

                desc3_esp_entry = Entry(add_game_window, width = 20)
                desc3_esp_entry.place(x=400, y=450)

                desc4_esp_entry = Entry(add_game_window, width = 20)
                desc4_esp_entry.place(x=400, y=500)

                desc5_esp_entry = Entry(add_game_window, width = 20)
                desc5_esp_entry.place(x=400, y=550)

                price_entry = Entry(add_game_window, width = 20)
                price_entry.place(x=800, y=50)

                appsize_entry  = Entry(add_game_window, width = 20)
                appsize_entry.place(x=800, y=100)

                add_app_button = Button(add_game_window, text = 'Add Game', command = add_app)
                add_app_button.place(x=700, y=475)

                def back():
                    add_game_window.destroy()

                back_button = Button(add_game_window, image = exiticon, command = back)
                back_button.place(x=25,y=25)
                
                
            #labels de informacion
            #nombre
            name = Label(seller1, text = seller1_info[1], font = 'Helvetica 24', fg = 'firebrick3')
            name.place(x=300, y=100)

            #apellido
            lastname = Label(seller1, text = seller1_info[2], font = 'Helvetica 24', fg = 'firebrick3')
            lastname.place(x=300, y=200)

            #email
            email = Label(seller1, text = seller1_info[3], font = 'Helvetica 24', fg = 'firebrick3')
            email.place(x=300, y=300)

            #sitio web
            website = Label(seller1, text = seller1_info[4], font = 'Helvetica 24', fg = 'firebrick3')
            website.place(x=300, y=400)

            #cantidad de apps de vendedor
            amount_apps = Label(seller1, text = seller1_info[5], font = 'Helvetica 24', fg = 'firebrick3')
            amount_apps.place(x=400, y=500)

            #info app 1
            app1 = Label(seller1, text = seller1_info[6], font = 'Helvetica 24', fg = 'firebrick3')
            app1.place(x=700, y=100)

            app1_downloads = Label(seller1, text = 'Downloads US: '+app1_info[11]+'Downloads CR: '+app1_esp_info[11], font = 'Helvetica 16')
            app1_downloads.place(x=600, y=140)

            app1_money_label = Label(seller1, text = '$ made:', font = 'Helvetica 16')
            app1_money_label.place(x=780, y=150)

            app1_money = Label(seller1, text = (int(app1_info[11]) + int(app1_esp_info[11])) * 0.99, fg = 'firebrick3', font = 'Helvetica 24')
            app1_money.place(x=860, y=145)

            #info app 2
            app2 = Label(seller1, text = seller1_info[7], font = 'Helvetica 24', fg = 'firebrick3')
            app2.place(x=700, y=200)

            app2_downloads = Label(seller1, text = 'Downloads US: '+game1_info[11]+'Downloads CR: '+game1_esp_info[11], font = 'Helvetica 16')
            app2_downloads.place(x=600, y=240)

            #info app 3
            app3 = Label(seller1, text = seller1_info[8], font = 'Helvetica 24', fg = 'firebrick3')
            app3.place(x=700, y=300)

            app3_downloads = Label(seller1, text = 'Downloads US: '+game2_info[11]+'Downloads CR: '+game2_esp_info[11], font = 'Helvetica 16')
            app3_downloads.place(x=600, y=340)

            #info app 4
            app4 = Label(seller1, text = seller1_info[9], font = 'Helvetica 24', fg = 'firebrick3')
            app4.place(x=700, y=400)
            
            app4_downloads = Label(seller1, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app4_downloads.place(x=600, y=440)

            #info app 5
            app5 = Label(seller1, text = seller1_info[10], font = 'Helvetica 24', fg = 'firebrick3')
            app5.place(x=700, y=500)

            app5_downloads = Label(seller1, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app5_downloads.place(x=600, y=540)

            #labels para indicar dato a mostrar
            name_label = Label(seller1, text  = 'Seller name:', font = 'Helvetica 24')
            name_label.place(x=100, y=100)

            lastname_label = Label(seller1, text = 'Last Name:', font = 'Helvetica 24')
            lastname_label.place(x=100, y=200)

            email_label = Label(seller1, text = 'Email:', font = 'Helvetica 24')
            email_label.place(x=100, y=300)

            website_label = Label(seller1, text = 'Website:', font = 'Helvetica 24')
            website_label.place(x=100, y=400)

            amount_apps_label = Label(seller1, text = 'Amount apps on sale', font = 'Helvetica 24')
            amount_apps_label.place(x=100, y=500)

            app1_label = Label(seller1, text = 'App 1', font = 'Helvetica 24')
            app1_label.place(x=600, y=100)

            app2_label = Label(seller1, text = 'App 2', font = 'Helvetica 24')
            app2_label.place(x=600, y=200)

            app3_label = Label(seller1, text = 'App 3', font = 'Helvetica 24')
            app3_label.place(x=600, y=300)

            app4_label = Label(seller1, text = 'App 4', font = 'Helvetica 24')
            app4_label.place(x=600, y=400)

            app5_label = Label(seller1, text = 'App 5', font = 'Helvetica 24')
            app5_label.place(x=600, y=500)

            #boton para agregar apps
            add_app_button = Button(seller1, text = 'Add app', font = 'Helvetica 24', command = add_app_window)
            add_app_button.place(x=650, y=50)

            add_game_button = Button(seller1, text = 'Add game', font = 'Helvetica 24', command = add_game_window)
            add_game_button.place(x=850, y=50)

        #misma estructura que vendedor 1
        def seller2():
            seller2 = Toplevel()
            seller2.title('Admin App')
            seller2.minsize(1000,600)
            seller2.resizable(width=NO, height=NO)

            all_sellers = open('sellers.txt', 'r')
            read_sellers = all_sellers.readlines()
            seller2_line = read_sellers[2]
            seller2_info = seller2_line.split(',')
            
            apps = open('apps.txt', 'r')
            read_apps = apps.readlines()
            app1 = read_apps[2]
            app1_info = app1.split(',')

            apps_esp = open('apps_esp.txt', 'r')
            read_apps_esp = apps_esp.readlines()
            app1_esp = read_apps_esp[2]
            app1_esp_info = app1_esp.split(',')

            games = open('games.txt', 'r')
            read_games = games.readlines()
            game1 = read_games[5]
            game1_info = game1.split(',')

            games_esp = open('games_esp.txt', 'r')
            read_games_esp = games_esp.readlines()
            game1_esp = read_games_esp[5]
            game1_esp_info = game1_esp.split(',')

            def back():
                seller2.destroy()

            back_button = Button(seller2, image = exiticon, command = back)
            back_button.place(x=25,y=25)

            def add_app_window():
                add_app_window = Toplevel()
                add_app_window.title('Admin App')
                add_app_window.minsize(1000,600)
                add_app_window.resizable(width=NO, height=NO)

                def add_app():
                    a = open ('appcount.txt','r+')
                    lastIndex = a.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    appname = name_entry.get()
                    desc1 = desc1_entry.get()
                    desc2 = desc2_entry.get()
                    desc3 = desc3_entry.get()
                    desc4 = desc4_entry.get()
                    desc5 = desc5_entry.get()
                    price = price_entry.get()
                    appsize = appsize_entry.get()
                    b = open('apps.txt','a')
                    info = '2' + ',' + productid + ',' + '0' + ',' + appname + ',' + desc1 + ',' + desc2 + ',' + desc3 + ',' + desc4 + ',' + desc5 + ',' + price + ',' + appsize + ',' + '0'
                    b.write('\n' + str(info))
                    a.close
                    b.close

                    c = open('appcount.txt','r+')
                    lastIndex = c.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    desc1_esp = desc1_esp_entry.get()
                    desc2_esp = desc2_esp_entry.get()
                    desc3_esp = desc3_esp_entry.get()
                    desc4_esp = desc4_esp_entry.get()
                    desc5_esp = desc5_esp_entry.get()
                    d = open('apps_esp.txt','a')
                    info = '2' + ',' + productid + ',' + '0' + ',' + appname + ',' + desc1_esp + ',' + desc2_esp + ',' + desc3_esp + ',' + desc4_esp + ',' + desc5_esp + ',' + price + ',' + appsize + ',' + '0'
                    d.write('\n' + str(info))
                    c.write('\n' + str(int(productid) + 1))
                    c.close
                    d.close

                    e = open('sellers.txt', 'r+')
                    read_seller_info = e.readlines()
                    seller1_line = read_seller_info[1]
                    seller1_info = seller1_line.split(',')
                    seller2_line = read_seller_info[2]
                    seller2_info = seller2_line.split(',')
                    seller3_line = read_seller_info[3]
                    seller3_info = seller3_line.split(',')
                    seller4_line = read_seller_info[4]
                    seller4_info = seller4_line.split(',')
                    seller5_line = read_seller_info[5]
                    seller5_info = seller5_line.split(',')
                    seller6_line = read_seller_info[6]
                    seller6_info = seller6_line.split(',')
                    seller7_line = read_seller_info[7]
                    seller7_info = seller7_line.split(',')
                    seller8_line = read_seller_info[8]
                    seller8_info = seller8_line.split(',')
                    seller9_line = read_seller_info[9]
                    seller9_info = seller9_line.split(',')
                    seller10_line = read_seller_info[10]
                    seller10_info = seller10_line.split(',')

                    if seller2_info[6] == '':
                        seller2_info[6] = name_entry.get() + ' (I)'
                        seller2_info[5] = str(int(seller2_info[5]) + 1)
                    elif seller2_info[7] == '':
                        seller2_info[7] = name_entry.get() + ' (I)'
                        seller2_info[5] = str(int(seller2_info[5]) + 1)
                    elif seller2_info[8] == '':
                        seller2_info[8] = name_entry.get() + ' (I)'
                        seller2_info[5] = str(int(seller2_info[5]) + 1)
                    elif seller2_info[9] == '':
                        seller2_info[9] = name_entry.get() + ' (I)'
                        seller2_info[5] = str(int(seller2_info[5]) + 1)
                    elif seller2_info[10] == '':
                        seller2_info[10] = name_entry.get() + ' (I)'
                        seller2_info[5] = str(int(seller2_info[5]) + 1)
                    else:
                        print('You have challenged the Matrix')
                    
                    new_1 = seller1_info[0] + ',' + seller1_info[1] + ',' + seller1_info[2] + ',' + seller1_info[3] + ',' + seller1_info[4] + ',' + seller1_info[5] + ',' + seller1_info[6] + ',' + seller1_info[7] + ',' + seller1_info[8] + ',' + seller1_info[9] + ',' + seller1_info[10] + ',' + seller1_info[11] + ',' + seller1_info[12] 
                    new_2 = seller2_info[0] + ',' + seller2_info[1] + ',' + seller2_info[2] + ',' + seller2_info[3] + ',' + seller2_info[4] + ',' + seller2_info[5] + ',' + seller2_info[6] + ',' + seller2_info[7] + ',' + seller2_info[8] + ',' + seller2_info[9] + ',' + seller2_info[10] + ',' + seller2_info[11] + ',' + seller2_info[12] 
                    new_3 = seller3_info[0] + ',' + seller3_info[1] + ',' + seller3_info[2] + ',' + seller3_info[3] + ',' + seller3_info[4] + ',' + seller3_info[5] + ',' + seller3_info[6] + ',' + seller3_info[7] + ',' + seller3_info[8] + ',' + seller3_info[9] + ',' + seller3_info[10] + ',' + seller3_info[11] + ',' + seller3_info[12] 
                    new_4 = seller4_info[0] + ',' + seller4_info[1] + ',' + seller4_info[2] + ',' + seller4_info[3] + ',' + seller4_info[4] + ',' + seller4_info[5] + ',' + seller4_info[6] + ',' + seller4_info[7] + ',' + seller4_info[8] + ',' + seller4_info[9] + ',' + seller4_info[10] + ',' + seller4_info[11] + ',' + seller4_info[12] 
                    new_5 = seller5_info[0] + ',' + seller5_info[1] + ',' + seller5_info[2] + ',' + seller5_info[3] + ',' + seller5_info[4] + ',' + seller5_info[5] + ',' + seller5_info[6] + ',' + seller5_info[7] + ',' + seller5_info[8] + ',' + seller5_info[9] + ',' + seller5_info[10] + ',' + seller5_info[11] + ',' + seller5_info[12] 
                    new_6 = seller6_info[0] + ',' + seller6_info[1] + ',' + seller6_info[2] + ',' + seller6_info[3] + ',' + seller6_info[4] + ',' + seller6_info[5] + ',' + seller6_info[6] + ',' + seller6_info[7] + ',' + seller6_info[8] + ',' + seller6_info[9] + ',' + seller6_info[10] + ',' + seller6_info[11] + ',' + seller6_info[12] 
                    new_7 = seller7_info[0] + ',' + seller7_info[1] + ',' + seller7_info[2] + ',' + seller7_info[3] + ',' + seller7_info[4] + ',' + seller7_info[5] + ',' + seller7_info[6] + ',' + seller7_info[7] + ',' + seller7_info[8] + ',' + seller7_info[9] + ',' + seller7_info[10] + ',' + seller7_info[11] + ',' + seller7_info[12] 
                    new_8 = seller8_info[0] + ',' + seller8_info[1] + ',' + seller8_info[2] + ',' + seller8_info[3] + ',' + seller8_info[4] + ',' + seller8_info[5] + ',' + seller8_info[6] + ',' + seller8_info[7] + ',' + seller8_info[8] + ',' + seller8_info[9] + ',' + seller8_info[10] + ',' + seller8_info[11] + ',' + seller8_info[12]
                    new_9 = seller9_info[0] + ',' + seller9_info[1] + ',' + seller9_info[2] + ',' + seller9_info[3] + ',' + seller9_info[4] + ',' + seller9_info[5] + ',' + seller9_info[6] + ',' + seller9_info[7] + ',' + seller9_info[8] + ',' + seller9_info[9] + ',' + seller9_info[10] + ',' + seller9_info[11] + ',' + seller9_info[12] 
                    new_10 = seller10_info[0] + ',' + seller10_info[1] + ',' + seller10_info[2] + ',' + seller10_info[3] + ',' + seller10_info[4] + ',' + seller10_info[5] + ',' + seller10_info[6] + ',' + seller10_info[7] + ',' + seller10_info[8] + ',' + seller10_info[9] + ',' + seller10_info[10] + ',' + seller10_info[11] + ',' + seller10_info[12] 
                    f = open('sellers.txt', 'w')
                    g = f.close
                    h = open('sellers.txt', 'a')
                    write0 = h.write('#0-sellerid, 1-name, 2-lastname, 3-email, 4-website, 5-amountappsonsale, 6-app1, 7-app2, 8-app3, 9-app4, 10-app5, 11-downloadsUS, 12-downloadsCR' + '\n')
                    write1 = h.write(new_1)
                    write2 = h.write(new_2)
                    write3 = h.write(new_3)
                    write4 = h.write(new_4)
                    write5 = h.write(new_5)
                    write6 = h.write(new_6)
                    write7 = h.write(new_7)
                    write8 = h.write(new_8)
                    write9 = h.write(new_9)
                    write10 = h.write(new_10)
                    i = h.close

                    success_label = Label(add_app_window, text = 'Success', font = 'Helvetica 38', fg = 'firebrick3')
                    success_label.place(x=680, y=400)

                #labels para info de app que se quiera agregar
                appname_label = Label(add_app_window, text = 'App Name', font = 'Helvetica 24')
                appname_label.place(x=100, y=50)

                desc1_label = Label(add_app_window, text = 'Description 1', font = 'Helvetica 24')
                desc1_label.place(x=100, y=100)

                desc2_label = Label(add_app_window, text = 'Description 2', font = 'Helvetica 24')
                desc2_label.place(x=100, y=150)

                desc3_label = Label(add_app_window, text = 'Description 3', font = 'Helvetica 24')
                desc3_label.place(x=100, y=200)

                desc4_label = Label(add_app_window, text = 'Description 4', font = 'Helvetica 24')
                desc4_label.place(x=100, y=250)

                desc5_label = Label(add_app_window, text = 'Description 5', font = 'Helvetica 24')
                desc5_label.place(x=100, y=300)

                desc1_esp_label = Label(add_app_window, text = 'Description 1 in Spanish', font = 'Helvetica 24')
                desc1_esp_label.place(x=100, y=350)

                desc2_esp_label = Label(add_app_window, text = 'Description 2 in Spanish', font = 'Helvetica 24')
                desc2_esp_label.place(x=100, y=400)

                desc3_esp_label = Label(add_app_window, text = 'Description 3 in Spanish', font = 'Helvetica 24')
                desc3_esp_label.place(x=100, y=450)

                desc4_esp_label = Label(add_app_window, text = 'Description 4 in Spanish', font = 'Helvetica 24')
                desc4_esp_label.place(x=100, y=500)

                desc5_esp_label = Label(add_app_window, text = 'Description 5 in Spanish', font = 'Helvetica 24')
                desc5_esp_label.place(x=100, y=550)

                price_label = Label(add_app_window, text = 'Price ($) or "Free"', font = 'Helvetica 24')
                price_label.place(x=600, y=50)

                appsize_label  = Label(add_app_window, text = 'App Size', font = 'Helvetica 24')
                appsize_label.place(x=600, y=100)

                #entries
                name_entry = Entry(add_app_window, width = 20)
                name_entry.place(x=400, y=50)

                desc1_entry = Entry(add_app_window, width = 20)
                desc1_entry.place(x=400, y=100)

                desc2_entry = Entry(add_app_window, width = 20)
                desc2_entry.place(x=400, y=150)

                desc3_entry = Entry(add_app_window, width = 20)
                desc3_entry.place(x=400, y=200)

                desc4_entry = Entry(add_app_window, width = 20)
                desc4_entry.place(x=400, y=250)

                desc5_entry = Entry(add_app_window, width = 20)
                desc5_entry.place(x=400, y=300)

                desc1_esp_entry = Entry(add_app_window, width = 20)
                desc1_esp_entry.place(x=400, y=350)

                desc2_esp_entry = Entry(add_app_window, width = 20)
                desc2_esp_entry.place(x=400, y=400)

                desc3_esp_entry = Entry(add_app_window, width = 20)
                desc3_esp_entry.place(x=400, y=450)

                desc4_esp_entry = Entry(add_app_window, width = 20)
                desc4_esp_entry.place(x=400, y=500)

                desc5_esp_entry = Entry(add_app_window, width = 20)
                desc5_esp_entry.place(x=400, y=550)

                price_entry = Entry(add_app_window, width = 20)
                price_entry.place(x=800, y=50)

                appsize_entry  = Entry(add_app_window, width = 20)
                appsize_entry.place(x=800, y=100)

                add_app_button = Button(add_app_window, text = 'Add App', command = add_app)
                add_app_button.place(x=700, y=475)

                def back():
                    add_app_window.destroy()

                back_button = Button(add_app_window, image = exiticon, command = back)
                back_button.place(x=25,y=25)

            def add_game_window():
                add_game_window = Toplevel()
                add_game_window.title('Admin App')
                add_game_window.minsize(1000,600)
                add_game_window.resizable(width=NO, height=NO)

                def add_app():
                    a = open ('appcount.txt','r+')
                    lastIndex = a.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    appname = name_entry.get()
                    desc1 = desc1_entry.get()
                    desc2 = desc2_entry.get()
                    desc3 = desc3_entry.get()
                    desc4 = desc4_entry.get()
                    desc5 = desc5_entry.get()
                    price = price_entry.get()
                    appsize = appsize_entry.get()
                    b = open('games.txt','a')
                    info = '2' + ',' + productid + ',' + '1' + ',' + appname + ',' + desc1 + ',' + desc2 + ',' + desc3 + ',' + desc4 + ',' + desc5 + ',' + price + ',' + appsize + ',' + '0'
                    b.write('\n' + str(info))
                    a.close
                    b.close

                    c = open('appcount.txt','r+')
                    lastIndex = c.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    desc1_esp = desc1_esp_entry.get()
                    desc2_esp = desc2_esp_entry.get()
                    desc3_esp = desc3_esp_entry.get()
                    desc4_esp = desc4_esp_entry.get()
                    desc5_esp = desc5_esp_entry.get()
                    d = open('games_esp.txt','a')
                    info = '2' + ',' + productid + ',' + '1' + ',' + appname + ',' + desc1_esp + ',' + desc2_esp + ',' + desc3_esp + ',' + desc4_esp + ',' + desc5_esp + ',' + price + ',' + appsize + ',' + '0'
                    d.write('\n' + str(info))
                    c.write('\n' + str(int(productid) + 1))
                    c.close
                    d.close

                    e = open('sellers.txt', 'r+')
                    read_seller_info = e.readlines()
                    seller1_line = read_seller_info[1]
                    seller1_info = seller1_line.split(',')
                    seller2_line = read_seller_info[2]
                    seller2_info = seller2_line.split(',')
                    seller3_line = read_seller_info[3]
                    seller3_info = seller3_line.split(',')
                    seller4_line = read_seller_info[4]
                    seller4_info = seller4_line.split(',')
                    seller5_line = read_seller_info[5]
                    seller5_info = seller5_line.split(',')
                    seller6_line = read_seller_info[6]
                    seller6_info = seller6_line.split(',')
                    seller7_line = read_seller_info[7]
                    seller7_info = seller7_line.split(',')
                    seller8_line = read_seller_info[8]
                    seller8_info = seller8_line.split(',')
                    seller9_line = read_seller_info[9]
                    seller9_info = seller9_line.split(',')
                    seller10_line = read_seller_info[10]
                    seller10_info = seller10_line.split(',')

                    if seller2_info[6] == '':
                        seller2_info[6] = name_entry.get() + ' (I)'
                        seller2_info[5] = str(int(seller2_info[5]) + 1)
                    elif seller2_info[7] == '':
                        seller2_info[7] = name_entry.get() + ' (I)'
                        seller2_info[5] = str(int(seller2_info[5]) + 1)
                    elif seller2_info[8] == '':
                        seller2_info[8] = name_entry.get() + ' (I)'
                        seller2_info[5] = str(int(seller2_info[5]) + 1)
                    elif seller2_info[9] == '':
                        seller2_info[9] = name_entry.get() + ' (I)'
                        seller2_info[5] = str(int(seller2_info[5]) + 1)
                    elif seller2_info[10] == '':
                        seller2_info[10] = name_entry.get() + ' (I)'
                        seller2_info[5] = str(int(seller2_info[5]) + 1)
                    else:
                        print('You have challenged the Matrix')
                    
                    new_1 = seller1_info[0] + ',' + seller1_info[1] + ',' + seller1_info[2] + ',' + seller1_info[3] + ',' + seller1_info[4] + ',' + seller1_info[5] + ',' + seller1_info[6] + ',' + seller1_info[7] + ',' + seller1_info[8] + ',' + seller1_info[9] + ',' + seller1_info[10] + ',' + seller1_info[11] + ',' + seller1_info[12] 
                    new_2 = seller2_info[0] + ',' + seller2_info[1] + ',' + seller2_info[2] + ',' + seller2_info[3] + ',' + seller2_info[4] + ',' + seller2_info[5] + ',' + seller2_info[6] + ',' + seller2_info[7] + ',' + seller2_info[8] + ',' + seller2_info[9] + ',' + seller2_info[10] + ',' + seller2_info[11] + ',' + seller2_info[12] 
                    new_3 = seller3_info[0] + ',' + seller3_info[1] + ',' + seller3_info[2] + ',' + seller3_info[3] + ',' + seller3_info[4] + ',' + seller3_info[5] + ',' + seller3_info[6] + ',' + seller3_info[7] + ',' + seller3_info[8] + ',' + seller3_info[9] + ',' + seller3_info[10] + ',' + seller3_info[11] + ',' + seller3_info[12] 
                    new_4 = seller4_info[0] + ',' + seller4_info[1] + ',' + seller4_info[2] + ',' + seller4_info[3] + ',' + seller4_info[4] + ',' + seller4_info[5] + ',' + seller4_info[6] + ',' + seller4_info[7] + ',' + seller4_info[8] + ',' + seller4_info[9] + ',' + seller4_info[10] + ',' + seller4_info[11] + ',' + seller4_info[12] 
                    new_5 = seller5_info[0] + ',' + seller5_info[1] + ',' + seller5_info[2] + ',' + seller5_info[3] + ',' + seller5_info[4] + ',' + seller5_info[5] + ',' + seller5_info[6] + ',' + seller5_info[7] + ',' + seller5_info[8] + ',' + seller5_info[9] + ',' + seller5_info[10] + ',' + seller5_info[11] + ',' + seller5_info[12] 
                    new_6 = seller6_info[0] + ',' + seller6_info[1] + ',' + seller6_info[2] + ',' + seller6_info[3] + ',' + seller6_info[4] + ',' + seller6_info[5] + ',' + seller6_info[6] + ',' + seller6_info[7] + ',' + seller6_info[8] + ',' + seller6_info[9] + ',' + seller6_info[10] + ',' + seller6_info[11] + ',' + seller6_info[12] 
                    new_7 = seller7_info[0] + ',' + seller7_info[1] + ',' + seller7_info[2] + ',' + seller7_info[3] + ',' + seller7_info[4] + ',' + seller7_info[5] + ',' + seller7_info[6] + ',' + seller7_info[7] + ',' + seller7_info[8] + ',' + seller7_info[9] + ',' + seller7_info[10] + ',' + seller7_info[11] + ',' + seller7_info[12] 
                    new_8 = seller8_info[0] + ',' + seller8_info[1] + ',' + seller8_info[2] + ',' + seller8_info[3] + ',' + seller8_info[4] + ',' + seller8_info[5] + ',' + seller8_info[6] + ',' + seller8_info[7] + ',' + seller8_info[8] + ',' + seller8_info[9] + ',' + seller8_info[10] + ',' + seller8_info[11] + ',' + seller8_info[12]
                    new_9 = seller9_info[0] + ',' + seller9_info[1] + ',' + seller9_info[2] + ',' + seller9_info[3] + ',' + seller9_info[4] + ',' + seller9_info[5] + ',' + seller9_info[6] + ',' + seller9_info[7] + ',' + seller9_info[8] + ',' + seller9_info[9] + ',' + seller9_info[10] + ',' + seller9_info[11] + ',' + seller9_info[12] 
                    new_10 = seller10_info[0] + ',' + seller10_info[1] + ',' + seller10_info[2] + ',' + seller10_info[3] + ',' + seller10_info[4] + ',' + seller10_info[5] + ',' + seller10_info[6] + ',' + seller10_info[7] + ',' + seller10_info[8] + ',' + seller10_info[9] + ',' + seller10_info[10] + ',' + seller10_info[11] + ',' + seller10_info[12] 
                    f = open('sellers.txt', 'w')
                    g = f.close
                    h = open('sellers.txt', 'a')
                    write0 = h.write('#0-sellerid, 1-name, 2-lastname, 3-email, 4-website, 5-amountappsonsale, 6-app1, 7-app2, 8-app3, 9-app4, 10-app5, 11-downloadsUS, 12-downloadsCR' + '\n')
                    write1 = h.write(new_1)
                    write2 = h.write(new_2)
                    write3 = h.write(new_3)
                    write4 = h.write(new_4)
                    write5 = h.write(new_5)
                    write6 = h.write(new_6)
                    write7 = h.write(new_7)
                    write8 = h.write(new_8)
                    write9 = h.write(new_9)
                    write10 = h.write(new_10)
                    i = h.close

                    success_label = Label(add_game_window, text = 'Success', font = 'Helvetica 38', fg = 'firebrick3')
                    success_label.place(x=680, y=400)

                #labels para info de app que se quiera agregar
                appname_label = Label(add_game_window, text = 'Game Name', font = 'Helvetica 24')
                appname_label.place(x=100, y=50)

                desc1_label = Label(add_game_window, text = 'Description 1', font = 'Helvetica 24')
                desc1_label.place(x=100, y=100)

                desc2_label = Label(add_game_window, text = 'Description 2', font = 'Helvetica 24')
                desc2_label.place(x=100, y=150)

                desc3_label = Label(add_game_window, text = 'Description 3', font = 'Helvetica 24')
                desc3_label.place(x=100, y=200)

                desc4_label = Label(add_game_window, text = 'Description 4', font = 'Helvetica 24')
                desc4_label.place(x=100, y=250)

                desc5_label = Label(add_game_window, text = 'Description 5', font = 'Helvetica 24')
                desc5_label.place(x=100, y=300)

                desc1_esp_label = Label(add_game_window, text = 'Description 1 in Spanish', font = 'Helvetica 24')
                desc1_esp_label.place(x=100, y=350)

                desc2_esp_label = Label(add_game_window, text = 'Description 2 in Spanish', font = 'Helvetica 24')
                desc2_esp_label.place(x=100, y=400)

                desc3_esp_label = Label(add_game_window, text = 'Description 3 in Spanish', font = 'Helvetica 24')
                desc3_esp_label.place(x=100, y=450)

                desc4_esp_label = Label(add_game_window, text = 'Description 4 in Spanish', font = 'Helvetica 24')
                desc4_esp_label.place(x=100, y=500)

                desc5_esp_label = Label(add_game_window, text = 'Description 5 in Spanish', font = 'Helvetica 24')
                desc5_esp_label.place(x=100, y=550)

                price_label = Label(add_game_window, text = 'Price ($) or "Free"', font = 'Helvetica 24')
                price_label.place(x=600, y=50)

                appsize_label  = Label(add_game_window, text = 'App Size', font = 'Helvetica 24')
                appsize_label.place(x=600, y=100)

                #entries
                name_entry = Entry(add_game_window, width = 20)
                name_entry.place(x=400, y=50)

                desc1_entry = Entry(add_game_window, width = 20)
                desc1_entry.place(x=400, y=100)

                desc2_entry = Entry(add_game_window, width = 20)
                desc2_entry.place(x=400, y=150)

                desc3_entry = Entry(add_game_window, width = 20)
                desc3_entry.place(x=400, y=200)

                desc4_entry = Entry(add_game_window, width = 20)
                desc4_entry.place(x=400, y=250)

                desc5_entry = Entry(add_game_window, width = 20)
                desc5_entry.place(x=400, y=300)

                desc1_esp_entry = Entry(add_game_window, width = 20)
                desc1_esp_entry.place(x=400, y=350)

                desc2_esp_entry = Entry(add_game_window, width = 20)
                desc2_esp_entry.place(x=400, y=400)

                desc3_esp_entry = Entry(add_game_window, width = 20)
                desc3_esp_entry.place(x=400, y=450)

                desc4_esp_entry = Entry(add_game_window, width = 20)
                desc4_esp_entry.place(x=400, y=500)

                desc5_esp_entry = Entry(add_game_window, width = 20)
                desc5_esp_entry.place(x=400, y=550)

                price_entry = Entry(add_game_window, width = 20)
                price_entry.place(x=800, y=50)

                appsize_entry  = Entry(add_game_window, width = 20)
                appsize_entry.place(x=800, y=100)

                add_app_button = Button(add_game_window, text = 'Add Game', command = add_app)
                add_app_button.place(x=700, y=475)

                def back():
                    add_game_window.destroy()

                back_button = Button(add_game_window, image = exiticon, command = back)
                back_button.place(x=25,y=25)
                
                
            #labels de informacion
            name = Label(seller2, text = seller2_info[1], font = 'Helvetica 24', fg = 'firebrick3')
            name.place(x=300, y=100)

            lastname = Label(seller2, text = seller2_info[2], font = 'Helvetica 24', fg = 'firebrick3')
            lastname.place(x=300, y=200)

            email = Label(seller2, text = seller2_info[3], font = 'Helvetica 24', fg = 'firebrick3')
            email.place(x=300, y=300)

            website = Label(seller2, text = seller2_info[4], font = 'Helvetica 24', fg = 'firebrick3')
            website.place(x=300, y=400)

            amount_apps = Label(seller2, text = seller2_info[5], font = 'Helvetica 24', fg = 'firebrick3')
            amount_apps.place(x=400, y=500)

            app1 = Label(seller2, text = seller2_info[6], font = 'Helvetica 24', fg = 'firebrick3')
            app1.place(x=700, y=100)

            app1_downloads = Label(seller2, text = 'Downloads US: '+app1_info[11]+'Downloads CR: '+app1_esp_info[11], font = 'Helvetica 16')
            app1_downloads.place(x=600, y=140)

            app1_money_label = Label(seller2, text = '$ made:', font = 'Helvetica 16')
            app1_money_label.place(x=780, y=150)

            app1_money = Label(seller2, text = (int(app1_info[11]) + int(app1_esp_info[11])) * 4.2, fg = 'firebrick3', font = 'Helvetica 24')
            app1_money.place(x=860, y=145)

            app2 = Label(seller2, text = seller2_info[7], font = 'Helvetica 24', fg = 'firebrick3')
            app2.place(x=700, y=200)
            
            app2_money_label = Label(seller2, text = '$ made:', font = 'Helvetica 16')
            app2_money_label.place(x=780, y=250)

            app2_money = Label(seller2, text = (int(app1_info[11]) + int(app1_esp_info[11])) * 2.99, fg = 'firebrick3', font = 'Helvetica 24')
            app2_money.place(x=860, y=245)

            app2_downloads = Label(seller2, text = 'Downloads US: '+game1_info[11]+'Downloads CR: '+game1_esp_info[11], font = 'Helvetica 16')
            app2_downloads.place(x=600, y=240)

            app3 = Label(seller2, text = seller2_info[8], font = 'Helvetica 24', fg = 'firebrick3')
            app3.place(x=700, y=300)

            app3_downloads = Label(seller2, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0'+'\n', font = 'Helvetica 16')
            app3_downloads.place(x=600, y=340)

            app4 = Label(seller2, text = seller2_info[9], font = 'Helvetica 24', fg = 'firebrick3')
            app4.place(x=700, y=400)
            
            app4_downloads = Label(seller2, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app4_downloads.place(x=600, y=440)

            app5 = Label(seller2, text = seller2_info[10], font = 'Helvetica 24', fg = 'firebrick3')
            app5.place(x=700, y=500)

            app5_downloads = Label(seller2, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app5_downloads.place(x=600, y=540)

            name_label = Label(seller2, text  = 'Seller name:', font = 'Helvetica 24')
            name_label.place(x=100, y=100)

            lastname_label = Label(seller2, text = 'Last Name:', font = 'Helvetica 24')
            lastname_label.place(x=100, y=200)

            email_label = Label(seller2, text = 'Email:', font = 'Helvetica 24')
            email_label.place(x=100, y=300)

            website_label = Label(seller2, text = 'Website:', font = 'Helvetica 24')
            website_label.place(x=100, y=400)

            amount_apps_label = Label(seller2, text = 'Amount apps on sale', font = 'Helvetica 24')
            amount_apps_label.place(x=100, y=500)

            app1_label = Label(seller2, text = 'App 1', font = 'Helvetica 24')
            app1_label.place(x=600, y=100)

            app2_label = Label(seller2, text = 'App 2', font = 'Helvetica 24')
            app2_label.place(x=600, y=200)

            app3_label = Label(seller2, text = 'App 3', font = 'Helvetica 24')
            app3_label.place(x=600, y=300)

            app4_label = Label(seller2, text = 'App 4', font = 'Helvetica 24')
            app4_label.place(x=600, y=400)

            app5_label = Label(seller2, text = 'App 5', font = 'Helvetica 24')
            app5_label.place(x=600, y=500)

            #boton para agregar apps
            add_app_button = Button(seller2, text = 'Add app', font = 'Helvetica 24', command = add_app_window)
            add_app_button.place(x=650, y=50)

            add_game_button = Button(seller2, text = 'Add game', font = 'Helvetica 24', command = add_game_window)
            add_game_button.place(x=850, y=50)

        #misma estructura que vendedor 1
        def seller3():
            seller3 = Toplevel()
            seller3.title('Admin App')
            seller3.minsize(1000,600)
            seller3.resizable(width=NO, height=NO)

            sellercanvas = Canvas(seller3, width = 1000, height = 600)
            sellercanvas.place(x=0,y=0)

            all_sellers = open('sellers.txt', 'r')
            read_sellers = all_sellers.readlines()
            seller3_line = read_sellers[3]
            seller3_info = seller3_line.split(',')
            
            apps = open('apps.txt', 'r')
            read_apps = apps.readlines()
            app1 = read_apps[3]
            app1_info = app1.split(',')
            app2 = read_apps[4]
            app2_info = app2.split(',')
            app3 = read_apps[8]
            app3_info = app2.split(',')

            apps_esp = open('apps_esp.txt', 'r')
            read_apps_esp = apps_esp.readlines()
            app1_esp = read_apps_esp[3]
            app1_esp_info = app1_esp.split(',')
            app2_esp = read_apps_esp[4]
            app2_esp_info = app2_esp.split(',')
            app3_esp = read_apps_esp[8]
            app3_esp_info = app3_esp.split(',')

            games = open('games.txt', 'r')
            read_games = games.readlines()
            game1 = read_games[4]
            game1_info = game1.split(',')

            games_esp = open('games_esp.txt', 'r')
            read_games_esp = games_esp.readlines()
            game1_esp = read_games_esp[4]
            game1_esp_info = game1_esp.split(',')

            def back():
                seller3.destroy()

            back_button = Button(seller3, image = exiticon, command = back)
            back_button.place(x=25,y=25)

            def add_app_window():
                add_app_window = Toplevel()
                add_app_window.title('Admin App')
                add_app_window.minsize(1000,600)
                add_app_window.resizable(width=NO, height=NO)

                def add_app():
                    a = open ('appcount.txt','r+')
                    lastIndex = a.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    appname = name_entry.get()
                    desc1 = desc1_entry.get()
                    desc2 = desc2_entry.get()
                    desc3 = desc3_entry.get()
                    desc4 = desc4_entry.get()
                    desc5 = desc5_entry.get()
                    price = price_entry.get()
                    appsize = appsize_entry.get()
                    b = open('apps.txt','a')
                    info = '3' + ',' + productid + ',' + '0' + ',' + appname + ',' + desc1 + ',' + desc2 + ',' + desc3 + ',' + desc4 + ',' + desc5 + ',' + price + ',' + appsize + ',' + '0'
                    b.write('\n' + str(info))
                    a.close
                    b.close

                    c = open('appcount.txt','r+')
                    lastIndex = c.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    desc1_esp = desc1_esp_entry.get()
                    desc2_esp = desc2_esp_entry.get()
                    desc3_esp = desc3_esp_entry.get()
                    desc4_esp = desc4_esp_entry.get()
                    desc5_esp = desc5_esp_entry.get()
                    d = open('apps_esp.txt','a')
                    info = '3' + ',' + productid + ',' + '0' + ',' + appname + ',' + desc1_esp + ',' + desc2_esp + ',' + desc3_esp + ',' + desc4_esp + ',' + desc5_esp + ',' + price + ',' + appsize + ',' + '0'
                    d.write('\n' + str(info))
                    c.write('\n' + str(int(productid) + 1))
                    c.close
                    d.close

                    e = open('sellers.txt', 'r+')
                    read_seller_info = e.readlines()
                    seller1_line = read_seller_info[1]
                    seller1_info = seller1_line.split(',')
                    seller2_line = read_seller_info[2]
                    seller2_info = seller2_line.split(',')
                    seller3_line = read_seller_info[3]
                    seller3_info = seller3_line.split(',')
                    seller4_line = read_seller_info[4]
                    seller4_info = seller4_line.split(',')
                    seller5_line = read_seller_info[5]
                    seller5_info = seller5_line.split(',')
                    seller6_line = read_seller_info[6]
                    seller6_info = seller6_line.split(',')
                    seller7_line = read_seller_info[7]
                    seller7_info = seller7_line.split(',')
                    seller8_line = read_seller_info[8]
                    seller8_info = seller8_line.split(',')
                    seller9_line = read_seller_info[9]
                    seller9_info = seller9_line.split(',')
                    seller10_line = read_seller_info[10]
                    seller10_info = seller10_line.split(',')

                    if seller3_info[6] == '':
                        seller3_info[6] = name_entry.get() + ' (I)'
                        seller3_info[5] = str(int(seller3_info[5]) + 1)
                    elif seller3_info[7] == '':
                        seller3_info[7] = name_entry.get() + ' (I)'
                        seller3_info[5] = str(int(seller3_info[5]) + 1)
                    elif seller3_info[8] == '':
                        seller3_info[8] = name_entry.get() + ' (I)'
                        seller3_info[5] = str(int(seller3_info[5]) + 1)
                    elif seller3_info[9] == '':
                        seller3_info[9] = name_entry.get() + ' (I)'
                        seller3_info[5] = str(int(seller3_info[5]) + 1)
                    elif seller3_info[10] == '':
                        seller3_info[10] = name_entry.get() + ' (I)'
                        seller3_info[5] = str(int(seller3_info[5]) + 1)
                    else:
                        print('You have challenged the Matrix')
                    
                    new_1 = seller1_info[0] + ',' + seller1_info[1] + ',' + seller1_info[2] + ',' + seller1_info[3] + ',' + seller1_info[4] + ',' + seller1_info[5] + ',' + seller1_info[6] + ',' + seller1_info[7] + ',' + seller1_info[8] + ',' + seller1_info[9] + ',' + seller1_info[10] + ',' + seller1_info[11] + ',' + seller1_info[12] 
                    new_2 = seller2_info[0] + ',' + seller2_info[1] + ',' + seller2_info[2] + ',' + seller2_info[3] + ',' + seller2_info[4] + ',' + seller2_info[5] + ',' + seller2_info[6] + ',' + seller2_info[7] + ',' + seller2_info[8] + ',' + seller2_info[9] + ',' + seller2_info[10] + ',' + seller2_info[11] + ',' + seller2_info[12] 
                    new_3 = seller3_info[0] + ',' + seller3_info[1] + ',' + seller3_info[2] + ',' + seller3_info[3] + ',' + seller3_info[4] + ',' + seller3_info[5] + ',' + seller3_info[6] + ',' + seller3_info[7] + ',' + seller3_info[8] + ',' + seller3_info[9] + ',' + seller3_info[10] + ',' + seller3_info[11] + ',' + seller3_info[12] 
                    new_4 = seller4_info[0] + ',' + seller4_info[1] + ',' + seller4_info[2] + ',' + seller4_info[3] + ',' + seller4_info[4] + ',' + seller4_info[5] + ',' + seller4_info[6] + ',' + seller4_info[7] + ',' + seller4_info[8] + ',' + seller4_info[9] + ',' + seller4_info[10] + ',' + seller4_info[11] + ',' + seller4_info[12] 
                    new_5 = seller5_info[0] + ',' + seller5_info[1] + ',' + seller5_info[2] + ',' + seller5_info[3] + ',' + seller5_info[4] + ',' + seller5_info[5] + ',' + seller5_info[6] + ',' + seller5_info[7] + ',' + seller5_info[8] + ',' + seller5_info[9] + ',' + seller5_info[10] + ',' + seller5_info[11] + ',' + seller5_info[12] 
                    new_6 = seller6_info[0] + ',' + seller6_info[1] + ',' + seller6_info[2] + ',' + seller6_info[3] + ',' + seller6_info[4] + ',' + seller6_info[5] + ',' + seller6_info[6] + ',' + seller6_info[7] + ',' + seller6_info[8] + ',' + seller6_info[9] + ',' + seller6_info[10] + ',' + seller6_info[11] + ',' + seller6_info[12] 
                    new_7 = seller7_info[0] + ',' + seller7_info[1] + ',' + seller7_info[2] + ',' + seller7_info[3] + ',' + seller7_info[4] + ',' + seller7_info[5] + ',' + seller7_info[6] + ',' + seller7_info[7] + ',' + seller7_info[8] + ',' + seller7_info[9] + ',' + seller7_info[10] + ',' + seller7_info[11] + ',' + seller7_info[12] 
                    new_8 = seller8_info[0] + ',' + seller8_info[1] + ',' + seller8_info[2] + ',' + seller8_info[3] + ',' + seller8_info[4] + ',' + seller8_info[5] + ',' + seller8_info[6] + ',' + seller8_info[7] + ',' + seller8_info[8] + ',' + seller8_info[9] + ',' + seller8_info[10] + ',' + seller8_info[11] + ',' + seller8_info[12]
                    new_9 = seller9_info[0] + ',' + seller9_info[1] + ',' + seller9_info[2] + ',' + seller9_info[3] + ',' + seller9_info[4] + ',' + seller9_info[5] + ',' + seller9_info[6] + ',' + seller9_info[7] + ',' + seller9_info[8] + ',' + seller9_info[9] + ',' + seller9_info[10] + ',' + seller9_info[11] + ',' + seller9_info[12] 
                    new_10 = seller10_info[0] + ',' + seller10_info[1] + ',' + seller10_info[2] + ',' + seller10_info[3] + ',' + seller10_info[4] + ',' + seller10_info[5] + ',' + seller10_info[6] + ',' + seller10_info[7] + ',' + seller10_info[8] + ',' + seller10_info[9] + ',' + seller10_info[10] + ',' + seller10_info[11] + ',' + seller10_info[12] 
                    f = open('sellers.txt', 'w')
                    g = f.close
                    h = open('sellers.txt', 'a')
                    write0 = h.write('#0-sellerid, 1-name, 2-lastname, 3-email, 4-website, 5-amountappsonsale, 6-app1, 7-app2, 8-app3, 9-app4, 10-app5, 11-downloadsUS, 12-downloadsCR' + '\n')
                    write1 = h.write(new_1)
                    write2 = h.write(new_2)
                    write3 = h.write(new_3)
                    write4 = h.write(new_4)
                    write5 = h.write(new_5)
                    write6 = h.write(new_6)
                    write7 = h.write(new_7)
                    write8 = h.write(new_8)
                    write9 = h.write(new_9)
                    write10 = h.write(new_10)
                    i = h.close

                    success_label = Label(add_app_window, text = 'Success', font = 'Helvetica 38', fg = 'firebrick3')
                    success_label.place(x=680, y=400)

                #labels para info de app que se quiera agregar
                appname_label = Label(add_app_window, text = 'App Name', font = 'Helvetica 24')
                appname_label.place(x=100, y=50)

                desc1_label = Label(add_app_window, text = 'Description 1', font = 'Helvetica 24')
                desc1_label.place(x=100, y=100)

                desc2_label = Label(add_app_window, text = 'Description 2', font = 'Helvetica 24')
                desc2_label.place(x=100, y=150)

                desc3_label = Label(add_app_window, text = 'Description 3', font = 'Helvetica 24')
                desc3_label.place(x=100, y=200)

                desc4_label = Label(add_app_window, text = 'Description 4', font = 'Helvetica 24')
                desc4_label.place(x=100, y=250)

                desc5_label = Label(add_app_window, text = 'Description 5', font = 'Helvetica 24')
                desc5_label.place(x=100, y=300)

                desc1_esp_label = Label(add_app_window, text = 'Description 1 in Spanish', font = 'Helvetica 24')
                desc1_esp_label.place(x=100, y=350)

                desc2_esp_label = Label(add_app_window, text = 'Description 2 in Spanish', font = 'Helvetica 24')
                desc2_esp_label.place(x=100, y=400)

                desc3_esp_label = Label(add_app_window, text = 'Description 3 in Spanish', font = 'Helvetica 24')
                desc3_esp_label.place(x=100, y=450)

                desc4_esp_label = Label(add_app_window, text = 'Description 4 in Spanish', font = 'Helvetica 24')
                desc4_esp_label.place(x=100, y=500)

                desc5_esp_label = Label(add_app_window, text = 'Description 5 in Spanish', font = 'Helvetica 24')
                desc5_esp_label.place(x=100, y=550)

                price_label = Label(add_app_window, text = 'Price ($) or "Free"', font = 'Helvetica 24')
                price_label.place(x=600, y=50)

                appsize_label  = Label(add_app_window, text = 'App Size', font = 'Helvetica 24')
                appsize_label.place(x=600, y=100)

                #entries
                name_entry = Entry(add_app_window, width = 20)
                name_entry.place(x=400, y=50)

                desc1_entry = Entry(add_app_window, width = 20)
                desc1_entry.place(x=400, y=100)

                desc2_entry = Entry(add_app_window, width = 20)
                desc2_entry.place(x=400, y=150)

                desc3_entry = Entry(add_app_window, width = 20)
                desc3_entry.place(x=400, y=200)

                desc4_entry = Entry(add_app_window, width = 20)
                desc4_entry.place(x=400, y=250)

                desc5_entry = Entry(add_app_window, width = 20)
                desc5_entry.place(x=400, y=300)

                desc1_esp_entry = Entry(add_app_window, width = 20)
                desc1_esp_entry.place(x=400, y=350)

                desc2_esp_entry = Entry(add_app_window, width = 20)
                desc2_esp_entry.place(x=400, y=400)

                desc3_esp_entry = Entry(add_app_window, width = 20)
                desc3_esp_entry.place(x=400, y=450)

                desc4_esp_entry = Entry(add_app_window, width = 20)
                desc4_esp_entry.place(x=400, y=500)

                desc5_esp_entry = Entry(add_app_window, width = 20)
                desc5_esp_entry.place(x=400, y=550)

                price_entry = Entry(add_app_window, width = 20)
                price_entry.place(x=800, y=50)

                appsize_entry  = Entry(add_app_window, width = 20)
                appsize_entry.place(x=800, y=100)

                add_app_button = Button(add_app_window, text = 'Add App', command = add_app)
                add_app_button.place(x=700, y=475)

                def back():
                    add_app_window.destroy()

                back_button = Button(add_app_window, image = exiticon, command = back)
                back_button.place(x=25,y=25)

            def add_game_window():
                add_game_window = Toplevel()
                add_game_window.title('Admin App')
                add_game_window.minsize(1000,600)
                add_game_window.resizable(width=NO, height=NO)

                def add_app():
                    a = open ('appcount.txt','r+')
                    lastIndex = a.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    appname = name_entry.get()
                    desc1 = desc1_entry.get()
                    desc2 = desc2_entry.get()
                    desc3 = desc3_entry.get()
                    desc4 = desc4_entry.get()
                    desc5 = desc5_entry.get()
                    price = price_entry.get()
                    appsize = appsize_entry.get()
                    b = open('games.txt','a')
                    info = '3' + ',' + productid + ',' + '1' + ',' + appname + ',' + desc1 + ',' + desc2 + ',' + desc3 + ',' + desc4 + ',' + desc5 + ',' + price + ',' + appsize + ',' + '0'
                    b.write('\n' + str(info))
                    a.close
                    b.close

                    c = open('appcount.txt','r+')
                    lastIndex = c.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    desc1_esp = desc1_esp_entry.get()
                    desc2_esp = desc2_esp_entry.get()
                    desc3_esp = desc3_esp_entry.get()
                    desc4_esp = desc4_esp_entry.get()
                    desc5_esp = desc5_esp_entry.get()
                    d = open('games_esp.txt','a')
                    info = '3' + ',' + productid + ',' + '1' + ',' + appname + ',' + desc1_esp + ',' + desc2_esp + ',' + desc3_esp + ',' + desc4_esp + ',' + desc5_esp + ',' + price + ',' + appsize + ',' + '0'
                    d.write('\n' + str(info))
                    c.write('\n' + str(int(productid) + 1))
                    c.close
                    d.close

                    e = open('sellers.txt', 'r+')
                    read_seller_info = e.readlines()
                    seller1_line = read_seller_info[1]
                    seller1_info = seller1_line.split(',')
                    seller2_line = read_seller_info[2]
                    seller2_info = seller2_line.split(',')
                    seller3_line = read_seller_info[3]
                    seller3_info = seller3_line.split(',')
                    seller4_line = read_seller_info[4]
                    seller4_info = seller4_line.split(',')
                    seller5_line = read_seller_info[5]
                    seller5_info = seller5_line.split(',')
                    seller6_line = read_seller_info[6]
                    seller6_info = seller6_line.split(',')
                    seller7_line = read_seller_info[7]
                    seller7_info = seller7_line.split(',')
                    seller8_line = read_seller_info[8]
                    seller8_info = seller8_line.split(',')
                    seller9_line = read_seller_info[9]
                    seller9_info = seller9_line.split(',')
                    seller10_line = read_seller_info[10]
                    seller10_info = seller10_line.split(',')

                    if seller3_info[6] == '':
                        seller3_info[6] = name_entry.get() + ' (I)'
                        seller3_info[5] = str(int(seller3_info[5]) + 1)
                    elif seller3_info[7] == '':
                        seller3_info[7] = name_entry.get() + ' (I)'
                        seller3_info[5] = str(int(seller3_info[5]) + 1)
                    elif seller3_info[8] == '':
                        seller3_info[8] = name_entry.get() + ' (I)'
                        seller3_info[5] = str(int(seller3_info[5]) + 1)
                    elif seller3_info[9] == '':
                        seller3_info[9] = name_entry.get() + ' (I)'
                        seller3_info[5] = str(int(seller3_info[5]) + 1)
                    elif seller3_info[10] == '':
                        seller3_info[10] = name_entry.get() + ' (I)'
                        seller3_info[5] = str(int(seller3_info[5]) + 1)
                    else:
                        print('You have challenged the Matrix')
                    
                    new_1 = seller1_info[0] + ',' + seller1_info[1] + ',' + seller1_info[2] + ',' + seller1_info[3] + ',' + seller1_info[4] + ',' + seller1_info[5] + ',' + seller1_info[6] + ',' + seller1_info[7] + ',' + seller1_info[8] + ',' + seller1_info[9] + ',' + seller1_info[10] + ',' + seller1_info[11] + ',' + seller1_info[12] 
                    new_2 = seller2_info[0] + ',' + seller2_info[1] + ',' + seller2_info[2] + ',' + seller2_info[3] + ',' + seller2_info[4] + ',' + seller2_info[5] + ',' + seller2_info[6] + ',' + seller2_info[7] + ',' + seller2_info[8] + ',' + seller2_info[9] + ',' + seller2_info[10] + ',' + seller2_info[11] + ',' + seller2_info[12] 
                    new_3 = seller3_info[0] + ',' + seller3_info[1] + ',' + seller3_info[2] + ',' + seller3_info[3] + ',' + seller3_info[4] + ',' + seller3_info[5] + ',' + seller3_info[6] + ',' + seller3_info[7] + ',' + seller3_info[8] + ',' + seller3_info[9] + ',' + seller3_info[10] + ',' + seller3_info[11] + ',' + seller3_info[12] 
                    new_4 = seller4_info[0] + ',' + seller4_info[1] + ',' + seller4_info[2] + ',' + seller4_info[3] + ',' + seller4_info[4] + ',' + seller4_info[5] + ',' + seller4_info[6] + ',' + seller4_info[7] + ',' + seller4_info[8] + ',' + seller4_info[9] + ',' + seller4_info[10] + ',' + seller4_info[11] + ',' + seller4_info[12] 
                    new_5 = seller5_info[0] + ',' + seller5_info[1] + ',' + seller5_info[2] + ',' + seller5_info[3] + ',' + seller5_info[4] + ',' + seller5_info[5] + ',' + seller5_info[6] + ',' + seller5_info[7] + ',' + seller5_info[8] + ',' + seller5_info[9] + ',' + seller5_info[10] + ',' + seller5_info[11] + ',' + seller5_info[12] 
                    new_6 = seller6_info[0] + ',' + seller6_info[1] + ',' + seller6_info[2] + ',' + seller6_info[3] + ',' + seller6_info[4] + ',' + seller6_info[5] + ',' + seller6_info[6] + ',' + seller6_info[7] + ',' + seller6_info[8] + ',' + seller6_info[9] + ',' + seller6_info[10] + ',' + seller6_info[11] + ',' + seller6_info[12] 
                    new_7 = seller7_info[0] + ',' + seller7_info[1] + ',' + seller7_info[2] + ',' + seller7_info[3] + ',' + seller7_info[4] + ',' + seller7_info[5] + ',' + seller7_info[6] + ',' + seller7_info[7] + ',' + seller7_info[8] + ',' + seller7_info[9] + ',' + seller7_info[10] + ',' + seller7_info[11] + ',' + seller7_info[12] 
                    new_8 = seller8_info[0] + ',' + seller8_info[1] + ',' + seller8_info[2] + ',' + seller8_info[3] + ',' + seller8_info[4] + ',' + seller8_info[5] + ',' + seller8_info[6] + ',' + seller8_info[7] + ',' + seller8_info[8] + ',' + seller8_info[9] + ',' + seller8_info[10] + ',' + seller8_info[11] + ',' + seller8_info[12]
                    new_9 = seller9_info[0] + ',' + seller9_info[1] + ',' + seller9_info[2] + ',' + seller9_info[3] + ',' + seller9_info[4] + ',' + seller9_info[5] + ',' + seller9_info[6] + ',' + seller9_info[7] + ',' + seller9_info[8] + ',' + seller9_info[9] + ',' + seller9_info[10] + ',' + seller9_info[11] + ',' + seller9_info[12] 
                    new_10 = seller10_info[0] + ',' + seller10_info[1] + ',' + seller10_info[2] + ',' + seller10_info[3] + ',' + seller10_info[4] + ',' + seller10_info[5] + ',' + seller10_info[6] + ',' + seller10_info[7] + ',' + seller10_info[8] + ',' + seller10_info[9] + ',' + seller10_info[10] + ',' + seller10_info[11] + ',' + seller10_info[12] 
                    f = open('sellers.txt', 'w')
                    g = f.close
                    h = open('sellers.txt', 'a')
                    write0 = h.write('#0-sellerid, 1-name, 2-lastname, 3-email, 4-website, 5-amountappsonsale, 6-app1, 7-app2, 8-app3, 9-app4, 10-app5, 11-downloadsUS, 12-downloadsCR' + '\n')
                    write1 = h.write(new_1)
                    write2 = h.write(new_2)
                    write3 = h.write(new_3)
                    write4 = h.write(new_4)
                    write5 = h.write(new_5)
                    write6 = h.write(new_6)
                    write7 = h.write(new_7)
                    write8 = h.write(new_8)
                    write9 = h.write(new_9)
                    write10 = h.write(new_10)
                    i = h.close

                    success_label = Label(add_game_window, text = 'Success', font = 'Helvetica 38', fg = 'firebrick3')
                    success_label.place(x=680, y=400)

                #labels para info de app que se quiera agregar
                appname_label = Label(add_game_window, text = 'Game Name', font = 'Helvetica 24')
                appname_label.place(x=100, y=50)

                desc1_label = Label(add_game_window, text = 'Description 1', font = 'Helvetica 24')
                desc1_label.place(x=100, y=100)

                desc2_label = Label(add_game_window, text = 'Description 2', font = 'Helvetica 24')
                desc2_label.place(x=100, y=150)

                desc3_label = Label(add_game_window, text = 'Description 3', font = 'Helvetica 24')
                desc3_label.place(x=100, y=200)

                desc4_label = Label(add_game_window, text = 'Description 4', font = 'Helvetica 24')
                desc4_label.place(x=100, y=250)

                desc5_label = Label(add_game_window, text = 'Description 5', font = 'Helvetica 24')
                desc5_label.place(x=100, y=300)

                desc1_esp_label = Label(add_game_window, text = 'Description 1 in Spanish', font = 'Helvetica 24')
                desc1_esp_label.place(x=100, y=350)

                desc2_esp_label = Label(add_game_window, text = 'Description 2 in Spanish', font = 'Helvetica 24')
                desc2_esp_label.place(x=100, y=400)

                desc3_esp_label = Label(add_game_window, text = 'Description 3 in Spanish', font = 'Helvetica 24')
                desc3_esp_label.place(x=100, y=450)

                desc4_esp_label = Label(add_game_window, text = 'Description 4 in Spanish', font = 'Helvetica 24')
                desc4_esp_label.place(x=100, y=500)

                desc5_esp_label = Label(add_game_window, text = 'Description 5 in Spanish', font = 'Helvetica 24')
                desc5_esp_label.place(x=100, y=550)

                price_label = Label(add_game_window, text = 'Price ($) or "Free"', font = 'Helvetica 24')
                price_label.place(x=600, y=50)

                appsize_label  = Label(add_game_window, text = 'App Size', font = 'Helvetica 24')
                appsize_label.place(x=600, y=100)

                #entries
                name_entry = Entry(add_game_window, width = 20)
                name_entry.place(x=400, y=50)

                desc1_entry = Entry(add_game_window, width = 20)
                desc1_entry.place(x=400, y=100)

                desc2_entry = Entry(add_game_window, width = 20)
                desc2_entry.place(x=400, y=150)

                desc3_entry = Entry(add_game_window, width = 20)
                desc3_entry.place(x=400, y=200)

                desc4_entry = Entry(add_game_window, width = 20)
                desc4_entry.place(x=400, y=250)

                desc5_entry = Entry(add_game_window, width = 20)
                desc5_entry.place(x=400, y=300)

                desc1_esp_entry = Entry(add_game_window, width = 20)
                desc1_esp_entry.place(x=400, y=350)

                desc2_esp_entry = Entry(add_game_window, width = 20)
                desc2_esp_entry.place(x=400, y=400)

                desc3_esp_entry = Entry(add_game_window, width = 20)
                desc3_esp_entry.place(x=400, y=450)

                desc4_esp_entry = Entry(add_game_window, width = 20)
                desc4_esp_entry.place(x=400, y=500)

                desc5_esp_entry = Entry(add_game_window, width = 20)
                desc5_esp_entry.place(x=400, y=550)

                price_entry = Entry(add_game_window, width = 20)
                price_entry.place(x=800, y=50)

                appsize_entry  = Entry(add_game_window, width = 20)
                appsize_entry.place(x=800, y=100)

                add_app_button = Button(add_game_window, text = 'Add Game', command = add_app)
                add_app_button.place(x=700, y=475)

                def back():
                    add_game_window.destroy()

                back_button = Button(add_game_window, image = exiticon, command = back)
                back_button.place(x=25,y=25)
                
                
            #labels de informacion
            name = Label(sellercanvas, text = seller3_info[1], font = 'Helvetica 24', fg = 'firebrick3')
            name.place(x=300, y=100)

            lastname = Label(sellercanvas, text = seller3_info[2], font = 'Helvetica 24', fg = 'firebrick3')
            lastname.place(x=300, y=200)

            email = Label(sellercanvas, text = seller3_info[3], font = 'Helvetica 24', fg = 'firebrick3')
            email.place(x=300, y=300)

            website = Label(sellercanvas, text = seller3_info[4], font = 'Helvetica 24', fg = 'firebrick3')
            website.place(x=300, y=400)

            amount_apps = Label(sellercanvas, text = seller3_info[5], font = 'Helvetica 24', fg = 'firebrick3')
            amount_apps.place(x=400, y=500)

            app1 = Label(sellercanvas, text = seller3_info[6], font = 'Helvetica 24', fg = 'firebrick3')
            app1.place(x=700, y=100)

            app1_downloads = Label(sellercanvas, text = 'Downloads US: '+app1_info[11]+'Downloads CR: '+app1_esp_info[11], font = 'Helvetica 16')
            app1_downloads.place(x=600, y=140)

            app1_money_label = Label(sellercanvas, text = '$ made:', font = 'Helvetica 16')
            app1_money_label.place(x=780, y=150)

            app1_money = Label(sellercanvas, text = (int(app1_info[11]) + int(app1_esp_info[11])) * 1.99, fg = 'firebrick3', font = 'Helvetica 24')
            app1_money.place(x=860, y=145)

            app2 = Label(sellercanvas, text = seller3_info[7], font = 'Helvetica 24', fg = 'firebrick3')
            app2.place(x=700, y=200)
            
            app2_money_label = Label(sellercanvas, text = '$ made:', font = 'Helvetica 16')
            app2_money_label.place(x=780, y=250)

            app2_money = Label(sellercanvas, text = (int(app2_info[11]) + int(app2_esp_info[11])) * 1.99, fg = 'firebrick3', font = 'Helvetica 24')
            app2_money.place(x=860, y=245)

            app2_downloads = Label(sellercanvas, text = 'Downloads US: '+app2_info[11]+'Downloads CR: '+app2_esp_info[11], font = 'Helvetica 16')
            app2_downloads.place(x=600, y=240)

            app3 = Label(sellercanvas, text = seller3_info[8], font = 'Helvetica 24', fg = 'firebrick3')
            app3.place(x=700, y=300)

            app3_downloads = Label(sellercanvas, text = 'Downloads US: '+game1_info[11]+'Downloads CR: '+game1_esp_info[11], font = 'Helvetica 16')
            app3_downloads.place(x=600, y=340)

            app4 = Label(sellercanvas, text = seller3_info[9], font = 'Helvetica 24', fg = 'firebrick3')
            app4.place(x=700, y=400)

            app4_money_label = Label(sellercanvas, text = '$ made:', font = 'Helvetica 16')
            app4_money_label.place(x=780, y=450)

            app4_money = Label(sellercanvas, text = (int(game1_info[11]) + int(game1_esp_info[11])) * 0.99, fg = 'firebrick3', font = 'Helvetica 24')
            app4_money.place(x=860, y=445)
            
            app4_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app4_downloads.place(x=600, y=440)

            app5 = Label(sellercanvas, text = seller3_info[10], font = 'Helvetica 24', fg = 'firebrick3')
            app5.place(x=700, y=500)

            app5_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app5_downloads.place(x=600, y=540)

            name_label = Label(sellercanvas, text  = 'Seller name:', font = 'Helvetica 24')
            name_label.place(x=100, y=100)

            lastname_label = Label(sellercanvas, text = 'Last Name:', font = 'Helvetica 24')
            lastname_label.place(x=100, y=200)

            email_label = Label(sellercanvas, text = 'Email:', font = 'Helvetica 24')
            email_label.place(x=100, y=300)

            website_label = Label(sellercanvas, text = 'Website:', font = 'Helvetica 24')
            website_label.place(x=100, y=400)

            amount_apps_label = Label(sellercanvas, text = 'Amount apps on sale', font = 'Helvetica 24')
            amount_apps_label.place(x=100, y=500)

            app1_label = Label(sellercanvas, text = 'App 1', font = 'Helvetica 24')
            app1_label.place(x=600, y=100)

            app2_label = Label(sellercanvas, text = 'App 2', font = 'Helvetica 24')
            app2_label.place(x=600, y=200)

            app3_label = Label(sellercanvas, text = 'App 3', font = 'Helvetica 24')
            app3_label.place(x=600, y=300)

            app4_label = Label(sellercanvas, text = 'App 4', font = 'Helvetica 24')
            app4_label.place(x=600, y=400)

            app5_label = Label(sellercanvas, text = 'App 5', font = 'Helvetica 24')
            app5_label.place(x=600, y=500)

            #boton para agregar apps
            add_app_button = Button(sellercanvas, text = 'Add app', font = 'Helvetica 24', command = add_app_window)
            add_app_button.place(x=650, y=50)

            add_game_button = Button(sellercanvas, text = 'Add game', font = 'Helvetica 24', command = add_game_window)
            add_game_button.place(x=850, y=50)

        #misma estructura que vendedor 1
        def seller4():
            seller4 = Toplevel()
            seller4.title('Admin App')
            seller4.minsize(1000,600)
            seller4.resizable(width=NO, height=NO)

            sellercanvas = Canvas(seller4, width = 1000, height = 600)
            sellercanvas.place(x=0,y=0)

            all_sellers = open('sellers.txt', 'r')
            read_sellers = all_sellers.readlines()
            seller4_line = read_sellers[4]
            seller4_info = seller4_line.split(',')
            
            apps = open('apps.txt', 'r')
            read_apps = apps.readlines()
            app1 = read_apps[5]
            app1_info = app1.split(',')

            apps_esp = open('apps_esp.txt', 'r')
            read_apps_esp = apps_esp.readlines()
            app1_esp = read_apps_esp[5]
            app1_esp_info = app1_esp.split(',')

            def back():
                seller4.destroy()

            back_button = Button(seller4, image = exiticon, command = back)
            back_button.place(x=25,y=25)

            def add_app_window():
                add_app_window = Toplevel()
                add_app_window.title('Admin App')
                add_app_window.minsize(1000,600)
                add_app_window.resizable(width=NO, height=NO)

                def add_app():
                    a = open ('appcount.txt','r+')
                    lastIndex = a.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    appname = name_entry.get()
                    desc1 = desc1_entry.get()
                    desc2 = desc2_entry.get()
                    desc3 = desc3_entry.get()
                    desc4 = desc4_entry.get()
                    desc5 = desc5_entry.get()
                    price = price_entry.get()
                    appsize = appsize_entry.get()
                    b = open('apps.txt','a')
                    info = '4' + ',' + productid + ',' + '0' + ',' + appname + ',' + desc1 + ',' + desc2 + ',' + desc3 + ',' + desc4 + ',' + desc5 + ',' + price + ',' + appsize + ',' + '0'
                    b.write('\n' + str(info))
                    a.close
                    b.close

                    c = open('appcount.txt','r+')
                    lastIndex = c.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    desc1_esp = desc1_esp_entry.get()
                    desc2_esp = desc2_esp_entry.get()
                    desc3_esp = desc3_esp_entry.get()
                    desc4_esp = desc4_esp_entry.get()
                    desc5_esp = desc5_esp_entry.get()
                    d = open('apps_esp.txt','a')
                    info = '4' + ',' + productid + ',' + '0' + ',' + appname + ',' + desc1_esp + ',' + desc2_esp + ',' + desc3_esp + ',' + desc4_esp + ',' + desc5_esp + ',' + price + ',' + appsize + ',' + '0'
                    d.write('\n' + str(info))
                    c.write('\n' + str(int(productid) + 1))
                    c.close
                    d.close

                    e = open('sellers.txt', 'r+')
                    read_seller_info = e.readlines()
                    seller1_line = read_seller_info[1]
                    seller1_info = seller1_line.split(',')
                    seller2_line = read_seller_info[2]
                    seller2_info = seller2_line.split(',')
                    seller3_line = read_seller_info[3]
                    seller3_info = seller3_line.split(',')
                    seller4_line = read_seller_info[4]
                    seller4_info = seller4_line.split(',')
                    seller5_line = read_seller_info[5]
                    seller5_info = seller5_line.split(',')
                    seller6_line = read_seller_info[6]
                    seller6_info = seller6_line.split(',')
                    seller7_line = read_seller_info[7]
                    seller7_info = seller7_line.split(',')
                    seller8_line = read_seller_info[8]
                    seller8_info = seller8_line.split(',')
                    seller9_line = read_seller_info[9]
                    seller9_info = seller9_line.split(',')
                    seller10_line = read_seller_info[10]
                    seller10_info = seller10_line.split(',')

                    if seller4_info[6] == '':
                        seller4_info[6] = name_entry.get() + ' (I)'
                        seller4_info[5] = str(int(seller4_info[5]) + 1)
                    elif seller4_info[7] == '':
                        seller4_info[7] = name_entry.get() + ' (I)'
                        seller4_info[5] = str(int(seller4_info[5]) + 1)
                    elif seller4_info[8] == '':
                        seller4_info[8] = name_entry.get() + ' (I)'
                        seller4_info[5] = str(int(seller4_info[5]) + 1)
                    elif seller4_info[9] == '':
                        seller4_info[9] = name_entry.get() + ' (I)'
                        seller4_info[5] = str(int(seller4_info[5]) + 1)
                    elif seller4_info[10] == '':
                        seller4_info[10] = name_entry.get() + ' (I)'
                        seller4_info[5] = str(int(seller4_info[5]) + 1)
                    else:
                        print('You have challenged the Matrix')
                    
                    new_1 = seller1_info[0] + ',' + seller1_info[1] + ',' + seller1_info[2] + ',' + seller1_info[3] + ',' + seller1_info[4] + ',' + seller1_info[5] + ',' + seller1_info[6] + ',' + seller1_info[7] + ',' + seller1_info[8] + ',' + seller1_info[9] + ',' + seller1_info[10] + ',' + seller1_info[11] + ',' + seller1_info[12] 
                    new_2 = seller2_info[0] + ',' + seller2_info[1] + ',' + seller2_info[2] + ',' + seller2_info[3] + ',' + seller2_info[4] + ',' + seller2_info[5] + ',' + seller2_info[6] + ',' + seller2_info[7] + ',' + seller2_info[8] + ',' + seller2_info[9] + ',' + seller2_info[10] + ',' + seller2_info[11] + ',' + seller2_info[12] 
                    new_3 = seller3_info[0] + ',' + seller3_info[1] + ',' + seller3_info[2] + ',' + seller3_info[3] + ',' + seller3_info[4] + ',' + seller3_info[5] + ',' + seller3_info[6] + ',' + seller3_info[7] + ',' + seller3_info[8] + ',' + seller3_info[9] + ',' + seller3_info[10] + ',' + seller3_info[11] + ',' + seller3_info[12] 
                    new_4 = seller4_info[0] + ',' + seller4_info[1] + ',' + seller4_info[2] + ',' + seller4_info[3] + ',' + seller4_info[4] + ',' + seller4_info[5] + ',' + seller4_info[6] + ',' + seller4_info[7] + ',' + seller4_info[8] + ',' + seller4_info[9] + ',' + seller4_info[10] + ',' + seller4_info[11] + ',' + seller4_info[12] 
                    new_5 = seller5_info[0] + ',' + seller5_info[1] + ',' + seller5_info[2] + ',' + seller5_info[3] + ',' + seller5_info[4] + ',' + seller5_info[5] + ',' + seller5_info[6] + ',' + seller5_info[7] + ',' + seller5_info[8] + ',' + seller5_info[9] + ',' + seller5_info[10] + ',' + seller5_info[11] + ',' + seller5_info[12] 
                    new_6 = seller6_info[0] + ',' + seller6_info[1] + ',' + seller6_info[2] + ',' + seller6_info[3] + ',' + seller6_info[4] + ',' + seller6_info[5] + ',' + seller6_info[6] + ',' + seller6_info[7] + ',' + seller6_info[8] + ',' + seller6_info[9] + ',' + seller6_info[10] + ',' + seller6_info[11] + ',' + seller6_info[12] 
                    new_7 = seller7_info[0] + ',' + seller7_info[1] + ',' + seller7_info[2] + ',' + seller7_info[3] + ',' + seller7_info[4] + ',' + seller7_info[5] + ',' + seller7_info[6] + ',' + seller7_info[7] + ',' + seller7_info[8] + ',' + seller7_info[9] + ',' + seller7_info[10] + ',' + seller7_info[11] + ',' + seller7_info[12] 
                    new_8 = seller8_info[0] + ',' + seller8_info[1] + ',' + seller8_info[2] + ',' + seller8_info[3] + ',' + seller8_info[4] + ',' + seller8_info[5] + ',' + seller8_info[6] + ',' + seller8_info[7] + ',' + seller8_info[8] + ',' + seller8_info[9] + ',' + seller8_info[10] + ',' + seller8_info[11] + ',' + seller8_info[12]
                    new_9 = seller9_info[0] + ',' + seller9_info[1] + ',' + seller9_info[2] + ',' + seller9_info[3] + ',' + seller9_info[4] + ',' + seller9_info[5] + ',' + seller9_info[6] + ',' + seller9_info[7] + ',' + seller9_info[8] + ',' + seller9_info[9] + ',' + seller9_info[10] + ',' + seller9_info[11] + ',' + seller9_info[12] 
                    new_10 = seller10_info[0] + ',' + seller10_info[1] + ',' + seller10_info[2] + ',' + seller10_info[3] + ',' + seller10_info[4] + ',' + seller10_info[5] + ',' + seller10_info[6] + ',' + seller10_info[7] + ',' + seller10_info[8] + ',' + seller10_info[9] + ',' + seller10_info[10] + ',' + seller10_info[11] + ',' + seller10_info[12] 
                    f = open('sellers.txt', 'w')
                    g = f.close
                    h = open('sellers.txt', 'a')
                    write0 = h.write('#0-sellerid, 1-name, 2-lastname, 3-email, 4-website, 5-amountappsonsale, 6-app1, 7-app2, 8-app3, 9-app4, 10-app5, 11-downloadsUS, 12-downloadsCR' + '\n')
                    write1 = h.write(new_1)
                    write2 = h.write(new_2)
                    write3 = h.write(new_3)
                    write4 = h.write(new_4)
                    write5 = h.write(new_5)
                    write6 = h.write(new_6)
                    write7 = h.write(new_7)
                    write8 = h.write(new_8)
                    write9 = h.write(new_9)
                    write10 = h.write(new_10)
                    i = h.close

                    success_label = Label(add_app_window, text = 'Success', font = 'Helvetica 38', fg = 'firebrick3')
                    success_label.place(x=680, y=400)

                #labels para info de app que se quiera agregar
                appname_label = Label(add_app_window, text = 'App Name', font = 'Helvetica 24')
                appname_label.place(x=100, y=50)

                desc1_label = Label(add_app_window, text = 'Description 1', font = 'Helvetica 24')
                desc1_label.place(x=100, y=100)

                desc2_label = Label(add_app_window, text = 'Description 2', font = 'Helvetica 24')
                desc2_label.place(x=100, y=150)

                desc3_label = Label(add_app_window, text = 'Description 3', font = 'Helvetica 24')
                desc3_label.place(x=100, y=200)

                desc4_label = Label(add_app_window, text = 'Description 4', font = 'Helvetica 24')
                desc4_label.place(x=100, y=250)

                desc5_label = Label(add_app_window, text = 'Description 5', font = 'Helvetica 24')
                desc5_label.place(x=100, y=300)

                desc1_esp_label = Label(add_app_window, text = 'Description 1 in Spanish', font = 'Helvetica 24')
                desc1_esp_label.place(x=100, y=350)

                desc2_esp_label = Label(add_app_window, text = 'Description 2 in Spanish', font = 'Helvetica 24')
                desc2_esp_label.place(x=100, y=400)

                desc3_esp_label = Label(add_app_window, text = 'Description 3 in Spanish', font = 'Helvetica 24')
                desc3_esp_label.place(x=100, y=450)

                desc4_esp_label = Label(add_app_window, text = 'Description 4 in Spanish', font = 'Helvetica 24')
                desc4_esp_label.place(x=100, y=500)

                desc5_esp_label = Label(add_app_window, text = 'Description 5 in Spanish', font = 'Helvetica 24')
                desc5_esp_label.place(x=100, y=550)

                price_label = Label(add_app_window, text = 'Price ($) or "Free"', font = 'Helvetica 24')
                price_label.place(x=600, y=50)

                appsize_label  = Label(add_app_window, text = 'App Size', font = 'Helvetica 24')
                appsize_label.place(x=600, y=100)

                #entries
                name_entry = Entry(add_app_window, width = 20)
                name_entry.place(x=400, y=50)

                desc1_entry = Entry(add_app_window, width = 20)
                desc1_entry.place(x=400, y=100)

                desc2_entry = Entry(add_app_window, width = 20)
                desc2_entry.place(x=400, y=150)

                desc3_entry = Entry(add_app_window, width = 20)
                desc3_entry.place(x=400, y=200)

                desc4_entry = Entry(add_app_window, width = 20)
                desc4_entry.place(x=400, y=250)

                desc5_entry = Entry(add_app_window, width = 20)
                desc5_entry.place(x=400, y=300)

                desc1_esp_entry = Entry(add_app_window, width = 20)
                desc1_esp_entry.place(x=400, y=350)

                desc2_esp_entry = Entry(add_app_window, width = 20)
                desc2_esp_entry.place(x=400, y=400)

                desc3_esp_entry = Entry(add_app_window, width = 20)
                desc3_esp_entry.place(x=400, y=450)

                desc4_esp_entry = Entry(add_app_window, width = 20)
                desc4_esp_entry.place(x=400, y=500)

                desc5_esp_entry = Entry(add_app_window, width = 20)
                desc5_esp_entry.place(x=400, y=550)

                price_entry = Entry(add_app_window, width = 20)
                price_entry.place(x=800, y=50)

                appsize_entry  = Entry(add_app_window, width = 20)
                appsize_entry.place(x=800, y=100)

                add_app_button = Button(add_app_window, text = 'Add App', command = add_app)
                add_app_button.place(x=700, y=475)

                def back():
                    add_app_window.destroy()

                back_button = Button(add_app_window, image = exiticon, command = back)
                back_button.place(x=25,y=25)

            def add_game_window():
                add_game_window = Toplevel()
                add_game_window.title('Admin App')
                add_game_window.minsize(1000,600)
                add_game_window.resizable(width=NO, height=NO)

                def add_app():
                    a = open ('appcount.txt','r+')
                    lastIndex = a.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    appname = name_entry.get()
                    desc1 = desc1_entry.get()
                    desc2 = desc2_entry.get()
                    desc3 = desc3_entry.get()
                    desc4 = desc4_entry.get()
                    desc5 = desc5_entry.get()
                    price = price_entry.get()
                    appsize = appsize_entry.get()
                    b = open('games.txt','a')
                    info = '4' + ',' + productid + ',' + '1' + ',' + appname + ',' + desc1 + ',' + desc2 + ',' + desc3 + ',' + desc4 + ',' + desc5 + ',' + price + ',' + appsize + ',' + '0'
                    b.write('\n' + str(info))
                    a.close
                    b.close

                    c = open('appcount.txt','r+')
                    lastIndex = c.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    desc1_esp = desc1_esp_entry.get()
                    desc2_esp = desc2_esp_entry.get()
                    desc3_esp = desc3_esp_entry.get()
                    desc4_esp = desc4_esp_entry.get()
                    desc5_esp = desc5_esp_entry.get()
                    d = open('games_esp.txt','a')
                    info = '4' + ',' + productid + ',' + '1' + ',' + appname + ',' + desc1_esp + ',' + desc2_esp + ',' + desc3_esp + ',' + desc4_esp + ',' + desc5_esp + ',' + price + ',' + appsize + ',' + '0'
                    d.write('\n' + str(info))
                    c.write('\n' + str(int(productid) + 1))
                    c.close
                    d.close

                    e = open('sellers.txt', 'r+')
                    read_seller_info = e.readlines()
                    seller1_line = read_seller_info[1]
                    seller1_info = seller1_line.split(',')
                    seller2_line = read_seller_info[2]
                    seller2_info = seller2_line.split(',')
                    seller3_line = read_seller_info[3]
                    seller3_info = seller3_line.split(',')
                    seller4_line = read_seller_info[4]
                    seller4_info = seller4_line.split(',')
                    seller5_line = read_seller_info[5]
                    seller5_info = seller5_line.split(',')
                    seller6_line = read_seller_info[6]
                    seller6_info = seller6_line.split(',')
                    seller7_line = read_seller_info[7]
                    seller7_info = seller7_line.split(',')
                    seller8_line = read_seller_info[8]
                    seller8_info = seller8_line.split(',')
                    seller9_line = read_seller_info[9]
                    seller9_info = seller9_line.split(',')
                    seller10_line = read_seller_info[10]
                    seller10_info = seller10_line.split(',')

                    if seller4_info[6] == '':
                        seller4_info[6] = name_entry.get() + ' (I)'
                        seller4_info[5] = str(int(seller4_info[5]) + 1)
                    elif seller4_info[7] == '':
                        seller4_info[7] = name_entry.get() + ' (I)'
                        seller4_info[5] = str(int(seller4_info[5]) + 1)
                    elif seller4_info[8] == '':
                        seller4_info[8] = name_entry.get() + ' (I)'
                        seller4_info[5] = str(int(seller4_info[5]) + 1)
                    elif seller4_info[9] == '':
                        seller4_info[9] = name_entry.get() + ' (I)'
                        seller4_info[5] = str(int(seller4_info[5]) + 1)
                    elif seller4_info[10] == '':
                        seller4_info[10] = name_entry.get() + ' (I)'
                        seller4_info[5] = str(int(seller4_info[5]) + 1)
                    else:
                        print('You have challenged the Matrix')
                    
                    new_1 = seller1_info[0] + ',' + seller1_info[1] + ',' + seller1_info[2] + ',' + seller1_info[3] + ',' + seller1_info[4] + ',' + seller1_info[5] + ',' + seller1_info[6] + ',' + seller1_info[7] + ',' + seller1_info[8] + ',' + seller1_info[9] + ',' + seller1_info[10] + ',' + seller1_info[11] + ',' + seller1_info[12] 
                    new_2 = seller2_info[0] + ',' + seller2_info[1] + ',' + seller2_info[2] + ',' + seller2_info[3] + ',' + seller2_info[4] + ',' + seller2_info[5] + ',' + seller2_info[6] + ',' + seller2_info[7] + ',' + seller2_info[8] + ',' + seller2_info[9] + ',' + seller2_info[10] + ',' + seller2_info[11] + ',' + seller2_info[12] 
                    new_3 = seller3_info[0] + ',' + seller3_info[1] + ',' + seller3_info[2] + ',' + seller3_info[3] + ',' + seller3_info[4] + ',' + seller3_info[5] + ',' + seller3_info[6] + ',' + seller3_info[7] + ',' + seller3_info[8] + ',' + seller3_info[9] + ',' + seller3_info[10] + ',' + seller3_info[11] + ',' + seller3_info[12] 
                    new_4 = seller4_info[0] + ',' + seller4_info[1] + ',' + seller4_info[2] + ',' + seller4_info[3] + ',' + seller4_info[4] + ',' + seller4_info[5] + ',' + seller4_info[6] + ',' + seller4_info[7] + ',' + seller4_info[8] + ',' + seller4_info[9] + ',' + seller4_info[10] + ',' + seller4_info[11] + ',' + seller4_info[12] 
                    new_5 = seller5_info[0] + ',' + seller5_info[1] + ',' + seller5_info[2] + ',' + seller5_info[3] + ',' + seller5_info[4] + ',' + seller5_info[5] + ',' + seller5_info[6] + ',' + seller5_info[7] + ',' + seller5_info[8] + ',' + seller5_info[9] + ',' + seller5_info[10] + ',' + seller5_info[11] + ',' + seller5_info[12] 
                    new_6 = seller6_info[0] + ',' + seller6_info[1] + ',' + seller6_info[2] + ',' + seller6_info[3] + ',' + seller6_info[4] + ',' + seller6_info[5] + ',' + seller6_info[6] + ',' + seller6_info[7] + ',' + seller6_info[8] + ',' + seller6_info[9] + ',' + seller6_info[10] + ',' + seller6_info[11] + ',' + seller6_info[12] 
                    new_7 = seller7_info[0] + ',' + seller7_info[1] + ',' + seller7_info[2] + ',' + seller7_info[3] + ',' + seller7_info[4] + ',' + seller7_info[5] + ',' + seller7_info[6] + ',' + seller7_info[7] + ',' + seller7_info[8] + ',' + seller7_info[9] + ',' + seller7_info[10] + ',' + seller7_info[11] + ',' + seller7_info[12] 
                    new_8 = seller8_info[0] + ',' + seller8_info[1] + ',' + seller8_info[2] + ',' + seller8_info[3] + ',' + seller8_info[4] + ',' + seller8_info[5] + ',' + seller8_info[6] + ',' + seller8_info[7] + ',' + seller8_info[8] + ',' + seller8_info[9] + ',' + seller8_info[10] + ',' + seller8_info[11] + ',' + seller8_info[12]
                    new_9 = seller9_info[0] + ',' + seller9_info[1] + ',' + seller9_info[2] + ',' + seller9_info[3] + ',' + seller9_info[4] + ',' + seller9_info[5] + ',' + seller9_info[6] + ',' + seller9_info[7] + ',' + seller9_info[8] + ',' + seller9_info[9] + ',' + seller9_info[10] + ',' + seller9_info[11] + ',' + seller9_info[12] 
                    new_10 = seller10_info[0] + ',' + seller10_info[1] + ',' + seller10_info[2] + ',' + seller10_info[3] + ',' + seller10_info[4] + ',' + seller10_info[5] + ',' + seller10_info[6] + ',' + seller10_info[7] + ',' + seller10_info[8] + ',' + seller10_info[9] + ',' + seller10_info[10] + ',' + seller10_info[11] + ',' + seller10_info[12] 
                    f = open('sellers.txt', 'w')
                    g = f.close
                    h = open('sellers.txt', 'a')
                    write0 = h.write('#0-sellerid, 1-name, 2-lastname, 3-email, 4-website, 5-amountappsonsale, 6-app1, 7-app2, 8-app3, 9-app4, 10-app5, 11-downloadsUS, 12-downloadsCR' + '\n')
                    write1 = h.write(new_1)
                    write2 = h.write(new_2)
                    write3 = h.write(new_3)
                    write4 = h.write(new_4)
                    write5 = h.write(new_5)
                    write6 = h.write(new_6)
                    write7 = h.write(new_7)
                    write8 = h.write(new_8)
                    write9 = h.write(new_9)
                    write10 = h.write(new_10)
                    i = h.close

                    success_label = Label(add_game_window, text = 'Success', font = 'Helvetica 38', fg = 'firebrick3')
                    success_label.place(x=680, y=400)

                #labels para info de app que se quiera agregar
                appname_label = Label(add_game_window, text = 'Game Name', font = 'Helvetica 24')
                appname_label.place(x=100, y=50)

                desc1_label = Label(add_game_window, text = 'Description 1', font = 'Helvetica 24')
                desc1_label.place(x=100, y=100)

                desc2_label = Label(add_game_window, text = 'Description 2', font = 'Helvetica 24')
                desc2_label.place(x=100, y=150)

                desc3_label = Label(add_game_window, text = 'Description 3', font = 'Helvetica 24')
                desc3_label.place(x=100, y=200)

                desc4_label = Label(add_game_window, text = 'Description 4', font = 'Helvetica 24')
                desc4_label.place(x=100, y=250)

                desc5_label = Label(add_game_window, text = 'Description 5', font = 'Helvetica 24')
                desc5_label.place(x=100, y=300)

                desc1_esp_label = Label(add_game_window, text = 'Description 1 in Spanish', font = 'Helvetica 24')
                desc1_esp_label.place(x=100, y=350)

                desc2_esp_label = Label(add_game_window, text = 'Description 2 in Spanish', font = 'Helvetica 24')
                desc2_esp_label.place(x=100, y=400)

                desc3_esp_label = Label(add_game_window, text = 'Description 3 in Spanish', font = 'Helvetica 24')
                desc3_esp_label.place(x=100, y=450)

                desc4_esp_label = Label(add_game_window, text = 'Description 4 in Spanish', font = 'Helvetica 24')
                desc4_esp_label.place(x=100, y=500)

                desc5_esp_label = Label(add_game_window, text = 'Description 5 in Spanish', font = 'Helvetica 24')
                desc5_esp_label.place(x=100, y=550)

                price_label = Label(add_game_window, text = 'Price ($) or "Free"', font = 'Helvetica 24')
                price_label.place(x=600, y=50)

                appsize_label  = Label(add_game_window, text = 'App Size', font = 'Helvetica 24')
                appsize_label.place(x=600, y=100)

                #entries
                name_entry = Entry(add_game_window, width = 20)
                name_entry.place(x=400, y=50)

                desc1_entry = Entry(add_game_window, width = 20)
                desc1_entry.place(x=400, y=100)

                desc2_entry = Entry(add_game_window, width = 20)
                desc2_entry.place(x=400, y=150)

                desc3_entry = Entry(add_game_window, width = 20)
                desc3_entry.place(x=400, y=200)

                desc4_entry = Entry(add_game_window, width = 20)
                desc4_entry.place(x=400, y=250)

                desc5_entry = Entry(add_game_window, width = 20)
                desc5_entry.place(x=400, y=300)

                desc1_esp_entry = Entry(add_game_window, width = 20)
                desc1_esp_entry.place(x=400, y=350)

                desc2_esp_entry = Entry(add_game_window, width = 20)
                desc2_esp_entry.place(x=400, y=400)

                desc3_esp_entry = Entry(add_game_window, width = 20)
                desc3_esp_entry.place(x=400, y=450)

                desc4_esp_entry = Entry(add_game_window, width = 20)
                desc4_esp_entry.place(x=400, y=500)

                desc5_esp_entry = Entry(add_game_window, width = 20)
                desc5_esp_entry.place(x=400, y=550)

                price_entry = Entry(add_game_window, width = 20)
                price_entry.place(x=800, y=50)

                appsize_entry  = Entry(add_game_window, width = 20)
                appsize_entry.place(x=800, y=100)

                add_app_button = Button(add_game_window, text = 'Add Game', command = add_app)
                add_app_button.place(x=700, y=475)

                def back():
                    add_game_window.destroy()

                back_button = Button(add_game_window, image = exiticon, command = back)
                back_button.place(x=25,y=25)
                
                
            #labels de informacion
            name = Label(sellercanvas, text = seller4_info[1], font = 'Helvetica 24', fg = 'firebrick3')
            name.place(x=300, y=100)

            lastname = Label(sellercanvas, text = seller4_info[2], font = 'Helvetica 24', fg = 'firebrick3')
            lastname.place(x=300, y=200)

            email = Label(sellercanvas, text = seller4_info[3], font = 'Helvetica 24', fg = 'firebrick3')
            email.place(x=300, y=300)

            website = Label(sellercanvas, text = seller4_info[4], font = 'Helvetica 24', fg = 'firebrick3')
            website.place(x=300, y=400)

            amount_apps = Label(sellercanvas, text = seller4_info[5], font = 'Helvetica 24', fg = 'firebrick3')
            amount_apps.place(x=400, y=500)

            app1 = Label(sellercanvas, text = seller4_info[6], font = 'Helvetica 24', fg = 'firebrick3')
            app1.place(x=700, y=100)

            app1_downloads = Label(sellercanvas, text = 'Downloads US: '+app1_info[11]+'Downloads CR: '+app1_esp_info[11], font = 'Helvetica 16')
            app1_downloads.place(x=600, y=140)

            app2 = Label(sellercanvas, text = seller4_info[7], font = 'Helvetica 24', fg = 'firebrick3')
            app2.place(x=700, y=200)

            app2_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app2_downloads.place(x=600, y=240)

            app3 = Label(sellercanvas, text = seller4_info[8], font = 'Helvetica 24', fg = 'firebrick3')
            app3.place(x=700, y=300)

            app3_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app3_downloads.place(x=600, y=340)

            app4 = Label(sellercanvas, text = seller4_info[9], font = 'Helvetica 24', fg = 'firebrick3')
            app4.place(x=700, y=400)
            
            app4_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app4_downloads.place(x=600, y=440)

            app5 = Label(sellercanvas, text = seller4_info[10], font = 'Helvetica 24', fg = 'firebrick3')
            app5.place(x=700, y=500)

            app5_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app5_downloads.place(x=600, y=540)

            name_label = Label(sellercanvas, text  = 'Seller name:', font = 'Helvetica 24')
            name_label.place(x=100, y=100)

            lastname_label = Label(sellercanvas, text = 'Last Name:', font = 'Helvetica 24')
            lastname_label.place(x=100, y=200)

            email_label = Label(sellercanvas, text = 'Email:', font = 'Helvetica 24')
            email_label.place(x=100, y=300)

            website_label = Label(sellercanvas, text = 'Website:', font = 'Helvetica 24')
            website_label.place(x=100, y=400)

            amount_apps_label = Label(sellercanvas, text = 'Amount apps on sale', font = 'Helvetica 24')
            amount_apps_label.place(x=100, y=500)

            app1_label = Label(sellercanvas, text = 'App 1', font = 'Helvetica 24')
            app1_label.place(x=600, y=100)

            app2_label = Label(sellercanvas, text = 'App 2', font = 'Helvetica 24')
            app2_label.place(x=600, y=200)

            app3_label = Label(sellercanvas, text = 'App 3', font = 'Helvetica 24')
            app3_label.place(x=600, y=300)

            app4_label = Label(sellercanvas, text = 'App 4', font = 'Helvetica 24')
            app4_label.place(x=600, y=400)

            app5_label = Label(sellercanvas, text = 'App 5', font = 'Helvetica 24')
            app5_label.place(x=600, y=500)

            #boton para agregar apps
            add_app_button = Button(sellercanvas, text = 'Add app', font = 'Helvetica 24', command = add_app_window)
            add_app_button.place(x=650, y=50)

            add_game_button = Button(sellercanvas, text = 'Add game', font = 'Helvetica 24', command = add_game_window)
            add_game_button.place(x=850, y=50)

        #misma estructura que vendedor 1
        def seller5():
            seller5 = Toplevel()
            seller5.title('Admin App')
            seller5.minsize(1000,600)
            seller5.resizable(width=NO, height=NO)

            sellercanvas = Canvas(seller5, width = 1000, height = 600)
            sellercanvas.place(x=0,y=0)

            all_sellers = open('sellers.txt', 'r')
            read_sellers = all_sellers.readlines()
            seller5_line = read_sellers[5]
            seller5_info = seller5_line.split(',')
            
            apps = open('apps.txt', 'r')
            read_apps = apps.readlines()
            app1 = read_apps[6]
            app1_info = app1.split(',')

            apps_esp = open('apps_esp.txt', 'r')
            read_apps_esp = apps_esp.readlines()
            app1_esp = read_apps_esp[6]
            app1_esp_info = app1_esp.split(',')

            games = open('games.txt', 'r')
            read_games = games.readlines()
            game1 = read_games[8]
            game1_info = game1.split(',')

            games_esp = open('games_esp.txt', 'r')
            read_games_esp = games_esp.readlines()
            game1_esp = read_games_esp[8]
            game1_esp_info = game1_esp.split(',')


            def back():
                seller5.destroy()

            back_button = Button(seller5, image = exiticon, command = back)
            back_button.place(x=25,y=25)

            def add_app_window():
                add_app_window = Toplevel()
                add_app_window.title('Admin App')
                add_app_window.minsize(1000,600)
                add_app_window.resizable(width=NO, height=NO)

                def add_app():
                    a = open ('appcount.txt','r+')
                    lastIndex = a.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    appname = name_entry.get()
                    desc1 = desc1_entry.get()
                    desc2 = desc2_entry.get()
                    desc3 = desc3_entry.get()
                    desc4 = desc4_entry.get()
                    desc5 = desc5_entry.get()
                    price = price_entry.get()
                    appsize = appsize_entry.get()
                    b = open('apps.txt','a')
                    info = '5' + ',' + productid + ',' + '0' + ',' + appname + ',' + desc1 + ',' + desc2 + ',' + desc3 + ',' + desc4 + ',' + desc5 + ',' + price + ',' + appsize + ',' + '0'
                    b.write('\n' + str(info))
                    a.close
                    b.close

                    c = open('appcount.txt','r+')
                    lastIndex = c.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    desc1_esp = desc1_esp_entry.get()
                    desc2_esp = desc2_esp_entry.get()
                    desc3_esp = desc3_esp_entry.get()
                    desc4_esp = desc4_esp_entry.get()
                    desc5_esp = desc5_esp_entry.get()
                    d = open('apps_esp.txt','a')
                    info = '5' + ',' + productid + ',' + '0' + ',' + appname + ',' + desc1_esp + ',' + desc2_esp + ',' + desc3_esp + ',' + desc4_esp + ',' + desc5_esp + ',' + price + ',' + appsize + ',' + '0'
                    d.write('\n' + str(info))
                    c.write('\n' + str(int(productid) + 1))
                    c.close
                    d.close

                    e = open('sellers.txt', 'r+')
                    read_seller_info = e.readlines()
                    seller1_line = read_seller_info[1]
                    seller1_info = seller1_line.split(',')
                    seller2_line = read_seller_info[2]
                    seller2_info = seller2_line.split(',')
                    seller3_line = read_seller_info[3]
                    seller3_info = seller3_line.split(',')
                    seller4_line = read_seller_info[4]
                    seller4_info = seller4_line.split(',')
                    seller5_line = read_seller_info[5]
                    seller5_info = seller5_line.split(',')
                    seller6_line = read_seller_info[6]
                    seller6_info = seller6_line.split(',')
                    seller7_line = read_seller_info[7]
                    seller7_info = seller7_line.split(',')
                    seller8_line = read_seller_info[8]
                    seller8_info = seller8_line.split(',')
                    seller9_line = read_seller_info[9]
                    seller9_info = seller9_line.split(',')
                    seller10_line = read_seller_info[10]
                    seller10_info = seller10_line.split(',')

                    if seller5_info[6] == '':
                        seller5_info[6] = name_entry.get() + ' (I)'
                        seller5_info[5] = str(int(seller5_info[5]) + 1)
                    elif seller5_info[7] == '':
                        seller5_info[7] = name_entry.get() + ' (I)'
                        seller5_info[5] = str(int(seller5_info[5]) + 1)
                    elif seller5_info[8] == '':
                        seller5_info[8] = name_entry.get() + ' (I)'
                        seller5_info[5] = str(int(seller5_info[5]) + 1)
                    elif seller5_info[9] == '':
                        seller5_info[9] = name_entry.get() + ' (I)'
                        seller5_info[5] = str(int(seller5_info[5]) + 1)
                    elif seller5_info[10] == '':
                        seller5_info[10] = name_entry.get() + ' (I)'
                        seller5_info[5] = str(int(seller5_info[5]) + 1)
                    else:
                        print('You have challenged the Matrix')
                    
                    new_1 = seller1_info[0] + ',' + seller1_info[1] + ',' + seller1_info[2] + ',' + seller1_info[3] + ',' + seller1_info[4] + ',' + seller1_info[5] + ',' + seller1_info[6] + ',' + seller1_info[7] + ',' + seller1_info[8] + ',' + seller1_info[9] + ',' + seller1_info[10] + ',' + seller1_info[11] + ',' + seller1_info[12] 
                    new_2 = seller2_info[0] + ',' + seller2_info[1] + ',' + seller2_info[2] + ',' + seller2_info[3] + ',' + seller2_info[4] + ',' + seller2_info[5] + ',' + seller2_info[6] + ',' + seller2_info[7] + ',' + seller2_info[8] + ',' + seller2_info[9] + ',' + seller2_info[10] + ',' + seller2_info[11] + ',' + seller2_info[12] 
                    new_3 = seller3_info[0] + ',' + seller3_info[1] + ',' + seller3_info[2] + ',' + seller3_info[3] + ',' + seller3_info[4] + ',' + seller3_info[5] + ',' + seller3_info[6] + ',' + seller3_info[7] + ',' + seller3_info[8] + ',' + seller3_info[9] + ',' + seller3_info[10] + ',' + seller3_info[11] + ',' + seller3_info[12] 
                    new_4 = seller4_info[0] + ',' + seller4_info[1] + ',' + seller4_info[2] + ',' + seller4_info[3] + ',' + seller4_info[4] + ',' + seller4_info[5] + ',' + seller4_info[6] + ',' + seller4_info[7] + ',' + seller4_info[8] + ',' + seller4_info[9] + ',' + seller4_info[10] + ',' + seller4_info[11] + ',' + seller4_info[12] 
                    new_5 = seller5_info[0] + ',' + seller5_info[1] + ',' + seller5_info[2] + ',' + seller5_info[3] + ',' + seller5_info[4] + ',' + seller5_info[5] + ',' + seller5_info[6] + ',' + seller5_info[7] + ',' + seller5_info[8] + ',' + seller5_info[9] + ',' + seller5_info[10] + ',' + seller5_info[11] + ',' + seller5_info[12] 
                    new_6 = seller6_info[0] + ',' + seller6_info[1] + ',' + seller6_info[2] + ',' + seller6_info[3] + ',' + seller6_info[4] + ',' + seller6_info[5] + ',' + seller6_info[6] + ',' + seller6_info[7] + ',' + seller6_info[8] + ',' + seller6_info[9] + ',' + seller6_info[10] + ',' + seller6_info[11] + ',' + seller6_info[12] 
                    new_7 = seller7_info[0] + ',' + seller7_info[1] + ',' + seller7_info[2] + ',' + seller7_info[3] + ',' + seller7_info[4] + ',' + seller7_info[5] + ',' + seller7_info[6] + ',' + seller7_info[7] + ',' + seller7_info[8] + ',' + seller7_info[9] + ',' + seller7_info[10] + ',' + seller7_info[11] + ',' + seller7_info[12] 
                    new_8 = seller8_info[0] + ',' + seller8_info[1] + ',' + seller8_info[2] + ',' + seller8_info[3] + ',' + seller8_info[4] + ',' + seller8_info[5] + ',' + seller8_info[6] + ',' + seller8_info[7] + ',' + seller8_info[8] + ',' + seller8_info[9] + ',' + seller8_info[10] + ',' + seller8_info[11] + ',' + seller8_info[12]
                    new_9 = seller9_info[0] + ',' + seller9_info[1] + ',' + seller9_info[2] + ',' + seller9_info[3] + ',' + seller9_info[4] + ',' + seller9_info[5] + ',' + seller9_info[6] + ',' + seller9_info[7] + ',' + seller9_info[8] + ',' + seller9_info[9] + ',' + seller9_info[10] + ',' + seller9_info[11] + ',' + seller9_info[12] 
                    new_10 = seller10_info[0] + ',' + seller10_info[1] + ',' + seller10_info[2] + ',' + seller10_info[3] + ',' + seller10_info[4] + ',' + seller10_info[5] + ',' + seller10_info[6] + ',' + seller10_info[7] + ',' + seller10_info[8] + ',' + seller10_info[9] + ',' + seller10_info[10] + ',' + seller10_info[11] + ',' + seller10_info[12] 
                    f = open('sellers.txt', 'w')
                    g = f.close
                    h = open('sellers.txt', 'a')
                    write0 = h.write('#0-sellerid, 1-name, 2-lastname, 3-email, 4-website, 5-amountappsonsale, 6-app1, 7-app2, 8-app3, 9-app4, 10-app5, 11-downloadsUS, 12-downloadsCR' + '\n')
                    write1 = h.write(new_1)
                    write2 = h.write(new_2)
                    write3 = h.write(new_3)
                    write4 = h.write(new_4)
                    write5 = h.write(new_5)
                    write6 = h.write(new_6)
                    write7 = h.write(new_7)
                    write8 = h.write(new_8)
                    write9 = h.write(new_9)
                    write10 = h.write(new_10)
                    i = h.close

                    success_label = Label(add_app_window, text = 'Success', font = 'Helvetica 38', fg = 'firebrick3')
                    success_label.place(x=680, y=400)

                #labels para info de app que se quiera agregar
                appname_label = Label(add_app_window, text = 'App Name', font = 'Helvetica 24')
                appname_label.place(x=100, y=50)

                desc1_label = Label(add_app_window, text = 'Description 1', font = 'Helvetica 24')
                desc1_label.place(x=100, y=100)

                desc2_label = Label(add_app_window, text = 'Description 2', font = 'Helvetica 24')
                desc2_label.place(x=100, y=150)

                desc3_label = Label(add_app_window, text = 'Description 3', font = 'Helvetica 24')
                desc3_label.place(x=100, y=200)

                desc4_label = Label(add_app_window, text = 'Description 4', font = 'Helvetica 24')
                desc4_label.place(x=100, y=250)

                desc5_label = Label(add_app_window, text = 'Description 5', font = 'Helvetica 24')
                desc5_label.place(x=100, y=300)

                desc1_esp_label = Label(add_app_window, text = 'Description 1 in Spanish', font = 'Helvetica 24')
                desc1_esp_label.place(x=100, y=350)

                desc2_esp_label = Label(add_app_window, text = 'Description 2 in Spanish', font = 'Helvetica 24')
                desc2_esp_label.place(x=100, y=400)

                desc3_esp_label = Label(add_app_window, text = 'Description 3 in Spanish', font = 'Helvetica 24')
                desc3_esp_label.place(x=100, y=450)

                desc4_esp_label = Label(add_app_window, text = 'Description 4 in Spanish', font = 'Helvetica 24')
                desc4_esp_label.place(x=100, y=500)

                desc5_esp_label = Label(add_app_window, text = 'Description 5 in Spanish', font = 'Helvetica 24')
                desc5_esp_label.place(x=100, y=550)

                price_label = Label(add_app_window, text = 'Price ($) or "Free"', font = 'Helvetica 24')
                price_label.place(x=600, y=50)

                appsize_label  = Label(add_app_window, text = 'App Size', font = 'Helvetica 24')
                appsize_label.place(x=600, y=100)

                #entries
                name_entry = Entry(add_app_window, width = 20)
                name_entry.place(x=400, y=50)

                desc1_entry = Entry(add_app_window, width = 20)
                desc1_entry.place(x=400, y=100)

                desc2_entry = Entry(add_app_window, width = 20)
                desc2_entry.place(x=400, y=150)

                desc3_entry = Entry(add_app_window, width = 20)
                desc3_entry.place(x=400, y=200)

                desc4_entry = Entry(add_app_window, width = 20)
                desc4_entry.place(x=400, y=250)

                desc5_entry = Entry(add_app_window, width = 20)
                desc5_entry.place(x=400, y=300)

                desc1_esp_entry = Entry(add_app_window, width = 20)
                desc1_esp_entry.place(x=400, y=350)

                desc2_esp_entry = Entry(add_app_window, width = 20)
                desc2_esp_entry.place(x=400, y=400)

                desc3_esp_entry = Entry(add_app_window, width = 20)
                desc3_esp_entry.place(x=400, y=450)

                desc4_esp_entry = Entry(add_app_window, width = 20)
                desc4_esp_entry.place(x=400, y=500)

                desc5_esp_entry = Entry(add_app_window, width = 20)
                desc5_esp_entry.place(x=400, y=550)

                price_entry = Entry(add_app_window, width = 20)
                price_entry.place(x=800, y=50)

                appsize_entry  = Entry(add_app_window, width = 20)
                appsize_entry.place(x=800, y=100)

                add_app_button = Button(add_app_window, text = 'Add App', command = add_app)
                add_app_button.place(x=700, y=475)

                def back():
                    add_app_window.destroy()

                back_button = Button(add_app_window, image = exiticon, command = back)
                back_button.place(x=25,y=25)

            def add_game_window():
                add_game_window = Toplevel()
                add_game_window.title('Admin App')
                add_game_window.minsize(1000,600)
                add_game_window.resizable(width=NO, height=NO)

                def add_app():
                    a = open ('appcount.txt','r+')
                    lastIndex = a.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    appname = name_entry.get()
                    desc1 = desc1_entry.get()
                    desc2 = desc2_entry.get()
                    desc3 = desc3_entry.get()
                    desc4 = desc4_entry.get()
                    desc5 = desc5_entry.get()
                    price = price_entry.get()
                    appsize = appsize_entry.get()
                    b = open('games.txt','a')
                    info = '5' + ',' + productid + ',' + '1' + ',' + appname + ',' + desc1 + ',' + desc2 + ',' + desc3 + ',' + desc4 + ',' + desc5 + ',' + price + ',' + appsize + ',' + '0'
                    b.write('\n' + str(info))
                    a.close
                    b.close

                    c = open('appcount.txt','r+')
                    lastIndex = c.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    desc1_esp = desc1_esp_entry.get()
                    desc2_esp = desc2_esp_entry.get()
                    desc3_esp = desc3_esp_entry.get()
                    desc4_esp = desc4_esp_entry.get()
                    desc5_esp = desc5_esp_entry.get()
                    d = open('games_esp.txt','a')
                    info = '5' + ',' + productid + ',' + '1' + ',' + appname + ',' + desc1_esp + ',' + desc2_esp + ',' + desc3_esp + ',' + desc4_esp + ',' + desc5_esp + ',' + price + ',' + appsize + ',' + '0'
                    d.write('\n' + str(info))
                    c.write('\n' + str(int(productid) + 1))
                    c.close
                    d.close

                    e = open('sellers.txt', 'r+')
                    read_seller_info = e.readlines()
                    seller1_line = read_seller_info[1]
                    seller1_info = seller1_line.split(',')
                    seller2_line = read_seller_info[2]
                    seller2_info = seller2_line.split(',')
                    seller3_line = read_seller_info[3]
                    seller3_info = seller3_line.split(',')
                    seller4_line = read_seller_info[4]
                    seller4_info = seller4_line.split(',')
                    seller5_line = read_seller_info[5]
                    seller5_info = seller5_line.split(',')
                    seller6_line = read_seller_info[6]
                    seller6_info = seller6_line.split(',')
                    seller7_line = read_seller_info[7]
                    seller7_info = seller7_line.split(',')
                    seller8_line = read_seller_info[8]
                    seller8_info = seller8_line.split(',')
                    seller9_line = read_seller_info[9]
                    seller9_info = seller9_line.split(',')
                    seller10_line = read_seller_info[10]
                    seller10_info = seller10_line.split(',')

                    if seller5_info[6] == '':
                        seller5_info[6] = name_entry.get() + ' (I)'
                        seller5_info[5] = str(int(seller5_info[5]) + 1)
                    elif seller5_info[7] == '':
                        seller5_info[7] = name_entry.get() + ' (I)'
                        seller5_info[5] = str(int(seller5_info[5]) + 1)
                    elif seller5_info[8] == '':
                        seller5_info[8] = name_entry.get() + ' (I)'
                        seller5_info[5] = str(int(seller5_info[5]) + 1)
                    elif seller5_info[9] == '':
                        seller5_info[9] = name_entry.get() + ' (I)'
                        seller5_info[5] = str(int(seller5_info[5]) + 1)
                    elif seller5_info[10] == '':
                        seller5_info[10] = name_entry.get() + ' (I)'
                        seller5_info[5] = str(int(seller5_info[5]) + 1)
                    else:
                        print('You have challenged the Matrix')
                    
                    new_1 = seller1_info[0] + ',' + seller1_info[1] + ',' + seller1_info[2] + ',' + seller1_info[3] + ',' + seller1_info[4] + ',' + seller1_info[5] + ',' + seller1_info[6] + ',' + seller1_info[7] + ',' + seller1_info[8] + ',' + seller1_info[9] + ',' + seller1_info[10] + ',' + seller1_info[11] + ',' + seller1_info[12] 
                    new_2 = seller2_info[0] + ',' + seller2_info[1] + ',' + seller2_info[2] + ',' + seller2_info[3] + ',' + seller2_info[4] + ',' + seller2_info[5] + ',' + seller2_info[6] + ',' + seller2_info[7] + ',' + seller2_info[8] + ',' + seller2_info[9] + ',' + seller2_info[10] + ',' + seller2_info[11] + ',' + seller2_info[12] 
                    new_3 = seller3_info[0] + ',' + seller3_info[1] + ',' + seller3_info[2] + ',' + seller3_info[3] + ',' + seller3_info[4] + ',' + seller3_info[5] + ',' + seller3_info[6] + ',' + seller3_info[7] + ',' + seller3_info[8] + ',' + seller3_info[9] + ',' + seller3_info[10] + ',' + seller3_info[11] + ',' + seller3_info[12] 
                    new_4 = seller4_info[0] + ',' + seller4_info[1] + ',' + seller4_info[2] + ',' + seller4_info[3] + ',' + seller4_info[4] + ',' + seller4_info[5] + ',' + seller4_info[6] + ',' + seller4_info[7] + ',' + seller4_info[8] + ',' + seller4_info[9] + ',' + seller4_info[10] + ',' + seller4_info[11] + ',' + seller4_info[12] 
                    new_5 = seller5_info[0] + ',' + seller5_info[1] + ',' + seller5_info[2] + ',' + seller5_info[3] + ',' + seller5_info[4] + ',' + seller5_info[5] + ',' + seller5_info[6] + ',' + seller5_info[7] + ',' + seller5_info[8] + ',' + seller5_info[9] + ',' + seller5_info[10] + ',' + seller5_info[11] + ',' + seller5_info[12] 
                    new_6 = seller6_info[0] + ',' + seller6_info[1] + ',' + seller6_info[2] + ',' + seller6_info[3] + ',' + seller6_info[4] + ',' + seller6_info[5] + ',' + seller6_info[6] + ',' + seller6_info[7] + ',' + seller6_info[8] + ',' + seller6_info[9] + ',' + seller6_info[10] + ',' + seller6_info[11] + ',' + seller6_info[12] 
                    new_7 = seller7_info[0] + ',' + seller7_info[1] + ',' + seller7_info[2] + ',' + seller7_info[3] + ',' + seller7_info[4] + ',' + seller7_info[5] + ',' + seller7_info[6] + ',' + seller7_info[7] + ',' + seller7_info[8] + ',' + seller7_info[9] + ',' + seller7_info[10] + ',' + seller7_info[11] + ',' + seller7_info[12] 
                    new_8 = seller8_info[0] + ',' + seller8_info[1] + ',' + seller8_info[2] + ',' + seller8_info[3] + ',' + seller8_info[4] + ',' + seller8_info[5] + ',' + seller8_info[6] + ',' + seller8_info[7] + ',' + seller8_info[8] + ',' + seller8_info[9] + ',' + seller8_info[10] + ',' + seller8_info[11] + ',' + seller8_info[12]
                    new_9 = seller9_info[0] + ',' + seller9_info[1] + ',' + seller9_info[2] + ',' + seller9_info[3] + ',' + seller9_info[4] + ',' + seller9_info[5] + ',' + seller9_info[6] + ',' + seller9_info[7] + ',' + seller9_info[8] + ',' + seller9_info[9] + ',' + seller9_info[10] + ',' + seller9_info[11] + ',' + seller9_info[12] 
                    new_10 = seller10_info[0] + ',' + seller10_info[1] + ',' + seller10_info[2] + ',' + seller10_info[3] + ',' + seller10_info[4] + ',' + seller10_info[5] + ',' + seller10_info[6] + ',' + seller10_info[7] + ',' + seller10_info[8] + ',' + seller10_info[9] + ',' + seller10_info[10] + ',' + seller10_info[11] + ',' + seller10_info[12] 
                    f = open('sellers.txt', 'w')
                    g = f.close
                    h = open('sellers.txt', 'a')
                    write0 = h.write('#0-sellerid, 1-name, 2-lastname, 3-email, 4-website, 5-amountappsonsale, 6-app1, 7-app2, 8-app3, 9-app4, 10-app5, 11-downloadsUS, 12-downloadsCR' + '\n')
                    write1 = h.write(new_1)
                    write2 = h.write(new_2)
                    write3 = h.write(new_3)
                    write4 = h.write(new_4)
                    write5 = h.write(new_5)
                    write6 = h.write(new_6)
                    write7 = h.write(new_7)
                    write8 = h.write(new_8)
                    write9 = h.write(new_9)
                    write10 = h.write(new_10)
                    i = h.close

                    success_label = Label(add_game_window, text = 'Success', font = 'Helvetica 38', fg = 'firebrick3')
                    success_label.place(x=680, y=400)

                #labels para info de app que se quiera agregar
                appname_label = Label(add_game_window, text = 'Game Name', font = 'Helvetica 24')
                appname_label.place(x=100, y=50)

                desc1_label = Label(add_game_window, text = 'Description 1', font = 'Helvetica 24')
                desc1_label.place(x=100, y=100)

                desc2_label = Label(add_game_window, text = 'Description 2', font = 'Helvetica 24')
                desc2_label.place(x=100, y=150)

                desc3_label = Label(add_game_window, text = 'Description 3', font = 'Helvetica 24')
                desc3_label.place(x=100, y=200)

                desc4_label = Label(add_game_window, text = 'Description 4', font = 'Helvetica 24')
                desc4_label.place(x=100, y=250)

                desc5_label = Label(add_game_window, text = 'Description 5', font = 'Helvetica 24')
                desc5_label.place(x=100, y=300)

                desc1_esp_label = Label(add_game_window, text = 'Description 1 in Spanish', font = 'Helvetica 24')
                desc1_esp_label.place(x=100, y=350)

                desc2_esp_label = Label(add_game_window, text = 'Description 2 in Spanish', font = 'Helvetica 24')
                desc2_esp_label.place(x=100, y=400)

                desc3_esp_label = Label(add_game_window, text = 'Description 3 in Spanish', font = 'Helvetica 24')
                desc3_esp_label.place(x=100, y=450)

                desc4_esp_label = Label(add_game_window, text = 'Description 4 in Spanish', font = 'Helvetica 24')
                desc4_esp_label.place(x=100, y=500)

                desc5_esp_label = Label(add_game_window, text = 'Description 5 in Spanish', font = 'Helvetica 24')
                desc5_esp_label.place(x=100, y=550)

                price_label = Label(add_game_window, text = 'Price ($) or "Free"', font = 'Helvetica 24')
                price_label.place(x=600, y=50)

                appsize_label  = Label(add_game_window, text = 'App Size', font = 'Helvetica 24')
                appsize_label.place(x=600, y=100)

                #entries
                name_entry = Entry(add_game_window, width = 20)
                name_entry.place(x=400, y=50)

                desc1_entry = Entry(add_game_window, width = 20)
                desc1_entry.place(x=400, y=100)

                desc2_entry = Entry(add_game_window, width = 20)
                desc2_entry.place(x=400, y=150)

                desc3_entry = Entry(add_game_window, width = 20)
                desc3_entry.place(x=400, y=200)

                desc4_entry = Entry(add_game_window, width = 20)
                desc4_entry.place(x=400, y=250)

                desc5_entry = Entry(add_game_window, width = 20)
                desc5_entry.place(x=400, y=300)

                desc1_esp_entry = Entry(add_game_window, width = 20)
                desc1_esp_entry.place(x=400, y=350)

                desc2_esp_entry = Entry(add_game_window, width = 20)
                desc2_esp_entry.place(x=400, y=400)

                desc3_esp_entry = Entry(add_game_window, width = 20)
                desc3_esp_entry.place(x=400, y=450)

                desc4_esp_entry = Entry(add_game_window, width = 20)
                desc4_esp_entry.place(x=400, y=500)

                desc5_esp_entry = Entry(add_game_window, width = 20)
                desc5_esp_entry.place(x=400, y=550)

                price_entry = Entry(add_game_window, width = 20)
                price_entry.place(x=800, y=50)

                appsize_entry  = Entry(add_game_window, width = 20)
                appsize_entry.place(x=800, y=100)

                add_app_button = Button(add_game_window, text = 'Add Game', command = add_app)
                add_app_button.place(x=700, y=475)

                def back():
                    add_game_window.destroy()

                back_button = Button(add_game_window, image = exiticon, command = back)
                back_button.place(x=25,y=25)
                
                
            #labels de informacion
            name = Label(sellercanvas, text = seller5_info[1], font = 'Helvetica 24', fg = 'firebrick3')
            name.place(x=300, y=100)

            lastname = Label(sellercanvas, text = seller5_info[2], font = 'Helvetica 24', fg = 'firebrick3')
            lastname.place(x=300, y=200)

            email = Label(sellercanvas, text = seller5_info[3], font = 'Helvetica 24', fg = 'firebrick3')
            email.place(x=300, y=300)

            website = Label(sellercanvas, text = seller5_info[4], font = 'Helvetica 24', fg = 'firebrick3')
            website.place(x=300, y=400)

            amount_apps = Label(sellercanvas, text = seller5_info[5], font = 'Helvetica 24', fg = 'firebrick3')
            amount_apps.place(x=400, y=500)

            app1 = Label(sellercanvas, text = seller5_info[6], font = 'Helvetica 24', fg = 'firebrick3')
            app1.place(x=700, y=100)

            app1_downloads = Label(sellercanvas, text = 'Downloads US: '+app1_info[11]+'Downloads CR: '+app1_esp_info[11], font = 'Helvetica 16')
            app1_downloads.place(x=600, y=140)

            app2 = Label(sellercanvas, text = seller5_info[7], font = 'Helvetica 24', fg = 'firebrick3')
            app2.place(x=700, y=200)

            app2_downloads = Label(sellercanvas, text = 'Downloads US: '+game1_info[11]+'\n'+'Downloads CR: '+game1_esp_info[11], font = 'Helvetica 16')
            app2_downloads.place(x=600, y=240)

            app3 = Label(sellercanvas, text = seller5_info[8], font = 'Helvetica 24', fg = 'firebrick3')
            app3.place(x=700, y=300)

            app3_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app3_downloads.place(x=600, y=340)

            app4 = Label(sellercanvas, text = seller5_info[9], font = 'Helvetica 24', fg = 'firebrick3')
            app4.place(x=700, y=400)
            
            app4_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app4_downloads.place(x=600, y=440)

            app5 = Label(sellercanvas, text = seller5_info[10], font = 'Helvetica 24', fg = 'firebrick3')
            app5.place(x=700, y=500)

            app5_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app5_downloads.place(x=600, y=540)

            name_label = Label(sellercanvas, text  = 'Seller name:', font = 'Helvetica 24')
            name_label.place(x=100, y=100)

            lastname_label = Label(sellercanvas, text = 'Last Name:', font = 'Helvetica 24')
            lastname_label.place(x=100, y=200)

            email_label = Label(sellercanvas, text = 'Email:', font = 'Helvetica 24')
            email_label.place(x=100, y=300)

            website_label = Label(sellercanvas, text = 'Website:', font = 'Helvetica 24')
            website_label.place(x=100, y=400)

            amount_apps_label = Label(sellercanvas, text = 'Amount apps on sale', font = 'Helvetica 24')
            amount_apps_label.place(x=100, y=500)

            app1_label = Label(sellercanvas, text = 'App 1', font = 'Helvetica 24')
            app1_label.place(x=600, y=100)

            app2_label = Label(sellercanvas, text = 'App 2', font = 'Helvetica 24')
            app2_label.place(x=600, y=200)

            app3_label = Label(sellercanvas, text = 'App 3', font = 'Helvetica 24')
            app3_label.place(x=600, y=300)

            app4_label = Label(sellercanvas, text = 'App 4', font = 'Helvetica 24')
            app4_label.place(x=600, y=400)

            app5_label = Label(sellercanvas, text = 'App 5', font = 'Helvetica 24')
            app5_label.place(x=600, y=500)

            #boton para agregar apps
            add_app_button = Button(sellercanvas, text = 'Add app', font = 'Helvetica 24', command = add_app_window)
            add_app_button.place(x=650, y=50)

            add_game_button = Button(sellercanvas, text = 'Add game', font = 'Helvetica 24', command = add_game_window)
            add_game_button.place(x=850, y=50)

        #misma estructura que vendedor 1
        def seller6():
            seller6 = Toplevel()
            seller6.title('Admin App')
            seller6.minsize(1000,600)
            seller6.resizable(width=NO, height=NO)

            sellercanvas = Canvas(seller6, width = 1000, height = 600)
            sellercanvas.place(x=0,y=0)

            all_sellers = open('sellers.txt', 'r')
            read_sellers = all_sellers.readlines()
            seller6_line = read_sellers[6]
            seller6_info = seller6_line.split(',')
            
            apps = open('apps.txt', 'r')
            read_apps = apps.readlines()
            app1 = read_apps[7]
            app1_info = app1.split(',')

            apps_esp = open('apps_esp.txt', 'r')
            read_apps_esp = apps_esp.readlines()
            app1_esp = read_apps_esp[7]
            app1_esp_info = app1_esp.split(',')

            def back():
                seller6.destroy()

            back_button = Button(seller6, image = exiticon, command = back)
            back_button.place(x=25,y=25)

            def add_app_window():
                add_app_window = Toplevel()
                add_app_window.title('Admin App')
                add_app_window.minsize(1000,600)
                add_app_window.resizable(width=NO, height=NO)

                def add_app():
                    a = open ('appcount.txt','r+')
                    lastIndex = a.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    appname = name_entry.get()
                    desc1 = desc1_entry.get()
                    desc2 = desc2_entry.get()
                    desc3 = desc3_entry.get()
                    desc4 = desc4_entry.get()
                    desc5 = desc5_entry.get()
                    price = price_entry.get()
                    appsize = appsize_entry.get()
                    b = open('apps.txt','a')
                    info = '6' + ',' + productid + ',' + '0' + ',' + appname + ',' + desc1 + ',' + desc2 + ',' + desc3 + ',' + desc4 + ',' + desc5 + ',' + price + ',' + appsize + ',' + '0'
                    b.write('\n' + str(info))
                    a.close
                    b.close

                    c = open('appcount.txt','r+')
                    lastIndex = c.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    desc1_esp = desc1_esp_entry.get()
                    desc2_esp = desc2_esp_entry.get()
                    desc3_esp = desc3_esp_entry.get()
                    desc4_esp = desc4_esp_entry.get()
                    desc5_esp = desc5_esp_entry.get()
                    d = open('apps_esp.txt','a')
                    info = '6' + ',' + productid + ',' + '0' + ',' + appname + ',' + desc1_esp + ',' + desc2_esp + ',' + desc3_esp + ',' + desc4_esp + ',' + desc5_esp + ',' + price + ',' + appsize + ',' + '0'
                    d.write('\n' + str(info))
                    c.write('\n' + str(int(productid) + 1))
                    c.close
                    d.close

                    e = open('sellers.txt', 'r+')
                    read_seller_info = e.readlines()
                    seller1_line = read_seller_info[1]
                    seller1_info = seller1_line.split(',')
                    seller2_line = read_seller_info[2]
                    seller2_info = seller2_line.split(',')
                    seller3_line = read_seller_info[3]
                    seller3_info = seller3_line.split(',')
                    seller4_line = read_seller_info[4]
                    seller4_info = seller4_line.split(',')
                    seller5_line = read_seller_info[5]
                    seller5_info = seller5_line.split(',')
                    seller6_line = read_seller_info[6]
                    seller6_info = seller6_line.split(',')
                    seller7_line = read_seller_info[7]
                    seller7_info = seller7_line.split(',')
                    seller8_line = read_seller_info[8]
                    seller8_info = seller8_line.split(',')
                    seller9_line = read_seller_info[9]
                    seller9_info = seller9_line.split(',')
                    seller10_line = read_seller_info[10]
                    seller10_info = seller10_line.split(',')

                    if seller6_info[6] == '':
                        seller6_info[6] = name_entry.get() + ' (I)'
                        seller6_info[5] = str(int(seller6_info[5]) + 1)
                    elif seller6_info[7] == '':
                        seller6_info[7] = name_entry.get() + ' (I)'
                        seller6_info[5] = str(int(seller6_info[5]) + 1)
                    elif seller6_info[8] == '':
                        seller6_info[8] = name_entry.get() + ' (I)'
                        seller6_info[5] = str(int(seller6_info[5]) + 1)
                    elif seller6_info[9] == '':
                        seller6_info[9] = name_entry.get() + ' (I)'
                        seller6_info[5] = str(int(seller6_info[5]) + 1)
                    elif seller6_info[10] == '':
                        seller6_info[10] = name_entry.get() + ' (I)'
                        seller6_info[5] = str(int(seller6_info[5]) + 1)
                    else:
                        print('You have challenged the Matrix')
                    
                    new_1 = seller1_info[0] + ',' + seller1_info[1] + ',' + seller1_info[2] + ',' + seller1_info[3] + ',' + seller1_info[4] + ',' + seller1_info[5] + ',' + seller1_info[6] + ',' + seller1_info[7] + ',' + seller1_info[8] + ',' + seller1_info[9] + ',' + seller1_info[10] + ',' + seller1_info[11] + ',' + seller1_info[12] 
                    new_2 = seller2_info[0] + ',' + seller2_info[1] + ',' + seller2_info[2] + ',' + seller2_info[3] + ',' + seller2_info[4] + ',' + seller2_info[5] + ',' + seller2_info[6] + ',' + seller2_info[7] + ',' + seller2_info[8] + ',' + seller2_info[9] + ',' + seller2_info[10] + ',' + seller2_info[11] + ',' + seller2_info[12] 
                    new_3 = seller3_info[0] + ',' + seller3_info[1] + ',' + seller3_info[2] + ',' + seller3_info[3] + ',' + seller3_info[4] + ',' + seller3_info[5] + ',' + seller3_info[6] + ',' + seller3_info[7] + ',' + seller3_info[8] + ',' + seller3_info[9] + ',' + seller3_info[10] + ',' + seller3_info[11] + ',' + seller3_info[12] 
                    new_4 = seller4_info[0] + ',' + seller4_info[1] + ',' + seller4_info[2] + ',' + seller4_info[3] + ',' + seller4_info[4] + ',' + seller4_info[5] + ',' + seller4_info[6] + ',' + seller4_info[7] + ',' + seller4_info[8] + ',' + seller4_info[9] + ',' + seller4_info[10] + ',' + seller4_info[11] + ',' + seller4_info[12] 
                    new_5 = seller5_info[0] + ',' + seller5_info[1] + ',' + seller5_info[2] + ',' + seller5_info[3] + ',' + seller5_info[4] + ',' + seller5_info[5] + ',' + seller5_info[6] + ',' + seller5_info[7] + ',' + seller5_info[8] + ',' + seller5_info[9] + ',' + seller5_info[10] + ',' + seller5_info[11] + ',' + seller5_info[12] 
                    new_6 = seller6_info[0] + ',' + seller6_info[1] + ',' + seller6_info[2] + ',' + seller6_info[3] + ',' + seller6_info[4] + ',' + seller6_info[5] + ',' + seller6_info[6] + ',' + seller6_info[7] + ',' + seller6_info[8] + ',' + seller6_info[9] + ',' + seller6_info[10] + ',' + seller6_info[11] + ',' + seller6_info[12] 
                    new_7 = seller7_info[0] + ',' + seller7_info[1] + ',' + seller7_info[2] + ',' + seller7_info[3] + ',' + seller7_info[4] + ',' + seller7_info[5] + ',' + seller7_info[6] + ',' + seller7_info[7] + ',' + seller7_info[8] + ',' + seller7_info[9] + ',' + seller7_info[10] + ',' + seller7_info[11] + ',' + seller7_info[12] 
                    new_8 = seller8_info[0] + ',' + seller8_info[1] + ',' + seller8_info[2] + ',' + seller8_info[3] + ',' + seller8_info[4] + ',' + seller8_info[5] + ',' + seller8_info[6] + ',' + seller8_info[7] + ',' + seller8_info[8] + ',' + seller8_info[9] + ',' + seller8_info[10] + ',' + seller8_info[11] + ',' + seller8_info[12]
                    new_9 = seller9_info[0] + ',' + seller9_info[1] + ',' + seller9_info[2] + ',' + seller9_info[3] + ',' + seller9_info[4] + ',' + seller9_info[5] + ',' + seller9_info[6] + ',' + seller9_info[7] + ',' + seller9_info[8] + ',' + seller9_info[9] + ',' + seller9_info[10] + ',' + seller9_info[11] + ',' + seller9_info[12] 
                    new_10 = seller10_info[0] + ',' + seller10_info[1] + ',' + seller10_info[2] + ',' + seller10_info[3] + ',' + seller10_info[4] + ',' + seller10_info[5] + ',' + seller10_info[6] + ',' + seller10_info[7] + ',' + seller10_info[8] + ',' + seller10_info[9] + ',' + seller10_info[10] + ',' + seller10_info[11] + ',' + seller10_info[12] 
                    f = open('sellers.txt', 'w')
                    g = f.close
                    h = open('sellers.txt', 'a')
                    write0 = h.write('#0-sellerid, 1-name, 2-lastname, 3-email, 4-website, 5-amountappsonsale, 6-app1, 7-app2, 8-app3, 9-app4, 10-app5, 11-downloadsUS, 12-downloadsCR' + '\n')
                    write1 = h.write(new_1)
                    write2 = h.write(new_2)
                    write3 = h.write(new_3)
                    write4 = h.write(new_4)
                    write5 = h.write(new_5)
                    write6 = h.write(new_6)
                    write7 = h.write(new_7)
                    write8 = h.write(new_8)
                    write9 = h.write(new_9)
                    write10 = h.write(new_10)
                    i = h.close

                    success_label = Label(add_app_window, text = 'Success', font = 'Helvetica 38', fg = 'firebrick3')
                    success_label.place(x=680, y=400)

                #labels para info de app que se quiera agregar
                appname_label = Label(add_app_window, text = 'App Name', font = 'Helvetica 24')
                appname_label.place(x=100, y=50)

                desc1_label = Label(add_app_window, text = 'Description 1', font = 'Helvetica 24')
                desc1_label.place(x=100, y=100)

                desc2_label = Label(add_app_window, text = 'Description 2', font = 'Helvetica 24')
                desc2_label.place(x=100, y=150)

                desc3_label = Label(add_app_window, text = 'Description 3', font = 'Helvetica 24')
                desc3_label.place(x=100, y=200)

                desc4_label = Label(add_app_window, text = 'Description 4', font = 'Helvetica 24')
                desc4_label.place(x=100, y=250)

                desc5_label = Label(add_app_window, text = 'Description 5', font = 'Helvetica 24')
                desc5_label.place(x=100, y=300)

                desc1_esp_label = Label(add_app_window, text = 'Description 1 in Spanish', font = 'Helvetica 24')
                desc1_esp_label.place(x=100, y=350)

                desc2_esp_label = Label(add_app_window, text = 'Description 2 in Spanish', font = 'Helvetica 24')
                desc2_esp_label.place(x=100, y=400)

                desc3_esp_label = Label(add_app_window, text = 'Description 3 in Spanish', font = 'Helvetica 24')
                desc3_esp_label.place(x=100, y=450)

                desc4_esp_label = Label(add_app_window, text = 'Description 4 in Spanish', font = 'Helvetica 24')
                desc4_esp_label.place(x=100, y=500)

                desc5_esp_label = Label(add_app_window, text = 'Description 5 in Spanish', font = 'Helvetica 24')
                desc5_esp_label.place(x=100, y=550)

                price_label = Label(add_app_window, text = 'Price ($) or "Free"', font = 'Helvetica 24')
                price_label.place(x=600, y=50)

                appsize_label  = Label(add_app_window, text = 'App Size', font = 'Helvetica 24')
                appsize_label.place(x=600, y=100)

                #entries
                name_entry = Entry(add_app_window, width = 20)
                name_entry.place(x=400, y=50)

                desc1_entry = Entry(add_app_window, width = 20)
                desc1_entry.place(x=400, y=100)

                desc2_entry = Entry(add_app_window, width = 20)
                desc2_entry.place(x=400, y=150)

                desc3_entry = Entry(add_app_window, width = 20)
                desc3_entry.place(x=400, y=200)

                desc4_entry = Entry(add_app_window, width = 20)
                desc4_entry.place(x=400, y=250)

                desc5_entry = Entry(add_app_window, width = 20)
                desc5_entry.place(x=400, y=300)

                desc1_esp_entry = Entry(add_app_window, width = 20)
                desc1_esp_entry.place(x=400, y=350)

                desc2_esp_entry = Entry(add_app_window, width = 20)
                desc2_esp_entry.place(x=400, y=400)

                desc3_esp_entry = Entry(add_app_window, width = 20)
                desc3_esp_entry.place(x=400, y=450)

                desc4_esp_entry = Entry(add_app_window, width = 20)
                desc4_esp_entry.place(x=400, y=500)

                desc5_esp_entry = Entry(add_app_window, width = 20)
                desc5_esp_entry.place(x=400, y=550)

                price_entry = Entry(add_app_window, width = 20)
                price_entry.place(x=800, y=50)

                appsize_entry  = Entry(add_app_window, width = 20)
                appsize_entry.place(x=800, y=100)

                add_app_button = Button(add_app_window, text = 'Add App', command = add_app)
                add_app_button.place(x=700, y=475)

                def back():
                    add_app_window.destroy()

                back_button = Button(add_app_window, image = exiticon, command = back)
                back_button.place(x=25,y=25)

            def add_game_window():
                add_game_window = Toplevel()
                add_game_window.title('Admin App')
                add_game_window.minsize(1000,600)
                add_game_window.resizable(width=NO, height=NO)

                def add_app():
                    a = open ('appcount.txt','r+')
                    lastIndex = a.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    appname = name_entry.get()
                    desc1 = desc1_entry.get()
                    desc2 = desc2_entry.get()
                    desc3 = desc3_entry.get()
                    desc4 = desc4_entry.get()
                    desc5 = desc5_entry.get()
                    price = price_entry.get()
                    appsize = appsize_entry.get()
                    b = open('games.txt','a')
                    info = '6' + ',' + productid + ',' + '1' + ',' + appname + ',' + desc1 + ',' + desc2 + ',' + desc3 + ',' + desc4 + ',' + desc5 + ',' + price + ',' + appsize + ',' + '0'
                    b.write('\n' + str(info))
                    a.close
                    b.close

                    c = open('appcount.txt','r+')
                    lastIndex = c.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    desc1_esp = desc1_esp_entry.get()
                    desc2_esp = desc2_esp_entry.get()
                    desc3_esp = desc3_esp_entry.get()
                    desc4_esp = desc4_esp_entry.get()
                    desc5_esp = desc5_esp_entry.get()
                    d = open('games_esp.txt','a')
                    info = '6' + ',' + productid + ',' + '1' + ',' + appname + ',' + desc1_esp + ',' + desc2_esp + ',' + desc3_esp + ',' + desc4_esp + ',' + desc5_esp + ',' + price + ',' + appsize + ',' + '0'
                    d.write('\n' + str(info))
                    c.write('\n' + str(int(productid) + 1))
                    c.close
                    d.close

                    e = open('sellers.txt', 'r+')
                    read_seller_info = e.readlines()
                    seller1_line = read_seller_info[1]
                    seller1_info = seller1_line.split(',')
                    seller2_line = read_seller_info[2]
                    seller2_info = seller2_line.split(',')
                    seller3_line = read_seller_info[3]
                    seller3_info = seller3_line.split(',')
                    seller4_line = read_seller_info[4]
                    seller4_info = seller4_line.split(',')
                    seller5_line = read_seller_info[5]
                    seller5_info = seller5_line.split(',')
                    seller6_line = read_seller_info[6]
                    seller6_info = seller6_line.split(',')
                    seller7_line = read_seller_info[7]
                    seller7_info = seller7_line.split(',')
                    seller8_line = read_seller_info[8]
                    seller8_info = seller8_line.split(',')
                    seller9_line = read_seller_info[9]
                    seller9_info = seller9_line.split(',')
                    seller10_line = read_seller_info[10]
                    seller10_info = seller10_line.split(',')

                    if seller6_info[6] == '':
                        seller6_info[6] = name_entry.get() + ' (I)'
                        seller6_info[5] = str(int(seller6_info[5]) + 1)
                    elif seller6_info[7] == '':
                        seller6_info[7] = name_entry.get() + ' (I)'
                        seller6_info[5] = str(int(seller6_info[5]) + 1)
                    elif seller6_info[8] == '':
                        seller6_info[8] = name_entry.get() + ' (I)'
                        seller6_info[5] = str(int(seller6_info[5]) + 1)
                    elif seller6_info[9] == '':
                        seller6_info[9] = name_entry.get() + ' (I)'
                        seller6_info[5] = str(int(seller6_info[5]) + 1)
                    elif seller6_info[10] == '':
                        seller6_info[10] = name_entry.get() + ' (I)'
                        seller6_info[5] = str(int(seller6_info[5]) + 1)
                    else:
                        print('You have challenged the Matrix')
                    
                    new_1 = seller1_info[0] + ',' + seller1_info[1] + ',' + seller1_info[2] + ',' + seller1_info[3] + ',' + seller1_info[4] + ',' + seller1_info[5] + ',' + seller1_info[6] + ',' + seller1_info[7] + ',' + seller1_info[8] + ',' + seller1_info[9] + ',' + seller1_info[10] + ',' + seller1_info[11] + ',' + seller1_info[12] 
                    new_2 = seller2_info[0] + ',' + seller2_info[1] + ',' + seller2_info[2] + ',' + seller2_info[3] + ',' + seller2_info[4] + ',' + seller2_info[5] + ',' + seller2_info[6] + ',' + seller2_info[7] + ',' + seller2_info[8] + ',' + seller2_info[9] + ',' + seller2_info[10] + ',' + seller2_info[11] + ',' + seller2_info[12] 
                    new_3 = seller3_info[0] + ',' + seller3_info[1] + ',' + seller3_info[2] + ',' + seller3_info[3] + ',' + seller3_info[4] + ',' + seller3_info[5] + ',' + seller3_info[6] + ',' + seller3_info[7] + ',' + seller3_info[8] + ',' + seller3_info[9] + ',' + seller3_info[10] + ',' + seller3_info[11] + ',' + seller3_info[12] 
                    new_4 = seller4_info[0] + ',' + seller4_info[1] + ',' + seller4_info[2] + ',' + seller4_info[3] + ',' + seller4_info[4] + ',' + seller4_info[5] + ',' + seller4_info[6] + ',' + seller4_info[7] + ',' + seller4_info[8] + ',' + seller4_info[9] + ',' + seller4_info[10] + ',' + seller4_info[11] + ',' + seller4_info[12] 
                    new_5 = seller5_info[0] + ',' + seller5_info[1] + ',' + seller5_info[2] + ',' + seller5_info[3] + ',' + seller5_info[4] + ',' + seller5_info[5] + ',' + seller5_info[6] + ',' + seller5_info[7] + ',' + seller5_info[8] + ',' + seller5_info[9] + ',' + seller5_info[10] + ',' + seller5_info[11] + ',' + seller5_info[12] 
                    new_6 = seller6_info[0] + ',' + seller6_info[1] + ',' + seller6_info[2] + ',' + seller6_info[3] + ',' + seller6_info[4] + ',' + seller6_info[5] + ',' + seller6_info[6] + ',' + seller6_info[7] + ',' + seller6_info[8] + ',' + seller6_info[9] + ',' + seller6_info[10] + ',' + seller6_info[11] + ',' + seller6_info[12] 
                    new_7 = seller7_info[0] + ',' + seller7_info[1] + ',' + seller7_info[2] + ',' + seller7_info[3] + ',' + seller7_info[4] + ',' + seller7_info[5] + ',' + seller7_info[6] + ',' + seller7_info[7] + ',' + seller7_info[8] + ',' + seller7_info[9] + ',' + seller7_info[10] + ',' + seller7_info[11] + ',' + seller7_info[12] 
                    new_8 = seller8_info[0] + ',' + seller8_info[1] + ',' + seller8_info[2] + ',' + seller8_info[3] + ',' + seller8_info[4] + ',' + seller8_info[5] + ',' + seller8_info[6] + ',' + seller8_info[7] + ',' + seller8_info[8] + ',' + seller8_info[9] + ',' + seller8_info[10] + ',' + seller8_info[11] + ',' + seller8_info[12]
                    new_9 = seller9_info[0] + ',' + seller9_info[1] + ',' + seller9_info[2] + ',' + seller9_info[3] + ',' + seller9_info[4] + ',' + seller9_info[5] + ',' + seller9_info[6] + ',' + seller9_info[7] + ',' + seller9_info[8] + ',' + seller9_info[9] + ',' + seller9_info[10] + ',' + seller9_info[11] + ',' + seller9_info[12] 
                    new_10 = seller10_info[0] + ',' + seller10_info[1] + ',' + seller10_info[2] + ',' + seller10_info[3] + ',' + seller10_info[4] + ',' + seller10_info[5] + ',' + seller10_info[6] + ',' + seller10_info[7] + ',' + seller10_info[8] + ',' + seller10_info[9] + ',' + seller10_info[10] + ',' + seller10_info[11] + ',' + seller10_info[12] 
                    f = open('sellers.txt', 'w')
                    g = f.close
                    h = open('sellers.txt', 'a')
                    write0 = h.write('#0-sellerid, 1-name, 2-lastname, 3-email, 4-website, 5-amountappsonsale, 6-app1, 7-app2, 8-app3, 9-app4, 10-app5, 11-downloadsUS, 12-downloadsCR' + '\n')
                    write1 = h.write(new_1)
                    write2 = h.write(new_2)
                    write3 = h.write(new_3)
                    write4 = h.write(new_4)
                    write5 = h.write(new_5)
                    write6 = h.write(new_6)
                    write7 = h.write(new_7)
                    write8 = h.write(new_8)
                    write9 = h.write(new_9)
                    write10 = h.write(new_10)
                    i = h.close

                    success_label = Label(add_game_window, text = 'Success', font = 'Helvetica 38', fg = 'firebrick3')
                    success_label.place(x=680, y=400)

                #labels para info de app que se quiera agregar
                appname_label = Label(add_game_window, text = 'Game Name', font = 'Helvetica 24')
                appname_label.place(x=100, y=50)

                desc1_label = Label(add_game_window, text = 'Description 1', font = 'Helvetica 24')
                desc1_label.place(x=100, y=100)

                desc2_label = Label(add_game_window, text = 'Description 2', font = 'Helvetica 24')
                desc2_label.place(x=100, y=150)

                desc3_label = Label(add_game_window, text = 'Description 3', font = 'Helvetica 24')
                desc3_label.place(x=100, y=200)

                desc4_label = Label(add_game_window, text = 'Description 4', font = 'Helvetica 24')
                desc4_label.place(x=100, y=250)

                desc5_label = Label(add_game_window, text = 'Description 5', font = 'Helvetica 24')
                desc5_label.place(x=100, y=300)

                desc1_esp_label = Label(add_game_window, text = 'Description 1 in Spanish', font = 'Helvetica 24')
                desc1_esp_label.place(x=100, y=350)

                desc2_esp_label = Label(add_game_window, text = 'Description 2 in Spanish', font = 'Helvetica 24')
                desc2_esp_label.place(x=100, y=400)

                desc3_esp_label = Label(add_game_window, text = 'Description 3 in Spanish', font = 'Helvetica 24')
                desc3_esp_label.place(x=100, y=450)

                desc4_esp_label = Label(add_game_window, text = 'Description 4 in Spanish', font = 'Helvetica 24')
                desc4_esp_label.place(x=100, y=500)

                desc5_esp_label = Label(add_game_window, text = 'Description 5 in Spanish', font = 'Helvetica 24')
                desc5_esp_label.place(x=100, y=550)

                price_label = Label(add_game_window, text = 'Price ($) or "Free"', font = 'Helvetica 24')
                price_label.place(x=600, y=50)

                appsize_label  = Label(add_game_window, text = 'App Size', font = 'Helvetica 24')
                appsize_label.place(x=600, y=100)

                #entries
                name_entry = Entry(add_game_window, width = 20)
                name_entry.place(x=400, y=50)

                desc1_entry = Entry(add_game_window, width = 20)
                desc1_entry.place(x=400, y=100)

                desc2_entry = Entry(add_game_window, width = 20)
                desc2_entry.place(x=400, y=150)

                desc3_entry = Entry(add_game_window, width = 20)
                desc3_entry.place(x=400, y=200)

                desc4_entry = Entry(add_game_window, width = 20)
                desc4_entry.place(x=400, y=250)

                desc5_entry = Entry(add_game_window, width = 20)
                desc5_entry.place(x=400, y=300)

                desc1_esp_entry = Entry(add_game_window, width = 20)
                desc1_esp_entry.place(x=400, y=350)

                desc2_esp_entry = Entry(add_game_window, width = 20)
                desc2_esp_entry.place(x=400, y=400)

                desc3_esp_entry = Entry(add_game_window, width = 20)
                desc3_esp_entry.place(x=400, y=450)

                desc4_esp_entry = Entry(add_game_window, width = 20)
                desc4_esp_entry.place(x=400, y=500)

                desc5_esp_entry = Entry(add_game_window, width = 20)
                desc5_esp_entry.place(x=400, y=550)

                price_entry = Entry(add_game_window, width = 20)
                price_entry.place(x=800, y=50)

                appsize_entry  = Entry(add_game_window, width = 20)
                appsize_entry.place(x=800, y=100)

                add_app_button = Button(add_game_window, text = 'Add Game', command = add_app)
                add_app_button.place(x=700, y=475)

                def back():
                    add_game_window.destroy()

                back_button = Button(add_game_window, image = exiticon, command = back)
                back_button.place(x=25,y=25)
                
                
            #labels de informacion
            name = Label(sellercanvas, text = seller6_info[1], font = 'Helvetica 24', fg = 'firebrick3')
            name.place(x=300, y=100)

            lastname = Label(sellercanvas, text = seller6_info[2], font = 'Helvetica 24', fg = 'firebrick3')
            lastname.place(x=300, y=200)

            email = Label(sellercanvas, text = seller6_info[3], font = 'Helvetica 24', fg = 'firebrick3')
            email.place(x=300, y=300)

            website = Label(sellercanvas, text = seller6_info[4], font = 'Helvetica 24', fg = 'firebrick3')
            website.place(x=300, y=400)

            amount_apps = Label(sellercanvas, text = seller6_info[5], font = 'Helvetica 24', fg = 'firebrick3')
            amount_apps.place(x=400, y=500)

            app1 = Label(sellercanvas, text = seller6_info[6], font = 'Helvetica 24', fg = 'firebrick3')
            app1.place(x=700, y=100)

            app1_downloads = Label(sellercanvas, text = 'Downloads US: '+app1_info[11]+'Downloads CR: '+app1_esp_info[11], font = 'Helvetica 16')
            app1_downloads.place(x=600, y=140)

            app2 = Label(sellercanvas, text = seller6_info[7], font = 'Helvetica 24', fg = 'firebrick3')
            app2.place(x=700, y=200)

            app2_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app2_downloads.place(x=600, y=240)

            app3 = Label(sellercanvas, text = seller6_info[8], font = 'Helvetica 24', fg = 'firebrick3')
            app3.place(x=700, y=300)

            app3_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app3_downloads.place(x=600, y=340)

            app4 = Label(sellercanvas, text = seller6_info[9], font = 'Helvetica 24', fg = 'firebrick3')
            app4.place(x=700, y=400)
            
            app4_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app4_downloads.place(x=600, y=440)

            app5 = Label(sellercanvas, text = seller6_info[10], font = 'Helvetica 24', fg = 'firebrick3')
            app5.place(x=700, y=500)

            app5_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app5_downloads.place(x=600, y=540)

            name_label = Label(sellercanvas, text  = 'Seller name:', font = 'Helvetica 24')
            name_label.place(x=100, y=100)

            lastname_label = Label(sellercanvas, text = 'Last Name:', font = 'Helvetica 24')
            lastname_label.place(x=100, y=200)

            email_label = Label(sellercanvas, text = 'Email:', font = 'Helvetica 24')
            email_label.place(x=100, y=300)

            website_label = Label(sellercanvas, text = 'Website:', font = 'Helvetica 24')
            website_label.place(x=100, y=400)

            amount_apps_label = Label(sellercanvas, text = 'Amount apps on sale', font = 'Helvetica 24')
            amount_apps_label.place(x=100, y=500)

            app1_label = Label(sellercanvas, text = 'App 1', font = 'Helvetica 24')
            app1_label.place(x=600, y=100)

            app2_label = Label(sellercanvas, text = 'App 2', font = 'Helvetica 24')
            app2_label.place(x=600, y=200)

            app3_label = Label(sellercanvas, text = 'App 3', font = 'Helvetica 24')
            app3_label.place(x=600, y=300)

            app4_label = Label(sellercanvas, text = 'App 4', font = 'Helvetica 24')
            app4_label.place(x=600, y=400)

            app5_label = Label(sellercanvas, text = 'App 5', font = 'Helvetica 24')
            app5_label.place(x=600, y=500)

            #boton para agregar apps
            add_app_button = Button(sellercanvas, text = 'Add app', font = 'Helvetica 24', command = add_app_window)
            add_app_button.place(x=650, y=50)

            add_game_button = Button(sellercanvas, text = 'Add game', font = 'Helvetica 24', command = add_game_window)
            add_game_button.place(x=850, y=50)

        #misma estructura que vendedor 1
        def seller7():
            seller7 = Toplevel()
            seller7.title('Admin App')
            seller7.minsize(1000,600)
            seller7.resizable(width=NO, height=NO)

            sellercanvas = Canvas(seller7, width = 1000, height = 600)
            sellercanvas.place(x=0,y=0)

            all_sellers = open('sellers.txt', 'r')
            read_sellers = all_sellers.readlines()
            seller7_line = read_sellers[7]
            seller7_info = seller7_line.split(',')

            games = open('games.txt', 'r')
            read_games = games.readlines()
            game1 = read_games[2]
            game1_info = game1.split(',')
            game2 = read_games[3]
            game2_info = game2.split(',')
            game3 = read_games[6]
            game3_info = game3.split(',')

            games_esp = open('games_esp.txt', 'r')
            read_games_esp = games_esp.readlines()
            game1_esp = read_games_esp[2]
            game1_esp_info = game1_esp.split(',')
            game2_esp = read_games_esp[3]
            game2_esp_info = game2_esp.split(',')
            game3_esp = read_games_esp[6]
            game3_esp_info = game3_esp.split(',')

            def back():
                seller7.destroy()

            back_button = Button(seller7, image = exiticon, command = back)
            back_button.place(x=25,y=25)

            def add_app_window():
                add_app_window = Toplevel()
                add_app_window.title('Admin App')
                add_app_window.minsize(1000,600)
                add_app_window.resizable(width=NO, height=NO)

                def add_app():
                    a = open ('appcount.txt','r+')
                    lastIndex = a.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    appname = name_entry.get()
                    desc1 = desc1_entry.get()
                    desc2 = desc2_entry.get()
                    desc3 = desc3_entry.get()
                    desc4 = desc4_entry.get()
                    desc5 = desc5_entry.get()
                    price = price_entry.get()
                    appsize = appsize_entry.get()
                    b = open('apps.txt','a')
                    info = '7' + ',' + productid + ',' + '0' + ',' + appname + ',' + desc1 + ',' + desc2 + ',' + desc3 + ',' + desc4 + ',' + desc5 + ',' + price + ',' + appsize + ',' + '0'
                    b.write('\n' + str(info))
                    a.close
                    b.close

                    c = open('appcount.txt','r+')
                    lastIndex = c.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    desc1_esp = desc1_esp_entry.get()
                    desc2_esp = desc2_esp_entry.get()
                    desc3_esp = desc3_esp_entry.get()
                    desc4_esp = desc4_esp_entry.get()
                    desc5_esp = desc5_esp_entry.get()
                    d = open('apps_esp.txt','a')
                    info = '7' + ',' + productid + ',' + '0' + ',' + appname + ',' + desc1_esp + ',' + desc2_esp + ',' + desc3_esp + ',' + desc4_esp + ',' + desc5_esp + ',' + price + ',' + appsize + ',' + '0'
                    d.write('\n' + str(info))
                    c.write('\n' + str(int(productid) + 1))
                    c.close
                    d.close

                    e = open('sellers.txt', 'r+')
                    read_seller_info = e.readlines()
                    seller1_line = read_seller_info[1]
                    seller1_info = seller1_line.split(',')
                    seller2_line = read_seller_info[2]
                    seller2_info = seller2_line.split(',')
                    seller3_line = read_seller_info[3]
                    seller3_info = seller3_line.split(',')
                    seller4_line = read_seller_info[4]
                    seller4_info = seller4_line.split(',')
                    seller5_line = read_seller_info[5]
                    seller5_info = seller5_line.split(',')
                    seller6_line = read_seller_info[6]
                    seller6_info = seller6_line.split(',')
                    seller7_line = read_seller_info[7]
                    seller7_info = seller7_line.split(',')
                    seller8_line = read_seller_info[8]
                    seller8_info = seller8_line.split(',')
                    seller9_line = read_seller_info[9]
                    seller9_info = seller9_line.split(',')
                    seller10_line = read_seller_info[10]
                    seller10_info = seller10_line.split(',')

                    if seller7_info[6] == '':
                        seller7_info[6] = name_entry.get() + ' (I)'
                        seller7_info[5] = str(int(seller7_info[5]) + 1)
                    elif seller7_info[7] == '':
                        seller7_info[7] = name_entry.get() + ' (I)'
                        seller7_info[5] = str(int(seller7_info[5]) + 1)
                    elif seller7_info[8] == '':
                        seller7_info[8] = name_entry.get() + ' (I)'
                        seller7_info[5] = str(int(seller7_info[5]) + 1)
                    elif seller7_info[9] == '':
                        seller7_info[9] = name_entry.get() + ' (I)'
                        seller7_info[5] = str(int(seller7_info[5]) + 1)
                    elif seller7_info[10] == '':
                        seller7_info[10] = name_entry.get() + ' (I)'
                        seller7_info[5] = str(int(seller7_info[5]) + 1)
                    else:
                        print('You have challenged the Matrix')
                    
                    new_1 = seller1_info[0] + ',' + seller1_info[1] + ',' + seller1_info[2] + ',' + seller1_info[3] + ',' + seller1_info[4] + ',' + seller1_info[5] + ',' + seller1_info[6] + ',' + seller1_info[7] + ',' + seller1_info[8] + ',' + seller1_info[9] + ',' + seller1_info[10] + ',' + seller1_info[11] + ',' + seller1_info[12] 
                    new_2 = seller2_info[0] + ',' + seller2_info[1] + ',' + seller2_info[2] + ',' + seller2_info[3] + ',' + seller2_info[4] + ',' + seller2_info[5] + ',' + seller2_info[6] + ',' + seller2_info[7] + ',' + seller2_info[8] + ',' + seller2_info[9] + ',' + seller2_info[10] + ',' + seller2_info[11] + ',' + seller2_info[12] 
                    new_3 = seller3_info[0] + ',' + seller3_info[1] + ',' + seller3_info[2] + ',' + seller3_info[3] + ',' + seller3_info[4] + ',' + seller3_info[5] + ',' + seller3_info[6] + ',' + seller3_info[7] + ',' + seller3_info[8] + ',' + seller3_info[9] + ',' + seller3_info[10] + ',' + seller3_info[11] + ',' + seller3_info[12] 
                    new_4 = seller4_info[0] + ',' + seller4_info[1] + ',' + seller4_info[2] + ',' + seller4_info[3] + ',' + seller4_info[4] + ',' + seller4_info[5] + ',' + seller4_info[6] + ',' + seller4_info[7] + ',' + seller4_info[8] + ',' + seller4_info[9] + ',' + seller4_info[10] + ',' + seller4_info[11] + ',' + seller4_info[12] 
                    new_5 = seller5_info[0] + ',' + seller5_info[1] + ',' + seller5_info[2] + ',' + seller5_info[3] + ',' + seller5_info[4] + ',' + seller5_info[5] + ',' + seller5_info[6] + ',' + seller5_info[7] + ',' + seller5_info[8] + ',' + seller5_info[9] + ',' + seller5_info[10] + ',' + seller5_info[11] + ',' + seller5_info[12] 
                    new_6 = seller6_info[0] + ',' + seller6_info[1] + ',' + seller6_info[2] + ',' + seller6_info[3] + ',' + seller6_info[4] + ',' + seller6_info[5] + ',' + seller6_info[6] + ',' + seller6_info[7] + ',' + seller6_info[8] + ',' + seller6_info[9] + ',' + seller6_info[10] + ',' + seller6_info[11] + ',' + seller6_info[12] 
                    new_7 = seller7_info[0] + ',' + seller7_info[1] + ',' + seller7_info[2] + ',' + seller7_info[3] + ',' + seller7_info[4] + ',' + seller7_info[5] + ',' + seller7_info[6] + ',' + seller7_info[7] + ',' + seller7_info[8] + ',' + seller7_info[9] + ',' + seller7_info[10] + ',' + seller7_info[11] + ',' + seller7_info[12] 
                    new_8 = seller8_info[0] + ',' + seller8_info[1] + ',' + seller8_info[2] + ',' + seller8_info[3] + ',' + seller8_info[4] + ',' + seller8_info[5] + ',' + seller8_info[6] + ',' + seller8_info[7] + ',' + seller8_info[8] + ',' + seller8_info[9] + ',' + seller8_info[10] + ',' + seller8_info[11] + ',' + seller8_info[12]
                    new_9 = seller9_info[0] + ',' + seller9_info[1] + ',' + seller9_info[2] + ',' + seller9_info[3] + ',' + seller9_info[4] + ',' + seller9_info[5] + ',' + seller9_info[6] + ',' + seller9_info[7] + ',' + seller9_info[8] + ',' + seller9_info[9] + ',' + seller9_info[10] + ',' + seller9_info[11] + ',' + seller9_info[12] 
                    new_10 = seller10_info[0] + ',' + seller10_info[1] + ',' + seller10_info[2] + ',' + seller10_info[3] + ',' + seller10_info[4] + ',' + seller10_info[5] + ',' + seller10_info[6] + ',' + seller10_info[7] + ',' + seller10_info[8] + ',' + seller10_info[9] + ',' + seller10_info[10] + ',' + seller10_info[11] + ',' + seller10_info[12] 
                    f = open('sellers.txt', 'w')
                    g = f.close
                    h = open('sellers.txt', 'a')
                    write0 = h.write('#0-sellerid, 1-name, 2-lastname, 3-email, 4-website, 5-amountappsonsale, 6-app1, 7-app2, 8-app3, 9-app4, 10-app5, 11-downloadsUS, 12-downloadsCR' + '\n')
                    write1 = h.write(new_1)
                    write2 = h.write(new_2)
                    write3 = h.write(new_3)
                    write4 = h.write(new_4)
                    write5 = h.write(new_5)
                    write6 = h.write(new_6)
                    write7 = h.write(new_7)
                    write8 = h.write(new_8)
                    write9 = h.write(new_9)
                    write10 = h.write(new_10)
                    i = h.close

                    success_label = Label(add_app_window, text = 'Success', font = 'Helvetica 38', fg = 'firebrick3')
                    success_label.place(x=680, y=400)

                #labels para info de app que se quiera agregar
                appname_label = Label(add_app_window, text = 'App Name', font = 'Helvetica 24')
                appname_label.place(x=100, y=50)

                desc1_label = Label(add_app_window, text = 'Description 1', font = 'Helvetica 24')
                desc1_label.place(x=100, y=100)

                desc2_label = Label(add_app_window, text = 'Description 2', font = 'Helvetica 24')
                desc2_label.place(x=100, y=150)

                desc3_label = Label(add_app_window, text = 'Description 3', font = 'Helvetica 24')
                desc3_label.place(x=100, y=200)

                desc4_label = Label(add_app_window, text = 'Description 4', font = 'Helvetica 24')
                desc4_label.place(x=100, y=250)

                desc5_label = Label(add_app_window, text = 'Description 5', font = 'Helvetica 24')
                desc5_label.place(x=100, y=300)

                desc1_esp_label = Label(add_app_window, text = 'Description 1 in Spanish', font = 'Helvetica 24')
                desc1_esp_label.place(x=100, y=350)

                desc2_esp_label = Label(add_app_window, text = 'Description 2 in Spanish', font = 'Helvetica 24')
                desc2_esp_label.place(x=100, y=400)

                desc3_esp_label = Label(add_app_window, text = 'Description 3 in Spanish', font = 'Helvetica 24')
                desc3_esp_label.place(x=100, y=450)

                desc4_esp_label = Label(add_app_window, text = 'Description 4 in Spanish', font = 'Helvetica 24')
                desc4_esp_label.place(x=100, y=500)

                desc5_esp_label = Label(add_app_window, text = 'Description 5 in Spanish', font = 'Helvetica 24')
                desc5_esp_label.place(x=100, y=550)

                price_label = Label(add_app_window, text = 'Price ($) or "Free"', font = 'Helvetica 24')
                price_label.place(x=600, y=50)

                appsize_label  = Label(add_app_window, text = 'App Size', font = 'Helvetica 24')
                appsize_label.place(x=600, y=100)

                #entries
                name_entry = Entry(add_app_window, width = 20)
                name_entry.place(x=400, y=50)

                desc1_entry = Entry(add_app_window, width = 20)
                desc1_entry.place(x=400, y=100)

                desc2_entry = Entry(add_app_window, width = 20)
                desc2_entry.place(x=400, y=150)

                desc3_entry = Entry(add_app_window, width = 20)
                desc3_entry.place(x=400, y=200)

                desc4_entry = Entry(add_app_window, width = 20)
                desc4_entry.place(x=400, y=250)

                desc5_entry = Entry(add_app_window, width = 20)
                desc5_entry.place(x=400, y=300)

                desc1_esp_entry = Entry(add_app_window, width = 20)
                desc1_esp_entry.place(x=400, y=350)

                desc2_esp_entry = Entry(add_app_window, width = 20)
                desc2_esp_entry.place(x=400, y=400)

                desc3_esp_entry = Entry(add_app_window, width = 20)
                desc3_esp_entry.place(x=400, y=450)

                desc4_esp_entry = Entry(add_app_window, width = 20)
                desc4_esp_entry.place(x=400, y=500)

                desc5_esp_entry = Entry(add_app_window, width = 20)
                desc5_esp_entry.place(x=400, y=550)

                price_entry = Entry(add_app_window, width = 20)
                price_entry.place(x=800, y=50)

                appsize_entry  = Entry(add_app_window, width = 20)
                appsize_entry.place(x=800, y=100)

                add_app_button = Button(add_app_window, text = 'Add App', command = add_app)
                add_app_button.place(x=700, y=475)

                def back():
                    add_app_window.destroy()

                back_button = Button(add_app_window, image = exiticon, command = back)
                back_button.place(x=25,y=25)

            def add_game_window():
                add_game_window = Toplevel()
                add_game_window.title('Admin App')
                add_game_window.minsize(1000,600)
                add_game_window.resizable(width=NO, height=NO)

                def add_app():
                    a = open ('appcount.txt','r+')
                    lastIndex = a.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    appname = name_entry.get()
                    desc1 = desc1_entry.get()
                    desc2 = desc2_entry.get()
                    desc3 = desc3_entry.get()
                    desc4 = desc4_entry.get()
                    desc5 = desc5_entry.get()
                    price = price_entry.get()
                    appsize = appsize_entry.get()
                    b = open('games.txt','a')
                    info = '7' + ',' + productid + ',' + '1' + ',' + appname + ',' + desc1 + ',' + desc2 + ',' + desc3 + ',' + desc4 + ',' + desc5 + ',' + price + ',' + appsize + ',' + '0'
                    b.write('\n' + str(info))
                    a.close
                    b.close

                    c = open('appcount.txt','r+')
                    lastIndex = c.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    desc1_esp = desc1_esp_entry.get()
                    desc2_esp = desc2_esp_entry.get()
                    desc3_esp = desc3_esp_entry.get()
                    desc4_esp = desc4_esp_entry.get()
                    desc5_esp = desc5_esp_entry.get()
                    d = open('games_esp.txt','a')
                    info = '7' + ',' + productid + ',' + '1' + ',' + appname + ',' + desc1_esp + ',' + desc2_esp + ',' + desc3_esp + ',' + desc4_esp + ',' + desc5_esp + ',' + price + ',' + appsize + ',' + '0'
                    d.write('\n' + str(info))
                    c.write('\n' + str(int(productid) + 1))
                    c.close
                    d.close

                    e = open('sellers.txt', 'r+')
                    read_seller_info = e.readlines()
                    seller1_line = read_seller_info[1]
                    seller1_info = seller1_line.split(',')
                    seller2_line = read_seller_info[2]
                    seller2_info = seller2_line.split(',')
                    seller3_line = read_seller_info[3]
                    seller3_info = seller3_line.split(',')
                    seller4_line = read_seller_info[4]
                    seller4_info = seller4_line.split(',')
                    seller5_line = read_seller_info[5]
                    seller5_info = seller5_line.split(',')
                    seller6_line = read_seller_info[6]
                    seller6_info = seller6_line.split(',')
                    seller7_line = read_seller_info[7]
                    seller7_info = seller7_line.split(',')
                    seller8_line = read_seller_info[8]
                    seller8_info = seller8_line.split(',')
                    seller9_line = read_seller_info[9]
                    seller9_info = seller9_line.split(',')
                    seller10_line = read_seller_info[10]
                    seller10_info = seller10_line.split(',')

                    if seller7_info[6] == '':
                        seller7_info[6] = name_entry.get() + ' (I)'
                        seller7_info[5] = str(int(seller7_info[5]) + 1)
                    elif seller7_info[7] == '':
                        seller7_info[7] = name_entry.get() + ' (I)'
                        seller7_info[5] = str(int(seller7_info[5]) + 1)
                    elif seller7_info[8] == '':
                        seller7_info[8] = name_entry.get() + ' (I)'
                        seller7_info[5] = str(int(seller7_info[5]) + 1)
                    elif seller7_info[9] == '':
                        seller7_info[9] = name_entry.get() + ' (I)'
                        seller7_info[5] = str(int(seller7_info[5]) + 1)
                    elif seller7_info[10] == '':
                        seller7_info[10] = name_entry.get() + ' (I)'
                        seller7_info[5] = str(int(seller7_info[5]) + 1)
                    else:
                        print('You have challenged the Matrix')
                    
                    new_1 = seller1_info[0] + ',' + seller1_info[1] + ',' + seller1_info[2] + ',' + seller1_info[3] + ',' + seller1_info[4] + ',' + seller1_info[5] + ',' + seller1_info[6] + ',' + seller1_info[7] + ',' + seller1_info[8] + ',' + seller1_info[9] + ',' + seller1_info[10] + ',' + seller1_info[11] + ',' + seller1_info[12] 
                    new_2 = seller2_info[0] + ',' + seller2_info[1] + ',' + seller2_info[2] + ',' + seller2_info[3] + ',' + seller2_info[4] + ',' + seller2_info[5] + ',' + seller2_info[6] + ',' + seller2_info[7] + ',' + seller2_info[8] + ',' + seller2_info[9] + ',' + seller2_info[10] + ',' + seller2_info[11] + ',' + seller2_info[12] 
                    new_3 = seller3_info[0] + ',' + seller3_info[1] + ',' + seller3_info[2] + ',' + seller3_info[3] + ',' + seller3_info[4] + ',' + seller3_info[5] + ',' + seller3_info[6] + ',' + seller3_info[7] + ',' + seller3_info[8] + ',' + seller3_info[9] + ',' + seller3_info[10] + ',' + seller3_info[11] + ',' + seller3_info[12] 
                    new_4 = seller4_info[0] + ',' + seller4_info[1] + ',' + seller4_info[2] + ',' + seller4_info[3] + ',' + seller4_info[4] + ',' + seller4_info[5] + ',' + seller4_info[6] + ',' + seller4_info[7] + ',' + seller4_info[8] + ',' + seller4_info[9] + ',' + seller4_info[10] + ',' + seller4_info[11] + ',' + seller4_info[12] 
                    new_5 = seller5_info[0] + ',' + seller5_info[1] + ',' + seller5_info[2] + ',' + seller5_info[3] + ',' + seller5_info[4] + ',' + seller5_info[5] + ',' + seller5_info[6] + ',' + seller5_info[7] + ',' + seller5_info[8] + ',' + seller5_info[9] + ',' + seller5_info[10] + ',' + seller5_info[11] + ',' + seller5_info[12] 
                    new_6 = seller6_info[0] + ',' + seller6_info[1] + ',' + seller6_info[2] + ',' + seller6_info[3] + ',' + seller6_info[4] + ',' + seller6_info[5] + ',' + seller6_info[6] + ',' + seller6_info[7] + ',' + seller6_info[8] + ',' + seller6_info[9] + ',' + seller6_info[10] + ',' + seller6_info[11] + ',' + seller6_info[12] 
                    new_7 = seller7_info[0] + ',' + seller7_info[1] + ',' + seller7_info[2] + ',' + seller7_info[3] + ',' + seller7_info[4] + ',' + seller7_info[5] + ',' + seller7_info[6] + ',' + seller7_info[7] + ',' + seller7_info[8] + ',' + seller7_info[9] + ',' + seller7_info[10] + ',' + seller7_info[11] + ',' + seller7_info[12] 
                    new_8 = seller8_info[0] + ',' + seller8_info[1] + ',' + seller8_info[2] + ',' + seller8_info[3] + ',' + seller8_info[4] + ',' + seller8_info[5] + ',' + seller8_info[6] + ',' + seller8_info[7] + ',' + seller8_info[8] + ',' + seller8_info[9] + ',' + seller8_info[10] + ',' + seller8_info[11] + ',' + seller8_info[12]
                    new_9 = seller9_info[0] + ',' + seller9_info[1] + ',' + seller9_info[2] + ',' + seller9_info[3] + ',' + seller9_info[4] + ',' + seller9_info[5] + ',' + seller9_info[6] + ',' + seller9_info[7] + ',' + seller9_info[8] + ',' + seller9_info[9] + ',' + seller9_info[10] + ',' + seller9_info[11] + ',' + seller9_info[12] 
                    new_10 = seller10_info[0] + ',' + seller10_info[1] + ',' + seller10_info[2] + ',' + seller10_info[3] + ',' + seller10_info[4] + ',' + seller10_info[5] + ',' + seller10_info[6] + ',' + seller10_info[7] + ',' + seller10_info[8] + ',' + seller10_info[9] + ',' + seller10_info[10] + ',' + seller10_info[11] + ',' + seller10_info[12] 
                    f = open('sellers.txt', 'w')
                    g = f.close
                    h = open('sellers.txt', 'a')
                    write0 = h.write('#0-sellerid, 1-name, 2-lastname, 3-email, 4-website, 5-amountappsonsale, 6-app1, 7-app2, 8-app3, 9-app4, 10-app5, 11-downloadsUS, 12-downloadsCR' + '\n')
                    write1 = h.write(new_1)
                    write2 = h.write(new_2)
                    write3 = h.write(new_3)
                    write4 = h.write(new_4)
                    write5 = h.write(new_5)
                    write6 = h.write(new_6)
                    write7 = h.write(new_7)
                    write8 = h.write(new_8)
                    write9 = h.write(new_9)
                    write10 = h.write(new_10)
                    i = h.close

                    success_label = Label(add_game_window, text = 'Success', font = 'Helvetica 38', fg = 'firebrick3')
                    success_label.place(x=680, y=400)

                #labels para info de app que se quiera agregar
                appname_label = Label(add_game_window, text = 'Game Name', font = 'Helvetica 24')
                appname_label.place(x=100, y=50)

                desc1_label = Label(add_game_window, text = 'Description 1', font = 'Helvetica 24')
                desc1_label.place(x=100, y=100)

                desc2_label = Label(add_game_window, text = 'Description 2', font = 'Helvetica 24')
                desc2_label.place(x=100, y=150)

                desc3_label = Label(add_game_window, text = 'Description 3', font = 'Helvetica 24')
                desc3_label.place(x=100, y=200)

                desc4_label = Label(add_game_window, text = 'Description 4', font = 'Helvetica 24')
                desc4_label.place(x=100, y=250)

                desc5_label = Label(add_game_window, text = 'Description 5', font = 'Helvetica 24')
                desc5_label.place(x=100, y=300)

                desc1_esp_label = Label(add_game_window, text = 'Description 1 in Spanish', font = 'Helvetica 24')
                desc1_esp_label.place(x=100, y=350)

                desc2_esp_label = Label(add_game_window, text = 'Description 2 in Spanish', font = 'Helvetica 24')
                desc2_esp_label.place(x=100, y=400)

                desc3_esp_label = Label(add_game_window, text = 'Description 3 in Spanish', font = 'Helvetica 24')
                desc3_esp_label.place(x=100, y=450)

                desc4_esp_label = Label(add_game_window, text = 'Description 4 in Spanish', font = 'Helvetica 24')
                desc4_esp_label.place(x=100, y=500)

                desc5_esp_label = Label(add_game_window, text = 'Description 5 in Spanish', font = 'Helvetica 24')
                desc5_esp_label.place(x=100, y=550)

                price_label = Label(add_game_window, text = 'Price ($) or "Free"', font = 'Helvetica 24')
                price_label.place(x=600, y=50)

                appsize_label  = Label(add_game_window, text = 'App Size', font = 'Helvetica 24')
                appsize_label.place(x=600, y=100)

                #entries
                name_entry = Entry(add_game_window, width = 20)
                name_entry.place(x=400, y=50)

                desc1_entry = Entry(add_game_window, width = 20)
                desc1_entry.place(x=400, y=100)

                desc2_entry = Entry(add_game_window, width = 20)
                desc2_entry.place(x=400, y=150)

                desc3_entry = Entry(add_game_window, width = 20)
                desc3_entry.place(x=400, y=200)

                desc4_entry = Entry(add_game_window, width = 20)
                desc4_entry.place(x=400, y=250)

                desc5_entry = Entry(add_game_window, width = 20)
                desc5_entry.place(x=400, y=300)

                desc1_esp_entry = Entry(add_game_window, width = 20)
                desc1_esp_entry.place(x=400, y=350)

                desc2_esp_entry = Entry(add_game_window, width = 20)
                desc2_esp_entry.place(x=400, y=400)

                desc3_esp_entry = Entry(add_game_window, width = 20)
                desc3_esp_entry.place(x=400, y=450)

                desc4_esp_entry = Entry(add_game_window, width = 20)
                desc4_esp_entry.place(x=400, y=500)

                desc5_esp_entry = Entry(add_game_window, width = 20)
                desc5_esp_entry.place(x=400, y=550)

                price_entry = Entry(add_game_window, width = 20)
                price_entry.place(x=800, y=50)

                appsize_entry  = Entry(add_game_window, width = 20)
                appsize_entry.place(x=800, y=100)

                add_app_button = Button(add_game_window, text = 'Add Game', command = add_app)
                add_app_button.place(x=700, y=475)

                def back():
                    add_game_window.destroy()

                back_button = Button(add_game_window, image = exiticon, command = back)
                back_button.place(x=25,y=25)
                
                
            #labels de informacion
            name = Label(sellercanvas, text = seller7_info[1], font = 'Helvetica 24', fg = 'firebrick3')
            name.place(x=300, y=100)

            lastname = Label(sellercanvas, text = seller7_info[2], font = 'Helvetica 24', fg = 'firebrick3')
            lastname.place(x=300, y=200)

            email = Label(sellercanvas, text = seller7_info[3], font = 'Helvetica 24', fg = 'firebrick3')
            email.place(x=300, y=300)

            website = Label(sellercanvas, text = seller7_info[4], font = 'Helvetica 24', fg = 'firebrick3')
            website.place(x=300, y=400)

            amount_apps = Label(sellercanvas, text = seller7_info[5], font = 'Helvetica 24', fg = 'firebrick3')
            amount_apps.place(x=400, y=500)

            app1 = Label(sellercanvas, text = seller7_info[6], font = 'Helvetica 24', fg = 'firebrick3')
            app1.place(x=700, y=100)

            app1_downloads = Label(sellercanvas, text = 'Downloads US: '+game1_info[11]+'Downloads CR: '+game1_esp_info[11], font = 'Helvetica 16')
            app1_downloads.place(x=600, y=140)

            app1_money_label = Label(sellercanvas, text = '$ made:', font = 'Helvetica 16')
            app1_money_label.place(x=780, y=150)

            app1_money = Label(sellercanvas, text = (int(game1_info[11]) + int(game1_esp_info[11])) * 0.99, fg = 'firebrick3', font = 'Helvetica 24')
            app1_money.place(x=860, y=145)

            app2 = Label(sellercanvas, text = seller7_info[7], font = 'Helvetica 24', fg = 'firebrick3')
            app2.place(x=700, y=200)
            
            app2_money_label = Label(sellercanvas, text = '$ made:', font = 'Helvetica 16')
            app2_money_label.place(x=780, y=250)

            app2_money = Label(sellercanvas, text = (int(game2_info[11]) + int(game2_esp_info[11])) * 6.99, fg = 'firebrick3', font = 'Helvetica 24')
            app2_money.place(x=860, y=245)

            app2_downloads = Label(sellercanvas, text = 'Downloads US: '+game2_info[11]+'Downloads CR: '+game2_esp_info[11], font = 'Helvetica 16')
            app2_downloads.place(x=600, y=240)

            app3 = Label(sellercanvas, text = seller7_info[8], font = 'Helvetica 24', fg = 'firebrick3')
            app3.place(x=700, y=300)

            app3_money_label = Label(sellercanvas, text = '$ made:', font = 'Helvetica 16')
            app3_money_label.place(x=780, y=350)

            app3_money = Label(sellercanvas, text = (int(game3_info[11]) + int(game3_esp_info[11])) * 6.99, fg = 'firebrick3', font = 'Helvetica 24')
            app3_money.place(x=860, y=345)

            app3_downloads = Label(sellercanvas, text = 'Downloads US: '+game3_info[11]+'Downloads CR: '+game3_esp_info[11], font = 'Helvetica 16')
            app3_downloads.place(x=600, y=340)

            app4 = Label(sellercanvas, text = seller7_info[9], font = 'Helvetica 24', fg = 'firebrick3')
            app4.place(x=700, y=400)
            
            app4_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app4_downloads.place(x=600, y=440)

            app5 = Label(sellercanvas, text = seller7_info[10], font = 'Helvetica 24', fg = 'firebrick3')
            app5.place(x=700, y=500)

            app5_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app5_downloads.place(x=600, y=540)

            name_label = Label(sellercanvas, text  = 'Seller name:', font = 'Helvetica 24')
            name_label.place(x=100, y=100)

            lastname_label = Label(sellercanvas, text = 'Last Name:', font = 'Helvetica 24')
            lastname_label.place(x=100, y=200)

            email_label = Label(sellercanvas, text = 'Email:', font = 'Helvetica 24')
            email_label.place(x=100, y=300)

            website_label = Label(sellercanvas, text = 'Website:', font = 'Helvetica 24')
            website_label.place(x=100, y=400)

            amount_apps_label = Label(sellercanvas, text = 'Amount apps on sale', font = 'Helvetica 24')
            amount_apps_label.place(x=100, y=500)

            app1_label = Label(sellercanvas, text = 'App 1', font = 'Helvetica 24')
            app1_label.place(x=600, y=100)

            app2_label = Label(sellercanvas, text = 'App 2', font = 'Helvetica 24')
            app2_label.place(x=600, y=200)

            app3_label = Label(sellercanvas, text = 'App 3', font = 'Helvetica 24')
            app3_label.place(x=600, y=300)

            app4_label = Label(sellercanvas, text = 'App 4', font = 'Helvetica 24')
            app4_label.place(x=600, y=400)

            app5_label = Label(sellercanvas, text = 'App 5', font = 'Helvetica 24')
            app5_label.place(x=600, y=500)

            #boton para agregar apps
            add_app_button = Button(sellercanvas, text = 'Add app', font = 'Helvetica 24', command = add_app_window)
            add_app_button.place(x=650, y=50)

            add_game_button = Button(sellercanvas, text = 'Add game', font = 'Helvetica 24', command = add_game_window)
            add_game_button.place(x=850, y=50)

        #misma estructura que vendedor 1
        def seller8():
            seller8 = Toplevel()
            seller8.title('Admin App')
            seller8.minsize(1000,600)
            seller8.resizable(width=NO, height=NO)

            sellercanvas = Canvas(seller8, width = 1000, height = 600)
            sellercanvas.place(x=0,y=0)

            all_sellers = open('sellers.txt', 'r')
            read_sellers = all_sellers.readlines()
            seller8_line = read_sellers[8]
            seller8_info = seller8_line.split(',')

            def back():
                seller8.destroy()

            back_button = Button(seller8, image = exiticon, command = back)
            back_button.place(x=25,y=25)

            def add_app_window():
                add_app_window = Toplevel()
                add_app_window.title('Admin App')
                add_app_window.minsize(1000,600)
                add_app_window.resizable(width=NO, height=NO)

                def add_app():
                    a = open ('appcount.txt','r+')
                    lastIndex = a.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    appname = name_entry.get()
                    desc1 = desc1_entry.get()
                    desc2 = desc2_entry.get()
                    desc3 = desc3_entry.get()
                    desc4 = desc4_entry.get()
                    desc5 = desc5_entry.get()
                    price = price_entry.get()
                    appsize = appsize_entry.get()
                    b = open('apps.txt','a')
                    info = '8' + ',' + productid + ',' + '0' + ',' + appname + ',' + desc1 + ',' + desc2 + ',' + desc3 + ',' + desc4 + ',' + desc5 + ',' + price + ',' + appsize + ',' + '0'
                    b.write('\n' + str(info))
                    a.close
                    b.close

                    c = open('appcount.txt','r+')
                    lastIndex = c.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    desc1_esp = desc1_esp_entry.get()
                    desc2_esp = desc2_esp_entry.get()
                    desc3_esp = desc3_esp_entry.get()
                    desc4_esp = desc4_esp_entry.get()
                    desc5_esp = desc5_esp_entry.get()
                    d = open('apps_esp.txt','a')
                    info = '8' + ',' + productid + ',' + '0' + ',' + appname + ',' + desc1_esp + ',' + desc2_esp + ',' + desc3_esp + ',' + desc4_esp + ',' + desc5_esp + ',' + price + ',' + appsize + ',' + '0'
                    d.write('\n' + str(info))
                    c.write('\n' + str(int(productid) + 1))
                    c.close
                    d.close

                    e = open('sellers.txt', 'r+')
                    read_seller_info = e.readlines()
                    seller1_line = read_seller_info[1]
                    seller1_info = seller1_line.split(',')
                    seller2_line = read_seller_info[2]
                    seller2_info = seller2_line.split(',')
                    seller3_line = read_seller_info[3]
                    seller3_info = seller3_line.split(',')
                    seller4_line = read_seller_info[4]
                    seller4_info = seller4_line.split(',')
                    seller5_line = read_seller_info[5]
                    seller5_info = seller5_line.split(',')
                    seller6_line = read_seller_info[6]
                    seller6_info = seller6_line.split(',')
                    seller7_line = read_seller_info[7]
                    seller7_info = seller7_line.split(',')
                    seller8_line = read_seller_info[8]
                    seller8_info = seller8_line.split(',')
                    seller9_line = read_seller_info[9]
                    seller9_info = seller9_line.split(',')
                    seller10_line = read_seller_info[10]
                    seller10_info = seller10_line.split(',')

                    if seller8_info[6] == '':
                        seller8_info[6] = name_entry.get() + ' (I)'
                        seller8_info[5] = str(int(seller8_info[5]) + 1)
                    elif seller8_info[7] == '':
                        seller8_info[7] = name_entry.get() + ' (I)'
                        seller8_info[5] = str(int(seller8_info[5]) + 1)
                    elif seller8_info[8] == '':
                        seller8_info[8] = name_entry.get() + ' (I)'
                        seller8_info[5] = str(int(seller8_info[5]) + 1)
                    elif seller8_info[9] == '':
                        seller8_info[9] = name_entry.get() + ' (I)'
                        seller8_info[5] = str(int(seller8_info[5]) + 1)
                    elif seller8_info[10] == '':
                        seller8_info[10] = name_entry.get() + ' (I)'
                        seller8_info[5] = str(int(seller8_info[5]) + 1)
                    else:
                        print('You have challenged the Matrix')
                    
                    new_1 = seller1_info[0] + ',' + seller1_info[1] + ',' + seller1_info[2] + ',' + seller1_info[3] + ',' + seller1_info[4] + ',' + seller1_info[5] + ',' + seller1_info[6] + ',' + seller1_info[7] + ',' + seller1_info[8] + ',' + seller1_info[9] + ',' + seller1_info[10] + ',' + seller1_info[11] + ',' + seller1_info[12] 
                    new_2 = seller2_info[0] + ',' + seller2_info[1] + ',' + seller2_info[2] + ',' + seller2_info[3] + ',' + seller2_info[4] + ',' + seller2_info[5] + ',' + seller2_info[6] + ',' + seller2_info[7] + ',' + seller2_info[8] + ',' + seller2_info[9] + ',' + seller2_info[10] + ',' + seller2_info[11] + ',' + seller2_info[12] 
                    new_3 = seller3_info[0] + ',' + seller3_info[1] + ',' + seller3_info[2] + ',' + seller3_info[3] + ',' + seller3_info[4] + ',' + seller3_info[5] + ',' + seller3_info[6] + ',' + seller3_info[7] + ',' + seller3_info[8] + ',' + seller3_info[9] + ',' + seller3_info[10] + ',' + seller3_info[11] + ',' + seller3_info[12] 
                    new_4 = seller4_info[0] + ',' + seller4_info[1] + ',' + seller4_info[2] + ',' + seller4_info[3] + ',' + seller4_info[4] + ',' + seller4_info[5] + ',' + seller4_info[6] + ',' + seller4_info[7] + ',' + seller4_info[8] + ',' + seller4_info[9] + ',' + seller4_info[10] + ',' + seller4_info[11] + ',' + seller4_info[12] 
                    new_5 = seller5_info[0] + ',' + seller5_info[1] + ',' + seller5_info[2] + ',' + seller5_info[3] + ',' + seller5_info[4] + ',' + seller5_info[5] + ',' + seller5_info[6] + ',' + seller5_info[7] + ',' + seller5_info[8] + ',' + seller5_info[9] + ',' + seller5_info[10] + ',' + seller5_info[11] + ',' + seller5_info[12] 
                    new_6 = seller6_info[0] + ',' + seller6_info[1] + ',' + seller6_info[2] + ',' + seller6_info[3] + ',' + seller6_info[4] + ',' + seller6_info[5] + ',' + seller6_info[6] + ',' + seller6_info[7] + ',' + seller6_info[8] + ',' + seller6_info[9] + ',' + seller6_info[10] + ',' + seller6_info[11] + ',' + seller6_info[12] 
                    new_7 = seller7_info[0] + ',' + seller7_info[1] + ',' + seller7_info[2] + ',' + seller7_info[3] + ',' + seller7_info[4] + ',' + seller7_info[5] + ',' + seller7_info[6] + ',' + seller7_info[7] + ',' + seller7_info[8] + ',' + seller7_info[9] + ',' + seller7_info[10] + ',' + seller7_info[11] + ',' + seller7_info[12] 
                    new_8 = seller8_info[0] + ',' + seller8_info[1] + ',' + seller8_info[2] + ',' + seller8_info[3] + ',' + seller8_info[4] + ',' + seller8_info[5] + ',' + seller8_info[6] + ',' + seller8_info[7] + ',' + seller8_info[8] + ',' + seller8_info[9] + ',' + seller8_info[10] + ',' + seller8_info[11] + ',' + seller8_info[12]
                    new_9 = seller9_info[0] + ',' + seller9_info[1] + ',' + seller9_info[2] + ',' + seller9_info[3] + ',' + seller9_info[4] + ',' + seller9_info[5] + ',' + seller9_info[6] + ',' + seller9_info[7] + ',' + seller9_info[8] + ',' + seller9_info[9] + ',' + seller9_info[10] + ',' + seller9_info[11] + ',' + seller9_info[12] 
                    new_10 = seller10_info[0] + ',' + seller10_info[1] + ',' + seller10_info[2] + ',' + seller10_info[3] + ',' + seller10_info[4] + ',' + seller10_info[5] + ',' + seller10_info[6] + ',' + seller10_info[7] + ',' + seller10_info[8] + ',' + seller10_info[9] + ',' + seller10_info[10] + ',' + seller10_info[11] + ',' + seller10_info[12] 
                    f = open('sellers.txt', 'w')
                    g = f.close
                    h = open('sellers.txt', 'a')
                    write0 = h.write('#0-sellerid, 1-name, 2-lastname, 3-email, 4-website, 5-amountappsonsale, 6-app1, 7-app2, 8-app3, 9-app4, 10-app5, 11-downloadsUS, 12-downloadsCR' + '\n')
                    write1 = h.write(new_1)
                    write2 = h.write(new_2)
                    write3 = h.write(new_3)
                    write4 = h.write(new_4)
                    write5 = h.write(new_5)
                    write6 = h.write(new_6)
                    write7 = h.write(new_7)
                    write8 = h.write(new_8)
                    write9 = h.write(new_9)
                    write10 = h.write(new_10)
                    i = h.close

                    success_label = Label(add_app_window, text = 'Success', font = 'Helvetica 38', fg = 'firebrick3')
                    success_label.place(x=680, y=400)

                #labels para info de app que se quiera agregar
                appname_label = Label(add_app_window, text = 'App Name', font = 'Helvetica 24')
                appname_label.place(x=100, y=50)

                desc1_label = Label(add_app_window, text = 'Description 1', font = 'Helvetica 24')
                desc1_label.place(x=100, y=100)

                desc2_label = Label(add_app_window, text = 'Description 2', font = 'Helvetica 24')
                desc2_label.place(x=100, y=150)

                desc3_label = Label(add_app_window, text = 'Description 3', font = 'Helvetica 24')
                desc3_label.place(x=100, y=200)

                desc4_label = Label(add_app_window, text = 'Description 4', font = 'Helvetica 24')
                desc4_label.place(x=100, y=250)

                desc5_label = Label(add_app_window, text = 'Description 5', font = 'Helvetica 24')
                desc5_label.place(x=100, y=300)

                desc1_esp_label = Label(add_app_window, text = 'Description 1 in Spanish', font = 'Helvetica 24')
                desc1_esp_label.place(x=100, y=350)

                desc2_esp_label = Label(add_app_window, text = 'Description 2 in Spanish', font = 'Helvetica 24')
                desc2_esp_label.place(x=100, y=400)

                desc3_esp_label = Label(add_app_window, text = 'Description 3 in Spanish', font = 'Helvetica 24')
                desc3_esp_label.place(x=100, y=450)

                desc4_esp_label = Label(add_app_window, text = 'Description 4 in Spanish', font = 'Helvetica 24')
                desc4_esp_label.place(x=100, y=500)

                desc5_esp_label = Label(add_app_window, text = 'Description 5 in Spanish', font = 'Helvetica 24')
                desc5_esp_label.place(x=100, y=550)

                price_label = Label(add_app_window, text = 'Price ($) or "Free"', font = 'Helvetica 24')
                price_label.place(x=600, y=50)

                appsize_label  = Label(add_app_window, text = 'App Size', font = 'Helvetica 24')
                appsize_label.place(x=600, y=100)

                #entries
                name_entry = Entry(add_app_window, width = 20)
                name_entry.place(x=400, y=50)

                desc1_entry = Entry(add_app_window, width = 20)
                desc1_entry.place(x=400, y=100)

                desc2_entry = Entry(add_app_window, width = 20)
                desc2_entry.place(x=400, y=150)

                desc3_entry = Entry(add_app_window, width = 20)
                desc3_entry.place(x=400, y=200)

                desc4_entry = Entry(add_app_window, width = 20)
                desc4_entry.place(x=400, y=250)

                desc5_entry = Entry(add_app_window, width = 20)
                desc5_entry.place(x=400, y=300)

                desc1_esp_entry = Entry(add_app_window, width = 20)
                desc1_esp_entry.place(x=400, y=350)

                desc2_esp_entry = Entry(add_app_window, width = 20)
                desc2_esp_entry.place(x=400, y=400)

                desc3_esp_entry = Entry(add_app_window, width = 20)
                desc3_esp_entry.place(x=400, y=450)

                desc4_esp_entry = Entry(add_app_window, width = 20)
                desc4_esp_entry.place(x=400, y=500)

                desc5_esp_entry = Entry(add_app_window, width = 20)
                desc5_esp_entry.place(x=400, y=550)

                price_entry = Entry(add_app_window, width = 20)
                price_entry.place(x=800, y=50)

                appsize_entry  = Entry(add_app_window, width = 20)
                appsize_entry.place(x=800, y=100)

                add_app_button = Button(add_app_window, text = 'Add App', command = add_app)
                add_app_button.place(x=700, y=475)

                def back():
                    add_app_window.destroy()

                back_button = Button(add_app_window, image = exiticon, command = back)
                back_button.place(x=25,y=25)

            def add_game_window():
                add_game_window = Toplevel()
                add_game_window.title('Admin App')
                add_game_window.minsize(1000,600)
                add_game_window.resizable(width=NO, height=NO)

                def add_app():
                    a = open ('appcount.txt','r+')
                    lastIndex = a.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    appname = name_entry.get()
                    desc1 = desc1_entry.get()
                    desc2 = desc2_entry.get()
                    desc3 = desc3_entry.get()
                    desc4 = desc4_entry.get()
                    desc5 = desc5_entry.get()
                    price = price_entry.get()
                    appsize = appsize_entry.get()
                    b = open('games.txt','a')
                    info = '8' + ',' + productid + ',' + '1' + ',' + appname + ',' + desc1 + ',' + desc2 + ',' + desc3 + ',' + desc4 + ',' + desc5 + ',' + price + ',' + appsize + ',' + '0'
                    b.write('\n' + str(info))
                    a.close
                    b.close

                    c = open('appcount.txt','r+')
                    lastIndex = c.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    desc1_esp = desc1_esp_entry.get()
                    desc2_esp = desc2_esp_entry.get()
                    desc3_esp = desc3_esp_entry.get()
                    desc4_esp = desc4_esp_entry.get()
                    desc5_esp = desc5_esp_entry.get()
                    d = open('games_esp.txt','a')
                    info = '8' + ',' + productid + ',' + '1' + ',' + appname + ',' + desc1_esp + ',' + desc2_esp + ',' + desc3_esp + ',' + desc4_esp + ',' + desc5_esp + ',' + price + ',' + appsize + ',' + '0'
                    d.write('\n' + str(info))
                    c.write('\n' + str(int(productid) + 1))
                    c.close
                    d.close

                    e = open('sellers.txt', 'r+')
                    read_seller_info = e.readlines()
                    seller1_line = read_seller_info[1]
                    seller1_info = seller1_line.split(',')
                    seller2_line = read_seller_info[2]
                    seller2_info = seller2_line.split(',')
                    seller3_line = read_seller_info[3]
                    seller3_info = seller3_line.split(',')
                    seller4_line = read_seller_info[4]
                    seller4_info = seller4_line.split(',')
                    seller5_line = read_seller_info[5]
                    seller5_info = seller5_line.split(',')
                    seller6_line = read_seller_info[6]
                    seller6_info = seller6_line.split(',')
                    seller7_line = read_seller_info[7]
                    seller7_info = seller7_line.split(',')
                    seller8_line = read_seller_info[8]
                    seller8_info = seller8_line.split(',')
                    seller9_line = read_seller_info[9]
                    seller9_info = seller9_line.split(',')
                    seller10_line = read_seller_info[10]
                    seller10_info = seller10_line.split(',')

                    if seller8_info[6] == '':
                        seller8_info[6] = name_entry.get() + ' (I)'
                        seller8_info[5] = str(int(seller8_info[5]) + 1)
                    elif seller8_info[7] == '':
                        seller8_info[7] = name_entry.get() + ' (I)'
                        seller8_info[5] = str(int(seller8_info[5]) + 1)
                    elif seller8_info[8] == '':
                        seller8_info[8] = name_entry.get() + ' (I)'
                        seller8_info[5] = str(int(seller8_info[5]) + 1)
                    elif seller8_info[9] == '':
                        seller8_info[9] = name_entry.get() + ' (I)'
                        seller8_info[5] = str(int(seller8_info[5]) + 1)
                    elif seller8_info[10] == '':
                        seller8_info[10] = name_entry.get() + ' (I)'
                        seller8_info[5] = str(int(seller8_info[5]) + 1)
                    else:
                        print('You have challenged the Matrix')
                    
                    new_1 = seller1_info[0] + ',' + seller1_info[1] + ',' + seller1_info[2] + ',' + seller1_info[3] + ',' + seller1_info[4] + ',' + seller1_info[5] + ',' + seller1_info[6] + ',' + seller1_info[7] + ',' + seller1_info[8] + ',' + seller1_info[9] + ',' + seller1_info[10] + ',' + seller1_info[11] + ',' + seller1_info[12] 
                    new_2 = seller2_info[0] + ',' + seller2_info[1] + ',' + seller2_info[2] + ',' + seller2_info[3] + ',' + seller2_info[4] + ',' + seller2_info[5] + ',' + seller2_info[6] + ',' + seller2_info[7] + ',' + seller2_info[8] + ',' + seller2_info[9] + ',' + seller2_info[10] + ',' + seller2_info[11] + ',' + seller2_info[12] 
                    new_3 = seller3_info[0] + ',' + seller3_info[1] + ',' + seller3_info[2] + ',' + seller3_info[3] + ',' + seller3_info[4] + ',' + seller3_info[5] + ',' + seller3_info[6] + ',' + seller3_info[7] + ',' + seller3_info[8] + ',' + seller3_info[9] + ',' + seller3_info[10] + ',' + seller3_info[11] + ',' + seller3_info[12] 
                    new_4 = seller4_info[0] + ',' + seller4_info[1] + ',' + seller4_info[2] + ',' + seller4_info[3] + ',' + seller4_info[4] + ',' + seller4_info[5] + ',' + seller4_info[6] + ',' + seller4_info[7] + ',' + seller4_info[8] + ',' + seller4_info[9] + ',' + seller4_info[10] + ',' + seller4_info[11] + ',' + seller4_info[12] 
                    new_5 = seller5_info[0] + ',' + seller5_info[1] + ',' + seller5_info[2] + ',' + seller5_info[3] + ',' + seller5_info[4] + ',' + seller5_info[5] + ',' + seller5_info[6] + ',' + seller5_info[7] + ',' + seller5_info[8] + ',' + seller5_info[9] + ',' + seller5_info[10] + ',' + seller5_info[11] + ',' + seller5_info[12] 
                    new_6 = seller6_info[0] + ',' + seller6_info[1] + ',' + seller6_info[2] + ',' + seller6_info[3] + ',' + seller6_info[4] + ',' + seller6_info[5] + ',' + seller6_info[6] + ',' + seller6_info[7] + ',' + seller6_info[8] + ',' + seller6_info[9] + ',' + seller6_info[10] + ',' + seller6_info[11] + ',' + seller6_info[12] 
                    new_7 = seller7_info[0] + ',' + seller7_info[1] + ',' + seller7_info[2] + ',' + seller7_info[3] + ',' + seller7_info[4] + ',' + seller7_info[5] + ',' + seller7_info[6] + ',' + seller7_info[7] + ',' + seller7_info[8] + ',' + seller7_info[9] + ',' + seller7_info[10] + ',' + seller7_info[11] + ',' + seller7_info[12] 
                    new_8 = seller8_info[0] + ',' + seller8_info[1] + ',' + seller8_info[2] + ',' + seller8_info[3] + ',' + seller8_info[4] + ',' + seller8_info[5] + ',' + seller8_info[6] + ',' + seller8_info[7] + ',' + seller8_info[8] + ',' + seller8_info[9] + ',' + seller8_info[10] + ',' + seller8_info[11] + ',' + seller8_info[12]
                    new_9 = seller9_info[0] + ',' + seller9_info[1] + ',' + seller9_info[2] + ',' + seller9_info[3] + ',' + seller9_info[4] + ',' + seller9_info[5] + ',' + seller9_info[6] + ',' + seller9_info[7] + ',' + seller9_info[8] + ',' + seller9_info[9] + ',' + seller9_info[10] + ',' + seller9_info[11] + ',' + seller9_info[12] 
                    new_10 = seller10_info[0] + ',' + seller10_info[1] + ',' + seller10_info[2] + ',' + seller10_info[3] + ',' + seller10_info[4] + ',' + seller10_info[5] + ',' + seller10_info[6] + ',' + seller10_info[7] + ',' + seller10_info[8] + ',' + seller10_info[9] + ',' + seller10_info[10] + ',' + seller10_info[11] + ',' + seller10_info[12] 
                    f = open('sellers.txt', 'w')
                    g = f.close
                    h = open('sellers.txt', 'a')
                    write0 = h.write('#0-sellerid, 1-name, 2-lastname, 3-email, 4-website, 5-amountappsonsale, 6-app1, 7-app2, 8-app3, 9-app4, 10-app5, 11-downloadsUS, 12-downloadsCR' + '\n')
                    write1 = h.write(new_1)
                    write2 = h.write(new_2)
                    write3 = h.write(new_3)
                    write4 = h.write(new_4)
                    write5 = h.write(new_5)
                    write6 = h.write(new_6)
                    write7 = h.write(new_7)
                    write8 = h.write(new_8)
                    write9 = h.write(new_9)
                    write10 = h.write(new_10)
                    i = h.close

                    success_label = Label(add_game_window, text = 'Success', font = 'Helvetica 38', fg = 'firebrick3')
                    success_label.place(x=680, y=400)

                #labels para info de app que se quiera agregar
                appname_label = Label(add_game_window, text = 'Game Name', font = 'Helvetica 24')
                appname_label.place(x=100, y=50)

                desc1_label = Label(add_game_window, text = 'Description 1', font = 'Helvetica 24')
                desc1_label.place(x=100, y=100)

                desc2_label = Label(add_game_window, text = 'Description 2', font = 'Helvetica 24')
                desc2_label.place(x=100, y=150)

                desc3_label = Label(add_game_window, text = 'Description 3', font = 'Helvetica 24')
                desc3_label.place(x=100, y=200)

                desc4_label = Label(add_game_window, text = 'Description 4', font = 'Helvetica 24')
                desc4_label.place(x=100, y=250)

                desc5_label = Label(add_game_window, text = 'Description 5', font = 'Helvetica 24')
                desc5_label.place(x=100, y=300)

                desc1_esp_label = Label(add_game_window, text = 'Description 1 in Spanish', font = 'Helvetica 24')
                desc1_esp_label.place(x=100, y=350)

                desc2_esp_label = Label(add_game_window, text = 'Description 2 in Spanish', font = 'Helvetica 24')
                desc2_esp_label.place(x=100, y=400)

                desc3_esp_label = Label(add_game_window, text = 'Description 3 in Spanish', font = 'Helvetica 24')
                desc3_esp_label.place(x=100, y=450)

                desc4_esp_label = Label(add_game_window, text = 'Description 4 in Spanish', font = 'Helvetica 24')
                desc4_esp_label.place(x=100, y=500)

                desc5_esp_label = Label(add_game_window, text = 'Description 5 in Spanish', font = 'Helvetica 24')
                desc5_esp_label.place(x=100, y=550)

                price_label = Label(add_game_window, text = 'Price ($) or "Free"', font = 'Helvetica 24')
                price_label.place(x=600, y=50)

                appsize_label  = Label(add_game_window, text = 'App Size', font = 'Helvetica 24')
                appsize_label.place(x=600, y=100)

                #entries
                name_entry = Entry(add_game_window, width = 20)
                name_entry.place(x=400, y=50)

                desc1_entry = Entry(add_game_window, width = 20)
                desc1_entry.place(x=400, y=100)

                desc2_entry = Entry(add_game_window, width = 20)
                desc2_entry.place(x=400, y=150)

                desc3_entry = Entry(add_game_window, width = 20)
                desc3_entry.place(x=400, y=200)

                desc4_entry = Entry(add_game_window, width = 20)
                desc4_entry.place(x=400, y=250)

                desc5_entry = Entry(add_game_window, width = 20)
                desc5_entry.place(x=400, y=300)

                desc1_esp_entry = Entry(add_game_window, width = 20)
                desc1_esp_entry.place(x=400, y=350)

                desc2_esp_entry = Entry(add_game_window, width = 20)
                desc2_esp_entry.place(x=400, y=400)

                desc3_esp_entry = Entry(add_game_window, width = 20)
                desc3_esp_entry.place(x=400, y=450)

                desc4_esp_entry = Entry(add_game_window, width = 20)
                desc4_esp_entry.place(x=400, y=500)

                desc5_esp_entry = Entry(add_game_window, width = 20)
                desc5_esp_entry.place(x=400, y=550)

                price_entry = Entry(add_game_window, width = 20)
                price_entry.place(x=800, y=50)

                appsize_entry  = Entry(add_game_window, width = 20)
                appsize_entry.place(x=800, y=100)

                add_app_button = Button(add_game_window, text = 'Add Game', command = add_app)
                add_app_button.place(x=700, y=475)

                def back():
                    add_game_window.destroy()

                back_button = Button(add_game_window, image = exiticon, command = back)
                back_button.place(x=25,y=25)
                
                
            #labels de informacion
            name = Label(sellercanvas, text = seller8_info[1], font = 'Helvetica 24', fg = 'firebrick3')
            name.place(x=300, y=100)

            lastname = Label(sellercanvas, text = seller8_info[2], font = 'Helvetica 24', fg = 'firebrick3')
            lastname.place(x=300, y=200)

            email = Label(sellercanvas, text = seller8_info[3], font = 'Helvetica 24', fg = 'firebrick3')
            email.place(x=300, y=300)

            website = Label(sellercanvas, text = seller8_info[4], font = 'Helvetica 24', fg = 'firebrick3')
            website.place(x=300, y=400)

            amount_apps = Label(sellercanvas, text = seller8_info[5], font = 'Helvetica 24', fg = 'firebrick3')
            amount_apps.place(x=400, y=500)

            app1 = Label(sellercanvas, text = seller8_info[6], font = 'Helvetica 24', fg = 'firebrick3')
            app1.place(x=700, y=100)

            app1_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app1_downloads.place(x=600, y=140)
            
            app2 = Label(sellercanvas, text = seller8_info[7], font = 'Helvetica 24', fg = 'firebrick3')
            app2.place(x=700, y=200)
            
            app2_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app2_downloads.place(x=600, y=240)

            app3 = Label(sellercanvas, text = seller8_info[8], font = 'Helvetica 24', fg = 'firebrick3')
            app3.place(x=700, y=300)

            app3_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app3_downloads.place(x=600, y=340)

            app4 = Label(sellercanvas, text = seller8_info[9], font = 'Helvetica 24', fg = 'firebrick3')
            app4.place(x=700, y=400)
            
            app4_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app4_downloads.place(x=600, y=440)

            app5 = Label(sellercanvas, text = seller8_info[10], font = 'Helvetica 24', fg = 'firebrick3')
            app5.place(x=700, y=500)

            app5_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app5_downloads.place(x=600, y=540)

            name_label = Label(sellercanvas, text  = 'Seller name:', font = 'Helvetica 24')
            name_label.place(x=100, y=100)

            lastname_label = Label(sellercanvas, text = 'Last Name:', font = 'Helvetica 24')
            lastname_label.place(x=100, y=200)

            email_label = Label(sellercanvas, text = 'Email:', font = 'Helvetica 24')
            email_label.place(x=100, y=300)

            website_label = Label(sellercanvas, text = 'Website:', font = 'Helvetica 24')
            website_label.place(x=100, y=400)

            amount_apps_label = Label(sellercanvas, text = 'Amount apps on sale', font = 'Helvetica 24')
            amount_apps_label.place(x=100, y=500)

            app1_label = Label(sellercanvas, text = 'App 1', font = 'Helvetica 24')
            app1_label.place(x=600, y=100)

            app2_label = Label(sellercanvas, text = 'App 2', font = 'Helvetica 24')
            app2_label.place(x=600, y=200)

            app3_label = Label(sellercanvas, text = 'App 3', font = 'Helvetica 24')
            app3_label.place(x=600, y=300)

            app4_label = Label(sellercanvas, text = 'App 4', font = 'Helvetica 24')
            app4_label.place(x=600, y=400)

            app5_label = Label(sellercanvas, text = 'App 5', font = 'Helvetica 24')
            app5_label.place(x=600, y=500)

            #boton para agregar apps
            add_app_button = Button(sellercanvas, text = 'Add app', font = 'Helvetica 24', command = add_app_window)
            add_app_button.place(x=650, y=50)

            add_game_button = Button(sellercanvas, text = 'Add game', font = 'Helvetica 24', command = add_game_window)
            add_game_button.place(x=850, y=50)

        #misma estructura que vendedor 1
        def seller9():
            seller9 = Toplevel()
            seller9.title('Admin App')
            seller9.minsize(1000,600)
            seller9.resizable(width=NO, height=NO)

            sellercanvas = Canvas(seller9, width = 1000, height = 600)
            sellercanvas.place(x=0,y=0)

            all_sellers = open('sellers.txt', 'r')
            read_sellers = all_sellers.readlines()
            seller9_line = read_sellers[9]
            seller9_info = seller9_line.split(',')

            def back():
                seller9.destroy()

            back_button = Button(seller9, image = exiticon, command = back)
            back_button.place(x=25,y=25)

            def add_app_window():
                add_app_window = Toplevel()
                add_app_window.title('Admin App')
                add_app_window.minsize(1000,600)
                add_app_window.resizable(width=NO, height=NO)

                def add_app():
                    a = open ('appcount.txt','r+')
                    lastIndex = a.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    appname = name_entry.get()
                    desc1 = desc1_entry.get()
                    desc2 = desc2_entry.get()
                    desc3 = desc3_entry.get()
                    desc4 = desc4_entry.get()
                    desc5 = desc5_entry.get()
                    price = price_entry.get()
                    appsize = appsize_entry.get()
                    b = open('apps.txt','a')
                    info = '9' + ',' + productid + ',' + '0' + ',' + appname + ',' + desc1 + ',' + desc2 + ',' + desc3 + ',' + desc4 + ',' + desc5 + ',' + price + ',' + appsize + ',' + '0'
                    b.write('\n' + str(info))
                    a.close
                    b.close

                    c = open('appcount.txt','r+')
                    lastIndex = c.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    desc1_esp = desc1_esp_entry.get()
                    desc2_esp = desc2_esp_entry.get()
                    desc3_esp = desc3_esp_entry.get()
                    desc4_esp = desc4_esp_entry.get()
                    desc5_esp = desc5_esp_entry.get()
                    d = open('apps_esp.txt','a')
                    info = '9' + ',' + productid + ',' + '0' + ',' + appname + ',' + desc1_esp + ',' + desc2_esp + ',' + desc3_esp + ',' + desc4_esp + ',' + desc5_esp + ',' + price + ',' + appsize + ',' + '0'
                    d.write('\n' + str(info))
                    c.write('\n' + str(int(productid) + 1))
                    c.close
                    d.close

                    e = open('sellers.txt', 'r+')
                    read_seller_info = e.readlines()
                    seller1_line = read_seller_info[1]
                    seller1_info = seller1_line.split(',')
                    seller2_line = read_seller_info[2]
                    seller2_info = seller2_line.split(',')
                    seller3_line = read_seller_info[3]
                    seller3_info = seller3_line.split(',')
                    seller4_line = read_seller_info[4]
                    seller4_info = seller4_line.split(',')
                    seller5_line = read_seller_info[5]
                    seller5_info = seller5_line.split(',')
                    seller6_line = read_seller_info[6]
                    seller6_info = seller6_line.split(',')
                    seller7_line = read_seller_info[7]
                    seller7_info = seller7_line.split(',')
                    seller8_line = read_seller_info[8]
                    seller8_info = seller8_line.split(',')
                    seller9_line = read_seller_info[9]
                    seller9_info = seller9_line.split(',')
                    seller10_line = read_seller_info[10]
                    seller10_info = seller10_line.split(',')

                    if seller9_info[6] == '':
                        seller9_info[6] = name_entry.get() + ' (I)'
                        seller9_info[5] = str(int(seller9_info[5]) + 1)
                    elif seller9_info[7] == '':
                        seller9_info[7] = name_entry.get() + ' (I)'
                        seller9_info[5] = str(int(seller9_info[5]) + 1)
                    elif seller9_info[8] == '':
                        seller9_info[8] = name_entry.get() + ' (I)'
                        seller9_info[5] = str(int(seller9_info[5]) + 1)
                    elif seller9_info[9] == '':
                        seller9_info[9] = name_entry.get() + ' (I)'
                        seller9_info[5] = str(int(seller9_info[5]) + 1)
                    elif seller9_info[10] == '':
                        seller9_info[10] = name_entry.get() + ' (I)'
                        seller9_info[5] = str(int(seller9_info[5]) + 1)
                    else:
                        print('You have challenged the Matrix')
                    
                    new_1 = seller1_info[0] + ',' + seller1_info[1] + ',' + seller1_info[2] + ',' + seller1_info[3] + ',' + seller1_info[4] + ',' + seller1_info[5] + ',' + seller1_info[6] + ',' + seller1_info[7] + ',' + seller1_info[8] + ',' + seller1_info[9] + ',' + seller1_info[10] + ',' + seller1_info[11] + ',' + seller1_info[12] 
                    new_2 = seller2_info[0] + ',' + seller2_info[1] + ',' + seller2_info[2] + ',' + seller2_info[3] + ',' + seller2_info[4] + ',' + seller2_info[5] + ',' + seller2_info[6] + ',' + seller2_info[7] + ',' + seller2_info[8] + ',' + seller2_info[9] + ',' + seller2_info[10] + ',' + seller2_info[11] + ',' + seller2_info[12] 
                    new_3 = seller3_info[0] + ',' + seller3_info[1] + ',' + seller3_info[2] + ',' + seller3_info[3] + ',' + seller3_info[4] + ',' + seller3_info[5] + ',' + seller3_info[6] + ',' + seller3_info[7] + ',' + seller3_info[8] + ',' + seller3_info[9] + ',' + seller3_info[10] + ',' + seller3_info[11] + ',' + seller3_info[12] 
                    new_4 = seller4_info[0] + ',' + seller4_info[1] + ',' + seller4_info[2] + ',' + seller4_info[3] + ',' + seller4_info[4] + ',' + seller4_info[5] + ',' + seller4_info[6] + ',' + seller4_info[7] + ',' + seller4_info[8] + ',' + seller4_info[9] + ',' + seller4_info[10] + ',' + seller4_info[11] + ',' + seller4_info[12] 
                    new_5 = seller5_info[0] + ',' + seller5_info[1] + ',' + seller5_info[2] + ',' + seller5_info[3] + ',' + seller5_info[4] + ',' + seller5_info[5] + ',' + seller5_info[6] + ',' + seller5_info[7] + ',' + seller5_info[8] + ',' + seller5_info[9] + ',' + seller5_info[10] + ',' + seller5_info[11] + ',' + seller5_info[12] 
                    new_6 = seller6_info[0] + ',' + seller6_info[1] + ',' + seller6_info[2] + ',' + seller6_info[3] + ',' + seller6_info[4] + ',' + seller6_info[5] + ',' + seller6_info[6] + ',' + seller6_info[7] + ',' + seller6_info[8] + ',' + seller6_info[9] + ',' + seller6_info[10] + ',' + seller6_info[11] + ',' + seller6_info[12] 
                    new_7 = seller7_info[0] + ',' + seller7_info[1] + ',' + seller7_info[2] + ',' + seller7_info[3] + ',' + seller7_info[4] + ',' + seller7_info[5] + ',' + seller7_info[6] + ',' + seller7_info[7] + ',' + seller7_info[8] + ',' + seller7_info[9] + ',' + seller7_info[10] + ',' + seller7_info[11] + ',' + seller7_info[12] 
                    new_8 = seller8_info[0] + ',' + seller8_info[1] + ',' + seller8_info[2] + ',' + seller8_info[3] + ',' + seller8_info[4] + ',' + seller8_info[5] + ',' + seller8_info[6] + ',' + seller8_info[7] + ',' + seller8_info[8] + ',' + seller8_info[9] + ',' + seller8_info[10] + ',' + seller8_info[11] + ',' + seller8_info[12]
                    new_9 = seller9_info[0] + ',' + seller9_info[1] + ',' + seller9_info[2] + ',' + seller9_info[3] + ',' + seller9_info[4] + ',' + seller9_info[5] + ',' + seller9_info[6] + ',' + seller9_info[7] + ',' + seller9_info[8] + ',' + seller9_info[9] + ',' + seller9_info[10] + ',' + seller9_info[11] + ',' + seller9_info[12] 
                    new_10 = seller10_info[0] + ',' + seller10_info[1] + ',' + seller10_info[2] + ',' + seller10_info[3] + ',' + seller10_info[4] + ',' + seller10_info[5] + ',' + seller10_info[6] + ',' + seller10_info[7] + ',' + seller10_info[8] + ',' + seller10_info[9] + ',' + seller10_info[10] + ',' + seller10_info[11] + ',' + seller10_info[12] 
                    f = open('sellers.txt', 'w')
                    g = f.close
                    h = open('sellers.txt', 'a')
                    write0 = h.write('#0-sellerid, 1-name, 2-lastname, 3-email, 4-website, 5-amountappsonsale, 6-app1, 7-app2, 8-app3, 9-app4, 10-app5, 11-downloadsUS, 12-downloadsCR' + '\n')
                    write1 = h.write(new_1)
                    write2 = h.write(new_2)
                    write3 = h.write(new_3)
                    write4 = h.write(new_4)
                    write5 = h.write(new_5)
                    write6 = h.write(new_6)
                    write7 = h.write(new_7)
                    write8 = h.write(new_8)
                    write9 = h.write(new_9)
                    write10 = h.write(new_10)
                    i = h.close

                    success_label = Label(add_app_window, text = 'Success', font = 'Helvetica 38', fg = 'firebrick3')
                    success_label.place(x=680, y=400)

                #labels para info de app que se quiera agregar
                appname_label = Label(add_app_window, text = 'App Name', font = 'Helvetica 24')
                appname_label.place(x=100, y=50)

                desc1_label = Label(add_app_window, text = 'Description 1', font = 'Helvetica 24')
                desc1_label.place(x=100, y=100)

                desc2_label = Label(add_app_window, text = 'Description 2', font = 'Helvetica 24')
                desc2_label.place(x=100, y=150)

                desc3_label = Label(add_app_window, text = 'Description 3', font = 'Helvetica 24')
                desc3_label.place(x=100, y=200)

                desc4_label = Label(add_app_window, text = 'Description 4', font = 'Helvetica 24')
                desc4_label.place(x=100, y=250)

                desc5_label = Label(add_app_window, text = 'Description 5', font = 'Helvetica 24')
                desc5_label.place(x=100, y=300)

                desc1_esp_label = Label(add_app_window, text = 'Description 1 in Spanish', font = 'Helvetica 24')
                desc1_esp_label.place(x=100, y=350)

                desc2_esp_label = Label(add_app_window, text = 'Description 2 in Spanish', font = 'Helvetica 24')
                desc2_esp_label.place(x=100, y=400)

                desc3_esp_label = Label(add_app_window, text = 'Description 3 in Spanish', font = 'Helvetica 24')
                desc3_esp_label.place(x=100, y=450)

                desc4_esp_label = Label(add_app_window, text = 'Description 4 in Spanish', font = 'Helvetica 24')
                desc4_esp_label.place(x=100, y=500)

                desc5_esp_label = Label(add_app_window, text = 'Description 5 in Spanish', font = 'Helvetica 24')
                desc5_esp_label.place(x=100, y=550)

                price_label = Label(add_app_window, text = 'Price ($) or "Free"', font = 'Helvetica 24')
                price_label.place(x=600, y=50)

                appsize_label  = Label(add_app_window, text = 'App Size', font = 'Helvetica 24')
                appsize_label.place(x=600, y=100)

                #entries
                name_entry = Entry(add_app_window, width = 20)
                name_entry.place(x=400, y=50)

                desc1_entry = Entry(add_app_window, width = 20)
                desc1_entry.place(x=400, y=100)

                desc2_entry = Entry(add_app_window, width = 20)
                desc2_entry.place(x=400, y=150)

                desc3_entry = Entry(add_app_window, width = 20)
                desc3_entry.place(x=400, y=200)

                desc4_entry = Entry(add_app_window, width = 20)
                desc4_entry.place(x=400, y=250)

                desc5_entry = Entry(add_app_window, width = 20)
                desc5_entry.place(x=400, y=300)

                desc1_esp_entry = Entry(add_app_window, width = 20)
                desc1_esp_entry.place(x=400, y=350)

                desc2_esp_entry = Entry(add_app_window, width = 20)
                desc2_esp_entry.place(x=400, y=400)

                desc3_esp_entry = Entry(add_app_window, width = 20)
                desc3_esp_entry.place(x=400, y=450)

                desc4_esp_entry = Entry(add_app_window, width = 20)
                desc4_esp_entry.place(x=400, y=500)

                desc5_esp_entry = Entry(add_app_window, width = 20)
                desc5_esp_entry.place(x=400, y=550)

                price_entry = Entry(add_app_window, width = 20)
                price_entry.place(x=800, y=50)

                appsize_entry  = Entry(add_app_window, width = 20)
                appsize_entry.place(x=800, y=100)

                add_app_button = Button(add_app_window, text = 'Add App', command = add_app)
                add_app_button.place(x=700, y=475)

                def back():
                    add_app_window.destroy()

                back_button = Button(add_app_window, image = exiticon, command = back)
                back_button.place(x=25,y=25)

            def add_game_window():
                add_game_window = Toplevel()
                add_game_window.title('Admin App')
                add_game_window.minsize(1000,600)
                add_game_window.resizable(width=NO, height=NO)

                def add_app():
                    a = open ('appcount.txt','r+')
                    lastIndex = a.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    appname = name_entry.get()
                    desc1 = desc1_entry.get()
                    desc2 = desc2_entry.get()
                    desc3 = desc3_entry.get()
                    desc4 = desc4_entry.get()
                    desc5 = desc5_entry.get()
                    price = price_entry.get()
                    appsize = appsize_entry.get()
                    b = open('games.txt','a')
                    info = '9' + ',' + productid + ',' + '1' + ',' + appname + ',' + desc1 + ',' + desc2 + ',' + desc3 + ',' + desc4 + ',' + desc5 + ',' + price + ',' + appsize + ',' + '0'
                    b.write('\n' + str(info))
                    a.close
                    b.close

                    c = open('appcount.txt','r+')
                    lastIndex = c.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    desc1_esp = desc1_esp_entry.get()
                    desc2_esp = desc2_esp_entry.get()
                    desc3_esp = desc3_esp_entry.get()
                    desc4_esp = desc4_esp_entry.get()
                    desc5_esp = desc5_esp_entry.get()
                    d = open('games_esp.txt','a')
                    info = '9' + ',' + productid + ',' + '1' + ',' + appname + ',' + desc1_esp + ',' + desc2_esp + ',' + desc3_esp + ',' + desc4_esp + ',' + desc5_esp + ',' + price + ',' + appsize + ',' + '0'
                    d.write('\n' + str(info))
                    c.write('\n' + str(int(productid) + 1))
                    c.close
                    d.close

                    e = open('sellers.txt', 'r+')
                    read_seller_info = e.readlines()
                    seller1_line = read_seller_info[1]
                    seller1_info = seller1_line.split(',')
                    seller2_line = read_seller_info[2]
                    seller2_info = seller2_line.split(',')
                    seller3_line = read_seller_info[3]
                    seller3_info = seller3_line.split(',')
                    seller4_line = read_seller_info[4]
                    seller4_info = seller4_line.split(',')
                    seller5_line = read_seller_info[5]
                    seller5_info = seller5_line.split(',')
                    seller6_line = read_seller_info[6]
                    seller6_info = seller6_line.split(',')
                    seller7_line = read_seller_info[7]
                    seller7_info = seller7_line.split(',')
                    seller8_line = read_seller_info[8]
                    seller8_info = seller8_line.split(',')
                    seller9_line = read_seller_info[9]
                    seller9_info = seller9_line.split(',')
                    seller10_line = read_seller_info[10]
                    seller10_info = seller10_line.split(',')

                    if seller9_info[6] == '':
                        seller9_info[6] = name_entry.get() + ' (I)'
                        seller9_info[5] = str(int(seller9_info[5]) + 1)
                    elif seller9_info[7] == '':
                        seller9_info[7] = name_entry.get() + ' (I)'
                        seller9_info[5] = str(int(seller9_info[5]) + 1)
                    elif seller9_info[8] == '':
                        seller9_info[8] = name_entry.get() + ' (I)'
                        seller9_info[5] = str(int(seller9_info[5]) + 1)
                    elif seller9_info[9] == '':
                        seller9_info[9] = name_entry.get() + ' (I)'
                        seller9_info[5] = str(int(seller9_info[5]) + 1)
                    elif seller9_info[10] == '':
                        seller9_info[10] = name_entry.get() + ' (I)'
                        seller9_info[5] = str(int(seller9_info[5]) + 1)
                    else:
                        print('You have challenged the Matrix')
                    
                    new_1 = seller1_info[0] + ',' + seller1_info[1] + ',' + seller1_info[2] + ',' + seller1_info[3] + ',' + seller1_info[4] + ',' + seller1_info[5] + ',' + seller1_info[6] + ',' + seller1_info[7] + ',' + seller1_info[8] + ',' + seller1_info[9] + ',' + seller1_info[10] + ',' + seller1_info[11] + ',' + seller1_info[12] 
                    new_2 = seller2_info[0] + ',' + seller2_info[1] + ',' + seller2_info[2] + ',' + seller2_info[3] + ',' + seller2_info[4] + ',' + seller2_info[5] + ',' + seller2_info[6] + ',' + seller2_info[7] + ',' + seller2_info[8] + ',' + seller2_info[9] + ',' + seller2_info[10] + ',' + seller2_info[11] + ',' + seller2_info[12] 
                    new_3 = seller3_info[0] + ',' + seller3_info[1] + ',' + seller3_info[2] + ',' + seller3_info[3] + ',' + seller3_info[4] + ',' + seller3_info[5] + ',' + seller3_info[6] + ',' + seller3_info[7] + ',' + seller3_info[8] + ',' + seller3_info[9] + ',' + seller3_info[10] + ',' + seller3_info[11] + ',' + seller3_info[12] 
                    new_4 = seller4_info[0] + ',' + seller4_info[1] + ',' + seller4_info[2] + ',' + seller4_info[3] + ',' + seller4_info[4] + ',' + seller4_info[5] + ',' + seller4_info[6] + ',' + seller4_info[7] + ',' + seller4_info[8] + ',' + seller4_info[9] + ',' + seller4_info[10] + ',' + seller4_info[11] + ',' + seller4_info[12] 
                    new_5 = seller5_info[0] + ',' + seller5_info[1] + ',' + seller5_info[2] + ',' + seller5_info[3] + ',' + seller5_info[4] + ',' + seller5_info[5] + ',' + seller5_info[6] + ',' + seller5_info[7] + ',' + seller5_info[8] + ',' + seller5_info[9] + ',' + seller5_info[10] + ',' + seller5_info[11] + ',' + seller5_info[12] 
                    new_6 = seller6_info[0] + ',' + seller6_info[1] + ',' + seller6_info[2] + ',' + seller6_info[3] + ',' + seller6_info[4] + ',' + seller6_info[5] + ',' + seller6_info[6] + ',' + seller6_info[7] + ',' + seller6_info[8] + ',' + seller6_info[9] + ',' + seller6_info[10] + ',' + seller6_info[11] + ',' + seller6_info[12] 
                    new_7 = seller7_info[0] + ',' + seller7_info[1] + ',' + seller7_info[2] + ',' + seller7_info[3] + ',' + seller7_info[4] + ',' + seller7_info[5] + ',' + seller7_info[6] + ',' + seller7_info[7] + ',' + seller7_info[8] + ',' + seller7_info[9] + ',' + seller7_info[10] + ',' + seller7_info[11] + ',' + seller7_info[12] 
                    new_8 = seller8_info[0] + ',' + seller8_info[1] + ',' + seller8_info[2] + ',' + seller8_info[3] + ',' + seller8_info[4] + ',' + seller8_info[5] + ',' + seller8_info[6] + ',' + seller8_info[7] + ',' + seller8_info[8] + ',' + seller8_info[9] + ',' + seller8_info[10] + ',' + seller8_info[11] + ',' + seller8_info[12]
                    new_9 = seller9_info[0] + ',' + seller9_info[1] + ',' + seller9_info[2] + ',' + seller9_info[3] + ',' + seller9_info[4] + ',' + seller9_info[5] + ',' + seller9_info[6] + ',' + seller9_info[7] + ',' + seller9_info[8] + ',' + seller9_info[9] + ',' + seller9_info[10] + ',' + seller9_info[11] + ',' + seller9_info[12] 
                    new_10 = seller10_info[0] + ',' + seller10_info[1] + ',' + seller10_info[2] + ',' + seller10_info[3] + ',' + seller10_info[4] + ',' + seller10_info[5] + ',' + seller10_info[6] + ',' + seller10_info[7] + ',' + seller10_info[8] + ',' + seller10_info[9] + ',' + seller10_info[10] + ',' + seller10_info[11] + ',' + seller10_info[12] 
                    f = open('sellers.txt', 'w')
                    g = f.close
                    h = open('sellers.txt', 'a')
                    write0 = h.write('#0-sellerid, 1-name, 2-lastname, 3-email, 4-website, 5-amountappsonsale, 6-app1, 7-app2, 8-app3, 9-app4, 10-app5, 11-downloadsUS, 12-downloadsCR' + '\n')
                    write1 = h.write(new_1)
                    write2 = h.write(new_2)
                    write3 = h.write(new_3)
                    write4 = h.write(new_4)
                    write5 = h.write(new_5)
                    write6 = h.write(new_6)
                    write7 = h.write(new_7)
                    write8 = h.write(new_8)
                    write9 = h.write(new_9)
                    write10 = h.write(new_10)
                    i = h.close

                    success_label = Label(add_game_window, text = 'Success', font = 'Helvetica 38', fg = 'firebrick3')
                    success_label.place(x=680, y=400)

                #labels para info de app que se quiera agregar
                appname_label = Label(add_game_window, text = 'Game Name', font = 'Helvetica 24')
                appname_label.place(x=100, y=50)

                desc1_label = Label(add_game_window, text = 'Description 1', font = 'Helvetica 24')
                desc1_label.place(x=100, y=100)

                desc2_label = Label(add_game_window, text = 'Description 2', font = 'Helvetica 24')
                desc2_label.place(x=100, y=150)

                desc3_label = Label(add_game_window, text = 'Description 3', font = 'Helvetica 24')
                desc3_label.place(x=100, y=200)

                desc4_label = Label(add_game_window, text = 'Description 4', font = 'Helvetica 24')
                desc4_label.place(x=100, y=250)

                desc5_label = Label(add_game_window, text = 'Description 5', font = 'Helvetica 24')
                desc5_label.place(x=100, y=300)

                desc1_esp_label = Label(add_game_window, text = 'Description 1 in Spanish', font = 'Helvetica 24')
                desc1_esp_label.place(x=100, y=350)

                desc2_esp_label = Label(add_game_window, text = 'Description 2 in Spanish', font = 'Helvetica 24')
                desc2_esp_label.place(x=100, y=400)

                desc3_esp_label = Label(add_game_window, text = 'Description 3 in Spanish', font = 'Helvetica 24')
                desc3_esp_label.place(x=100, y=450)

                desc4_esp_label = Label(add_game_window, text = 'Description 4 in Spanish', font = 'Helvetica 24')
                desc4_esp_label.place(x=100, y=500)

                desc5_esp_label = Label(add_game_window, text = 'Description 5 in Spanish', font = 'Helvetica 24')
                desc5_esp_label.place(x=100, y=550)

                price_label = Label(add_game_window, text = 'Price ($) or "Free"', font = 'Helvetica 24')
                price_label.place(x=600, y=50)

                appsize_label  = Label(add_game_window, text = 'App Size', font = 'Helvetica 24')
                appsize_label.place(x=600, y=100)

                #entries
                name_entry = Entry(add_game_window, width = 20)
                name_entry.place(x=400, y=50)

                desc1_entry = Entry(add_game_window, width = 20)
                desc1_entry.place(x=400, y=100)

                desc2_entry = Entry(add_game_window, width = 20)
                desc2_entry.place(x=400, y=150)

                desc3_entry = Entry(add_game_window, width = 20)
                desc3_entry.place(x=400, y=200)

                desc4_entry = Entry(add_game_window, width = 20)
                desc4_entry.place(x=400, y=250)

                desc5_entry = Entry(add_game_window, width = 20)
                desc5_entry.place(x=400, y=300)

                desc1_esp_entry = Entry(add_game_window, width = 20)
                desc1_esp_entry.place(x=400, y=350)

                desc2_esp_entry = Entry(add_game_window, width = 20)
                desc2_esp_entry.place(x=400, y=400)

                desc3_esp_entry = Entry(add_game_window, width = 20)
                desc3_esp_entry.place(x=400, y=450)

                desc4_esp_entry = Entry(add_game_window, width = 20)
                desc4_esp_entry.place(x=400, y=500)

                desc5_esp_entry = Entry(add_game_window, width = 20)
                desc5_esp_entry.place(x=400, y=550)

                price_entry = Entry(add_game_window, width = 20)
                price_entry.place(x=800, y=50)

                appsize_entry  = Entry(add_game_window, width = 20)
                appsize_entry.place(x=800, y=100)

                add_app_button = Button(add_game_window, text = 'Add Game', command = add_app)
                add_app_button.place(x=700, y=475)

                def back():
                    add_game_window.destroy()

                back_button = Button(add_game_window, image = exiticon, command = back)
                back_button.place(x=25,y=25)
                
                
            #labels de informacion
            name = Label(sellercanvas, text = seller9_info[1], font = 'Helvetica 24', fg = 'firebrick3')
            name.place(x=300, y=100)

            lastname = Label(sellercanvas, text = seller9_info[2], font = 'Helvetica 24', fg = 'firebrick3')
            lastname.place(x=300, y=200)

            email = Label(sellercanvas, text = seller9_info[3], font = 'Helvetica 24', fg = 'firebrick3')
            email.place(x=300, y=300)

            website = Label(sellercanvas, text = seller9_info[4], font = 'Helvetica 24', fg = 'firebrick3')
            website.place(x=300, y=400)

            amount_apps = Label(sellercanvas, text = seller9_info[5], font = 'Helvetica 24', fg = 'firebrick3')
            amount_apps.place(x=400, y=500)

            app1 = Label(sellercanvas, text = seller9_info[6], font = 'Helvetica 24', fg = 'firebrick3')
            app1.place(x=700, y=100)

            app1_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app1_downloads.place(x=600, y=140)
            
            app2 = Label(sellercanvas, text = seller9_info[7], font = 'Helvetica 24', fg = 'firebrick3')
            app2.place(x=700, y=200)
            
            app2_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app2_downloads.place(x=600, y=240)

            app3 = Label(sellercanvas, text = seller9_info[8], font = 'Helvetica 24', fg = 'firebrick3')
            app3.place(x=700, y=300)

            app3_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app3_downloads.place(x=600, y=340)

            app4 = Label(sellercanvas, text = seller9_info[9], font = 'Helvetica 24', fg = 'firebrick3')
            app4.place(x=700, y=400)
            
            app4_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app4_downloads.place(x=600, y=440)

            app5 = Label(sellercanvas, text = seller9_info[10], font = 'Helvetica 24', fg = 'firebrick3')
            app5.place(x=700, y=500)

            app5_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app5_downloads.place(x=600, y=540)

            name_label = Label(sellercanvas, text  = 'Seller name:', font = 'Helvetica 24')
            name_label.place(x=100, y=100)

            lastname_label = Label(sellercanvas, text = 'Last Name:', font = 'Helvetica 24')
            lastname_label.place(x=100, y=200)

            email_label = Label(sellercanvas, text = 'Email:', font = 'Helvetica 24')
            email_label.place(x=100, y=300)

            website_label = Label(sellercanvas, text = 'Website:', font = 'Helvetica 24')
            website_label.place(x=100, y=400)

            amount_apps_label = Label(sellercanvas, text = 'Amount apps on sale', font = 'Helvetica 24')
            amount_apps_label.place(x=100, y=500)

            app1_label = Label(sellercanvas, text = 'App 1', font = 'Helvetica 24')
            app1_label.place(x=600, y=100)

            app2_label = Label(sellercanvas, text = 'App 2', font = 'Helvetica 24')
            app2_label.place(x=600, y=200)

            app3_label = Label(sellercanvas, text = 'App 3', font = 'Helvetica 24')
            app3_label.place(x=600, y=300)

            app4_label = Label(sellercanvas, text = 'App 4', font = 'Helvetica 24')
            app4_label.place(x=600, y=400)

            app5_label = Label(sellercanvas, text = 'App 5', font = 'Helvetica 24')
            app5_label.place(x=600, y=500)

            #boton para agregar apps
            add_app_button = Button(sellercanvas, text = 'Add app', font = 'Helvetica 24', command = add_app_window)
            add_app_button.place(x=650, y=50)

            add_game_button = Button(sellercanvas, text = 'Add game', font = 'Helvetica 24', command = add_game_window)
            add_game_button.place(x=850, y=50)

        #misma estructura que vendedor 1
        def seller10():
            seller10 = Toplevel()
            seller10.title('Admin App')
            seller10.minsize(1000,600)
            seller10.resizable(width=NO, height=NO)

            sellercanvas = Canvas(seller10, width = 1000, height = 600)
            sellercanvas.place(x=0,y=0)

            all_sellers = open('sellers.txt', 'r')
            read_sellers = all_sellers.readlines()
            seller10_line = read_sellers[10]
            seller10_info = seller10_line.split(',')

            def back():
                seller10.destroy()

            back_button = Button(seller10, image = exiticon, command = back)
            back_button.place(x=25,y=25)

            def add_app_window():
                add_app_window = Toplevel()
                add_app_window.title('Admin App')
                add_app_window.minsize(1000,600)
                add_app_window.resizable(width=NO, height=NO)

                def add_app():
                    a = open ('appcount.txt','r+')
                    lastIndex = a.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    appname = name_entry.get()
                    desc1 = desc1_entry.get()
                    desc2 = desc2_entry.get()
                    desc3 = desc3_entry.get()
                    desc4 = desc4_entry.get()
                    desc5 = desc5_entry.get()
                    price = price_entry.get()
                    appsize = appsize_entry.get()
                    b = open('apps.txt','a')
                    info = '10' + ',' + productid + ',' + '0' + ',' + appname + ',' + desc1 + ',' + desc2 + ',' + desc3 + ',' + desc4 + ',' + desc5 + ',' + price + ',' + appsize + ',' + '0'
                    b.write('\n' + str(info))
                    a.close
                    b.close

                    c = open('appcount.txt','r+')
                    lastIndex = c.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    desc1_esp = desc1_esp_entry.get()
                    desc2_esp = desc2_esp_entry.get()
                    desc3_esp = desc3_esp_entry.get()
                    desc4_esp = desc4_esp_entry.get()
                    desc5_esp = desc5_esp_entry.get()
                    d = open('apps_esp.txt','a')
                    info = '10' + ',' + productid + ',' + '0' + ',' + appname + ',' + desc1_esp + ',' + desc2_esp + ',' + desc3_esp + ',' + desc4_esp + ',' + desc5_esp + ',' + price + ',' + appsize + ',' + '0'
                    d.write('\n' + str(info))
                    c.write('\n' + str(int(productid) + 1))
                    c.close
                    d.close

                    e = open('sellers.txt', 'r+')
                    read_seller_info = e.readlines()
                    seller1_line = read_seller_info[1]
                    seller1_info = seller1_line.split(',')
                    seller2_line = read_seller_info[2]
                    seller2_info = seller2_line.split(',')
                    seller3_line = read_seller_info[3]
                    seller3_info = seller3_line.split(',')
                    seller4_line = read_seller_info[4]
                    seller4_info = seller4_line.split(',')
                    seller5_line = read_seller_info[5]
                    seller5_info = seller5_line.split(',')
                    seller6_line = read_seller_info[6]
                    seller6_info = seller6_line.split(',')
                    seller7_line = read_seller_info[7]
                    seller7_info = seller7_line.split(',')
                    seller8_line = read_seller_info[8]
                    seller8_info = seller8_line.split(',')
                    seller9_line = read_seller_info[9]
                    seller9_info = seller9_line.split(',')
                    seller10_line = read_seller_info[10]
                    seller10_info = seller10_line.split(',')

                    if seller10_info[6] == '':
                        seller10_info[6] = name_entry.get() + ' (I)'
                        seller10_info[5] = str(int(seller10_info[5]) + 1)
                    elif seller10_info[7] == '':
                        seller10_info[7] = name_entry.get() + ' (I)'
                        seller10_info[5] = str(int(seller10_info[5]) + 1)
                    elif seller10_info[8] == '':
                        seller10_info[8] = name_entry.get() + ' (I)'
                        seller10_info[5] = str(int(seller10_info[5]) + 1)
                    elif seller10_info[9] == '':
                        seller10_info[9] = name_entry.get() + ' (I)'
                        seller10_info[5] = str(int(seller10_info[5]) + 1)
                    elif seller10_info[10] == '':
                        seller10_info[10] = name_entry.get() + ' (I)'
                        seller10_info[5] = str(int(seller10_info[5]) + 1)
                    else:
                            print('You have challenged the Matrix')
                    
                    new_1 = seller1_info[0] + ',' + seller1_info[1] + ',' + seller1_info[2] + ',' + seller1_info[3] + ',' + seller1_info[4] + ',' + seller1_info[5] + ',' + seller1_info[6] + ',' + seller1_info[7] + ',' + seller1_info[8] + ',' + seller1_info[9] + ',' + seller1_info[10] + ',' + seller1_info[11] + ',' + seller1_info[12] 
                    new_2 = seller2_info[0] + ',' + seller2_info[1] + ',' + seller2_info[2] + ',' + seller2_info[3] + ',' + seller2_info[4] + ',' + seller2_info[5] + ',' + seller2_info[6] + ',' + seller2_info[7] + ',' + seller2_info[8] + ',' + seller2_info[9] + ',' + seller2_info[10] + ',' + seller2_info[11] + ',' + seller2_info[12] 
                    new_3 = seller3_info[0] + ',' + seller3_info[1] + ',' + seller3_info[2] + ',' + seller3_info[3] + ',' + seller3_info[4] + ',' + seller3_info[5] + ',' + seller3_info[6] + ',' + seller3_info[7] + ',' + seller3_info[8] + ',' + seller3_info[9] + ',' + seller3_info[10] + ',' + seller3_info[11] + ',' + seller3_info[12] 
                    new_4 = seller4_info[0] + ',' + seller4_info[1] + ',' + seller4_info[2] + ',' + seller4_info[3] + ',' + seller4_info[4] + ',' + seller4_info[5] + ',' + seller4_info[6] + ',' + seller4_info[7] + ',' + seller4_info[8] + ',' + seller4_info[9] + ',' + seller4_info[10] + ',' + seller4_info[11] + ',' + seller4_info[12] 
                    new_5 = seller5_info[0] + ',' + seller5_info[1] + ',' + seller5_info[2] + ',' + seller5_info[3] + ',' + seller5_info[4] + ',' + seller5_info[5] + ',' + seller5_info[6] + ',' + seller5_info[7] + ',' + seller5_info[8] + ',' + seller5_info[9] + ',' + seller5_info[10] + ',' + seller5_info[11] + ',' + seller5_info[12] 
                    new_6 = seller6_info[0] + ',' + seller6_info[1] + ',' + seller6_info[2] + ',' + seller6_info[3] + ',' + seller6_info[4] + ',' + seller6_info[5] + ',' + seller6_info[6] + ',' + seller6_info[7] + ',' + seller6_info[8] + ',' + seller6_info[9] + ',' + seller6_info[10] + ',' + seller6_info[11] + ',' + seller6_info[12] 
                    new_7 = seller7_info[0] + ',' + seller7_info[1] + ',' + seller7_info[2] + ',' + seller7_info[3] + ',' + seller7_info[4] + ',' + seller7_info[5] + ',' + seller7_info[6] + ',' + seller7_info[7] + ',' + seller7_info[8] + ',' + seller7_info[9] + ',' + seller7_info[10] + ',' + seller7_info[11] + ',' + seller7_info[12] 
                    new_8 = seller8_info[0] + ',' + seller8_info[1] + ',' + seller8_info[2] + ',' + seller8_info[3] + ',' + seller8_info[4] + ',' + seller8_info[5] + ',' + seller8_info[6] + ',' + seller8_info[7] + ',' + seller8_info[8] + ',' + seller8_info[9] + ',' + seller8_info[10] + ',' + seller8_info[11] + ',' + seller8_info[12]
                    new_9 = seller9_info[0] + ',' + seller9_info[1] + ',' + seller9_info[2] + ',' + seller9_info[3] + ',' + seller9_info[4] + ',' + seller9_info[5] + ',' + seller9_info[6] + ',' + seller9_info[7] + ',' + seller9_info[8] + ',' + seller9_info[9] + ',' + seller9_info[10] + ',' + seller9_info[11] + ',' + seller9_info[12] 
                    new_10 = seller10_info[0] + ',' + seller10_info[1] + ',' + seller10_info[2] + ',' + seller10_info[3] + ',' + seller10_info[4] + ',' + seller10_info[5] + ',' + seller10_info[6] + ',' + seller10_info[7] + ',' + seller10_info[8] + ',' + seller10_info[9] + ',' + seller10_info[10] + ',' + seller10_info[11] + ',' + seller10_info[12] 
                    f = open('sellers.txt', 'w')
                    g = f.close
                    h = open('sellers.txt', 'a')
                    write0 = h.write('#0-sellerid, 1-name, 2-lastname, 3-email, 4-website, 5-amountappsonsale, 6-app1, 7-app2, 8-app3, 9-app4, 10-app5, 11-downloadsUS, 12-downloadsCR' + '\n')
                    write1 = h.write(new_1)
                    write2 = h.write(new_2)
                    write3 = h.write(new_3)
                    write4 = h.write(new_4)
                    write5 = h.write(new_5)
                    write6 = h.write(new_6)
                    write7 = h.write(new_7)
                    write8 = h.write(new_8)
                    write9 = h.write(new_9)
                    write10 = h.write(new_10)
                    i = h.close

                    success_label = Label(add_app_window, text = 'Success', font = 'Helvetica 38', fg = 'firebrick3')
                    success_label.place(x=680, y=400)

                #labels para info de app que se quiera agregar
                appname_label = Label(add_app_window, text = 'App Name', font = 'Helvetica 24')
                appname_label.place(x=100, y=50)

                desc1_label = Label(add_app_window, text = 'Description 1', font = 'Helvetica 24')
                desc1_label.place(x=100, y=100)

                desc2_label = Label(add_app_window, text = 'Description 2', font = 'Helvetica 24')
                desc2_label.place(x=100, y=150)

                desc3_label = Label(add_app_window, text = 'Description 3', font = 'Helvetica 24')
                desc3_label.place(x=100, y=200)

                desc4_label = Label(add_app_window, text = 'Description 4', font = 'Helvetica 24')
                desc4_label.place(x=100, y=250)

                desc5_label = Label(add_app_window, text = 'Description 5', font = 'Helvetica 24')
                desc5_label.place(x=100, y=300)

                desc1_esp_label = Label(add_app_window, text = 'Description 1 in Spanish', font = 'Helvetica 24')
                desc1_esp_label.place(x=100, y=350)

                desc2_esp_label = Label(add_app_window, text = 'Description 2 in Spanish', font = 'Helvetica 24')
                desc2_esp_label.place(x=100, y=400)

                desc3_esp_label = Label(add_app_window, text = 'Description 3 in Spanish', font = 'Helvetica 24')
                desc3_esp_label.place(x=100, y=450)

                desc4_esp_label = Label(add_app_window, text = 'Description 4 in Spanish', font = 'Helvetica 24')
                desc4_esp_label.place(x=100, y=500)

                desc5_esp_label = Label(add_app_window, text = 'Description 5 in Spanish', font = 'Helvetica 24')
                desc5_esp_label.place(x=100, y=550)

                price_label = Label(add_app_window, text = 'Price ($) or "Free"', font = 'Helvetica 24')
                price_label.place(x=600, y=50)

                appsize_label  = Label(add_app_window, text = 'App Size', font = 'Helvetica 24')
                appsize_label.place(x=600, y=100)

                #entries
                name_entry = Entry(add_app_window, width = 20)
                name_entry.place(x=400, y=50)

                desc1_entry = Entry(add_app_window, width = 20)
                desc1_entry.place(x=400, y=100)

                desc2_entry = Entry(add_app_window, width = 20)
                desc2_entry.place(x=400, y=150)

                desc3_entry = Entry(add_app_window, width = 20)
                desc3_entry.place(x=400, y=200)

                desc4_entry = Entry(add_app_window, width = 20)
                desc4_entry.place(x=400, y=250)

                desc5_entry = Entry(add_app_window, width = 20)
                desc5_entry.place(x=400, y=300)

                desc1_esp_entry = Entry(add_app_window, width = 20)
                desc1_esp_entry.place(x=400, y=350)

                desc2_esp_entry = Entry(add_app_window, width = 20)
                desc2_esp_entry.place(x=400, y=400)

                desc3_esp_entry = Entry(add_app_window, width = 20)
                desc3_esp_entry.place(x=400, y=450)

                desc4_esp_entry = Entry(add_app_window, width = 20)
                desc4_esp_entry.place(x=400, y=500)

                desc5_esp_entry = Entry(add_app_window, width = 20)
                desc5_esp_entry.place(x=400, y=550)

                price_entry = Entry(add_app_window, width = 20)
                price_entry.place(x=800, y=50)

                appsize_entry  = Entry(add_app_window, width = 20)
                appsize_entry.place(x=800, y=100)

                add_app_button = Button(add_app_window, text = 'Add App', command = add_app)
                add_app_button.place(x=700, y=475)

                def back():
                    add_app_window.destroy()

                back_button = Button(add_app_window, image = exiticon, command = back)
                back_button.place(x=25,y=25)

            def add_game_window():
                add_game_window = Toplevel()
                add_game_window.title('Admin App')
                add_game_window.minsize(1000,600)
                add_game_window.resizable(width=NO, height=NO)

                def add_app():
                    a = open ('appcount.txt','r+')
                    lastIndex = a.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    appname = name_entry.get()
                    desc1 = desc1_entry.get()
                    desc2 = desc2_entry.get()
                    desc3 = desc3_entry.get()
                    desc4 = desc4_entry.get()
                    desc5 = desc5_entry.get()
                    price = price_entry.get()
                    appsize = appsize_entry.get()
                    b = open('games.txt','a')
                    info = '10' + ',' + productid + ',' + '1' + ',' + appname + ',' + desc1 + ',' + desc2 + ',' + desc3 + ',' + desc4 + ',' + desc5 + ',' + price + ',' + appsize + ',' + '0'
                    b.write('\n' + str(info))
                    a.close
                    b.close

                    c = open('appcount.txt','r+')
                    lastIndex = c.readlines()
                    productid = lastIndex[len(lastIndex) - 1]
                    desc1_esp = desc1_esp_entry.get()
                    desc2_esp = desc2_esp_entry.get()
                    desc3_esp = desc3_esp_entry.get()
                    desc4_esp = desc4_esp_entry.get()
                    desc5_esp = desc5_esp_entry.get()
                    d = open('games_esp.txt','a')
                    info = '10' + ',' + productid + ',' + '1' + ',' + appname + ',' + desc1_esp + ',' + desc2_esp + ',' + desc3_esp + ',' + desc4_esp + ',' + desc5_esp + ',' + price + ',' + appsize + ',' + '0'
                    d.write('\n' + str(info))
                    c.write('\n' + str(int(productid) + 1))
                    c.close
                    d.close

                    e = open('sellers.txt', 'r+')
                    read_seller_info = e.readlines()
                    seller1_line = read_seller_info[1]
                    seller1_info = seller1_line.split(',')
                    seller2_line = read_seller_info[2]
                    seller2_info = seller2_line.split(',')
                    seller3_line = read_seller_info[3]
                    seller3_info = seller3_line.split(',')
                    seller4_line = read_seller_info[4]
                    seller4_info = seller4_line.split(',')
                    seller5_line = read_seller_info[5]
                    seller5_info = seller5_line.split(',')
                    seller6_line = read_seller_info[6]
                    seller6_info = seller6_line.split(',')
                    seller7_line = read_seller_info[7]
                    seller7_info = seller7_line.split(',')
                    seller8_line = read_seller_info[8]
                    seller8_info = seller8_line.split(',')
                    seller9_line = read_seller_info[9]
                    seller9_info = seller9_line.split(',')
                    seller10_line = read_seller_info[10]
                    seller10_info = seller10_line.split(',')

                    if seller10_info[6] == '':
                        seller10_info[6] = name_entry.get() + ' (I)'
                    elif seller10_info[7] == '':
                        seller10_info[7] = name_entry.get() + ' (I)'
                        seller10_info[5] = str(int(seller10_info[5]) + 1)
                    elif seller10_info[8] == '':
                        seller10_info[8] = name_entry.get() + ' (I)'
                        seller10_info[5] = str(int(seller10_info[5]) + 1)
                    elif seller10_info[9] == '':
                        seller10_info[9] = name_entry.get() + ' (I)'
                        seller10_info[5] = str(int(seller10_info[5]) + 1)
                    elif seller10_info[10] == '':
                        seller10_info[10] = name_entry.get() + ' (I)'
                        seller10_info[5] = str(int(seller10_info[5]) + 1)
                    else:
                        print('You have challenged the Matrix')
                    
                    new_1 = seller1_info[0] + ',' + seller1_info[1] + ',' + seller1_info[2] + ',' + seller1_info[3] + ',' + seller1_info[4] + ',' + seller1_info[5] + ',' + seller1_info[6] + ',' + seller1_info[7] + ',' + seller1_info[8] + ',' + seller1_info[9] + ',' + seller1_info[10] + ',' + seller1_info[11] + ',' + seller1_info[12] 
                    new_2 = seller2_info[0] + ',' + seller2_info[1] + ',' + seller2_info[2] + ',' + seller2_info[3] + ',' + seller2_info[4] + ',' + seller2_info[5] + ',' + seller2_info[6] + ',' + seller2_info[7] + ',' + seller2_info[8] + ',' + seller2_info[9] + ',' + seller2_info[10] + ',' + seller2_info[11] + ',' + seller2_info[12] 
                    new_3 = seller3_info[0] + ',' + seller3_info[1] + ',' + seller3_info[2] + ',' + seller3_info[3] + ',' + seller3_info[4] + ',' + seller3_info[5] + ',' + seller3_info[6] + ',' + seller3_info[7] + ',' + seller3_info[8] + ',' + seller3_info[9] + ',' + seller3_info[10] + ',' + seller3_info[11] + ',' + seller3_info[12] 
                    new_4 = seller4_info[0] + ',' + seller4_info[1] + ',' + seller4_info[2] + ',' + seller4_info[3] + ',' + seller4_info[4] + ',' + seller4_info[5] + ',' + seller4_info[6] + ',' + seller4_info[7] + ',' + seller4_info[8] + ',' + seller4_info[9] + ',' + seller4_info[10] + ',' + seller4_info[11] + ',' + seller4_info[12] 
                    new_5 = seller5_info[0] + ',' + seller5_info[1] + ',' + seller5_info[2] + ',' + seller5_info[3] + ',' + seller5_info[4] + ',' + seller5_info[5] + ',' + seller5_info[6] + ',' + seller5_info[7] + ',' + seller5_info[8] + ',' + seller5_info[9] + ',' + seller5_info[10] + ',' + seller5_info[11] + ',' + seller5_info[12] 
                    new_6 = seller6_info[0] + ',' + seller6_info[1] + ',' + seller6_info[2] + ',' + seller6_info[3] + ',' + seller6_info[4] + ',' + seller6_info[5] + ',' + seller6_info[6] + ',' + seller6_info[7] + ',' + seller6_info[8] + ',' + seller6_info[9] + ',' + seller6_info[10] + ',' + seller6_info[11] + ',' + seller6_info[12] 
                    new_7 = seller7_info[0] + ',' + seller7_info[1] + ',' + seller7_info[2] + ',' + seller7_info[3] + ',' + seller7_info[4] + ',' + seller7_info[5] + ',' + seller7_info[6] + ',' + seller7_info[7] + ',' + seller7_info[8] + ',' + seller7_info[9] + ',' + seller7_info[10] + ',' + seller7_info[11] + ',' + seller7_info[12] 
                    new_8 = seller8_info[0] + ',' + seller8_info[1] + ',' + seller8_info[2] + ',' + seller8_info[3] + ',' + seller8_info[4] + ',' + seller8_info[5] + ',' + seller8_info[6] + ',' + seller8_info[7] + ',' + seller8_info[8] + ',' + seller8_info[9] + ',' + seller8_info[10] + ',' + seller8_info[11] + ',' + seller8_info[12]
                    new_9 = seller9_info[0] + ',' + seller9_info[1] + ',' + seller9_info[2] + ',' + seller9_info[3] + ',' + seller9_info[4] + ',' + seller9_info[5] + ',' + seller9_info[6] + ',' + seller9_info[7] + ',' + seller9_info[8] + ',' + seller9_info[9] + ',' + seller9_info[10] + ',' + seller9_info[11] + ',' + seller9_info[12] 
                    new_10 = seller10_info[0] + ',' + seller10_info[1] + ',' + seller10_info[2] + ',' + seller10_info[3] + ',' + seller10_info[4] + ',' + seller10_info[5] + ',' + seller10_info[6] + ',' + seller10_info[7] + ',' + seller10_info[8] + ',' + seller10_info[9] + ',' + seller10_info[10] + ',' + seller10_info[11] + ',' + seller10_info[12] 
                    f = open('sellers.txt', 'w')
                    g = f.close
                    h = open('sellers.txt', 'a')
                    write0 = h.write('#0-sellerid, 1-name, 2-lastname, 3-email, 4-website, 5-amountappsonsale, 6-app1, 7-app2, 8-app3, 9-app4, 10-app5, 11-downloadsUS, 12-downloadsCR' + '\n')
                    write1 = h.write(new_1)
                    write2 = h.write(new_2)
                    write3 = h.write(new_3)
                    write4 = h.write(new_4)
                    write5 = h.write(new_5)
                    write6 = h.write(new_6)
                    write7 = h.write(new_7)
                    write8 = h.write(new_8)
                    write9 = h.write(new_9)
                    write10 = h.write(new_10)
                    i = h.close

                    success_label = Label(add_game_window, text = 'Success', font = 'Helvetica 38', fg = 'firebrick3')
                    success_label.place(x=680, y=400)

                #labels para info de app que se quiera agregar
                appname_label = Label(add_game_window, text = 'Game Name', font = 'Helvetica 24')
                appname_label.place(x=100, y=50)

                desc1_label = Label(add_game_window, text = 'Description 1', font = 'Helvetica 24')
                desc1_label.place(x=100, y=100)

                desc2_label = Label(add_game_window, text = 'Description 2', font = 'Helvetica 24')
                desc2_label.place(x=100, y=150)

                desc3_label = Label(add_game_window, text = 'Description 3', font = 'Helvetica 24')
                desc3_label.place(x=100, y=200)

                desc4_label = Label(add_game_window, text = 'Description 4', font = 'Helvetica 24')
                desc4_label.place(x=100, y=250)

                desc5_label = Label(add_game_window, text = 'Description 5', font = 'Helvetica 24')
                desc5_label.place(x=100, y=300)

                desc1_esp_label = Label(add_game_window, text = 'Description 1 in Spanish', font = 'Helvetica 24')
                desc1_esp_label.place(x=100, y=350)

                desc2_esp_label = Label(add_game_window, text = 'Description 2 in Spanish', font = 'Helvetica 24')
                desc2_esp_label.place(x=100, y=400)

                desc3_esp_label = Label(add_game_window, text = 'Description 3 in Spanish', font = 'Helvetica 24')
                desc3_esp_label.place(x=100, y=450)

                desc4_esp_label = Label(add_game_window, text = 'Description 4 in Spanish', font = 'Helvetica 24')
                desc4_esp_label.place(x=100, y=500)

                desc5_esp_label = Label(add_game_window, text = 'Description 5 in Spanish', font = 'Helvetica 24')
                desc5_esp_label.place(x=100, y=550)

                price_label = Label(add_game_window, text = 'Price ($) or "Free"', font = 'Helvetica 24')
                price_label.place(x=600, y=50)

                appsize_label  = Label(add_game_window, text = 'App Size', font = 'Helvetica 24')
                appsize_label.place(x=600, y=100)

                #entries
                name_entry = Entry(add_game_window, width = 20)
                name_entry.place(x=400, y=50)

                desc1_entry = Entry(add_game_window, width = 20)
                desc1_entry.place(x=400, y=100)

                desc2_entry = Entry(add_game_window, width = 20)
                desc2_entry.place(x=400, y=150)

                desc3_entry = Entry(add_game_window, width = 20)
                desc3_entry.place(x=400, y=200)

                desc4_entry = Entry(add_game_window, width = 20)
                desc4_entry.place(x=400, y=250)

                desc5_entry = Entry(add_game_window, width = 20)
                desc5_entry.place(x=400, y=300)

                desc1_esp_entry = Entry(add_game_window, width = 20)
                desc1_esp_entry.place(x=400, y=350)

                desc2_esp_entry = Entry(add_game_window, width = 20)
                desc2_esp_entry.place(x=400, y=400)

                desc3_esp_entry = Entry(add_game_window, width = 20)
                desc3_esp_entry.place(x=400, y=450)

                desc4_esp_entry = Entry(add_game_window, width = 20)
                desc4_esp_entry.place(x=400, y=500)

                desc5_esp_entry = Entry(add_game_window, width = 20)
                desc5_esp_entry.place(x=400, y=550)

                price_entry = Entry(add_game_window, width = 20)
                price_entry.place(x=800, y=50)

                appsize_entry  = Entry(add_game_window, width = 20)
                appsize_entry.place(x=800, y=100)

                add_app_button = Button(add_game_window, text = 'Add Game', command = add_app)
                add_app_button.place(x=700, y=475)

                def back():
                    add_game_window.destroy()

                back_button = Button(add_game_window, image = exiticon, command = back)
                back_button.place(x=25,y=25)
                
                
            #labels de informacion
            name = Label(sellercanvas, text = seller10_info[1], font = 'Helvetica 24', fg = 'firebrick3')
            name.place(x=300, y=100)

            lastname = Label(sellercanvas, text = seller10_info[2], font = 'Helvetica 24', fg = 'firebrick3')
            lastname.place(x=300, y=200)

            email = Label(sellercanvas, text = seller10_info[3], font = 'Helvetica 24', fg = 'firebrick3')
            email.place(x=300, y=300)

            website = Label(sellercanvas, text = seller10_info[4], font = 'Helvetica 24', fg = 'firebrick3')
            website.place(x=300, y=400)

            amount_apps = Label(sellercanvas, text = seller10_info[5], font = 'Helvetica 24', fg = 'firebrick3')
            amount_apps.place(x=400, y=500)

            app1 = Label(sellercanvas, text = seller10_info[6], font = 'Helvetica 24', fg = 'firebrick3')
            app1.place(x=700, y=100)

            app1_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app1_downloads.place(x=600, y=140)
            
            app2 = Label(sellercanvas, text = seller10_info[7], font = 'Helvetica 24', fg = 'firebrick3')
            app2.place(x=700, y=200)
            
            app2_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app2_downloads.place(x=600, y=240)

            app3 = Label(sellercanvas, text = seller10_info[8], font = 'Helvetica 24', fg = 'firebrick3')
            app3.place(x=700, y=300)

            app3_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app3_downloads.place(x=600, y=340)

            app4 = Label(sellercanvas, text = seller10_info[9], font = 'Helvetica 24', fg = 'firebrick3')
            app4.place(x=700, y=400)
            
            app4_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app4_downloads.place(x=600, y=440)

            app5 = Label(sellercanvas, text = seller10_info[10], font = 'Helvetica 24', fg = 'firebrick3')
            app5.place(x=700, y=500)

            app5_downloads = Label(sellercanvas, text = 'Downloads US: '+'0'+'\n'+'Downloads CR: '+'0', font = 'Helvetica 16')
            app5_downloads.place(x=600, y=540)

            name_label = Label(sellercanvas, text  = 'Seller name:', font = 'Helvetica 24')
            name_label.place(x=100, y=100)

            lastname_label = Label(sellercanvas, text = 'Last Name:', font = 'Helvetica 24')
            lastname_label.place(x=100, y=200)

            email_label = Label(sellercanvas, text = 'Email:', font = 'Helvetica 24')
            email_label.place(x=100, y=300)

            website_label = Label(sellercanvas, text = 'Website:', font = 'Helvetica 24')
            website_label.place(x=100, y=400)

            amount_apps_label = Label(sellercanvas, text = 'Amount apps on sale', font = 'Helvetica 24')
            amount_apps_label.place(x=100, y=500)

            app1_label = Label(sellercanvas, text = 'App 1', font = 'Helvetica 24')
            app1_label.place(x=600, y=100)

            app2_label = Label(sellercanvas, text = 'App 2', font = 'Helvetica 24')
            app2_label.place(x=600, y=200)

            app3_label = Label(sellercanvas, text = 'App 3', font = 'Helvetica 24')
            app3_label.place(x=600, y=300)

            app4_label = Label(sellercanvas, text = 'App 4', font = 'Helvetica 24')
            app4_label.place(x=600, y=400)

            app5_label = Label(sellercanvas, text = 'App 5', font = 'Helvetica 24')
            app5_label.place(x=600, y=500)

            #boton para agregar apps
            add_app_button = Button(sellercanvas, text = 'Add app', font = 'Helvetica 24', command = add_app_window)
            add_app_button.place(x=650, y=50)

            add_game_button = Button(sellercanvas, text = 'Add game', font = 'Helvetica 24', command = add_game_window)
            add_game_button.place(x=850, y=50)

        seller1_button = Button(monitor_window, text = 'Seller 1', font = 'Helvetica 24', command = seller1)
        seller1_button.place(x=200,y=100)

        seller2_button = Button(monitor_window, text = 'Seller 2', font = 'Helvetica 24', command = seller2)
        seller2_button.place(x=200,y=200)
        
        seller3_button = Button(monitor_window, text = 'Seller 3', font = 'Helvetica 24', command = seller3)
        seller3_button.place(x=200,y=300)

        seller4_button = Button(monitor_window, text = 'Seller 4', font = 'Helvetica 24', command = seller4)
        seller4_button.place(x=200,y=400)

        seller5_button = Button(monitor_window, text = 'Seller 5', font = 'Helvetica 24', command = seller5)
        seller5_button.place(x=200,y=500)

        seller6_button = Button(monitor_window, text = 'Seller 6', font = 'Helvetica 24', command = seller6)
        seller6_button.place(x=600,y=100)

        seller7_button = Button(monitor_window, text = 'Seller 7', font = 'Helvetica 24', command = seller7)
        seller7_button.place(x=600,y=200)

        seller8_button = Button(monitor_window, text = 'Seller 8', font = 'Helvetica 24', command = seller8)
        seller8_button.place(x=600,y=300)

        seller9_button = Button(monitor_window, text = 'Seller 9', font = 'Helvetica 24', command = seller9)
        seller9_button.place(x=600,y=400)

        seller10_button = Button(monitor_window, text = 'Seller 10', font = 'Helvetica 24', command = seller10)
        seller10_button.place(x=600,y=500)

    def reset():
        #reset de sellers
        a = open('sellers.txt', 'w')
        a.close
        b = open('sellers.txt', 'a')
        write0 = '#0-sellerid, 1-name, 2-lastname, 3-email, 4-website, 5-amountappsonsale, 6-app1, 7-app2, 8-app3, 9-app4, 10-app5, 11-downloadsUS, 12-downloadsCR' + '\n'
        write1 = '1, Jeff, Schmidt, jschmidtcr@gmail.com, www.ventas-jeff.com,3, Jeff Schmidt\'s Python (A), NOTLIM (A), Unbreakable (A),,, 0, 0' + '\n'
        write2 = '2, Mariana, Alison, malison@420.com, www.420weed.com,2, Weed Smoke PRO (A), Monument Valley (A),,,, 0, 0' + '\n'
        write3 = '3, Ed, Sheeran, ted@edsheeran.com, www.edsheeran.com,4, Math with Ed Sheeran (A), Taylor\'s Swift (A), Kiss me pls (A), Game of Shots (A),, 0, 0' + '\n'
        write4 = '4, Edward, Kenway, kenway@ubisoft.com, www.ubisoft.com,1, The Pirate Bay (A),,,,, 0,0' + '\n'
        write5 = '5, Tim, Cook, tcook@apple.com, apple.com,2, Apple Music (A), Stocks (A),,,, 0,0' + '\n'
        write6 = '6, Jeff, Bezos, jbezos@netflix.com,netflix.com,1, Netflix (A),,,,,0,0' + '\n'
        write7 = '7, Alejandro, Ibarra, alejandroi@hotmail.com,ale.net,3, Intro & Taller (A), Jessie (A), Life is Strange (A),,,0,0'

        b.write(write0)
        b.write(write1)
        b.write(write2)
        b.write(write3)
        b.write(write4)
        b.write(write5)
        b.write(write6)
        b.write(write7)
        b.close()

        #reset de apps (eng)
        apps = open('apps.txt', 'r+')
        read_apps = apps.readlines()

        app0_line = read_apps[0]
        app1_line = read_apps[1]
        app2_line = read_apps[2]
        app3_line = read_apps[3]
        app4_line = read_apps[4]
        app5_line = read_apps[5]
        app6_line = read_apps[6]
        app7_line = read_apps[7]
        app8_line = read_apps[8]
        apps.close()

        c = open('apps.txt', 'w')
        c.close()
        
        d = open('apps.txt', 'a')
        write0 = app0_line 
        write1 = app1_line 
        write2 = app2_line 
        write3 = app3_line 
        write4 = app4_line 
        write5 = app5_line 
        write6 = app6_line 
        write7 = app7_line
        write8 = app8_line

        d.write(write0)
        d.write(write1)
        d.write(write2)
        d.write(write3)
        d.write(write4)
        d.write(write5)
        d.write(write6)
        d.write(write7)
        d.write(write8)
        d.close()

        #reset de games (eng)
        games = open('games.txt', 'r+')
        read_games = games.readlines()

        game0_line = read_games[0]
        game1_line = read_games[1]
        game2_line = read_games[2]
        game3_line = read_games[3]
        game4_line = read_games[4]
        game5_line = read_games[5]
        game6_line = read_games[6]
        game7_line = read_games[7]
        game8_line = read_games[8]
        games.close()

        e = open('games.txt', 'w')
        e.close()

        f = open('games.txt', 'a')
        write0 = game0_line 
        write1 = game1_line 
        write2 = game2_line 
        write3 = game3_line 
        write4 = game4_line
        write5 = game5_line 
        write6 = game6_line 
        write7 = game7_line 
        write8 = game8_line

        f.write(write0)
        f.write(write1)
        f.write(write2)
        f.write(write3)
        f.write(write4)
        f.write(write5)
        f.write(write6)
        f.write(write7)
        f.write(write8)
        f.close()

        #reset de apps esp
        apps = open('apps_esp.txt', 'r+')
        read_apps = apps.readlines()

        app0_line = read_apps[0]
        app1_line = read_apps[1]
        app2_line = read_apps[2]
        app3_line = read_apps[3]
        app4_line = read_apps[4]
        app5_line = read_apps[5]
        app6_line = read_apps[6]
        app7_line = read_apps[7]
        app8_line = read_apps[8]
        apps.close()

        c = open('apps_esp.txt', 'w')
        c.close()
        
        d = open('apps_esp.txt', 'a')
        write0 = app0_line 
        write1 = app1_line
        write2 = app2_line 
        write3 = app3_line 
        write4 = app4_line 
        write5 = app5_line
        write6 = app6_line
        write7 = app7_line
        write8 = app8_line

        d.write(write0)
        d.write(write1)
        d.write(write2)
        d.write(write3)
        d.write(write4)
        d.write(write5)
        d.write(write6)
        d.write(write7)
        d.write(write8)

        #reset de games (esp)
        games = open('games_esp.txt', 'r+')
        read_games = games.readlines()

        game0_line = read_games[0]
        game1_line = read_games[1]
        game2_line = read_games[2]
        game3_line = read_games[3]
        game4_line = read_games[4]
        game5_line = read_games[5]
        game6_line = read_games[6]
        game7_line = read_games[7]
        game8_line = read_games[8]
        games.close()

        e = open('games_esp.txt', 'w')
        e.close()

        f = open('games_esp.txt', 'a')
        write0 = game0_line
        write1 = game1_line
        write2 = game2_line
        write3 = game3_line
        write4 = game4_line
        write5 = game5_line
        write6 = game6_line
        write7 = game7_line
        write8 = game8_line

        f.write(write0)
        f.write(write1)
        f.write(write2)
        f.write(write3)
        f.write(write4)
        f.write(write5)
        f.write(write6)
        f.write(write7)
        f.write(write8)
        f.close()

        #reset de conteo de vendedores y apps
        g = open('sellercount.txt', 'w')
        g.close()

        h = open('sellercount.txt', 'a')
        h.write('#ID de siguiente vendedor a registrar'+'\n'+'8')
        h.close()

        i = open('appcount.txt', 'w')
        i.close()

        j = open('appcount.txt', 'a')
        j.write('#ID de siguiente aplicacion a registrar'+'\n'+'17')
        j.close()

        warninglabel = Label(logged_canvas, text = 'Additional sellers and app data has been reset.\nTo add apps, at least 10 sellers have to be registered\nCurrent amount of sellers: 7', font = 'Helvetica 16', fg = 'firebrick3')
        warninglabel.place(x=350, y=510)

    monitor_seller_button = Button(logged_canvas, image = monitorsellericon, font = 'Helvetica 24', command = monitor_window)
    monitor_seller_button.place(x=550, y=150)

    add_seller_button = Button(logged_canvas, image = addsellericon, font = 'Helvetica 24', command = register_window)
    add_seller_button.place(x=100, y= 150)

    reset_button = Button(logged_canvas, image = resetsellericon, font = 'Helvetica 24', command = reset)
    reset_button.place(x=750, y=500)

#labels de ventana principal
access_label = Label(root, text = 'Developer Access', font = 'Helvetica 36')
access_label.place(x=350, y=70)

riddle_label = Label(root, image = riddle)
riddle_label.place(x=320, y=150)

riddle_instruction_label = Label(root, text = 'What is the function missing?', font = 'Helvetica 24')
riddle_instruction_label.place(x=330, y= 290)

key_entry = Entry(root, width = 25, show = '*')
key_entry.place(x=380, y=360)

login_button = Button(root, text = 'I\'m feeling lucky', font = 'Helvetica 24', command = check_login)
login_button.place(x=390, y=400)
