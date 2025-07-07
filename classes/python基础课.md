# Python基础课
# 第一部分： Python 入门
## 第一章： 认识 Python
### 1.1 什么是 Python？
Python 是一种*高级编程语言*，它由 Guido van Rossum 于 1991 年首次发布。Python 以其简洁和易读的语法而闻名，非常适合初学者。你可以用 Python 做很多事情，比如开发网站、数据分析、人工智能、自动化任务等等。总之，**如果你有一个问题，Python 可能就是解决问题的那把钥匙。**
### 1.2 编写第一个 Python 程序
我们来编写一个简单的 Python 程序，输出“Hello, World!”。

- 打开你的 IDE（如 VS Code）。
- 创建一个新文件，命名为 `hello.py`。
- 在文件中输入以下代码：
```python
print("Hello, World!")
```
保存文件并运行它，你应该会看到输出：
```
Hello, World!
```
### 1.3 注释和基本语法
#### 注释
注释是代码中的解释性文字，**Python 不会执行它们**。注释有助于你和其他人理解代码。**编写注释是非常有必要的。**

- 单行注释：使用 # 开头
```python
# 这是一个单行注释
print("Hello, World!")  # 这也是一个单行注释
```
- 多行注释：使用三个单引号或双引号
```python
'''
这是一个多行注释
可以有多行文字
'''
```
#### 基本语法（以下的内容不理解也没关系，后续的课程中会详细讲解）
- 变量：用来存储数据，可以是数字、字符串等。
```python
name = "Alice"
age = 25
```
- 数据类型：Python 有多种内置数据类型，如整数、浮点数、字符串、列表、字典等。
```python
integer_num = 10
float_num = 3.14
string_text = "Hello"
list_example = [1, 2, 3]
dict_example = {"name": "Alice", "age": 25}
```
- 条件语句：用来控制程序的执行流程。
```python
if age > 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```
- 循环：用来重复执行某些代码。
```python
for i in range(5):
    print(i)

while age < 30:
    print("Still young!")
    age += 1
```

### 1.4  必知常用函数

在开始编写复杂的 Python 程序之前，让我们先来认识一些像“打火石”一样的基本函数。它们简单易用，且编程过程中离不开这些简单的函数。

#### 1.4.1 `print()`： 打印输出

`print()` 函数就像它的名字一样简单直接，就是将内容打印到屏幕上。

**基本用法：**

```python
print("Hello, world!")  # 输出：Hello, world!
print(123)              # 输出：123
print(3.14)             # 输出：3.14
```

你可以在 `print()` 函数中放入各种类型的数据，包括字符串、数字等等。

**多个值输出：**

```python
name = "Alice"
age = 25
print("姓名:", name, "年龄:", age)  # 输出：姓名: Alice 年龄: 25
```

使用逗号 `,` 分隔多个值，`print()` 函数会将它们依次打印出来，并默认用空格隔开。

#### 1.4.2 `input()`： 获取用户输入

`input()` 函数用于获取用户从键盘输入的内容。

**基本用法：**

```python
name = input("请输入您的姓名：") 
print("您好，", name + "!")   # 使用 + 号连接字符串
```

这段代码会先提示用户输入姓名，然后将用户输入的内容存储到 `name` 变量中，最后打印出问候语。

**注意:**  `input()` 函数返回的值始终是 **字符串类型**，即使用户输入的是数字。

#### 1.4.3  `type()`： 查看数据类型

`type()` 函数用于查看数据所属的类型。

**示例：**

```python
name = "Alice"
age = 25
is_student = True

print(type(name))        # 输出：<class 'str'>，表示字符串类型
print(type(age))         # 输出：<class 'int'>，表示整数类型
print(type(is_student))  # 输出：<class 'bool'>，表示布尔类型
```

了解数据类型对于编写程序至关重要，因为它决定了你如何操作和处理这些数据。

恭喜你完成了 Python 入门的第一章！希望你对 Python 有了一个初步的了解，并对继续学习充满兴趣。接下来，我们将真正推开python的大门，一窥这门强大的编程语言。
## 第二章：数据类型与运算符

本章我们将学习 Python 中的基本数据类型、变量和赋值，以及常用的运算符。这些知识是学习 Python 的基础，也是编写程序必不可少的工具。

### 2.1 数据类型

Python 具有多种内建数据类型，可以分为数字、序列、集合、映射等几大类。下面是对部分基础的数据类型的介绍。

#### 2.1.1  数字 (Numbers)

数字类型表示数值数据，例如：

* **整数 (int):**  没有小数点的数字，例如：10, -5, 0

```python
age = 25
quantity = -10
```

* **浮点数 (float):**  带有小数点的数字，例如：3.14, -2.5, 0.0

```python
pi = 3.14159
temperature = -12.5
```

#### 2.1.2 字符串 (Strings)

字符串类型表示文本数据，用单引号 `''` 或双引号 `""` 包裹起来，例如：

```python
name = "Alice"
message = 'Hello, world!'
```

**字符串操作**

Python 提供了丰富的字符串操作方法，例如：

* **拼接:** 使用 `+` 运算符连接字符串。

```python
greeting = "Hello, " + name + "!"
print(greeting) # 输出: Hello, Alice!
```

* **重复:** 使用 `*` 运算符重复字符串。

```python
repeated_string = "abc" * 3
print(repeated_string) # 输出: abcabcabc
```

* **索引:** 使用方括号 `[]` 访问字符串中的单个字符，**索引从 0 开始**。

```python
first_letter = name[0]
print(first_letter)  # 输出: A
```

* **切片:** 使用 `[start:end:step]`  提取字符串的一部分。（参考4.1.3）

```python
substring = message[7:12]
print(substring)  # 输出: world
```

* **长度:** 使用 `len()` 函数获取字符串的长度。

```python
length = len(message)
print(length)  # 输出: 13
```

* **常用方法**:  Python 还提供了许多其他的字符串方法，例如：

    *   `.lower()`:  将字符串转换为小写。
    *   `.upper()`:  将字符串转换为大写。
    *   `.strip()`:  去除字符串开头和结尾的空格。
    *   `.replace(old, new)`:  将字符串中的旧字符串替换为新字符串。
    *   `.split(sep)`:  使用指定分隔符将字符串分割成列表。

**f-string（格式化字符串）** 是Python 3.6 引入的一种新的字符串格式化方法。它通过在字符串前加上 `f` 或 `F`，可以在字符串内部直接嵌入表达式，并以其值进行替换。**功能强大，用了的都说好**。

在 f-string 中，表达式需要被大括号 `{}` 包围，表达式会在运行时被求值并格式化为字符串。

```python
width = 10
height = 5
area = f"The area of the rectangle is {width * height} square units."
print(area)

import math
radius = 7
circumference = f"The circumference of the circle is {2 * math.pi * radius:.2f} units."
print(circumference)
```

输出：
```output
The area of the rectangle is 50 square units.
The circumference of the circle is 43.98 units.
```

