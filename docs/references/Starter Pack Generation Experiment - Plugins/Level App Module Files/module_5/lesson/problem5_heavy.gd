extends SequenceEvent

func trigger():
	clear_number_line_ticks(get_number_line())
	use_place_tool(get_num_line(0), 1, 3)
	await delay(1)
	use_place_tool(get_num_line(0), 2, 3)
