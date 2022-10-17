# python_linux_hw2

Вторая домашка, Григорян Михаил ФТиАД-22

Программа, возвращающая значение выражения, используя алгоритм сортировочной станции и обратную польскую запись

Принимает на вход строку с выражением и опционально флаг, чтобы вернуть выражение в обратной польской записи перед ответом 

Пример вызова:

python3 rpn_calculator.py "-2 + 2 - 3 * (1 + 4) + 1000" - возвращает только значение выражения

python3 rpn_calculator.py "-2.1 * 3.5 + 3 / 2 + 4 - 3 + (2 + 3) * 5" -rpn - возращает обратную польскую запись выражения и значение выражения

Можно вызвать через командную строку следующим образом: 

- Выдает ошибку, если в строке есть другие символы, кроме цифр, точки, операторов и скобок
- Выдает ошибку при делении на ноль
- реализована возможность использовать в выражении унарный минус
- можно вводить дробные числа
