# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node and node.next:
            node.val = node.next.val
            node.next = node.next.next
            

# ヘルパー関数: リストを作成
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# ヘルパー関数: リストを配列に変換
def linked_list_to_array(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# テスト実行
if __name__ == "__main__":
    # 初期リスト作成
    values = [4, 5, 1, 9]
    head = create_linked_list(values)
    print(head.val)  # 4
    print(head.next.val)  # 5
    print(head.next.next.val)  # 1
    print(head.next.next.next.val)  # 9

    # 削除するノードの取得（値が5のノード）
    node_to_delete = head.next  # 5のノード

    # 削除処理
    sol = Solution()
    sol.deleteNode(node_to_delete)

    # 結果のリストを表示(動作確認のために必要なヘルパー)
    result = linked_list_to_array(head)
    print(result)  # [4, 1, 9]

    # テストケース
    assert result == [4, 1, 9], "Test Failed!"
    print("Test Passed!")
