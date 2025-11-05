# utils.py - 工具函数模块

class Calculator:
    """计算器类"""
    
    @staticmethod
    def add(a, b):
        """加法运算"""
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """减法运算"""
        return a - b
    
    @staticmethod
    def multiply(a, b):
        """乘法运算"""
        return a * b

def check_even_odd(number):
    """检查奇偶性"""
    return "偶数" if number % 2 == 0 else "奇数"

def get_factorial(n):
    """计算阶乘"""
    if n == 0:
        return 1
    else:
        return n * get_factorial(n-1)

def greet_user(name):
    """问候用户函数"""
    return f"欢迎 {name} 使用测试项目！"