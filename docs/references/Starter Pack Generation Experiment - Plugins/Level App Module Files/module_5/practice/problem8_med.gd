extends SequenceEvent

func trigger():
	var number_line = get_number_line()
	clear_number_line_ticks(number_line)
	use_cut_hint_tool(number_line.bar, 1, 2)
	await delay(1)
	use_cut_hint_tool(number_line.bar, 1, 4)
	use_cut_hint_tool(number_line.bar, 3, 4)
	await delay(1)
	use_cut_hint_tool(number_line.bar, 1, 2)
	use_cut_hint_tool(number_line.bar, 1, 4)
	use_cut_hint_tool(number_line.bar, 3, 4)
	use_cut_hint_tool(number_line.bar, 1, 8)
	use_cut_hint_tool(number_line.bar, 3, 8)
	use_cut_hint_tool(number_line.bar, 5, 8)
	use_cut_hint_tool(number_line.bar, 7, 8)
