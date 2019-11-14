from collections import namedtuple

Technology = namedtuple('Technology', ['name', 'courses'])
Course = namedtuple('Course', ['name', 'participants'])

technologies = {}

while True:
	line = input()
	if line == 'end':
		break

	technology_name, course_tokens = line.split(' - ')
	courses = course_tokens.split(', ')
	course_participants = [(tokens[0], int(tokens[1])) for tokens in [token.split(':') for token in courses]]

	technologies.setdefault(technology_name, {})

	for course_name, participants in course_participants:
		technologies[technology_name].setdefault(course_name, 0)
		technologies[technology_name][course_name] += participants

technology_tuples = \
	[Technology(name=key, courses=list([Course(name=item[0], participants=item[1]) for item in value.items()])) for
	 key, value in technologies.items()]

[list.sort(tech.courses, key=lambda c: c.participants, reverse=True) for tech in technology_tuples]
list.sort(technology_tuples, key=lambda t: sum(c.participants for c in t.courses), reverse=True)

most_popular_tech = technology_tuples[0]
most_popular_participants = sum(c.participants for c in most_popular_tech.courses)
print(f'Most popular: {most_popular_tech.name} ({most_popular_participants} participants)')

least_popular_tech = technology_tuples[-1]
least_popular_participants = sum(c.participants for c in least_popular_tech.courses)
print(f'Least popular: {least_popular_tech.name} ({least_popular_participants} participants)')

for tech in technology_tuples:
	tech_total_participants = sum(c.participants for c in tech.courses)
	print(f'{tech.name} ({tech_total_participants} participants):')
	for course in tech.courses:
		print(f'--{course.name} -> {course.participants}')