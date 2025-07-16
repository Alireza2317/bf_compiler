+ put first cell to 1
copies the current cell to the next cell
and puts curser on next cell
ruins the right cell of this new cell
should be 0 at the start
[>+>+<<-]>>[<<+>>-]< copy it

>
+ 2nd cell is 2
[>+>+<<-]>>[<<+>>-]< copy it

>>(+++++++++++) the loop counter

[ start main loop
	cursor is on the loop ctr now/ two cells from last value
	[>>+<<-] first relocate the ctr two cells over to right
	<

	these lines will add the previous two numbers to current cell
	<[>+<-]>
	<<<[>>>+<<<-]>>>

	[>+>+<<-]>>[<<+>>-]< copy it

	now the calculation is done but the copies of the previus number is gone
	so we go and create its copy again
	first make sure its 2next cell is empty
	<[-]>

	<<< move to the cell that should be copied
	[>+>+<<-]>>[<<+>>-]< copy it

	now the copy of the last number is gone
	actually the original cell is 0 and its copy is there
	so we basically should do a reverse copy
	>> move the the last cell
	[<+>-]< move its value to the cell before
	[>+>+<<-]>>[<<+>>-]< copy it

	first time i should go back 5 cells back
	second time 7 cells
	third time 9 cells
	>>
	- decrement loop ctr
]
#