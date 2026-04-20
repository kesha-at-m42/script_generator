extends SequenceEvent

func trigger() -> void:
	var line = get_number_line()
	use_cut_hint_tool(line.bar, 1, 3)
	await delay(0.75)
	use_cut_hint_tool(line.bar, 2, 3)