**f-string 格式说明符**

**数值格式说明符**

1. **固定小数位数 (`.nf`)**

    `.nf`  将数值格式化为浮点数，并保留 `n` 位小数。

    ```python
    value = 3.14159
    formatted_value = f"{value:.2f}"
    print(formatted_value)  # 输出 3.14
    ```

2. **宽度和对齐 (`:[对齐方式][宽度].nf`)**

    `:10.2f`  将数字格式化为宽度为 10 的浮点数，并保留两位小数。默认右对齐。

    * `<`：左对齐
    * `>`：右对齐
    * `^`：居中对齐

    ```python
    value = 3.14159
    formatted_value = f"{value:10.2f}"   # 右对齐
    print(formatted_value)  # 输出       3.14

    formatted_value = f"{value:<10.2f}"  # 左对齐
    print(formatted_value)  # 输出 3.14      

    formatted_value = f"{value:^10.2f}"  # 居中对齐
    print(formatted_value)  # 输出   3.14   
    ```

3. 千位分隔符 (`,`)

    `,`  在数字中添加千位分隔符。

    ```python
    value = 1234567.89
    formatted_value = f"{value:,}"
    print(formatted_value)  # 输出 1,234,567.89
    ```

4. 百分比 (`.n%`)

    `.n%` 将数值格式化为百分比，并保留 `n` 位小数。

    ```python
    value = 0.1234
    formatted_value = f"{value:.2%}"
    print(formatted_value)  # 输出 12.34%
    ```

5. 指数计数法 (`.ne`)

    `.ne`  将数值格式化为指数计数法，并保留 `n` 位小数。

    ```python
    value = 1234567
    formatted_value = f"{value:.2e}"
    print(formatted_value)  # 输出 1.23e+06
    ```

**字符串格式说明符**

1. 对齐和宽度 (`: [对齐方式][宽度]`)

    * `<10` 表示左对齐，宽度为 10。
    * `>10` 表示右对齐，宽度为 10。
    * `^10` 表示居中对齐，宽度为 10。

    ```python
    text = "hello"
    print(f"{text:<10}")  # 输出 'hello     '
    print(f"{text:>10}")  # 输出 '     hello'
    print(f"{text:^10}")  # 输出 '  hello   '
    ```

2. 截断 (`.n`)

    `.n`  表示截断字符串，只显示前 `n` 个字符。

    ```python
    text = "hello world"
    print(f"{text:.5}")  # 输出 'hello'
    ```

#### 2.1.3 布尔值 (Booleans)

布尔值表示真假，只有两个值：`True` 和 `False`。

```python
is_active = True
is_deleted = False
```

布尔值通常用于条件语句和循环语句中，用于控制程序流程。

### 2.2 变量和赋值

变量是用来存储数据的容器。在 Python 中，可以使用 `=` 符号对变量进行赋值。

**示例：**

```python
# 将数字 10 赋值给变量 age
age = 10

# 将字符串 "Alice" 赋值给变量 name
name = "Alice"

# 将布尔值 True 赋值给变量 is_active
is_active = True
```

**注意：**

* 变量名必须以字母或下划线开头，后面可以跟字母、数字或下划线。
* 变量名区分大小写，`age` 和 `Age` 是不同的变量。

### 2.3 运算符

运算符用于对数据进行操作。常见的运算符包括：

**2.3.1 算术运算符**

| 运算符 | 描述 | 示例 | 结果 |
|---|---|---|---|
| + | 加法 | 10 + 5 | 15 |
| - | 减法 | 10 - 5 | 5 |
| * | 乘法 | 10 * 5 | 50 |
| / | 除法 | 10 / 5 | 2.0 |
| // | 整除 | 10 // 3 | 3 |
| % | 取余 | 10 % 3 | 1 |
| ** | 幂运算 | 2 ** 3 | 8 |

**2.3.2 比较运算符**

| 运算符 | 描述 | 示例 | 结果 |
|---|---|---|---|
| == | 等于 | 10 == 10 | True |
| != | 不等于 | 10 != 5 | True |
| > | 大于 | 10 > 5 | True |
| < | 小于 | 10 < 5 | False |
| >= | 大于等于 | 10 >= 10 | True |
| <= | 小于等于 | 10 <= 5 | False |

**2.3.3 逻辑运算符**

| 运算符 | 描述 | 示例 | 结果 |
|---|---|---|---|
| and | 逻辑与 | True and True | True |
| or | 逻辑或 | True or False | True |
| not | 逻辑非 | not True | False |

**示例：**

```python
# 算术运算
result = 10 + 5
print(result)  # 输出 15

# 比较运算
is_equal = 10 == 5
print(is_equal)  # 输出 False

# 逻辑运算
is_true = True and False
print(is_true)  # 输出 False
```

### 2.4 数据类型转换

有时需要将一种数据类型转换为另一种数据类型。可以使用内置函数进行类型转换。

| 函数 | 描述 | 示例 |
|---|---|---|
| int() | 转换为整数 | int("10") | 10 |
| float() | 转换为浮点数 | float("3.14") | 3.14 |
| str() | 转换为字符串 | str(10) | "10" |
| bool() | 转换为布尔值 | bool(0) | False |

**示例：**

```python
# 将字符串 "10" 转换为整数
integer_number = int("10")

# 将浮点数 3.14 转换为字符串
string_number = str(3.14)
```

### 2.5 输入和输出

* **输入：** 使用 `input()` 函数从用户获取输入。
* **输出：** 使用 `print()` 函数将数据输出到控制台。

**示例：**

```python
# 获取用户输入的姓名
name = input("请输入您的姓名：")

# 打印欢迎信息
print(f"您好，{name}！")
```

## 第三章：流程控制

本章将学习 Python 中的流程控制语句，包括条件语句和循环语句，以及一些控制语句。这些语句可以帮助我们控制程序的执行流程，让程序更灵活、更强大。

### 3.1 条件语句

条件语句用于根据条件判断执行不同的代码块。Python 中主要的条件语句是 `if-else` 语句。

**3.1.1 `if` 语句**

`if` 语句用于判断一个条件是否成立，如果成立则执行代码块。

**语法：**

```python
if 条件:
    代码块
```

**示例：**

```python
age = 18

if age >= 18:
    print("您已成年。")
```

**3.1.2 `if-else` 语句**

`if-else` 语句用于判断一个条件是否成立，如果成立则执行第一个代码块，否则执行第二个代码块。

**语法：**

```python
if 条件:
    代码块1
else:
    代码块2
```

**示例：**

```python
age = 15

if age >= 18:
    print("您已成年。")
else:
    print("您未成年。")
```

**3.1.3 嵌套条件语句**

在 `if` 或 `else` 代码块中还可以嵌套其他 `if-else` 语句，形成更复杂的判断逻辑。而 `elif` 则提供了一种更为简洁的方式来处理多条件判断，相当于是 `else if` 的缩写，避免了过多的嵌套，使得代码更加清晰易读。

