from curses.ascii import isalpha


class CaesarCoder:
    

    def Coder(message_in, key, lang):
        if lang=='rus':
            ord_first=ord('а')
            ord_last = ord('я')
        else:
            ord_first=ord('a')
            ord_last = ord('z')
        new_str=""
        for i in message_in.lower():
            if i.isalpha():
                new_str+=chr((ord(i)%ord_first+key)%(ord_last - ord_first+1) + ord_first)
            else: 
                new_str+=i
                continue
        return new_str
    
    def Decoder(message_in, key, lang):
        if lang=='rus':
            ord_first=ord('а')
            ord_last = ord('я')
        else:
            ord_first=ord('a')
            ord_last = ord('z')
        new_str=""
        for i in message_in.lower():
            if i.isalpha():
                new_str+=chr((ord(i)%ord_first-key)%(ord_last - ord_first + 1) + ord_first)
            else: 
                new_str+=i
                continue
        return new_str
