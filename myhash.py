from hashlib import *
import base64
######################

class Myhash:
    def __init__(self,type,):
        self.type = type
        pass



###################

    def hash1 (self,choose):
        if choose =="encode":

            word_encode = base64.b64encode(str(self).encode("UTF-8")).decode()
            return word_encode
        elif choose == "decode":

            word_decode = base64.b64decode(str(self)).decode("ascii")
            return word_decode
        else :
            print ("Error")


    def hash2 (self,choose):
        if choose =="encode":

            word_encode = base64.b16encode(str(self).encode("UTF-8")).decode()
            return word_encode
        elif choose == "decode":

            word_decode = base64.b16decode(str(self)).decode("ascii")
            return word_decode
        else :
            print ("Error")



    def hash3 (self,choose):

        if choose =="encode":

            word_encode = base64.b32encode(str(self).encode("UTF-8")).decode()
            return word_encode
        elif choose == "decode":

            word_decode = base64.b32decode(str(self)).decode("ascii")
            return word_decode
        else :
            print ("Error")



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


    def hard(self,choose):
        if choose == "encode":
             r1 = Myhash.hash1(str(self),"encode")
             r2 = Myhash.hash2(str(r1),"encode")
             r3 = Myhash.hash3(str(r2),"encode")

             return r3
        elif choose == "decode":
             r1 = Myhash.hash3(str(self),"decode")
             r2 = Myhash.hash2(str(r1),"decode")
             r3 = Myhash.hash1(str(r2),"decode")
             return r3

        else :

            return "Erorr"


    def hard2(self,choose):
        if choose == "encode":
            r1 = Myhash.hash1(str(self), "encode")
            r2 = Myhash.hash2(str(r1), "encode")
            r3 = Myhash.hash3(str(r2), "encode")
            r4 = Myhash.hard(str(r3),"encode")
            return r4
        elif choose == "decode":
            r1 = Myhash.hash3(str(self), "decode")
            r2 = Myhash.hash2(str(r1), "decode")
            r3 = Myhash.hash1(str(r2), "decode")
            r4 = Myhash.hard(str(r3), "decode")
            return r4

        else:

            return "Erorr"








