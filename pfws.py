from math import sqrt
from typing import List, Dict
from primePy import primes
import os

letters : Dict[str, str] = {"a": "0'0'0'0", "b": "0'0'0'1", "c": "0'0'1'0", "d": "0'0'0'2", "e": "0'0'1'(1)", 
                            "f": "0'0'1'1", "g": "0'1'(1'0)", "h": "0'0'0'3", "i": "0'0'2'0", "j": "0'1'0'1", 
                            "k": "0'0'1'(2)", "l": "0'0'1'2", "m": "0'1'(1'(1))", "n": "0'1'(1)'1", "o": "0'1'1'0",
                            "p": "0'0'0'4", "q": "0'1'(1'1)", "r": "0'0'2'1", "s": "1'(1'(1'0))", "t": "0'1'0'2", 
                            "u": "1'0'1'0", "v": "1'(1'0)'1", "w": "0'0'1'(3)", "x": "0'0'1'3", "y": "0'2'0'0", 
                            "z": "0'1'(2)'1"}

inv_letters : Dict[str, str] = {v: k for k, v in letters.items()}

def pfns(num : int) -> str:
    if num == 1: return "0"
    if num == 0: return "()"
    
    ps : List[int] = primes.upto(num)
    ps.reverse()
    fs : List[int] = primes.factors(num)
    final : str = ""
    p : int
    for p in ps:
        count = 0
        while p in fs:
            count += 1
            fs.remove(p)
        final += f"{count}'"
    final = final[:-1]
    curr : str = final[0]
    while curr == "0" or curr == "'": 
        final = final[1:]
        curr = final[0]
    return simplify_pfns(final)

def anns(num : str) -> int:
    if num == "0": return 1
    if num == "()": return 0

    fs = num.split("'")
    ps = primes.first(len(fs))
    ps.reverse()
    total : int = 1
    i : int
    for i in range(len(fs)):
        total *= pow(ps[i], int(fs[i]))

    return total

def simplify_pfns(m : str) -> str:
    temp : str = ""
    final : str = ""
    curr : str
    for curr in m:
        if curr == "'" or curr == "0": temp += curr
        else:
            amount = len(temp) // 2
            if amount > 1:
                new = simplify_pfns(pfns(amount))
                final += f"'({new})'"
            else: 
                final += temp
            temp = ""
            #if (not curr.isalpha() and not curr.isnumeric()) and final[-1] == "'": final = final[:-1]
            final += curr
    if len(temp) > 0:
        amount = (len(temp)) // 2
        if amount > 1:
            new = simplify_pfns(pfns(amount))
            final += f"'({new})"
        else: final += temp

    return final

def desimplify_pfns(m : str) -> int:
    final : str = ""
    layer : int = 0
    i : int = 0
    #print(m)
    while i != len(m):
        if m[i] == "(":
            layer += 1
            start : int = i
            while layer != 0:
                i += 1
                if m[i] == "(": layer += 1
                elif m[i] == ")": layer -= 1
            count : int = desimplify_pfns(m[start + 1 : i])
            final += "0"
            for _ in range(count - 1): final += "'0"
        else:
            final += m[i]
        i += 1
    #print(final)
    return anns(final)

def pfws(m : str) -> str:
    final : str = ""
    prev : str = " "
    while m != "":
        if m[0].isnumeric():
            if prev.isalpha(): final += "'"
            num : int = 0
            while m[0].isnumeric():
                num *= 10
                num += int(m[0])
                prev = m[0]
                m = m[1:]
                if len(m) == 0: break
            final += f"{pfns(num)}'"
        elif m[0].isalpha(): 
            if not prev.isalpha(): final += "'"
            final += f"{letters[m[0]]}'"
            prev = m[0]
            m = m[1:]
        else: 
            if m[0] == " ": final += "[]'"
            else: final += f"{m[0]}'"
            prev = m[0]
            m = m[1:]      

    if final[-1] == "'": final = final[:-1]
    return final

def anws(m : str) -> str:
    final : str = ""
    strlen : int = len(m) + 2
    m = f"  {m}  "
    letter : bool = False
    i : int = 2

    while i < strlen:
        if m[i:i + 2] == "[]":
            letter = False
            final += " "
            i += 2
        elif m[i:i + 2] == "()":
            letter = False
            final += "0"
            i += 2
        elif m[i] != "'" and not m[i].isnumeric():
            letter = False
            final += m[i]
            i += 1
        elif m[i] == "'":
            primes : int = 1 if final != "" else 2
            while m[i + 1] == "'": 
                primes += 1
                i += 1
            if primes > 2: letter = False
            if primes % 2 == 0: letter = not letter
            final += "'" * ((primes - (0 if i == strlen - 1 else 1)) // 2)
            i += 1
        elif letter:
            temp : str = ""
            layer : int = 0 
            chars : int = 0
            while chars != 4 or layer != 0: 
                if m[i] == "(": layer += 1
                elif m[i] == ")": layer -= 1
                elif m[i].isnumeric(): chars += 1
                temp += m[i]
                i += 1
            final += inv_letters[temp]
        else:
            temp : str = ""
            while ((m[i : i + 2] != "''") 
                   and not (m[i] == "'" 
                            and not m[i + 1].isnumeric() 
                            and not m[i + 2].isnumeric()) 
                   and i < strlen):
                temp += m[i]
                i += 1
            final += str(desimplify_pfns(temp))

    return final

def simplify_pfws(m : str) -> str:
    temp : str = ""
    final : str = ""
    prev : str = " "
    curr : str
    for curr in m:
        if (curr == "'" and prev == "0") or curr == "0": temp += curr
        else:
            amount = len(temp) // 2
            if amount > 1:
                new = pfns(amount)
                final += f"[{new}]'"
            else: final += temp
            temp = ""
            #print(final, "-", curr)
            final += curr
        prev = curr

    if len(temp) > 0:
        amount = (len(temp) + 1) // 2
        if amount > 1:
            new = pfns(amount)
            final += f"[{new}]"
        else: final += temp

    return final

def desimplify_pfws(m : str) -> str:
    final : str = ""
    strlen : int = len(m) + 1
    m = f" {m} "
    layer : int = 0
    i : int = 1
    while i != strlen:
        if m[i] == "[" and m[i + 1].isnumeric():
            layer += 1
            start : int = i
            while layer != 0:
                i += 1
                if m[i] == "[": layer += 1
                elif m[i] == "]": layer -= 1
            count : int = desimplify_pfns(m[start + 1 : i])
            final += "0"
            for _ in range(count - 1): final += "'0"
        else:
            final += m[i]
        i += 1
    
    return final   

def convert() -> None:
    os.system('cls')
    n : str = input("(anws -> pfws)\n\nprompt: ").lower()
    m : str = pfws(n)
    print(f"\nraw pfws:        {m}")
    p = simplify_pfws(m)
    print(f"\nsimplified pfws: {p}")
    input("\n\npress enter...")

def translate() -> None:
    os.system('cls')
    n : str = input("(pfws -> anws)\n\nprompt: ").lower()
    m : str = desimplify_pfws(n)
    print(f"\nraw pfws: {m}")
    p : str = anws(m)
    print(f"\nanws:     {p}")
    input("\n\npress enter...")


def main() -> None:
    on : bool = True
    while on:
        os.system('cls')
        print("1. anws -> pfws\n2. pfws -> anws\n3. leave\n")
        opt : str = input("> choose (1 - 3): ")
        match opt:
            case "1":
                convert()
            case "2":
                translate()
            case "3":
                break
            case _:
                pass

main()