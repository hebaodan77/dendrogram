# Dendrogram - Python 树状图生成器

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/)
[![WTFPL](http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-1.png)](http://www.wtfpl.net/)

将嵌套的字典/列表结构可视化为树形图的轻量级工具，支持自定义符号和自动优化布局。

```plaintext
┣━ project:JSON Test Data
┣━ version:1.0
┣━ isActive:True
┣━ tags
┃  ┣━ [0] test
┃  ┣━ [1] json
┃  ┗━ [2] data
┗━ author
   ┣━ name:Test User
   ┣━ email:test@example.com
   ┣━ age:30
   ┗━ isAdmin:False
```

## 要求
   - Python 3.6 或更高版本, 代码含有 f-string 特性

## 功能特性

- 🌳 **多类型支持**：自动识别字典、列表及其嵌套结构
- ✨ **智能布局**：自动清理冗余连接线（`mod()`方法）
- 🎨 **可定制符号**：支持修改分支/树干显示符号
- 📦 **零依赖**：仅需标准库，开箱即用

## 快速开始

### 基础用法
```python
from dendrogram import Dendrogram

data = {
    "name": "Alice",
    "skills": ["Python", "Git"],
    "contact": {"email": "alice@example.com"}
}

d = Dendrogram()
d.tree(data)
print(d)
```

### 输出效果
```plaintext
┣━ name:Alice
┣━ skills
┃  ┣━ [0] Python
┃  ┗━ [1] Git
┗━ contact
   ┗━ email:alice@example.com
```

## 高级配置

### 自定义符号
```python
custom = Dendrogram(
    branch="├── ",  # 分支符号
    tail="└── ",    # 末尾符号
    bone="│   "     # 树干符号
)
```

### 方法说明
| 方法        | 参数               | 描述                          |
|-------------|--------------------|-----------------------------|
| `tree()`    | obj, distance=0    | 递归生成树状图                 |
| `mod()`     | -                  | 优化显示布局（自动调用）         |

## 应用场景

1. **调试复杂JSON结构**
2. **配置文件可视化**
3. **教学演示数据结构**
4. **日志层级分析**

## 贡献指南

欢迎提交 Issue 或 PR！请确保：
- 代码符合 PEP 8 规范
- 补充对应单元测试
- 更新文档说明

## 许可证
本项目作为公共资源发布，遵循 [WTFPL 许可证](LICENSE)。  
您可以在遵守许可证条款的前提下自由使用、修改和分发代码。

本项目采用 **WTFPL** 许可证。  
你可以：
- 乱用 ✅
- 乱改 ✅
- 闭源 ✅
- 商用 ✅
- 不署名 ✅
