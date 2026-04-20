extends SequenceEvent

func trigger():
	var number_line = get_number_line()
	clear_number_line_ticks(number_line)
	use_place_tick_tool(number_line, 4)
	await delay(1)
	use_place_tick_tool(number_line, 2)
	use_place_tick_tool(number_line, 6)
