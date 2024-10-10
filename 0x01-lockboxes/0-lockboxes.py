#!/usr/bin/python3
"""Combined Lockboxes Solution"""

def canUnlockAll(boxes):
    """Check if all boxes can be opened
    Args:
        boxes (list): List of lists containing the keys inside each box
    Returns:
        bool: True if all boxes can be opened, otherwise, False
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0] 

    while stack:
        current_box = stack.pop()

        # Traverse all the keys in the current box
        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True 
                stack.append(key)

    return all(visited)


def main():
    """Entry point"""
    boxes = [
        [1],
        [2],
        [3],
        [4],
        [] 
    ]
    print(canUnlockAll(boxes))

if __name__ == '__main__':
    main()
