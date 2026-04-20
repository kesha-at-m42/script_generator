extends SequenceEvent

func trigger():
	var number_lines = get_number_lines()
	for line in number_lines:
		clear_number_line_ticks(line)
	use_cut_hint_tool(number_lines[0].bar, 1, 3)
	await delay(0.25)
	use_cut_hint_tool(number_lines[0].bar, 2, 3)
	await delay(1)
	use_cut_hint_tool(number_lines[0].bar, 2, 3)
	use_place_tick_tool(number_lines[0], 4)
	await delay(1)
	use_cut_hint_tool(number_lines[1].bar, 1, 2)
	await delay(0.5)
	use_cut_hint_tool(number_lines[1].bar, 1, 4)
	await delay(0.25)
	use_cut_hint_tool(number_lines[1].bar, 3, 4)
	await delay(1)
	use_cut_hint_tool(number_lines[1].bar, 3, 4)
	use_place_tick_tool(number_lines[1], 6)
