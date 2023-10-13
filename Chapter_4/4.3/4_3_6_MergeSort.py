def merge_sort(*args):
    args = args[0]
    if len(args) == 1:
        return args
    middle = len(args) // 2
    left = merge_sort(args[:middle])
    rigth = merge_sort(args[middle:])
    end = []
    i = j = 0
    while i < len(left) and j < len(rigth):
        if left[i] < rigth[j]:
            end.append(left[i])
            i += 1
        else:
            end.append(rigth[j])
            j += 1
    if i < len(left):
        end += left[i:]
    if j < len(rigth):
        end += rigth[j:]
    return end



result = merge_sort([3, 2, 1])
print(result)