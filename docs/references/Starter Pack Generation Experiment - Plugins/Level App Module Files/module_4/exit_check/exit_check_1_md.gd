extends SequenceEvent

func trigger() -> void:
	var lines = get_number_lines()
	clear_selected()
	await delay(0.5)
	for i in range(lines[1].bar._parts.size()):
		var part = lines[1].bar._parts[i]
		use_highlight_tool(part, true)
		use_write_tool(part, var_to_str(i+1))
		await delay(0.5)
		use_highlight_tool(part, false)
		use_write_tool(part, "")
