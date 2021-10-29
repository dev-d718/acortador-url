# Developed by Dev-D_Y_Punto

import requests , sys , time , os , socket
from bs4 import BeautifulSoup as bSoup 
from colorama import init , Fore
init()

def Main() :
    os.system('clear')

    banner = """
                               8888888b.  8888888888 888     888       8888888b.              
                               888  "Y88b 888        888     888       888  "Y88b             
                               888    888 888        888     888       888    888             
                               888    888 8888888    Y88b   d88P       888    888             
                               888    888 888         Y88b d88P        888    888             
                               888    888 888          Y88o88P  888888 888    888             
                               888  .d88P 888           Y888P          888  .d88P             
                               8888888P"  8888888888     Y8P           8888888P"              
                                                               
                                                               
                                                               
                               Y88b   d88P        8888888b.                    888            
                                Y88b d88P         888   Y88b                   888            
                                 Y88o88P          888    888                   888            
                                  Y888P           888   d88P 888  888 88888b.  888888 .d88b.  
                                   888            8888888P"  888  888 888 "88b 888   d88""88b 
                                   888            888        888  888 888  888 888   888  888 
                                   888            888        Y88b 888 888  888 Y88b. Y88..88P 
                                   888   88888888 888         "Y88888 888  888  "Y888 "Y88P" """

    tagline = """                                                                                               [v 1.0]
    -------------------------------------------------------------------------------------------------------------------------------
                                         Oculta Tus Enlaces Maliciosos   [+] By Dev-D_Y_Punto
    -------------------------------------------------------------------------------------------------------------------------------
 """
    def banners() :
        print(Fore.CYAN+banner)
        print(Fore.LIGHTCYAN_EX+tagline)
    banners()    

    itms = ["Comprobando internet /","Comprobando internet -","Comprobando internet \\","Comprobando internet |"]

    def spinning_cursor():
        while True:
            for cursor in itms:
                yield cursor

    spinner = spinning_cursor()
    for iii in range(50):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b')
    try:
        ip = socket.gethostbyname("www.google.com")  
    except Exception as e:
        os.system('clear')
        banners()
        print(Fore.LIGHTRED_EX + "No Internet !")  
        time.sleep(5)
        exit()    

    os.system('clear')
    banners()
    
    print(Fore.CYAN + "[01] Facebook     [07] Amazon         [13] Linkedin           [19] Twitch          [25]                 ")
    print("[02] Google       [08] Apple          [14] Microsoft          [20] Twitter         [26]                   ")
    print("[03] Instagram    [09] Badoo          [15] Netflix            [21] Wifi            [27]                   ")
    print("[04] Youtube      [10] Ebay           [16] Paypal             [22] WordPress       [28]                   ")
    print("[05] Twitter      [11] GitHub         [17] Pinterest          [23] Yahoo           [29]                   ")
    print("[06] Spotify      [12] iCloud         [18] Snapchat           [24] Pornhub         [30]                   ")
    smedia = input("\nSelector > ")
    if smedia == "01" :
        social = "https://www.facebook.com"
    elif smedia == "02" :
        social = "https://www.google.com"
    elif smedia == "03" :
        social = "https://www.instagram.com"
    elif smedia == "04" :
        social = "https://www.youtube.com"
    elif smedia == "05" :
        social = "https://www.twitter.com"
    elif smedia == "06" :
        social = "https://www.spotify.com" 
    elif smedia == "07" :
        social = "https://www.amazon.com"  
    else :
        print("Opcion por defecto Facebook !")
        social = "https:/www.facebook.com" 

    iurl = input("\nPon aqui tu url : ")

    postname = input("\n-Nombre para el enlace de la publicación (ej:separa-siempre-las-palabras-que-quieras-asi-con "-") : ")    

    url = "https://www.shorturl.at/shortener.php"
    data = {"u": iurl}

    res = requests.post(url,data=data)
    rcode = res.status_code

    if  rcode == 200 :
        #rdata = res.text
        page_html = res.text
        page_soup = bSoup(page_html,"html.parser")
        urltag = page_soup.find("input",{"id":"shortenurl"})

        surl = urltag['value']
        full_url = social + "-" + postname + "@" + surl

        print(Fore.LIGHTGREEN_EX + "\nCopia este link >  ",full_url)

    else :
        print(Fore.LIGHTRED_EX + "Error !",rcode)
    
    print(Fore.CYAN+"")
    loop = int(input("Enmascarar de nuevo ?\n\n[98] SI\n[99] No\n\nChoice > "))
    if loop == 98 :
        Main()
    else:
        exit()    


Main()        
