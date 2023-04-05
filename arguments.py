def year_of_birth(name,age):
    year = 2023 -age
    print(f"Hello {name},you were born in {year}")

def my_country(country="Kenya"):
    print(f"Hello you are from {country}")

def hello(*names):
    for name in names:
        print(f"hello {name}")

def sum(*nums):
    answer=0
    for num in nums:
        answer += num
    return answer

def concatenate_args(*strngs):
    answer=""
    for strng in strngs:
        answer += strng
    return answer

def concatenate_kwargs(**kwargs):
    answer=""
    for text in kwargs.values():
        answer += text
    return answer

def multiply_many(**kwargs):
    answer=1
    for num in kwargs.value():
        answer *= num
    return answer
