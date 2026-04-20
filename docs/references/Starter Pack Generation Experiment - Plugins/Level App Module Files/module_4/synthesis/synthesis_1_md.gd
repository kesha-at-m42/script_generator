extends SequenceEvent

func trigger():
	var parts = get_num_line_intervals()
	for part in parts:
		use_highlight_tool(part, true)
