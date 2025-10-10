counter_passed = 0
counter_failed = 0
total_scores = 0
total_passed = 0
total_failed = 0

counter_scores = int(input("Ingrese la cantidad de notas: "))

for i in range(counter_scores):
    new_score = int(input(f'Ingrese nota {i+1}: '))
    total_scores += new_score
    if (new_score >= 70):
        counter_passed += 1
        total_passed += new_score
    else:
        counter_failed += 1
        total_failed += new_score

print(f'Su total de notas aprobadas es {counter_passed}')
print(f'Su total de notas desaprobadas es {counter_failed}')
print (f' Su promedio total es {total_scores/counter_scores}')
if (total_passed != 0):
    print (f' Su promedio de aprobadas es {total_passed/counter_passed}')
if (total_failed != 0):
    print (f' Su promedio de desaprobadas es {total_failed/counter_failed}')