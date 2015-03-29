#-*- coding: utf-8 -*-
import os
import sys
import functools

def job(input, code):
	out = {}
	ns = {}
	ns['input'] = input
	ns['out'] = out # use group by
	ofds = [] # out files

	exec(code, ns)
	SEP_IN = ns.get('SEP_IN', '')

	def _start_job():
		pass

	def _end_job():
		pass

	def _get_line(input):
		filename = input.strip()
		filename = filename.replace('file://', '')
		with open(filename) as f:
			for line in f:
				yield line

	def _get_out_files(input):
		filename = '%s.out' % input
		return [filename]

	start_job = ns.get('start_job', _start_job)
	end_job = ns.get('end_job', _end_job)
	get_line = ns.get('get_line', _get_line)
	get_out_files = ns.get('get_out_files', _get_out_files)

	func_names = ns.get('FUNC_LIST', ())
	func_list = [ns[func] for func in func_names]

	ofds = []
	try:
		for i, name in enumerate(get_out_files(input)):
			f = open(name, 'w')
			ofds.append(f)
			ns['write_%d' % i] = f.write
			if i == 0:
				ns['write'] = f.write

		start_job()
		for ri, line in enumerate(get_line(input)):
			try:
				if not line:
					continue
				line = line.strip()
				cols = line.split(SEP_IN)
				ns['ri'] = ri
				ns['c'] = cols
				for fi, func in enumerate(func_list):
					print 'func:', func_names[fi]
					func()

			except Exception as e:
				print 'line:', e

		end_job()
	finally:
		map(file.close, ofds)


def get_rule_code(filename):
	#compile(open(filename, "rb").read(), filename, 'exec')
	code = ''
	with open(filename, "rb") as f:
		code = compile(f.read(), filename, 'exec')
	return code


def main():
	rule_filename = 'p1_rule.py'
	code = get_rule_code(rule_filename)
	env = {}
	exec(code, env)


	def _get_output(input):
		output = '%s.out\n' % input
		return output
	get_output = env.get('get_output', _get_output)

	for l in sys.stdin:
		input = l.strip()
		sys.stderr.write('%s\n' % input)

		try:
			job(input, code)
		except Exception as e:
			print 'job:', e
		finally:
			output = get_output(input)
			sys.stdout.write(output)


if __name__ == '__main__':
	main()