**语法：**

```python
if 条件1:
    代码块1
    if 条件2:
        代码块2
else:
    代码块3
```

**示例：**

```python
score = 85

if score >= 90:
    print("优秀！")
elif score >= 80:
    print("良好！")
elif score >= 70:
    print("中等！")
else:
    print("不及格！")
```

### 3.2 循环语句

循环语句用于重复执行一段代码块。Python 中常用的循环语句有 `for` 循环和 `while` 循环。

**3.2.1 `for` 循环**

`for` 循环用于遍历一个可迭代对象，例如列表、元组、字符串等，并依次执行代码块。

**语法：**

```python
for 变量 in 可迭代对象:
    代码块
```

**示例：**

```python
# 遍历列表
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(f"Hello, {name}!")

# 遍历字符串
text = "Python"
for char in text:
    print(char)
```

**3.2.2 `while` 循环**

`while` 循环用于重复执行一段代码块，直到某个条件不满足为止。

**语法：**

```python
while 条件:
    代码块
```

**示例：**

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

### 3.3 循环控制语句

循环控制语句可以改变循环的执行流程。常用的循环控制语句有 `break` 和 `continue`。

**3.3.1 `break` 语句**

`break` 语句用于立即退出当前循环。

**示例：**

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

**3.3.2 `continue` 语句**

`continue` 语句用于跳过当前循环的剩余代码，继续执行下一轮循环。

**示例：**

```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

## 第四章： 列表与元组

本章将介绍 Python 中两种重要的数据结构：列表和元组。它们都是用来存储多个元素的容器，但有着不同的特点和应用场景。

### 4.1 列表(List)

列表是 Python 中最常用的数据结构之一，它是一个**有序**的**可变**序列，**可以存储不同类型的数据**。

#### 4.1.1 创建列表

可以使用方括号 `[]` 来创建列表，元素之间用 `,` 分隔。

```python
# 创建一个空列表
empty_list = []

# 创建一个包含整数的列表
numbers = [1, 2, 3, 4, 5]

# 创建一个包含字符串的列表
names = ["Alice", "Bob", "Charlie"]

# 创建一个包含不同类型元素的列表
mixed_list = [1, "Hello", 3.14, True]
```

#### 4.1.2 访问列表元素

可以使用 **索引(index)** 来访问列表中的元素，**索引从 0 开始。** 使用负索引从序列末尾开始访问元素，**负索引从 -1 开始。**

```python
# 访问列表的第一个元素
numbers[0] # 1

# 访问列表的最后一个元素
numbers[-1] # 5

#访问列表的第二个元素
names[1] # "Bob"
```

#### 4.1.3 切片(Slicing)

可以使用切片来访问列表的一部分元素。切片使用 `:` 分隔，语法为 `[start:end:stop]`， 其中 `start` 是起始索引，`end` 是结束索引 **（不包括该索引的元素）**。

```python
# 访问列表的第一个到第三个元素
numbers[0:3] # [1, 2, 3]

# 访问列表的第二个到最后一个元素
numbers[1:] # [2, 3, 4, 5]

# 访问列表的倒数第二个元素
numbers[-2] # 4

# 访问列表的奇数元素
numbers[::2] # [1, 3, 5]
```

#### 4.1.4 遍历列表

可以使用 `for` 循环里遍历列表中的每个元素。

```python
for name in names:
    print(name)
```

#### 4.1.5 修改列表元素

可以使用索引来修改列表中的元素。

```python
# 修改列表的第一个元素
numbers[0] = 10

# 修改列表的第三个元素
names[2] = "David"
```

#### 4.1.6 添加列表元素

- **`.append()` 方法：** 在列表末尾添加一个元素。
- **`.insert()` 方法：** 在指定位置添加一个元素。

```python
numbers.append(6) # 在列表末尾添加元素 6
names.insert(1, "Emily") # 在列表的第二个位置添加元素"Emily"
```

#### 4.1.7 删除列表元素

- **`del` 语句：** 删除指定位置的元素。
- **`.remove()` 方法：** 删除第一个出现的指定元素。
- **`.pop()` 方法：** 删除指定位置的元素**并返回该元素**。

```python
del numbers[2] # 删除列表的第三个元素
names.remove("Alice") # 删除列表中的第一个 "Alice" 元素
last_name = names.pop() # 删除列表的最后一个元素并将其赋值给变量 last_name
```

### 元组(Tuple)

元组与列表类似，也是用来存储多个元素的容器，但元组是不可变的，**一旦创建，就无法被修改**。

#### 4.2.1 创建元组

可以使用圆括号 `()` 来创建元组，元素之间用 `,` 分隔。

```python
# 创建一个空元组
empty_tuple = ()

# 创建一个包含整数的元组
numbers_tuple = (1, 2, 3, 4, 5, 6)

# 创建一个包含字符串的元组
names_tuple = ("Alice", "Bob", "Charlie")
```

#### 4.2.2 访问元组元素

与列表一样，可以使用索引来访问元组中的元素。

```python
# 访问元组的第一个元素
numbers[0] # 1

# 访问元组的最后一个元素
numbers[-1] # 6

#访问元组的第二个元素
names[1] # "Bob"
```

#### 4.2.3 切片(Slicing)

可以使用切片来访问元组的一部分元素，与列表的切片操作相同。

```python
# 访问元组的第一个到第三个元素
numbers[0:3] # (1, 2, 3)

# 访问元组的第二个到最后一个元素
numbers[1:] # (2, 3, 4, 5, 6)
```

#### 4.2.4 遍历元组

可以使用 `for` 循环来遍历元组中的每个元素。

```python
for name in names:
    print(name)
```

#### 4.2.5 不可变性

元组是**不可变的**，这意味着一旦创建，就无法修改其元素

```python
numbers_tuple[0] = 10 # 报错: TypeError: `Tuple` object does not support item assignment
```

### 4.3 列表和元组的常用方法
方法|描述|返回值|
----|----|------|
`len()`|返回列表或元组的长度|整数
`max()`|返回列表或元组中的最大元素|元素
`min()`|返回列表或元组中的最小元素|元素
`sum()`|返回列表中所有元素的和|元素
`.count()`|返回列表中指定元素出现的次数|整数
`.index()`|返回列表中第一个出现的指定元素的索引|整数
`.sort()`|对列表进行排序 *(原列表会被修改)*|None
`.reverse()`|对列表进行反转 *(原列表会被修改)*|None

```python
# 定义一个列表
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# 使用len()函数获取列表长度
list_length = len(numbers) # 8

# 使用max()函数获取列表中的最大元素
max_element = max(numbers) # 9

# 使用min()函数获取列表中的最小元素
min_element = min(numbers) # 1

# 使用sum()函数获取列表中所有元素的和
sum_elements = sum(numbers) # 31

# 使用count()函数获取列表中1出现的次数
count_1 = numbers.count(1) # 2

# 使用index()函数获取元素4第一次出现的索引
index_4 = numbers.index(4) # 2

