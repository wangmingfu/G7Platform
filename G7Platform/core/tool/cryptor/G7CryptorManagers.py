#-*- coding: utf-8
__author__ = 'yuyang'

from G7Platform.G7Globals import *
from G7Platform.profile.settings.G7Settings import *
from G7Platform.core.tool.Cryptor.G7Cryptor import *

cryptor_types = {
    "base64":"0",
    "des":"2",
    "xxtea":"3",
    "aes":"4",
    "rsa":"5",
    "md5":"6",
}

class BMCryptorType:

    base64 = "base64"
    des = "des"
    xxtea = "xxtea"
    aes = "aes"
    rsa = "rsa"
    md5 = "md5"

    @property
    def cryptorPrefix(self, cryptorType):
        if cryptorType in list(cryptor_types.keys()):
            return cryptor_types[cryptorType]
        else:
            return "0"

class BMCryptorManager:

    password = ""

    # 单例
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_inst'):
            cls._inst=super(BMCryptorManager,cls).__new__(cls,*args,**kwargs)
        return cls._inst

    def __init__(self):
        self.password = desPassword

    def md5PasswordEncrypt(self, text):
        # (text.md5+String(reverse(text)).md5).md5.md5.md5
        strmk0 = md5Encrypt(text)
        textList = list(text)
        textList.reverse()
        strmk1 = md5Encrypt("".join(textList))
        zero = md5Encrypt(strmk0+strmk1)
        first = md5Encrypt(zero)
        second = md5Encrypt(first)
        return second
    
    def desBase64_B64EncodeText(self, b64Text):

        if len(b64Text) > 0:
            desEncodeText = desEncode(base64Decode(b64Text), self.password)
            return desEncodeText
        else:
            return ""

    def desBase64_B64DecodeText(self, b64Text):

        if len(b64Text) > 0:
            desDecodeText = desDecode(base64Decode(b64Text), self.password)
            return desDecodeText
        else:
            return ""

    #des 混�?? base64???解�??  �?text�???? �?base64�????
    def desBase64_TextEncodeB64(self, text):

        if len(text) > 0:
            desEncodeText = desEncode(text, self.password)
            return base64Encode(desEncodeText)
        else:
            return ""

    def desBase64_TextDecodeB64(self, text):

        if len(text) > 0:
            desDecodeText = desDecode(text, self.password)
            return base64Encode(desDecodeText)
        else:
            return ""

    def desBase64_B64EncodeB64(self, b64Text):

        if len(b64Text) > 0:
            desEncodeText = desEncode(base64Decode(b64Text), self.password)
            return base64Encode(desEncodeText)
        else:
            return ""

    def desBase64_B64DecodeB64(self, b64Text):

        if len(b64Text) > 0:
            desDecodeText = desDecode(base64Decode(b64Text), self.password)
            return base64Encode(desDecodeText)
        else:
            return ""

    def getB64DecryptText(self, text):

        if type(text) == type(b''):
            cryptor_type = str(text[:1])[1:-1]
        else:
            cryptor_type = text[:1]

        cryptor_text = text[1:]
        decryptBytes = base64Decode(cryptor_text)
        if cryptor_type == "0":
            decryptBytes = base64Decode(cryptor_text)
        elif cryptor_type == "2":
            decryptBytes = self.desBase64_B64DecodeText(cryptor_text)
        elif cryptor_type == "3":
            decryptBytes = self.desBase64_B64DecodeText(cryptor_text)
        elif cryptor_type == "4":
            decryptBytes = self.desBase64_B64DecodeText(cryptor_text)
        elif cryptor_type == "5":
            decryptBytes = self.desBase64_B64DecodeText(cryptor_text)
        elif cryptor_type == "6":
            decryptBytes = self.desBase64_B64DecodeText(cryptor_text)
        else:
            decryptBytes = b''

        return self.bytesToString(decryptBytes)

    def getTextEncryptB64(self, text, cryptror_type):

        if cryptror_type not in cryptor_types.keys():
            return ""

        prefix = cryptor_types[cryptror_type]
        encryptBytes = bytes(prefix,"utf-8")+base64Encode(text)
        if cryptror_type == BMCryptorType.base64:
            encryptBytes = bytes(prefix,"utf-8")+base64Encode(text)
        elif cryptror_type == BMCryptorType.des:
            encryptBytes = bytes(prefix,"utf-8")+self.desBase64_TextEncodeB64(text)
        elif cryptror_type == BMCryptorType.xxtea:
            encryptBytes = bytes(prefix,"utf-8")+self.desBase64_TextEncodeB64(text)
        elif cryptror_type == BMCryptorType.aes:
            encryptBytes = bytes(prefix,"utf-8")+self.desBase64_TextEncodeB64(text)
        elif cryptror_type == BMCryptorType.rsa:
            encryptBytes = bytes(prefix,"utf-8")+self.desBase64_TextEncodeB64(text)
        elif cryptror_type == BMCryptorType.md5:
            encryptBytes = bytes(prefix,"utf-8")+self.desBase64_TextEncodeB64(text)
        else:
            encryptBytes = b''

        return self.bytesToString(encryptBytes)

    def bytesToString(self, bytesString):
        return bytesString.decode("utf-8")
