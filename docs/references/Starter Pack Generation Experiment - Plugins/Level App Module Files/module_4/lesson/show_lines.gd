extends SequenceEvent

func trigger():
	var lines = get_number_lines()
	for line in lines:
		use_show_tool(line)
