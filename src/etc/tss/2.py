

def solution(seconds):

    if seconds % 20 != 0 and seconds > 130:
        seconds -= 130
        choco_count = 1
    else:
        choco_count = 0

    cola_count = min(seconds // 300, 10)
    seconds -= 300 * cola_count

    snack_count = min(seconds // 120, 20)
    seconds -= 120 * snack_count

    jelle_count = min(seconds // 20, 30)
    seconds -= 20 * jelle_count

    while choco_count < 30 and snack_count > 2 and jelle_count > 1:
        choco_count += 2
        snack_count -= 2
        jelle_count -= 1

    while cola_count < 10 and choco_count > 2 and jelle_count > 2:
        cola_count += 1
        choco_count -= 2
        jelle_count -= 2

    print(cola_count,choco_count,snack_count, jelle_count)
    return cola_count + snack_count + jelle_count + choco_count

if __name__ == '__main__':
    print(solution(330))

"""
    choco_count = min(seconds // 130, 30)
    seconds -= 130 * choco_count

    while (seconds % 120 != 0 and seconds % 20 != 0) \
            and choco_count < 30 and cola_count > 0:
        seconds += 170
        cola_count -= 1
        choco_count += 1
        
    
    while seconds % 20 != 0 and snack_count < 20 and choco_count > 0:
        seconds += 10
        choco_count -= 1
        snack_count += 1
"""