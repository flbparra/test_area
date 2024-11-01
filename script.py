import time
from collections import Counter
class Cifra():
    
    def __init__(self):
        self._texto = ''
        self._k = 3
        
    @property
    def texto(self):
        return f'Ultimo texto traduzido:\n{self._texto}'
    
    @texto.setter
    def texto(self, texto_atual):
        self._texto = texto_atual
    
    @property
    def k(self):
        return self._k
    
    @k.setter
    def k(self, novo_k):
        self._k = novo_k 
    
    def cifra_cesar(self, texto):
        result = ''
        for char in texto:
            
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                new_char = chr((ord(char) - base + self.k) % 26 + base)
                result+= new_char
            else:
                result += char
        
        return result
    
    def decifrador_deslocamento(self, texto, k=3):
        
            self.k = k
            txt_decifrado = ''
            
            for char in texto:
                if char.isalpha():
                    base = ord('A') if char.isupper() else ord('a')
                    txt_decifrado += chr((ord(char)-base - self.k) % 26 + base)
                else:
                    txt_decifrado += char
            return txt_decifrado
    
    def decifrador_forca_bruta(self, texto):
        
        resultados = {}
        
        for k in range(1, 26):
            texto_decifrado = self.decifrador_deslocamento(texto, k)
            resultados[k] = texto_decifrado
            print(f'K: {k} \nMesagem: {texto_decifrado}')
        
        return resultados
    
    def decifrador_por_frequencia(self, texto):
        
        """Metodo declara, freq tirada do site que a professora passou, depois conta e faz a frequencia do texto encripitado
        - ordena os caracteres do texto pela frequencia"""
        
        freq = {
        'a': 13.9, 'b': 1.0, 'c': 4.4, 'd': 5.4, 'e': 12.2,
        'f': 1.0, 'g': 1.2, 'h': 0.8, 'i': 6.9, 'j': 0.4,
        'k': 0.1, 'l': 2.8, 'm': 4.2, 'n': 5.3, 'o': 10.8,
        'p': 2.9, 'q': 0.9, 'r': 6.9, 's': 7.9, 't': 4.9,
        'u': 4.0, 'v': 1.3, 'w': 0.0, 'x': 0.3, 'y': 0.0, 'z': 0.4
    }
        contador_txt = Counter(texto)
        total_char_txt = sum(contador_txt.values())
        freq_txt = {char: (cont / total_char_txt) * 100 for char, cont in contador_txt.items()}
        
        chars_order_pt = sorted(freq, key=freq.get, reverse=True)
        chars_order_enc = sorted(freq_txt, key=freq_txt.get, reverse=True)\
        
        
        substituicao = {}
        
        for index, char_encriptado in enumerate(chars_order_enc):
            if index < len(chars_order_pt):
                substituicao[char_encriptado] = chars_order_pt[index]
        
        texto_descriptado = ''.join(substituicao.get(char, char) for char in texto)
        
        return texto_descriptado, texto_cifrado
        


texto = 'O Brasil e um pais tropical, conhecido por suas belas praias, sua rica biodiversidade e sua cultura vibrante. A Amazonia, maior floresta tropical do mundo, abriga uma imensa variedade de especies de plantas e animais, muitas das quais nao sao encontradas em nenhum outro lugar do planeta. A capital do pais, Brasilia, foi projetada pelo famoso arquiteto Oscar Niemeyer e e um simbolo da arquitetura moderna. Alem disso, o Brasil e conhecido por sua musica, como a bossa nova e o samba, e por eventos como o Carnaval, que atrai milhares de turistas todos os anos.'
mesagem = Cifra()
texto_cifrado = mesagem.cifra_cesar(texto)



print('Texto cifrado:', texto_cifrado)
print(mesagem.decifrador_deslocamento(texto_cifrado))
forca_bruta = mesagem.decifrador_forca_bruta(texto_cifrado)

print(mesagem.decifrador_por_frequencia(texto_cifrado))

