from itertools import islice


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей',  'Дмитрий', 'Борис', 'Елена', 'Владимир', 'Антон', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
if len(klasses) < len(tutors):
    [klasses.append('None') for _ in range(len(tutors) - len(klasses))]
tutor_klass_gen = ((tutor, klass) for tutor, klass in zip(tutors, klasses))
# print(*tutor_klass_gen)
# print(next(tutor_klass_gen))
# print(next(tutor_klass_gen))
print(*islice(tutor_klass_gen, 100))

