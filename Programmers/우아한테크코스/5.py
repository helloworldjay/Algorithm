def solution(penter, pexit, pescape, data):
    packeted_data = "" # data after packet
    for i in range(len(data)//len(penter)):
        data_let = data[i*len(penter):(i+1)*len(penter)] # split data by penter size
        if data_let == penter or data_let == pexit or data_let == pescape: # condition for adding pescape
            packeted_data += pescape + data_let
        else : packeted_data += data_let
    return penter + packeted_data + pexit

print(solution("1100",	"0010",	"1001",	"1101100100101111001111000000"))

print("110011011001100110010010111100111001110000000010" == "110011011001100110010010111100111001110000000010" )