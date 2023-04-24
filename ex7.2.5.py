def sequence_del(my_str):
    return ''.join(c for i, c in enumerate(my_str) if c != my_str[i-1] or i == 0)


print(sequence_del("ppyyyyythhhhhooonnnnn"))
print(sequence_del("SSSSsssshhhh"))
print(sequence_del("Heeyyy   yyouuuu!!!"))