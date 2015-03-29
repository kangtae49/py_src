SEP_IN=','
IDX_A = 1
IDX_B = 2
FUNC_LIST = (
	'f1',
	'f2',
	'write_row',
)
def start_job():
	pass

def end_job():
	pass


def get_line(input):
	filename = input
	filename = filename.replace('file://', '')
	with open(filename) as f:
		for line in f:
			yield line

def get_out_files(input):
	filename = '%s.out' % input
	return [filename]

def f1():
	print 'f1'

def f2():
	print 'f2'

def write_row():
	write('%s\n' % ','.join(c))

