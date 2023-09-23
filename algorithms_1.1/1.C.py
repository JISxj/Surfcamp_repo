number = "".join([x if x in "1234567890" else "" for x in input()])

if len(number) <= 8:
    code = "495"
    num = number
else:
    code = number[1:4]
    num = number[4:]



for i in range(3):
    _number = "".join([x if x in "1234567890" else "" for x in input()])
    if len(_number) <= 8:
        _code = "495"
        _num = _number
    else:
        _code = _number[1:4]
        _num = _number[4:]
    if _num == num and _code == code:
        print("YES", end=" ")
    else:
        print("NO", end=" ")