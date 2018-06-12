import winsound as ws

encoder={'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--',
      'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..',
      'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--',
      'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.' ,'s':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
      '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', ' ':' ',
      '.':'.-.-.-', ',':'--..--', '?':'..--..'}

decoder={'.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e', '..-.':'f', '--.':'g', '....':'h', '..':'i', '.---':'j', '-.-':'k', '.-..':'l', '--':'m',
      '-.':'n', '---':'o', '.--.':'p', '--.-':'q', '.-.':'r', '...':'s', '-':'t', '..-':'u', '...-':'v', '.--':'w', '-..-':'x', '-.--':'y', '--..':'z',
      '-----':'0', '.----':'1', '..---':'2', '...--':'3', '....-':'4', '.....':'5', '-....':'6', '--...':'7', '---..':'8', '----.':'9', ' ':' ',
      '.-.-.-':'.', '--..--':',', '..--..':'?'}

def _dit_beep():
    ws.Beep(1750, 300)

def _dah_beep():
    ws.Beep(1750, 900)

def _space_beep():
    ws.Beep(37, 1800)

def _encode():
    print("!!Start your speaker before you enter your string!!")

    estrin=input("Enter string to be encoded: ")

    estrout=[]

    for p in range(len(estrin)):
        estrout.append(encoder[estrin[p]])

    for i in estrout:
        if i is ' ':
            _space_beep()
            print(i, end="")
        else:
            for j in i:
                print(j, end="")
                if j is '.':
                    _dit_beep()
                elif j is '-':
                    _dah_beep()
            print(' ', end="")
            ws.Beep(37, 900)

def _decode():
    print("Enter morse code:")
    dstrin=input()
    dlist=[]
    dmidstr=[]
    for g in range(len(dstrin)):
        str=''
        if dstrin[g]==' ':
            if dstrin[g-1]==' ':
                dlist.append(' ')
            else:
                dlist.append(str.join(dmidstr))
                dmidstr=[]
        else:
            dmidstr.append(dstrin[g])
        if g is len(dstrin)-1:
            dlist.append(str.join(dmidstr))
    dstrout=[]
    print(dlist)
    for k in dlist:
        dstrout.append(decoder[k])
    for i in dstrout:
        print(i, end="")
    
if __name__=="__main__":
    choice=int(input("Enter 1 to encode and play, 2 to decode: "))
    if choice==1:
        _encode()
    elif choice==2:
        _decode()
        
