extends SequenceEvent

func trigger() -> void:
	var lines = get_number_lines()
	use_highlight_tool(lines[0]._ticks[1], true)
	await delay(0.5)
	use_highlight_tool(lines[1].bar._parts[0], true)
	await delay(0.1)
	use_highlight_tool(lines[1].bar._parts[1], true)
