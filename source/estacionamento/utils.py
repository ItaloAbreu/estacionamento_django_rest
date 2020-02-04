def diff_of_times(date1, date2):
	from datetime import timedelta, datetime
	diff = (date1 - date2)

	seconds = diff.seconds
	minutes = round(seconds/60, 2)
	hours = round(minutes/60, 2)
	days = round(hours/24, 2)

	if days >= 1.0:
		return f'{days} days'
	elif hours >= 1.0:
		return f'{hours} hours'
	elif minutes >= 1.0:
		return f'{minutes} minutes'
	return f'{seconds} seconds'