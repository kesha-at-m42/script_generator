extends SequenceEvent

func trigger() -> void:
	var line = get_number_line()
	clear_number_line_tick_highlights(line)
	for i in range(0,3):
		use_highlight_tool(line.bar._parts[i], true)
		await delay(0.5)
		use_highlight_tool(line.bar._parts[i], false)
	use_highlight_tool(line._ticks[3], true)
