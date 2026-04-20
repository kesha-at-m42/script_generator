extends SequenceEvent

func trigger() -> void:
	var lines = get_number_lines()
	clear_selected()
	for line in lines:
		for part in line.bar._parts:
			use_highlight_tool(part, true)
			await delay(0.5)
			use_highlight_tool(part, false)
		await delay(0.5)
	use_select_tool(lines[1])
