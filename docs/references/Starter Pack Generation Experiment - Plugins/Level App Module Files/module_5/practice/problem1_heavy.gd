extends SequenceEvent

func trigger():
	var number_line = get_number_line()
	clear_number_line_ticks(number_line)
	use_place_tick_tool(number_line, 2)
