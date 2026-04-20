extends SequenceEvent

func trigger():
	var number_line = get_number_line(1)
	clear_number_line_shaded_ticks(number_line)
	number_line.arrow_added.emit(0,1)
	await delay(3)
	use_paint_tool(number_line._ticks[1])
