# updating the file

from typing import Union

def calc(num1: Union[float, int], num2: Union[float, int], operator: str) -> Union[float, int]:
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2
    if operator == "/":
        return num1 / num2

