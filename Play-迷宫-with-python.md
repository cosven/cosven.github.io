title: Play 迷宫 with python and pygame
date: 2015-06-27 09:56:59
tags: [python, algorithm]
categories: 算法
---

这篇笔记主要包含两个大的部分。**迷宫自动生成** 和 **迷宫寻路**

**迷宫自动生成** 包含了......算法

**迷宫寻路** 包含了......算法

[项目工程代码](/attachment/maze.zip)

<!--more-->

## 迷宫自动生成

**生成的迷宫将会满足什么条件 ?**
从迷宫的任意一点出发，可以达到迷宫另外的任意一点。

### 使用类似深度优先算法生成迷宫

> `深度优先算法` 是什么？是搜索算法的一种。是沿着树的深度遍历树的节点，尽可能深的搜索树的分支。当节点v的所在边都己被探寻过，搜索将回溯到发现节点v的那条边的起始节点。这一过程一直进行到已发现从源节点可达的所有节点为止。如果还存在未被发现的节点，则选择其中一个作为源节点并重复以上过程，整个进程反复进行直到所有节点都被访问为止。属于盲目搜索。
深度优先搜索是图论中的经典算法，利用深度优先搜索算法可以产生目标图的相应拓扑排序表，利用拓扑排序表可以方便的解决很多相关的图论问题，如最大路径问题等等。

#### 算法目标

让图上所有的点都互相连通（一开始所有的点都都被强 隔开）

#### 算法过程

- 用一个数组来保存已经互相连通的点，对于已经连通的点，我们对它进行 **标记**，并用 *connected\_points* 来保存。
也就是说，当所有的点都被标记完了，我们的算法就结束。

- 用一个数组来保存未被标记的点，初始的时候，所有的点都未被标记。我们用
*unconnected\_points* 来表示。

- 另外还需要创建 一个栈。*dfs\_visited\_pointes\_stack*

1. 随机选择一个点作为起点，把起点设置为 **当前格** 并进行 **标记**
2. 当还存在未被标记的点时，也就是 *unconnected\_points* 不为空的时候。
    1. 当 **当前格** 有未被标记的邻格 （四邻格模式）
        1. 随机选择一个 **未被标记** 的邻格
        2. 将 **当前格** 入栈
        3. 移除 **当前格** 与 邻格之间的墙
        4. **标记** 邻格，并将它设为 **当前格**

    2. （**当前格** 已经没有未被 **标记** 邻格了），判断栈是否为空，如果不为空
        1. 栈顶得格子出栈，并让它成为**当前格**
        2. 跳到上面的循环

    3. （栈空了，**当前格** 已经没有未被 **标记** 邻格了）
        1. 随机从 *unconnected\_points* 中选择一个格子设为 **当前格**
        2. 跳到上面的循环

3. *unconnected\_points*为空，算法结束

#### 关键算法代码

后面可运行的整体工程代码

```python
def generate_dfs(self, current_person):
    """dfs 生成迷宫核心算法
    """
    self.connected_persons.append(current_person)
    self.unconnected_persons.remove(current_person)
    current_person.is_connected = True

    while len(self.unconnected_persons) > 0:    # 当还有未被访问的点
        self.mark_neighbor_to_no(current_person)
        while len(self.visited_stack) > 0:
            current_person = self.visited_stack.pop()
            self.mark_neighbor_to_no(current_person)
        count = len(self.unconnected_persons)
        print u"剩余的没有连接的点个数: %d" % count
        if count == 0:
            break
        num = randint(0, count)
        current_person = self.unconnected_persons[num]
        return self.generate_dfs(current_person)
    return True

def mark_neighbor_to_no(self, current_person):
    """dfs 生成迷宫的一部分
    
    选择当前点的一个邻居来充当当前点
    """
    neighbor_pid = current_person.get_random_unconnected_neighbor_pid()
    if neighbor_pid != False:
        # 随机选择一个邻格
        neighbor = Person.get_person_by_pid(neighbor_pid)

        # 将当前格入栈
        self.visited_stack.append(current_person)

        # 拆墙
        Maze.crash_wall(current_person, neighbor)   # 把墙销毁
        pygame.display.update()
        
        # 标记已经访问过的点
        self.connected_persons.append(neighbor)
        self.unconnected_persons.remove(neighbor)
        neighbor.is_connected = True    # 标记邻格
        
        # 将邻格设为当前格
        current_person = neighbor
        return self.mark_neighbor_to_no(current_person)
    
    # 当前格已经没有未被标记的邻格了
    return True

```

#### 演示gif

