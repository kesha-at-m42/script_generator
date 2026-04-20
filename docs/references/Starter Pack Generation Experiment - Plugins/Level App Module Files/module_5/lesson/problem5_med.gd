extends SequenceEvent

func trigger():
	var number_line = get_number_line()
	use_cut_hint_tool(number_line.bar, 1, 3)
	await delay(1)
	use_cut_hint_tool(number_line.bar, 2, 3)
