def find_common_free_slots_matrix(schedules, days_exam):
    """
    Retorna os horários vagos comuns para os dias especificados.

    :param @schedules: Dicionário com os horários dos cursos.
    :param @days_exam: Lista de índices representando os dias a serem considerados (0 - Seg, 1 - Ter, etc.).
    :return: Matriz com horários vagos comuns para os dias especificados.
    """
    common_free_slots = [[1] * 8 for _ in days_exam]

    for timetable in schedules.values():
        for i, day_idx in enumerate(days_exam):
            for slot_idx, slot in enumerate(timetable[day_idx]):
                if slot != 0:
                    common_free_slots[i][slot_idx] = 0 # ocupado

    return common_free_slots


schedules = {
    "Agro": [
        [4, 4, 1, 1, 0, 5, 2, 2],
        [1, 10, 2, 5, 12, 12, 0, 0],
        [6, 13, 13, 13, 0, 0, 0, 0],
        [14, 14, 3, 9, 11, 80, 0, 0],
        [6, 3, 8, 8, 7, 7, 0, 0],
    ],
    "Informática": [
        [5, 9, 16, 16, 2, 2, 17, 17],
        [10, 3, 1, 1, 4, 4, 11, 0],
        [5, 11, 6, 1, 0, 0, 0, 0],
        [80, 2, 8, 8, 6, 3, 0, 0],
        [7, 7, 19, 19, 20, 20, 20, 20],
    ],
    "Alimentos": [
        [4, 4, 5, 10, 1, 21, 2, 2],
        [22, 22, 5, 6, 1, 1, 0, 0],
        [23, 23, 24, 24, 0, 0, 0, 0],
        [11, 9, 2, 0, 7, 7, 0, 0],
        [26, 26, 81, 6, 3, 3, 8, 8],
    ],
}

students_recovery = {
    "Aluno1": [1, 2, 3, 5],
    "Aluno2": [2, 6],
    "Aluno3": [2],
    "Aluno4": [1, 7, 17, 20],
}

days_exam = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
result = find_common_free_slots_matrix(schedules, days_exam)

day_names = ["seg", "ter", "qua", "qui", "sex"]
for i, free_slots in enumerate(result):
    print(f"{day_names[days_exam[i]]}: {' '.join(map(str, free_slots))}")

recovery_disciplines = set() # set nao aceita valores duplicados

for disciplines in students_recovery.values():
    recovery_disciplines.update(disciplines)

recovery_disciplines = sorted(recovery_disciplines)

print(f"Disciplinas de recuperação: {', '.join(map(str, recovery_disciplines))}")

