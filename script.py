import Langdetect

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
        
        return resultados


texto = 'Tenta todas as 26 possíveis chaves de deslocamento e exibe os Amem.'
mesagem = Cifra()
texto_cifrado = mesagem.cifra_cesar(texto)
print('Texto cifrado:', texto_cifrado)
print(mesagem.decifrador_deslocamento(texto_cifrado))
forca_bruta = mesagem.decifrador_forca_bruta(texto_cifrado)