# 使用sort()函数对列表进行排序
numbers.sort()

# 使用reverse()函数对列表进行反转
numbers.reverse()

# 定义一个元组
numbers_tuple = (3, 1, 4, 1, 5, 9, 2, 6)

# 元组使用len(), max(), min(), count(), index()方法的示例
tuple_length = len(numbers_tuple)
max_element_tuple = max(numbers_tuple)
min_element_tuple = min(numbers_tuple)
count_1_tuple = numbers_tuple.count(1)
index_4_tuple = numbers_tuple.index(4)
```

## 第五章： 函数

### 5.1 函数的定义和调用

想象一下，你有一个制作美味披萨的食谱。每次你想做披萨时，你都要重复一遍步骤：准备面团、添加酱料、铺上芝士，然后烤制。如果有一个按钮可以一键完成所有这些步骤，是不是很方便？**函数**就像这样的按钮，它可以让我们把重复的代码封装起来，方便重复使用。

**定义函数**

定义函数就像写一个新的食谱。它包含两部分：

1. **函数名**：就像食谱的名称，方便我们识别和调用。
2. **函数体**：包含我们需要执行的代码。

使用 `def` 关键字定义函数：

```python
def make_pizza():
    # 准备面团
    # 添加酱料
    # 铺上芝士
    # 烤制
    print("披萨已完成！")
```

**调用函数**

调用函数就像按下食谱按钮，执行函数体内的代码。

```python
make_pizza()  # 调用函数
```

输出结果：

```
披萨已完成！
```

**示例：**

```python
def say_hello():
    print("你好！")

def calculate_area(length, width):
    area = length * width
    print("面积为:", area)

say_hello()
calculate_area(5, 3)
```

输出结果：

```
你好！
面积为: 15
```

### 5.2 函数的参数和返回值

**参数**

就像烹饪食谱需要不同的食材一样，**函数也可以接受不同的参数**，这些参数可以影响函数的行为。

```python
def calculate_area(length, width):
    area = length * width
    print("面积为:", area)

calculate_area(5, 3)  # 传入参数
```

在调用 `calculate_area()` 函数时，我们传递了两个参数：`5` 和 `3`，分别代表长和宽。函数内部可以使用这些参数来计算面积。

**返回值**

函数还可以返回结果，就像食谱会告诉我们最终的成果是什么。

```python
def calculate_area(length, width):
    area = length * width
    return area  # 返回面积值

