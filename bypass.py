import pystyle
import requests

def main():
    base_urls = [
        "https://dlr-api.woozym.workers.dev/api/deloreanv2/goatbypassersontop/free?url=",
        "https://api.bypass.vip/bypass?url=",
        "https://bypass.pm/bypass2?url="
    ]
    banner = """
                        :::!~!!!!!:.
                    .xUHWH!! !!?M88WHX:.
                    .X*#M@$!!  !X!M$$$$$$WWx:.
                :!!!!!!?H! :!$!$$$$$$$$$$8X:
                !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
                :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
                ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
                !:~~~ .:!M"T#$$$$WX??#MRRMMM!
                ~?WuxiW*`   `"#$$$$8!!!!??!!!
                :X- M$$$$       `"T#$T~!8$WUXU~
                :%`  ~#$$$m:        ~!~ ?$$$$$$
            :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
    .....   -~~:<` !    ~?T#$$@@W@*?$$      /`
    W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
    #"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
    :::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
    .~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
    Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
    $R@i.~~ !     :   ~$$$$$B$$en:``
    ?MXT@Wx.~    :     ~"##*$$$$M~
    """
    text = pystyle.Colorate.Vertical(pystyle.Colors.red_to_yellow, """
    ___  _   _ ___  ____ ____ ____ ____ ____ 
    |__]  \_/  |__] |__| [__  [__  |___ |__/ 
    |__]   |   |    |  | ___] ___] |___ |  \ 
                                             
    """, 1)
    banner = pystyle.Colorate.Vertical(pystyle.Colors.yellow_to_red, banner, 1)
    pystyle.System.Clear()
    print(pystyle.Add.Add(banner, text, 13))
    print()
    url = pystyle.Write.Input("Enter url -> ", pystyle.Colors.yellow_to_red, interval=0.0025)
    result_found = False
    for urls in base_urls:
        r = requests.get(urls + url)
        if r.status_code in [200, 201]:
            data = r.json()
            result = data.get("result") or data.get("destination")
            if result:
                print(result)
                result_found = True
                break
    if not result_found:
        print(pystyle.Colorate.Color(pystyle.Colors.red, "Impossible de bypass l'URL fournie."))
    pystyle.Write.Input("\nAppuyez sur Entrée pour continuer...", pystyle.Colors.yellow_to_red)
    main()
main()
