def highest_number(site_nmbers):
    if len(site_nmbers) == 0:
        return "can't work with empty dataset"
    for number in site_nmbers:
        if not isinstance(number, (int, float)):
            return "All elements must be numbers"
    max_value = max(site_nmbers)
    return site_nmbers.index(max_value)

def avg_check(numbers, cap):
    if len(numbers) < 2:
        return "can't average less than two things dipshit"
    for number in numbers:
        if not isinstance(number, (int, float)):
            return "All elements must be numbers"
    avg = sum(numbers) / len(numbers)
    if avg > cap:
        return f"limit {avg} exceeds cap {cap}"
    return f"Average {avg} is within cap {cap}"


def max_count(numbers, cap):
    if len(numbers) < 2:
        return "too low an input"
    for number in numbers:
        if not isinstance(number, (int, float)):
            return "must be numbers also"
        




def drug_anomaly(data):
    flagged = []
    for i, medicine in enumerate(data):
        for j in range(len(medicine) - 1):
            if medicine[j] == 0 and medicine[j + 1] == 0:
                flagged.append(i)
                break
    return flagged










# 1
test = [300, 450, 120, 800, 540, 760, 310, 900, 500, 620]
print(highest_number(test))