![dfs生成迷宫演示](http://7viixf.com1.z0.glb.clouddn.com/algorithm/generate_maze_dfs.gif)


## 迷宫破解

### 使用深度优先算法破解迷宫

#### 算法过程（貌似下面这个思路有点不同寻常，虽然也可以）

- 创建 一个**栈**保存曾经走过的点：*dfs\_visited\_pointes\_stack*
- 将 **起点** **标记**为 **当前格**

1. 当 **当前格** 有可以走通的邻格 （四邻格模式）
    1. 标记 **当前格** 已经走过
    1. 选择其中一个可以走通的邻格
    2. 如果邻格是目标点，退出算法，否则往下
    3. 将 **当前格** 入栈
    4. 将邻格设为 **当前格**, 循环

2. （**当前格** 已经没有未被 **标记** 邻格了），判断栈是否为空，如果不为空
    1. 栈顶得格子出栈，并让它成为**当前格**
    2. 跳到上面的循环

3. 算法结束


#### 关键算法代码

```python

def hacking_dfs(self, current_person, goal_person):
    self.dfs_maze_path.append(current_person)

    current_person.is_walked = True
    current_person.set_tried(self.screen)
    # pygame.display.update()

    # print "walked person: %d, walked stack: %d" % (len(self.walked_persons),
    #         len(self.walked_persons))
    neighbor_pid = current_person.get_walkable_neighbor_pid(current_person)
    # print "walking: ", neighbor_pid

    if current_person.pid == goal_person.pid:
        notify('hacking succeed !')
        return True

    if neighbor_pid == False:
        if len(self.walked_stack) > 0:
            self.dfs_maze_path = list(self.walked_stack)
            
            current_person = self.walked_stack.pop()
            return self.hacking_dfs(current_person, goal_person)

        notify('hacking failed !')
        return False
    
    neighbor = Person.get_person_by_pid(neighbor_pid)

    self.walked_stack.append(current_person)
    self.walked_persons.append(current_person)

    current_person = neighbor
    return self.hacking_dfs(neighbor, goal_person)
```


### 使用 A\* 算法 更快的 破解迷宫

> 广度优先算法：？

> 迪杰斯特拉算法: 来自维基百科的gif解释：![迪杰斯特拉](http://7viixf.com1.z0.glb.clouddn.com/algorithm/Dijkstra_Animation.gif)

> A\* ：？

广度优先 -> 地接斯特拉 -> A star, 三者可以说有个递进的关系在

#### 算法过程

> 启发式搜索：？

- 自定义一个启发式函数，估算当前点到目标点的代价。（在迷宫这种特定的环境下，常用的启发式函数就是计算当前点到终点的距离：abs(x-goal_x) + abs(y-goal_y)）

- 创建一个 **队列** 保存曾经走过的点: *astar\_visited\_pointes\_queue*
- 创建一个数组保存每一点到起点的 **距离**: *current\_distance*，初始化为无穷大

- 将 **起点** 放入队列, 设置它到起点的距离为0

1. 当 **队列不为空** 的时候
    1. 从队列pop一个元素出来，将它标记为 **当前点**
    2. 如果当前点就是目标点，算法结束
    3. 计算 **当前点** 的每个邻居 **各自** 到起点的距离，使用启发式函数估算它们 **各自** 到目标点的距离, 相加得到 **各自的** 总距离。对比这个距离与之前保存的距离，如果比之前的距离小，那么用现在的距离更新之前保存的距离值。
    4. 把它们 **放入队列** 中，对 **队列进行升序排序**

#### 关键算法代码

```python
def hacking_astar(self, goal_person):
    while len(self.astar_walked_queue) > 0:
        # 因为后面的顺序是从大到小
        current_person = self.astar_walked_queue.popleft()
        print "排序之后选择了：", current_person.calculate_total_distance(goal_person)

        current_person.set_tried(self.screen)
        pygame.display.update()

        if current_person.pid == goal_person.pid:
            notify("Hacking succeed !")
            return True

        current_dis = current_person.astar_distance
        for neighbor_pid in current_person.neighbor_pids:
            neighbor = Person.get_person_by_pid(neighbor_pid)

            if not Maze.has_wall_between(current_person, neighbor):
                if neighbor.astar_distance == None:
                    neighbor.astar_distance = 1 + current_dis   # 1 如果不同的话，就是不同权重
                    neighbor.astar_came_from = current_person
                    self.astar_walked_queue.append(neighbor)
                else:
                    neighbor.astar_distance = neighbor.astar_distance 

                    # 在这里没有判断相等的情况
                    # 相等的话说明可以有两条道路走，我们只选择其中一条。
                    if not (1 + current_dis) > neighbor.astar_distance:
                        neighbor.astar_distance = 1 + current_dis
                        neighbor.astar_came_from = current_person
   
        print "排序中... "
        # 对队列中的元素进行从小到大的排序（这里也可以用sorted来排序）
        tmp_list = list()   # 在这中迷宫中，queue中元素不会很多
        while len(self.astar_walked_queue) > 0:
            tmp_person = self.astar_walked_queue.pop()
            tmp_dis = tmp_person.calculate_total_distance(goal_person)
            
            if len(tmp_list) > 0:
                last_person = tmp_list[-1]
                if tmp_person.calculate_total_distance(goal_person) >= \
                        last_person.calculate_total_distance(goal_person):
                    tmp_list.append(tmp_person)
                    continue

                for i, person in enumerate(tmp_list):
                    if tmp_dis < person.calculate_total_distance(goal_person):
                        tmp_list.insert(i, tmp_person)
                        break
            else:
                tmp_list.append(tmp_person)
        
        self.astar_walked_queue = deque(tmp_list)   # deque是python中的一个高效率的队列类
        # sorted(self.astar_walked_queue, key=lambda person:
        #         person.calculate_total_distance(goal_person))

        print "排序完毕... "

    notify('Hacking failed !')
    return False

```

#### 演示gif

![astar演示](http://7viixf.com1.z0.glb.clouddn.com/algorithm/hack_maze_astar.gif)



附带遇到的一些问题
----------------------


##### 一个类的什么样的成员或者变量应该设为私有，什么样的变量设为公有？

参考: <http://programmers.stackexchange.com/questions/143736/why-do-we-need-private-variables>

- 大概的一个总结：这些变量默认都应该设置为私有的，只有必须公开的才设为公有成员。
- 感觉这东西应该有一个比较官方的说法才对。


##### GUI中按钮等元素的Hover等事件是怎样从“底层”实现的？

** 想法 **

从编写 opengl 和 pygame 来看，一些比较“底层”的函数调用可以帮我们得到鼠标当前的位置。也可以对一些鼠标的移动、点击事件进行处理。
所以要实现 hover 这个事件响应：在每次鼠标事件中判断鼠标当前点是否在一个按钮的范围内.

##### 是创建多个对象好，还是使用多个属性数组来描述对象好？
先记录下这个问题


