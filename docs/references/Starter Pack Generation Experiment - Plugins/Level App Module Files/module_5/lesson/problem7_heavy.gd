extends SequenceEvent

func trigger():
	var number_line = get_number_line()
	number_line.arrow_added.emit(0,3)
	await delay(1.5)
	use_paint_tool(number_line._ticks[3])
