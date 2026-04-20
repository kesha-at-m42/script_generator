extends SequenceEvent

func trigger():
	var number_line = get_number_line()
	for part in number_line.bar._parts:
		use_highlight_tool(part, true)
		await delay(0.5)
		use_highlight_tool(part, false)
