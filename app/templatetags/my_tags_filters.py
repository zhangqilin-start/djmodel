from django import template
register = template.Library() #register的名字是固定的

@register.filter()
def multi_filter(x, y):
    return x*y
# 一个函数加上装饰器register.filter就变成了一个自定义的过滤器,上述过滤器实现的是两个数的相乘
# 自定义的过滤器要在模板语法中使用
# 自定义过滤器的局限性:第一个是形参是被修饰的变量,第二个形参是过滤器的参数:过滤器最多只能放两个参数
# 自定义过滤器的优势:进行逻辑判断时,只能用过滤器

# 自定义标签
@register.simple_tag
def multi_tag(x,y):
    return x*y
# 自定义标签无参数个数限制
