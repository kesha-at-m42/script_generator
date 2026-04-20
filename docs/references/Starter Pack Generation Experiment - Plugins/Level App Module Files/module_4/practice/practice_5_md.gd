extends SequenceEvent

func trigger() -> void:
	var line = get_number_line()
	use_cut_hint_tool(line.bar, 1, 2)
	await delay(0.75)
	use_cut_hint_tool(line.bar, 1, 4)
	use_cut_hint_tool(line.bar, 3, 4)
	await delay(0.75)
	use_cut_hint_tool(line.bar, 1, 8)
	use_cut_hint_tool(line.bar, 3, 8)
	use_cut_hint_tool(line.bar, 5, 8)
	use_cut_hint_tool(line.bar, 7, 8)
