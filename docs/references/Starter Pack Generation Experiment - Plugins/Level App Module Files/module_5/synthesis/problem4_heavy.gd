extends SequenceEvent

func trigger():
	use_highlight_tool(get_num_line_interval(1,2))
	await delay(1)
	use_choice_tool([1])
