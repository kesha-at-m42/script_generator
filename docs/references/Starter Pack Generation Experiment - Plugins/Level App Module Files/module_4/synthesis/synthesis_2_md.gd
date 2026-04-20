extends SequenceEvent

func trigger():
	var intervals = get_num_line_intervals()
	for part in intervals:
		use_highlight_tool(part, true)
		await  delay(0.5)
		use_highlight_tool(part, false)
