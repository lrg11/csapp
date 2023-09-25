adaboost是一种基于分类器（决策树桩）的集成学习方法，训练多个分类器来组合成一个强分类器
gbdt是基于决策树的集成学习方法，通过训练多个弱决策树来组合成一个强决策树，xgboost和lightgbm都是基于梯度提升决策树的集成学习方法，可看作gbdt的升级版实现​​
xgboost是对gbdt的优化改进
         目标函数中加入了正则项来控制模型复杂度，替代了剪枝。利用one-hot独热编码的特征稀疏性。支持列抽样。对损失函数进行了优化，gbdt只用到一阶导数，而xgboost同时用到一阶和二阶导数。
lightgbm是在xgboost基础上进一步改进
         内存需求更小，不同于xgboost的pre-sorted决策树算法，lightgbm使用基于histogram的决策树算法，xgboost需要用两倍数据大小的内存空间，一半用于数据（float32），一半是排序后的索引，而lightgbm不需要索引，且特征值只需要离散后值，一个字节搞定，内存需求是前者的1/8=1/2*1/4。
        计算速度快，数据分割上histogram更快，所有特征共享一张索引，还减少了计算分割点增益的次数
        通信代价小，histogram还可用于分布式计算。
        但是lightgbm的决策树算法不能找到很精确的分割点，牺牲一定精度换取速度，相当于自带正则化。
这些算法在决策树算法、时间复杂度、决策树生长策略、并行计算、优化目标、正则化和分布式计算等方面存在一些不同。他们之间的选择取决于数据集大小、性能需求。adaboost适用于简单问题，xgboost和lightgbm适用于更复杂和大规模的数据集，gbdt通常是中间选项。​



> Problem: [148. 排序链表](https://leetcode.cn/problems/sort-list/description/)

  [TOC]
  
  # 思路
  > 看到要求的时间复杂度是$O(nlogn)$, 想到归并排序，最简单做法就是把链表遍历一遍，存入数组，再调用归并排序（Python默认的sorted函数或者列表sort方法都是归并排序？），时间复杂度满足要求，但是空间复杂度是$O(n)$, 不是常数级。再看是链表，只能操作指针进行手动归并排序，可以假设函数已经实现排序功能，从中间截断，赋值为None的操作别忘了，链表前半部分递归调用自身，排好序；后半部分也是，递归调用，相对于二叉树的后序遍历，最后合并两个有序链表操作用$O(n)$时间，常数空间解决
  
  # 解题方法
  > 从中间断开，分成两个链表，递归调用链表前后两半部分，后序遍历，合并两个有序链表的部分放在最后面，最后返回合并后的链表头指针
  
  # 复杂度
  - 时间复杂度: 
  > $O(nlogn)$
  
  - 空间复杂度: 
  > $O(1)，只操作指针，没有额外数组空间开销
  


  # Code
  ```Python3 []
  
  # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #nums = []
        cur = head
        cnt = 0
        #slow = head
        while cur:
            cur = cur.next
            #slow = slow.next
            #nums.append(cur.val)
            cnt+=1
        if cnt <= 1:
            return head
        half = cnt // 2
        cur = head
        for i in range(half - 1):
            cur = cur.next
        after = cur.next
        cur.next = None
        headnew = self.sortList(head)
        afternew = self.sortList(after)
        curfrot = headnew
        curafter = afternew 
        res = None
        cur = None
        while curfrot and curafter:
            if curfrot.val > curafter.val:
                if res == None:
                    res = curafter
                    curafter =  curafter.next
                    cur = res

                else:
                    cur.next = curafter
                    cur = cur.next
                    curafter = curafter.next
            else:
                if res == None:
                    res = curfrot
                    cur = res
                    curfrot =  curfrot.next
                else:
                    cur.next = curfrot
                    cur = cur.next
                    curfrot = curfrot.next
        if curafter:
            cur.next = curafter
        if curfrot:
            cur.next = curfrot
        return res
        
        
  ```
  