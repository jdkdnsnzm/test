# main.py - 更新主程序集成功能
import utils
import config

def main():
    print(f"=== {config.PROJECT_NAME} ===")
    print(f"版本: {config.VERSION}")
    print(f"作者: {config.AUTHOR}")
    print("=" * 30)
    
    # 使用工具函数
    calc = utils.Calculator()
    print("计算功能演示:")
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 × 5 = {calc.multiply(10, 5)}")
    
    # 使用其他函数
    print(f"\n数字10是: {utils.check_even_odd(10)}")
    print(f"5的阶乘是: {utils.get_factorial(5)}")
    
    # 用户问候
    name = "测试用户"
    print(f"\n{utils.greet_user(name)}")
    
    print("\n项目功能集成完成！")

if __name__ == "__main__":
    main()