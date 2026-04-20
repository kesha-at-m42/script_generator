extends SequenceEvent

func trigger():
	var number_line = get_number_line()
	var bar = number_line.bar
	for i in range(bar._parts.size()-1):
		var part = bar._parts[i]
		use_highlight_tool(part, true)
		await delay(0.5)
		use_highlight_tool(part, false)
	use_choice_tool([1])
