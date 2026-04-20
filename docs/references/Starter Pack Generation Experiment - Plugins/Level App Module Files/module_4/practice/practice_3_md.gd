extends SequenceEvent

func trigger() -> void:
	var lines = get_number_lines()
	use_highlight_tool(lines[0].bar._parts[0], true)
	use_highlight_tool(lines[1].bar._parts[0], true)
