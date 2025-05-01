class Dendrogram:
    """
    树状图生成器，用于将字典或列表结构可视化输出为树形结构
    支持嵌套字典和列表的混合结构
    """
    
    def __init__(self):
        # 树状图绘制符号常量
        self.branch = '┣━ '  # 分支符号
        self.tail = '┗━ '    # 末尾分支符号
        self.bone = '┃  '     # 树干符号
        self.warehouse = []   # 存储生成的树状图行
        
    def tree(self, obj: dict or list, distance=0):
        """
        递归生成树状图
        :param obj: 要处理的对象(字典或列表)
        :param distance: 当前递归深度(控制缩进)
        """
        is_dict = isinstance(obj, dict)  # 判断对象类型
        obj_length = len(obj) - 1       # 计算对象长度(用于判断最后一个元素)
        
        # 统一化处理:将字典和列表转换为可迭代的键值对
        iter_obj = obj.items() if is_dict else obj
        
        for i, item in enumerate(iter_obj):
            # 生成当前深度的树干部分[零件1:树干]
            detail = self.bone * distance
            
            # 判断是否为当前层级的最后一个元素
            is_last = (i == obj_length)
            # 生成分支前缀[零件1 -> 零件2:分枝]
            front = detail + (self.tail if is_last else self.branch)
            
            # 统一化处理键值对
            key, value = item if is_dict else (i, item)
            
            # [零件2 -> 零件3:叶子or分枝]
            if isinstance(value, (dict, list)):
                # 处理嵌套结构
                key_prefix = f'{front}{key}' if is_dict else f'{front}[{key}]'
                self.warehouse.append(key_prefix)
                self.tree(value, distance + 1)  # 递归处理
            else:
                # 处理叶子节点
                key_value = f'{front}{key}:{value}' if is_dict else f'{front}[{key}] {value}'
                self.warehouse.append(key_value)
    
    def mod(self):
        """
        优化树状图显示效果，清理多余的树干符号
        采用后处理方式，避免在递归过程中频繁修改
        """
        len_warehouse = len(self.warehouse)
        
        # 找出所有末尾分支的位置
        site = ((x, line.find('┗')) 
               for x, line in enumerate(self.warehouse) 
               if '┗' in line)
        
        # 预计算每行的树干长度
        branch_len = [i.rfind('┃') for i in self.warehouse]
        
        # 清理多余的树干符号
        for x, y in site:
            for cx in range(x + 1, len_warehouse):
                if branch_len[cx] >= y:
                    # 替换多余的树干符号为空格
                    self.warehouse[cx] = (f'{self.warehouse[cx][:y]} '
                                        f'{self.warehouse[cx][y + 1:]}')
                else:
                    break
    
    def __str__(self):
        """
        输出最终的树状图字符串
        :return: 格式化后的树状图字符串
        """
        self.mod()  # 先优化显示效果
        return '\n'.join(self.warehouse)



# 使用示例
if __name__ == "__main__":
    true = True
    false = False
    null = None
    
    test_data = {
    "project": "JSON Test Data",
    "version": 1.0,
    "isActive": true,
    "tags": ["test", "json", "data"],
    "author": {
        "name": "Test User",
        "email": "test@example.com",
        "age": 30,
        "isAdmin": false
    },
    "settings": {
        "debugMode": true,
        "maxConnections": 5,
        "timeout": null
    },
    "testCases": [
        {
            "id": 1,
            "description": "Successful login",
            "expectedResult": "Welcome page"
        },
        {
            "id": 2,
            "description": "Invalid login",
            "expectedResult": "Error message"
        }
    ],
    "metadata": {
        "createdAt": "2023-05-15T10:00:00Z",
        "lastUpdated": "2023-05-16T15:30:00Z"
    }
}

    d = Dendrogram()
    d.tree(test_data)
    print(d)
