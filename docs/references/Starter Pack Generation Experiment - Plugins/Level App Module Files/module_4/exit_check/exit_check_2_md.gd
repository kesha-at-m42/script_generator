extends SequenceEvent

func trigger() -> void:
	var frac_bar = get_number_line().bar
	use_highlight_tool(frac_bar._parts[0], true)
	use_highlight_tool(frac_bar._parts[1], true)
