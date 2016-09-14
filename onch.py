import config

class onch:

    '''
      "onch" means 'open mouth,close heart.
    '''

    def encode(self, codes):
        before_encode = []
        after_encode = ''

        before_encode.extend(codes)
        dict = config.code_dict

        for each_latter in before_encode:
            if each_latter in dict:
                after_encode = after_encode + dict[each_latter]
                continue
            after_encode = after_encode + each_latter

        return(after_encode)

    def decode(self, codes):
        code_dict = config.code_dict
        decodes = ''
        before_decode = []
        before_decode.extend(codes)

        for each_latter in before_decode:
            for each_item in code_dict:
                if code_dict[each_item] == each_latter:
                    decodes = decodes + each_item
                    break

        return(decodes)



if __name__ == '__main__':
    omch = onch()
    after_encode = ''
    after_decode = ''
    after_encode = omch.encode('i am not alone any more,but much lonelier than ever.')
    print(after_encode.capitalize())
    print('------------------Encode end here------------------')
    after_decode = omch.decode(after_encode)
    print(after_decode.capitalize())
    print('------------------Decode end here------------------')