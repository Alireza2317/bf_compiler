import sys
from collections import deque
TAPE_MAXLEN = 10_000


class BFFileReader:
	@classmethod
	def read_file(cls) -> str:
		try:
			code_path: str = sys.argv[-1]

			with open(code_path, 'r') as file:
				raw_code: str = file.read()
		except IndexError:
			print('Please enter a filename!')
			exit()
		except FileNotFoundError:
			print('File does not exist!')
			exit()

		return raw_code

	@classmethod
	def strip_code(cls, raw_code: str) -> str:
		code: str = ''
		for char in raw_code:
			if char in '[<+-.,>]':
				code += char

		return code

	@classmethod
	def get_code(cls) -> str:
		raw_code: str = cls.read_file()
		return cls.strip_code(raw_code)


class BFCompiler:
	def	__init__(self) -> None:
		self.set_code()
		self.init_tape()

		self.head: int = 0

		self.saved_input: deque[str] = deque()

	def init_tape(self) -> None:
		self.tape: list[int] = [
			0 for _ in range(TAPE_MAXLEN)
		]

	def set_code(self) -> None:
		self.code = BFFileReader.get_code()

	def _find_end_bracket(self, code: str, index: int) -> int:
		if code[index] != '[':
			raise ValueError('Loop does not start here!')

		index += 1

		openings_count: int = 0
		while index < len(code):
			if code[index] == '[':
				openings_count += 1
			elif code[index] == ']':
				if openings_count == 0:
					return index
				openings_count -= 1

			index += 1

		raise SyntaxError('Unbalanced Brackets!')

	@property
	def current_cell(self) -> int:
		return self.tape[self.head]

	def run_simple_operation(self, code_char: str) -> None:
		match code_char:
			case '>':
				self.head += 1
				if self.head >= TAPE_MAXLEN:
					raise IndexError('Tape head went beyond maximum!')
			case '<':
				self.head -= 1
				if self.head < 0:
					raise IndexError('Tape head went beyond maximum!')
			case '+':
				self.tape[self.head] = (self.current_cell + 1) % 256
			case '-':
				self.tape[self.head] = (self.current_cell - 1) % 256
			case '.':
				print(chr(self.current_cell), end='')
			case ',':
				if not self.saved_input:
					input_str: str = input()

					self.saved_input.extend(input_str)
					self.saved_input.append('\n')

				self.tape[self.head] = ord(self.saved_input.popleft())

	def run(self, code: str | None = None) -> None:
		if code is None:
			code = self.code

		i: int = 0
		while i < len(code):
			if code[i] not in '[]':
				self.run_simple_operation(code[i])
			elif code[i] == '[':
				end_i: int = self._find_end_bracket(code, i)
				new_code: str = code[i+1:end_i+1]
				if self.current_cell != 0:
					self.run(new_code)
				i = end_i
			elif code[i] == ']':
				if self.current_cell != 0: # loop continues
					i = 0
					continue
				# loop ends

			i+=1


if __name__ == '__main__':
	compiler = BFCompiler()
	compiler.run()