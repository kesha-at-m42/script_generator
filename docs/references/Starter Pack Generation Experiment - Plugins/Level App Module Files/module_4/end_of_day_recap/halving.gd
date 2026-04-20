extends SequenceEvent

func trigger() -> void:
	var line = get_number_line()
	use_highlight_tool(line._ticks[4], true)
	await delay(0.5)
	use_highlight_tool(line._ticks[4], false)
	use_highlight_tool(line._ticks[2], true)
	use_highlight_tool(line._ticks[6], true)
	await delay(0.5)
	use_highlight_tool(line._ticks[2], false)
	use_highlight_tool(line._ticks[6], false)
	use_highlight_tool(line._ticks[1], true)
	use_highlight_tool(line._ticks[3], true)
	use_highlight_tool(line._ticks[5], true)
	use_highlight_tool(line._ticks[7], true)
