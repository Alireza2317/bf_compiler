import sys
from collections import deque
TAPE_MAXLEN = 10_000

class BFCompiler:
	def	__init__(self) -> None:
		self.set_code()
		self.init_tape()
		self.head: int = 0
		self.code_end_indices: list[int] = []
		self.code_start_indices: list[int] = []
		self.abs_code_index: int = 0

	def init_tape(self) -> None:
		self.tape: deque = deque(maxlen=TAPE_MAXLEN)

		for _ in range(TAPE_MAXLEN):
			self.tape.append(0)

	def set_code(self) -> None:
		raw: str = self.read_file()
		self.code: str = self.strip_code(raw)

	def read_file(self) -> str:
		try:
			#code_path: str = sys.argv[1]
			code_path: str = 'test.bf'

			with open(code_path, 'r') as file:
				raw_code: str = file.read()
		except IndexError:
			print('Please enter a filename!')
			exit()
		except FileNotFoundError:
			print('File does not exist!')
			exit()

		return raw_code

	def strip_code(self, raw_code: str) -> str:
		code: str = ''
		for char in raw_code:
			if char in '[<+-.,>]':
				code += char

		return code

	def _find_end_bracket(self, current_index: int, code: str) -> int:
		openings_count: int = 0
		for i in range(current_index+1, len(code)):
			if code[i] == '[':
				openings_count += 1
			elif code[i] == ']':
				if openings_count == 0:
					return i
				openings_count -= 1

		raise SyntaxError('Unbalanced Brackets!')

	@property
	def current_cell(self):
		return self.tape[self.head]

	def run(self, code: str | None = None):
		if code is None:
			code = self.code

		code_index: int = 0
		while code_index < len(code):
			match code[code_index]:
				case '[':
					self.code_start_indices.append(code_index)
					end_i: int = self._find_end_bracket(code_index, code)
					self.code_end_indices.append(end_i)
					self.run(code[code_index+1:end_i+1])
				case ']':

					if self.current_cell != 0:
						code_index = self.code_start_indices[-1] + 1

					else: # loop ends
						self.code_start_indices.pop()
						code_index = self.code_end_indices.pop()

				case '>':
					self.head += 1
				case '<':
					self.head -= 1
				case '+':
					self.tape[self.head] += 1
				case '-':
					self.tape[self.head] -= 1

				case '.':
					print(chr(self.current_cell), end='')

				case ',':
					self.tape[self.head] = ord(input()[0])

			code_index += 1


if __name__ == '__main__':
	compiler = BFCompiler()
	compiler.run()