from datetime import timedelta
import re


class Lecture:
	def __init__(self, lecture, course, trainer, duration, server):
		self.lecture = lecture
		self.course = course
		self.trainer = trainer
		self.duration = duration
		self.server = server

	def get_link(self):
		link_template = 'https://streamcdn{}.softuni.bg/course={}&lecture={}&trainer={}'
		result = link_template.format(self.server, self.course, self.lecture, self.trainer)
		return result


def format_timedelta(_timedelta):
	seconds = _timedelta.total_seconds()
	hours = seconds // 3600
	minutes = (seconds % 3600) // 60
	seconds = seconds % 60
	result = f'{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}'
	return result


def parse_duration(duration_str):
	_match = re.match(r'(?:(?P<hours>\d+)h)?(?P<minutes>\d+)m', duration_str)
	groups = _match.groupdict()

	hours, minutes = int(groups['hours']), int(groups['minutes'])

	duration = timedelta(hours=hours, minutes=minutes)

	return duration


lectures = []

MAX_SERVER_DURATION = timedelta(hours=10)
current_server_duration = timedelta()
current_server_index = 1

line = input()
while not line.startswith('scrape'):
	tokens = dict((kvp.split(':') for kvp in line.split(';')))

	tokens['duration'] = parse_duration(tokens['duration'])

	if current_server_duration + tokens['duration'] > MAX_SERVER_DURATION:
		current_server_index += 1
		current_server_duration = timedelta()

	tokens['server'] = current_server_index

	lecture = Lecture(**tokens)
	current_server_duration += lecture.duration
	lectures.append(lecture)

	line = input()

_, scrape_type, value = line.split(' ')

filtered_lectures = None
if scrape_type == 'course':
	filtered_lectures = [lecture for lecture in lectures if lecture.course == value]
elif scrape_type == 'trainer':
	filtered_lectures = [lecture for lecture in lectures if lecture.trainer == value]

links = [lecture.get_link() for lecture in filtered_lectures]
total_duration = sum([lecture.duration for lecture in filtered_lectures], timedelta())
print(*links, sep='\n')

print(f'total duration: {format_timedelta(total_duration)}')
