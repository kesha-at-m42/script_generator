extends SequenceEvent

func trigger() -> void:
	var line = get_number_line()
	clear_number_line_tick_highlights(line)
	for i in range(1,5):
		use_highlight_tool(line._ticks[i], true)
		await delay(0.25)
		use_highlight_tool(line._ticks[i], false)
	use_highlight_tool(line._ticks[5], true)
