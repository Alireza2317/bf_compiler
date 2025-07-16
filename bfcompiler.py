import sys

TAPE_MAXLEN = 10_000

class BFCompiler:
	def	__init__(self) -> None:
		self.set_code()
		self.init_tape()

		#self.code_end_indices: list[int] = []
		#self.code_start_indices: list[int] = []

		self.code_pieces: list[str] = []

	def init_tape(self) -> None:
		self.tape: list[int] = []

		for _ in range(TAPE_MAXLEN):
			self.tape.append(0)

		self.head: int = 0

	def set_code(self) -> None:
		raw: str = self._read_file()
		self.code: str = self._strip_code(raw)

		self.code_index: int = 0

	def _read_file(self) -> str:
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

	def _strip_code(self, raw_code: str) -> str:
		code: str = ''
		for char in raw_code:
			if char in '[<+-.,>]':
				code += char

		return code

	def _find_end_bracket(self, code: str, current_index: int) -> int:
		if code[current_index] != '[':
			raise ValueError('Loop does not start here!')

		current_index += 1

		openings_count: int = 0
		while current_index < len(code):
			if code[current_index] == '[':
				openings_count += 1
			elif code[current_index] == ']':
				if openings_count == 0:
					return current_index
				openings_count -= 1

			current_index += 1

		raise SyntaxError('Unbalanced Brackets!')

	def add_code_loop(self) -> None:
		pass

	@property
	def current_code_char(self) -> str:
		return self.code[self.code_index]

	@property
	def current_cell(self) -> int:
		return self.tape[self.head]

	def run(self, code: str | None = None) -> None:
		if code is None:
			code = self.code

		code_index: int = 0

		while code_index < len(code):
			match code[code_index]:
				case '[':
					...
				case ']':
					...

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

			self.code_index += 1


if __name__ == '__main__':
	compiler = BFCompiler()


	compiler.run()