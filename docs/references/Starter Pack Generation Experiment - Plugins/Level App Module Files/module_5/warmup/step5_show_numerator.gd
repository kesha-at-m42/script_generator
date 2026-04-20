extends SequenceEvent

func trigger():
	var number_line = get_number_line(1)
	use_highlight_tool(number_line._ticks[1], true, 3)
