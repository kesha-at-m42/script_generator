extends SequenceEvent

func trigger() -> void:
	var line = get_number_line()
	var curr = 1
	for part in line.bar._parts:
		use_highlight_tool(part, true)
		use_write_tool(part, var_to_str(curr))
		curr+=1
	use_choice_tool([1])
