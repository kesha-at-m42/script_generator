extends SequenceEvent

func trigger() -> void:
	var line = get_number_line()
	clear_number_line_tick_highlights(line)
	use_highlight_tool(line._ticks[4], true)
	await delay(1)
	use_highlight_tool(line._ticks[2], true)
	use_highlight_tool(line._ticks[4], false)
	await delay(1)
	use_highlight_tool(line._ticks[1], true)
	use_highlight_tool(line._ticks[2], false)
	await delay(1)
	for i in range(1,4):
		use_highlight_tool(line._ticks[i], true)
		await delay(0.25)
		use_highlight_tool(line._ticks[i], false)
