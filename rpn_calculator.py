import re
import argparse


class rpn_calculator:
    def __init__(self, expression):
        # объявим операторы - это стандартные + - * / и скобки
        self.ops = {
            "+": (lambda a, b: a + b),
            "-": (lambda a, b: a - b),
            "*": (lambda a, b: a * b),
            "/": (lambda a, b: a / b),
            "(": "(",
            ")": "("
        }
        self.expression = expression
        # заменим числа с унарным минусом типа -d на (0 - d)
        self.right_expression = re.sub(
            r"-(\d+\.?\d*)", "(0 - \\1)", self.expression
        )


    def is_expression_correct(self):
        condition = len(re.findall(
            r"[^0-9.+/*()-]", ''.join(
                self.right_expression.split()
            )))
        if condition > 0:
            raise ValueError("В записи выражения могут присутствовать только числа, скобки () и операторы - + / *")
        pass

    def from_infix_to_rpn(self) -> str:
        self.is_expression_correct()
        # приоритет операций
        priority = {"+": 1, "-": 1, "*": 2, "/": 2, "(": -1, ")": 0}
        temp = []
        rpn_expression = ""
        # алгоритм сортировочной станции
        for i in self.right_expression:
            if i in self.ops:
                if i == "(":
                    temp.append(i)
                else:
                    while temp and priority[temp[-1]] >= priority[i]:
                        rpn_expression += ' ' + temp.pop()
                    if i == ')':
                        temp.pop()
                    else:
                        temp.append(i)
            else:
                rpn_expression += i
        while temp:
            rpn_expression += ' ' + temp.pop()
        return rpn_expression

    def eval_rpn(self) -> float:
        # переводим выражение в обратную польскую запись
        rpn = self.from_infix_to_rpn()
        # токенизируем с помощью регулярных выражений
        tokens = re.findall(
            r"[-+/*()]|[+-]?(?:(?:\d*\.\d+)|(?:\d+\.?))(?:[Ee][+-]?\d+)?", rpn
        )
        stack = []
        # валидируем
        for token in tokens:
            if token in self.ops:
                arg2 = stack.pop()
                arg1 = stack.pop()
                if token == "/" and arg2 == 0:
                    raise ZeroDivisionError(
                        "Ты пытаешься делить на ноль. Не делай так, пожалуйста (」°ロ°)」"
                    )
                else:
                    result = self.ops[token](arg1, arg2)
                stack.append(result)
            else:
                stack.append(float(token))
        result = stack.pop()
        # если число вида d.0 то вернем просто d
        if result % 1 == 0:
            result = int(result)
        return result


# ну и далее просто считываем аргументы и считаем все
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("expression", help = "expression in infix form", type = str)
    parser.add_argument("-rpn", "--reverse_polish_notation",
                        help = "flag is to return expression in reverse polish notation",
                        action = "store_true")
    args = parser.parse_args()
    p = rpn_calculator(args.expression)
    if args.reverse_polish_notation:
        print(p.from_infix_to_rpn())
    print(p.eval_rpn())


