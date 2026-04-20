extends SequenceEvent

func trigger():
	var number_line = get_number_line()
	use_paint_tool(number_line._ticks[4])
