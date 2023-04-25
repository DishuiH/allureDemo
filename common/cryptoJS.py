# -*- coding: utf-8 -*-
# @Time : 2022/11/18 14:14
# @Author : Shawn Xiao
# @FileName: cryptoJS.py
# @Software: PyCharm
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import base64


class AesCrypt:
    def __init__(self, __key):
        self.key = __key.encode('utf8')
        self.mode = AES.MODE_ECB  # 模式可以更改为MODE_CBC需要添加vi待研究

        # 生成加密器，参数密匙和模式,ECB需要偏移量
        self.cryptor = AES.new(self.key, self.mode)

    @staticmethod
    def add_to_16(text):
        pad = 16 - len(text.encode('utf-8')) % 16
        text = text + pad * chr(pad)
        return text.encode('utf-8')

    def encrypt(self, text, base=16):
        """  加密方法
        :param text: 需要加密的文本
        :param base:  需要加密的类型
        :return:加密完的字符串
        """
        # 预处理,填充明文为16的倍数
        text = self.add_to_16(text)

        # 加密,输出bytes类型
        cipher_text = self.cryptor.encrypt(text)
        if base == 16:
            # 返回16进制密文
            return b2a_hex(cipher_text).decode('utf-8')
        elif base == 64:
            # 返回base64密文
            return base64.b64encode(cipher_text).decode('utf-8')

    def decrypt(self, ciphertext, base=16):
        if base == 16:
            # 解密16进制密文
            text = a2b_hex(ciphertext)
        elif base == 64:
            # 解密base64密文
            text = base64.b64decode(ciphertext)  # base64解码
        else:
            raise Exception('不支持的编码')
        utf8_text = self.cryptor.decrypt(text).decode('utf8')
        return utf8_text[0:-ord(utf8_text[-1])]


if __name__ == '__main__':
    key = 'd5fdec7c7746261f'
    txt = '123456'
    ase = AesCrypt(key)
    print(ase.encrypt(txt))

    print(ase.decrypt('6e670907d658b6d35167cd2b41f3a565'))
