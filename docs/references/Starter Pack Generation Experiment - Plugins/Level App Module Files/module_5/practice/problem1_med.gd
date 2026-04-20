extends SequenceEvent

func trigger():
	var number_line = get_number_line()
	clear_number_line_ticks(number_line)
	use_cut_hint_tool(number_line.bar, 1, 2)
