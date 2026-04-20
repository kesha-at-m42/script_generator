extends SequenceEvent

func trigger():
	var lines = get_number_lines()
	clear_selected()
	for line in lines:
		use_highlight_tool(line.bar._parts[line.bar._parts.size()-1])
		await delay(1)
	for line in lines:
		use_highlight_tool(line.bar._parts[line.bar._parts.size()-1], false)
	
	use_select_tool_line(lines[2])
