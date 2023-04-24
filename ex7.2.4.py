def seven_boom(end_number):
    result = []
    for i in range(end_number+1):
        if i % 7 == 0 or '7' in str(i):
            result.append('BOOM')
        else:
            result.append(i)
    return result


print(seven_boom(17))