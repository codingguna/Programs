import random

def calc_rel_fre(lst):
    freq={}
    total=len(lst)
    for item in lst:
        freq[item]=freq.get(item,0)+1
    for item,count in freq.items():
        freq[item]=count/total
    return freq
def calc_cumu_prob(prob):
    cum_prob={}
    cum=0.0
    for symbol,pro in prob.items():
        cum_prob[symbol]=(cum,cum+pro)
        cum+=pro
    return cum_prob
def encode_seq(data,cum_prob):
    low=0.0
    high=1.0
    ranges=[]
    for symbol in data:
        rang_=high-low
        high=low +rang_*cum_prob[symbol][1]
        low=low+rang_*cum_prob[symbol][0]
        ranges.append((low,high))
    key=random.uniform(ranges[-1][0],ranges[-1][1])
    return key,ranges
def decode_val(encoded_val,length,cum_prob):
    decoded_data=[]
    low=0.0
    high=1.0
    for _ in range(length):
        range_=high-low
        code=(encoded_val-low)/range_
        for symbol,(sym_low,sym_high) in cum_prob.items():
            if sym_low<=code<sym_high:
                decoded_data.append(symbol)
                high=low+range_*sym_high
                low=low+range_*sym_low
                break
    return decoded_data

data=list(map(int,input("enetr the sequence of image value : ").split(" ")))

probab=calc_rel_fre(data)
print(f'probability of gray levels : \n {probab}')

cum_prob=calc_cumu_prob(probab)
print(f"cumulative probability :\n {cum_prob}")

encoded_value,ranges=encode_seq(data,cum_prob)

print(f'Encoded value: {encoded_value}\n')
print(f'ranges : {ranges}')

decoded_data=decode_val(encoded_value,len(data),cum_prob)

for i,symbol in enumerate(data):
    range_=cum_prob[symbol]
    print(f"range for '{symbol}': {range_}")
print(f'decoded sequence: {decoded_data}')