area = calculate_area(5, 3)
print("面积为:", area)
```

函数使用 `return` 关键字返回计算好的面积值，并将它赋值给变量 `area`。

**示例：**

```python
def convert_temperature(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit

celsius = 25
fahrenheit = convert_temperature(celsius)
print(celsius, "摄氏度等于", fahrenheit, "华氏度")
```

输出结果：

```
25 摄氏度等于 77.0 华氏度
```

### 5.3 递归函数

递归函数就像一个俄罗斯套娃，它自身调用自己。

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print("5 的阶乘为:", result)
```

在这个例子中，`factorial(5)` 会调用 `factorial(4)`，`factorial(4)` 又会调用 `factorial(3)`，直到 `factorial(0)` 返回 1，然后一层层返回最终结果。

**注意：** 递归函数必须有一个终止条件，否则会陷入无限循环。

**示例：**

```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i), end=" ")
```

输出结果：

```
0 1 1 2 3 5 8 13 21 34 
```

## 第六章： 模块

### 6.1 模块的概念和导入

**模块**可以被看作一个工具箱，里面包含各种工具（如函数、类、变量等），我们可以根据需要从工具箱中取出合适的工具来使用。*这是Python最强大的特性之一*，因为它拥有一个庞大且活跃的社区和生态系统。

在Python中，一个.py文件就是一个模块。模块可以包含各种功能，帮助我们组织代码，提高代码的可重用性和可维护性。

**导入模块**

使用 `import` 关键字导入模块：

```python
import 模块名
```

例如，导入 `math` 模块：

```python
import math
```

导入后，可以使用 `模块名.工具名` 的方式访问模块中的函数、变量或类：

```python
print(math.pi)  # 输出圆周率
print(math.sqrt(25))  # 计算平方根
```

**导入特定工具**

可以使用 `from 模块名 import 工具名` 导入特定的工具：

```python
from math import pi, sqrt

print(pi)
print(sqrt(25))
```

**自定义模块名称**

使用 `import 模块名 as 别名` 自定义模块名称：

```python
import math as m

print(m.pi)
```

### 6.2 内置模块

Python 自带一些内置模块，我们可以直接使用，无需额外安装。

#### 6.2.1 `math` 模块

`math` 模块提供了许多常用的数学函数，包括三角函数、对数函数、指数函数、幂函数等等。使用 `math` 模块可以简化数学计算，提高代码效率。

**导入 `math` 模块：**

```python
import math
```

**常用函数：**

* **三角函数:**
    * `math.sin(x)`: 计算正弦值。
    * `math.cos(x)`: 计算余弦值。
    * `math.tan(x)`: 计算正切值。
    * `math.asin(x)`: 计算反正弦值。
    * `math.acos(x)`: 计算反余弦值。
    * `math.atan(x)`: 计算反正切值。
    * `math.degrees(x)`: 将弧度转换为角度。
    * `math.radians(x)`: 将角度转换为弧度。

* **对数函数:**
    * `math.log(x, base)`: 计算以 `base` 为底的 `x` 的对数。
    * `math.log10(x)`: 计算以 10 为底的 `x` 的对数。
    * `math.log2(x)`: 计算以 2 为底的 `x` 的对数。

* **指数函数:**
    * `math.exp(x)`: 计算 `e` 的 `x` 次方。

* **幂函数:**
    * `math.pow(x, y)`: 计算 `x` 的 `y` 次方。

* **其他函数:**
    * `math.sqrt(x)`: 计算 `x` 的平方根。
    * `math.ceil(x)`: 返回大于或等于 `x` 的最小整数。
    * `math.floor(x)`: 返回小于或等于 `x` 的最大整数。
    * `math.fabs(x)`: 返回 `x` 的绝对值。
    * `math.pi`: 圆周率。
    * `math.e`: 自然常数。

**示例：**

```python
import math

# 计算 30 度角的正弦值
sin_value = math.sin(math.radians(30))
print("30 度角的正弦值为:", sin_value)

# 计算 10 的平方根
sqrt_value = math.sqrt(10)
print("10 的平方根为:", sqrt_value)

# 计算以 2 为底的 8 的对数
log_value = math.log2(8)
print("以 2 为底的 8 的对数为:", log_value)
```

**输出结果：**

```
30 度角的正弦值为: 0.5
10 的平方根为: 3.1622776601683795
以 2 为底的 8 的对数为: 3.0
```

通过使用 `math` 模块，我们可以轻松地完成各种数学计算，提高代码效率。

### 6.2.2 `random` 模块

`random` 模块提供了生成随机数和随机序列的功能。在许多应用场景中，我们都需要用到随机性，比如：

* **游戏开发：** 随机生成游戏角色属性、事件、道具等。
* **数据分析：** 随机抽样、模拟数据等。
* **密码学：** 生成随机密码、密钥等。

**导入 `random` 模块：**

```python
import random
```

**常用函数：**

* **`random.seed(seed)`:** 设置随机数种子。

* **`random.random()`:** 生成一个 **0 到 1 之间的随机浮点数**，包含 0 但不包含 1。

* **`random.uniform(a, b)`:** 生成一个 **a 到 b 之间的随机浮点数**，包含 a 和 b。

* **`random.randint(a, b)`:** 生成一个 **a 到 b 之间的随机整数**，包含 a 和 b。

* **`random.randrange(start, stop, step)`:**  从指定范围内以 `step` 为步长随机选择一个整数。如果省略 `step`，则默认步长为 1。

* **`random.choice(sequence)`:** 从序列（如列表、元组等）中随机选择一个元素。

* **`random.sample(sequence, k)`:** 从序列中随机选择 **k 个元素**，并返回一个新的列表。

* **`random.shuffle(sequence)`:**  随机打乱序列的元素顺序。

**示例：**

```python
import random

# 生成一个 0 到 1 之间的随机浮点数
random_float = random.random()
print("随机浮点数:", random_float)

# 生成一个 1 到 10 之间的随机整数
random_int = random.randint(1, 10)
print("随机整数:", random_int)

# 从列表中随机选择一个元素
fruits = ["苹果", "香蕉", "橘子"]
random_fruit = random.choice(fruits)
print("随机水果:", random_fruit)

# 从列表中随机选择 2 个元素
random_fruits = random.sample(fruits, 2)
print("随机选择的水果:", random_fruits)

# 打乱列表元素顺序
random.shuffle(fruits)
print("打乱后的水果列表:", fruits)
```

**输出结果：**

```
随机浮点数: 0.765432123456789
随机整数: 7
随机水果: 橘子
随机选择的水果: ['苹果', '香蕉']
打乱后的水果列表: ['香蕉', '橘子', '苹果']
```

### 6.3 创建自己的模块

我们可以将常用的代码封装成模块，方便在其他程序中使用。

**创建模块文件：**

```python
# my_module.py
def greet(name):
    print("Hello,", name)

def calculate_sum(a, b):
    return a + b
```

**导入模块：**

```python
import my_module

my_module.greet("Alice")
sum = my_module.calculate_sum(2, 3)
print(sum)
```

# 第三部分： 数据结构
## 第七章： 字典

### 7.1 字典（Dict）

**字典**是一种数据结构，它使用 **键值对** 存储数据。每个键值对包含一个**唯一的键** 和**与其关联的值**。字典可以帮助我们以一种更灵活、更直观的方式组织数据。

**定义字典**

使用花括号 `{}` 定义字典，键值对之间用冒号 `:` 分隔，多个键值对用逗号 `,` 分隔：

```python
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "北京"
}
```

**访问字典中的值**

使用方括号 `[]` 和键名访问对应值：

```python
print(my_dict["name"])  # 输出 Alice
```

**遍历字典**

可以使用 `for` 循环遍历字典中的键值对：

```python
for key, value in my_dict.items():
    print(key, ":", value)
```

**输出结果：**

```
name : Alice
age : 25
city : 北京
```

**添加键值对**

直接使用键名赋值即可添加新的键值对：

```python
my_dict["job"] = "程序员"
print(my_dict)
```

**输出结果：**

```
{'name': 'Alice', 'age': 25, 'city': '北京', 'job': '程序员'}
```

**修改键值对**

使用键名赋值修改对应值：

```python
my_dict["age"] = 26
print(my_dict)
```

**输出结果：**

```
{'name': 'Alice', 'age': 26, 'city': '北京', 'job': '程序员'}
```

**删除键值对**

使用 `del` 语句删除指定键值对：

```python
del my_dict["city"]
print(my_dict)
```

**输出结果：**

```
{'name': 'Alice', 'age': 26, 'job': '程序员'}
```

### 7.2 字典的常用方法

除了基本的定义、访问、添加、修改和删除操作，字典还提供了一些常用的方法：

* **`.get(key, default)`:** 获取指定键对应的值，如果键不存在，则返回默认值。

* **`.keys()`:** 返回字典所有键的列表。

* **`.values()`:** 返回字典所有值的列表。

* **`.items()`:** 返回字典所有键值对的列表。

* **`.clear()`:** 清空字典。

* **`.copy()`:** 创建字典的副本。

* **`.pop(key, default)`:** 删除指定键的键值对，并返回该键对应的值，如果键不存在，则返回默认值。

* **`.update(other_dict)`:** 将另一个字典的内容更新到当前字典中。

**示例：**

```python
my_dict = {"name": "Alice", "age": 25, "city": "北京"}

# 获取 "age" 对应的值
age = my_dict.get("age")
print("age:", age)

# 获取不存在的键 "country" 对应的值，默认值为 "未知"
country = my_dict.get("country", "未知")
print("country:", country)

# 获取所有键的列表
keys = my_dict.keys()
print("keys:", keys)

# 获取所有值的列表
values = my_dict.values()
print("values:", values)

# 获取所有键值对的列表
items = my_dict.items()
print("items:", items)
```

**输出结果：**

```
age: 25
country: 未知
keys: dict_keys(['name', 'age', 'city'])
values: dict_values(['Alice', 25, '北京'])
items: dict_items([('name', 'Alice'), ('age', 25), ('city', '北京')])
```

注：虽然 `dict.items()` 看起来像是复制了一遍字典的键值对，但实际上*它并没有创建字典的副本*，而是返回了一个**视图对象（view object）** 。这种视图对象是**动态**的，意味着如果在原字典上进行修改（如添加或删除键值对），这个视图对象也会实时反映这些变化。

## 第八章： 集合

### 8.1 集合（Set）

在 Python 中，**集合 (set)** 是一种无序且不重复的元素集合。想象一下，你有一袋不同颜色的弹珠，这就是一个集合。集合中的每个弹珠都是唯一的，并且没有特定的顺序。

#### 8.1.1 定义集合

使用花括号 `{}` 或 `set()` 函数定义集合：

```python
my_set = {1, 2, 3}
print(my_set)  # 输出：{1, 2, 3}

empty_set = set()  # 创建空集合
print(empty_set)  # 输出：set()
```

#### 8.1.2 集合元素

*   集合中的元素必须是 **不可变** 的类型，例如数字、字符串、元组。
*   集合会 **自动去除重复** 的元素。

```python
my_set = {1, 2, 2, 3}
print(my_set)  # 输出：{1, 2, 3}
```

#### 8.1.3 遍历集合

使用 `for` 循环遍历集合中的元素：

```python
my_set = {"apple", "banana", "orange"}
for fruit in my_set:
    print(fruit)
```

#### 8.1.4 添加元素

*   使用 `.add()` 方法添加单个元素：

```python
my_set.add("grape")
print(my_set)  # 输出：{'apple', 'banana', 'orange', 'grape'}
```

*   使用 `.update()` 方法添加多个元素：

```python
my_set.update(["kiwi", "mango"])
print(my_set)  # 输出：{'apple', 'kiwi', 'grape', 'mango', 'banana', 'orange'}
```

#### 8.1.5 删除元素

*   使用 `.remove()` 方法删除指定元素，如果元素不存在会报错：

```python
my_set.remove("banana")
print(my_set)  # 输出：{'apple', 'kiwi', 'grape', 'mango', 'orange'}
```

*   使用 `.discard()` 方法删除指定元素，如果元素不存在也不会报错：

```python
my_set.discard("watermelon")  # 不会报错，即使 "watermelon" 不在集合中
print(my_set)
```

### 8.2 集合的常用方法

*   `.union()` / `|`：返回两个集合的并集。
*   `.intersection()` / `&`：返回两个集合的交集。
*   `.difference()` / `-`：返回两个集合的差集。
*   `.issubset()` / `<=`：判断一个集合是否是另一个集合的子集。
*   `.issuperset()` / `>=`：判断一个集合是否是另一个集合的超集。
*   `.copy()`：复制一个集合。

方法示例：
```python
# 定义两个集合
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# 使用 union() 方法或 | 运算符获取并集
union_result = set1.union(set2)
union_result_operator = set1 | set2

# 使用 intersection() 方法或 & 运算符获取交集
intersection_result = set1.intersection(set2)
intersection_result_operator = set1 & set2

# 使用 difference() 方法或 - 运算符获取差集
difference_result = set1.difference(set2)
difference_result_operator = set1 - set2

# 使用 issubset() 方法或 <= 运算符判断子集
issubset_result = set1.issubset(set2)
issubset_result_operator = set1 <= set2

# 使用 issuperset() 方法或 >= 运算符判断超集
issuperset_result = set1.issuperset(set2)
issuperset_result_operator = set1 >= set2

# 使用 copy() 方法复制集合
copy_result = set1.copy()
```

### 8.3 集合的应用场景

*   **去重：**  快速去除列表或其他可迭代对象中的重复元素。
*   **成员测试：**  高效地检查一个元素是否存在于一个大型数据集中。
*   **数学运算：**  执行集合运算，例如并集、交集、差集等。

### 8.4 集合运算：并集、交集、差集

#### 8.4.1 并集

**并集**包含了*两个集合中的所有元素*，可以使用 `.union()` 方法或 `|` 运算符

#### 8.4.2 交集

**交集**包含了*两个集合中都存在的元素*，可以使用 `.intersection()` 方法或 `&` 运算符

#### 8.4.3 差集

**差集**包含了*在第一个集合中但不在第二个集合中的元素*，可以使用 `.difference()` 方法或 `-` 运算符，差运算是**非对称的**，即 `set_a - set_b` 与 `set_b - set_a` 结果不同。

#### 8.4.4 超集
**超集**是指*一个集合包含了另一个集合的所有元素*，同时前者可能还包含一些后者没有的元素。

换句话说，如果集合 A 的所有元素都在集合 B 中，则*集合 B 是集合 A 的超集*，写作 B ⊇ A（或者 A ⊆ B）。

如果 B 包含了 A 的所有元素，并且 B 还有其他元素，那么 B 是 A 的*真超集*，记作 B ⊃ A。

使用`.issuperset()` 方法或 `>=` 运算符判断一个集合是否是另一个集合的超集。

# 第四部分： 面向对象编程
## 第九章： 类和对象

### 9.1 类和对象的定义

在面向对象编程（OOP，*Object-Oriented Programming*）中，**类 (class)**  就好比是创建对象的蓝图或模板。它定义了对象的属性（数据）和方法（行为）。

**类就像汽车的设计图纸**，图纸上描述了汽车的各种特征，如品牌、型号、颜色、车轮数量等（属性），以及汽车可以执行的操作，如加速、刹车、转弯等（方法）。

**对象**则是一辆根据设计图纸生产出来的汽车，它*拥有图纸上定义的所有属性和方法*。

#### 9.1.1 定义类

在 Python 中，使用 `class` 关键字定义类：

```python
class Car:
    # 类属性
    wheels = 4

    # 构造方法
    def __init__(self, brand, model, color):
        # 实例属性
        self.brand = brand
        self.model = model
        self.color = color

    # 实例方法
    def accelerate(self):
        print(f"{self.brand} {self.model} 正在加速！")

    def brake(self):
        print(f"{self.brand} {self.model} 正在刹车！")
```

**代码解析:**

* `class Car:` 定义了一个名为 `Car` 的类。
* `wheels = 4` 是一个**类属性**，表示所有汽车都有 4 个轮子。
* `__init__` 是一个特殊的**构造方法**，用于创建对象时初始化实例属性。
    * `self` 参数表示当前对象实例。
    * `brand`、`model`、`color` 是实例属性。
* `accelerate()` 和 `brake()` 是**实例方法**，用于描述对象的行为。

### 9.2 属性和方法

#### 9.2.1 类属性

类属性属于类本身，*所有类的实例都共享相同的类属性值*。

#### 9.2.2 实例属性

实例属性属于类的每个实例，*每个实例可以有不同的属性值*。

#### 9.2.3 实例方法

实例方法是与类的实例相关联的函数，可以通过实例调用。**实例方法的第一个参数始终是 `self`**，表示当前对象实例。

### 9.3 实例化对象

**实例化** 就是根据类创建对象的过程。

```python
# 创建 Car 类的实例
my_car = Car("Toyota", "Camry", "Silver")
```

这行代码创建了一个名为 `my_car` 的 `Car` 类实例，并传递了品牌、型号和颜色参数给构造方法进行初始化。

**访问属性和调用方法：**

```python
# 访问实例属性
print(my_car.brand)  # 输出：Toyota
print(my_car.color)  # 输出：Silver

# 调用实例方法
my_car.accelerate()  # 输出：Toyota Camry 正在加速！
my_car.brake()  # 输出：Toyota Camry 正在刹车！
```

### 9.4 面向对象的基本概念

*   **封装:** 将数据和操作封装在一个单元（类）中，隐藏内部实现细节，*对外提供接口*。
*   **继承:**  创建一个新类（子类）从现有类（父类）*继承属性和方法*，并可以添加新的属性和方法。
*   **多态:**  不同类型的对象可以响应相同的函数调用，*但表现出不同的行为*。

## 第十章：深入类和对象

在上一章中，我们学习了类和对象的基本概念。本章将深入探讨类的更多细节，包括构造方法、实例方法、类方法、静态方法以及特殊方法。

### 10.1 构造方法（`__init__`）

**构造方法** 是类的一个特殊方法，用于在创建对象时初始化实例属性。它在实例化对象时自动调用。

* 构造方法的名称固定为 `__init__`。
* 第一个参数始终是 `self`，表示当前对象实例。
* 其他参数用于接收初始化实例属性的值。

**示例:**

```python
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

# 创建 Dog 对象时，自动调用 __init__ 方法进行初始化
my_dog = Dog("Buddy", "Labrador", 3) 
print(my_dog.name)  # 输出: Buddy
```

### 10.2 实例方法和类方法

#### 10.2.1 实例方法

**实例方法** 是与类的实例相关联的方法。它们可以访问和修改实例属性。

* 实例方法的第一个参数始终是 `self`，表示当前对象实例。

**示例:**

```python
class Dog:
    # ... (其他代码)

    def bark(self):
        print(f"{self.name} 说：汪汪！")

my_dog = Dog("Buddy", "Labrador", 3)
my_dog.bark()  # 输出: Buddy 说：汪汪！
```

#### 10.2.2 类方法

**类方法** 是与类本身相关联的方法。可以访问和修改类属性^9.2.1^，但*不能访问实例属性*。

* 类方法使用 `@classmethod` 装饰器定义。
* 第一个参数是 `cls`，表示当前类本身。

*注：在Python中，**装饰器（decorator）是一种特殊的函数**，通过将一个函数传递给装饰器并返回一个新的函数，可以在不改变原函数代码的情况下添加功能。*

**示例:**

```python
class MyClass:
    class_variable = 0

    def __init__(self, value):
        self.instance_variable = value

    @classmethod
    def class_method(cls, value):
        cls.class_variable += value
        print(f"Class variable is now {cls.class_variable}")

# 创建实例
obj1 = MyClass(10)
obj2 = MyClass(20)

# 调用类方法
MyClass.class_method(5)  # 输出: Class variable is now 5
obj1.class_method(10)    # 输出: Class variable is now 15
```

### 10.3 静态方法

**静态方法**  与类或实例都没有绑定关系。它们不能访问实例属性或类属性。

* 静态方法使用 `@staticmethod` 装饰器定义。
* 静态方法不需要 `self` 或 `cls` 参数。

**示例:**

```python
class Dog:
    # ... (其他代码)

    @staticmethod
    def is_valid_age(age):
        return 0 <= age <= 20

print(Dog.is_valid_age(15))  # 输出: True
```

### 10.4 特殊方法

**特殊方法**也称为**魔术方法**，以双下划线 `__` 开始和结束。它们用于定义类的特殊行为，例如字符串表示形式、长度、迭代等。

#### 10.4.1  <code>\_\_str__</code> 方法

`__str__` 方法用于返回对象的字符串表示形式。当使用 `print()` 函数打印对象或使用 `str()` 函数将对象转换为字符串时，会自动调用此方法。

**示例:**

```python
class Dog:
    # ... (其他代码)

    def __str__(self):
        return f"名字: {self.name}, 品种: {self.breed}, 年龄: {self.age}"

my_dog = Dog("Buddy", "Labrador", 3)
print(my_dog)  # 输出: 名字: Buddy, 品种: Labrador, 年龄: 3
```

#### 10.4.2   <code>\_\_len__</code> 方法

`__len__` 方法用于返回对象的长度。当使用 `len()` 函数获取对象的长度时，会自动调用此方法。

**示例:**

```python
class Dog:
    # ... (其他代码)

    def __len__(self):
        return self.age

my_dog = Dog("Buddy", "Labrador", 3)
print(len(my_dog))  # 输出: 3
```

## 第十一章： 继承和多态

继承和多态是面向对象编程（OOP）的两个重要支柱，*它们使得代码更具可重用性和可扩展性*。

### 11.1 继承的概念和语法

**继承** 就像现实生活中子女继承父母的基因一样，在编程中，它允许我们创建一个新类（子类）基于现有类（父类），继承父类的属性和方法。子类可以添加新的属性和方法，也可以修改或重写父类的属性和方法。

**语法：**

```python
class 子类名(父类名):
    # 子类代码块
```

*   `子类名`：要创建的新类的名称。
*   `父类名`：要继承的现有类的名称。

### 11.2 子类和父类

*   **父类（Superclass）** 也称为基类或超类，是被继承的类。
*   **子类（Subclass）** 也称为派生类，是从父类继承而来的类。

### 11.3 多态性

**多态** 意味着 "多种形态"，在 OOP 中，它表示不同类型的对象可以响应相同的函数调用，但表现出不同的行为。

**示例：**

```python
class Animal:  # 父类
    def speak(self):
        print("动物发出声音")

class Dog(Animal):  # 子类
    def speak(self):
        print("汪汪！")

class Cat(Animal):  # 子类
    def speak(self):
        print("喵喵！")

# 创建不同类型的对象
animal = Animal()
dog = Dog()
cat = Cat()

# 调用相同的方法，表现出不同的行为
animal.speak()  # 输出: 动物发出声音
dog.speak()     # 输出: 汪汪！
cat.speak()     # 输出: 喵喵！
```

在这个例子中，`Animal`、`Dog` 和 `Cat` 类都有一个 `speak()` 方法，但它们的实现不同。当我们调用不同对象的 `speak()` 方法时，会根据对象的实际类型执行相应的代码，这就是多态性。

### 11.4 方法重写

**方法重写**  是指子类重新定义父类中已有的方法，以改变方法的行为。

**示例：**

```python
class Animal:
    def move(self):
        print("动物在移动")

class Fish(Animal):
    def move(self):
        print("鱼在游泳")

# 创建 Fish 对象
my_fish = Fish()

# 调用 move() 方法，会执行子类重写后的方法
my_fish.move()  # 输出: 鱼在游泳
```


# 第五部分： 文件操作与异常处理
## 第十二章： 文件操作

在编程中，我们经常需要与文件进行交互，例如读取数据、写入数据、修改文件等。本章将介绍 Python 中的文件操作。

### 12.1 文件的打开和关闭

在 Python 中，使用 `open()` 函数打开文件，并返回一个文件对象。

**语法：**

```python
file_object = open(file_path, mode)
```

*   **`file_path`:** 文件的路径，可以是相对路径或绝对路径。
*   **`mode`:**  打开文件的模式，例如读取模式 (`"r"`)、写入模式 (`"w"`)、追加模式 (`"a"`) 等。

**文件打开模式:**

| 模式 | 描述                                                         |
| :--- | :----------------------------------------------------------- |
| `'r'` | 读取模式（默认）。如果文件不存在，则抛出 `FileNotFoundError` 异常。 |
| `'w'` | 写入模式。如果文件存在，则清空文件内容；如果文件不存在，则创建新文件。 |
| `'a'` | 追加模式。如果文件存在，则将内容追加到文件末尾；如果文件不存在，则创建新文件。 |
| `'x'` | 创建模式。如果文件已存在，则抛出 `FileExistsError` 异常。 |
| `'b'` | 二进制模式，用于读取或写入二进制文件（例如图片、音频等）。      |
| `'t'` | 文本模式（默认），用于读取或写入文本文件。                  |
| `'+'` | 更新模式，允许同时进行读写操作。                          |

**示例：**

```python
# 以读取模式打开文件
file = open("my_file.txt", "r")

# 以写入模式打开文件，如果文件不存在则创建
file = open("new_file.txt", "w") 

# 以追加模式打开文件
file = open("my_file.txt", "a")
```

**关闭文件**

使用完文件后，务必使用 `close()` 方法关闭文件，以释放资源。

```python
file.close()
```

### 12.2 文件的读写操作

#### 12.2.1 读取文件

*   **`read()`:** 读取文件全部内容。

```python
file = open("my_file.txt", "r")
content = file.read()
print(content)
file.close()
```

*   **`readline()`:** 读取一行内容。

```python
file = open("my_file.txt", "r")
line = file.readline()
print(line)  # 输出第一行内容
file.close()
```

*   **`readlines()`:**  读取所有行，并返回一个列表，每行内容作为列表的一个元素。

```python
file = open("my_file.txt", "r")
lines = file.readlines()
print(lines)  # 输出所有行内容的列表
file.close()
```

#### 12.2.2 写入文件

*   **`write()`:** 将字符串写入文件。

```python
file = open("my_file.txt", "w")
file.write("Hello, world!\n")
file.close()
```

*   **`writelines()`:**  将字符串列表写入文件。

```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
file = open("my_file.txt", "w")
file.writelines(lines)
file.close()
```

### 12.3 文件的路径和模式

*   **文件路径** 指示文件在计算机中的位置。可以使用相对路径或绝对路径。

    *   **相对路径：**  相对于当前工作目录的路径。
    *   **绝对路径：**  从根目录开始的完整路径。

*   **文件模式**  指定如何打开文件，例如读取模式、写入模式等^12.1^。

### 12.4 文件操作的常用方法

*   **`.tell()`:**  返回文件指针的当前位置。
*   **`.seek(offset, whence)`:**  移动文件指针到指定位置。
*   **`.flush()`:**  将缓冲区中的数据写入文件。

### 12.5  `with` 语句

为了避免忘记关闭文件，可以使用 `with` 语句自动管理文件资源。

```python
with open("my_file.txt", "r") as file:
    content = file.read()
    print(content)

# 文件在 with 语句块结束后自动关闭
```
## 第十三章： 异常处理

在编写程序时，我们无法预料所有可能发生的情况，例如用户输入错误的数据、文件不存在、网络连接中断等等。这些意外情况被称为**异常 (Exception)**。如果不处理异常，程序就会崩溃中断。本章将介绍 Python 中的异常处理机制。

### 13.1 异常的概念和分类

**异常** 是指程序运行过程中发生的错误或意外情况，它会干扰程序的正常流程。

Python 中的异常有很多种类型，例如：

* **`ZeroDivisionError`**: 除以零时引发。
* **`TypeError`**: 对不兼容的数据类型执行操作时引发。
* **`ValueError`**:  当函数接收到类型正确但值不合适时引发。
* **`FileNotFoundError`**:  打开不存在的文件时引发。
* **`IndexError`**:  访问列表中不存在的索引时引发。
* **`KeyError`**: 访问字典中不存在的键时引发。

### 13.2 捕获异常：`try-except-else-finally`

为了处理异常，我们可以使用 `try-except` 语句块来捕获和处理异常。

**语法：**

```python
try:
    # 可能引发异常的代码块
except 异常类型1:
    # 处理异常类型1的代码块
except 异常类型2:
    # 处理异常类型2的代码块
else:
    # 如果 try 块中没有异常发生，则执行此代码块
finally:
    # 无论是否发生异常，都会执行此代码块
```

*   **`try` 块：**  包含可能引发异常的代码。
*   **`except` 块：**  捕获并处理指定类型的异常。可以有多个 `except` 块。
*   **`else` 块：**  如果 `try` 块中没有异常发生，则执行此代码块。
*   **`finally` 块：**  无论是否发生异常，都会执行此代码块，通常用于释放资源（例如关闭文件、关闭数据库连接等）。

**示例：**

```python
try:
    num1 = int(input("请输入第一个数字："))
    num2 = int(input("请输入第二个数字："))
    result = num1 / num2
except ZeroDivisionError:
    print("错误：除数不能为零！")
except ValueError:
    print("错误：请输入有效的数字！")
else:
    print("结果：", result)
finally:
    print("程序结束。")
```

**代码解析:**

1.  程序首先尝试执行 `try` 块中的代码，即获取用户输入的两个数字并进行除法运算。
2.  如果用户输入的第二个数字为 0，则会引发 `ZeroDivisionError` 异常，程序会跳转到 `except ZeroDivisionError:` 块，并输出错误信息。
3.  如果用户输入的不是有效的数字，则会引发 `ValueError` 异常，程序会跳转到 `except ValueError:` 块，并输出错误信息。
4.  如果 `try` 块中没有发生异常，则会执行 `else` 块，输出计算结果。
5.  无论是否发生异常，`finally` 块中的代码都会被执行，用于输出程序结束信息。

### 13.3 抛出异常：`raise`

可以使用 `raise` 语句手动抛出异常。

**语法：**

```python
raise 异常类型("可选的错误信息")
```

**示例：**

```python
def check_age(age):
    if age < 0:
        raise ValueError("年龄不能为负数！")
    elif age > 120:
        raise ValueError("年龄不合法！")
    else:
        print("年龄有效。")

try:
    user_age = int(input("请输入您的年龄："))
    check_age(user_age)
except ValueError as e:
    print("错误：", e)
```

### 13.4 自定义异常

除了内置异常类型，我们还可以创建自定义异常类型，用于表示程序中特定的错误情况。

**创建自定义异常类：**

```python
class MyCustomError(Exception):
    pass
```

**使用自定义异常：**

```python
def my_function(value):
    if value < 0:
        raise MyCustomError("值不能为负数！")

try:
    my_function(-1)
except MyCustomError as e:
    print("发生自定义异常：", e)
```

# 结语
## 第十四章： 结语
恭喜你，你已经完成了这门 Python 基础课程，迈出了成为一名 Python 程序员的第一步。

回顾这段学习旅程，你已经掌握了 Python 的基本语法、数据类型、控制流程、函数、模块等核心概念，也学会了如何使用字典、集合来组织数据，用类和对象构建更复杂的程序，还能处理文件和异常。这些知识就像积木一样，为你今后搭建更宏伟的 Python 工程奠定了坚实的基础。

然而，这仅仅是一个开始。这个世界广阔而深邃，还有许多宝藏等待你去探索。保持你的好奇心和求知欲，不断学习和实践，你将不断突破自己的编程技能，创造出更多令人惊叹的作品。

记住，**学习编程最好的方式就是动手实践。** 永远也不要害怕犯错，每一次错误都是宝贵的学习机会。

我们有缘再会。